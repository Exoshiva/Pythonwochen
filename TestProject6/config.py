# config.py

"""
ZENTRALE KONFIGURATION
----------------------
Hier werden alle Einstellungen, die das Aussehen und Verhalten der App steuern hinterlegt.
Vorteil: Wenn man z.B. den Fenstertitel ändern will, müssen wir das nur hier tun.

WICHTIG ZUR SICHERHEIT:
Sensible Daten (wie API-Keys, Passwörter) gehören NICHT! hier rein, 
sondern in die .env Datei. Diese Datei hier wird nämlich oft geteilt (GitHub),
die .env Datei bleibt aber aus Sicherheitsgründen privat auf dem PC.
"""

# --- GUI Einstellungen ---
APP_TITLE = "Wetter App v1.3"  # Versions-Upgrade ;)
WINDOW_SIZE = "500x525"        # Die perfekte Höhe für Daten + Vorhersage für diese Anwendung

# --- Excel Einstellungen ---
EXCEL_FOLDER = "Wetter-Berichte"
EXCEL_FILENAME = "wetter_report.xlsx"

# --- Design Konstanten (Optional, falls man Farben zentral steuern möchte) ---
FONT_MAIN = ("Arial", 16, "bold")
FONT_NORMAL = ("Arial", 12)