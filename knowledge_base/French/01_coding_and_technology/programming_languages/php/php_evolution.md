---
# Metadata
title: "PHP — Version History & Evolution"
description: "Comprehensive version history and evolution of PHP from 1.0 to modern PHP."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [php, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# PHP — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| PHP/FI | 1995 | Outils de page d'accueil personnelle (Rasmus Lerdorf) |
| PHP3.0 | 1998 | Premier PHP moderne ; Zeev Suraski et Andi Gutmans réécrivent |
| PHP4.0 | 2000 | Zend Engine, prise en charge des sessions, mise en mémoire tampon de sortie |
| PHP5.0 | 2004 | **Modèle POO**, PDO, SQLite, SOAP, itérateurs |
| PHP5.1 | 2005 | Extension PDO, améliorations des performances |
| PHP5.2 | 2006 | `json_encode`/`json_decode`, extension`filter`|
| PHP5.3 | 2009 | **Espaces de noms**, liaisons statiques tardives, fermetures |
| PHP5.4 | 2012 | Syntaxe de tableau court`[]`, traits, serveur Web intégré |
| PHP5.5 | 2013 | Générateurs,`yield`,`list()`sur objets,`::class`|
| PHP5.6 | 2014 | Fonctions variadiques, expressions scalaires constantes |
| PHP7.0 | 2015 | **Majeur** : Zend Engine 3, astuces de type scalaire, types de retour,`??`|
| PHP7.1 | 2016 | Types nullables, retour `void`, itérable, visibilité constante de classe |
| PHP7.2 | 2017 |  Indice de type `object`, élargissement du type de paramètre |
| PHP7.3 | 2018 | Virgules de fin dans les appels de fonction,`JsonException`|
| PHP7.4 | 2019 | **Propriétés typées**, fonctions fléchées, affectation de fusion nulle |
| PHP8.0 | 2020 | **Majeur** : JIT, arguments nommés, expression de correspondance, types d'union, attributs |
| PHP8.1 | 2021 | Énumérations, fibres, propriétés `readonly`, types d'intersection |
| PHP8.2 | 2022 |  Classes `readonly`, types DNF,`null`/`false`/`true`en tant que types autonomes |
| PHP8.3 | 2023 | Constantes de classe typées, attribut `#[\Override]`,`json_validate`|
| PHP8.4 | 2024 | Hooks de propriété, attribut `#[\Deprecated]`, visibilité asymétrique |
## Étapes majeures
### PHP/FI et PHP 3 (1995-1999)
- **1995** : Rasmus Lerdorf lance "Personal Home Page Tools"
- **1998** : PHP 3 — réécriture complète par Suraski & Gutmans ; devient un langage de script
- Fonctionnalités clés : intégré dans HTML, gestion des formulaires, prise en charge des bases de données
### PHP 4 — Moteur Zend (2000-2004)
- **Zend Engine 1** : bytecode compilé, beaucoup plus rapide
- Gestion de session, mise en mémoire tampon de sortie, PEAR
- Première véritable ère de framework de développement web
### PHP 5 — PHP orienté objet (2004-2014)
- **5.0** : Réécriture complète de la POO — classes, interfaces, exceptions, PDO
- **5.3** : Espaces de noms (critiques pour PHP moderne), fermetures, liaisons statiques tardives
- **5.4** : Traits, syntaxe de tableau courte `[]`, serveur Web intégré
- **5.5** : Générateurs (`yield`), `finally`
### PHP 7 — La révolution des performances (2015-2019)
- **7.0** : Zend Engine 3 — **2x plus rapide**, déclarations de type scalaire, déclarations de type de retour
- **7.1** : types nullables (`?int`), type de retour vide
- **7.4** : Propriétés typées, fonctions fléchées `fn() =>`, affectation de fusion nulle `??=`
### PHP 8 — PHP moderne (2020-présent)
- **8.0** : compilateur JIT, arguments nommés, expression de correspondance, types d'union, attributs (`#[...]`), opérateur nullsafe`?->`
- **8.1** : Énumérations, fibres (concurrence légère), propriétés en lecture seule, types d'intersection
- **8.2** : classes en lecture seule, types DNF,`null`/`false`/`true`en tant que types autonomes
- **8.3** : Constantes de classe typées,`#[\Override]`,`json_validate()`
- **8.4** : Propriétés hooks,`#[\Deprecated]`, visibilité asymétrique
## Évolution du système de types
```
PHP 4:    No type hints
PHP 5.0:  Class type hints
PHP 5.1:  Array type hint
PHP 7.0:  Scalar types (int, string, float, bool), return types
PHP 7.1:  Nullable types (?int), void, iterable
PHP 7.2:  object type
PHP 7.4:  Typed properties
PHP 8.0:  Union types (int|string), mixed
PHP 8.1:  Intersection types (A&B), never, first-class callable syntax
PHP 8.2:  DNF types ((A&B)|C), null/false/true standalone
PHP 8.3:  Typed class constants
PHP 8.4:  Property hooks (get/set)
```

## Évolution de la syntaxe
```php
// PHP 3/4: Basic scripting
$users = array(1, 2, 3);

// PHP 5.4: Short array syntax
$users = [1, 2, 3];

// PHP 5.3: Namespaces
namespace App\Models;

// PHP 7.0: Scalar types
function add(int $a, int $b): int { return $a + $b; }

// PHP 7.4: Arrow functions
$doubled = array_map(fn($x) => $x * 2, $numbers);

// PHP 8.0: Named arguments, match
$result = process(value: $input, strict: true);
$label = match($status) { 0 => 'inactive', 1 => 'active', default => 'unknown' };

// PHP 8.1: Enums
enum Status: string { case Active = 'active'; case Inactive = 'inactive'; }

// PHP 8.4: Property hooks
class User {
    public string $name { get => strtoupper($this->name); set; }
}
```

## Principes de conception clés
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Croissance de l'écosystème
```
1995: PHP/FI — personal tool
2000: PHP 4 + PEAR — package management begins
2004: PHP 5 + OOP — enterprise adoption
2008: Composer (dependency management) — modern PHP ecosystem
2011: Laravel framework — elegant PHP
2015: PHP 7 — performance revolution
2020: PHP 8 — JIT, modern features
2025: PHP powers ~75% of websites with known server-side language
       WordPress, Wikipedia, Slack, Mailchimp all run on PHP
```
