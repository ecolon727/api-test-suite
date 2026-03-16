import requests 
from config.settings import BASE_URL


def get(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    return requests.get(url)