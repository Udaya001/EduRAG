from sqlalchemy import Column, Integer, String, Text, JSON, DateTime
from app.db.database import Base
from datetime import datetime

class ContentModel(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, index=True)
    title = Column(String)
    grade = Column(String)
    content = Column(Text)
    metadata_ = Column("metadata", JSON)  


class FeedbackModel(Base):
    __tablename__ = "feedback"


    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)  
    comment = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)  

class LogModel(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow) 