import pytest
from app import app  

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to MyApp" in response.data


def test_healthcheck(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_not_found(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404


def test_post_request(client):
    response = client.post("/api/data", json={"key": "value"})
    assert response.status_code == 201
    assert response.json["message"] == "Data received successfully"
