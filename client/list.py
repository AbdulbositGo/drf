import requests as r
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
username =  input("Username: ")
password = getpass()

aouth_response = r.post(auth_endpoint, json={'username': username, "password": password})
print(aouth_response.json())

if aouth_response.status_code == 200:
    TOKEN = aouth_response.json().get('token')

    headers = {
        'Authorization': f"Token {TOKEN}"
    }

    endpoint = f"http://127.0.0.1:8000/api/products/"
    response = r.get(endpoint, headers=headers)
    print(response.json())
