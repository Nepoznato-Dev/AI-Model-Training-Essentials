---
# Metadata
title: "Perl — Version History & Evolution"
description: "Comprehensive version history and evolution of Perl from 1.0 to modern Perl."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Perl — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| 1.0 | 1987 | Rilis awal (Larry Wall) |
| 2.0 | 1988 |  Fungsi `study`, regex lebih baik |
| 3.0 | 1989 |  Variabel`my`(pelingkupan leksikal) |
| 4.0 | 1991 | `O'Reilly`"Pemrograman Perl" (Buku Unta) |
| 5.0 | 1994 | **Mayor**: modul, referensi, penutupan,`use strict`|
| 5.6 | 2000 |  Perbaikan `our`,`state`(lebih baru), `v-strings`,`y2k`|
| 5.8 | 2002 | **Dukungan Unicode**, pragma`ithreads`,`open`|
| 5.10 | 2007 | `say`,`//`ditentukan-atau,`given`/`when`,`~~`smartmatch |
| 5.12 | 2010 | `package NAME VERSION`,`...`(yada-yada), Unicode 5.2 |
| 5.14 | 2011 | `s///r`(substitusi non-destruktif), peningkatan`package`|
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | Leksikal`$_`, pengacakan hash,`my`dalam kondisional |
| 5.20 | 2014 | **Tanda tangan subrutin** (eksperimental), pemotongan`%hash`|
| 5.22 | 2015 |  Dereferensi `&`,`<<>>`(terbuka aman) |
| 5.24 | 2016 | Dereferensi postfix stabil |
| 5.26 | 2017 | **Lexical`$_`di`while`**,`.`di`@INC`dihapus (keamanan) |
| 5.28 | 2018 | Unicode 10.0,`delete`pada potongan kunci/nilai |
| 5.30 | 2019 | `my`dalam kondisi`for`/`while`|
| 5.32 | 2020 |  Operator `isa`, Unicode 13.0 |
| 5.34 | 2021 | `try`/`catch`(percobaan), blok`defer`|
| 5.36 | 2022 | **`use v5.36`**: tanda tangan diaktifkan,`$_`default,`defer`|
| 5.38 | 2023 |  Kata kunci`class`(eksperimental),`try`/`catch`stabil |
| 5.40 | 2024 |  Operator bitwise `^`, peningkatan daftar`for`|
| 5.42 | 2025 | Pembangunan yang sedang berlangsung |
## Tonggak Penting
### Perl 1–4: Era Pembuatan Naskah (1987–1993)
- **1987**: Larry Wall merilis Perl — "Ekstraksi Praktis dan Bahasa Laporan"
- **Sasaran**: Menggabungkan sed, awk, grep, shell menjadi satu alat skrip yang hebat
- **3.0**: Pelingkupan leksikal (`my`)
- **4.0**: The Camel Book — Perl diadopsi secara luas untuk tugas-tugas sysadmin
### Perl 5: Zaman Keemasan (1994–2019)
- **5.0 (1994)**: Penulisan ulang lengkap — **modul**, **referensi**, **penutupan**, **objek**
- **5.6 (2000)**:`our`, v-string
- **5.8 (2002)**: **Dukungan Unicode**, thread penerjemah (`ithreads`)
- **5.10 (2007)**:`say`,`//`(ditentukan-atau),`given`/`when`(switch), smartmatch
- **5.12–5.28**: Peningkatan bertahap, peningkatan Unicode
### Perl Modern (2020–sekarang)
- **5.32 (2020)**: Operator`isa`(pemeriksaan tipe lebih bersih)
- **5.34 (2021)**:`try`/`catch`(eksperimental), blok `defer`
- **5.36 (2022)**: **`use v5.36`** — tanda tangan diaktifkan secara default,`$_`default,`defer`
- **5.38 (2023)**: Kata kunci`class`(eksperimental — OOP bawaan),`try`/`catch`stabil
- **5.40 (2024)**: Peningkatan operator bitwise
## Evolusi Sintaks
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

## Ekosistem CPAN
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## Prinsip Desain Utama
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## Pertumbuhan Ekosistem
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
