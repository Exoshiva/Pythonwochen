import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta # Für Zeitrechnung
# 1. Die .env Datei suchen und laden
load_dotenv() 

# 2. Den Schlüssel sicher aus der "Umgebung" holen
# WICHTIG: In den Klammern muss GENAU der Name stehen, 
# den du in deiner .env Datei links vom = geschrieben hast (z.B. API_KEY oder WEATHER_API_KEY)
api_key = os.getenv("API_KEY")

# Kleiner Test (kannst du später löschen), um zu sehen, ob er geladen wurde:
if api_key:
    print("API Key erfolgreich geladen!")
else:
    print("Fehler: Kein API Key gefunden. Prüfe den Namen in der .env Datei.")
    exit() # Beendet das Programm