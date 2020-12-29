import requests


post_data = {
    "firstName": "Jonah",
    "lastName": "Nguyen",
    "hobby": "Gamer girl",
    "bio": "Best audition player ever",
    "favNum": 8
}

res = requests.post('http://127.0.0.1:5000/create_user', json=post_data)
if res.ok:
    print(res.json())