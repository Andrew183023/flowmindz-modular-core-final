import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env

def get_connection():
    # Monta a URL do banco manualmente
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    
    print("[DEBUG] DATABASE_URL:", db_url)  # Log útil pra testar

    return psycopg2.connect(db_url)


