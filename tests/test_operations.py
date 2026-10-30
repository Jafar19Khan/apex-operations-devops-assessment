from unittest.mock import patch


def test_list_operations_returns_items(client):
    with patch("app.main.list_operations", return_value=[]):
        response = client.get("/api/v1/operations")
    assert response.status_code == 200
    assert response.get_json() == {"items": []}


def test_create_operation_rejects_missing_name(client):
    response = client.post("/api/v1/operations", json={"status": "created"})
    assert response.status_code == 400


def test_create_operation_rejects_invalid_status(client):
    response = client.post(
        "/api/v1/operations", json={"name": "demo", "status": "unknown"}
    )
    assert response.status_code == 400


def test_create_operation_returns_created_record(client):
    expected = {"id": 1, "name": "demo", "status": "created"}
    with patch("app.main.create_operation", return_value=expected):
        response = client.post("/api/v1/operations", json={"name": "demo"})
    assert response.status_code == 201
    assert response.get_json() == expected
