---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [typescript, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# TypeScript — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Çıkış Tarihi | Anahtar Tema |
|-----------|---------------|-----------|
| 0.8 | Ekim 2012 | İlk halka açık yayın (Anders Hejlsberg) |
| 0.9 | Nisan 2013 | Jenerikler |
| 1.0 | Nisan 2014 | İlk kararlı sürüm |
| 1.1 | Kasım 2014 | Derleyici performansı |
| 1.4 | Ocak 2015 | Şablon değişmez türleri (temel),`let`|
| 1.5 | Temmuz 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | Eylül 2015 | `abstract`sınıfları, JSX desteği |
| 1.7 | Kasım 2015 | `async/await`(ES2017 hedefi) |
| 1.8 | Şubat 2016 | Etiketli şablon dizeleri,`--strictNullChecks`|
| 2.0 | Eylül 2016 | **Ana**: Birleşim/kavşak türleri,`never`,`keyof`,`protected`|
| 2.1 | Aralık 2016 |  `keyof`, haritalanmış tipler,`async`jeneratörler |
| 2.2 | Şubat 2017 | `object`tipi, geliştirilmiş`this`|
| 2.3 | Nisan 2017 | Genel varsayılanlar,`--strict`modu |
| 2.4 | Haziran 2017 | Zayıf türler, dize numaralandırmaları |
| 2.5 | Eylül 2017 | İsteğe bağlı yakalama bağlama |
| 2.6 | Ekim 2017 | Katı işlev türleri,`--strictFunctionTypes`|
| 2.7 | Ocak 2018 | Kesin atama (`!`),`const`numaralandırmaları |
| 2.8 | Mart 2018 | **Koşullu tipler**,`Exclude`,`Extract`|
| 2.9 | Haziran 2018 |  Sayısal/sembol için `keyof`,`import()`türleri |
| 3.0 | Temmuz 2018 | **Binbaşı**: Hareketsiz gruplar, `unknown`, proje referansları |
| 3.1 | Eylül 2018 | Tuple'larda eşlenen türler,`readonly`dizileri |
| 3.2 | Kasım 2018 | `bigint`,`object`yayılması |
| 3.4 | Mart 2019 | `const`iddiaları, yüksek dereceli tür çıkarımı |
| 3.5 | Mayıs 2019 | `Omit`yardımcı türü |
| 3.7 | Kasım 2019 | **İsteğe bağlı zincirleme**, birleştirmeyi geçersiz kılma, özyinelemeli türler |
| 3.8 | Şubat 2020 | `type-only`ithalat/ihracat,`#private`alanları |
| 3.9 | Mayıs 2020 |  `// @ts-expect-error`, geliştirilmiş çıkarım |
| 4.0 | Ağu 2020 | **Major**: Variadic demetler, etiketli demetler, şablon değişmez türleri |
| 4.1 | Kasım 2020 | **Şablon değişmez türleri**, anahtarın yeniden eşlenmesi, özyinelemeli koşullu |
| 4.2 | Şubat 2021 | Soyut özellikler, eşlenen türlerde`~`|
| 4.3 | Haziran 2021 | Ayrı yazma türleri,`override`anahtar sözcüğü |
| 4.4 | Ağu 2021 | Sembol/indeks imzaları, kontrol akışının daraltılması |
| 4.5 | Kasım 2021 |  `.js`'den `.d.ts`, `.d.ts`'de`await`|
| 4.6 | Şubat 2022 | Blok kapsamlı fonksiyon kontrolleri, nesne dinlenme kesin türleri |
| 4.7 | Mayıs 2022 | `infer`için`extends`kısıtlamaları, `.ts`'de ESM |
| 4.8 | Ağu 2022 | İyileştirilmiş kavşak azaltma,`--strictNullChecks`düzeltmeleri |
| 4.9 | Kasım 2022 | **`satisfies`operatörü**,`in`daraltma |
| 5.0 | Mart 2023 | **Ana**:`const`tipi parametreler, dekoratörler,`enum`revizyonu |
| 5.1 | Haziran 2023 | İlgisiz tip ayarlayıcılar,`--exactOptionalPropertyTypes`|
| 5.2 | Ağu 2023 | `using`bildirimleri (açık kaynak yönetimi) |
| 5.3 | Kasım 2023 | İçe aktarma öznitelikleri,`switch true`daraltma |
| 5.4 | Mart 2024 | `NoInfer`yardımcı programı, daraltılmış kapatma parametreleri |
| 5.5 | Haziran 2024 | Çıkarılan tür yüklemleri, normal ifade için`@`|
| 5.6 | Eylül 2024 |  `--erasableSyntaxOnly`, yineleyici yardımcıları |
| 5.7 | Kasım 2024 | `--noCheck`, yol tamamlamalar |
| 5.8 | Şubat 2025 | Geliştirilmiş`isolatedDeclarations`|
## Önemli Kilometre Taşları
### İlk Günler (2012–2015)
- **0.8 (2012)**: Anders Hejlsberg (C# yaratıcısı) Microsoft'ta TypeScript'i yönetiyor
- **1.0 (2014)**: Kararlı sürüm; sınıflar, arayüzler, temel türler
- **1.5 (2015)**: ES6 özellikleri — yıkım, ad alanları, `for...of`
### Tip Devrimi (2016–2018)
- **2.0 (2016)**: Birleşim türleri, kesişim türleri,`never`,`keyof`— TypeScript'in tür sistemi benzersiz hale geliyor
- **2.8 (2018)**: Koşullu türler — gelişmiş tür düzeyinde programlamanın temeli
- **3.0 (2018)**: Geri kalan parametrelerdeki gruplar,`unknown`türü, proje referansları
### Modern TypeScript (2019 – günümüz)
- **3.7 (2019)**: İsteğe bağlı`?.`zincirleme ve`??`birleştirmeyi geçersiz kılma (JS standardından önce!)
- **4.0 (2020)**: Değişken tanımlamalar, şablon değişmez türleri
- **4.1 (2020)**: Şablon değişmez türleri — tür düzeyinde dize işlemleri
- **4.9 (2022)**:`satisfies`operatörü — genişletme olmadan tür kontrolü
- **5.0 (2023)**:`const`tipi parametreler, dekoratörler (aşama 3)
- **5.2 (2023)**:`using`bildirimleri — açık kaynak yönetimi
## Tür Sistem Gelişimi
```
2012: Basic types, classes, interfaces
2014: Generics, enums
2016: Union types, intersection types, discriminated unions
2018: Conditional types, mapped types, keyof, infer
2020: Template literal types, variadic tuples
2022: satisfies operator
2023: const type parameters
2023: using declarations
```

## Dekoratör Evrimi
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Yapılandırma Gelişimi
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Ekosistem Büyümesi
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Temel Tasarım Kararları
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
