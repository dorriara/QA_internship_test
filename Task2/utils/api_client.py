import requests
from Task2.data.test_data import BASE_URL

API_V1 = f"{BASE_URL}/api/1"
API_V2 = f"{BASE_URL}/api/2"

class ApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def create_item(self, data):
        return self.session.post(
            f"{API_V1}/item",
            json=data
        )

    def get_item(self, item_id):
        return self.session.get(
            f"{API_V1}/item/{item_id}"
        )

    def get_seller_items(self, seller_id):
        return self.session.get(
            f"{API_V1}/{seller_id}/item"
        )

    def get_statistics(self, item_id, version=1):
        base_url = API_V1 if version == 1 else API_V2
        return self.session.get(
            f"{base_url}/statistic/{item_id}"
        )

    def delete_item(self, item_id):
        return self.session.delete(
            f"{API_V2}/item/{item_id}"
        )

    def put_item(self, data, version=1):
        base_url = API_V1 if version == 1 else API_V2
        return self.session.put(
            f"{base_url}/item",
            json = data
        )

    def get_noex_endpoint(self, version=1):
        base_url = API_V1 if version == 1 else API_V2
        return self.session.get(
            f"{base_url}/test"
        )