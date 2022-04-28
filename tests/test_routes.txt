import json
import sys
import os
import pytest
from flask_cors import CORS
from flask import Flask, request, render_template

sys.path.append(os.path.abspath(os.path.join('..', 'server')))

from app import app

def test_index_route():
    # app = Flask(__name__)
    client = app.test_client()
    url = '/'
    response = app.test_client().get(url)
    print(response.status_code)
    assert response.status_code == 200


def eliza_testEliza_route():
    # app = Flask(__name__)
    client = app.test_client()
    url = '/api/testEliza'

    response = client.get(url)
    assert response.status_code == 200
    assert response.get_data() == 'Eliza has been imported and is accessible'


def test_hello_route():
    # app = Flask(__name__)  # instantiate flask object
    client = app.test_client()
    url = '/hello'
    response = client.get(url)
    print(response.status_code)
    assert response.status_code == 200

def test_message_eliza():
    client = app.test_client()
    url ='/api/msgEliza'
    json ={
        "user": "you",
        "message": "hello Eliza!"
    }
    response = client.post(url, json)
    print(response.status_code)
    assert response.status_code == 200

def test_inintalMsgEliza():
    client = app.test_client()
    url = '/api/initialMsgEliza'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json == json.loads('{"message":"How do you do.  Please tell me your problem."}')

def test_api_test_Eliza():
    client = app.test_client()
    url='/api/test'
    response = client.get(url)
    assert response.status_code == 200
