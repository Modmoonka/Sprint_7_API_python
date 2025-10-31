import requests
from data import *
from config import *

class Api:
    
    @staticmethod
    @allure.step('Регистрация нового курьера')
    def register_new_courier_and_return_login_password(data):
        login_pass = []
        url = CONFIG.courier
        response = requests.post(url, data=data)

        if response.status_code == 201:
            login_pass.append(data["login"])
            login_pass.append(data["password"])
            login_pass.append(data["firstName"])
        return login_pass, response

    @staticmethod
    @allure.step('Вход курьера в систему')
    def login_courier(login_data):
        url = CONFIG.courier_login
        response = requests.post(url, json=login_data)
        return response


    @staticmethod
    @allure.step('Метод создания заказа')
    def create_order(color):
        url = CONFIG.orders
        payload = get_order_payload(color)
        order_response = requests.post(url, json=payload)
        return order_response

    @staticmethod
    @allure.step('Метод получение списка заказов')
    def get_order_list():
        url = CONFIG.orders
        response = requests.get(url)
        return response


    @staticmethod
    @allure.step('Метод удаления курьера')
    def delete_courier(courier_id):
        url = f"{CONFIG.courier}/{courier_id}"
        del_response = requests.delete(url)
        return del_response