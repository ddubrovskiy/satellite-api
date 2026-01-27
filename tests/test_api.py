# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_satellite():
    response = client.post("/satellites", json={"name": "TestSat", "battery_level": 60.0})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "TestSat"
    assert data["battery_level"] == 60.0

def test_create_invalid_satellite():
    response = client.post("/satellites", json={"name": "BadSat", "battery_level": 200.0})
    assert response.status_code == 422  # Pydantic validation error

def test_get_satellites():
    response = client.get("/satellites")
    assert response.status_code == 200
    assert isinstance(response.json(), list)