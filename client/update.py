import requests as r
import random

endpoint = "http://127.0.0.1:8000/api/products/51/update"
data = {
    "title": "Product 51",
    "content": "This is some informations about Product 51",
    "price:": 51*11
}
response = r.put(endpoint, json=data)

print(response.json())
