import fitz
import os
import json

class Book:
    def __init__(self,Name,Pages):
        self.Name = Name
        self.Pages = Pages

def load_text(book , page):
    docs = fitz.open("Books/"+book)
    return docs[page].get_text()

def get_all_books():
    bookslist = []
    booksurl = os.listdir("Books")
    for bookurl in booksurl:
        docs = fitz.open(f"Books/{bookurl}")
        bookslist.append(Book(Name = bookurl,Pages = docs.page_count))
    return bookslist

def extract_book(book_name):
    book_data = []

    with fitz.open(os.path.join("Books", book_name)) as docs:
        for page_index in range(docs.page_count):
            text = docs[page_index].get_text("text").strip()

            if len(text) < 50:
                continue  # skip useless pages

            book_data.append({
                "book": book_name,
                "page": page_index + 1, 
                "text": text
            })

    return book_data

def chunk_page(book_name, page_number, text, lines_per_chunk=6):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    chunks = []
    for i in range(0, len(lines), lines_per_chunk):
        chunk_lines = lines[i:i + lines_per_chunk]
        chunks.append({
            "book": book_name,
            "page": page_number,
            "line_start": i + 1,
            "line_end": i + len(chunk_lines),
            "text": " ".join(chunk_lines)
        })

    return chunks

def extract_all_books():
    all_chunks = []

    for book in get_all_books():
        print("Processing:", book.Name)

        with fitz.open(os.path.join("Books", book.Name)) as docs:
            for page_index in range(docs.page_count):
                text = docs[page_index].get_text("text").strip()

                if len(text) < 50:
                    continue

                chunks = chunk_page(
                    book.Name,
                    page_index + 1,
                    text
                )

                all_chunks.extend(chunks)

    return all_chunks

def save():
    save = extract_all_books()
    open("data/chunks.json","w").write(json.dumps(save))