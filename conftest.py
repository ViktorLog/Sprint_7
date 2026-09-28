import pytest
import requests

from helpers import (
    delete_courier,
    generate_courier_data,
    register_new_courier_and_return_login_password,
)
from urls import Urls


@pytest.fixture
def courier_data():
    data = generate_courier_data()
    yield data
    delete_courier(data["login"], data["password"])


@pytest.fixture
def registered_courier():
    login, password, first_name = (
        register_new_courier_and_return_login_password()
    )
    courier = {
        "login": login,
        "password": password,
        "firstName": first_name,
    }

    yield courier

    delete_courier(login, password)


@pytest.fixture
def created_order_tracks():
    tracks = []
    yield tracks

    for track in tracks:
        requests.put(Urls.CANCEL_ORDER_URL, params={"track": track})
