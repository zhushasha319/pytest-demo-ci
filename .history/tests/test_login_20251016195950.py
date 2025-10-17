# test_login.py
import requests
import pytest

# @pytest.mark.parametrize 是参数化装饰器
# 它会用不同的参数组合多次运行同一个测试函数

@pytest.mark.parametrize("email,password,status_code", [
    ("eve.holt@reqres.in", "cityslicka", 200),
    ("wrong.email", "wrongpass", 400)
])
def test_login(email, password, status_code):
    url = "https://reqres.in/api/login"
    res = requests.post(url, json={"email": email, "password": password})
    assert res.status_code == status_code
