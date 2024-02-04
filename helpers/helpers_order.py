import requests

from data.endpoints import *


def create_order(ingredients: list, token):
    payload = {"ingredients": ingredients}
    return requests.post(base_url + Endpoints.crud_order, data=payload, headers={"Authorization": token})


def taken_user_order(token):
    return requests.get(base_url + Endpoints.crud_order, headers={"Authorization": token})
