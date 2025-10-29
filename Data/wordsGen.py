import itertools
import string

n = 4

# Define all lowercase letters
letters = string.ascii_lowercase

# Generate all possible 4-letter combinations
combinations = itertools.product(letters, repeat=n)

# Write them to words.txt
with open("words.txt", "w") as f:
    for combo in combinations:
        word = ''.join(combo)
        f.write(word + "\n")

print(f"✅ File 'words.txt' created with all possible {n}-letter combinations.")
