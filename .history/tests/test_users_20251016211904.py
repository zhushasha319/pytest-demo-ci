import requests

def test_get_users(login_token):
    assert login_token is not None, "未成功登录，token为空"
    url = "https://dummyjson.com/users"
    headers = {"Authorization": f"Bearer {login_token}"}
    res = requests.get(url, headers=headers)
    print("用户接口响应：", res.status_code)
    assert res.status_code == 200
