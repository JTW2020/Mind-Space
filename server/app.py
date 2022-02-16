from flask import Flask
from flask import jsonify  # Potentially used for later purposes

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return {
        "sender": "Eliza",
        "message": "Hello there user!"
    }



@app.route("/api/test")
def api():
    return '<p>This is the test api endpoint</p>'
