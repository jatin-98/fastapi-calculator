def test_api_calculate_add(client):
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "10 + 5"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}


def test_api_calculate_subtract(client):
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "10 - 5"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_api_calculate_multiply(client):
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "10 * 5"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 50.0}


def test_api_calculate_divide(client):
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "10 / 5"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}


def test_api_calculate_chained(client):
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "1 + 5 + 7 - 2"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 11.0}


def test_api_calculate_invalid_expression(client):
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": "invalid_op"},
    )
    # The service raises ValueError, endpoint returns 400
    assert response.status_code == 400


def test_api_calculate_missing_field(client):
    # Pydantic schema validation should block missing fields
    response = client.post(
        "/api/v1/calculator/",
        json={"wrong_field": "10 + 5"},
    )
    assert response.status_code == 422


def test_api_calculate_empty_string(client):
    # Pydantic schema validation should block empty strings due to min_length=1
    response = client.post(
        "/api/v1/calculator/",
        json={"expression": ""},
    )
    assert response.status_code == 422
