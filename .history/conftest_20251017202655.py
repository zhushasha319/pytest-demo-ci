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
    """使用 ReqRes 模拟登录，返回 token"""
    url = "https://reqres.in/api/login"
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, json=data, headers=headers)
    logger.info(f"登录响应: {res.status_code} {res.text}")
    token = res.json().get("token")
    if token:
        logger.info(f"✅ 登录成功，token={token}")
    else:
        pytest.skip("❌ 登录失败，未返回 token")
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
