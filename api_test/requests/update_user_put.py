import json
import requests


auth_token='da3753df756792af44eb09c710cbd3a90b77f678f33e0e19431194dd9a7aeff6'
hed = {'Authorization': 'Bearer ' + auth_token}

payload={
    "name":"Allasani Peddana",
    "email":"allasani.peddana@15ce.com",
    "status":"active"
    
}


#Create a new user
resp=requests.patch("https://gorest.co.in/public-api/users", data=payload, headers=hed)
print(resp)
print(resp.json())

