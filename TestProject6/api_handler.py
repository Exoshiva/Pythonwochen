import requests
import os
from dotenv import load_dotenv


# 1. Umgebungsvariablen aus der .env laden (mit dotenv_load)
load_dotenv() 

# 2. Hiermit wird der Key sauber aus der .env geholt
api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather_data(city):
    """
        Diese Funktion ruft die Wetterdaten ab und gibt sie zurück.
    """
    if not city:
        return None # NEU: Rückgabe von nichts bei leerer Eingabe
    
    # 3. API-URL aufbauen (Metrisch für Celsius, lang=de für deutsche Texte)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric" 
    
    try:
        # 3.1 Anfrage senden
        response = requests.get(url)
        # Prüft ob die API fehler meldet (z.B. 404 Stadt nicht gefunden)
        response.raise_for_status() 

        # 4. JSON Daten auspacken
        data = response.json()
        
        # Jetzt das Dictonary aufrufen
        return {
            "stadt": city,
            "temp": data['main']['temp'],
            "desc": data['weather'][0]['description'],
            "hum": data['main']['humidity'],
            "wind": data['wind']['speed'],
            "icon": data['weather'][0]['icon'],
            "error": None # Kein Fehler (Anfrage wird gestartet)
        }
    
    except requests.exceptions.HTTPError:  
        # Eine spezielle Meldung wenn Stadt nicht gefunden wurde (404)
        return {"error": "Die Stadt wurde nicht gefunden"} 
    except requests.exceptions.ConnectionError:
        # Fehlermeldung wenn keine Internetverbindung besteht
        return {"error": "Keine Internetverbindung"}
   
    except Exception as e:
        # Dies gibt alle anderen Fehler aus
        return {"error": f"Fehler: {e}"}
    
    # --- NEU: Funktion für die Wettervorhersage ---
def get_forecast_data(city):
    """
    Holt die 5-Tage-Vorhersage und filtert einen Wert pro Tag heraus.
    """
    if not city:
        return None
    # Die neue URL für "forecast" statt "weather"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data =response.json()
        
        filtered_forecast = []
        # Die API liefert alle 3h Daten. Ich möchte aber nur 1x pro Tag (mittags) abrufen
        # Jetzt suchen wir Einträge, die '12:00:00' im Zeitstempel haben.
        for item in data['list']:
            if "12:00:00" in item['dt_txt']: # dt = DateTime
                filtered_forecast.append({
                    "datum": item['dt_txt'], # Format: "2025-12-16 12:00:00"
                    "temp": item['main']['temp'], # <--- Wetter Temperatur
                    "desc": item['weather'][0]['description'], # <--- Wetter Beschreibung
                    "icon": item['weather'][0]['icon'] # <--- Passendes Wetter Bild
                })
        # Falls wir zufällig vor 12 Uhr abrufen und der heutige Tag fehlt, nehmen wir die ersten 5 Treffer
        return filtered_forecast[:5] # Begrenzt auf die ersten 5 Einträge
    except Exception as e:
        print(f"Vorhersage-Fehler: {e}")
        return None 
    