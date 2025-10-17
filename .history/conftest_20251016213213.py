# conftest.py
import pytest
import requests
import yaml
import os


import pytest
import requests

@pytest.fixture(scope="session")
def login_token():
    """
    登录 reqres.in 获取 token
    """
    url = "https://reqres.in/api/login"
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, json=data, headers=headers)
    print("登录响应：", res.status_code, res.text)

    if res.status_code == 200:
        token = res.json().get("token")
        print("✅ 获取到 token:", token)
        return token
    else:
        print("❌ 登录失败，状态码：", res.status_code)
        return None
 
@pytest.fixture(scope="session")
def base_url():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, "config.yaml")

    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    env = config["base"]["env"]  # dev/test
    return config["env"][env]