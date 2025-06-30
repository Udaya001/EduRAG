import os
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

FAISS_INDEX_PATH = "faiss_index"

def get_vectorstore():
    if os.path.exists(FAISS_INDEX_PATH):
        embeddings = GoogleGenerativeAIEmbeddings(model="embedding-001")
        return FAISS.load_local(FAISS_INDEX_PATH, embeddings)
    else:
        return None

def save_vectorstore(vectorstore):
    vectorstore.save_local(FAISS_INDEX_PATH)