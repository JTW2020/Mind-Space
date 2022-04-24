import pickle
from os import environ as env
import sys

from flask_cors import CORS
from flask import jsonify, session  # Potentially used for later purposes
from flask import Flask, request, Response, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user
from flask_session import Session

from Eliza.commented_eliza import Eliza
from db.index import db_session, init_db
from db.user_model import User
from db.unique_eliza_model import Unique_Eliza

app = Flask(__name__)
app.secret_key = 'partycat'

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

# importing models

app.logger.info('code runs before init_db')
init_db()

CORS(app)

# Instantiating Eliza here
"""
Kind of like the login helper method
"""


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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

    """
    Beforehand Eliza was instantiated at the top of the file, we now need to pull the
    Eliza instance from the database to pass responses in to

    will look something like this:

    - retrieve Eliza from db
    - instantiate it
    - pass methods to the object
    - get and return responses
    """
    print('This is the session id:' + str(session['id']), file=sys.stderr)
    #if request.method == 'POST':

    #    # This method gets the json data from the request object
    #    # To access the stored values, access the list with the corresponding key

    #    input_message = request.get_json()
    #    user_msg = input_message['userMessage']
    #    print(user_msg)
    return {
        "message": 'hello'
        # "message": eliza.respond(user_msg)
    }


@app.route("/api/testEliza")
def test_eliza():
    eliza = Eliza()
    return eliza.test_output()


@app.route("/api/userSignup", methods=['POST'])
def create_user():
    error = None
    if request.method == 'POST':
        msg = request.get_json()

        username = msg['username']

        ''' 
        Password is hashed in the following line
        '''
        hashed_pwd = bcrypt.generate_password_hash(
            msg['password']).decode('utf-8')

        '''
        User object is created and stored in the following lines
        '''
        user = User(username, hashed_pwd)
        db_session.add(user)
        
        eliza = pickle.dumps(Eliza())
        user.users_eliza.append(Unique_Eliza(eliza))
        db_session.commit()


    return 'OK'


""" This method is used to login the user """
@app.route("/api/userLogin", methods=['POST'])
def auth_user():
    error = None
    if request.method == 'POST':
        msg = request.get_json()
        username = msg['username']
        password = msg['password']

        user = User.query.filter_by(username=username).first()

        if not user or not bcrypt.check_password_hash(user.password, password):
            return Response(status=401)

        login_user(user, remember=True)
        print('This is the user_id:' + str(user.id), file=sys.stderr)
        return 'OK'


@app.route("/api/testSessionInfo")
def test_session_info():
    app.logger.info()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
