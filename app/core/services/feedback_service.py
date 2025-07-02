from app.db.models import FeedbackModel
from app.db.database import SessionLocal

class FeedbackService:
    def submit_feedback(self, question, answer, rating, comment=None):
        db = SessionLocal()
        try:
            feedback = FeedbackModel(
                question=question,
                answer=answer,
                rating=rating,
                comment=comment
            )
            db.add(feedback)
            db.commit()
            return {"message": "Thank you for your feedback!"}
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()