from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

def get_llm(model_name="models/gemini-1.5-flash"):
    return ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=0.3
    )