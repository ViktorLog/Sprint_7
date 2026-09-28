class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    COURIER_URL = f"{BASE_URL}/api/v1/courier"
    COURIER_LOGIN_URL = f"{COURIER_URL}/login"
    ORDERS_URL = f"{BASE_URL}/api/v1/orders"
    CANCEL_ORDER_URL = f"{ORDERS_URL}/cancel"
