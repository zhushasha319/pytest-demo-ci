import requests

def request_handler(method, url, **kwargs)://   """
    通用请求函数：支持 GET / POST / PUT / DELETE
    """
    method = method.lower()
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
            raise ValueError("Unsupported method")

        return res
    except Exception as e:
        print(f"❌ 请求异常：{e}")
        return None
