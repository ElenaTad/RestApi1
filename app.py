import requests


Base_URL = 'https://gorest.co.in/'


response = requests.get(f"{Base_URL}//public-api/users")
print(response.json())

print(response.status_code)