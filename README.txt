# 🌐 Domain Name Availability Checker

[](https://www.python.org/)
[](https://www.google.com/search?q=LICENSE)
[](https://www.nltk.org/)

A Python tool to generate, check, and find the meanings of available `.com` domain names. It combines multithreaded DNS/WHOIS lookups with NLTK (WordNet) for meaning extraction.

## 🧠 Features

  * ✅ Fast **DNS-based pre-scan** to quickly filter unavailable domains.
  * 🔍 Accurate **WHOIS verification** for final availability checks.
  * 💬 Meaning extraction for available domains using **NLTK WordNet**.
  * ⚡ **Multithreaded** for faster checking of large wordlists.
  * 🔡 Includes generators for both **4-letter combinations** and **real English words**.

## 🚀 Workflow & Usage

Follow these steps to find available domains and their meanings.

### 1️⃣ Installation

Clone the repository and install the required Python packages:

```bash
pip install python-whois nltk
```

### 2️⃣ Step 1: Generate a Wordlist

You can generate a wordlist to check. Choose one of the following options:

**Option A: Generate all 4-letter word combinations**

```bash
python Data/wordsGen.py
```

  * **Output:** `Data/words.txt`

**Option B: Generate a dictionary of valid English words**

```bash
python Data/dictGen.py
```

  * **Output:** `Data/dict.txt`

### 3️⃣ Step 2: Run the Domain Checker

Run `main.py` to check the availability of domains from your generated wordlist.

*(Note: You may need to edit `main.py` to point to your desired input file, e.g., `Data/words.txt` or `Data/dict.txt`)*

```bash
python main.py
```

  * **Output:** `resultDomains.txt` (contains a list of available domains)

### 4️⃣ Step 3: Extract Meanings

Once you have a list of available domains, run `meaning.py` to fetch their definitions. This script reads `resultDomains.txt` and uses WordNet.

```bash
python CustomProcessing/meaning.py
```

  * **Output:** `CustomProcessing/meaning.txt` (contains available domains with their meanings)

-----

## 📁 Project Structure

```
.
├── CustomProcessing/
│   ├── meaning.py         # Extracts meanings of verified domain words
│   └── meaning.txt        # Output file with domain meanings
│
├── Data/
│   ├── dictGen.py         # Generates a dictionary (valid English words)
│   ├── dict.txt           # List of English words
│   ├── wordsGen.py        # Generates 4-letter word combinations
│   └── words.txt          # Output file containing all generated words
│
├── main.py                # Runs DNS + WHOIS domain availability check
├── .gitignore
├── .gitattributes
└── README.md
```

## 📜 Output Files

| File | Description |
| :--- | :--- |
| `Data/words.txt` | Generated 4-letter word combinations |
| `Data/dict.txt` | Generated English word dictionary |
| `resultDomains.txt` | List of available domain names |
| `CustomProcessing/meaning.txt` | Meanings of the available domains |

-----

## 👨‍💻 Author

**Athul Murali T**
<br>
Computer Science Engineer | MERN & ML Enthusiast
<br>
📧 *[athul.t.murali@gmail.com](mailto:athul.t.murali@gmail.com)*