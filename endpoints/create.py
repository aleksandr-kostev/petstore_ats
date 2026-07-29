import requests

class PostRequest:

    def __init__(self, base_url: str, endpoint: str):
        self.base_url = base_url
        self.endpoint = endpoint
        self.response = None
        self.response_json = None

    # Отправка запроса
    def send_request(self, payload: dict):
        self.response = requests.post(f'{self.base_url}{self.endpoint}', json=payload)
        self.response_json = self.response.json()

    # Получение id созданного питомца
    def get_id(self):
        self.created_pet_id = self.response_json['id']
        return self.created_pet_id

    # Проверка имени созданного питомца
    def check_name(self, name):
        assert self.response_json['name'] == name, (
            f"Expected pet name {name}, but got {self.response_json['name']}"
        )

    # Проверка статус кода
    def check_response_status(self, expected_code: int):
        assert self.response.status_code == expected_code, (f"Expected status code {expected_code}, but got {self.response.status_code}")

    # Проверка headers
    def check_headers(self):
        assert ("application/json" in self.response.headers.get("Content-Type", "")), \
            "Expected Content-Type to contain 'application/json'"