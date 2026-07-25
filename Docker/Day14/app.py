from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():

    username = os.getenv("USERNAME", "Guest")

    return f"""
    <h1>Docker Environment Variables</h1>
    <h2>Welcome {username}</h2>
    """

app.run(host="0.0.0.0", port=5000)
