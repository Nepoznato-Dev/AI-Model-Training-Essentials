---
# Metadata
title: "Perl — Version History & Evolution"
description: "Comprehensive version history and evolution of Perl from 1.0 to modern Perl."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [perl, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Perl — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| 1.0 | 1987 | İlk sürüm (Larry Wall) |
| 2.0 | 1988 | `study`işlevi, daha iyi normal ifade |
| 3.0 | 1989 | `my`değişkenleri (sözcüksel kapsam) |
| 4.0 | 1991 | `O'Reilly`"Programlama Perl" (Deve kitabı) |
| 5.0 | 1994 | **Ana**: modüller, referanslar, kapanışlar,`use strict`|
| 5.6 | 2000 | `our`,`state`(daha sonra),`v-strings`,`y2k`düzeltmeleri |
| 5.8 | 2002 | **Unicode desteği**, `ithreads`,`open`pragması |
| 5.10 | 2007 | `say`,`//`tanımlanmış-veya,`given`/`when`,`~~`akıllı eşleşme |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(tahribatsız ikame),`package`iyileştirmeleri |
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | Sözcüksel `$_`, karma rastgeleleştirme, koşullu ifadelerde`my`|
| 5.20 | 2014 | **Alt rutin imzaları** (deneysel),`%hash`dilimleme |
| 5.22 | 2015 | `&`referans kaldırma,`<<>>`(güvenli açık) |
| 5.24 | 2016 | Postfix'in referans kaldırma işlemi stabil |
| 5.26 | 2017 | **`while`'deki sözcüksel`$_`**, `@INC`'deki`.`kaldırıldı (güvenlik) |
| 5.28 | 2018 | Anahtar/değer dilimlerinde Unicode 10.0,`delete`|
| 5.30 | 2019 | `for`/`while`koşullarında`my`|
| 5.32 | 2020 | `isa`operatörü, Unicode 13.0 |
| 5.34 | 2021 | `try`/`catch`(deneysel),`defer`blokları |
| 5.36 | 2022 | **`use v5.36`**: imzalar etkin,`$_`varsayılan,`defer`|
| 5.38 | 2023 | `class`anahtar kelimesi (deneysel),`try`/`catch`kararlı |
| 5.40 | 2024 | `^`bitsel operatörler,`for`liste iyileştirmeleri |
| 5.42 | 2025 | Devam eden geliştirme |
## Önemli Kilometre Taşları
### Perl 1–4: Komut Dosyası Çağı (1987–1993)
- **1987**: Larry Wall Perl'ü yayınladı — "Pratik Çıkarma ve Rapor Dili"
- **Hedef**: Sed, awk, grep ve Shell'i tek bir güçlü komut dosyası oluşturma aracında birleştirin
- **3.0**: Sözcüksel kapsam belirleme (`my`)
- **4.0**: The Camel Book — Perl, sistem yöneticisi görevleri için geniş çapta benimsenmeye başlandı
### Perl 5: Altın Çağ (1994–2019)
- **5.0 (1994)**: Tamamen yeniden yazma — **modüller**, **referanslar**, **kapatmalar**, **nesneler**
- **5.6 (2000)**: `our`, v-dizeleri
- **5.8 (2002)**: **Unicode desteği**, yorumlayıcı konuları (`ithreads`)
- **5.10 (2007)**:`say`,`//`(tanımlı-veya),`given`/`when`(anahtar), akıllı eşleşme
- **5.12–5.28**: Artımlı iyileştirmeler, Unicode yükseltmeleri
### Modern Perl (2020-günümüz)
- **5.32 (2020)**:`isa`operatörü (temizleyici tipi kontrolü)
- **5.34 (2021)**:`try`/`catch`(deneysel),`defer`blokları
- **5.36 (2022)**: **`use v5.36`** — imzalar varsayılan olarak etkindir,`$_`varsayılan,`defer`
- **5.38 (2023)**:`class`anahtar kelimesi (deneysel — yerleşik OOP),`try`/`catch`kararlı
- **5.40 (2024)**: Bit bazında operatör iyileştirmeleri
## Söz Dizimi Gelişimi
```perl
# Perl 1-4: Basic scripting
#!/usr/bin/perl
$name = "World";
print "Hello, $name\n";

# Perl 5.0: References, closures, modules
use strict;
use warnings;
my $greeting = sub { "Hello, $_[0]" };
print $greeting->("World");

# Perl 5.8: Unicode
use utf8;
my $text = "café";

# Perl 5.10: say, defined-or
use v5.10;
say "Hello!";
my $value = $input // 'default';

# Perl 5.20: Subroutine signatures (experimental)
use experimental 'signatures';
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.36: Modern Perl
use v5.36;
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.38: class keyword (experimental)
use experimental 'class';
class Dog {
    field $name :param;
    field $breed :param;
    method bark { say "$name says Woof!" }
}
my $dog = Dog->new(name => "Rex", breed => "Lab");
```

## CPAN Ekosistemi
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Temel Tasarım İlkeleri
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Ekosistem Büyümesi
```
1987: Perl 1.0 — sysadmin scripting
1994: Perl 5.0 — modules, OOP, the web CGI era
1995: CPAN launched — module ecosystem
2000: Perl powers the early web (CGI scripts)
2002: Perl 5.8 — Unicode, ithreads
2005: Catalyst, Dancer — web frameworks
2007: Perl 5.10 — modern syntax additions
2010: Moose — modern OOP (meta-object protocol)
2022: Perl 5.36 — modern defaults
2025: Perl still powers sysadmin, bioinformatics, legacy web apps
       CPAN: 200,000+ modules; used by cPanel, DuckDuckGo
```
