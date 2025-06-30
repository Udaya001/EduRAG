from pydantic import BaseModel

class UploadContentResponse(BaseModel):
    message: str
    content_id: int

class AnswerResponse(BaseModel):
    answer: str

class MetricsResponse(BaseModel):
    total_contents: int