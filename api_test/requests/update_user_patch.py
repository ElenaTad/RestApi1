import requests
import json

auth_token = 'da3753df756792af44eb09c710cbd3a90b77f678f33e0e19431194dd9a7aeff6'
hed = {'Authorization': 'Bearer ' + auth_token}

payload = {
    "name": "Anahit Poghosyan",
    "status": "inactive"

}
# For taking ID of user to update
def test_get_users():
    response = requests.get("https://gorest.co.in/public-api/users?id=3761")
    response_body = response.json()
    print(response_body)
    assert response_body["code"] == 200


def test_update_user_patch():
    response = requests.patch("https://gorest.co.in/public-api/users/3761", data=payload, headers=hed)
    response_body = response.json()
    assert response_body["code"] == 200