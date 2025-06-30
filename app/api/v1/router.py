from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.services.content_service import ContentService
from app.core.services.tutor_service import TutorService
from app.core.schemas.request import UploadContentRequest, AskQuestionRequest
from app.core.schemas.response import UploadContentResponse, AnswerResponse, MetricsResponse, TopicListResponse

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
    persona: str = Query("default", description="Persona: default, friendly, strict, humorous")
):
    answer = service.generate_answer(request.question, persona=persona)
    return {"answer": answer}


@router.get("/topics", response_model=TopicListResponse)
async def get_topics(
    grade: str = Query(None, description="Filter by grade"),
    topic: str = Query(None, description="Filter by topic"),
    service: ContentService = Depends()
):
    results = service.get_filtered_topics(grade=grade, topic=topic)
    return {"topics": results}


@router.get("/metrics")
async def get_metrics(service: ContentService = Depends()):
    metrics = service.get_system_metrics()
    return metrics