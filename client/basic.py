import requests as r

endpoint = "http://127.0.0.1:8000/api/"

response = r.get(endpoint,  json={"title": "Hello"})

print(response.json())
