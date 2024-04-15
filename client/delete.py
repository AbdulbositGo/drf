import requests as r

pk = input("Enter a product pk: ")

try:
    pk = int(pk)
except ValueError as e:
    print(e)

endpoint = f"http://127.0.0.1:8000/api/products/{pk}/delete"

response = r.delete(endpoint)

print(response.status_code)
