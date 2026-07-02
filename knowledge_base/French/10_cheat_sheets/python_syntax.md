# Aide-mémoire de syntaxe Python

Référence rapide pour la syntaxe Python 3.x et les motifs courants.

---

## Syntaxe de base

### Variables et types de données
```python
# Affectation de variable (aucune déclaration nécessaire)
x = 5
name = "Alice"
is_active = True
price = 19.99

# Vérification du type
type(x)           # <class 'int'>
isinstance(x, int)  # True

# Conversion de type
int("5")          # 5
str(5)            # "5"
float(5)          # 5.0
bool(1)           # True
```

### Chaînes de caractères
```python
s = "Hello, World!"

# Découpage
s[0]              # 'H'
s[-1]             # '!'
s[0:5]            # 'Hello'
s[7:]             # 'World!'
s[::-1]           # Inverser la chaîne

# Méthodes
s.lower()         # 'hello, world!'
s.upper()         # 'HELLO, WORLD!'
s.split(",")      # ['Hello', ' World!']
s.replace("World", "Python")
s.strip()         # Supprimer les espaces
f"Value: {x}"     # Formatage f-string
```

---

## Flux de contrôle

### Conditions
```python
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("Equals 10")
else:
    print("Less than 10")

# Opérateur ternaire
result = "yes" if condition else "no"
```

### Boucles
```python
# Boucle for
for i in range(5):      # 0 à 4
    print(i)

for item in [1, 2, 3]:
    print(item)

for key, value in dict.items():
    print(key, value)

# Boucle while
while x < 10:
    x += 1

# Contrôle de boucle
break       # Quitter la boucle
continue    # Passer à l'itération suivante
else:       # S'exécute si la boucle se termine sans break
```

---

## Structures de données

### Listes
```python
lst = [1, 2, 3, 4, 5]

lst.append(6)           # Ajouter à la fin
lst.insert(0, 0)        # Insérer à l'indice
lst.remove(3)           # Supprimer par valeur
lst.pop()               # Supprimer et renvoyer le dernier
lst.pop(0)              # Supprimer et renvoyer le premier
lst.index(2)            # Trouver l'indice de la valeur
lst.count(2)            # Compter les occurrences
lst.sort()              # Trier sur place
sorted(lst)             # Renvoyer une copie triée
lst.reverse()           # Inverser sur place
lst[1:4]                # Tranche
[i*2 for i in lst]      # Compréhension de liste
```

### Dictionnaires
```python
d = {"name": "Alice", "age": 30}

d["age"]                # Accéder à la valeur
d.get("age", 0)         # Accès sûr avec valeur par défaut
d.keys()                # Obtenir toutes les clés
d.values()              # Obtenir toutes les valeurs
d.items()               # Obtenir les paires clé-valeur
d.update({"city": "NYC"})
del d["age"]            # Supprimer la clé

{k: v*2 for k, v in d.items()}  # Compréhension de dictionnaire
```

### Ensembles
```python
s = {1, 2, 3, 3, 4}     # {1, 2, 3, 4} - doublons supprimés

s.add(5)
s.remove(3)
s.discard(10)           # Supprimer si présent (pas d'erreur)
s.union({4, 5, 6})      # Combiner des ensembles
s.intersection({2, 3})  # Éléments communs
s.difference({3, 4})    # Éléments dans s mais pas dans l'autre
```

### Tuples
```python
t = (1, 2, 3)
t[0]                    # Accès (immuable)
x, y, z = t             # Dépaquetage
```

---

## Fonctions

### Définition
```python
def greet(name, greeting="Hello"):
    """Docstring : décrire la fonction"""
    return f"{greeting}, {name}!"

# Appel avec arguments positionnels et nommés
greet("Alice")
greet("Bob", greeting="Hi")

# Arguments variables
def sum_all(*args):
    return sum(args)

def print_all(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

### Fonctions lambda
```python
square = lambda x: x ** 2
sorted(lst, key=lambda x: x[1])
```

---

## Classes

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # Variable d'instance
        self.age = age
    
    def greet(self):          # Méthode d'instance
        return f"Hi, I'm {self.name}"
    
    @classmethod
    def from_birth_year(cls, name, year):
        age = 2025 - year
        return cls(name, age)
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# Héritage
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

---

## Entrées/sorties de fichiers

```python
# Lecture de fichiers
with open("file.txt", "r") as f:
    content = f.read()        # Lire le fichier entier
    lines = f.readlines()     # Lire sous forme de liste de lignes

# Écriture de fichiers
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Mode ajout
with open("file.txt", "a") as f:
    f.write("More content\n")
```

---

## Gestion des erreurs

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

# Lever des exceptions
raise ValueError("Invalid value")
```

---

## Modules et imports

```python
import math
from datetime import datetime
from collections import defaultdict, Counter
import numpy as np
from mymodule import my_function as mf

# Modules courants de la bibliothèque standard
os, sys, json, re, random, itertools, functools, pathlib
```

---

## Motifs courants

### Opérations sur les listes
```python
# Filtrer
evens = [x for x in lst if x % 2 == 0]

# Mapper
squares = [x**2 for x in lst]

# Zip
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# Énumérer
for i, val in enumerate(lst):
    print(f"{i}: {val}")
```

### Opérations sur les chaînes
```python
# Joindre une liste de chaînes
", ".join(["a", "b", "c"])  # "a, b, c"

# Découper une chaîne
"a,b,c".split(",")          # ['a', 'b', 'c']

# Vérifier une sous-chaîne
"test" in "this is a test"  # True

# Formater des chaînes
"{} {}".format("Hello", "World")
f"{value:.2f}"              # 2 décimales
```

### Opérations sur les dictionnaires
```python
# Fusionner des dictionnaires
{**d1, **d2}
d1 | d2                     # Python 3.9+

# Valeur par défaut
d.get("key", default_value)

# Itérer
for k, v in d.items():
    pass
```

---

## Fonctions intégrées

```python
len(), str(), int(), float(), bool()
range(), enumerate(), zip()
map(), filter(), reduce()   # reduce vient de functools
sorted(), reversed()
min(), max(), sum()
abs(), round(), pow()
dir(), help(), type()
isinstance(), issubclass()
any(), all()
```

---

## Conseils rapides

- Utiliser `#` pour les commentaires sur une seule ligne
- Utiliser `"""triple quotes"""` pour les docstrings et les chaînes multilignes
- L'indentation est importante (généralement 4 espaces)
- Conventions de nommage : `snake_case` pour les variables/fonctions, `PascalCase` pour les classes
- `__name__ == "__main__"` pour vérifier si le script est exécuté directement
- Utiliser `virtualenv` ou `venv` pour l'isolation des projets
- Installer les paquets avec `pip install package_name`

---

*Dernière mise à jour : juin 2025 | Python 3.x*
