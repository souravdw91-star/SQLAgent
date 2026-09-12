from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings
from src.db.connection import get_db_connection
from src.agent.toolkit import get_sql_toolkit
from src.prompts.system_prompts import SQL_PREFIX, SQL_SUFFIX

def build_sql_agent():
    # 1. Validate environment
    settings.validate()

    # 2. LLM initialization
    llm = ChatGoogleGenerativeAI(
        model=settings.GEMINI_MODEL,
        temperature=0,
        google_api_key=settings.GOOGLE_API_KEY,
        streaming=False
    )

    # 3. DB & Toolkit setup
    db = get_db_connection()
    toolkit = get_sql_toolkit(db=db, llm=llm)

    # 4. Construct the agent executor
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        agent_type="tool-calling",
        verbose=True,
        prefix=SQL_PREFIX,
        suffix=SQL_SUFFIX,
        handle_parsing_errors=True
    )
    return agent_executor