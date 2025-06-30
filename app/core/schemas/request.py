from pydantic import BaseModel
from typing import Dict, Optional

class UploadContentRequest(BaseModel):
    content: str
    metadata: Dict[str, str]

class AskQuestionRequest(BaseModel):
    question: str
    persona: Optional[str] = "default"  # default, friendly, strict, humorous