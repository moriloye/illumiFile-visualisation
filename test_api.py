import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_meta_alerts(client):
    response = client.get("/api/meta_alerts?delta=0.5")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_realtime_aggregation(client):
    response = client.post("/api/realtime_aggregation", json={"alerts": [1, 2, 3], "delta": 0.5})
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert data["processed_alerts"] == 3
