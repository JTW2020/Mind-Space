import pickle
from os import environ as env
import sys

from flask_cors import CORS
from flask import Flask, request, Response, render_template, session, send_from_directory
from flask_session import Session
from flask_bcrypt import Bcrypt

from sqlalchemy import select

from Eliza.commented_eliza import Eliza
from db.index import db_session, init_db
from db.user_model import User
from db.unique_eliza_model import Unique_Eliza

app = Flask(__name__, static_folder="client/build/static", template_folder="client/build")

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_NAME'] = 'session_cookie'
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.secret_key = 'partycat'
app.config.from_object(__name__)
Session(app)

CORS(app)

bcrypt = Bcrypt(app)

# importing models

app.logger.info('code runs before init_db')
init_db()


# Instantiating Eliza here
"""
Kind of like the login helper method
"""

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

    """
    Beforehand Eliza was instantiated at the top of the file, we now need to pull the
    Eliza instance from the database to pass responses in to

    will look something like this:

    - retrieve Eliza from db
    - instantiate it
    - pass methods to the object
    - get and return responses
    """

    statement = select(User, Unique_Eliza) \
        .filter_by(id=session.get('id'))
    result = db_session.execute(statement).all()

    print('This is the stored Eliza binary:' + str(result), file=sys.stderr)
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
        
        session['id'] = user.id

        # user.id returns the user's id
        print('This is the session_id:' + str(session.get('id')), file=sys.stderr)
        return 'OK'


@app.route("/api/testSessionInfo")
def test_session_info():
    app.logger.info()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
