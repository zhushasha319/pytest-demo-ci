# test_login.py
import requests

def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    res = requests.get(url)
    assert res.status_code == 200
