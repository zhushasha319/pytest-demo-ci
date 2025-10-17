# conftest.py
import pytest
import 
@pytest.fixture(scope="session")
def api_headers():
    return {"Authorization": "Bearer your_api_key_here"}
