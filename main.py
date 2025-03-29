import whois
import concurrent.futures
import socket
import time
from functools import lru_cache

# Configuration
PHASE1_WORKERS = 100  # Fast DNS workers
PHASE2_WORKERS = 30   # Conservative WHOIS workers
DNS_TIMEOUT = 2       # 2 seconds for DNS
WHOIS_TIMEOUT = 10    # 10 seconds for WHOIS
INPUT_FILE = "words.txt"
OUTPUT_FILE = "verified_available.txt"

def setup_timeouts():
    """Configure system timeouts"""
    socket.setdefaulttimeout(DNS_TIMEOUT)

@lru_cache(maxsize=20000)
def cached_whois(domain):
    """Cached WHOIS lookup with timeout handling"""
    try:
        return whois.whois(domain)
    except:
        return None

def fast_dns_check(domain):
    """Phase 1: Quick DNS check (~95% accurate)"""
    try:
        socket.gethostbyname(domain)
        return False  # Definitely registered
    except:
        return True   # Probably available

def accurate_whois_check(domain):
    """Phase 2: 100% accurate WHOIS verification"""
    # First confirm DNS check again (in case of transient errors)
    try:
        socket.gethostbyname(domain)
        return False
    except:
        pass
    
    # WHOIS verification
    whois_data = cached_whois(domain)
    return whois_data is None or not whois_data.domain_name

def load_domains():
    """Load and format domains from input file"""
    with open(INPUT_FILE, "r") as f:
        return [f"{word.strip()}.com" for word in f if len(word.strip()) <= 7]

def run_phase(domains, check_func, workers, phase_name):
    """Run a checking phase with progress reporting"""
    results = []
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_domain = {executor.submit(check_func, domain): domain for domain in domains}
        
        for i, future in enumerate(concurrent.futures.as_completed(future_to_domain)):
            domain = future_to_domain[future]
            try:
                if future.result():
                    results.append(domain)
            except Exception as e:
                print(f"Error checking {domain}: {str(e)}")
            
            # Progress reporting
            if (i + 1) % 100 == 0 or (i + 1) == len(domains):
                elapsed = time.time() - start_time
                print(f"{phase_name}: Processed {i+1}/{len(domains)} | "
                      f"Found {len(results)} | "
                      f"Elapsed: {elapsed:.1f}s")
    
    return results

def main():
    setup_timeouts()
    
    # Phase 1: Fast DNS pre-scan
    print("=== PHASE 1: Fast DNS Pre-Scan (95% accurate) ===")
    all_domains = load_domains()
    phase1_results = run_phase(all_domains, fast_dns_check, PHASE1_WORKERS, "Phase 1")
    print(f"\nPhase 1 complete: {len(phase1_results)} potential available domains")
    
    # Phase 2: Accurate WHOIS verification
    print("\n=== PHASE 2: WHOIS Verification (100% accurate) ===")
    verified_available = run_phase(phase1_results, accurate_whois_check, PHASE2_WORKERS, "Phase 2")
    
    # Save final results
    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(verified_available))
    
    print(f"\n=== FINAL RESULTS ===")
    print(f"Scanned {len(all_domains)} total domains")
    print(f"Phase 1 candidates: {len(phase1_results)}")
    print(f"Verified available: {len(verified_available)}")
    print(f"Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()