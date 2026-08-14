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
# PHP — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| PHP/FI | 1995 | Alat Halaman Beranda Pribadi (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | PHP modern pertama; Zeev Suraski & Andi Gutman menulis ulang |
| PHP 4.0 | 2000 | Zend Engine, dukungan sesi, buffering keluaran |
| PHP 5.0 | 2004 | **Model OOP**, PDO, SQLite, SOAP, iterator |
| PHP 5.1 | 2005 | Ekstensi PDO, peningkatan kinerja |
| PHP 5.2 | 2006 |  Ekstensi`json_encode`/`json_decode`,`filter`|
| PHP 5.3 | 2009 | **Namespace**, binding statis akhir, penutupan |
| PHP 5.4 | 2012 | Sintaks array pendek `[]`, ciri-ciri, server web bawaan |
| PHP 5.5 | 2013 | Generator,`yield`,`list()`pada objek,`::class`|
| PHP 5.6 | 2014 | Fungsi variadik, ekspresi skalar konstan |
| PHP 7.0 | 2015 | **Utama**: Zend Engine 3, petunjuk tipe skalar, tipe kembalian,`??`|
| PHP 7.1 | 2016 | Tipe nullable, pengembalian `void`, iterable, visibilitas konstan kelas |
| PHP 7.2 | 2017 |  Petunjuk tipe `object`, pelebaran tipe parameter |
| PHP 7.3 | 2018 | Tanda koma di akhir pemanggilan fungsi,`JsonException`|
| PHP 7.4 | 2019 | **Properti yang diketik**, fungsi panah, penetapan penggabungan nol |
| PHP 8.0 | 2020 | **Mayor**: JIT, argumen bernama, ekspresi kecocokan, tipe gabungan, atribut |
| PHP 8.1 | 2021 | Enum, serat, properti `readonly`, tipe persimpangan |
| PHP 8.2 | 2022 |  Kelas `readonly`, tipe DNF,`null`/`false`/`true`sebagai tipe mandiri |
| PHP 8.3 | 2023 | Konstanta kelas yang diketik, atribut `#[\Override]`,`json_validate`|
| PHP 8.4 | 2024 | Kait properti, atribut `#[\Deprecated]`, visibilitas asimetris |
## Tonggak Penting
### PHP/FI dan PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf merilis "Personal Home Page Tools"
- **1998**: PHP 3 — penulisan ulang lengkap oleh Suraski & Gutmans; menjadi bahasa skrip
- Fitur utama: tertanam dalam HTML, penanganan formulir, dukungan basis data
### PHP 4 — Mesin Zend (2000–2004)
- **Zend Engine 1**: mengkompilasi bytecode, jauh lebih cepat
- Penanganan sesi, buffering keluaran, PEAR
- Era kerangka pengembangan web nyata pertama
### PHP 5 — PHP Berorientasi Objek (2004–2014)
- **5.0**: Selesaikan penulisan ulang OOP — kelas, antarmuka, pengecualian, PDO
- **5.3**: Namespace (penting untuk PHP modern), penutupan, pengikatan statis akhir
- **5.4**: Sifat, sintaksis array pendek`[]`, server web bawaan
- **5.5**: Generator (`yield`), `finally`
### PHP 7 — Revolusi Kinerja (2015–2019)
- **7.0**: Zend Engine 3 — **2x lebih cepat**, deklarasi tipe skalar, deklarasi tipe pengembalian
- **7.1**: Tipe nullable (`?int`), tipe pengembalian tidak berlaku
- **7.4**: Properti yang diketik, fungsi panah`fn() =>`, penetapan penggabungan nol `??=`
### PHP 8 — PHP modern (2020–sekarang)
- **8.0**: Kompiler JIT, argumen bernama, ekspresi kecocokan, tipe gabungan, atribut (`#[...]`), operator nullsafe`?->`
- **8.1**: Enum, serat (konkurensi ringan), properti hanya baca, jenis perpotongan
- **8.2**: Kelas hanya baca, tipe DNF,`null`/`false`/`true`sebagai tipe mandiri
- **8.3**: Konstanta kelas yang diketik,`#[\Override]`,`json_validate()`
- **8.4**: Pengait properti,`#[\Deprecated]`, visibilitas asimetris
## Ketik Evolusi Sistem
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

## Evolusi Sintaks
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

## Prinsip Desain Utama
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Pertumbuhan Ekosistem
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
