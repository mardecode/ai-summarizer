import pytest
from app.ports.resumidor_port import ResumidorPort

class FakeAdapter(ResumidorPort):
    def resumir(self, texto: str) -> str:
        return "Resumen de prueba"

def test_port_resumidor():
    adapter = FakeAdapter()
    texto = "Este es un texto de prueba para resumir."
    resumen = adapter.resumir(texto)
    assert resumen == "Resumen de prueba"
 