from data import *
import pytest
from api import Api
import allure
import uuid

class TestCreateCourier:

    @allure.title('Проверяем, что курьера можно создать')
    @allure.description('запрос возвращает {"ok":true}')
    def test_register_courier_return_ok(self, courier):
        login, password, courier_id, response = courier 
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Проверка: если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_register_two_identical_couriers(self, courier):
        # Регистрируем первого курьера
        login, password, courier_id, _ = courier

        # Повторная регистрация с теми же данными
        duplicate_data = {
            "login": login, 
            "password": "newpass123", 
            "firstName": "Test2"}
        _, response = Api.register_new_courier_and_return_login_password(duplicate_data)

        assert response.status_code == 409 and response.json()['message'] == ErrorText.RegistrationErrorText.LOGIN_USED_ERROR_TEXT


    @pytest.mark.parametrize("invalid_data", [registration_data_without_login(), registration_data_without_password()])
    @allure.title('Проверяем, что запрос возвращает ошибку, если нет заполнения одного из обязательных полей')
    def test_register_courier_without_mandatory_info_returns_400(self, invalid_data):
        _, reg_response = Api.register_new_courier_and_return_login_password(invalid_data)
        assert reg_response.status_code == 400 and "message" in reg_response.json() and reg_response.json()["message"] == ErrorText.RegistrationErrorText.NOT_ENOUGH_DATA_TO_REG_ERROR_TEXT