import json
import requests


auth_token='da3753df756792af44eb09c710cbd3a90b77f678f33e0e19431194dd9a7aeff6'
hed = {'Authorization': 'Bearer ' + auth_token}

payload={
    "name":"Ani Petrosyan",
    "email":"ait@15ce.com",
    "gender":"female",
    "status":"active"
    
}

# For taking ID of user to update
def test_get_users():

     response=requests.get("https://gorest.co.in/public-api/users/3759")
     response_body=response.json()
     print(response_body)
     assert response_body["code"]==200


def test_update_user_put():

     response=requests.put("https://gorest.co.in/public-api/users/3759", data=payload, headers=hed)
     response_body=response.json()
     print(response_body)
     assert response_body["code"] == 200

def test_users_updated_info():

    response=requests.get("https://gorest.co.in/public-api/users/3396")
    response_body=response.json()
    print(response_body)
    assert response_body["data","name"] == "Ani"



#