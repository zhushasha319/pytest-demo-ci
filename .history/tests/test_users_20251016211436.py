import requests

def test_get_users(login_token):
    import pytest
    if login_token is None:
        pytest.skip("无法获取 token，可能是网络或接口问题，跳过测试")
    # 带 token 发请求
    url = "https://dummyjson.com/users"
    headers = {"Authorization": f"Bearer {login_token}"}
    res = requests.get(url, headers=headers)
    assert res.status_code == 200
    print("用户数据：", res.json())