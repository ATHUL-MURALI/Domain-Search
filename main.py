import whois
import concurrent.futures

# Function to check domain availability
def check_domain_availability(domain):
    try:
        domain_info = whois.whois(domain)
        if not domain_info.domain_name:
            return domain, "available"
    except Exception:  # Handles both PywhoisError and unexpected errors
        return domain, "available"
    return domain, "not available"

# Load 6-letter words from the dictionary file
def load_dictionary_words():
    with open("words.txt", "r") as file:
        return [word.strip() for word in file if len(word.strip()) == 6]

# Optimized main function using ThreadPoolExecutor
def main():
    words = load_dictionary_words()
    domains = [word + ".com" for word in words]

    available_domains = []
    all_statuses = []

    # Use ThreadPoolExecutor for concurrent WHOIS lookups
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(check_domain_availability, domains)

        # Collect results
        for domain, status in results:
            print(f"{domain}: {status}")
            all_statuses.append(f"{domain}: {status}\n")
            if status == "available":
                available_domains.append(f"{domain}\n")

    # Write results to files efficiently
    with open("domain_status.txt", "w") as status_file:
        status_file.writelines(all_statuses)  # Buffered writing

    with open("available.txt", "w") as available_file:
        available_file.writelines(available_domains)  # Buffered writing

if __name__ == "__main__":
    main()
