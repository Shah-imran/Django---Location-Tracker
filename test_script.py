import random
import requests
from threading import Thread

user_token = "4cd8d412a77049066ea2ae98fd33d509a761035b"
headers = {
    "Authorization": f"Token {user_token}"
}

def my_task():
    latitude = round(random.uniform(24.85, 24.9), 6)
    longitude = round(random.uniform(91.85, 91.9), 6)

    print(latitude, longitude)

    post_data = {
        "latitude": latitude,
        "longitude": longitude
    }

    request = requests.post(
        "http://localhost:8000/api/locations/create/",
        data=post_data,
        headers=headers
    )

    response = request.json()

    print(response)

for i in range(100):
    th = Thread(target=my_task)
    th.start()