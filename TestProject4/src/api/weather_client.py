import os
import requests
from dotenv import load_dotenv

# 1. Lädt die Konfiguration aus der .env Datei
load_dotenv()

# 2. Holt den Key sicher aus der Umgebung
api_key = os.getenv("OPENWEATHER_API_KEY")
city = input("Hallo! Bitte gib eine Stadt ein: ")
# Aufruf des Key 
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
	data = requests.get(url).json()

	temperatur = data["main"]["temp"]
	gefühlt = data["main"]["feels_like"]
	beschreibung = data["weather"][0]["description"]
	feuchtigkeit = data["main"]["humidity"]
	wind = data["wind"]["speed"]

	print(f"Wetterbericht für {city}:")
	print(f"Temperatur: {temperatur}°C")
	print(f"Gefühlt: {gefühlt}°C")
	print(f"Beschreibung: {beschreibung}")
	print(f"Luftfeuchtigkeit: {feuchtigkeit}%")
	print(f"Wind: {wind} m/s")

	print(f"\nIn {city} beträgt die Temperatur {temperatur}°C und gefühlt {gefühlt}°C. Die Luftfeuchtigkeit beträgt {feuchtigkeit}%.")


except:
	print("Fehler: Stadt nicht gefunden oder API-Problem!")




