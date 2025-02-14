from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_all_characters():
    """Test para verificar el endpoint que lista todos los personajes"""
    response = client.get("/characters")
    assert response.status_code == 200
    characters = response.json()
    assert len(characters) > 0
    assert all(
        all(key in char for key in ["name", "age", "description", "greeting"])
        for char in characters
    )

def test_search_characters():
    """Test para verificar la búsqueda de personajes por descripción"""
    # Buscar personajes que contengan "conejo" en su descripción
    response = client.get("/characters/search", params={"query": "conejo"})
    assert response.status_code == 200
    characters = response.json()
    assert len(characters) > 0
    assert all("conejo" in char["description"].lower() for char in characters)

def test_search_characters_no_results():
    """Test para verificar búsqueda sin resultados"""
    response = client.get("/characters/search", params={"query": "personaje inexistente xyz"})
    assert response.status_code == 200
    characters = response.json()
    assert len(characters) == 0

def test_search_characters_validation():
    """Test para verificar la validación de la longitud mínima de búsqueda"""
    response = client.get("/characters/search", params={"query": "ab"})
    assert response.status_code == 422  # Validation error 