from Task2.data.test_data import *

class TestGetItem:
    def test_success_get(self, api_client, get_item_id):
        response = api_client.create_item(VALID_DATA_GET_ITEM)
        data = response.json()
        item_id = get_item_id(data)
        response = api_client.get_item(item_id)
        data = response.json()
        assert response.status_code == 200
        assert data[0]["id"] == item_id, f'Значение id не совпадает'
        assert data[0]["sellerId"] == VALID_DATA_GET_ITEM["sellerID"], f'Значение sellerID не совпадает'
        assert data[0]["name"] == VALID_DATA_GET_ITEM["name"], f'Значение name не совпадает'
        assert data[0]["price"] == VALID_DATA_GET_ITEM["price"], f'Значение price не совпадает'
        assert data[0]["statistics"]["likes"] == VALID_DATA_GET_ITEM["statistics"]["likes"], f'Значение likes не совпадает'
        assert data[0]["statistics"]["viewCount"] == VALID_DATA_GET_ITEM["statistics"]["viewCount"], f'Значение viewCount не совпадает'
        assert data[0]["statistics"]["contacts"] == VALID_DATA_GET_ITEM["statistics"]["contacts"], f'Значение contacts не совпадает'

    def test_invalid_get(self, api_client):
        response = api_client.get_item(INVALID_ID)
        data = response.json()
        assert response.status_code == 400
        assert "ID" and "не UUID" in data["result"]["message"]

    def test_noex_get(self, api_client):
        response = api_client.get_item(NOEX_ID)
        data = response.json()
        assert response.status_code == 404
        assert "item" and "not found" in data["result"]["message"]
