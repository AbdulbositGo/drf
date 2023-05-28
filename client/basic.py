import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/"

response = requests.get(endpoint)

print(response.text)