import allure

from helpers.helpers_user import *


class TestLoginUser:
    @allure.title("Успешная авторизация пользователя")
    @allure.description("Успешная авторизация пользователя на платформе с корректными данными")
    def test_success_authorization_with_correct_data(self, registration_and_delete_user):
        response = login_user(registration_and_delete_user['email'], registration_and_delete_user['password'])

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user']['email'] == str(registration_and_delete_user.get('email'))
        assert response.json()['user']['name'] == str(registration_and_delete_user.get('name'))

    @allure.title("Авторизация пользователя с некорректными данными")
    @allure.description("Провести авторизацию пользователя с некорректными данными для выявления ошибки")
    def test_authorization_user_incorrect_data(self):
        email = f'{generate_random_string(10)}@mail.ru'
        password = generate_random_string(10)
        response = login_user(email, password)

        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == 'email or password are incorrect'
