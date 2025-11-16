from Task2.data.test_data import *

class TestDeleteItem:
    def test_success_delete(self, api_client, get_item_id):
        response = api_client.create_item(VALID_DATA_DELETE)
        data = response.json()
        item_id = get_item_id(data)
        response = api_client.delete_item(item_id)
        assert response.status_code == 200
        response = api_client.get_item(item_id)
        assert response.status_code == 404

    def test_invalid_delete(self, api_client):
        response = api_client.delete_item(INVALID_ID)
        data = response.json()
        assert response.status_code == 400
        assert "переданный id айтема некорректный" in data["result"]["message"]

    def test_noex_delete(self, api_client):
        response = api_client.delete_item(NOEX_ID)
        assert response.status_code == 404