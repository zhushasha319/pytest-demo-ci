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
    res = requests.post(url, json=data)
    token = res.json().get("token")
    return token

@pytest.fixture(scope="session")
def base_url():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, "config.yaml")

    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    env = config["base"]["env"]  # dev/test
    return config["env"][env]