import requests

class PutRequest:

    def __init__(self, base_url: str, endpoint: str):
        self.base_url = base_url
        self.endpoint = endpoint
        self.response = None
        self.response_json = None

    # Отправка запроса по id питомца
    def send_request_pet(self, payload: dict):
        self.response = requests.put(f'{self.base_url}{self.endpoint}', json=payload)
        self.response_json = self.response.json()

    # Отправка запроса по username пользователя
    def send_request_user(self, payload: dict, username):
        self.response = requests.put(f'{self.base_url}{self.endpoint}/{username}', json=payload)

    # Проверка имени измененного питомца
    def check_name(self, name: str):
        assert self.response_json['name'] == name, (
            f"Expected pet name {name}, but got {self.response_json['name']}"
        )

    # Проверка статус кода
    def check_response_status(self):
        assert self.response.status_code == 200, (f"Expected status code 200")

    # Проверка headers
    def check_headers(self):
        assert ("application/json" in self.response.headers.get("Content-Type", "")), \
            "Expected Content-Type to contain 'application/json'"