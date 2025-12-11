import customtkinter as ctk
# Ich importieren meine Funktion aus der Datei weather_client.py

from src.api.weather_client import get_weather_data
# --- Grundeinstellungen für das Design ---
ctk.set_appearance_mode("System")  # Modi: "System" (Standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (Standard), "green", "dark-blue"

def button_klick():
    # 1. Hier verarbeite ich den Text und hole mir das, was der User eingetippt hat
    stadt_name = entry_feld.get()
    
    # 2. Ich rufe die Logik auf und übergeben die Stadt
    wetter_info = get_weather_data(stadt_name)
    
    # 3. Ich aktualisiere das Label mit dem Ergebnis
    # WICHTIG: In CustomTkinter heißt es .configure(), nicht .config()
    label_anzeige.configure(text=wetter_info)

# Der GUI-Aufbau
fenster = ctk.CTk()
fenster.title("Wetter App v1.1")
fenster.geometry("400x500") # höhe verändert

# Überschrift
# KORREKTUR: ctk.CTkLabel statt ctk.CTk.Label
label_titel = ctk.CTkLabel(fenster, text="Der Wetter-Check", font=("Arial", 16, "bold"))
label_titel.pack(pady=20)

# Das Eingabefeld (Hier tippt der User z.B. "Hamburg" ein)
# KORREKTUR: ctk.CTkEntry statt ctk.CTk.Entry
entry_feld = ctk.CTkEntry(fenster, font=("Arial", 12))
entry_feld.pack(pady=10)
# Jetzt setze ich noch den Fokus direkt ins Feld, damit man gleich tippen kann
entry_feld.focus() 

# Das Ergebnis-Label (es erscheint der Text aus weather_client)
# KORREKTUR: ctk.CTkLabel statt ctk.CTk.Label
label_anzeige = ctk.CTkLabel(fenster, text="Bitte Stadt eingeben...", font=("Arial", 11), justify="left")
label_anzeige.pack(pady=20)

# Der Button für den User zum senden der Anfrage
# Hier warst du schon fast richtig, ctk.CTkButton ist korrekt (ohne Punkt dazwischen)
button = ctk.CTkButton(fenster, text="Suchen", command=button_klick, font=("Arial", 12))
button.pack(pady=10)


fenster.mainloop()