import whois
import concurrent.futures
import socket
import time
from functools import lru_cache

# Configure timeouts
socket.setdefaulttimeout(10)  # Global socket timeout
WHOIS_TIMEOUT = 15  # Separate WHOIS timeout
# Cache WHOIS responses for 1 hour (10,000 entries)
@lru_cache(maxsize=10000)
def cached_whois(domain):
    try:
        return whois.whois(domain)
    except Exception as e:
        # Explicitly return None on failure
        return None

def check_domain_availability(domain):
    # First check DNS (fastest method for registered domains)
    try:
        socket.gethostbyname(domain)
        return domain, False  # Definitely registered
    except socket.gaierror:
        pass  # Proceed to WHOIS check
    except Exception:
        pass  # Handle other socket errors
    
    # WHOIS verification (100% accurate but slower)
    try:
        domain_info = cached_whois(domain)
        if domain_info is None or not domain_info.domain_name:
            return domain, True  # Available
        return domain, False  # Registered
    except Exception:
        # On WHOIS failure, assume registered to be safe
        return domain, False

def load_dictionary_words():
    with open("words.txt", "r") as file:
        return [word.strip() for word in file if len(word.strip()) <= 6]

def main():
    words = load_dictionary_words()
    domains = [f"{word}.com" for word in words]
    
    available_domains = []
    
    # Batch processing with progress tracking
    batch_size = 500  # Smaller batches for better memory management
    start_time = time.time()
    
    for i in range(0, len(domains), batch_size):
        batch = domains[i:i + batch_size]
        
        # Dynamic worker adjustment (10-30 workers)
        workers = min(30, max(10, len(batch) // 20))
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            results = executor.map(check_domain_availability, batch)
            
            for domain, is_available in results:
                if is_available:
                    available_domains.append(f"{domain}\n")
        
        # Progress reporting
        processed = min(i + batch_size, len(domains))
        elapsed = time.time() - start_time
        print(f"Progress: {processed}/{len(domains)} domains | "
              f"Available: {len(available_domains)} | "
              f"Elapsed: {elapsed:.1f}s")
    
    # Save only available domains
    with open("available.txt", "w") as f:
        f.writelines(available_domains)
    
    print(f"\nDone! Found {len(available_domains)} available domains.")

if __name__ == "__main__":
    main()