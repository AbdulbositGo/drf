import requests as r

endpoint = f"http://127.0.0.1:8000/api/products/53/delete"

response = r.delete(endpoint)

print(response.status_code)
