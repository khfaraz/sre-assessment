from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route("/")
def home():
    # Removed artificial delay that caused high latency.
    return "Hello from SRE Test!"

@app.route("/healthz")
def health():
    # Health endpoint should return HTTP 200 when OK.
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)