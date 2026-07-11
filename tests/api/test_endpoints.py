from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_api_calculate_add():
    response = client.post(
        "/api/v1/calculator/",
        json={"a": 10, "b": 5, "operation": "add"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}


def test_api_calculate_subtract():
    response = client.post(
        "/api/v1/calculator/",
        json={"a": 10, "b": 5, "operation": "subtract"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_api_calculate_multiply():
    response = client.post(
        "/api/v1/calculator/",
        json={"a": 10, "b": 5, "operation": "multiply"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 50.0}


def test_api_calculate_divide():
    response = client.post(
        "/api/v1/calculator/",
        json={"a": 10, "b": 5, "operation": "divide"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}


def test_api_calculate_invalid_operation_schema():
    # Pydantic schema validation should block invalid operation literals
    response = client.post(
        "/api/v1/calculator/",
        json={"a": 10, "b": 5, "operation": "invalid_op"},
    )
    assert response.status_code == 422


def test_api_calculate_missing_field():
    # Pydantic schema validation should block missing fields
    response = client.post(
        "/api/v1/calculator/",
        json={"a": 10, "b": 5},
    )
    assert response.status_code == 422
