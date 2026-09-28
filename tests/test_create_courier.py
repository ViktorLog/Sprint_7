import allure
import pytest
import requests

from data import ResponseMessages
from urls import Urls


class TestCreateCourier:
    @allure.step("Отправить запрос на создание курьера")
    def create_courier(self, courier_data):
        return requests.post(Urls.COURIER_URL, data=courier_data)

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier_data):
        response = self.create_courier(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_returns_error(self, courier_data):
        first_response = self.create_courier(courier_data)
        second_response = self.create_courier(courier_data)

        assert first_response.status_code == 201
        assert second_response.status_code == 409
        assert second_response.json()["message"] == (
            ResponseMessages.COURIER_ALREADY_EXISTS
        )

    @allure.title("Для создания курьера нужны обязательные поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field_returns_error(
        self,
        courier_data,
        missing_field,
    ):
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["firstName"],
        }
        del payload[missing_field]

        response = self.create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == (
            ResponseMessages.NOT_ENOUGH_CREATION_DATA
        )
