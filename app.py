import requests


Base_URL = 'https://gorest.co.in/'


response = requests.get(f"{Base_URL}//public-api/users")
response_body=response.json()
print(response_body["code"])
print(response.url)

