# main.py
import uvicorn

from app.adapters.fastapi_adapter import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
