from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from app.core.rag.llm import get_llm
from app.core.config import settings

def get_sql_agent():
    db = SQLDatabase.from_uri(settings.SQLALCHEMY_DATABASE_URI)
    toolkit = SQLDatabaseToolkit(db=db, llm=get_llm())
    agent = create_sql_agent(llm=get_llm(), toolkit=toolkit, verbose=True)
    return agent

def run_sql_query(query):
    agent = get_sql_agent()
    return agent.run(query)