# conftest.py
import pytest
import requests
import yaml
import os


@pytest.fixture(scope="session")
def login_token():
    url = "https://dummyjson.com/auth/login"
    data = {
        "username": "kminchelle",
        "password": "0lelplR"
    }
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, json=data, headers=headers)
    # 打印调试看看响应内容
    print("Login response:", res.status_code, res.json())
    token = res.json().get("accessToken")  # 注意字段名
    return token

@pytest.fixture(scope="session")
def base_url():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, "config.yaml")

    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    env = config["base"]["env"]  # dev/test
    return config["env"][env]