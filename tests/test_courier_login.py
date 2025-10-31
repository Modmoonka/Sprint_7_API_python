import pytest
import allure
from api import Api
from data import *

class TestCourierLogin:

    @allure.title('Успешная авторизация курьера при заполнении всех обязательных полей')
    def test_login_with_registered_data(self, courier):
        login, password, expected_courier_id, _ = courier
        login_data = {"login": login, "password": password}
        login_response = Api.login_courier(login_data)
        
        assert login_response.status_code == 200
        response_json = login_response.json()
        assert "id" in response_json
        assert response_json["id"] == expected_courier_id 

    @allure.title('Проверка:c некорректными данными')
    def test_login_with_incorrect_credentials(self):
        login_data = {"login": "Login55", "password": "login55555"}
        login_response = Api.login_courier(login_data)
        assert login_response.status_code == 404
        assert "message" in login_response.json()
        assert login_response.json()["message"] == ErrorText.LoginErrorText.NON_EXISTENT_ACC_DATA_ERROR_TEXT


    @pytest.mark.parametrize("login_data", [{"login": "", "password": ""}])
    @allure.title('Проверка: если одного из полей нет, запрос возвращает ошибку;')
    def test_login_without_credentials_in_field(self, login_data):
        login_response = Api.login_courier(login_data)
        assert login_response.status_code == 400
        assert "message" in login_response.json()
        assert login_response.json()["message"] == ErrorText.LoginErrorText.EMPTY_LOGIN_PASSWORD_FIELD_ERROR_TEXT