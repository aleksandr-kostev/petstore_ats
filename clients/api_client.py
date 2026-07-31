import requests
from enum import Enum
from config import Config


class Endpoints(str, Enum):
    PET = "/pet" # Пример использования Endpoints.PET
    USER = "/user"


class ApiClient:
    def __init__(self, base_url: str = Config.BASE_URL, timeout: int = Config.TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.response = None

    def create_pet(self, payload: dict, endpoint: str = Endpoints.PET.value):
        self.response = requests.post(f"{self.base_url}{endpoint}", json=payload, timeout=self.timeout)
        return self.response

    def get_pet(self, pet_id: int, endpoint: str = Endpoints.PET.value):
        self.response = requests.get(f"{self.base_url}{endpoint}/{pet_id}", timeout=self.timeout)
        return self.response

    def delete_pet(self, pet_id: int, endpoint: str = Endpoints.PET.value):
        self.response = requests.delete(f"{self.base_url}{endpoint}/{pet_id}", timeout=self.timeout)
        return self.response

    def update_pet(self, payload: dict, endpoint: str = Endpoints.PET.value):
        self.response = requests.put(f"{self.base_url}{endpoint}", json=payload, timeout=self.timeout)
        return self.response

    def create_user(self, payload: dict, endpoint: str = Endpoints.USER.value):
        self.response = requests.post(f"{self.base_url}{endpoint}", json=payload, timeout=self.timeout)
        return self.response

    def get_user(self, username: str, endpoint: str = Endpoints.USER.value):
        self.response = requests.get(f"{self.base_url}{endpoint}/{username}", timeout=self.timeout)
        return self.response

    def delete_user(self, username: str, endpoint: str = Endpoints.USER.value):
        self.response = requests.delete(f"{self.base_url}{endpoint}/{username}", timeout=self.timeout)
        return self.response

    def update_user(self, username: str, payload: dict, endpoint: str = Endpoints.USER.value):
        self.response = requests.put(f"{self.base_url}{endpoint}/{username}", json=payload, timeout=self.timeout)
        return self.response

    def check_response_status(self, expected_code: int = 200):
        assert self.response.status_code == expected_code, (
            f"Expected response status code {expected_code}, but got {self.response.status_code}"
        )

    def check_headers(self, expected_content_type: str = "application/json"):
        content_type = self.response.headers.get("Content-Type", "")
        assert expected_content_type in content_type, (
            f"Expected Content-Type to contain {expected_content_type}, got '{content_type}'"
        )

    def get_json(self):
        try:
            return self.response.json()
        except requests.exceptions.JSONDecodeError:
            return None

    def check_pet_name(self, expected_name: str):
        json_data = self.get_json()
        assert json_data is not None, "Response body is not valid JSON"
        assert "name" in json_data, "Key 'name' is missing from JSON"
        actual_name = json_data['name']
        assert actual_name == expected_name, (
            f"Expected pet name {expected_name}, but got {actual_name}"
        )