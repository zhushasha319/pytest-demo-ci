import requests

def test_login_success():
    url = "https://reqres.in/api/login"
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    res = requests.post(url, json=data)
    assert res.status_code == 200
    assert "token" in res.json()

def test_login_fail():
    url = "https://reqres.in/api/login"
    data = {"email": "wrong.email", "password": "wrongpass"}
    res = requests.post(url, json=data)
    assert res.status_code == 400
    assert "error" in res.json()
