from Task2.data.test_data import *

class TestGetStatistics:
    def test_success_get_stat_v1(self, api_client, get_item_id):
        response = api_client.create_item(VALID_DATA_GET_STATISTICS)
        data = response.json()
        item_id = get_item_id(data)
        response = api_client.get_statistics(item_id, 1)
        data = response.json()
        assert response.status_code == 200
        assert data[0]["likes"] == VALID_DATA_GET_STATISTICS["statistics"]["likes"]
        assert data[0]["viewCount"] == VALID_DATA_GET_STATISTICS["statistics"]["viewCount"]
        assert data[0]["contacts"] == VALID_DATA_GET_STATISTICS["statistics"]["contacts"]
        api_client.delete_item(item_id)

    def test_invalid_get_stat_v1(self, api_client):
        response = api_client.get_statistics(INVALID_ID, 1)
        data = response.json()
        assert response.status_code == 400
        assert "передан некорректный идентификатор объявления" in data["result"]["message"]

    def test_noex_get_stat_v1(self, api_client):
        response = api_client.get_statistics(NOEX_ID, 1)
        data = response.json()
        assert response.status_code == 404
        assert "statistics" and "not found" in data["result"]["message"]

    def test_success_get_stat_v2(self, api_client, get_item_id):
        response = api_client.create_item(VALID_DATA_GET_STATISTICS)
        data = response.json()
        item_id = get_item_id(data)
        response = api_client.get_statistics(item_id, 2)
        data = response.json()
        assert response.status_code == 200
        assert data[0]["likes"] == VALID_DATA_GET_STATISTICS["statistics"]["likes"]
        assert data[0]["viewCount"] == VALID_DATA_GET_STATISTICS["statistics"]["viewCount"]
        assert data[0]["contacts"] == VALID_DATA_GET_STATISTICS["statistics"]["contacts"]
        api_client.delete_item(item_id)

    def test_invalid_get_stat_v2(self, api_client):
        response = api_client.get_statistics(INVALID_ID, 2)
        data = response.json()
        assert response.status_code == 400
        assert "передан некорректный идентификатор объявления" in data["result"]["message"]

    def test_noex_get_stat_v2(self, api_client):
        response = api_client.get_statistics(NOEX_ID, 2)
        data = response.json()
        assert response.status_code == 404
        assert "statistics" and "not found" in data["result"]["message"]
