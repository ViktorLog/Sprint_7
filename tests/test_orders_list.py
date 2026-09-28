import allure
import requests

from urls import Urls


class TestOrdersList:
    @allure.step("Отправить запрос на получение списка заказов")
    def get_orders(self):
        return requests.get(Urls.ORDERS_URL)

    @allure.title("Ответ содержит список заказов")
    def test_get_orders_returns_orders_list(self):
        response = self.get_orders()
        response_body = response.json()

        assert response.status_code == 200
        assert "orders" in response_body
        assert type(response_body["orders"]) == list
