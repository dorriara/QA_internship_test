from Task2.data.test_data import *

class TestOthers:
    def test_put_v1(self, api_client):
        response = api_client.put_item(VALID_DATA_PUT, 1)
        assert response.status_code == 405

    def test_put_v2(self, api_client):
        response = api_client.put_item(VALID_DATA_PUT, 2)
        assert response.status_code == 405

    def test_noex_endpoint_v1(self, api_client):
        response = api_client.get_noex_endpoint(1)
        assert response.status_code == 404

    def test_noex_endpoint_v2(self, api_client):
        response = api_client.get_noex_endpoint(2)
        assert response.status_code == 404