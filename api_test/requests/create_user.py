import json
import requests


auth_token='da3753df756792af44eb09c710cbd3a90b77f678f33e0e19431194dd9a7aeff6'
hed = {'Authorization': 'Bearer ' + auth_token}

mydata = open("data.json","r").read()



resp=requests.post("https://gorest.co.in/public-api/users", data=json.loads(mydata), headers=hed)
print(resp)
print(resp.json())

def test_status_code_201():
    response = requests.get('https://gorest.co.in/public-api/users')
    response_body = response.json()
    assert response_body["code"] == 201


#Get the new user
new_user=requests.get("https://gorest.co.in/public-api/users")
print(new_user,["Tenali Ramakhna"])







