
def test_get_users(login_token):
     url = "https://reqres.in/api/users?page=2"
     res = requests.get(url)
     assert res.status_code == 200
     print(f"使用 token：{login_token}")