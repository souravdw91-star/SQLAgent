from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI

def get_sql_toolkit(db: SQLDatabase, llm: ChatGoogleGenerativeAI) -> SQLDatabaseToolkit:
    """
    Wraps the database connection and model into standard SQL execution tools.
    """
    return SQLDatabaseToolkit(db=db, llm=llm)