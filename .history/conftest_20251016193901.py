# conftest.py
import pytest

@pytest.fixture(scope="session")
def api_headers():
    return {"Authorization": "Bearer your_api_key_here"}
