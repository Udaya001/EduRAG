from pydantic import BaseModel
from typing import Dict, Optional

class UploadContentRequest(BaseModel):
    content: str
    metadata: Dict[str, str]

class AskQuestionRequest(BaseModel):
    question: str
    persona: Optional[str] = "default"  # default, friendly, strict, humorous

class FeedbackRequest(BaseModel):
    question: str
    answer: str
    rating: int  # 1 to 5
    comment: Optional[str] = None