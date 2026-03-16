from utils.api_client import get 


def test_posts_status():
    response = get("posts")
    assert response.status_code == 200


def test_users_status():
    response = get("users")
    assert response.status_code == 200


def test_posts_not_empty():
    response = get("posts")
    data = response.json()
    assert len(data) > 0