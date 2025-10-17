import requests

def test_get_users(login_token):
    assert login_token is not None
    # 带 token 发请求
    url = "https://dummyjson.com/users"
    headers = {"Authorization": f"Bearer {login_token}"}
    res = requests.get(url, headers=headers)
    assert res.status_code == 200
    print("用户数据：", res.json())