from flask import Flask
import os

app = Flask(__name__)

DATA_FILE = "/data/visits.txt"

@app.route("/")
def home():
    count = 1

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            count = int(f.read()) + 1

    with open(DATA_FILE, "w") as f:
        f.write(str(count))

    return f"<h1>Visit Count: {count}</h1>"

app.run(host="0.0.0.0", port=5000)
