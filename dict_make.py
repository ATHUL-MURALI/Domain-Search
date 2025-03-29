import nltk
from nltk.corpus import words

# Download the word list if not already available
nltk.download("words")

# Extract words up to 7 letters and sort by length
filtered_words = sorted([word.lower() for word in words.words() if len(word) <= 7], key=len)

# Save to words.txt
with open("words.txt", "w") as file:
    file.write("\n".join(filtered_words))

print("words.txt has been generated with words sorted by length (1 to 7 letters).")
