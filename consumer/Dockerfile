# Utilizza un'immagine base con Python
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file requirements.txt e installa le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice dell'applicazione
COPY . .

# Definisce il comando di avvio di default (può essere sovrascritto in docker-compose)
CMD ["python", "producer.py"]
