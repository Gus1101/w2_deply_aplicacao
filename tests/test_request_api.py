import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.unit
def test_request_api_status_code():
    response = client.get("/")
    assert response.status_code == 200

@pytest.mark.unit
def test_request_api_json():
    response = client.get("/")
    assert response.json() == {"Olá":"Mundo"}