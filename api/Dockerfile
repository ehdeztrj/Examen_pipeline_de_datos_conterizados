FROM python:3.11-slim

WORKDIR /app

# Instalo SSH
RUN apt-get update && apt-get install -y openssh-client && rm -rf /var/lib/apt/lists/*

# Quito que compruebe estrictamente
RUN mkdir -p ~/.ssh && echo "StrictHostKeyChecking no" >> ~/.ssh/config

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para levantar el servidor FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]