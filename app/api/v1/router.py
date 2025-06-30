from fastapi import APIRouter, Depends, HTTPException
from app.core.services.content_service import ContentService
from app.core.services.tutor_service import TutorService
from app.core.schemas.request import UploadContentRequest, AskQuestionRequest
from app.core.schemas.response import UploadContentResponse, AnswerResponse

router = APIRouter()

@router.post("/upload-content", response_model=UploadContentResponse)
async def upload_content(
    request: UploadContentRequest,
    service: ContentService = Depends()
):
    result = service.upload_content(request)
    return result

@router.post("/ask", response_model=AnswerResponse)
async def ask_question(
    request: AskQuestionRequest,
    service: TutorService = Depends(),
    persona: str = "default"
):
    answer = service.generate_answer(request.question, persona=persona)
    return {"answer": answer}