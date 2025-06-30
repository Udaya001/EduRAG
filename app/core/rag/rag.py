from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from app.core.rag.llm import get_llm
from app.core.rag.vector_store import get_vectorstore
from app.utils.logger import get_logger

logger = get_logger(__name__)

# Define a customizable system prompt for the tutor persona
DEFAULT_SYSTEM_PROMPT = """
You are an intelligent educational tutor. Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context:
{context}

Question:
{question}

Answer:
"""

def get_rag_chain(persona: str = "default"):
    """
    Builds and returns a RetrievalQA chain using the configured LLM and vector store.
    Optionally applies different personas/system prompts.
    """
    vectorstore = get_vectorstore()
    if not vectorstore:
        logger.error("Vector store not found. Please upload content first.")
        raise ValueError("Vector store not initialized")

    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    # Customize system prompt based on persona
    system_prompt = {
        "default": DEFAULT_SYSTEM_PROMPT,
        "friendly": """
You're a friendly educational tutor! Help students understand concepts clearly.
Use simple language and be encouraging.
        
Context:
{context}

Question:
{question}

Friendly Answer:
""",
        "strict": """
You're a strict educational tutor. Only provide factual and precise answers based on the context.
Do not add opinions or extra information.

Context:
{context}

Question:
{question}

Strict Answer:
""",
        "humorous": """
You're a humorous tutor. Explain things with a light-hearted tone, but stay accurate.

Context:
{context}

Question:
{question}

Humorous Answer:
"""
    }.get(persona.lower(), DEFAULT_SYSTEM_PROMPT)

    QA_CHAIN_PROMPT = PromptTemplate.from_template(system_prompt)

    qa_chain = RetrievalQA.from_chain_type(
        llm=get_llm(),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )
    logger.info(f"RAG chain initialized with {persona} persona")
    return qa_chain


def generate_answer(question: str, persona: str = "default") -> str:
    """
    Takes a question and optional persona, retrieves context, and generates an answer.
    Returns only the final answer string.
    """
    qa_chain = get_rag_chain(persona)
    result = qa_chain({"query": question})
    logger.debug("Generated answer for question '{}': {}", question, result["result"])
    return result["result"]