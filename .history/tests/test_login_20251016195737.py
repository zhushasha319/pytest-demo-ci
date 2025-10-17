# test_login.py
import requests

def test_get_users():
    url = "https://reqres.in/api/users?page=2"
    res = requests.get(url)
    assert res.status_code == 200

    
@pytest.mark.parametrize("email,password,status_code", [
    ("eve.holt@reqres.in", "cityslicka", 200),
    ("wrong.email", "wrongpass", 400)
])
def test_login(email, password, status_code):
    url = "https://reqres.in/api/login"
    res = requests.post(url, json={"email": email, "password": password})
    assert res.status_code == status_code
