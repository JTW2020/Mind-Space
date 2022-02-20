from flask import Flask, request
from flask import jsonify  # Potentially used for later purposes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/hello")
def hello_world():
    return {
        "sender": "Eliza",
        "message": "Hello there user!"
    }


@app.route("/api/test")
def api():
    return '<p>This is the test api endpoint</p>'


@app.route("/api/msgEliza", methods=['POST'])
def msgToEliza():
    return {
        "message": "fluff"
    }
