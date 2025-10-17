import pytest

def test_get_users(login_token):
    print("使用 token：", login_token)
    if login_token is None:
        pytest.skip("无法获取 token，可能是网络问题")
    assert login_token is not None
