# API Test Suite

Python-based API automation framework built using pytest.

## Features
- Automated API testing
- Reusable API client
- Test data management
- Pytest fixtures
- Test markers (smoke, regression)
- CI integration with GitHub Actions

## Tech Stack
- Python
- pytest
- requests

## Project Structure
tests/ - test cases
utils/ - reusable API functions
config/ - environment configuration
data/ - test data
report/ - test results

# Running Tests

Install dependencies:
pip install -r requirements.txt

Run all tests:
pytest

Run smoke tests only:
pytest -m smoke

## CI/CD

Tests are automatically executed on every push using GitHub Actions

## API tested:
https://jsonplaceholder.typicode.com

## Test Coverage
- Endpoint availability
- Status code validation
- Response data validation