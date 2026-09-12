from typing import List, Optional
from langchain_community.utilities import SQLDatabase
from config.settings import settings

def get_db_connection(
    include_tables: Optional[List[str]] = None,
    ignore_tables: Optional[List[str]] = None,
    sample_rows_in_table_info: int = 2
) -> SQLDatabase:
    """
    Initializes a LangChain SQLDatabase connection with read limits and schema isolation.
    """
    return SQLDatabase.from_uri(
        database_uri=settings.mysql_uri,
        include_tables=include_tables,
        ignore_tables=ignore_tables,
        sample_rows_in_table_info=sample_rows_in_table_info
    )