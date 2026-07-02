# Python-Syntax-Spickzettel

Kurzübersicht für Python-3.x-Syntax und häufige Muster.

---

## Grundlegende Syntax

### Variablen und Datentypen
```python
# Variablenzuweisung (keine Deklaration erforderlich)
x = 5
name = "Alice"
is_active = True
price = 19.99

# Typprüfung
type(x)           # <class 'int'>
isinstance(x, int)  # True

# Typumwandlung
int("5")          # 5
str(5)            # "5"
float(5)          # 5.0
bool(1)           # True
```

### Strings
```python
s = "Hello, World!"

# Slicing
s[0]              # 'H'
s[-1]             # '!'
s[0:5]            # 'Hello'
s[7:]             # 'World!'
s[::-1]           # String umkehren

# Methoden
s.lower()         # 'hello, world!'
s.upper()         # 'HELLO, WORLD!'
s.split(",")      # ['Hello', ' World!']
s.replace("World", "Python")
s.strip()         # Leerraum entfernen
f"Value: {x}"     # f-string-Formatierung
```

---

## Kontrollfluss

### Bedingungen
```python
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equals 10")
else:
    print("Less than 10")

# Ternärer Operator
result = "yes" if condition else "no"
```

### Schleifen
```python
# For-Schleife
for i in range(5):      # 0 bis 4
    print(i)

for item in [1, 2, 3]:
    print(item)

for key, value in dict.items():
    print(key, value)

# While-Schleife
while x < 10:
    x += 1

# Schleifensteuerung
break       # Schleife beenden
continue    # Zur nächsten Iteration springen
else:       # Ausführen, wenn die Schleife ohne break endet
```

---

## Datenstrukturen

### Listen
```python
lst = [1, 2, 3, 4, 5]

lst.append(6)           # Am Ende hinzufügen
lst.insert(0, 0)        # An Index einfügen
lst.remove(3)           # Nach Wert entfernen
lst.pop()               # Letztes Element entfernen und zurückgeben
lst.pop(0)              # Erstes Element entfernen und zurückgeben
lst.index(2)            # Index des Werts finden
lst.count(2)            # Vorkommen zählen
lst.sort()              # An Ort und Stelle sortieren
sorted(lst)             # Sortierte Kopie zurückgeben
lst.reverse()           # An Ort und Stelle umkehren
lst[1:4]                # Slice
[i*2 for i in lst]      # List Comprehension
```

### Dictionaries
```python
d = {"name": "Alice", "age": 30}

d["age"]                # Auf Wert zugreifen
d.get("age", 0)         # Sicherer Zugriff mit Standardwert
d.keys()                # Alle Schlüssel holen
d.values()              # Alle Werte holen
d.items()               # Schlüssel-Wert-Paare holen
d.update({"city": "NYC"})
del d["age"]            # Schlüssel löschen

{k: v*2 for k, v in d.items()}  # Dict Comprehension
```

### Mengen
```python
s = {1, 2, 3, 3, 4}     # {1, 2, 3, 4} - Duplikate entfernt

s.add(5)
s.remove(3)
s.discard(10)           # Entfernen, falls vorhanden (kein Fehler)
s.union({4, 5, 6})      # Mengen zusammenführen
s.intersection({2, 3})  # Gemeinsame Elemente
s.difference({3, 4})    # Elemente in s, aber nicht in der anderen Menge
```

### Tupel
```python
t = (1, 2, 3)
t[0]                    # Zugriff (unveränderlich)
x, y, z = t             # Entpacken
```

---

## Funktionen

### Definition
```python
def greet(name, greeting="Hello"):
    """Docstring: Describe the function"""
    return f"{greeting}, {name}!"

# Mit Positions- und Keyword-Argumenten aufrufen
greet("Alice")
greet("Bob", greeting="Hi")

# Variable Argumente
def sum_all(*args):
    return sum(args)

def print_all(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

### Lambda-Funktionen
```python
square = lambda x: x ** 2
sorted(lst, key=lambda x: x[1])
```

---

## Klassen

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # Instanzvariable
        self.age = age
    
    def greet(self):          # Instanzmethode
        return f"Hi, I'm {self.name}"
    
    @classmethod
    def from_birth_year(cls, name, year):
        age = 2025 - year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# Vererbung
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

---

## Datei-I/O

```python
# Dateien lesen
with open("file.txt", "r") as f:
    content = f.read()        # Gesamte Datei lesen
    lines = f.readlines()     # Als Liste von Zeilen lesen

# Dateien schreiben
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Anhängemodus
with open("file.txt", "a") as f:
    f.write("More content\n")
```

---

## Fehlerbehandlung

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Type or value error")
except Exception as e:
    print(f"General error: {e}")
else:
    print("No errors occurred")
finally:
    print("Always executes")

# Ausnahmen auslösen
raise ValueError("Invalid value")
```

---

## Module und Imports

```python
import math
from datetime import datetime
from collections import defaultdict, Counter
import numpy as np
from mymodule import my_function as mf

# Häufige Standardbibliotheks-Module
os, sys, json, re, random, itertools, functools, pathlib
```

---

## Häufige Muster

### Listenoperationen
```python
# Filtern
evens = [x for x in lst if x % 2 == 0]

# Map
squares = [x**2 for x in lst]

# Zip
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# Enumerate
for i, val in enumerate(lst):
    print(f"{i}: {val}")
```

### String-Operationen
```python
# Liste von Strings verbinden
", ".join(["a", "b", "c"])  # "a, b, c"

# String aufteilen
"a,b,c".split(",")          # ['a', 'b', 'c']

# Teilstring prüfen
"test" in "this is a test"  # True

# Strings formatieren
"{} {}".format("Hello", "World")
f"{value:.2f}"              # 2 Dezimalstellen
```

### Dictionary-Operationen
```python
# Dictionaries zusammenführen
{**d1, **d2}
d1 | d2                     # Python 3.9+

# Standardwert
d.get("key", default_value)

# Iterieren
for k, v in d.items():
    pass
```

---

## Eingebaute Funktionen

```python
len(), str(), int(), float(), bool()
range(), enumerate(), zip()
map(), filter(), reduce()   # reduce aus functools
sorted(), reversed()
min(), max(), sum()
abs(), round(), pow()
dir(), help(), type()
isinstance(), issubclass()
any(), all()
```

---

## Kurztipps

- Verwenden Sie `#` für einzeilige Kommentare
- Verwenden Sie `"""triple quotes"""` für Docstrings und mehrzeilige Strings
- Einrückung ist wichtig (typischerweise 4 Leerzeichen)
- Namenskonventionen: `snake_case` für Variablen/Funktionen, `PascalCase` für Klassen
- `__name__ == "__main__"`, um zu prüfen, ob ein Skript direkt ausgeführt wird
- Verwenden Sie `virtualenv` oder `venv` für Projektisolierung
- Installieren Sie Pakete mit `pip install package_name`

---

*Zuletzt aktualisiert: Juni 2025 | Python 3.x*
