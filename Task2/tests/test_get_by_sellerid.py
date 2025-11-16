from Task2.data.test_data import *

class TestGetItemsBySellerId:
    def test_success_empty_get(self, api_client, get_item_id):
        response = api_client.create_item(VALID_DATA_GET_ITEMS_EMPTY)
        data = response.json()
        item_id = get_item_id(data)
        seller_id = VALID_DATA_GET_ITEMS_EMPTY["sellerID"]
        api_client.delete_item(item_id)
        response = api_client.get_seller_items(seller_id)
        data = response.json()
        assert response.status_code == 200
        assert data == []

    def test_success_one_get(self, api_client, get_item_id):
        response = api_client.create_item(VALID_DATA_GET_ITEMS)
        data = response.json()
        item_id = get_item_id(data)
        seller_id = VALID_DATA_GET_ITEMS["sellerID"]
        response = api_client.get_seller_items(seller_id)
        data = response.json()
        assert response.status_code == 200
        assert len(data) == 1
        api_client.delete_item(item_id)

    def test_success_get(self, api_client, get_item_id):
        response = api_client.create_item(VALID_DATA_GET_ITEMS_1)
        data = response.json()
        item_id_1 = get_item_id(data)
        response = api_client.create_item(VALID_DATA_GET_ITEMS_2)
        data = response.json()
        item_id_2 = get_item_id(data)
        response = api_client.create_item(VALID_DATA_GET_ITEMS_3)
        data = response.json()
        item_id_3 = get_item_id(data)
        seller_id = VALID_DATA_GET_ITEMS_1["sellerID"]
        response = api_client.get_seller_items(seller_id)
        data = response.json()
        assert response.status_code == 200
        assert len(data) == 3
        api_client.delete_item(item_id_1)
        api_client.delete_item(item_id_2)
        api_client.delete_item(item_id_3)

    def test_invalid_get(self, api_client):
        response = api_client.get_seller_items(INVALID_SELLERID)
        data = response.json()
        assert response.status_code == 400
        assert "передан некорректный идентификатор продавца" in data["result"]["message"]

    def test_invalid_str_get(self, api_client):
        response = api_client.get_seller_items(INVALID_STR_SELLERID)
        data = response.json()
        assert response.status_code == 400
        assert "передан некорректный идентификатор продавца" in data["result"]["message"]
