import pytest
import requests

@pytest.mark.parametrize("title,body,userId,status_code", [
    ("pytest test 1", "body text 1", 1, 201),
    ("pytest test 2", "body text 2", 2, 201),
])
def test_create_post(title, body, userId, status_code):
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"title": title, "body": body, "userId": userId}
    res = requests.post(url, json=data)
    print(res.json())
    assert res.status_code == status_code
