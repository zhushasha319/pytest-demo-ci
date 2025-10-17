import pytest
import allure
from utils.request_handler import request_handler
from utils.assert_util import assert_response
from utils.log_util import logger

@allure.feature("依赖链示例")
@allure.story("登录 → 创建帖子 → 删除帖子")
class TestDependencyDemo:

    @allure.title("Step1: 创建帖子")
    def test_create_post(self, base_url, login_token):
        url = f"{base_url}/posts"
        body = {
            "title": "依赖测试",
            "body": "模拟 token 测试",
            "userId": 1
        }
        headers = {"Authorization": f"Bearer {login_token}"}
        res = request_handler("post", url, json=body, headers=headers)
        assert_response(res, 201)
        self.post_id = res.json().get("id")
        logger.info(f"✅ 创建帖子成功 id={self.post_id}")

    @allure.title("Step2: 删除帖子")
    def test_delete_post(self, base_url, login_token):
        post_id = getattr(self, "post_id", 1)
        url = f"{base_url}/posts/{post_id}"
        headers = {"Authorization": f"Bearer {login_token}"}
        res = request_handler("delete", url, headers=headers)
        assert_response(res, 200)
        logger.info(f"✅ 删除帖子成功 id={post_id}")
