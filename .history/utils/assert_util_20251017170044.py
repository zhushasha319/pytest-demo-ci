from utils.log_util import logger

def assert_response(res, expected_status):
    """
    统一断言接口响应
    """
    try:
        assert res is not None, "响应为空"
        assert res.status_code == expected_status, f"状态码错误: {res.status_code}"
        logger.info(f"✅ 断言通过: 状态码 = {expected_status}")
    except AssertionError as e:
        logger.error(f"❌ 断言失败: {e}")
        raise e
