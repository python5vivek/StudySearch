You built a local search engine for PDFs using TF-IDF + cosine similarity. That’s not a toy. That’s a proper information retrieval pipeline. Clean. Classical. Effective.

Below is a professional README file you can put directly into your repository.

---

# 📚 PDF Book Search Engine (TF-IDF Based)

A lightweight local search engine that indexes multiple PDF books and allows fast semantic search across all pages using **word-level + character-level TF-IDF** and **cosine similarity**.

This project extracts text from PDFs, splits it into intelligent chunks, builds vector indexes, and enables fast top-K search results with scoring.

---

## 🚀 Features

* 📖 Extracts text from all PDFs inside `Books/`
* 🧩 Splits pages into small searchable chunks
* 🔠 Word-level TF-IDF (unigram + bigram)
* 🔡 Character-level TF-IDF (3–5 grams)
* ⚡ Hybrid scoring (70% word + 30% char)
* 💾 Saves trained vectorizers and sparse matrices
* 🔍 Fast cosine similarity search
* 📊 Returns book name, page number, line range, and score

---

## 🏗️ Project Structure

```
project/
│
├── Books/                  # All PDF books go here
├── data/                   # Auto-generated index files
│   ├── chunks.json
│   ├── word_vectorizer.pkl
│   ├── char_vectorizer.pkl
│   ├── word_matrix.npz
│   └── char_matrix.npz
│
├── Load_data.py            # PDF extraction & chunking
├── build_index.py          # TF-IDF training & saving
├── search.py               # Query search engine
└── README.md
```

---

## ⚙️ How It Works

### 1️⃣ Text Extraction

Using **PyMuPDF (fitz)**:

* Reads all PDFs from `Books/`
* Skips low-content pages
* Extracts clean text
* Splits text into small chunks (default: 6 lines per chunk)

Each chunk stores:

* Book name
* Page number
* Line range
* Text content

---

### 2️⃣ Index Building

Two TF-IDF models are created:

#### Word-level TF-IDF

* Lowercased
* English stopwords removed
* N-grams: (1,2)
* Max features: 50,000

#### Character-level TF-IDF

* Analyzer: `char_wb`
* N-grams: (3,5)
* Max features: 30,000

Matrices are saved as sparse `.npz` files.

---

### 3️⃣ Search Process

When a query is given:

* Transform query using both vectorizers
* Compute cosine similarity
* Combine scores:

```
final_score = 0.7 * word_score + 0.3 * char_score
```

* Return top-K results ranked by relevance

---

## 📦 Installation

```bash
pip install pymupdf scikit-learn numpy scipy joblib
```

---

---

## 🌐 Live Demo

🚀 Try StudySearch here:  
https://studysearch.pythonanywhere.com/

---



## 🛠️ Usage

### Step 1: Put PDFs inside `Books/`

```
Books/
    book1.pdf
    book2.pdf
```

---

### Step 2: Build Index

Run the indexing script:

```bash
python build_index.py
```

This will:

* Extract all text
* Build TF-IDF matrices
* Save everything into `data/`

---

### Step 3: Search

```python
from search import search

results = search("What is machine learning?", top_k=5)

for r in results:
    print(r["book"], r["page"])
    print(r["text"])
    print("Score:", r["score"])
    print("-" * 40)
```

---

## 🧠 Why Hybrid TF-IDF?

Word-level TF-IDF:

* Captures meaning
* Handles phrases

Character-level TF-IDF:

* Handles typos
* Handles partial matches
* Handles rare words

Combining both gives stronger retrieval accuracy.

---

## 📊 Output Example

```json
{
  "book": "ML_Book.pdf",
  "page": 42,
  "line_start": 7,
  "line_end": 12,
  "text": "Machine learning is a subset of artificial intelligence...",
  "score": 0.8732
}
```

---

## 📈 Future Improvements

* Add sentence embeddings (SBERT)
* Use FAISS for faster similarity search
* Add FastAPI backend
* Add web interface
* Add ranking boost for exact phrase matches

---

## 🧪 Tech Stack

* Python
* PyMuPDF
* Scikit-Learn
* NumPy
* SciPy
* Joblib

---

## 📜 License

MIT License

---

This project demonstrates a classical Information Retrieval system similar to early search engines before neural embeddings became popular.

Clean. Fast. Fully local. No API calls.

---

If you later upgrade this with embeddings + FAISS + FastAPI, it becomes a mini Google for your own books. And that’s a very powerful thing to build.
