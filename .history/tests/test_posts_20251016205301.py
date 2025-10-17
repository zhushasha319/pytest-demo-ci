import pytest
import yaml
import os
from utils.request_handler import request_handler

# 读取测试数据
def load_data():
    # 获取当前文件的父目录的父目录(即项目根目录)
    # __file__ 是当前文件的路径: d:\桌面\pytest_demo\tests\test_posts.py
    # os.path.dirname 第一次: d:\桌面\pytest_demo\tests
    # os.path.dirname 第二次: d:\桌面\pytest_demo (项目根目录)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 构建数据文件的完整路径
    # 结果: d:\桌面\pytest_demo\data\posts_data.yaml
    data_path = os.path.join(root_dir, "data", "posts_data.yaml")
    
    # 打开并读取 YAML 文件
    with open(data_path, encoding="utf-8") as f:
        return yaml.safe_load(f)  # 解析 YAML 并返回 Python 对象(通常是列表或字典)

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
