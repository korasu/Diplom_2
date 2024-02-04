import allure

from helpers.helpers_user import *


class TestChangeUserData:
    @allure.title("Смена email`а пользователя на портале")
    @allure.description("Успешная смена данных для email`а пользователя")
    def test_success_change_user_email(self, registration_and_delete_user):
        name = registration_and_delete_user['name']
        new_email = f'{generate_random_string(7)}@example.com'
        user_token = registration_and_delete_user['token']

        response = change_user(new_email, name, user_token)

        assert response.status_code == 200
        assert response.json()['user']['email'] == new_email
        assert response.json()['user']['name'] == name

    @allure.title("Смена имени пользователя на портале")
    @allure.description("Успешная смена данных для имени пользователя")
    def test_success_change_user_name(self, registration_and_delete_user):
        email = registration_and_delete_user['email']
        new_name = generate_random_string(7)
        user_token = registration_and_delete_user['token']

        response = change_user(email, new_name, user_token)

        assert response.status_code == 200
        assert response.json()['user']['email'] == email
        assert response.json()['user']['name'] == new_name

    @allure.title("Смена email`а пользователя на портале без авторизации")
    @allure.description("Попытка смены данных для email`а пользователя без авторизации")
    def test_change_user_email_without_authorization(self, registration_and_delete_user):
        name = registration_and_delete_user['name']
        new_email = f'{generate_random_string(7)}@example.com'

        response = change_user(new_email, name, "")

        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'

    @allure.title("Смена имени пользователя на порталебез авторизации")
    @allure.description("Попытка смена данных для имени пользователя без авторизации")
    def test_change_user_name_without_authorization(self, registration_and_delete_user):
        email = registration_and_delete_user['email']
        new_name = generate_random_string(7)

        response = change_user(email, new_name, "")

        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'
