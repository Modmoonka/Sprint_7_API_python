import pytest
import allure
from api import Api


class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        [],          # пустой массив — допустимо
        None         # поле не передаётся — тоже допустимо
    ])
    
    @allure.title('Создаём заказ с цветами: {color}')
    def test_create_order_with_color(self, color):
        order_resp = Api.create_order(color)
        
        # Проверяем успешный статус
        assert order_resp.status_code == 201
        
        # Проверяем наличие track в ответе
        assert "track" in order_resp.json()

