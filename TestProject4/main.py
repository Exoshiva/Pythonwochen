from src.api.weather_client import hole_wetter

def main():
    print("--- Wetter App Start ---")
    stadt_name = input("Gib eine Stadt ein: ")
    
    wetter_daten = hole_wetter(stadt_name)
    
    if wetter_daten:
        print(f"\n--- Wetterbericht für {wetter_daten['stadt']} ---")
        print(f"Temperatur:      {wetter_daten['temperatur']}°C")
        print(f"Gefühlt:         {wetter_daten['gefühlt']}°C")
        print(f"Beschreibung:    {wetter_daten['beschreibung']}")
        print(f"Luftfeuchtigkeit: {wetter_daten['luftfeuchtigkeit']}%")
        print(f"Wind:            {wetter_daten['wind']} m/s")
        print("--- Ende ---")
    else:
        print("Konnte Wetterdaten nicht laden.")

if __name__ == "__main__":
    main()