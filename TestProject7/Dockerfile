# Start mit einem offiziellen, leichten Python-Image
FROM python:3.9-slim

# Arbeitsordner im Container erstellen
WORKDIR /app

# requirements-Datei kopieren und Installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Den Rest des Codes Kopieren
CMD ['python', 'app.py']