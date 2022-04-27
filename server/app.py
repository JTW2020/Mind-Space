import pickle
from os import environ as env
import sys

from flask_cors import CORS
from flask import Flask, request, Response, render_template, session, send_from_directory
from flask_session import Session
from flask_bcrypt import Bcrypt

from sqlalchemy import select

from Eliza.commented_eliza import Eliza
from db.user_model import User
from db.unique_eliza_model import Unique_Eliza
from db.index import db_session, init_db

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

init_db()

from db.inbetween_reassembly_rating_model import InBetweenReassemblyRatings
from db.anxiety_reassembly_rating_model import AnxietyReassemblyRatings
from db.depression_reassembly_rating_model import DepressionReassemblyRatings
from db.anger_reassembly_rating_model import AngerReassemblyRatings
from db.disorder_reassembly_rating_model import DisorderReassemblyRatings

# Instantiating Eliza here
"""
Kind of like the login helper method
"""

@app.route("/home")
@app.route("/about")
@app.route("/chat")
@app.route("/login")
@app.route("/signup")
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

    if request.method == 'POST':

        #statement = select(User, Unique_Eliza) \
        #    .join(User.users_eliza) \
        #    .filter_by(id=session.get('id'))
        #result = db_session.execute(statement).fetchone()
        
        # The following line prints the serialized Eliza
        # print(result.Unique_Eliza.eliza, file=sys.stderr)


        #print(result.User, file=sys.stderr)

        #eliza = pickle.loads(result.Unique_Eliza.eliza)

        #statement = select(DisorderReassemblyRatings)

        #ratings = db_session.execute(statement).all()
        #ratings_list = [row.DisorderReassemblyRatings.rating for row in ratings]

        #print(ratings_list, file=sys.stderr)
        #eliza.setInitial()
        #eliza_msg = eliza.respond(usr_msg)
        # result.Unique_Eliza.eliza will return the eliza binary from db

        input_message = request.get_json()
        user_msg = input_message['userMessage']


        #print(eliza_msg, file=sys.stderr)
        print(session.get('id'), file=sys.stderr)
        
        pickled_eliza = session.get('eliza')
        eliza = pickle.loads(pickled_eliza)
        eliza_response = eliza.respond(user_msg)
        print(eliza_response, file=sys.stderr)
        print(eliza)
        print(session.sid, file=sys.stderr)

        pickled_eliza = pickle.dumps(eliza)
        session['eliza'] = pickled_eliza
        
        return {
            "message": eliza_response[0]
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


        emotions = [user.depression_score, user.anxiety_score, user.anger_score, user.disorder_score]

        index = 0
        max = 0
        maxIndex = -1
        ratings = []
        
        for elem in emotions:
            if elem > max:
                max = elem
                maxIndex = index

            index += 1

        if maxIndex == -1: # inbetween
            statement = select(InBetweenReassemblyRatings)
            result = db_session.execute(statement).all()
            ratings = [row.InBetweenReassemblyRatings.rating for row in result] 
        elif maxIndex == 0: # depression
            statement = select(DepressionReassemblyRatings)
            result = db_session.execute(statement).all()
            ratings = [row.DepressionReassemblyRatings.rating for row in result]
        elif maxIndex == 1: # anxious
            statement = select(AnxietyReassemblyRatings)
            result = db_session.execute(statement).all()
            ratings = [row.AnxietyReassemblyRatings.rating for row in result]
        elif maxIndex == 2: # anger
            statement = select(AngerReassemblyRatings)
            result = db_session.execute(statement).all()
            ratings = [row.AngerReassemblyRatings.rating for row in result]
        elif maxIndex == 3: # disorder
            statement = select(DisorderReassemblyRatings)
            result = db_session.execute(statement).all()
            ratings = [row.DisorderReassemblyRatings.rating for row in result]


        print(emotions, file=sys.stderr)
        print(ratings, file=sys.stderr)
        print(session.sid, file=sys.stderr)

        session['id'] = user.id
        eliza = Eliza()
        eliza.setInitial(emotions, ratings)
        pickled_eliza = pickle.dumps(eliza)
        session['eliza'] = pickled_eliza

        # user.id returns the user's id
        print('This is the session_id:' + str(session.get('id')), file=sys.stderr)
        
        return 'OK'


@app.route("/api/testSessionInfo")
def test_session_info():
    app.logger.info()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
