from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Docker Day 20 - Optimized Application"

@app.route("/health")
def health():
    return "healthy"

app.run(host="0.0.0.0", port=5000)
