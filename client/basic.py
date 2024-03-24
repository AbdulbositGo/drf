import requests as r


# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

response = r.get(endpoint,  json={"query": "Hello"})

# print(response) get status code
# print(response.text) row text response
# print(response.json())
# for i, j in response.json().items():
#     print(f"{i}: {j}")
# print(response.status_code) get staus code

# print(response.json()['message'])

print(response.json())