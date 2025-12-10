import os
import requests
from dotenv import load_dotenv

# 1. Dies läd die Konfiguration aus der .env Datei
load_dotenv()

# 2. Hier hole ich den Key sauber aus der Umgebung
api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather_data(city):
    """_summary_
        Diese Funktion ruft die Wetterdaten ab und gibt sie zurück.
    """
    if not city:
        return "Bitte eine Stadt eingeben"

    # 3. Jetzt der Aufruf der URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Fehler! Stadt nicht gefunden."

        data = response.json()

        # 4. Jetzt gebe ich an was ich ausgelesen haben möchte
        temp = data["main"]["temp"]
        min_temp = data["main"]["temp_min"]
        max_temp = data["main"]["temp_max"]
        humidity = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        
        # Das Ergebnis wird hier für die Ausgabe zusammengebaut
        ergebnis = (f"Wetter in {city}:\n"
                    f"Temperatur: {temp}°C\n"
                    f"Niedrigste erwartete Temperatur in der Region beträgt {min_temp}\n"
                    f"Das Termometer klettert heute maximal bis {max_temp}\n"
                    f"das fühlt sich an wie {humidity}\n"
                    f"Die Windgeschwindigkeit beträgt {wind} km/h\n")
        return ergebnis

# Und wenn das erledigt ist gebe es das zusammengebaute Ergebnis zurück
    except Exception as e:
        print(f"Fehler:{e}")
        return "Fehler: Stadt wurde nicht gefunden oder API-Proplem. Bitte versuchen Sie es erneut."


# Kleiner Test ob es funktioniert
if __name__ == "__main__":
    print(get_weather_data("London"))


    