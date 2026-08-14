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
# PHP: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| PHP/FI | 1995 | Strumenti della home page personale (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | Primo PHP moderno; Zeev Suraski e Andi Gutmans riscrivono |
| PHP4.0 | 2000 | Zend Engine, supporto sessione, buffering dell'output |
| PHP5.0 | 2004| **Modello OOP**, PDO, SQLite, SOAP, iteratori |
| PHP5.1 | 2005| Estensione PDO, miglioramenti delle prestazioni |
| PHP5.2 | 2006| `json_encode`/`json_decode`,`filter`estensione |
| PHP 5.3 | 2009| **Spazi dei nomi**, associazioni statiche tardive, chiusure |
| PHP5.4 | 2012| Sintassi dell'array breve`[]`, tratti, server web integrato |
| PHP5.5 | 2013| Generatori,`yield`,`list()`su oggetti,`::class`|
| PHP5.6 | 2014| Funzioni variadiche, espressioni scalari costanti |
| PHP7.0 | 2015| **Principale**: Zend Engine 3, suggerimenti sui tipi scalari, tipi restituiti,`??`|
| PHP7.1 | 2016| Tipi nullable,`void`return, iterabile, visibilità costante della classe |
| PHP7.2 | 2017 | `object`suggerimento tipo, ampliamento tipo parametro |
| PHP7.3 | 2018 | Virgole finali nelle chiamate di funzione,`JsonException`|
| PHP7.4 | 2019 | **Proprietà tipizzate**, funzioni freccia, assegnazione coalescente nulla |
| PHP8.0 | 2020 | **Maggiore**: JIT, argomenti denominati, espressione di corrispondenza, tipi di unione, attributi |
| PHP8.1 | 2021 | Enumerazioni, fibre, proprietà `readonly`, tipi di intersezione |
| PHP8.2 | 2022 |  Classi `readonly`, tipi DNF,`null`/`false`/`true`come tipi autonomi |
| PHP8.3 | 2023 | Costanti di classe digitate, attributo `#[\Override]`,`json_validate`|
| PHP8.4 | 2024 | Hook di proprietà, attributo `#[\Deprecated]`, visibilità asimmetrica |
## Traguardi importanti
### PHP/FI e PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf pubblica "Strumenti per la home page personale"
- **1998**: PHP 3 — riscrittura completa di Suraski & Gutmans; diventa un linguaggio di scripting
- Funzionalità principali: incorporato in HTML, gestione dei moduli, supporto del database
### PHP 4 — Motore Zend (2000–2004)
- **Zend Engine 1**: bytecode compilato, molto più veloce
- Gestione della sessione, buffering dell'output, PEAR
- La prima vera era del framework di sviluppo web
### PHP 5: PHP orientato agli oggetti (2004–2014)
- **5.0**: riscrittura completa dell'OOP: classi, interfacce, eccezioni, PDO
- **5.3**: spazi dei nomi (fondamentali per il PHP moderno), chiusure, collegamenti statici tardivi
- **5.4**: Tratti, sintassi dell'array breve `[]`, server web integrato
- **5.5**: Generatori (`yield`), `finally`
### PHP 7 — La rivoluzione delle prestazioni (2015–2019)
- **7.0**: Zend Engine 3 — **2 volte più veloce**, dichiarazioni di tipo scalare, dichiarazioni di tipo restituito
- **7.1**: tipi Nullable (`?int`), tipo di restituzione void
- **7.4**: proprietà digitate, funzioni freccia `fn() =>`, assegnazione di coalescenza nulla `??=`
### PHP 8: PHP moderno (2020-oggi)
- **8.0**: compilatore JIT, argomenti denominati, espressione di corrispondenza, tipi di unione, attributi (`#[...]`), operatore nullsafe`?->`
- **8.1**: enumerazioni, fibre (concorrenza leggera), proprietà di sola lettura, tipi di intersezione
- **8.2**: classi di sola lettura, tipi DNF,`null`/`false`/`true`come tipi autonomi
- **8.3**: costanti di classe tipizzate,`#[\Override]`,`json_validate()`
- **8.4**: Hook di proprietà,`#[\Deprecated]`, visibilità asimmetrica
## Digitare Evoluzione del sistema
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

## Evoluzione della sintassi
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

## Principi chiave di progettazione
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Crescita dell'ecosistema
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
