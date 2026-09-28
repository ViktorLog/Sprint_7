import allure
import pytest
import requests

from data import ResponseMessages
from helpers import generate_random_string
from urls import Urls


class TestLoginCourier:
    @allure.step("Отправить запрос на авторизацию курьера")
    def login_courier(self, credentials):
        return requests.post(Urls.COURIER_LOGIN_URL, data=credentials)

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, registered_courier):
        response = self.login_courier(
            {
                "login": registered_courier["login"],
                "password": registered_courier["password"],
            }
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Для авторизации нужны обязательные поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_without_required_field_returns_error(
        self,
        registered_courier,
        missing_field,
    ):
        credentials = {
            "login": registered_courier["login"],
            "password": registered_courier["password"],
        }
        del credentials[missing_field]

        response = self.login_courier(credentials)

        assert response.status_code == 400
        assert response.json()["message"] == (
            ResponseMessages.NOT_ENOUGH_LOGIN_DATA
        )

    @allure.title("Неверный логин или пароль возвращает ошибку")
    @pytest.mark.parametrize("invalid_field", ["login", "password"])
    def test_login_with_invalid_credentials_returns_error(
        self,
        registered_courier,
        invalid_field,
    ):
        credentials = {
            "login": registered_courier["login"],
            "password": registered_courier["password"],
        }
        credentials[invalid_field] = generate_random_string(10)

        response = self.login_courier(credentials)

        assert response.status_code == 404
        assert response.json()["message"] == (
            ResponseMessages.COURIER_NOT_FOUND
        )

    @allure.title("Несуществующий курьер не может авторизоваться")
    def test_login_nonexistent_courier_returns_error(self):
        response = self.login_courier(
            {
                "login": generate_random_string(10),
                "password": generate_random_string(10),
            }
        )

        assert response.status_code == 404
        assert response.json()["message"] == (
            ResponseMessages.COURIER_NOT_FOUND
        )
