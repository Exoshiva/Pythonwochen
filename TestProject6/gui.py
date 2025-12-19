from PIL import Image, ImageTk # <--- NEU: Um das Standart Icon von PyInstaller zu ändern (mit eigenem Bild)
import config # <--- Importiert configurationsdaten für 
from datetime import datetime # <--- NEU: Für forecast (Wettervorhersage)
import customtkinter as ctk # Für den Import von Customtkinter
# Importierung der eigenen Module 
import api_handler # Importiert Daten von api_handller.py
import excel_handler # Importiert daten von excel_handler.py
# Pillow um die Bilder der API zu bekommen
from PIL import Image # <--- NEU: Für die Bildverarbeitung
import requests # <--- Neu: um das Bild herunterzuladen
from io import BytesIO # <--- Neu: Um das Bild direkt aus dem Speicher der API zu lesen


class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # --- Grundeinstellungen für das Design ---
        ctk.set_appearance_mode("System") # Modi: "System" (Standard), "Dark", "Light")
        ctk.set_default_color_theme("blue") # Themes: "blue" (Standard), "green", "dark-blue")
        
        # Das Fenster Setup der App
        self.title(config.APP_TITLE) # Version erhöht ;)
        self.geometry(config.WINDOW_SIZE) # <--- Neu: Verweis die Daten aus der Config zu laden 
        
        # --- NEU: Das Fenster-Icon ---
        # Der folgende Codeblock versucht das Icon zu laden.
        # wenn es fehlt, stürzt die App nicht ab sondern nimmt das Standart Icon von CustomTkinter
        try:
            icon_img = ImageTk.PhotoImage(file="app_icon.ico")
            
            # Setzt das Icon für Fenster und Taskleiste
            self.wm_iconphoto(False, icon_img)
        except Exception as e:
            print(f"Hinweis: Fenster-Icon konnte nicht geladen werden: {e}")
        
        # Die UI der App
        self.create_widgets()
        
    def create_widgets(self):
        # Die Überschrift der App
        self.label_titel = ctk.CTkLabel(self, text="Der Wetter-Check", font=("Arial", 16, "bold"))
        self.label_titel.pack(pady=20)
        # Fokus wird hier direkt auf das Eingabefeld gelegt
        self.entry_feld = ctk.CTkEntry(self, font=("Arial", 12))
        self.entry_feld.pack(pady=10)
        
        # Enter-Taste (Return) löst jetzt auch den Klick aus
        self.entry_feld.bind('<Return>', self.button_klick)
        self.entry_feld.focus()

        # Ergebnis-Bereich 
        # 1. Ich nutze einen Container (Frame), damit Icon und Text nebeneinander Platziert werden können
        self.ergebnis_frame = ctk.CTkFrame(self)
        self.ergebnis_frame.pack(pady=10, fill="both", expand=True, padx=60)
        
        # 2. Spalten-Konfiguration (Links Icon, Rechts Text)
        self.ergebnis_frame.grid_columnconfigure(0, weight=1)
        self.ergebnis_frame.grid_columnconfigure(1, weight=2)
        
        # 3. Das Icon-Label (Links) - Hier landet das Bild 
        self.label_icon = ctk.CTkLabel(self.ergebnis_frame, text="")
        self.label_icon.grid(row=0, column=0, padx=25, pady=10)
        
        # 4. Das Text Label (Rechts)
        self.label_anzeige = ctk.CTkLabel(self.ergebnis_frame, text="Bitte Stadt eingeben", font=("Arial", 14), justify="left", anchor="w")
        self.label_anzeige.grid(row=0, column=1, sticky="w", padx=(10, 0)) # sticky="w" (w = West) und klebt am Icon Container
        
        # 5. Jetzt noch ein Extra Label für Fehleranzeigen (ganz unten) # <--- wird noch nicht angezeigt (Fixen!)
        self.error_label = ctk.CTkLabel(self, text="", text_color="red", font=("Arial", 12))
        self.error_label.pack(pady=5) 
        
        # 6. Der Button für den User zum senden der Anfrage
        self.button = ctk.CTkButton(self, text="Wetter abrufen", command=self.button_klick, font=("Arial", 12))
        self.button.pack(pady=10)
        
        # 7. Container für die 5-Tage-Vorschau (ganz unten) # <--- NEU: Für die Wettervorhersage
        self.forecast_label = ctk.CTkLabel(self, text="5-Tage-Trend (Mittags)", font=("Arial", 12, "bold"))
        self.forecast_label.pack(pady=(20, 5)) # <--- Breite 20, Abstand zum anderen Container 5 in der Y-Achse (senkrecht)
        
        self.forecast_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.forecast_frame.pack(fill="x", padx=10, pady=5)
        
    # --- Die Logik ---
    
    # Die Funktion kann jetzt ohne Argument (Button-Klick) durch drücken der Enter-Taste aufgerufen werden
    # 1. Hier verarbeite ich den Text und hole mir das, was der User eingetippt hat
    def button_klick(self, event=None):
        stadt_name = self.entry_feld.get() # Bezieht sich darauf was der User eingibt um Daten zu Stadt X abrufen zu können
        
        # Daten holen (gibt jetzt ein Dictonary zurück!)
        ergebnis = api_handler.get_weather_data(stadt_name)
        
        if ergebnis is None:
            self.label_anzeige.configure(text="Eingabe darf nicht leer sein!") # <--- NEU: Änderung vorgenommen 
            return
        
        # Prüft ob Fehler in der Eingabe drin sind (falscher Stadtname)
        if ergebnis.get("error") or ergebnis.get("Fehler"):
            # Fehlertext holen (entweder aus 'error' oder 'Fehler')
            text = ergebnis.get("error") if ergebnis.get("error") else ergebnis.get("Fehler")
            
            #Fehler anzeigen lassen (falls ein Fehler vorhanden ist)
            self.error_label.configure(text=text) # <--- KORREKTUR: Nutzung des error_labels
            self.label_icon.configure(image=None) # <--- NEU: Bei Fehler wird das Bild entfernt
            self.label_anzeige.configure(text="")
        else:
            # Bei Erfolgreicher Anfrage wird der Text für die Ausgabe in der GUI zusammengebaut
            gui_text = f"Wetter in {ergebnis['stadt']}:\n"\
                        f"Temperatur:{ergebnis['temp']}°C\n"\
                        f"Beschreibung:{ergebnis['desc']}\n"\
                        f"Windgeschwindkeit:{ergebnis['wind']} km/h\n"\
                        f"Luftfeuchtigkeit:{ergebnis['hum']}%"
            
            self.label_anzeige.configure(text=gui_text)
            
            # Icon laden und anzeigen
            icon_code = ergebnis['icon'] #z.B. "10b" (wird von der API im Hintergrund mitgeliefert)
            self.load_and_show_icon(icon_code)
            
            # --- NEU: Vorhersage laden ---
            forecast_data = api_handler.get_forecast_data(stadt_name)
            self.update_forecast_ui(forecast_data)       

            try:
                # In Excel abspeichern
                msg = excel_handler.save_to_excel(
                    ergebnis['stadt'],
                    ergebnis['temp'],
                    ergebnis['desc'],
                    ergebnis['wind'],
                    ergebnis['hum']
                )
                print(msg) # Zur Kontrolle in der Konsole
            except Exception as e:
                print(f"Excel-Problem ignoriert {e}") 
                
        # --- Logik Ende ---
                
    # --- Logik um die Bilder zu erhalten ---             
    def load_and_show_icon(self, icon_code):
        """
        Läd das Icon aus der OpenWeatherMap und zeigt es im Label an.
        """
        # Die URL zum Bild
        # ### DEBUG START: Um zu sehen ob es klappt und was passiert ###
        url = f"http://openweathermap.org/img/wn/{icon_code}@4x.png"
        print(f"DEBUG: Versuche Bild zu laden von {url}")
        #### DEBUG ENDE ###
        try:
                
            # Request senden (stream=True ist wichtig für Bilddaten)
            response = requests.get(url, stream=True)
            response.raise_for_status()
                
            # Bilddatei aus dem Speicher lesen
            img_data = Image.open(BytesIO(response.content))
                
            # Hier wandeln wir das Bild in CTkImage und passen die größe an
            my_image = ctk.CTkImage(light_image=img_data, dark_image=img_data, size=(100, 100))
                
            # Jetzt weisen wir alles dem Label zu
            self.label_icon.configure(image=my_image)
            self.label_icon.image = my_image # Hier halten wir die Referenz ein (Garbage Collector Schutz)
                
        except Exception as e:
            print(f"Fehler beim Laden des Icons: {e}")
    # --- Logik Ende --  
    
    # --- Logik für die Wettervorhersage ---         
    def update_forecast_ui(self, forecast_data):
        """
        Baut 5 kleine Karten unten im Fenster auf.
        """
        # 1. Alte Karten löschen (falls man 2x klickt)
        for widget in self.forecast_frame.winfo_children():
            widget.destroy()
        if not forecast_data:
            return
        
        # 2. Schleife durch die 5 Tage
        for day in forecast_data:
            # Es wird eine Karte (Frame) pro Tag angezeigt
            card = ctk.CTkFrame(self.forecast_frame, width=80)
            card.pack(side="left", padx=5, expand=True, fill="both")
            
            # Datum in Wochentag umwandeln
            dt_obj = datetime.strptime(day['datum'], "%Y-%m-%d %H:%M:%S")
            wochentag = dt_obj.strftime("%a") # z.B. "Mon", "Tue" etc.
            
            # Label: Tag
            lbl_day = ctk.CTkLabel(card, text=wochentag, font=("Arial", 12, "bold"))
            lbl_day.pack(pady=(5, 0))
            
            # Kleineres Icon laden
            try:
                icon_url = f"http://openweathermap.org/img/wn/{day['icon']}@2x.png"
                resp = requests.get(icon_url)
                img_data = Image.open(BytesIO(resp.content))
                # Kleineres Icon für die Übersicht (50x50)
                icon_img = ctk.CTkImage(img_data, size=(50, 50))
                
                lbl_icon = ctk.CTkLabel(card, text="", image=icon_img) 
                lbl_icon.pack(pady=0)
            except Exception as e:
                print(e)

            
            # Label: Temperatur
            lbl_temp = ctk.CTkLabel(card, text=f"{round(day['temp'])}C", font=("Arial", 12, "bold"))
            lbl_temp.pack(pady=(0, 5))
                
                
                
        
        
                

