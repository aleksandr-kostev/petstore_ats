import requests

class DeleteRequest:

    def __init__(self, base_url, endpoint):
        self.base_url = base_url
        self.endpoint = endpoint
        self.response = None

    # Отправка запроса по id питомца
    def send_request_pet(self, id: int):
        self.response = requests.delete(f'{self.base_url}{self.endpoint}/{id}')

    # Отправка запроса по username пользователя
    def send_request_user(self, username):
        self.response = requests.delete(f'{self.base_url}{self.endpoint}/{username}')

    # Проверка статус кода
    def check_response_status(self):
        assert self.response.status_code == 200, (f"Expected status code 200")

    # Проверка headers
    def check_headers(self):
        assert ("application/json" in self.response.headers.get("Content-Type", "")), \
            "Expected Content-Type to contain 'application/json'"