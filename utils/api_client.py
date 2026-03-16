import requests 

BASE_URL = "https://jsonplaceholder.typicode.com"

def get(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    return requests.get(url)