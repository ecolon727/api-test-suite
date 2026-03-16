import pytest
import json

@pytest.fixture
def test_data():
    with open("data/test_data.json") as f:
        return json.load(f)