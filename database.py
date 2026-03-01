import sqlalchemy
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("BASE_DB_URL")
engine = create_engine(DATABASE_URL,connect_args={"sslmode": "require"}  
)

with engine.connect() as conn:
    result = conn.execute(
        text("select 'Hello world'")
    )
    print(result.all())



with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM JOBS"))
    for row in result:
        print(row)

def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM JOBS"))
        jobs = [dict(row) for row in result.mappings()]  
        
    return jobs



        