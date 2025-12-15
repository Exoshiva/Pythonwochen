from gui import WeatherApp

def main():
    # Erstellt das App-Objekt aus meiner GUI-Klasse
    app = WeatherApp()
    # Hier starte ich den Loop damit das Fenster der App immer offen bleibt
    app.mainloop()
    
if __name__ == "__main__":
    main()
    
