import pytest
import yaml
import os
from utils.request_handler import request_handler

def load_data():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "data", "posts_data.yaml"), encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize("case", load_data())
def test_create_post(base_url, case):
    url = f"{base_url}/posts"
    res = request_handler("post", url, json={
        "title": case["title"],
        "body": case["body"],
        "userId": case["userId"]
    })
    print("响应数据：", res.json())
    assert res.status_code == case["status_code"]
