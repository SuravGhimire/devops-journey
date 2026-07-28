from flask import Flask
import psycopg2
import time

app = Flask(__name__)

conn = None

for i in range(10):
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="devopsdb",
            user="saurav",
            password="password123"
        )
        print("Connected to PostgreSQL!")
        break
    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL...")
        time.sleep(2)

@app.route("/")
def home():

    cur = conn.cursor()

    cur.execute("SELECT version();")

    version = cur.fetchone()

    cur.close()

    return f"""
    <h1>Flask + PostgreSQL</h1>
    <p>{version[0]}</p>
    """

app.run(host="0.0.0.0", port=5000)
