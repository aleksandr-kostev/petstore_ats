import string
import random
import pytest

from conftest import delete_test_user


@pytest.mark.parametrize(
    "create_user_payload, expected_code",
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
    indirect=["create_user_payload"],
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

# Create user (POST)
def test_create_user(client,create_user_payload, expected_code,  delete_test_user):
    # Тест
    client.create_user(create_user_payload)

    # Передача username в фикстуру удаления
    delete_test_user['username'] = create_user_payload.get('username')

    # Проверки
    client.check_response_status(expected_code)
    client.check_headers()

# Get user by username (GET)
def test_get_user(client, create_user_payload, delete_test_user):
    # Создание пользователя для теста
    client.create_user(create_user_payload)

    # Получение username пользователя для теста
    username = create_user_payload.get('username')

    # Передача username в фикстуру удаления
    delete_test_user['username'] = username

    # Тест
    client.get_user(username)

    # Проверки
    client.check_response_status()
    client.check_headers()

# Delete user (DELETE)
def test_delete_user(client, create_user_payload):
    # Создание пользователя для теста
    client.create_user(create_user_payload)

    # Получение username пользователя для теста
    username = create_user_payload.get('username')

    # Тест
    client.delete_user(username)

    # Проверки
    client.check_response_status()
    client.check_headers()

# Update user (PUT)
def test_update_user(client, create_user_payload, delete_test_user):
    # Создание пользователя для теста
    payload = create_user_payload
    client.create_user(payload)

    # Получение username пользователя для теста
    username = payload.get('username')



    # Изменение пейлоуда для теста
    new_username = ''.join(random.choices(string.ascii_letters, k=8))
    payload['username'] = delete_test_user ['username'] = new_username

    # Тест
    client.update_user(username, payload)
    # Проверки
    client.check_response_status()
    client.check_headers()