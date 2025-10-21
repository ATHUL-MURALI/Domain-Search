import nltk
from nltk.corpus import wordnet

# Ensure necessary NLTK data is downloaded
nltk.download('wordnet')
nltk.download('omw-1.4')

def get_meaning(word):
    synsets = wordnet.synsets(word)
    return synsets[0].definition() if synsets else None  # Get the first definition if available

def process_dataset(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            word = line.strip().split('.com')[0]  # Extract word before .com
            meaning = get_meaning(word)
            if meaning:  # Only write if a meaning is found
                outfile.write(f"{line.strip()} - {meaning}\n")

# File paths
input_file = "verified_available.txt"
output_file = "meaning.txt"

# Process dataset
process_dataset(input_file, output_file)

print(f"Processed meanings saved to {output_file}")
