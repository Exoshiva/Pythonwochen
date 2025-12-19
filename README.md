# 🐍 Pythonwochen - FIAE Portfolio

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Security](https://img.shields.io/badge/Security-Bandit%20Scan-green)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)

Willkommen in meinem zentralen Code-Repository!
Dieses Repository dokumentiert meinen Lernfortschritt während meiner **Umschulung zum Fachinformatiker für Anwendungsentwicklung (FIAE)**.

Es dient nicht nur als Sammelbecken für Python-Projekte, sondern als **aktiver DevSecOps-Playground**, in dem ich moderne CI/CD-Pipelines, Sicherheits-Scans und **Clean Code Prinzipien** implementiere.

---

## DevSecOps & Security Features

Ein Hauptfokus dieses Repositories liegt auf **Automatisierung und Sicherheit**.
Jeder Commit durchläuft automatisch eine Security-Pipeline, um unsicheren Code zu verhindern.

### Implementierte Pipelines:
* **GitHub Actions:** Automatisierter Workflow bei jedem Push.
* **GitLab CI:** Plattformunabhängige Konfiguration (`.gitlab-ci.yml`).
* **SAST (Static Application Security Testing):**
    * **Tool:** Bandit
    * **Funktion:** Scannt Python-Code rekursiv auf Sicherheitslücken (z.B. Hardcoded Passwords, Debug-Modus, SQL-Injection Risiken).
    * **Policy:** Der Build schlägt fehl, wenn Sicherheitsrisiken gefunden werden (Quality Gate).
* **Secrets Management:** Konsequente Nutzung von `.env` Dateien und Environment Variables, um API-Keys und sensible Daten aus dem Quellcode fernzuhalten.

---

## Code Quality & Architecture

Neben der Funktionalität lege ich großen Wert auf Wartbarkeit und Lesbarkeit des Codes (besonders in **TestProject6**):

* **Modularisierung (MVC-Ansatz):** Trennung von Logik (`api_handler.py`, `excel_handler.py`), Daten und Oberfläche (`gui.py`, `main.py`).
* **Type Hinting:** Konsequente Nutzung von Python Type Hints (z.B. `def get_weather(city: str) -> dict`) für bessere IDE-Unterstützung und Fehlervermeidung.
* **Error Handling:** Vermeidung von "nackten Excepts". Stattdessen gezieltes Abfangen von Fehlern (z.B. `requests.exceptions.ConnectionError`) für stabile Laufzeiten.
* **Input Validation:** Validierung von Nutzereingaben vor der Verarbeitung (z.B. Prüfung auf leere Strings oder ungültige Zeichen).

---

## Projekt-Übersicht

Das Repository ist in verschiedene Lern-Module unterteilt:

| Projekt | Beschreibung | Tech Stack & Features |
| :--- | :--- | :--- |
| **TestProject1 - 5** | Grundlagen der Programmierung | Python Basics, Algorithmen |
| **TestProject6** | **Wetter-App (OOP & Modular)** | `Tkinter`, `Pandas`, `OpenWeatherMap API`, `OpenPyXL`<br>Feature: Export in Excel, dyn. Dateinamen, Input-Validierung |
| **TestProject7** | Flask Web-App & Dockerisierung | `Flask`, `Docker`, `HTML/CSS` |
| **...** | *Weitere Projekte folgen* | ... |

---

## Technologien & Tools

* **Sprache:** Python 3.9+
* **Frameworks:** Flask, CustomTkinter / Tkinter
* **DevOps:** Docker, Git, GitHub Actions, GitLab CI
* **Security:** Bandit (SAST)
* **IDE:** VS Code (mit GitLens & Extensions)

---

## How to Run

Um die Projekte lokal zu testen (Voraussetzung: Python installiert):

1.  **Repository klonen:**
    ```bash
    git clone [https://github.com/Exoshiva/Pythonwochen.git](https://github.com/Exoshiva/Pythonwochen.git)
    cd Pythonwochen
    ```

2.  **Virtuelle Umgebung erstellen & aktivieren:**
    ```bash
    python -m venv .venv
    # Windows (PowerShell):
    .\.venv\Scripts\Activate.ps1
    # Mac/Linux:
    source .venv/bin/activate
    ```

3.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r TestProject6/requirements.txt
    ```

4.  **Environment Setup (Wichtig für Security!):**
    Erstelle eine `.env` Datei im Projektordner und füge deinen API-Key hinzu:
    ```
    OPENWEATHER_API_KEY=dein_eigener_key
    ```

---

*© 2025 Lars Patzenbein - Built with Coffee, and Clean Code in Dresden.*