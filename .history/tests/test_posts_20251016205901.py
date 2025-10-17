import pytest
import yaml
import os
from utils.request_handler import request_handler

import yaml, os

def load_data():
    root = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(root, "data", "posts_data.yaml"), encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data


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
