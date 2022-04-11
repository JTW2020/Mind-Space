from flask_cors import CORS
from flask import jsonify  # Potentially used for later purposes
from flask import Flask, request, render_template
from Eliza.commented_eliza import Eliza
from db.index import db_session, init_db

# importing models
from db.user_model import User

print('code runs before init_db')
init_db()

app = Flask(__name__)
CORS(app)

# Instantiating Eliza here
eliza = Eliza()
eliza.load('./Eliza/inbetween.txt')


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

        # This method gets the json data from the request object
        # To access the stored values, access the list with the corresponding key

        input_message = request.get_json()
        user_msg = input_message['userMessage']
        print(user_msg)
    return {
        "message": eliza.respond(user_msg)
    }


@app.route("/api/testEliza")
def test_eliza():
    eliza = Eliza()
    return eliza.test_output()


@app.route("/api/userSignup", methods=['POST'])
def create_user():
    error = None
    if request.method == 'POST':
        print("/api/userSignup is being called")
        msg = request.get_json()
        username = msg['username']
        password = msg['password']
        user = User(username=username, password=password)

        db_session.add(user)
        db_session.commit()

        app.logger.debug('\npassword: ' + password)

    return 'OK'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
