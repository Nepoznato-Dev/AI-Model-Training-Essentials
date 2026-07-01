<!-- 
Ce fichier a été traduit automatiquement de l'anglais vers le français.
Source : coding_languages.md
Note : Les termes techniques, exemples de code et noms propres peuvent rester en anglais.
Pour améliorer la précision, veuillez contribuer avec des modifications via des pull requests.
-->

# Langages de Programmation

## Python

Python est un langage de programmation de haut niveau, interprété, dynamiquement typé et à usage général. Il met l'accent sur la lisibilité et utilise l'indentation significative comme délimiteurs de blocs.

### Syntaxe de base

```python
# Variables et types
name: str = "Alice"
age: int = 30
score: float = 9.5
active: bool = True

# Conditionnels
if age >= 18:
    print("adulte")
elif age >= 13:
    print("adolescent")
else:
    print("enfant")

# Boucles
for i in range(5):
    print(i)

while active:
    active = False
```

### Fonctions et annotations de type

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Bonjour, {name}! " * times).strip()
```

### Listes en compréhension

```python
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

### Classes et POO

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def introduce(self) -> str:
        return f"Je m'appelle {self.name} et j'ai {self.age} ans."
```

## JavaScript

JavaScript est un langage de programmation interprété, orienté objet et événementiel, principalement utilisé pour le développement web côté client et serveur.

### Syntaxe de base

```javascript
// Variables et types
let name = "Alice";
const age = 30;
let score = 9.5;
let active = true;

// Conditionnels
if (age >= 18) {
    console.log("adulte");
} else if (age >= 13) {
    console.log("adolescent");
} else {
    console.log("enfant");
}

// Boucles
for (let i = 0; i < 5; i++) {
    console.log(i);
}

while (active) {
    active = false;
}
```

### Fonctions

```javascript
function greet(name, times = 1) {
    return `Bonjour, ${name}! `.repeat(times).trim();
}

// Fonction fléchée
const greetArrow = (name, times = 1) => {
    return `Bonjour, ${name}! `.repeat(times).trim();
};
```

### Manipulation de tableaux

```javascript
const numbers = [1, 2, 3, 4, 5];
const squares = numbers.map(x => x ** 2);
const evens = numbers.filter(x => x % 2 === 0);
const sum = numbers.reduce((acc, x) => acc + x, 0);
```

## Java

Java est un langage de programmation compilé, orienté objet et multiplateforme, largement utilisé dans les applications d'entreprise et le développement Android.

### Syntaxe de base

```java
// Variables et types
String name = "Alice";
int age = 30;
double score = 9.5;
boolean active = true;

// Conditionnels
if (age >= 18) {
    System.out.println("adulte");
} else if (age >= 13) {
    System.out.println("adolescent");
} else {
    System.out.println("enfant");
}

// Boucles
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

while (active) {
    active = false;
}
```

### Classes et POO

```java
public class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String introduce() {
        return "Je m'appelle " + name + " et j'ai " + age + " ans.";
    }
}
```

## C++

C++ est un langage de programmation compilé, performant et polyvalent, utilisé pour les systèmes, les jeux vidéo et les applications critiques.

### Syntaxe de base

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // Variables et types
    string name = "Alice";
    int age = 30;
    double score = 9.5;
    bool active = true;
    
    // Conditionnels
    if (age >= 18) {
        cout << "adulte" << endl;
    } else if (age >= 13) {
        cout << "adolescent" << endl;
    } else {
        cout << "enfant" << endl;
    }
    
    // Boucles
    for (int i = 0; i < 5; i++) {
        cout << i << endl;
    }
    
    while (active) {
        active = false;
    }
    
    return 0;
}
```

## Fundamentaux du Codage (Agnostique au Langage)

Les concepts fondamentaux de programmation sont communs à tous les langages :

- **Variables** : Stockage de données nommées
- **Types de données** : Définition de la nature des données (nombres, texte, booléens, etc.)
- **Structures de contrôle** : Conditionnels (if/else) et boucles (for, while)
- **Fonctions** : Blocs de code réutilisables
- **Structures de données** : Tableaux, listes, dictionnaires, ensembles
- **Programmation orientée objet** : Classes, objets, héritage, polymorphisme
- **Gestion des erreurs** : Try/catch, exceptions
- **Entrée/Sortie** : Lecture et écriture de données

Ces concepts fondamentaux s'appliquent quel que soit le langage de programmation choisi. La maîtrise de ces bases permet d'apprendre plus facilement de nouveaux langages.
