import os
import requests
from dotenv import load_dotenv

# 1. Lädt die Konfiguration aus der .env Datei
load_dotenv()

# 2. Holt den Key sicher aus der Umgebung
api_key = os.getenv("OPENWEATHER_API_KEY")

# Sicherheits-Check: Falls die .env Datei fehlt oder leer ist
if not api_key:
    print("FEHLER: Kein API-Key gefunden! Hast du die .env Datei erstellt?")
    exit() # Beendet das Programm sofort

city = input("Hallo! Bitte gib eine Stadt ein: ")

# Hier wird der sichere Key verwendet
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

# Prüfen, ob die Stadt gefunden wurde (Status Code 200 = OK)
if response.status_code == 200:
    data = response.json()

    temperatur = data["main"]["temp"]
    gefühlt = data["main"]["feels_like"]
    beschreibung = data["weather"][0]["description"]
    feuchtigkeit = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print(f"\n--- Wetterbericht für {city} ---")
    print(f"Temperatur: {temperatur}°C")
    print(f"Gefühlt: {gefühlt}°C")
    print(f"Beschreibung: {beschreibung}")
    print(f"Luftfeuchtigkeit: {feuchtigkeit}%")
    print(f"Wind: {wind} m/s")
    
    # Deine Zusammenfassung
    print(f"\nIn {city} beträgt die Temperatur {temperatur}°C gefühlt {gefühlt}°C. Die Luftfeuchtigkeit beträgt {feuchtigkeit}%.")
    print("Wetter-Check beendet!")

else:
    print("Fehler: Stadt nicht gefunden oder API-Problem!")