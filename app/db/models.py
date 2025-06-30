from sqlalchemy import Column, Integer, String, Text, JSON
from app.db.database import Base

class ContentModel(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, index=True)
    title = Column(String)
    grade = Column(String)
    content = Column(Text)
    metadata_ = Column("metadata", JSON)  