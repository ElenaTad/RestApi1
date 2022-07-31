import requests

resp=requests.delete("https://gorest.co.in/public-api/users/59")
print(resp.status_code)
assert resp.status_code==204,"User deletion failed"