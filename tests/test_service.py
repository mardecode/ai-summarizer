from app.adapters.gemini_flash_adapter import GeminiFlashAdapter
from app.domain.resumen_service import servicio_resumen

def test_service_resumidor():
    adaptador = GeminiFlashAdapter()
    texto_prueba= "El lobo sopló y resopló con todas sus fuerzas y la casita de palo se vino abajo. Por suerte, los dos cerditos habían corrido hacia la casa de la cerdita mayor mientras que el lobo feroz seguía soplando y resoplando. Los dos hermanos, casi sin respiración le contaron toda la historia."
    resumen = servicio_resumen(texto_prueba, adaptador)
    assert len(resumen) > 0
    assert len(resumen) < len(texto_prueba)
    assert "lobo" in resumen