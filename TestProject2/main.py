import requests
import json
import google.generativeai as genai # Neu: Impport für die KI

# --- KONFIGURATION --- Konstanten (PEP8: UPPER_CASE)
API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_FILE = "daten_export.json"

# Neu: API Key Konfiguration
# API Key hier ein Placeholder (Durch eigenen Key ersetzen!)
GEMINI_API_KEI = "HIER DEINEN KEY EINFÜGEN"
genai.configure(api_key=GEMINI_API_KEI)

# Ich nutze das Flash-Modell (schnell & günstig)
MODEL_NAME = "gemini-1.5-flash"

def hole_daten():
    print(f"Rufe Daten ab von: {API_URL} ...")
    
    try:
        response = requests.get(API_URL)
        
        response.raise_for_status()
        
        daten = response.json()
        print(f"{len(daten)} Datensätze empfangen.")
        return daten
    except Exception as e:
        print(f"Fehler: {e}")
        return []
    
def generiere_mail_draft(user): # Neu: Die KI-Funktion
    """Erstellt einen personalisierten"""
    
    # Daten extrahieren für den Promt
    name = user['name']
    company = user['company']['name']
    slogan = user['company']['catchPhrase']
    
    # Den Promt bauen (F-String)
    promt = (
        f"Schreibe einen sehr kurzen, professionellen E-Mail_Entwurf (auf Deutsch)"
        f"für einen Vertriebler, der {name} von der Firma '{company}' anschreibt."
        f"Beziehe dich lobend auf deren Slogan: '{slogan}'."
        f"Maximal 2-3 Sätze."
    )
    
    try:
        # Modell laden und anfragen
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(promt)
        
        # Anschließend den reinen Text zurückgeben (.text property)
        # .strip() entfernt Leerzeichen vorne/huínten
        return response.text.strip()

    except Exception as e:
        return f"Fehler beim Generieren: {e}"
        
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
        # --- Die List Comprehension ---
        # 1. Filtern (Syntax [ELEMENT for ELEMENT in LISTE if BEDINGUNG])
        biz_users = [user for user in users if user["email"].endswith(".biz")]
        
        print(f"Gefiltert: {len(biz_users)} von {len(users)} Benutzern haben .biz Mails.")
        # Hier wird jetzt nur die gefilterte Liste gespeichert
        speichere_daten(biz_users)
        
        # 2. NEU: KI-Schleife über die gefilterten User
        print("Starte KI-Generierung...")
        
        for user in biz_users:
            print(f" -> Generiere Text für: {user['name']}")
            
            # Hier rufen wir die KI auf
            ki_text = generiere_mail_draft(user)
            
            # Und speichern das Ergebnis direkt im Dictonary des Users
            user["i_email_draft"] = ki_text
            
        # 3. Speichern (jetzt inkl. KI-Text)
        speichere_daten(biz_users)
            
        
