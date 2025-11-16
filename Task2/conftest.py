import pytest, re
from Task2.utils.api_client import ApiClient
from Task2.data.test_data import ID_PATTERN

@pytest.fixture
def api_client():
    return ApiClient()

@pytest.fixture
def get_item_id():
    def get_id(data):
        match = re.search(ID_PATTERN, data["status"], re.IGNORECASE)
        if match:
            item_id = match.group(0)
            return item_id
        else:
            raise ValueError("ID не найден в поле 'status'")
    return get_id