# conftest.py
import pytest
import requests
import yaml
import os

@pytest.fixture(scope="session")
def login_token():
    url = "https://dummyjson.com/auth/login"
    data = {"username": "kminchelle", "password": "0lelplR"}
    res = requests.post(url, json=data)
    return res.json().get("token")
def base_url():
# 获取当前目录
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, "config.yaml")

# 读取yaml内容
    with open(config_path, encoding="utf-8") as f:
     config = yaml.safe_load(f)

    env = config["base"]["env"]
    return config["env"][env]