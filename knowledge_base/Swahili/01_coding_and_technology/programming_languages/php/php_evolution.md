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

# PHP - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| PHP/FI | 1995 | Zana za Kibinafsi za Ukurasa wa Nyumbani (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | PHP ya kwanza ya kisasa; Zeev Suraski na Andi Gutmans waandika upya |
| PHP 4.0 | 2000 | Injini ya Zend, usaidizi wa kipindi, uakibishaji wa pato |
| PHP 5.0 | 2004 | **Muundo wa OOP**, PDO, SQLite, SABUNI, viboreshaji |
| PHP 5.1 | 2005 | PDO ugani, utendakazi maboresho |
| PHP 5.2 | 2006 | `json_encode`/`json_decode`,`filter`kiendelezi |
| PHP 5.3 | 2009 | **Nafasi za majina**, vifungashio vilivyochelewa, kufungwa |
| PHP 5.4 | 2012 | Sintaksia fupi ya safu`[]`, sifa, seva ya wavuti iliyojengwa ndani |
| PHP 5.5 | 2013 | Jenereta,`yield`,`list()`kwenye vitu,`::class`|
| PHP 5.6 | 2014 | Utendaji tofauti, misemo ya mara kwa mara ya scalar |
| PHP 7.0 | 2015 | **Meja**: Zend Engine 3, vidokezo vya aina ya scalar, aina za kurejesha,`??`|
| PHP 7.1 | 2016 | Aina zinazoweza kubatilishwa,`void`kurudi, iterable, darasa mwonekano wa mara kwa mara |
| PHP 7.2 | 2017 |  Kidokezo cha aina ya `object`, upanuzi wa aina ya kigezo |
| PHP 7.3 | 2018 | Koma zinazofuata katika simu za kukokotoa,`JsonException`|
| PHP 7.4 | 2019 | **Sifa zilizoainishwa**, vitendaji vya mshale, kazi ya kuunganisha batili |
| PHP 8.0 | 2020 | **Kubwa**: JIT, hoja zilizopewa majina, usemi unaolingana, aina za muungano, sifa |
| PHP 8.1 | 2021 | Enums, nyuzi, mali za `readonly`, aina za makutano |
| PHP 8.2 | 2022 |  Madarasa ya `readonly`, aina za DNF,`null`/`false`/`true`kama aina zinazojitegemea |
| PHP 8.3 | 2023 | Vipindi vya darasa vilivyochapwa, sifa ya `#[\Override]`,`json_validate`|
| PHP 8.4 | 2024 | Kulabu za mali, sifa ya `#[\Deprecated]`, mwonekano wa asymmetric |
## Mafanikio Makuu
### PHP/FI na PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf atoa "Zana za Kibinafsi za Ukurasa wa Nyumbani"
- **1998**: PHP 3 - kamilisha kuandika upya na Suraski & Gutmans; inakuwa lugha ya maandishi
- Vipengele muhimu: iliyoingia katika HTML, utunzaji wa fomu, msaada wa hifadhidata
### PHP 4 — Zend Engine (2000–2004)
- ** Injini ya Zend 1 **: Imekusanywa bytecode, haraka zaidi
- Ushughulikiaji wa kikao, uakibishaji wa pato, PEAR
- Enzi ya kwanza ya mfumo halisi wa ukuzaji wa wavuti
### PHP 5 - PHP Yenye Malengo (2004–2014)
- **5.0**: Kamilisha kuandika upya kwa OOP - madarasa, violesura, vighairi, PDO
- **5.3**: Nafasi za majina (muhimu kwa PHP ya kisasa), kufungwa, vifungo vya kuchelewa tuli
- **5.4**: Sifa, sintaksia fupi ya safu`[]`, seva ya wavuti iliyojengwa ndani
- **5.5**: Jenereta (`yield`), `finally`
### PHP 7 — Mapinduzi ya Utendaji (2015–2019)
- **7.0**: Zend Engine 3 — **2x kasi zaidi**, matamko ya aina ya scalar, matamko ya aina ya kurejesha
- **7.1**: Aina zinazoweza kubatilishwa (`?int`), aina ya kurudi utupu
- **7.4**: Sifa zilizochapwa, vitendaji vya mshale`fn() =>`, mgawo usiofaa wa kuunganisha `??=`
### PHP 8 - PHP ya kisasa (2020-sasa)
- **8.0**: Kikusanyaji cha JIT, hoja zilizopewa jina, usemi unaolingana, aina za muungano, sifa (`#[...]`), opereta nullsafe`?->`
- **8.1**: Enum, nyuzi (fedha nyepesi), mali za kusoma tu, aina za makutano
- **8.2**: Madarasa ya kusoma pekee, aina za DNF,`null`/`false`/`true`kama aina za pekee
- **8.3**: Viunga vya darasa vilivyoandikwa,`#[\Override]`,`json_validate()`
- **8.4**: ndoano za mali,`#[\Deprecated]`, mwonekano wa asymmetric
## Aina ya Mageuzi ya Mfumo
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

## Mageuzi ya Sintaksia
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

## Kanuni Muhimu za Usanifu
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Ukuaji wa Mfumo ikolojia
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
