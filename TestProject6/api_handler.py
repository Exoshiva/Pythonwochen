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