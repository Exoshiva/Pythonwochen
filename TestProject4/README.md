# Wetter-Check App v1.0

Dies ist eine einfache Wetter-App mit einer grafischen Benutzeroberfläche (GUI), die ich im Rahmen meiner Python-Wochen erstellt habe.

## Funktion

Die App ermöglicht es dem Nutzer, einen Stadtnamen einzugeben und die aktuellen Wetterdaten (Temperatur, gefühlte Temperatur, Min/Max, Wind) über die OpenWeatherMap API abzurufen.

## Screenshot

Hier ist ein Blick auf die Benutzeroberfläche:

![Screenshot der Wetter App GUI](Wetter_app_gui.png)

## Struktur

Das Projekt folgt einer MVC-ähnlichen Struktur:
* `src/api/weather_client.py`: Logik für den API-Aufruf.
* `main_gui.py` `weather_client.py` GUI und Programmablauf.