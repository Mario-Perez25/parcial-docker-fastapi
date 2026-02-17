from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get():
    response = client.get("/")
    assert response.status_code == 200

def test_post():
    response = client.post(
        "/predict",
        json={"edad": 30, "ingresos": 3000}
    )
    assert response.status_code == 200
    assert "prediccion" in response.json()
