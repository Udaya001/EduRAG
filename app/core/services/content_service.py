from app.db.models import ContentModel
from app.db.database import SessionLocal
from app.core.rag.vector_store import get_vectorstore, save_vectorstore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings  
from langchain.vectorstores import FAISS
import uuid

def add_to_vectorstore(texts):
    # Update embedding model to use Gemini
    embeddings = GoogleGenerativeAIEmbeddings(model="embedding-001")  

    vectorstore = get_vectorstore()
    if vectorstore:
        vectorstore.add_texts(texts=texts)
    else:
        vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings)
    save_vectorstore(vectorstore)


class ContentService:
    def upload_content(self, request):
        db = SessionLocal()
        try:
            content = ContentModel(
                topic=request.metadata.get("topic"),
                title=request.metadata.get("title"),
                grade=request.metadata.get("grade"),
                content=request.content,
                metadata_=request.metadata
            )
            db.add(content)
            db.commit()
            db.refresh(content)

            # Split and add to FAISS
            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            texts = splitter.split_text(request.content)
            add_to_vectorstore(texts)

            return {"message": "Content uploaded", "content_id": content.id}
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()