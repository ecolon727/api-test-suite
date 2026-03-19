from utils.api_client import get 

def test_posts_status():
    response = get("posts")
    assert response.status_code == 200


def test_specific_post(test_data):
    post_id = test_data["valid_post_id"]
    response = get(f"posts/{post_id}")
    assert response.status_code == 200


def test_users_status():
    response = get("users")
    assert response.status_code == 200


def test_users_not_empty():
    respone = get("users")
    data = respone.json()

    assert len(data) > 0


def test_posts_not_empty():
    response = get("posts")
    data = response.json()
    assert len(data) > 0