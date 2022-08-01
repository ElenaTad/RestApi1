import requests

auth_token='da3753df756792af44eb09c710cbd3a90b77f678f33e0e19431194dd9a7aeff6'
hed = {'Authorization': 'Bearer ' + auth_token}



     # To take an ID of user to delete
def test_get_users():

     response=requests.get("https://gorest.co.in/public-api/users/")
     response_body=response.json()
     print(response_body)
     assert response_body["code"]==200



def test_delete_user():

    response=requests.delete("https://gorest.co.in/public-api/users/3393", headers=hed)
    response_body = response.json()
    print(response_body)
    assert response_body["code"] == 204


def test_get_deleted_user():

     response=requests.get("https://gorest.co.in/public-api/users/3393",headers=hed)
     response_body = response.json()
     print(response_body)
     assert response_body["code"] == 200


































