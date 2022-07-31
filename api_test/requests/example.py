import requests
import json

def test_get_user_by_id():
    response=requests.get("https://gorest.co.in/public-api/users/3746")
    print(response.url)
    print(response.status_code)