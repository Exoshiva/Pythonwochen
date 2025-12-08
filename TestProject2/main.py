import requests
import json

# Konstanten (PEP8: UPPER_CASE)
API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "daten_export.json"

def hole_daten():
    print(f"Rufe Daten ab von: {API_URL} ...")
    
    try:
        response = requests.get(API_URL)
        #Prüft HTTP 200 OK
        response.raise_for_status()
        
        daten = response.json()
        print(f"{len(daten)} Datensätze empfangen.")
        return daten
    except Exception as e:
        print(f"Fehler: {e}")
        return []
    
def speichere_daten(daten):
    try:
        # encoding="utf-8" ist wichtig für Sonderzeichen
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(daten, file, indent=2, ensure_ascii=False)
        print(f"Daten erfolgreich in {OUTPUT_FILE} gespeichert.")
    except Exception as e:
        print(f"Speicherfehler: {e}")
            
if __name__ == "__main__":
    users = hole_daten()
    
    if users:
        # --- Hier die List Comprehension ---
        # Syntax [ELEMENT for ELEMENT in LISTE if BEDINGUNG]
        biz_users = [users for user in users if user["email"].endswith(".biz")]
        
        print(f"Gefiltert: {len(biz_users)} von {len(users)} Benutzern haben .biz Mails.")
        # Hier wird jetzt nur die gefilterte Liste gespeichert
        speichere_daten(biz_users)
        
