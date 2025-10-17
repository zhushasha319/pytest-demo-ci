# conftest.py
import pytest
import requests
import yaml
import os
from utils.log_util import logger

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
    """
    模拟登录成功，生成假 token
    （真实接口如 DummyJSON、ReqRes 已不稳定）
    """
    logger.info("🔑 模拟登录成功")
    token = "fake-token-123456"
    return token

@pytest.fixture()
def create_temp_user():
    """创建测试用户并在用例结束后删除"""
    logger.info("👤 创建测试用户")
    res = requests.post("https://dummyjson.com/users/add", json={"firstName": "pytestUser"})
    user_id = res.json().get("id")

    yield user_id   # 这里是用例执行阶段

    # 后置部分在 yield 后执行
    logger.info(f"🧹 删除测试用户 id={user_id}")
    requests.delete(f"https://dummyjson.com/users/{user_id}")
