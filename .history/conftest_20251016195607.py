# conftest.py
import pytest
import requests

@pytest.fixture(scope="session")
def login_token():
     url = "https://reqres.in/api/login"
     data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
     res = requests.post(url,json=data)
     token = res.json().get('token')
     return token


@pytest.mark.parametrize("email,password,status_code", [
    ("eve.holt@reqres.in", "cityslicka", 200),
    ("wrong.email", "wrongpass", 400)
])
def test_login(email, password, status_code):
    url = "https://reqres.in/api/login"
    res = requests.post(url, json={"email": email, "password": password})
    assert res.status_code == status_code
