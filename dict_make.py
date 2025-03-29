import nltk
from nltk.corpus import words

# Download the word list if not already available
nltk.download("words")

# Extract words up to 6 letters
filtered_words = [word.lower() for word in words.words() if len(word) <= 6]

# Save to words.txt
with open("words.txt", "w") as file:
    file.write("\n".join(filtered_words))

print("words.txt has been generated with words up to 6 letters.")
