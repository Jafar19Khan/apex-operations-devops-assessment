from unittest.mock import patch


def test_readiness_when_database_is_available(client):
    with patch("app.main.database_is_ready", return_value=True):
        response = client.get("/ready")
    assert response.status_code == 200
    assert response.get_json()["database"] == "connected"


def test_readiness_when_database_is_unavailable(client):
    with patch("app.main.database_is_ready", return_value=False):
        response = client.get("/ready")
    assert response.status_code == 503
    assert response.get_json()["status"] == "not_ready"
