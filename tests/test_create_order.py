import allure

from helpers.helpers_order import *


class TestCreateOrder:
    @allure.title("Создание заказа")
    @allure.description("Успешное создание заказа")
    def test_success_create_order(self, registration_and_delete_user):
        token = registration_and_delete_user['token']
        ingredients = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6e']

        response = create_order(ingredients, token)

        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title("Создание заказа без авторизации пользователя")
    @allure.description("Проверка возможности создания заказа без авторизации")
    def test_create_order_without_authorization(self, registration_and_delete_user):
        ingredients = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6e']

        response = create_order(ingredients, "token")

        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка возможности создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self, registration_and_delete_user):
        token = registration_and_delete_user['token']

        response = create_order([], token)

        assert response.status_code == 400
        assert response.json()['message'] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным hash значением ингредиентов")
    @allure.description("Проверка создание заказа с неверным hash значением ингредиентов")
    def test_create_order_with_incorrect_hash_ingredients(self, registration_and_delete_user):
        token = registration_and_delete_user['token']
        ingredients = ['61c0c5a71d1f820073', '71d1f82001bdaaa6e']

        response = create_order(ingredients, token)

        assert response.status_code == 500
