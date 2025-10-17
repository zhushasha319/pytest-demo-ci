import requests
from utils.log_util import logger

def request_handler(method, url, **kwargs):
    method = method.lower()
    logger.info(f"请求开始: [{method.upper()}] {url}")
    if "json" in kwargs:
        logger.info(f"请求体: {kwargs['json']}")
    if "params" in kwargs:
        logger.info(f"请求参数: {kwargs['params']}")

    try:
        if method == "get":
            res = requests.get(url, **kwargs)
        elif method == "post":
            res = requests.post(url, **kwargs)
        elif method == "put":
            res = requests.put(url, **kwargs)
        elif method == "delete":
            res = requests.delete(url, **kwargs)
        else:
            raise ValueError("Unsupported HTTP method")

        logger.info(f"响应状态码: {res.status_code}")
        logger.info(f"响应内容: {res.text[:300]}")
        return res

    except Exception as e:
        logger.error(f"请求异常: {e}")
        return None
