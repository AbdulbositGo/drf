import requests as r

endpoint = f"http://127.0.0.1:8000/api/products/"

data = {
    "title": "Product 51",
    "content": "This is some informations about Product 51",
    "price:": 51*11
}

response = r.post(endpoint, json=data)

print(response.json())

