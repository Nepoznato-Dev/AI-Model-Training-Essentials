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

# PHP — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| PHP/FI | 1995 | Kişisel Ana Sayfa Araçları (Rasmus Lerdorf) |
| PHP 3.0 | 1998 | İlk modern PHP; Zeev Suraski ve Andi Gutmans yeniden yazıyor |
| PHP 4.0 | 2000 | Zend Engine, oturum desteği, çıktı arabelleğe alma |
| PHP 5.0 | 2004 | **OOP modeli**, PDO, SQLite, SOAP, yineleyiciler |
| PHP 5.1 | 2005 | PDO uzantısı, performans iyileştirmeleri |
| PHP 5.2 | 2006 | `json_encode`/ `json_decode`,`filter`uzantısı |
| PHP 5.3 | 2009 | **Ad alanları**, son statik bağlamalar, kapatmalar |
| PHP 5.4 | 2012 | Kısa dizi sözdizimi `[]`, özellikler, yerleşik web sunucusu |
| PHP 5.5 | 2013 | Jeneratörler,`yield`, nesneler üzerinde `list()`,`::class`|
| PHP 5.6 | 2014 | Variadik fonksiyonlar, sabit skaler ifadeler |
| PHP7.0 | 2015 | **Ana**: Zend Engine 3, skaler tip ipuçları, dönüş tipleri,`??`|
| PHP 7.1 | 2016 | Null yapılabilir türler,`void`dönüş, yinelenebilir, sınıf sabit görünürlüğü |
| PHP 7.2 | 2017 | `object`türü ipucu, parametre türü genişletme |
| PHP 7.3 | 2018 | İşlev çağrılarında sondaki virgüller,`JsonException`|
| PHP 7.4 | 2019 | **Yazılan özellikler**, ok işlevleri, boş birleştirme ataması |
| PHP 8.0 | 2020 | **Ana**: JIT, adlandırılmış bağımsız değişkenler, eşleşme ifadesi, birleşim türleri, nitelikler |
| PHP 8.1 | 2021 | Numaralandırmalar, fiberler,`readonly`özellikleri, kesişim türleri |
| PHP 8.2 | 2022 | `readonly`sınıfları, DNF türleri, bağımsız türler olarak`null`/`false`/`true`|
| PHP 8.3 | 2023 | Yazılan sınıf sabitleri,`#[\Override]`özelliği,`json_validate`|
| PHP 8.4 | 2024 | Özellik kancaları,`#[\Deprecated]`özelliği, asimetrik görünürlük |
## Önemli Kilometre Taşları
### PHP/FI ve PHP 3 (1995–1999)
- **1995**: Rasmus Lerdorf "Kişisel Ana Sayfa Araçları"nı yayınladı
- **1998**: PHP 3 — Suraski ve Gutmans tarafından tamamen yeniden yazılmıştır; bir betik dili haline gelir
- Anahtar özellikler: HTML'ye gömülü, form işleme, veritabanı desteği
### PHP 4 — Zend Motoru (2000–2004)
- **Zend Engine 1**: Derlenmiş bayt kodu, çok daha hızlı
- Oturum yönetimi, çıktı arabelleğe alma, PEAR
- İlk gerçek web geliştirme çerçevesi dönemi
### PHP 5 — Nesneye Yönelik PHP (2004–2014)
- **5.0**: Tam OOP yeniden yazma — sınıflar, arayüzler, istisnalar, PDO
- **5.3**: Ad alanları (modern PHP için kritik), kapanışlar, geç statik bağlamalar
- **5.4**: Özellikler, kısa dizi sözdizimi `[]`, yerleşik web sunucusu
- **5,5**: Jeneratörler (`yield`), `finally`
### PHP 7 — Performans Devrimi (2015–2019)
- **7.0**: Zend Engine 3 — **2 kat daha hızlı**, skaler tür bildirimleri, dönüş türü bildirimleri
- **7.1**: Null yapılabilir türler (`?int`), geçersiz dönüş türü
- **7,4**: Yazılan özellikler, ok işlevleri `fn() =>`, boş birleştirme ataması `??=`
### PHP 8 — Modern PHP (2020-günümüz)
- **8.0**: JIT derleyicisi, adlandırılmış bağımsız değişkenler, eşleşme ifadesi, birleşim türleri, nitelikler ( `#[...]`), nullsafe operatörü`?->`
- **8.1**: Numaralandırmalar, fiberler (hafif eşzamanlılık), salt okunur özellikler, kesişim türleri
- **8.2**: Salt okunur sınıflar, DNF türleri, bağımsız türler olarak`null`/`false`/ `true`
- **8,3**: Yazılan sınıf sabitleri,`#[\Override]`,`json_validate()`
- **8,4**: Özellik kancaları, `#[\Deprecated]`, asimetrik görünürlük
## Tür Sistem Gelişimi
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

## Söz Dizimi Gelişimi
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

## Temel Tasarım İlkeleri
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## Ekosistem Büyümesi
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
