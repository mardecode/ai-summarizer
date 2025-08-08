from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.adapters.fastapi_adapter import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Bienvenido a la API de Resumen de Texto 🚀"}

def test_resumidor_endpoint():
    response = client.post("/gemini/flash/", json={"texto": "Hermanitos, hace mucho frío y ustedes la han pasado muy mal, así que disfrutemos la noche al calor de la fogata —dijo la cerdita mayor y encendió la chimenea. Justo en ese momento, los tres cerditos escucharon que tocaban la puerta."})
    assert response.status_code == 200
