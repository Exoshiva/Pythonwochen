import customtkinter as ctk
# Importierung des Api-Moduls 
import api_handler

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
        self.entry_feld.focus()
        
        # Das Ereignis-Label
        self.label_anzeige = ctk.CTkLabel(self, text="Bitte Stadt eingeben...", font=("Arial", 11), justify="left")
        self.label_anzeige.pack(pady=20)
        
        # Der Button für den User zum senden der Anfrage
        self.button = ctk.CTkButton(self, text="Suchen", command=self.button_klick, font=("Arial", 12))
        self.button.pack(pady=10)
        
    # Die Logik
    def button_klick(self):
        # 1. Hier verarbeite ich den Text und hole mir das, was der User eingetippt hat
        stadt_name = self.entry_feld.get()
        
        # 2. Ich rufe die Logik (aus api_handler.py) auf und übergeben die Stadt
        # ich übergebe auch 'self' (also die App), damit der Handler Status-Updates senden kann
        wetter_info = api_handler.get_weather_data(stadt_name)
        
        # 3. Ich aktualisiere das Label mit dem Ergebnis
        self.label_anzeige.configure(text=wetter_info)