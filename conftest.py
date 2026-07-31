import requests
import pytest
import string
import random
from config import Config
from endpoints.api_client import ApiClient

BASE_URL = 'https://petstore.swagger.io/v2'
PET_EP = '/pet'
USER_EP = '/user'


# Создание экземпляра класса ApiClient
@pytest.fixture
def client():
    return ApiClient()


# Создание пейлоуда питомца
@pytest.fixture
def create_pet_payload(request):
    pet_name = getattr(request, "param", "Doggie")
    payload = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },
      "name" : pet_name,
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }
    return payload

# Создание пейлоуда пользователя
@pytest.fixture
def create_user_payload(request):
    username = getattr(request, "param", "User")
    payload = {
            "id": 0,
            "username": username,
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 3
        }
    return payload

# Удаление питомца после теста
@pytest.fixture
def delete_test_pet():
    deleted_pet_id = {}
    delete = ApiClient()
    yield deleted_pet_id

    pet_id = deleted_pet_id.get("id")
    if pet_id:
        delete.delete_pet(pet_id)
        assert delete.response.status_code == 200, "Pet isn't deleted"


# Удаление пользователя после теста
@pytest.fixture
def delete_test_user():
    deleted_user_username = {}
    delete = ApiClient()
    yield deleted_user_username

    username = deleted_user_username.get("username")
    if username not in (" ", None, ""):
        delete.delete_user(username)
        assert delete.response.status_code  == 200, "User isn't deleted"