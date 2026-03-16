import requests 

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_posts_status():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200


def test_users_status():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200


def test_posts_not_empty():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert len(data) > 0