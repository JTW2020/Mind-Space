import sys
import pytest
from flask_cors import CORS
from flask import Flask, request, render_template


import json

def test_index_route():
    app = Flask(__name__)
    client = app.test_client()
    url = '/'
    response = app.test_client().get(url)
    assert response.status_code == 200

def eliza_testEliza_route():
    app = Flask(__name__)
    client = app.test_client()
    url = '/api/testEliza'

    response = client.get(url)
    assert response.status_code == 200
    #assert response.get_data() == 'Eliza has been imported and is accessible'

def test_hello_route():
    app = Flask(__name__) #instantiate flask object
    client = app.test_client()
    url = '/hello'
    response = client.get(url)
    assert response.status_code == 200

