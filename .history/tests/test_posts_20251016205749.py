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
# 这个装饰器会:
# 1. 调用 load_data() 获取测试数据列表
# 2. 对列表中的每个元素,运行一次 test_create_post 函数
# 3. 每次运行时,将当前元素赋值给 case 参数

def test_create_post(base_url, case):
    # base_url: 来自 conftest.py 中的 fixture,提供基础 URL
    # case: 当前测试用例的数据(从 YAML 文件中读取)
    
    # 构建完整的 API 地址
    # 例如: https://jsonplaceholder.typicode.com/posts
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
