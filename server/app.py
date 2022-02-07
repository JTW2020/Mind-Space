from flask import Flask
from flask import jsonify  # Potentially used for later purposes

app = Flask(__name__)


@app.route("/")
def hello_world():
    return {
        "user": "Eliza AI",
        "purpose": "help people"
    }


@app.route("/api/test")
def api():
    pass
