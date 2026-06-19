import os
from pypdf import PdfReader
from docx import Document

import chromadb
from chromadb.utils.embedding_functions import GoogleGenerativeAiEmbeddingFunction

from config import *

def extract_pdf(file_path):
    pages = []

    reader = PdfReader(file_path)

    for page_num, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:
            pages.append({
                "text": text,
                "source": os.path.basename(file_path),
                "page": page_num + 1
            })

    return pages


def extract_docx(file_path):

    doc = Document(file_path)

    text = "\n".join(
        para.text for para in doc.paragraphs
    )

    return [{
        "text": text,
        "source": os.path.basename(file_path),
        "page": 1
    }]


def chunk_text(text):

    chunks = []

    start = 0

    while start < len(text):

        end = start + CHUNK_SIZE

        chunks.append(text[start:end])

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


documents = []

for file in os.listdir(DATA_DIR):

    file_path = os.path.join(DATA_DIR, file)

    if file.endswith(".pdf"):
        documents.extend(extract_pdf(file_path))

    elif file.endswith(".docx"):
        documents.extend(extract_docx(file_path))


all_chunks = []

for doc in documents:

    chunks = chunk_text(doc["text"])

    for chunk in chunks:

        all_chunks.append({
            "text": chunk,
            "metadata": {
                "source": doc["source"],
                "page": doc["page"]
            }
        })

print(f"Created {len(all_chunks)} chunks")


client = chromadb.PersistentClient(path=DB_PATH)

embedding_fn = GoogleGenerativeAiEmbeddingFunction(
    api_key=GEMINI_API_KEY,
    model_name=EMBEDDING_MODEL
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_fn
)

ids = [f"id_{i}" for i in range(len(all_chunks))]
documents = [chunk["text"] for chunk in all_chunks]
metadatas = [chunk["metadata"] for chunk in all_chunks]

collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print("Indexing Completed")
