import google.generativeai as genai
import chromadb

from chromadb.utils.embedding_functions import GoogleGenerativeAiEmbeddingFunction

from config import *

genai.configure(api_key=GEMINI_API_KEY)


def query_rag(question):

    client = chromadb.PersistentClient(path=DB_PATH)

    embedding_fn = GoogleGenerativeAiEmbeddingFunction(
        api_key=GEMINI_API_KEY,
        model_name=EMBEDDING_MODEL
    )

    collection = client.get_collection(
        COLLECTION_NAME,
        embedding_function=embedding_fn
    )

    results = collection.query(
        query_texts=[question],
        n_results=TOP_K
    )

    context = ""

    citations = []

    for doc, meta in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):

        citation = f"{meta['source']} Page {meta['page']}"

        citations.append(citation)

        context += f"\n[{citation}]\n{doc}\n"

    prompt = f"""
You are a document question answering assistant.

Use ONLY the provided context.

If the answer is not present in the context, reply:

I cannot find the answer in the provided documents.

Context:
{context}

Question:
{question}

Answer:
"""

    model = genai.GenerativeModel(LLM_MODEL)

    response = model.generate_content(prompt)

    return response.text, citations, context
