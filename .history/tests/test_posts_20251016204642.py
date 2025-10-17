import pytest
import yaml
import os
from utils.request_handler import request_handler

# 读取测试数据
def load_data():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(root_dir, "data", "posts_data.yaml")
    with open(data_path, encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize("case", load_data())
def test_create_post(base_url, case):
    url = f"{base_url}/posts"
    res = request_handler("post", url, json={
        "title": case["title"],
        "body": case["body"],
        "userId": case["userId"]
    })
    assert res.status_code == case["status_code"]
    print("响应数据：", res.json())
