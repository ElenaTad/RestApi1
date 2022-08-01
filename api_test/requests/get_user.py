import requests
import json

Base_URL = "https://gorest.co.in/"

def get_all_users():

  response = requests.get(f'{Base_URL}/public-api/users')
  assert response.status_code == 200



def  test_response_content_type_equals_json():

     response = requests.get('https://gorest.co.in/public-api/users')
     assert response.headers["Content-Type"] =="application/json; charset=utf-8", "Wrong Content-Type"

def test_users_info():

    response = requests.get('https://gorest.co.in/public-api/users/13')
    response_body = response.json()
    assert response_body["code"] == 200

def tests_number_items_in_Data():

    response = requests.get('https://gorest.co.in/public-api/users/')
    response_body = response.json()
    assert len(response_body["data"]) == 10


def test_status_code_404():
    response = requests.get("https://gorest.co.in/public-api/users/111111111")
    response_body = response.json()
    assert response_body["code"]==404



























































