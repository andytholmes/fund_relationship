import os
from dotenv import load_dotenv

load_dotenv()

# SQL Server connection string format
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mssql+pyodbc://user:password@server_name/database_name?driver=ODBC+Driver+18+for+SQL+Server"
) 