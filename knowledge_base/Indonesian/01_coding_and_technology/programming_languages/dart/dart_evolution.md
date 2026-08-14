---
# Metadata
title: "Dart — Version History & Evolution"
description: "Comprehensive version history and evolution of Dart from 1.0 to modern Dart."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [dart, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Dart — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| 1.0 | 2013 | Rilis awal (Google, Lars Bak & Kasper Lund) |
| 1.2 | 2014 | Peningkatan kompiler Dart2JS |
| 1.3 | 2014 |  Dukungan`async`/`await`|
| 1.4 | 2014 |  `enum`, peningkatan mix |
| 1.5 | 2014 | Generator (`sync*`,`async*`) |
| 1.6 | 2014 |  Peningkatan`Future`|
| 1.8 | 2014 |  Peningkatan`dart:io`|
| 1.9 | 2015 | Mode kuat (ikut serta) |
| 1.11 | 2015 |  Peningkatan`Future.then`|
| 1.12 | 2015 | **Mode kuat** diterapkan |
| 2.0 | 2018 | **Mayor**: Sistem tipe suara, persiapan keselamatan `null`, penulisan ulang koleksi |
| 2.1 | 2018 |  Penyatuan`int`/ `double`,`await for`|
| 2.2 | 2019 | `Set`literal, peningkatan koleksi`const`|
| 2.3 | 2019 | Koleksi`if`, koleksi`for`, operator penyebaran`...`|
| 2.6 | 2019 | Metode penyuluhan |
| 2.7 | 2020 | Parameter bernama default |
| 2.10 | 2020 | **Keamanan suara nol** (ikut serta) |
| 2.12 | 2021 | **Keamanan nol diaktifkan secara default** |
| 2.13 | 2021 | Robeknya konstruktor |
| 2.14 | 2021 |  Peningkatan `late`, bilangan bulat tak bertanda |
| 2.15 | 2021 | Robekan konstruktor tipe fungsi umum dan stabil |
| 2.17 | 2022 | **Parameter super**, enum yang disempurnakan |
| 2.18 | 2022 | Inferensi tipe yang ditingkatkan |
| 2.19 | 2023 | Catatan dan pola (pratinjau) |
| 3.0 | 2023 | **Mayor**: Catatan, pola, pengubah kelas, ekspresi`switch`|
| 3.1 | 2023 | Perbaikan pola, kelas tersegel |
| 3.2 | 2023 | Peningkatan analisis statis |
| 3.3 | 2024 | Jenis ekstensi, peningkatan ekspresi`switch`|
| 3.4 | 2024 |  Elemen `if`, peningkatan`case`|
| 3,5 | 2024 | Makro (pratinjau), penyempurnaan bahasa lebih lanjut |
| 3.6 | 2025 | Pembangunan yang sedang berlangsung |
## Tonggak Penting
### Dart 1.x - Tahun-Tahun Awal (2013–2017)
- **2013**: Google merilis Dart — dirancang untuk pemrograman web terstruktur
- **Sasaran**: Menggantikan JavaScript untuk pengembangan web (ambisi kemudian berubah)
- **1.0**: Kelas, antarmuka, isolasi, pengetikan opsional
- **1.3**: dukungan`async`/ `await`
- **1.9**: Mode kuat (mengikuti pengetikan ketat)
- Dart VM digunakan sebentar di Chromium, lalu dihapus
### Pivot Flutter (2017–2018)
- **2017**: Kerangka kerja Flutter diumumkan — Dart menjadi bahasa UI
- Dart menemukan tujuannya: pengembangan seluler/desktop/web lintas platform
- **2.0 (2018)**: Penulisan ulang lengkap — sistem tipe suara, koleksi modern
### Panah 2.x — Panah Modern (2018–2023)
- **2.0**: Sistem tipe suara, tidak ada lagi`dynamic`secara default
- **2.3**: Koleksi`if`/`for`, operator penyebaran — cocok untuk pohon widget Flutter
- **2.6**: Metode penyuluhan
- **2.10**: Keamanan tidak terdengar (ikut serta)
- **2.12**: **Keamanan null diaktifkan secara default** — tipe nullable `?`
- **2.17**: Parameter super (`super.x`), enum yang ditingkatkan
### Dart 3.x — Catatan & Pola (2023–sekarang)
- **3.0 (2023)**: **Catatan** (pembawa data anonim), **pola** (penghancuran), **pengubah kelas** (`sealed`,`final`,`interface`,`base`), ekspresi `switch`
- **3.3 (2024)**: Jenis ekstensi (pembungkus tanpa biaya)
- **3.5 (2024)**: Pratinjau makro — metaprogramming waktu kompilasi
## Evolusi Sintaks
```dart
// Dart 1.x: Verbose, JavaScript-like
class Person {
  String name;
  int age;
  Person(this.name, this.age);
}

// Dart 2.0: Sound types
Person createPerson(String name, int age) {
  return Person(name, age);
}

// Dart 2.3: Collection if/for, spread
var widgets = [
  if (showHeader) HeaderWidget(),
  for (var item in items) ItemWidget(item),
  ...otherWidgets,
];

// Dart 2.6: Extension methods
extension StringX on String {
  String get shout => toUpperCase() + '!';
}

// Dart 2.12: Null safety
String? nullable;     // can be null
String nonNullable;   // cannot be null (enforced)

// Dart 2.17: Super parameters, enhanced enums
class NamedPerson extends Person {
  NamedPerson({super.name, super.age});  // pass to super constructor
}

enum Status {
  active('Active'),
  inactive('Inactive');
  final String label;
  const Status(this.label);
}

// Dart 3.0: Records and patterns
(String, int) getNameAndAge() => ('Alice', 30);

sealed class Shape {}
class Circle extends Shape { final double radius; Circle(this.radius); }
class Rect extends Shape { final double w, h; Rect(this.w, this.h); }

String describe(Shape s) => switch (s) {
  Circle(radius: var r) => 'Circle($r)',
  Rect(w: var w, h: var h) => 'Rect(${w}x${h})',
};
```

## Ketik Evolusi Sistem
```
Dart 1.0:  Optional types (annotations only)
Dart 1.9:  Strong mode (opt-in)
Dart 2.0:  Sound type system (enforced)
Dart 2.10: Sound null safety (opt-in)
Dart 2.12: Null safety by default (? nullable, ! assert)
Dart 2.15: Generic function types
Dart 3.0:  Records, sealed classes, patterns, class modifiers
Dart 3.3:  Extension types (zero-cost wrappers)
Dart 3.5:  Macros (compile-time metaprogramming)
```

## Prinsip Desain Utama
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Pertumbuhan Ekosistem
```
2013: Dart 1.0 released by Google
2015: AngularDart — Google uses Dart internally
2017: Flutter announced — Dart finds its purpose
2018: Dart 2.0 — sound type system
2021: Dart 2.12 — null safety
2022: Flutter 3 — iOS, Android, Web, Desktop, Embedded
2023: Dart 3.0 — records, patterns, sealed classes
2025: Flutter + Dart power apps from BMW, Alibaba, Google Pay, Toyota
       pub.dev hosts 30,000+ packages
       Dart runs on: mobile (Flutter), web (dart2wasm), server (dart:io), embedded
```
