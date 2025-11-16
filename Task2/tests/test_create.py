import pytest
from Task2.data.test_data import *

class TestCreateItem:
    def test_success_create(self, api_client, get_item_id):
        response = api_client.create_item(VALID_DATA_CREATE)
        data = response.json()
        assert response.status_code == 200
        assert "Сохранили объявление" in data["status"]
        item_id = get_item_id(data)
        assert item_id is not None, f"ID не найден"

    def test_create_without_sellerid(self, api_client):
        response = api_client.create_item(DATA_CREATE_WITHOUT_SELLERID)
        data = response.json()
        assert response.status_code == 400
        assert "поле sellerID обязательно" in data["result"]["message"]

    def test_create_without_name(self, api_client):
        response = api_client.create_item(DATA_CREATE_WITHOUT_NAME)
        data = response.json()
        assert response.status_code == 400
        assert "поле name обязательно" in data["result"]["message"]

    def test_create_without_price(self, api_client):
        response = api_client.create_item(DATA_CREATE_WITHOUT_PRICE)
        data = response.json()
        assert response.status_code == 400
        assert "поле price обязательно" in data["result"]["message"]

    def test_create_without_statistics(self, api_client):
        response = api_client.create_item(DATA_CREATE_WITHOUT_STATISTICS)
        data = response.json()
        assert response.status_code == 200
        assert "Сохранили объявление" in data["status"]

    @pytest.mark.parametrize("data", [data for data in INVALID_SELLER_DATA_CREATE])
    def test_create_invalid_sellerid(self, api_client, data):
        response = api_client.create_item(data)
        assert response.status_code == 400

    @pytest.mark.parametrize("data", [data for data in INVALID_PRICE_DATA_CREATE])
    def test_create_invalid_price(self, api_client, data):
        response = api_client.create_item(data)
        assert response.status_code == 400

    @pytest.mark.parametrize("data", [data for data in INVALID_STATPARAMS_DATA_CREATE])
    def test_create_invalid_statistics(self, api_client, data):
        response = api_client.create_item(data)
        assert response.status_code == 400

    def test_create_invalid_extra(self, api_client):
        response = api_client.create_item(INVALID_EXTRA_DATA_CREATE)
        assert response.status_code == 400

    def test_create_invalid_json(self, api_client):
        response = api_client.create_item({})
        assert response.status_code == 400