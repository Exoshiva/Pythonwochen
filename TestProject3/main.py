def greeting():
    """Begrüßt den Benutzer global."""
    string = "Hallo User"
    print(string)

greeting()

print("-----------------------")

class Person:
    """
    Eine Klasse, um eine Person mit Namen und Alter zu repräsentieren.
    """
    def __init__(self, name, age):
        # Hier werden die Attribute gesetzt, die wir beim Erstellen übergeben
        self.name = name 
        self.age = age
        
    def introduce(self):
        """Gibt eine Vorstellung der Person auf der Konsole aus."""
        # Sauberer f-String statt Verkettung mit +
        print(f"Hello my Name is {self.name}")

# Instanziierung (Objekt erstellen)
p1 = Person("Kirby", 25)

# Methodenaufruf
p1.introduce()

print("-----------------------")