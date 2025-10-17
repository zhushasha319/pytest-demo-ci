# conftest.py
import pytest
import requests
import yaml
import os
@pytest.fixture(scope="session")
def login_token():
     url = "https://reqres.in/api/login"
     data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
     res = requests.post(url,json=data)
     token = res.json().get('token')
     return token
def base_url():
     root_dir = os