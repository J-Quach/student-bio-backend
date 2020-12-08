import requests


post_data = {
    "firstName": "John",
    "lastName": "Do",
    "hobby": "I like to go on walks and rip dirt",
    "bio": "Im a guy that is simple and like math and NETLOGO",
    "favNum": 3
}

res = requests.post('http://127.0.0.1:5000/create_user', json=post_data)
if res.ok:
    print(res.json())