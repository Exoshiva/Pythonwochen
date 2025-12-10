import tkinter as tk
# Ich importieren meine Funktion aus der Datei weather_client.py

from src.api.weather_client import get_weather_data

def button_klick():
    # 1. Hier verarbeite ich den Text und holen das, was der User eingetippt hat
    stadt_name = entry_feld.get()
    
    # 2. Ich rufe die Logik auf und übergeben die Stadt
    wetter_info = get_weather_data(stadt_name)
    
    # 3. Ich aktualisiere das Label mit dem Ergebnis
    label_anzeige.config(text=wetter_info)

# Das ist der GUI-Aufbau
fenster = tk.Tk()
fenster.title("Wetter App v1.0")
fenster.geometry("400x400")

# Überschrift
label_titel = tk.Label(fenster, text="Der Wetter-Check", font=("Arial", 16, "bold"))
label_titel.pack(pady=10)

# Das Eingabefeld (Hier tippt der User z.B. "Hamburg" ein)
entry_feld = tk.Entry(fenster, font=("Arial", 12))
entry_feld.pack(pady=5)
# Jetzt setze ich noch den Fokus direkt ins Feld, damit man gleich tippen kann
entry_feld.focus() 

# Das Ergebnis-Label (es erscheint der Text aus weather_client)
label_anzeige = tk.Label(fenster, text="Bitte Stadt eingeben...", font=("Arial", 11), justify="left")
label_anzeige.pack(pady=20)

# Der Button für den User zum senden der Anfrage
button = tk.Button(fenster, text="Suchen", command=button_klick, font=("Arial", 12))
button.pack(pady=10)


fenster.mainloop()