import pytest
from api import Api
from data import courier_data

@pytest.fixture
def courier():
    data = courier_data()
    login_pass, reg_response = Api.register_new_courier_and_return_login_password(data)

    login_data = {
        "login": login_pass[0],
        "password": login_pass[1]
    }

    login_response = Api.login_courier(login_data)
    courier_id = login_response.json().get("id")
    
    yield login_pass[0], login_pass[1], courier_id
    del_response = Api.delete_courier(courier_id)
    assert del_response.status_code == 200