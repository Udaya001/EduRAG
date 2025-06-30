import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.config import settings

FAISS_INDEX_PATH = "faiss_index"

def get_vectorstore():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=settings.GOOGLE_API_KEY
    )
    
    if os.path.exists(FAISS_INDEX_PATH):
        return FAISS.load_local(
            FAISS_INDEX_PATH,
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )
    else:
        return None

def save_vectorstore(vectorstore):
    vectorstore.save_local(FAISS_INDEX_PATH)