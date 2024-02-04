import pytest

from helpers.helpers_user import *


@pytest.fixture
def registration_and_delete_user():
    data = {}
    email = f'{generate_random_string(7)}@example.com'
    name = f'{generate_random_string(8)}'
    password = f'{generate_random_string(12)}'
    data['email'] = email
    data['name'] = name
    data['password'] = password

    payload = {
        "email": email,
        "name": name,
        "password": password
    }

    response = create_user(payload)
    token = response.json()['accessToken']
    data['token'] = token
    data['response'] = response

    yield data
    remove_user(token)
