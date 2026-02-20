import json
import joblib
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

word_vectorizer = joblib.load("data/word_vectorizer.pkl")
char_vectorizer = joblib.load("data/char_vectorizer.pkl")

word_matrix = sparse.load_npz("data/word_matrix.npz")
char_matrix = sparse.load_npz("data/char_matrix.npz")


def search(query, top_k=5):
    query = query.strip().lower()


    word_query_vec = word_vectorizer.transform([query])
    char_query_vec = char_vectorizer.transform([query])


    word_scores = cosine_similarity(word_query_vec, word_matrix)[0]
    char_scores = cosine_similarity(char_query_vec, char_matrix)[0]


    final_scores = 0.7 * word_scores + 0.3 * char_scores

    top_indices = np.argsort(final_scores)[-top_k:][::-1]

    results = []
    for idx in top_indices:
        results.append({
            "book": chunks[idx]["book"],
            "page": chunks[idx]["page"],
            "line_start": chunks[idx]["line_start"],
            "line_end": chunks[idx]["line_end"],
            "text": chunks[idx]["text"],
            "score": float(final_scores[idx])
        })

    return results

