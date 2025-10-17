# conftest.py
import pytest
import requests
import yaml
import os

@pytest.fixture(scope="session")
def base_url():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, "config.yaml")

    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    env = config["base"]["env"]  # dev/test
    return config["env"][env]

@pytest.fixture(scope="session")
def login_token():
    """全局登录 fixture"""
    logger.info("🔑 开始执行登录前置操作")
    url = "https://dummyjson.com/auth/login"
    data = {"username": "kminchelle", "password": "0lelplR"}
    res = requests.post(url, json=data)
    token = res.json().get("token")
    if not token:
        pytest.skip("❌ 登录失败，跳过后续测试")
    logger.info(f"✅ 登录成功，token={token[:10]}...")
    return token