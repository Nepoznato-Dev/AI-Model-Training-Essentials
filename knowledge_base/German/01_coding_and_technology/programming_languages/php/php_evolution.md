<!--
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

-->
# PHP – Versionsverlauf und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| PHP/FI | 1995 | Persönliche Homepage-Tools (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | Erstes modernes PHP; Zeev Suraski und Andi Gutmans schreiben neu |
| PHP 4.0 | 2000 | Zend Engine, Sitzungsunterstützung, Ausgabepufferung |
| PHP 5.0 | 2004 | **OOP-Modell**, PDO, SQLite, SOAP, Iteratoren |
| PHP 5.1 | 2005 | PDO-Erweiterung, Leistungsverbesserungen |
| PHP 5.2 | 2006 | `json_encode`/`json_decode`,`filter`Erweiterung |
| PHP 5.3 | 2009 | **Namespaces**, späte statische Bindungen, Abschlüsse |
| PHP 5.4 | 2012 | Kurze Array-Syntax`[]`, Merkmale, integrierter Webserver |
| PHP 5.5 | 2013 | Generatoren,`yield`,`list()`für Objekte,`::class`|
| PHP 5.6 | 2014 | Variadische Funktionen, konstante Skalarausdrücke |
| PHP 7.0 | 2015 | **Major**: Zend Engine 3, Skalartyphinweise, Rückgabetypen,`??`|
| PHP 7.1 | 2016 | Nullable-Typen, `void`-Rückgabe, iterierbar, Sichtbarkeit von Klassenkonstanten |
| PHP 7.2 | 2017 | `object`Typhinweis, Parametertyperweiterung |
| PHP 7.3 | 2018 | Nachgestellte Kommas in Funktionsaufrufen,`JsonException`|
| PHP 7.4 | 2019 | **Typisierte Eigenschaften**, Pfeilfunktionen, Null-Koaleszenzzuweisung |
| PHP 8.0 | 2020 | **Hauptsächlich**: JIT, benannte Argumente, Übereinstimmungsausdruck, Union-Typen, Attribute |
| PHP 8.1 | 2021 | Aufzählungen, Fasern, `readonly`-Eigenschaften, Schnittpunkttypen |
| PHP 8.2 | 2022 |  `readonly`-Klassen, DNF-Typen,`null`/`false`/`true`als eigenständige Typen |
| PHP 8.3 | 2023 | Typisierte Klassenkonstanten, `#[\Override]`-Attribut,`json_validate`|
| PHP 8.4 | 2024 | Eigenschaften-Hooks, `#[\Deprecated]`-Attribut, asymmetrische Sichtbarkeit |
## Wichtige Meilensteine
### PHP/FI und PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf veröffentlicht „Personal Home Page Tools“
- **1998**: PHP 3 – komplette Neufassung durch Suraski & Gutmans; wird zu einer Skriptsprache
- Hauptmerkmale: eingebettet in HTML, Formularverarbeitung, Datenbankunterstützung
### PHP 4 – Zend Engine (2000–2004)
- **Zend Engine 1**: Kompilierter Bytecode, viel schneller
- Sitzungsverwaltung, Ausgabepufferung, PEAR
- Erste echte Webentwicklungs-Framework-Ära
### PHP 5 – Objektorientiertes PHP (2004–2014)
- **5.0**: Vollständiges OOP-Rewrite – Klassen, Schnittstellen, Ausnahmen, PDO
- **5.3**: Namespaces (kritisch für modernes PHP), Abschlüsse, späte statische Bindungen
- **5.4**: Merkmale, kurze Array-Syntax `[]`, integrierter Webserver
- **5.5**: Generatoren (`yield`), `finally`
### PHP 7 – Die Leistungsrevolution (2015–2019)
- **7.0**: Zend Engine 3 – **2x schneller**, Skalartypdeklarationen, Rückgabetypdeklarationen
- **7.1**: Nullable-Typen (`?int`), void-Rückgabetyp
- **7.4**: Typisierte Eigenschaften, Pfeilfunktionen `fn() =>`, Null-Koaleszenzzuweisung `??=`
### PHP 8 – Modernes PHP (2020–heute)
- **8.0**: JIT-Compiler, benannte Argumente, Übereinstimmungsausdruck, Union-Typen, Attribute (`#[...]`), Nullsafe-Operator`?->`
- **8.1**: Aufzählungen, Fasern (leichte Parallelität), schreibgeschützte Eigenschaften, Schnittpunkttypen
- **8.2**: Nur-Lese-Klassen, DNF-Typen,`null`/`false`/`true`als eigenständige Typen
- **8.3**: Typisierte Klassenkonstanten, `#[\Override]`,`json_validate()`
- **8.4**: Eigenschafts-Hooks,`#[\Deprecated]`, asymmetrische Sichtbarkeit
## Typsystementwicklung
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

## Syntaxentwicklung
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

## Wichtige Designprinzipien
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Ökosystemwachstum
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
