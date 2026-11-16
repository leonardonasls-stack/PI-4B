FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências do backend
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r ./backend/requirements.txt

# Copia código do backend, frontend e scripts SQL
COPY backend/ ./backend/
COPY frontend/ ./frontend/
COPY sql/ ./sql/

WORKDIR /app/backend

EXPOSE 8000

# O Render injeta a variável PORT dinamicamente; utilizamos sh para expandir $PORT
CMD ["sh", "-c", "uvicorn src.app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
