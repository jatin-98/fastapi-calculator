from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_api_calculate_add():
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "10 + 5"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}


def test_api_calculate_subtract():
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "10 - 5"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_api_calculate_multiply():
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "10 * 5"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 50.0}


def test_api_calculate_divide():
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "10 / 5"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}


def test_api_calculate_chained():
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "1 + 5 + 7 - 2"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 11.0}


def test_api_calculate_invalid_expression():
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "invalid_op"},
    )
    # The service raises ValueError, endpoint returns 400
    assert response.status_code == 400


def test_api_calculate_missing_field():
    # Pydantic schema validation should block missing fields
    response = client.post(
        "/api/v1/calculator/",
        json={"wrong_field": "10 + 5"},
    )
    assert response.status_code == 422
