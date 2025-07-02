from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from .llm import get_llm
from .vector_store import get_vectorstore
from .prompts import DEFAULT_PROMPT ,PERSONA_PROMPTS



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