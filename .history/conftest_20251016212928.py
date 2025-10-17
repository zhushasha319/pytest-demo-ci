# conftest.py
import pytest
import requests
import yaml
import os


@pytest.fixture(scope="session")
def login_token():
    """
    登录 dummyjson.com 获取 token
    """
    url = "https://dummyjson.com/auth/login"
    data = {
    "username": "atuny0",
    "password": "9uQFF1Lh"
     }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        res = requests.post(url, json=data, headers=headers, timeout=10)
        print("登录响应状态码：", res.status_code)
        print("登录响应内容：", res.text)
        if res.status_code == 200:
            token = res.json().get("token")
            print("✅ 获取到 token:", token[:20] + "..." if token else "None")
            return token
        else:
            print(f"❌ 登录失败，状态码：{res.status_code}，响应内容：{res.text}")
            return None
    except Exception as e:
        print(f"❌ 登录请求异常: {e}")
        return None
    
@pytest.fixture(scope="session")
def base_url():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, "config.yaml")

    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    env = config["base"]["env"]  # dev/test
    return config["env"][env]