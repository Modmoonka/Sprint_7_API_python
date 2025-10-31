import pytest
from api import Api
from data import *

class TestCourierLogin:

    @allure.title('Проверка: курьера можно создать заполнив обяз.поля')
    def test_login_with_registered_data(self, courier):
        login, password, _ = courier
        login_data = {"login": login, "password": password}
        login_response = Api.login_courier(login_data)
        assert login_response.status_code == 200
        assert "id" in login_response.json()


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