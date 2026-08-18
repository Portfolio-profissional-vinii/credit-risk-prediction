from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "API Operacional"

def test_predict_endpoint():
    payload = {
        "loan_amnt": 15000,
        "int_rate": 11.5,
        "annual_inc": 75000,
        "dti": 18.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "probabilidade_inadimplencia" in response.json()
    assert response.json()["recomendacao"] in ["Aprovado", "Reprovado"]