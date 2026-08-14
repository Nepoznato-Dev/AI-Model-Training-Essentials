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
# PHP — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| PHP/FI | 1995 | Mga Tool sa Personal na Home Page (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | Unang modernong PHP; Muling isinulat ni Zeev Suraski at Andi Gutmans |
| PHP 4.0 | 2000 | Zend Engine, suporta sa session, buffering ng output |
| PHP 5.0 | 2004 | **modelo ng OOP**, PDO, SQLite, SOAP, mga iterator |
| PHP 5.1 | 2005 | extension ng PDO, mga pagpapahusay sa pagganap |
| PHP 5.2 | 2006 | `json_encode`/`json_decode`,`filter`extension |
| PHP 5.3 | 2009 | **Namespaces**, late static bindings, closures |
| PHP 5.4 | 2012 | Maikling array syntax`[]`, mga katangian, built-in na web server |
| PHP 5.5 | 2013 | Mga Generator,`yield`,`list()`sa mga bagay,`::class`|
| PHP 5.6 | 2014 | Variadic function, pare-pareho ang scalar expression |
| PHP 7.0 | 2015 | **Major**: Zend Engine 3, mga pahiwatig ng uri ng scalar, mga uri ng pagbabalik,`??`|
| PHP 7.1 | 2016 | Mga nullable na uri,`void`return, iterable, class constant visibility |
| PHP 7.2 | 2017 | `object`uri ng pahiwatig, uri ng parameter widening |
| PHP 7.3 | 2018 | Trailing comma sa mga function call,`JsonException`|
| PHP 7.4 | 2019 | **Type properties**, arrow functions, null coalescing assignment |
| PHP 8.0 | 2020 | **Major**: JIT, pinangalanang mga argumento, expression ng pagtutugma, mga uri ng unyon, mga katangian |
| PHP 8.1 | 2021 | Mga enum, mga hibla, mga katangian ng `readonly`, mga uri ng intersection |
| PHP 8.2 | 2022 | `readonly`na mga klase, mga uri ng DNF,`null`/`false`/`true`bilang mga standalone na uri |
| PHP 8.3 | 2023 | Mga uri ng pare-pareho ng klase,`#[\Override]`attribute,`json_validate`|
| PHP 8.4 | 2024 | Property hook,`#[\Deprecated]`attribute, asymmetric visibility |
## Mga Pangunahing Milestone
### PHP/FI at PHP 3 (1995–1999)
- **1995**: Inilabas ni Rasmus Lerdorf ang "Mga Tool sa Personal na Home Page"
- **1998**: PHP 3 — kumpletong muling pagsulat ni Suraski & Gutmans; nagiging isang scripting language
- Mga pangunahing tampok: naka-embed sa HTML, paghawak ng form, suporta sa database
### PHP 4 — Zend Engine (2000–2004)
- **Zend Engine 1**: Compiled bytecode, mas mabilis
- Paghawak ng session, pag-buffer ng output, PEAR
- Unang tunay na panahon ng web development framework
### PHP 5 — Object-Oriented PHP (2004–2014)
- **5.0**: Kumpletuhin ang OOP rewrite — mga klase, interface, exception, PDO
- **5.3**: Namespaces (kritikal para sa modernong PHP), pagsasara, late static bindings
- **5.4**: Mga katangian, short array syntax`[]`, built-in na web server
- **5.5**: Mga Generator (`yield`), `finally`
### PHP 7 — Ang Rebolusyon sa Pagganap (2015–2019)
- **7.0**: Zend Engine 3 — **2x mas mabilis**, mga deklarasyon ng scalar type, mga deklarasyon ng return type
- **7.1**: Mga nullable na uri (`?int`), void return type
- **7.4**: Mga na-type na property, arrow function`fn() =>`, null coalescing assignment `??=`
### PHP 8 — Modernong PHP (2020–kasalukuyan)
- **8.0**: JIT compiler, pinangalanang argumento, match expression, uri ng unyon, attribute (`#[...]`), nullsafe operator`?->`
- **8.1**: Enums, fibers (lightweight concurrency), readonly property, mga uri ng intersection
- **8.2**: Readonly na mga klase, mga uri ng DNF,`null`/`false`/`true`bilang mga standalone na uri
- **8.3**: Mga na-type na constant ng klase,`#[\Override]`,`json_validate()`
- **8.4**: Property hooks,`#[\Deprecated]`, asymmetric visibility
## Uri ng System Evolution
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

## Syntax Evolution
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

## Pangunahing Prinsipyo ng Disenyo
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Paglago ng Ecosystem
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
