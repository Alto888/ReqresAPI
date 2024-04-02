import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA

BASE_URL = 'https://reqres.in/'
EMAIL_ENDS = '@reqres.in'
SINGLE_USER = 'api/users/2'
LIST_USERS = 'api/users?page=2'
USER_NOT_FOUND = 'users/23'


def test_list_users():
    response = httpx.get(BASE_URL + LIST_USERS)
    assert response.status_code == 200
    users_data = response.json()['data']
    for item in users_data:
        validate(item, USER_DATA_SCHEMA)
        assert item['email'].endswith(EMAIL_ENDS)
        # При написании кода с использованием переменной:
        # id = item['id']
        # avatar = f'{BASE_URL}img/faces/{id}-image.jpg'
        # assert item['avatar'] == avatar
        assert item['avatar'] == f'{BASE_URL}img/faces/{item['id']}-image.jpg'


def test_single_user():
    response = httpx.get(BASE_URL + SINGLE_USER)
    assert response.status_code == 200
    users_data = response.json()['data']
    validate(users_data, USER_DATA_SCHEMA)
    assert users_data['email'].endswith(EMAIL_ENDS)
    assert users_data['avatar'] == f'{BASE_URL}img/faces/{users_data['id']}-image.jpg'


def test_user_not_found():
    response = httpx.get(BASE_URL + USER_NOT_FOUND)
    assert response.status_code == 404






