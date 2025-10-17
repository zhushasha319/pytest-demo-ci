# test_login.py
import requests
import pytest

@pytest.mark.parametrize("email,password,status_code", [
    ("eve.holt@reqres.in", "cityslicka", 200),
    ("wrong.email", "wrongpass", 400)
])
def test_login(email, password, status_code):
    url = "https://reqres.in/api/login"
    res = requests.post(url, json={"email": email, "password": password})
    assert res.status_code == status_code
