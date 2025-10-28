from data import *
import pytest
from api import Api

class TestCreateCourier:

    @allure.title('Проверяем, что курьера можно создать')
    @allure.description('запрос возвращает {"ok":true}')
    def test_register_courier_return_ok(self):
        data = courier_data()
        login_pass, response = Api.register_new_courier_and_return_login_password(data)
        assert response.status_code == 201 and response.json() == {'ok': True}


    @allure.title('Проверка: если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_register_two_identical_couriers(self):
        data = courier_data()
        login_pass, response_1 = Api.register_new_courier_and_return_login_password(data)
        assert response_1.status_code == 201
        assert response_1.json() == {'ok': True}
        login_pass_2, response_2 = Api.register_new_courier_and_return_login_password(data)
        assert response_2.status_code == 409
        assert response_2.json()['message'] == ErrorText.RegistrationErrorText.LOGIN_USED_ERROR_TEXT


    @pytest.mark.parametrize("invalid_data", [registration_data_without_login(), registration_data_without_password()])
    @allure.title('Проверяем, что запрос возвращает ошибку, если нет заполнения одного из обязательных полей')
    def test_register_courier_without_mandatory_info_returns_400(self, invalid_data):
        _, reg_response = Api.register_new_courier_and_return_login_password(invalid_data)
        assert reg_response.status_code == 400
        assert "message" in reg_response.json()
        assert reg_response.json()["message"] == ErrorText.RegistrationErrorText.NOT_ENOUGH_DATA_TO_REG_ERROR_TEXT