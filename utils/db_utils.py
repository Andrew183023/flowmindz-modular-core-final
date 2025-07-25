import os
import psycopg2
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

def get_connection():
    db_url = os.getenv("DATABASE_URL")  # Usa a string pronta
    print("[DEBUG] DATABASE_URL:", db_url)

    result = urlparse(db_url)

    return psycopg2.connect(
        dbname=result.path[1:],
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port,
        sslmode="require"  # ESSENCIAL pro Railway
    )




