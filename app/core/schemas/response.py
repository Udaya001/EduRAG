from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime

class UploadContentResponse(BaseModel):
    message: str
    content_id: int

class AnswerResponse(BaseModel):
    answer: str

class TopicItem(BaseModel):
    topic: str
    grade: str
    title: str

class TopicListResponse(BaseModel):
    topics: List[TopicItem]

class MetricsResponse(BaseModel):
    total_topics: int
    total_files_uploaded: int
    vector_store_size: int

class FeedbackResponse(BaseModel):
    message: str

class QALogItem(BaseModel):
    id: int
    question: str
    answer: str
    timestamp: datetime

class QALogListResponse(BaseModel):
    logs: List[QALogItem]