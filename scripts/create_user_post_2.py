import requests


post_data = {
    "firstName": "Jotaro",
    "lastName": "Star",
    "hobby": "ORAORAORAORAORAOROARAORAORAORAORAOROA",
    "bio": "ORAORAORAORAORAOROARAORAORAORAORAOROAORAORAORAORAORAOROARAORAORAORAORAOROAORAORAORAORAORAOROARAORAORAORAORAOROAORAORAORAORAORAOROARAORAORAORAORAOROAORAORAORAORAORAOROARAORAORAORAORAOROA",
    "favNum": 55
}

res = requests.post('https://student-bio-backend.herokuapp.com/create_user', json=post_data)
if res.ok:
    print(res.json())