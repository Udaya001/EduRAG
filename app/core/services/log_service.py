from app.db.models import LogModel
from app.db.database import SessionLocal

class LogService:
    def log_question_answer(self, question, answer):
        db = SessionLocal()
        try:
            log_entry = LogModel(question=question, answer=answer)
            db.add(log_entry)
            db.commit()
        finally:
            db.close()

    def get_logs(self):
        db = SessionLocal()
        try:
            logs = db.query(LogModel).filter(LogModel.timestamp.isnot(None)).all()
            return logs
        finally:
            db.close()

