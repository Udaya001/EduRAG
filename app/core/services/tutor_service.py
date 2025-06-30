from app.core.rag.rag import generate_answer
from app.core.services.log_service import LogService 
class TutorService:
    def generate_answer(self, question, persona="default"):
        answer = generate_answer(question, persona)

        # Log the interaction
        LogService().log_question_answer(question, answer)

        return answer
