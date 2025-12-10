"""
Projekt für die Pythonwoche: OOP Grundlagen - Zugriff auf Attribute

Beschreibung: 
Dieses Skript demonstriert, wie man eine Klasse als reinen Daten-Container nutzt
und von außerhalb (extern) auf die Instanz-Attribute zugreift.
Statt statischer Rückgabewerte werden hier dynamische Instanz-Variablen verwendet.
"""

class Person:
    """
    Eine einfache Klasse, die Eigenschaften einer Person speichert.
    Sie dient als 'Bauplan' für Datenobjekte.
    """
    def __init__(self, name, age, sex):
        # Die Attribute werden hier dynamisch gesetzt
        self.name = name
        self.age = age
        self.sex = sex

# 1. Objekterstellung eines konkreten Objekts 'p1' mit Daten (Name, Alter, Geschlecht)
p1 = Person("Kirby", 25, "Digital")

# 2. Ausgabe: Zugriff auf die Daten von AUSSERHALB der Klasse
# Ich nutze f-Strings (String Interpolation) für die Formatierung.
# Ich rufen keine Methode mehr auf wie im vorherigen Code 
# sondern greife direkt auf p1.name, p1.age etc. zu.
print(f"Hallo mein Name ist {p1.name}. Mein Alter ist {p1.age}, ich bin {p1.sex} und das ist toll.")