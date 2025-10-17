import pytest
import yaml
import os
from utils.request_handler import request_handler
from utils.assert_util import assert_response
#展开数据
def load_data():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(root, "data", "posts_data.yaml")
    with open(data_path, encoding="utf-8") as f:
        return yaml.safe_load(f)
#多次测试，数据为load_data(),变成case→
@pytest.mark.parametrize("case", load_data())
def test_create_post(base_url, case):
    url = f"{base_url}/posts"
    res = request_handler("post", url, json={
        "title": case["title"],
        "body": case["body"],
        "userId": case["userId"]
    })
    assert_response(res, case["status_code"])

