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
# PHP — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| PHP/FI | 1995 | Narzędzia osobistej strony głównej (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | Pierwszy nowoczesny PHP; Zeev Suraski i Andi Gutmans piszą na nowo |
| PHP 4.0 | 2000 | Zend Engine, obsługa sesji, buforowanie wyjścia |
| PHP 5.0 | 2004 | **Model OOP**, PDO, SQLite, SOAP, iteratory |
| PHP 5.1 | 2005 | Rozszerzenie PDO, ulepszenia wydajności |
| PHP 5.2 | 2006 | `json_encode`/`json_decode`,`filter`rozszerzenie |
| PHP 5.3 | 2009 | **Przestrzenie nazw**, późne powiązania statyczne, zamknięcia |
| PHP 5.4 | 2012 | Składnia krótkiej tablicy`[]`, cechy, wbudowany serwer WWW |
| PHP 5.5 | 2013 | Generatory,`yield`,`list()`na obiektach,`::class`|
| PHP 5.6 | 2014 | Funkcje wariadyczne, stałe wyrażenia skalarne |
| PHP 7.0 | 2015 | **Główne**: Zend Engine 3, wskazówki dotyczące typów skalarnych, typy zwrotów,`??`|
| PHP 7.1 | 2016 | Typy dopuszczające wartość null, zwrot `void`, iterowalność, stała widoczność klasy |
| PHP 7.2 | 2017 |  Wskazówka dotycząca typu `object`, rozszerzenie typu parametru |
| PHP 7.3 | 2018 | Końcowe przecinki w wywołaniach funkcji,`JsonException`|
| PHP 7.4 | 2019 | **Wpisane właściwości**, funkcje strzałkowe, przypisanie łączenia wartości null |
| PHP 8.0 | 2020 | **Główne**: JIT, nazwane argumenty, wyrażenie dopasowania, typy unii, atrybuty |
| PHP 8.1 | 2021 | Wyliczenia, włókna, właściwości `readonly`, typy przecięć |
| PHP 8.2 | 2022 |  Klasy `readonly`, typy DNF,`null`/`false`/`true`jako typy samodzielne |
| PHP 8.3 | 2023 | Wpisane stałe klasy, atrybut `#[\Override]`,`json_validate`|
| PHP 8.4 | 2024 | Haki właściwości, atrybut `#[\Deprecated]`, widoczność asymetryczna |
## Główne kamienie milowe
### PHP/FI i PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf wydaje „Osobiste narzędzia strony głównej”
- **1998**: PHP 3 — całkowite przepisanie przez Suraski & Gutmans; staje się językiem skryptowym
- Kluczowe funkcje: osadzony w HTML, obsługa formularzy, obsługa baz danych
### PHP 4 — silnik Zend (2000–2004)
- **Zend Engine 1**: Skompilowany kod bajtowy, znacznie szybszy
- Obsługa sesji, buforowanie wyjścia, PEAR
- Pierwsza era prawdziwego frameworka do tworzenia stron internetowych
### PHP 5 — PHP zorientowane obiektowo (2004–2014)
- **5.0**: Kompletne przepisanie OOP — klasy, interfejsy, wyjątki, PDO
- **5.3**: Przestrzenie nazw (krytyczne dla współczesnego PHP), zamknięcia, późne wiązania statyczne
- **5.4**: Cechy, składnia krótkiej tablicy `[]`, wbudowany serwer WWW
- **5.5**: Generatory (`yield`), `finally`
### PHP 7 — rewolucja w wydajności (2015–2019)
- **7.0**: Zend Engine 3 — **2x szybszy**, deklaracje typu skalarnego, deklaracje typu zwracanego
- **7.1**: Typy dopuszczające wartość null (`?int`), zwracany typ void
- **7.4**: Właściwości wpisane, funkcje strzałkowe`fn() =>`, przypisanie koalescencji zerowej `??=`
### PHP 8 — nowoczesny PHP (2020 – obecnie)
- **8.0**: kompilator JIT, nazwane argumenty, wyrażenie dopasowania, typy unii, atrybuty (`#[...]`), operator nullsafe`?->`
- **8.1**: Wyliczenia, włókna (lekka współbieżność), właściwości tylko do odczytu, typy skrzyżowań
- **8.2**: Klasy tylko do odczytu, typy DNF,`null`/`false`/`true`jako typy samodzielne
- **8.3**: Wpisane stałe klasy,`#[\Override]`,`json_validate()`
- **8.4**: Haki właściwości, `#[\Deprecated]`, asymetryczna widoczność
## Wpisz ewolucję systemu
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

## Ewolucja składni
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

## Kluczowe zasady projektowania
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Rozwój ekosystemu
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
