import requests

# Dein API-Key (In echten Projekten verstecken wir den später in einer Config-Datei!)
API_KEY = "8bd2e13d3b0bba705210a56d5a4c53d3"

def hole_wetter(stadt, api_key=API_KEY):
    """
    Ruft das aktuelle Wetter von OpenWeatherMap ab.
    Erwartet einen gültigen API-Key.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": stadt,
        "appid": api_key,
        "units": "metric",
        "lang": "de"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status() # wirft HTTPError bei 400er oder 500er

        data = response.json()
        return {
            "stadt": data["name"],
            "temperatur": data["main"]["temp"],
            "gefühlt": data["main"]["feels_like"],
            "luftfeuchtigkeit": data["main"]["humidity"],
            "beschreibung": data["weather"][0]["description"],
            "wind": data["wind"]["speed"]
        }
        
    except requests.exceptions.HTTPError as e:
        status = response.status_code  # Korrektur: .status_code statt .status.code
        if status == 401:
            print("X ungültiger API-Key (401)")
        elif status == 404:
            print(f"X Stadt '{stadt}' nicht gefunden (404)")
        else:
            print(f"X HTTP-Fehler ({status}): {e}")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"X Verbindungsfehler: {e}")
        return None

# Dieser Block sorgt dafür, dass der Test-Code nur läuft, 
# wenn man die Datei direkt ausführt, aber nicht beim Importieren.
if __name__ == "__main__":
    ergebnis = hole_wetter("Leipzig")
    if ergebnis:
        print(f"Wetter in {ergebnis['stadt']}:")
        print(f" - Temperatur: {ergebnis['temperatur']}°C (gefühlt eher so {ergebnis['gefühlt']}°C)")
        print(f" - Beschreibung: {ergebnis['beschreibung']}")