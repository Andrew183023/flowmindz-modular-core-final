from urllib.parse import urlparse
import psycopg2
import os

def get_connection():
    result = urlparse(os.getenv("DATABASE_URL"))
    return psycopg2.connect(
        dbname=result.path[1:],  # remove o /
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port
    )


