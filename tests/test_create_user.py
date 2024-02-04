import allure
import pytest

from helpers.helpers_user import *


class TestCreateUser:
    @allure.title("Регистрация пользователя с корректными данными")
    @allure.description("Проверка успешной регистрации пользователя с корректными данными")
    def test_success_registration(self, registration_and_delete_user):
        assert registration_and_delete_user['response'].status_code == 200
        assert registration_and_delete_user['response'].json()['success'] == True

    @allure.title("Регистрация пользователя с теме же данными")
    @allure.title("Проверка получение ошибки при регистрации пользователя с уже зарегистрированными данными")
    def test_create_user_with_used_data(self, registration_and_delete_user):
        first_registration = registration_and_delete_user['response']

        payload = {
            "email": first_registration.json()['user']['email'],
            "name": first_registration.json()['user']['name'],
            "password": generate_random_string(10)
        }

        second_registration = create_user(payload)

        assert second_registration.status_code == 403
        assert second_registration.json()['message'] == 'User already exists'

    @allure.title("Регистрация пользователя с уже использованным email`ом")
    @allure.title("Проверка получение ошибки при регистрации пользователя с уже зарегистрированным email`ом")
    def test_create_user_with_used_email(self, registration_and_delete_user):
        payload = {
            "email": registration_and_delete_user['email'],
            "name": generate_random_string(6),
            "password": generate_random_string(10)
        }

        response = create_user(payload)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title("Регистрация пользователя с уже использованным именем")
    @allure.title("Проверка получение ошибки при регистрации пользователя с уже зарегистрированным именем")
    def test_create_user_with_used_name(self, registration_and_delete_user):
        payload = {
            "email": f'{generate_random_string(10)}@example.com',
            "name": registration_and_delete_user['name'],
            "password": generate_random_string(10)
        }

        response = create_user(payload)

        assert response.status_code == 200
        assert response.json()['success'] == True

    payload_without_requirement_parameter = [
        [{"name": generate_random_string(6), "password": generate_random_string(10)}, 'email'],
        [{"email": f'{generate_random_string(6)}@example.com', "password": generate_random_string(10)}, 'name'],
        [{"email": f'{generate_random_string(6)}@example.com', "name": generate_random_string(6)}, 'password']
    ]

    @pytest.mark.parametrize('payload', payload_without_requirement_parameter)
    @allure.title('Регистрация пользователя без одного из обязательного поля (unused_field: {payload[1]})')
    @allure.description('В данном тесте будет проверяться создание пользователя без одного из обязательных полей')
    def test_create_user_without_requirement_parameter(self, payload):
        response = create_user(payload[0])

        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
