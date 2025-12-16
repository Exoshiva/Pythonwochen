import customtkinter as ctk
# Importierung der Module 
import api_handler # Importiert Daten von api_handller.py
import excel_handler # Importiert daten von excel_handler.py

class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # --- Grundeinstellungen für das Design ---
        ctk.set_appearance_mode("System") # Modi: "System" (Standard), "Dark", "Light")
        ctk.set_default_color_theme("blue") # Themes: "blue" (Standard), "green", "dark-blue")
        
        # Das Fenster Setup der App
        self.title("Wetter App v1.1")
        self.geometry("400x500")
        
        # Die UI der App
        self.create_widgets()
        
    def create_widgets(self):
        # Die Überschrift der App
        self.label_titel = ctk.CTkLabel(self, text="Der Wetter-Check", font=("Arial", 16, "bold"))
        self.label_titel.pack(pady=20)
        # Fokus wird auf das Eingabefeld gelegt
        self.entry_feld = ctk.CTkEntry(self, font=("Arial", 12))
        self.entry_feld.pack(pady=10)
        
        # NEU: Enter-Taste (Return) löst jetzt auch den Klick aus
        self.entry_feld.bind('<Return>', self.button_klick)
        self.entry_feld.focus()
        
        # Das Ereignis-Label
        self.label_anzeige = ctk.CTkLabel(self, text="Bitte Stadt eingeben...", font=("Arial", 11), justify="left")
        self.label_anzeige.pack(pady=20)
        
        # Der Button für den User zum senden der Anfrage
        self.button = ctk.CTkButton(self, text="Suchen", command=self.button_klick, font=("Arial", 12))
        self.button.pack(pady=10)
        
    # Die Logik
    # NEU: Die Funktion kann jetzt ohne Argument (Button-Klick) durch drücken der Enter-Taste aufgerufen werden
    
    # 1. Hier verarbeite ich den Text und hole mir das, was der User eingetippt hat
    def button_klick(self, event=None):
        stadt_name = self.entry_feld.get() # Bezieht sich darauf was der User eingibt um Daten zu Stadt X abrufen zu können
        
        # NEU: Daten holen (gibt jetzt ein Dictonary zurück!)
        ergebnis = api_handler.get_weather_data(stadt_name)
        
        if ergebnis is None:
            self.label_anzeige.configure(text="Bitte Stadt eingeben")
            return
        
        # NEU: Pfüft ob Fehler in der Eingabe drin sind (falscher Stadtname)
        # ### FIX: Prüfen auf "error" UND "Fehler" (da api_handler beides nutzen kann) ###
        if ergebnis.get("error") or ergebnis.get("Fehler"):
            # Fehlertext holen (entweder aus 'error' oder 'Fehler')
            text = ergebnis.get("error") if ergebnis.get("error") else ergebnis.get("Fehler")
            
            #Fehler anzeigen lassen (falls ein Fehler vorhanden ist)
            self.label_anzeige.configure(text=text)
        else:
            # Bei Erfolgreicher Anfrage wird der Text für die Ausgabe in der GUI zusammengebaut
            gui_text = f"Wetter in {ergebnis['stadt']}:\n"\
                        f"Temperatur:{ergebnis['temp']}°C\n"\
                        f"Beschreibung:{ergebnis['desc']}"
            self.label_anzeige.configure(text=gui_text)
            
            # ### FIX: Logik verschoben! ###

            try:
                # NEU: In Excel abspeichern
                msg = excel_handler.save_to_excel(
                    ergebnis['stadt'],
                    ergebnis['temp'],
                    ergebnis['desc']
                )
                print(msg) # NEU: Zur Kontrolle in der Konsole
            except Exception as e:
                print(f"Excel-Problem ignoriert {e}") 
                       
        # 2. Ich rufe die Logik (aus api_handler.py) auf und übergeben die Stadt
        # ich übergebe auch 'self' (also die App), damit der Handler Status-Updates senden kann
        #wetter_info = api_handler.get_weather_data(stadt_name)
        
        # 3. Ich aktualisiere das Label mit dem Ergebnis
        #self.label_anzeige.configure(text=wetter_info)