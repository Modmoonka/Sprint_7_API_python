import allure
from api import Api

class TestOrderList:

    @allure.title('Проверь, что в тело ответа возвращается список заказов')
    def test_get_order_list(self):
        response = Api.get_order_list()
        assert response.status_code == 200
        assert "orders" in response.json() and type(response.json()['orders']) == list and "orders" is not None
