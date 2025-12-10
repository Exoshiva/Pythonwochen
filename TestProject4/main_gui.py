import tkinter as tk

def button_klick():
    # Meine importierte Wetterabfrage
    label_anzeige.config(text="Geben Sie eine Stadt ein.")

# 1. Das Hauptfenster
fenster = tk.Tk()
fenster.title("Wetter App v1.0")
fenster.geometry("400x300") # Breite x Höhe

# 2. Einen Text (Label) hinzufügen
label_anzeige = tk.Label(fenster, text="Drück den Knopf für Wetter", font=("Arial", 14))
label_anzeige.pack(pady=20) # pady ist der Abstand nach oben/unten

# 3. Einen Button hinzufügen
button = tk.Button(fenster, text="Wetter abrufen", command=button_klick)
button.pack()

# 4. Hält das Fenster offen.
fenster.mainloop()