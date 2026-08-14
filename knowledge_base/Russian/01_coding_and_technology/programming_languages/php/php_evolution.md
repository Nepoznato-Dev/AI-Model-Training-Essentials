---
# Metadata
title: "PHP — Version History & Evolution"
description: "Comprehensive version history and evolution of PHP from 1.0 to modern PHP."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# PHP — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| PHP/ФИ | 1995 | Инструменты для личной домашней страницы (Расмус Лердорф) |
| PHP 3.0 | 1998 | Первый современный PHP; Зеев Сураски и Энди Гутманс переписывают сценарий |
| PHP 4.0 | 2000 | Zend Engine, поддержка сеансов, буферизация вывода |
| PHP 5.0 | 2004 | **ООП-модель**, PDO, SQLite, SOAP, итераторы |
| PHP 5.1 | 2005 | Расширение PDO, улучшение производительности |
| PHP 5.2 | 2006 | `json_encode`/`json_decode`, расширение`filter`|
| PHP 5.3 | 2009 | **Пространства имен**, поздние статические привязки, замыкания |
| PHP 5.4 | 2012 | Синтаксис короткого массива `[]`, черты, встроенный веб-сервер |
| PHP 5.5 | 2013 | Генераторы,`yield`,`list()`на объектах,`::class`|
| PHP 5.6 | 2014 | Вариадические функции, постоянные скалярные выражения |
| PHP 7.0 | 2015 | **Основное**: Zend Engine 3, подсказки скалярного типа, возвращаемые типы,`??`|
| PHP 7.1 | 2016 | Типы, допускающие значение NULL, возврат `void`, итерируемость, видимость констант класса |
| PHP 7.2 | 2017 |  Подсказка типа `object`, расширение типа параметра |
| PHP 7.3 | 2018 | Завершающие запятые в вызовах функций,`JsonException`|
| PHP 7.4 | 2019 | **Типизированные свойства**, стрелочные функции, объединение значений NULL |
| PHP 8.0 | 2020 | **Основные**: JIT, именованные аргументы, выражение соответствия, типы объединения, атрибуты |
| PHP 8.1 | 2021 | Перечисления, волокна, свойства `readonly`, типы пересечений |
| PHP 8.2 | 2022 |  Классы `readonly`, типы DNF,`null`/`false`/`true`как отдельные типы |
| PHP 8.3 | 2023 | Типизированные константы класса, атрибут `#[\Override]`,`json_validate`|
| PHP 8.4 | 2024 | Перехватчики свойств, атрибут `#[\Deprecated]`, асимметричная видимость |
## Основные вехи
### PHP/FI и PHP 3 (1995–1999)
- **1995**: Расмус Лердорф выпускает «Инструменты для личной домашней страницы».
- **1998**: PHP 3 — полная переработка Suraski & Gutmans; становится языком сценариев
- Ключевые особенности: встроенный в HTML, обработка форм, поддержка баз данных.
### PHP 4 — Zend Engine (2000–2004 гг.)
- **Zend Engine 1**: скомпилированный байт-код намного быстрее.
- Обработка сеансов, буферизация вывода, PEAR
- Первая настоящая эра фреймворков веб-разработки.
### PHP 5 — объектно-ориентированный PHP (2004–2014 гг.)
- **5.0**: Полная переработка ООП — классы, интерфейсы, исключения, PDO.
- **5.3**: Пространства имен (критически важные для современного PHP), замыкания, поздние статические привязки.
- **5.4**: признаки, синтаксис короткого массива `[]`, встроенный веб-сервер.
- **5.5**: Генераторы (`yield`), `finally`
### PHP 7 — революция производительности (2015–2019 гг.)
- **7.0**: Zend Engine 3 — **в 2 раза быстрее**, объявления скалярных типов, объявления возвращаемых типов.
- **7.1**: типы, допускающие значение NULL (`?int`), тип возвращаемого значения void.
- **7.4**: Типизированные свойства, функции стрелок`fn() =>`, нулевое объединенное присвоение `??=`
### PHP 8 — Современный PHP (с 2020 г. по настоящее время)
- **8.0**: JIT-компилятор, именованные аргументы, выражение соответствия, типы объединения, атрибуты (`#[...]`), нулевой оператор `?->`. 
- **8.1**: перечисления, волокна (облегченный параллелизм), свойства только для чтения, типы пересечений.
- **8.2**: классы только для чтения, типы DNF,`null`/`false`/`true`как отдельные типы.
- **8.3**: Константы типизированного класса, `#[\Override]`, `json_validate()`. 
- **8.4**: перехватчики свойств, `#[\Deprecated]`, асимметричная видимость.
## Эволюция системы типов
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

## Эволюция синтаксиса
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

## Ключевые принципы проектирования
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Рост экосистемы
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
