from fastapi import FastAPI
from pydantic import BaseModel
from app.domain.resumen_service import servicio_resumen
from app.adapters.gemini_flash_adapter import GeminiFlashAdapter
from app.adapters.gemini_pro_adapter import GeminiProAdapter
from fastapi import HTTPException

app = FastAPI(title="API de Resumen de Texto")


class TextoEntrada(BaseModel):
    texto: str


@app.get("/")
def home():
    """
    Home endpoint.
    """
    return {"mensaje": "Bienvenido a la API de Resumen de Texto 🚀"}


@app.post("/gemini/flash/")
def resumir_gemini_flash(entrada: TextoEntrada):
    """
    Endpoint to summarize text using the Gemini Flash model.
    """
    try:
        adaptador = GeminiFlashAdapter()
        resumen = servicio_resumen(entrada.texto, adaptador)
        return {"resumen": resumen}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Ocurrió un error interno")


@app.post("/gemini/pro/")
def resumir_gemini_pro(entrada: TextoEntrada):
    """
    Endpoint to summarize text using the Gemini Pro model.
    """
    try:
        adaptador = GeminiProAdapter()
        resumen = servicio_resumen(entrada.texto, adaptador)
        return {"resumen": resumen}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Ocurrió un error interno")
