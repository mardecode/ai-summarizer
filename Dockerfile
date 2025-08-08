FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Code
ADD . /app
WORKDIR /app
RUN uv sync --locked --compile-bytecode

# Launch app
EXPOSE 8000
CMD ["uv","run","uvicorn","app.main:app", "--host=0.0.0.0", "--port=8000"]