import requests
import json


auth_token='da3753df756792af44eb09c710cbd3a90b77f678f33e0e19431194dd9a7aeff6'
hed = {'Authorization': 'Bearer ' + auth_token}
mydata = open("data.json","r").read()


def test_create_user_status_code_201():
   response=requests.post("https://gorest.co.in/public-api/users", data=json.loads(mydata), headers=hed)
   response_body = response.json()
   assert response_body["code"] == 201
   print(response_body)


def test_new_users_name():
    response=requests.get("https://gorest.co.in/public-api/users")
    response_body =response.json
    assert len(response_body["data"]) == 4