# 🌐 Domain Name Availability Checker

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![NLTK](https://img.shields.io/badge/NLTK-WordNet-yellow)](https://www.nltk.org/)

A Python-based project that **generates, checks, and processes domain names** to find available ones and extract their meanings.  
It combines **DNS lookups**, **WHOIS verification**, and **NLP (WordNet)**-based meaning extraction.


## 📁 Project Structure


.
├── CustomProcessing/
│   ├── meaning.py         # Extracts meanings of verified domain words
│   └── meaning.txt        # Output file with domain meanings
│
├── Data/
│   ├── dictGen.py         # Generates a dictionary (valid English words)
│   ├── dict.txt           # List of English words
│   ├── wordsGen.py        # Generates 4-letter word combinations
│   ├── words.txt          # Output file containing all generated words
│
├── main.py                # Runs DNS + WHOIS domain availability check
├── .gitignore             # Git ignore file
├── .gitattributes         # Git text settings
└── README.md              # Project documentation


---

## ⚙️ How It Works

1. **Generate Words** → Create possible domain name words using `wordsGen.py`  
2. **Generate Dictionary** → Build a dictionary of real words using `dictGen.py`  
3. **Check Domain Availability** → Run `main.py` to find available `.com` domains  
4. **Get Meanings** → Use `meaning.py` to fetch definitions of available domains  


## 🚀 Usage

### 1️⃣ Generate Word List
bash
python Data/wordsGen.py


### 2️⃣ Generate Dictionary

bash
python Data/dictGen.py


### 3️⃣ Run Domain Checker

bash
python main.py


**Output:** `resultDomains.txt` (contains available domains)

### 4️⃣ Extract Meanings

bash
python CustomProcessing/meaning.py


**Output:** `meaning.txt` (domain with meaning)

---

## 📦 Requirements

* Python 3.8+
* Install dependencies:

  bash
  pip install python-whois nltk
  

---

## 🧠 Features

* ✅ Fast **DNS-based pre-scan**
* 🔍 Accurate **WHOIS verification**
* 💬 Meaning extraction using **WordNet**
* ⚡ Multithreaded for better performance

---

## 📜 Output Files

| File                | Description                  |
| ------------------- | ---------------------------- |
| `words.txt`         | Generated word combinations  |
| `dict.txt`          | English word dictionary      |
| `resultDomains.txt` | Available domain names       |
| `meaning.txt`       | Meanings of verified domains |

---

## 👨‍💻 Author

**Athul Murali T**
Computer Science Engineer | MERN & ML Enthusiast
📧 *[athul.t.murali@gmail.com](mailto:athul.t.murali@gmail.com)*


---

✅ **Instructions:**  
1. Copy everything above.  
2. Paste it into your `README.md` file in your GitHub repo.  
3. Save → Commit → Refresh your repo — it’ll render beautifully.
