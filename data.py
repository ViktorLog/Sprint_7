class TestData:
    ORDER_DATA = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, улица Тестовая, 1",
        "metroStation": 4,
        "phone": "+7 999 000 00 01",
        "rentTime": 5,
        "deliveryDate": "2030-12-31",
        "comment": "Позвонить перед доставкой",
    }

    ORDER_BLACK = ORDER_DATA.copy()
    ORDER_BLACK["color"] = ["BLACK"]

    ORDER_GREY = ORDER_DATA.copy()
    ORDER_GREY["color"] = ["GREY"]

    ORDER_BOTH_COLORS = ORDER_DATA.copy()
    ORDER_BOTH_COLORS["color"] = ["BLACK", "GREY"]

    ORDER_PAYLOADS = [
        ORDER_BLACK,
        ORDER_GREY,
        ORDER_BOTH_COLORS,
        ORDER_DATA.copy(),
    ]


class ResponseMessages:
    COURIER_ALREADY_EXISTS = (
        "Этот логин уже используется. Попробуйте другой."
    )
    NOT_ENOUGH_CREATION_DATA = (
        "Недостаточно данных для создания учетной записи"
    )
    NOT_ENOUGH_LOGIN_DATA = "Недостаточно данных для входа"
    COURIER_NOT_FOUND = "Учетная запись не найдена"
