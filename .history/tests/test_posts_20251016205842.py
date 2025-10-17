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
    
    # 使用自定义的 request_handler 发送 POST 请求
    res = request_handler("post", url, json={
        "title": case["title"],      # 从测试数据中获取标题
        "body": case["body"],         # 从测试数据中获取正文
        "userId": case["userId"]      # 从测试数据中获取用户ID
    })
    
    # 断言: 验证响应状态码是否符合预期
    assert res.status_code == case["status_code"]
    
    # 打印响应数据(用于调试)
    print("响应数据：", res.json())
