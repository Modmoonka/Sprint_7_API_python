import pytest
from api import Api
from data import *

class TestCreateOrder:

    @pytest.mark.parametrize("color", [
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
    [],          # без цвета (пустой массив)
    None         # вообще не передавать поле "color"
])
    @allure.title('Проверь, что, когда создаёшь заказ: можно указать один из цветов — BLACK или GREY')
    def test_create_order_with_color(self, color):
        order_resp = Api.create_order(color)
        assert order_resp.status_code == 201
        assert "track" in order_resp.json()