import allure

from helpers.helpers_order import *


class TestGetOrder:
    @allure.title("Успешное получение заказа пользователя")
    @allure.description("Проверка получения заказа")
    def test_success_taken_order(self, registration_and_delete_user):
        token = registration_and_delete_user['token']
        ingredients = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6e']

        create_order(ingredients, token)
        response = taken_user_order(token)

        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['orders'][0]['ingredients'] == ingredients

    @allure.title("Получение заказа пользователя без авторизации")
    @allure.description("Проверка получения заказа пользователя без авторизации на портале")
    def test_taken_order_without_token(self):
        response = taken_user_order('')

        assert response.status_code == 401
        assert response.json()['success'] == False
        assert response.json()['message'] == "You should be authorised"
