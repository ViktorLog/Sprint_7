import json

import allure
import pytest
import requests

from data import TestData
from urls import Urls


class TestCreateOrder:
    @allure.step("Отправить запрос на создание заказа")
    def create_order(self, payload):
        return requests.post(
            Urls.ORDERS_URL,
            data=json.dumps(payload),
            headers={"Content-type": "application/json"},
        )

    @allure.title("Заказ можно создать с разными вариантами цвета")
    @pytest.mark.parametrize("payload", TestData.ORDER_PAYLOADS)
    def test_create_order_returns_track(self, payload, created_order_tracks):
        response = self.create_order(payload)
        response_body = response.json()

        assert "track" in response_body
        created_order_tracks.append(response_body["track"])
        assert response.status_code == 201