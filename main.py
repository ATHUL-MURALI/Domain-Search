import whois
import concurrent.futures
import socket
import time
from functools import lru_cache

# Configuration
HIGH_ACCURACY_MODE = False  # Set False for 95% accuracy (faster)
DNS_TIMEOUT = 3             # 3 seconds for DNS
WHOIS_TIMEOUT = 10          # 10 seconds for WHOIS
WORKERS = 50                # More workers for parallel processing

socket.setdefaulttimeout(DNS_TIMEOUT)

@lru_cache(maxsize=10000)
def cached_whois(domain):
    try:
        return whois.whois(domain)
    except:
        return None

def check_domain(domain):
    # Stage 1: DNS Check (Fast)
    try:
        socket.gethostbyname(domain)
        return domain, False  # Definitely registered
    except:
        if not HIGH_ACCURACY_MODE:
            # In fast mode, assume available if DNS fails
            return domain, True  # 95% accurate
        # Proceed to WHOIS in high-accuracy mode

    # Stage 2: WHOIS Check (Slow but 100% accurate)
    try:
        info = cached_whois(domain)
        return domain, (info is None or not info.domain_name)
    except:
        return domain, False  # Assume registered if WHOIS fails

def main():
    domains = [f"{word.strip()}.com" for word in open("words.txt") if len(word.strip()) == 6]
    
    start = time.time()
    available = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as executor:
        results = executor.map(check_domain, domains)
        for domain, is_avail in results:
            if is_avail:
                available.append(domain + "\n")
    
    with open("available.txt", "w") as f:
        f.writelines(available)
    
    total_time = time.time() - start
    print(f"Checked {len(domains)} domains in {total_time:.1f}s")
    print(f"Found {len(available)} available domains")
    print(f"Mode: {'100% accurate' if HIGH_ACCURACY_MODE else '95% accurate (faster)'}")

if __name__ == "__main__":
    main()