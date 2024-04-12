import requests as r
import random

endpoint = f"http://127.0.0.1:8000/api/products/50/"

response = r.get(endpoint)

print(response.json())
