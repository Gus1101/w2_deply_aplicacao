import pytest
from fastapi.testclient import TestClient
from main import *

client = TestClient(app)

@pytest.mark.unit
def test_request_api_status_code():
    response = client.get("/")
    assert response.status_code == 200

@pytest.mark.unit
def test_request_api_json():
    response = client.get("/")
    assert response.json() == {"Olá":"Mundo"}

@pytest.mark.unit
def test_request_lista_produtos_status_code():
	response = client.get("/lista_de_produtos")
	assert response.status_code == 200

@pytest.mark.unit
def test_request_lista_produtos_length():
	response = client.get("/lista_de_produtos")
	assert len(response.json()) == 3

@pytest.mark.unit
def test_request_busca_produto_inexistente_status_code():
	response = client.get("/lista_de_produtos/4")
	assert response.status_code == 404
	
@pytest.mark.unit
def test_request_busca_produto_existente_status_code():
	response = client.get("/lista_de_produtos/1")
	assert response.status_code == 200