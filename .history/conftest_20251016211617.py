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
    data = {"username": "kminchelle", "password": "0lelplR"}
    headers = {"Content-Type": "application/json"}

    res = requests.post(url, json=data, headers=headers)
    print("登录响应：", res.status_code, res.text)

    # 确保返回正确字段
    if res.status_code == 200:
        try:
            token = res.json().get("token")
            print("获取到 token：", token[:20] + "..." if token else "None")
            return token
        except Exception as e:
            print("解析响应异常：", e)
            return None
    else:
        print("登录失败，状态码：", res.status_code)
        return None

@pytest.fixture(scope="session")
def base_url():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, "config.yaml")

    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    env = config["base"]["env"]  # dev/test
    return config["env"][env]