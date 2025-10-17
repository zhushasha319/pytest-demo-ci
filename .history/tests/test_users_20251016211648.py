import requests

def test_get_users(login_token):
    assert login_token is not None, "未获取到 token"
    url = "https://dummyjson.com/users"
    headers = {"Authorization": f"Bearer {login_token}"}
    res = requests.get(url, headers=headers)
    print("用户接口响应：", res.status_code)
    print(res.json())
    assert res.status_code == 200
