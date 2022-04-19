import pytest
import sys
import os
import json
import flask
import requests
sys.path.append(os.path.abspath(os.path.join('..', 'server')))

def test_my_client(httpserver):
    httpserver.expect_request("localhost:5000/hello").respond_with_json({"message":"Hello there user!","sender": "Eliza"})
    assert requests.get(httpserver.url_for("/hello")).json() == {"message":"Hello there user!","sender": "Eliza"}

