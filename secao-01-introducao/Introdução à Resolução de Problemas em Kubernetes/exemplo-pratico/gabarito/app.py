from flask import Flask
import os
import logging
import psycopg2

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_HOST = os.environ.get("DB_HOST")                            
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD") 
DB_NAME = os.environ.get("DB_NAME")

@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME, connect_timeout=2) 
        cur = conn.cursor()
        cur.execute("SELECT version();")    
        db_version = cur.fetchone()
        conn.close()
        logger.info(f"Hello from Flask! PostgreSQL version: {db_version}")
        return f"Hello from Flask! PostgreSQL version: {db_version}"
    except psycopg2.Error as e:
        logger.error(f"Erro: {e}") 
        return f"Erro: {e}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) 