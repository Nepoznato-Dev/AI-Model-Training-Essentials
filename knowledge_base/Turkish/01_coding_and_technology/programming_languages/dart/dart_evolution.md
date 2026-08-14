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
# Dart — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| 1.0 | 2013 | İlk sürüm (Google, Lars Bak ve Kasper Lund) |
| 1.2 | 2014 | Dart2JS derleyici iyileştirmeleri |
| 1.3 | 2014 | `async`/`await`desteği |
| 1.4 | 2014 |  `enum`, karışım iyileştirmeleri |
| 1.5 | 2014 | Jeneratörler (`sync*`, `async*`) |
| 1.6 | 2014 | `Future`iyileştirmeleri |
| 1.8 | 2014 | `dart:io`iyileştirmeleri |
| 1.9 | 2015 | Güçlü mod (katılma) |
| 1.11 | 2015 | `Future.then`iyileştirmeleri |
| 1.12 | 2015 | **Güçlü mod** uygulandı |
| 2.0 | 2018 | **Ana**: Ses türü sistemi,`null`güvenlik hazırlığı, koleksiyonların yeniden yazılması |
| 2.1 | 2018 | `int`/`double`birleştirme,`await for`|
| 2.2 | 2019 | `Set`değişmez değeri,`const`koleksiyon iyileştirmeleri |
| 2.3 | 2019 | Koleksiyon`if`, koleksiyon`for`, yayılma operatörü`...`|
| 2.6 | 2019 | Uzatma yöntemleri |
| 2.7 | 2020 | Varsayılan adlandırılmış parametreler |
| 2.10 | 2020 | **Sessiz güvenlik** (katılım) |
| 2.12 | 2021 | **Null güvenliği varsayılan olarak etkindir** |
| 2.13 | 2021 | İnşaatçı yırtılmaları |
| 2.14 | 2021 | `late`iyileştirmeleri, işaretsiz tamsayılar |
| 2.15 | 2021 | Oluşturucu ayırmaları kararlı, genel işlev türleri |
| 2.17 | 2022 | **Süper parametreler**, gelişmiş numaralandırmalar |
| 2.18 | 2022 | Gelişmiş tür çıkarımı |
| 2.19 | 2023 | Kayıtlar ve modeller (önizleme) |
| 3.0 | 2023 | **Ana**: Kayıtlar, kalıplar, sınıf değiştiriciler,`switch`ifadeleri |
| 3.1 | 2023 | Desen iyileştirmeleri, mühürlü sınıflar |
| 3.2 | 2023 | Statik analiz iyileştirmeleri |
| 3.3 | 2024 | Uzantı türleri,`switch`ifade iyileştirmeleri |
| 3.4 | 2024 | `if`öğeleri,`case`iyileştirmeleri |
| 3.5 | 2024 | Makrolar (önizleme), dilde daha fazla iyileştirme |
| 3.6 | 2025 | Devam eden geliştirme |
## Önemli Kilometre Taşları
### Dart 1.x — İlk Yıllar (2013–2017)
- **2013**: Google, yapılandırılmış web programlama için tasarlanan Dart'ı piyasaya sürdü
- **Hedef**: Web geliştirme için JavaScript'i değiştirin (bu tutku daha sonra yeniden şekillendi)
- **1.0**: Sınıflar, arayüzler, izolasyonlar, isteğe bağlı yazma
- **1.3**:`async`/`await`desteği
- **1.9**: Güçlü mod (katı yazmayı etkinleştirme)
- Dart VM Chromium'da kısa süreliğine kullanıldı, ardından kaldırıldı
### Çarpıntı Pivotu (2017–2018)
- **2017**: Flutter çerçevesi duyuruldu — Dart, kullanıcı arayüzü dili oluyor
- Dart amacını buluyor: platformlar arası mobil/masaüstü/web geliştirme
- **2.0 (2018)**: Tamamen yeniden yazma — ses türü sistemi, modern koleksiyonlar
### Dart 2.x — Modern Dart (2018–2023)
- **2.0**: Ses tipi sistem, artık varsayılan olarak`dynamic`yok
- **2.3**:`if`/`for`Koleksiyonu, yayılma operatörü — Flutter widget ağaçları için harika
- **2.6**: Uzatma yöntemleri
- **2.10**: Tamamen sıfır güvenlik (katılım)
- **2.12**: **Varsayılan olarak boş güvenlik etkindir** —`?`null yapılabilir türler
- **2.17**: Süper parametreler (`super.x`), geliştirilmiş numaralandırmalar
### Dart 3.x — Kayıtlar ve Desenler (2023-günümüz)
- **3.0 (2023)**: **Kayıtlar** (anonim veri taşıyıcılar), **örüntüler** (yıkım), **sınıf değiştiriciler** (`sealed`,`final`,`interface`,`base`),`switch`ifadeleri
- **3.3 (2024)**: Uzantı türleri (sıfır maliyetli sarmalayıcılar)
- **3.5 (2024)**: Makro önizlemesi — derleme zamanı metaprogramlaması
## Söz Dizimi Gelişimi
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

## Tür Sistem Gelişimi
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

## Temel Tasarım İlkeleri
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## Ekosistem Büyümesi
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
