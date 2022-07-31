import requests

response = requests.get('https://gorest.co.in/')
print(response.url)

print(response.status_code)

print(response.ok)
