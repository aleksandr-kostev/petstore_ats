import requests
import pytest
import string
import random


BASE_URL = 'https://petstore.swagger.io/v2'
PET_EP = '/pet'
USER_EP = '/user'


# Создание пейлоуда питомца
@pytest.fixture
def create_pet_payload():
    payload = {
      "id": 0,
      "category": {
        "id": 0,
        "name": "string"
      },

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
    random_name = ''.join(random.choices(string.ascii_letters, k=8))
    payload["category"]["name"] = random_name
    return payload

# Создание пейлоуда пользователя
@pytest.fixture
def create_user_payload():
    payload = {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 3
        }
    random_name = ''.join(random.choices(string.ascii_letters, k=8))
    payload["username"] = random_name
    return payload

# Удаление питомца после теста
@pytest.fixture
def delete_test_pet():
    deleted_pet_id = {}
    yield deleted_pet_id

    pet_id = deleted_pet_id.get("id")
    if pet_id:
        delete_response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
        assert delete_response.status_code == 200, "Pet isn't deleted"


# Удаление пользователя после теста
@pytest.fixture
def delete_test_user():
    deleted_user_username = {}
    yield deleted_user_username

    username = deleted_user_username.get("username")
    if username:
        delete_response = requests.delete(f"{BASE_URL}/user/{username}")
        assert delete_response.status_code  == 200, "User isn't deleted"