import httpx
from jsonschema import validate
from core.contracts import USER_RESOURCE_SCHEMA

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
RESOURCE_NOT_FOUND = 'unknown/23'
YEAR_STARTS = '20'
PANTONE_VALUE_STARTS = '1'
COLOR_VALUE = '#C74375'


def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200
    users_data = response.json()['data']
    for item in users_data:
        validate(item, USER_RESOURCE_SCHEMA)
    assert str(item['year']).startswith(YEAR_STARTS)
    assert str(item['pantone_value']).startswith(PANTONE_VALUE_STARTS)


def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200
    users_data = response.json()['data']
    validate(users_data, USER_RESOURCE_SCHEMA)
    assert str(users_data['pantone_value']).startswith(PANTONE_VALUE_STARTS)
    assert str(users_data['year']).startswith(YEAR_STARTS)
    assert str(users_data['color']).__eq__(COLOR_VALUE)
    print(response.json())


def test_resource_not_found():
    response = httpx.get(BASE_URL + RESOURCE_NOT_FOUND)
    assert response.status_code == 404