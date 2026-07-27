import string
import random
from endpoints.create import PostRequest
from endpoints.delete import DeleteRequest
from endpoints.read import GetRequest
from endpoints.update import PutRequest


BASE_URL = 'https://petstore.swagger.io/v2'
PET_EP = '/pet'
USER_EP = '/user'


# Add a new pet to the store (POST)
def test_add_pet(create_pet_payload, delete_test_pet):
    # Создание пейлоуда
    payload = create_pet_payload
    name = payload['category']['name']
    # Отправка POST запроса
    add_new_pet = PostRequest(BASE_URL, PET_EP)
    add_new_pet.send_request(payload)
    # Передача id питомца в фикстуру удаления
    created_pet_id = add_new_pet.get_id()
    delete_test_pet["id"] = created_pet_id
    # Проверки
    add_new_pet.check_response_status()
    add_new_pet.check_headers()
    add_new_pet.check_name(name)

# Find pet by id (GET)
def test_get_pet(create_pet_payload, delete_test_pet):
    # Создание питомца для теста
    payload = create_pet_payload
    add_new_pet = PostRequest(BASE_URL, PET_EP)
    add_new_pet.send_request(payload)
    # Получение id питомца для теста
    created_pet_id = add_new_pet.get_id()
    # Передача id питомца в фикстуру удаления
    delete_test_pet['id'] = created_pet_id
    # Отправка GET запроса
    get_pet_by_id = GetRequest(BASE_URL, PET_EP)
    get_pet_by_id.send_request_pet(created_pet_id)
    # Проверки
    get_pet_by_id.check_response_status()
    get_pet_by_id.check_headers()

# Delete pet by id (DELETE)
def test_delete_pet(create_pet_payload):
    # Создание питомца для теста
    payload = create_pet_payload
    add_new_pet = PostRequest(BASE_URL, PET_EP)
    add_new_pet.send_request(payload)
    # Получение id питомца для теста
    created_pet_id = add_new_pet.get_id()
    # Отправка DELETE запроса
    delete_pet = DeleteRequest(BASE_URL, PET_EP)
    delete_pet.send_request_pet(created_pet_id)
    # Проверки
    delete_pet.check_response_status()
    delete_pet.check_headers()

# Update an existing pet (PUT)
def test_update_pet(create_pet_payload, delete_test_pet):
    # Создание питомца для теста
    payload = create_pet_payload
    add_new_pet = PostRequest(BASE_URL, PET_EP)
    add_new_pet.send_request(payload)
    # Получение id питомца для теста
    created_pet_id = add_new_pet.get_id()
    # Передача id питомца в фикстуру удаления
    delete_test_pet['id'] = created_pet_id
    # Изменение пейлоуда для теста
    payload['id'] = created_pet_id
    new_name = ''.join(random.choices(string.ascii_letters, k=8))
    payload['category']['name'] = new_name
    # Отправка PUT запроса
    update_pet = PutRequest(BASE_URL, PET_EP)
    update_pet.send_request_pet(payload)
    # Проверки
    update_pet.check_response_status()
    update_pet.check_headers()
    update_pet.check_name(new_name)

# Create user (POST)
def test_create_user(create_user_payload, delete_test_user):
    # Создание пейлоуда
    payload = create_user_payload
    # Отправка POST запроса
    create_new_user = PostRequest(BASE_URL, USER_EP)
    create_new_user.send_request(payload)
    # Передача username в фикстуру удаления
    created_user_username = payload['username']
    delete_test_user['username'] = created_user_username
    # Проверки
    create_new_user.check_response_status()
    create_new_user.check_headers()

# Get user by username (GET)
def test_get_user(create_user_payload, delete_test_user):
    # Создание пользователя для теста
    payload = create_user_payload
    add_new_user = PostRequest(BASE_URL, USER_EP)
    add_new_user.send_request(payload)
    # Получение username пользователя для теста
    created_user_username = payload['username']
    # Передача username в фикстуру удаления
    delete_test_user['username'] = created_user_username
    # Отправка запроса
    get_user = GetRequest(BASE_URL, USER_EP)
    get_user.send_request_user(created_user_username)
    # Проверки
    get_user.check_response_status()
    get_user.check_headers()

# Delete user (DELETE)
def test_delete_user(create_user_payload):
    # Создание пользователя для теста
    payload = create_user_payload
    add_new_user = PostRequest(BASE_URL, USER_EP)
    add_new_user.send_request(payload)
    # Получение username пользователя для теста
    created_user_username = payload['username']
    # Отправка запроса
    delete_user = DeleteRequest(BASE_URL, USER_EP)
    delete_user.send_request_user(created_user_username)
    # Проверки
    delete_user.check_response_status()
    delete_user.check_headers()

# Update user (PUT)
def test_update_user(create_user_payload, delete_test_user):
    # Создание пользователя для теста
    payload = create_user_payload
    add_new_user = PostRequest(BASE_URL, USER_EP)
    add_new_user.send_request(payload)
    # Получение username пользователя для теста
    created_user_username = payload['username']
    # Изменение пейлоуда для теста
    new_username = ''.join(random.choices(string.ascii_letters, k=8))
    payload['username'] = new_username
    # Отправка запроса
    update_user = PutRequest(BASE_URL, USER_EP)
    update_user.send_request_user(payload, created_user_username)
    # Передача username в фикстуру удаления
    delete_test_user['username'] = new_username
    # Проверки
    update_user.check_response_status()
    update_user.check_headers()


