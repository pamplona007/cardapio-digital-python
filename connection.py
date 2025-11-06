from pymysql import connect
import os
import dotenv

dotenv.load_dotenv()

connection = connect(
    host=os.getenv("DATABASE_HOST"),
    port=int(os.getenv("DATABASE_PORT")),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASS"),
    database=os.getenv("DATABASE_DB"),
    
)