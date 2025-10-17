import requests

def test_get_users(base_url):
    url = f"{base_url}/users"
    res = requests.get(url)
    print("用户接口响应：", res.status_code)
    print(res.json()[0])
    assert res.status_code == 200
