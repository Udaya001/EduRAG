from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from app.core.rag.llm import get_llm
from app.core.rag.vector_store import get_vectorstore

DEFAULT_PROMPT = """
You are an educational tutor. Use the following context to answer the question.
If you don't know the answer, just say so.

Context:
{context}

Question:
{question}

Answer:
"""

PERSONA_PROMPTS = {
    "friendly": """
You're a friendly tutor who explains things clearly and encourages students.

Context:
{context}

Question:
{question}

Friendly Answer:
""",
    "strict": """
You're a strict tutor. Only use information from the context. Be factual.

Context:
{context}

Question:
{question}

Strict Answer:
""",
    "humorous": """
You're a humorous tutor. Make learning fun while staying accurate.

Context:
{context}

Question:
{question}

Humorous Answer:
"""
}

def get_rag_chain(persona="default"):
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    prompt_template = PERSONA_PROMPTS.get(persona.lower(), DEFAULT_PROMPT)
    prompt = PromptTemplate.from_template(prompt_template)

    chain = RetrievalQA.from_chain_type(
        llm=get_llm(),
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
    return chain

def generate_answer(question: str, persona="default"):
    chain = get_rag_chain(persona)
    result = chain.invoke({"query": question})
    return result["result"]