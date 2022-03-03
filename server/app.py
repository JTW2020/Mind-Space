from flask_cors import CORS
from flask import jsonify  # Potentially used for later purposes
from flask import Flask, request, render_template
from Eliza.commented_eliza import Eliza

app = Flask(__name__)
CORS(app)

# Instantiating Eliza here
eliza = Eliza()


@app.route("/")
def index():
    return render_template("../client/build/index.html")


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
    error = None
    if request.method == 'POST':
        input_message = request.get_json()
        print(input_message)
    return {
        "message": "fluff"
    }


@app.route("/api/testEliza")
def test_eliza():
    eliza = Eliza()
    return eliza.test_output()
