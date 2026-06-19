# Document Q&A Bot using RAG (Retrieval-Augmented Generation)

## Project Description

This project is a Retrieval-Augmented Generation (RAG) based Document Question & Answer Bot built using Python. The system allows users to ask natural language questions about a collection of documents and receive accurate, context-aware answers with source citations.

The application processes multiple documents, converts them into vector embeddings, stores them in a ChromaDB vector database, retrieves the most relevant content for a query, and generates grounded responses using Google Gemini.

---

# Tech Stack

| Component             | Technology        | Version            |
| --------------------- | ----------------- | ------------------ |
| Programming Language  | Python            | 3.11+              |
| LLM                   | Google Gemini     | gemini-2.5-flash   |
| Embedding Model       | Gemini Embeddings | text-embedding-004 |
| Vector Database       | ChromaDB          | 0.4.22+            |
| PDF Processing        | pypdf             | 4.0.0+             |
| DOCX Processing       | python-docx       | 1.1.0+             |
| Environment Variables | python-dotenv     | 1.0.1+             |
| Progress Tracking     | tqdm              | 4.66.0+            |
| Optional UI           | Streamlit         | 1.30.0+            |

---

# Architecture Overview

The project follows a standard Retrieval-Augmented Generation (RAG) pipeline.

```text
Documents
(PDF / DOCX)
      |
      v
Document Loader
      |
      v
Text Extraction
      |
      v
Chunking with Overlap
      |
      v
Embeddings Generation
(text-embedding-004)
      |
      v
ChromaDB Vector Store
      |
      v
Similarity Search
      |
      v
Top-K Relevant Chunks
      |
      v
Google Gemini
      |
      v
Answer + Citations
```

### Pipeline Steps

1. Load documents from the local data folder.
2. Extract text and metadata.
3. Split content into overlapping chunks.
4. Generate embeddings for all chunks.
5. Store embeddings in ChromaDB.
6. Retrieve top-k relevant chunks for user queries.
7. Generate grounded answers using Gemini.
8. Display source citations.

---

# Chunking Strategy

### Strategy Used

Fixed-size character chunking with overlap.

### Configuration

* Chunk Size: 1000 characters
* Chunk Overlap: 200 characters

### Why This Strategy?

* Simple and efficient for beginner-level RAG systems.
* Prevents loss of context at chunk boundaries.
* Produces consistent chunk sizes for embedding generation.
* Improves retrieval accuracy by preserving nearby information.

---

# Embedding Model and Vector Database

## Embedding Model

**Model:** text-embedding-004

### Why?

* High-quality semantic embeddings.
* Integrates easily with Gemini.
* Supports semantic similarity search.
* Suitable for document retrieval tasks.

## Vector Database

**Database:** ChromaDB

### Why?

* Lightweight and easy to set up.
* Persistent storage support.
* No separate server required.
* Fast similarity search.
* Beginner-friendly.

---

# Project Structure

```text
document-qa-bot/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   ├── document1.pdf
│   ├── document2.pdf
│   ├── document3.pdf
│   ├── document4.docx
│   └── document5.docx
│
├── db/
│
└── src/
    ├── config.py
    ├── ingest.py
    ├── query.py
    └── main.py
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/document-qa-bot.git
cd document-qa-bot
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
```

## 5. Add Documents

Place all source documents inside the `data/` folder.

## 6. Run Indexing

```bash
python src/ingest.py
```

This step:

* Loads documents
* Chunks text
* Creates embeddings
* Stores vectors in ChromaDB

## 7. Start the Application

```bash
python src/main.py
```

---

# Environment Variables

| Variable       | Description           |
| -------------- | --------------------- |
| GEMINI_API_KEY | Google Gemini API Key |

### Obtaining Gemini API Key

1. Visit Google AI Studio.
2. Create a new API key.
3. Add it to the `.env` file.

⚠️ Never commit API keys to GitHub.

---

# Example Queries

| Query                                       | Expected Theme               |
| ------------------------------------------- | ---------------------------- |
| What is climate change?                     | Climate document summary     |
| What are the main causes of global warming? | Environmental impacts        |
| Explain machine learning.                   | AI document content          |
| What business strategy increased revenue?   | Business report findings     |
| Summarize the technology report.            | Technology document overview |

### Unanswerable Query Example

**Question:**
Who won the FIFA World Cup 2022?

**Expected Response:**

"I cannot find the answer in the provided documents."

---

# Features

* Multi-document support
* PDF and DOCX document processing
* Automatic text extraction
* Context-preserving chunking
* Semantic similarity search
* ChromaDB persistent vector storage
* Gemini-powered answer generation
* Source citations with filename and page number
* Interactive command-line interface
* Graceful handling of unknown queries

---

# Known Limitations

1. Retrieval quality depends on document quality and chunking strategy.
2. Fixed-size chunking may split information across chunks.
3. OCR is not supported for scanned PDFs.
4. Performance may decrease with very large document collections.
5. The system relies on external API availability for Gemini services.

---

# Future Improvements

* Streamlit web interface
* Hybrid search (keyword + semantic)
* OCR support for scanned PDFs
* Multi-language document support
* Re-ranking for improved retrieval accuracy

---

# Author

AI Engineering Internship Assignment

Developed as part of a Retrieval-Augmented Generation (RAG) implementation project using Python, ChromaDB, and Google Gemini.
