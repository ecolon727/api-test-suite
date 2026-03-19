from utils.api_client import get 

def test_users_status():
    response = get("users")
    assert response.status_code == 200


def test_users_not_empty():
    respone = get("users")
    data = respone.json()

    assert len(data) > 0