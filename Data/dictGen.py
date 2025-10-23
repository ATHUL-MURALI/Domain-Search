import nltk
from nltk.corpus import words

n = 7

# Download the word list if not already available
nltk.download("words")

# Extract words up to n letters and sort by length
filtered_words = sorted([word.lower() for word in words.words() if len(word) <= n], key=len)

# Save to words.txt
with open("dict.txt", "w") as file:
    file.write("\n".join(filtered_words))

print(f"words.txt has been generated with words sorted by length (1 to {n} letters).")
