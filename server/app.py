from flask_cors import CORS
from flask import jsonify  # Potentially used for later purposes
from flask import Flask, request, render_template
from Eliza.commented_eliza import Eliza

app = Flask(__name__, static_folder="client/build/static",
            template_folder="client/build")
CORS(app)

# Instantiating Eliza here
eliza = Eliza()
eliza.load('./Eliza/inbetween.txt')


@app.route("/")
def index():
    return render_template("index.html")


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

        # This method gets the json data from the request object
        # To access the stored values, access the list with the corresponding key

        input_message = request.get_json()
        user_msg = input_message['userMessage']
        print("This is the message being sent: " + user_msg)
    return {
        "message": eliza.respond(user_msg)
    }


@app.route("/api/initialMsgEliza", methods=['GET'])
def fromEliza():
    error = None
    if request.method == 'GET':
        return {
            "message": eliza.initial()
        }


@app.route("/api/testEliza")
def test_eliza():
    eliza = Eliza()
    return eliza.test_output()
