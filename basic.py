import requests as r


endpoint = "https://httpbin.org/anything"

response = r.get(endpoint, json={"query": "Hello"})
# print(response) get status code
# print(response.text) row text response
# print(response.json())
# for i, j in response.json().items():
#     print(f"{i}: {j}")
# print(response.status_code) get staus code