import random
import string

import requests

from urls import Urls


def generate_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def generate_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }


def register_new_courier_and_return_login_password():
    courier_data = generate_courier_data()
    response = requests.post(Urls.COURIER_URL, data=courier_data)

    if response.status_code == 201:
        return [
            courier_data["login"],
            courier_data["password"],
            courier_data["firstName"],
        ]

    return []


def delete_courier(login, password):
    login_response = requests.post(
        Urls.COURIER_LOGIN_URL,
        data={"login": login, "password": password},
    )

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]
        requests.delete(f"{Urls.COURIER_URL}/{courier_id}")
