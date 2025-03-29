import whois

def check_domain_availability(domain):
    try:
        domain_info = whois.whois(domain)
        if not domain_info.domain_name:
            return domain, "available"
    except whois.parser.PywhoisError:
        return domain, "available"
    return domain, "not available"

def load_dictionary_words():
    with open("words.txt", "r") as file:
        return [word.strip() for word in file if len(word.strip()) == 6]

def main():
    words = load_dictionary_words()
    with open("domain_status.txt", "w") as status_file, open("available.txt", "w") as available_file:
        for word in words:
            domain = word + ".com"
            domain, status = check_domain_availability(domain)
            print(f"{domain}: {status}")  # Print to terminal
            status_file.write(f"{domain}: {status}\n")
            if status == "available":
                available_file.write(f"{domain}\n")  # Write only available domains

if __name__ == "__main__":
    main()
