import pytest
from api import Api
from data import courier_data
import uuid

@pytest.fixture
def courier():
    data = courier_data()
    # Делаем логин уникальным
    data["login"] = f"{data['login']}_{uuid.uuid4().hex[:8]}"
    
    # Регистрируем и получаем ответ
    login_pass, reg_response =  Api.register_new_courier_and_return_login_password(data)
    assert reg_response.status_code == 201, f"Registration failed: {reg_response.text}"

    login, password, _ = login_pass
    login_data = {"login": login, "password": password}
    login_resp = Api.login_courier(login_data)
    assert login_resp.status_code == 200, f"Login failed: {login_resp.text}"
    courier_id = login_resp.json()["id"]

    # 4. Передаём в тест
    yield login, password, courier_id, reg_response

    # 5. Удаляем
    if courier_id:
        try:
            Api.delete_courier(courier_id)
        except Exception as e:
            print(f"Warning: Failed to delete courier {courier_id}: {e}")