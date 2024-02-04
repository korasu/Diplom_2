import random
import string
import requests

from data.endpoints import *


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_user(payload):
    return requests.post(base_url + Endpoints.create_user, data=payload)


def login_user(email, password):
    payload = {
        "email": email,
        "password": password
    }
    return requests.post(base_url + Endpoints.user_login, data=payload)


def change_user(email, name, token):
    payload = {
        "email": email,
        "name": name
    }
    return requests.patch(base_url + Endpoints.crud_user, data=payload, headers={'Authorization': token})


def remove_user(token):
    return requests.delete(base_url + Endpoints.crud_user, headers={'Authorization': token})
