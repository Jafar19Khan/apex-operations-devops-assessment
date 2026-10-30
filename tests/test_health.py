def test_health_returns_200_and_healthy(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_root_returns_service_information(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["service"] == "apex-operations-api"
