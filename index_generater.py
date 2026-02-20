import os
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import sparse
from Load_data import extract_all_books

if not os.path.exists("data"):
    os.mkdir("data")


chunks = extract_all_books()

texts = [chunk["text"] for chunk in chunks]

print("Total chunks:", len(texts))



word_vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2),
    max_features=50000
)

word_matrix = word_vectorizer.fit_transform(texts)

print("Word TF-IDF built.")


char_vectorizer = TfidfVectorizer(
    analyzer="char_wb",
    ngram_range=(3, 5),
    max_features=30000
)

char_matrix = char_vectorizer.fit_transform(texts)

print("Char TF-IDF built.")


joblib.dump(word_vectorizer, "data/word_vectorizer.pkl")
joblib.dump(char_vectorizer, "data/char_vectorizer.pkl")

sparse.save_npz("data/word_matrix.npz", word_matrix)
sparse.save_npz("data/char_matrix.npz", char_matrix)

print("Index saved successfully.")