import requests as r

endpoint = f"http://127.0.0.1:8000/api/products/"

response = r.get(endpoint)

print(response.json())
