from fastapi import FastAPI
from app.api.v1.router import router as api_router
from app.db.models import ContentModel
from app.db.database import engine
from app.utils.logger import get_logger

logger = get_logger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="EduRAG: Intelligent Tutor",
    description="AI-powered tutoring system using RAG, LangChain, and Gemini API.",
    version="1.0"
)

# Ensure tables exist
ContentModel.metadata.create_all(bind=engine)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {
        "message": "Welcome to EduRAG – Intelligent Tutor Using RAG and LangChain!"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)