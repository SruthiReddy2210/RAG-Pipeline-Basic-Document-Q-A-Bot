import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DATA_DIR = "./data"
DB_PATH = "./db"

COLLECTION_NAME = "document_knowledge_base"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 3

EMBEDDING_MODEL = "models/text-embedding-004"
LLM_MODEL = "gemini-2.5-flash"
