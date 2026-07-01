<!-- 
Diese Datei wurde automatisch vom Englischen ins Deutsche übersetzt.
Quelle: coding_languages.md
Hinweis: Technische Begriffe, Codebeispiele und Eigennamen können auf Englisch bleiben.
Für Verbesserungen der Genauigkeit tragen Sie bitte Bearbeitungen über Pull Requests bei.
-->

# Programmiersprachen

## Python

Python ist eine hochrangige, interpretierte, dynamisch typisierte Allzweck-Programmiersprache. Sie betont Lesbarkeit und verwendet signifikante Einrückung als Blockbegrenzer.

### Grundlegende Syntax

```python
# Variablen und Typen
name: str = "Alice"
alter: int = 30
punktzahl: float = 9.5
aktiv: bool = True

# Bedingte Anweisungen
if alter >= 18:
    print("Erwachsener")
elif alter >= 13:
    print("Jugendlicher")
else:
    print("Kind")

# Schleifen
for i in range(5):
    print(i)

while aktiv:
    aktiv = False
```

### Funktionen und Typannotationen

```python
def begriessen(name: str, anzahl: int = 1) -> str:
    return (f"Hallo, {name}! " * anzahl).strip()
```

### Listenkomprehensionen

```python
quadrate = [x**2 for x in range(10)]
gerade = [x for x in range(20) if x % 2 == 0]
```

### Klassen und OOP

```python
class Person:
    def __init__(self, name: str, alter: int):
        self.name = name
        self.alter = alter
    
    def vorstellen(self) -> str:
        return f"Ich heiße {self.name} und bin {self.alter} Jahre alt."
```

## JavaScript

JavaScript ist eine interpretierte, objektorientierte und ereignisgesteuerte Programmiersprache, die hauptsächlich für die Webentwicklung auf Client- und Serverseite verwendet wird.

### Grundlegende Syntax

```javascript
// Variablen und Typen
let name = "Alice";
const alter = 30;
let punktzahl = 9.5;
let aktiv = true;

// Bedingte Anweisungen
if (alter >= 18) {
    console.log("Erwachsener");
} else if (alter >= 13) {
    console.log("Jugendlicher");
} else {
    console.log("Kind");
}

// Schleifen
for (let i = 0; i < 5; i++) {
    console.log(i);
}

while (aktiv) {
    aktiv = false;
}
```

### Funktionen

```javascript
function begriessen(name, anzahl = 1) {
    return `Hallo, ${name}! `.repeat(anzahl).trim();
}

// Pfeilfunktion
const begriessenArrow = (name, anzahl = 1) => {
    return `Hallo, ${name}! `.repeat(anzahl).trim();
};
```

### Array-Manipulation

```javascript
const zahlen = [1, 2, 3, 4, 5];
const quadrate = zahlen.map(x => x ** 2);
const gerade = zahlen.filter(x => x % 2 === 0);
const summe = zahlen.reduce((acc, x) => acc + x, 0);
```

## Java

Java ist eine kompilierte, objektorientierte und plattformunabhängige Programmiersprache, die weit verbreitet in Unternehmensanwendungen und der Android-Entwicklung ist.

### Grundlegende Syntax

```java
// Variablen und Typen
String name = "Alice";
int alter = 30;
double punktzahl = 9.5;
boolean aktiv = true;

// Bedingte Anweisungen
if (alter >= 18) {
    System.out.println("Erwachsener");
} else if (alter >= 13) {
    System.out.println("Jugendlicher");
} else {
    System.out.println("Kind");
}

// Schleifen
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

while (aktiv) {
    aktiv = false;
}
```

### Klassen und OOP

```java
public class Person {
    private String name;
    private int alter;
    
    public Person(String name, int alter) {
        this.name = name;
        this.alter = alter;
    }
    
    public String vorstellen() {
        return "Ich heiße " + name + " und bin " + alter + " Jahre alt.";
    }
}
```

## C++

C++ ist eine kompilierte, leistungsstarke und vielseitige Programmiersprache, die für Systeme, Videospiele und kritische Anwendungen verwendet wird.

### Grundlegende Syntax

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // Variablen und Typen
    string name = "Alice";
    int alter = 30;
    double punktzahl = 9.5;
    bool aktiv = true;
    
    // Bedingte Anweisungen
    if (alter >= 18) {
        cout << "Erwachsener" << endl;
    } else if (alter >= 13) {
        cout << "Jugendlicher" << endl;
    } else {
        cout << "Kind" << endl;
    }
    
    // Schleifen
    for (int i = 0; i < 5; i++) {
        cout << i << endl;
    }
    
    while (aktiv) {
        aktiv = false;
    }
    
    return 0;
}
```

## Grundlagen des Codierens (Sprachunabhängig)

Die grundlegenden Programmierkonzepte sind allen Sprachen gemeinsam:

- **Variablen**: Benannte Datenspeicherung
- **Datentypen**: Definition der Art der Daten (Zahlen, Text, Boolesche Werte usw.)
- **Kontrollstrukturen**: Bedingte Anweisungen (if/else) und Schleifen (for, while)
- **Funktionen**: Wiederverwendbare Codeblöcke
- **Datenstrukturen**: Arrays, Listen, Wörterbücher, Mengen
- **Objektorientierte Programmierung**: Klassen, Objekte, Vererbung, Polymorphie
- **Fehlerbehandlung**: Try/catch, Ausnahmen
- **Ein-/Ausgabe**: Lesen und Schreiben von Daten

Diese grundlegenden Konzepte gelten unabhängig von der gewählten Programmiersprache. Die Beherrschung dieser Grundlagen ermöglicht das leichtere Erlernen neuer Sprachen.
