import json
import sys
import os
import pytest

import requests

sys.path.append(os.path.abspath(os.path.join('..', 'server')))

session = requests.Session()


def test_index():
    session.trust_env = False
    endpoint = '/'
    s = session.get('http://localhost:5000' + endpoint)
    # print('This is the status: ' + str(s.status_code))
    assert s.status_code == 200


def test_hello_endpoint():
    session.trust_env = False
    endpoint = '/hello'
    s = session.get('http://localhost:5000' + endpoint)
    assert s.status_code == 200

def test_testEliza_endpoint():
    session.trust_env = False
    endpoint = '/api/testEliza'
    s = session.get('http://localhost:5000' + endpoint)
    assert s.status_code == 200


def test_initialMsgEliza_endpoint():
    session.trust_env = False
    endpoint = '/api/initialMsgEliza'
    s = session.get('http://localhost:5000' + endpoint)
    assert s.status_code == 200
#


# def eliza_testEliza_route():
#    # app = Flask(__name__)
#    client = app.test_client()
#    url = '/api/testEliza'
#
#    response = client.get(url)
#    assert response.status_code == 200
#    assert response.get_data() == 'Eliza has been imported and is accessible'
#
#
#
# def test_message_eliza():
#    client = app.test_client()
#    url ='/api/msgEliza'
#    json ={
#        "user": "you",
#        "message": "hello Eliza!"
#    }
#    response = client.post(url, json)
#    print(response.status_code)
#    assert response.status_code == 200
#
# def test_inintalMsgEliza():
#    client = app.test_client()
#    url = '/api/initialMsgEliza'
#    response = client.get(url)
#    assert response.status_code == 200
#    assert response.json == json.loads('{"message":"How do you do.  Please tell me your problem."}')
#
# def test_api_test_Eliza():
#    client = app.test_client()
#    url= '/api/test'
#    response = client.get(url)
#    assert response.status_code == 200
