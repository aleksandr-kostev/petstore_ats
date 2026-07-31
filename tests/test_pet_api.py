import string
import random
import pytest


@pytest.mark.parametrize(
    "create_pet_payload, expected_code",
    [
        # Позитивные кейсы
        ("Doggie", 200),
        ("Ca", 200),
        ("Современные технологии развиваются очень быстро, открывая перед каждым"
         " человеком уникальные возможности для обучения, творчества, работы и "
         "эффективного общения в любое время суток из любой точки нашей большой планеты", 200),
        ("12345", 200),
        (" ", 200),
        ("Cat and Dog", 200),
        (" Cattie", 200),
        # Негативные кейсы
        (12345, 200),
        ("", 200),
        (None, 200)
    ],
    indirect=["create_pet_payload"],
    ids=[
        "Standard name",
        "Short name",
        "Long name (250 chars)",
        "Numeric string name",
        "Space",
        "Name with space",
        "Space at the beginning ",
        "Name is integer",
        "Empty string",
        "None"
    ]
)


# Add a new pet to the store (POST)
def test_add_pet(client, create_pet_payload, expected_code, delete_test_pet):
    # Тест
    client.create_pet(create_pet_payload)

    # Передача id питомца в фикстуру удаления
    if client.response.status_code == 200:
        pet_id = client.get_json()['id']
        if pet_id:
            delete_test_pet['id'] = pet_id

    # Проверки
    client.check_response_status(expected_code)
    client.check_headers()
    if client.response.status_code == 200:
        client.check_pet_name(create_pet_payload['name'])


# Find pet by id (GET)
def test_get_pet(client, create_pet_payload, delete_test_pet):
    # Создание питомца для теста
    client.create_pet(create_pet_payload)

    # Получение id для теста и передача в фикстуру удаления
    if client.response.status_code == 200:
        pet_id = client.get_json()['id']
        if pet_id:
            delete_test_pet['id'] = pet_id

    # Тест
    client.get_pet(pet_id)

    # Проверки
    client.check_response_status()
    client.check_headers()

# Delete pet by id (DELETE)
def test_delete_pet(client, create_pet_payload):
    # Создание питомца для теста
    client.create_pet(create_pet_payload)

    # Получение id для теста
    if client.response.status_code == 200:
        pet_id = client.get_json()['id']

    # Проверки
    client.delete_pet(pet_id)
    client.check_response_status()
    client.check_headers()

# Update an existing pet (PUT)
def test_update_pet(client, create_pet_payload, delete_test_pet):
    # Создание питомца для теста
    payload = create_pet_payload
    client.create_pet(payload)

    # Получение id для теста и передача в фикстуру удаления
    if client.response.status_code == 200:
        pet_id = client.get_json()['id']
        if pet_id:
            delete_test_pet['id'] = pet_id

    # Изменение пейлоуда для теста
    payload['id'] = pet_id
    new_name = ''.join(random.choices(string.ascii_letters, k=8))
    payload['name'] = new_name

    # Тест
    client.update_pet(payload)

    # Проверки
    client.check_response_status()
    client.check_headers()
    client.check_pet_name(new_name)





