import requests

def test_get_users(login_token):
    assert login_token is not None, "token 为空"
    url = "https://reqres.in/api/users?page=2"
    headers = {"Authorization": f"Bearer {login_token}"}
    res = requests.get(url, headers=headers)
    print("用户接口响应：", res.status_code)
    print(res.json())
    assert res.status_code == 200
