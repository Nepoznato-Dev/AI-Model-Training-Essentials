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
# PHP — Version History & Evolution

## Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| PHP/FI  | 1995 | Personal Home Page Tools (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | First modern PHP; Zeev Suraski & Andi Gutmans rewrite |
| PHP 4.0 | 2000 | Zend Engine, session support, output buffering |
| PHP 5.0 | 2004 | **OOP model**, PDO, SQLite, SOAP, iterators |
| PHP 5.1 | 2005 | PDO extension, performance improvements |
| PHP 5.2 | 2006 | `json_encode`/`json_decode`, `filter` extension |
| PHP 5.3 | 2009 | **Namespaces**, late static bindings, closures |
| PHP 5.4 | 2012 | Short array syntax `[]`, traits, built-in web server |
| PHP 5.5 | 2013 | Generators, `yield`, `list()` on objects, `::class` |
| PHP 5.6 | 2014 | Variadic functions, constant scalar expressions |
| PHP 7.0 | 2015 | **Major**: Zend Engine 3, scalar type hints, return types, `??` |
| PHP 7.1 | 2016 | Nullable types, `void` return, iterable, class constant visibility |
| PHP 7.2 | 2017 | `object` type hint, parameter type widening |
| PHP 7.3 | 2018 | Trailing commas in function calls, `JsonException` |
| PHP 7.4 | 2019 | **Typed properties**, arrow functions, null coalescing assignment |
| PHP 8.0 | 2020 | **Major**: JIT, named arguments, match expression, union types, attributes |
| PHP 8.1 | 2021 | Enums, fibers, `readonly` properties, intersection types |
| PHP 8.2 | 2022 | `readonly` classes, DNF types, `null`/`false`/`true` as standalone types |
| PHP 8.3 | 2023 | Typed class constants, `#[\Override]` attribute, `json_validate` |
| PHP 8.4 | 2024 | Property hooks, `#[\Deprecated]` attribute, asymmetric visibility |

## Major Milestones

### PHP/FI and PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf releases "Personal Home Page Tools"
- **1998**: PHP 3 — complete rewrite by Suraski & Gutmans; becomes a scripting language
- Key features: embedded in HTML, form handling, database support

### PHP 4 — Zend Engine (2000–2004)
- **Zend Engine 1**: Compiled bytecode, much faster
- Session handling, output buffering, PEAR
- First real web development framework era

### PHP 5 — Object-Oriented PHP (2004–2014)
- **5.0**: Complete OOP rewrite — classes, interfaces, exceptions, PDO
- **5.3**: Namespaces (critical for modern PHP), closures, late static bindings
- **5.4**: Traits, short array syntax `[]`, built-in web server
- **5.5**: Generators (`yield`), `finally`

### PHP 7 — The Performance Revolution (2015–2019)
- **7.0**: Zend Engine 3 — **2x faster**, scalar type declarations, return type declarations
- **7.1**: Nullable types (`?int`), void return type
- **7.4**: Typed properties, arrow functions `fn() =>`, null coalescing assignment `??=`

### PHP 8 — Modern PHP (2020–present)
- **8.0**: JIT compiler, named arguments, match expression, union types, attributes (`#[...]`), nullsafe operator `?->`
- **8.1**: Enums, fibers (lightweight concurrency), readonly properties, intersection types
- **8.2**: Readonly classes, DNF types, `null`/`false`/`true` as standalone types
- **8.3**: Typed class constants, `#[\Override]`, `json_validate()`
- **8.4**: Property hooks, `#[\Deprecated]`, asymmetric visibility

## Type System Evolution

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

## Key Design Principles

```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Ecosystem Growth

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
