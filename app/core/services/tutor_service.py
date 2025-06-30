from app.core.rag.rag import generate_answer

class TutorService:
    def generate_answer(self, question, persona="default"):
        return generate_answer(question, persona)