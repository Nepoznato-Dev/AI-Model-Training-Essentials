---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# TypeScript — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tanggal Rilis | Tema Utama |
|---------|-------------|-----------|
| 0,8 | Oktober 2012 | Rilis publik awal (Anders Hejlsberg) |
| 0,9 | April 2013 | Generik |
| 1.0 | April 2014 | Rilis stabil pertama |
| 1.1 | November 2014 | Kinerja kompiler |
| 1.4 | Januari 2015 | Tipe literal templat (dasar),`let`|
| 1.5 | Juli 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | September 2015 |  Kelas `abstract`, dukungan JSX |
| 1.7 | November 2015 | `async/await`(target ES2017) |
| 1.8 | Februari 2016 | String templat yang diberi tag,`--strictNullChecks`|
| 2.0 | September 2016 | **Mayor**: Tipe gabungan/persimpangan,`never`,`keyof`,`protected`|
| 2.1 | Desember 2016 |  `keyof`, tipe yang dipetakan, generator`async`|
| 2.2 | Februari 2017 |  Tipe `object`, ditingkatkan`this`|
| 2.3 | April 2017 | Default umum, mode`--strict`|
| 2.4 | Juni 2017 | Tipe lemah, string enum |
| 2.5 | September 2017 | Pengikatan tangkapan opsional |
| 2.6 | Oktober 2017 | Tipe fungsi ketat,`--strictFunctionTypes`|
| 2.7 | Januari 2018 | Penugasan pasti (`!`),`const`enum |
| 2.8 | Maret 2018 | **Jenis bersyarat**,`Exclude`,`Extract`|
| 2.9 | Juni 2018 | `keyof`untuk numerik/simbol, tipe`import()`|
| 3.0 | Juli 2018 | **Mayor**: Tupel sedang istirahat,`unknown`, referensi proyek |
| 3.1 | September 2018 | Tipe yang dipetakan pada tupel, array`readonly`|
| 3.2 | November 2018 | `bigint`,`object`menyebar |
| 3.4 | Maret 2019 |  Pernyataan `const`, inferensi tipe tingkat tinggi |
| 3,5 | Mei 2019 |  Tipe pembantu`Omit`|
| 3.7 | November 2019 | **Rantai opsional**, penggabungan nullish, tipe rekursif |
| 3.8 | Februari 2020 | `type-only`impor/ekspor, bidang`#private`|
| 3.9 | Mei 2020 | `// @ts-expect-error`, inferensi yang ditingkatkan |
| 4.0 | Agustus 2020 | **Mayor**: Tupel variadik, tupel berlabel, tipe literal templat |
| 4.1 | November 2020 | **Tipe literal templat**, pemetaan ulang kunci, kondisional rekursif |
| 4.2 | Februari 2021 | Properti abstrak,`~`dalam tipe yang dipetakan |
| 4.3 | Juni 2021 | Jenis penulisan terpisah, kata kunci`override`|
| 4.4 | Agustus 2021 | Tanda tangan simbol/indeks, penyempitan aliran kontrol |
| 4.5 | November 2021 | `.d.ts`dari`.js`,`await`di`.d.ts`|
| 4.6 | Februari 2022 | Pemeriksaan fungsi cakupan blok, jenis objek lainnya |
| 4.7 | Mei 2022 |  Kendala`extends`untuk`infer`, ESM di`.ts`|
| 4.8 | Agustus 2022 | Peningkatan pengurangan persimpangan, perbaikan`--strictNullChecks`|
| 4.9 | November 2022 | ** Operator `satisfies`**, penyempitan`in`|
| 5.0 | Maret 2023 | **Mayor**: Param tipe `const`, dekorator, perombakan`enum`|
| 5.1 | Juni 2023 | Penentu tipe yang tidak terkait,`--exactOptionalPropertyTypes`|
| 5.2 | Agustus 2023 |  Deklarasi`using`(manajemen sumber daya eksplisit) |
| 5.3 | November 2023 | Impor atribut, penyempitan`switch true`|
| 5.4 | Maret 2024 |  Utilitas `NoInfer`, parameter penutupan menyempit |
| 5.5 | Juni 2024 | Predikat tipe yang disimpulkan,`@`untuk regex |
| 5.6 | September 2024 | `--erasableSyntaxOnly`, pembantu iterator |
| 5.7 | November 2024 | `--noCheck`, penyelesaian jalur |
| 5.8 | Februari 2025 | Peningkatan`isolatedDeclarations`|
## Tonggak Penting
### Masa-masa Awal (2012–2015)
- **0.8 (2012)**: Anders Hejlsberg (pembuat C#) memimpin TypeScript di Microsoft
- **1.0 (2014)**: Rilis stabil; kelas, antarmuka, tipe dasar
- **1.5 (2015)**: Fitur ES6 — destrukturisasi, namespace, `for...of`
### Revolusi Tipe (2016–2018)
- **2.0 (2016)**: Tipe gabungan, tipe persimpangan,`never`,`keyof`— Sistem tipe TypeScript menjadi unik
- **2.8 (2018)**: Tipe bersyarat — dasar untuk pemrograman tingkat tipe tingkat lanjut
- **3.0 (2018)**: Tupel dalam parameter istirahat, tipe `unknown`, referensi proyek
### TypeScript Modern (2019–sekarang)
- **3.7 (2019)**: Rangkaian opsional`?.`dan penggabungan nullish`??`(sebelum standar JS!)
- **4.0 (2020)**: Tupel variadik, tipe literal templat
- **4.1 (2020)**: Tipe literal templat — manipulasi string tingkat tipe
- **4.9 (2022)**: Operator`satisfies`— pemeriksaan tipe tanpa pelebaran
- **5.0 (2023)**: Parameter tipe `const`, dekorator (tahap 3)
- **5.2 (2023)**: Deklarasi`using`— pengelolaan sumber daya eksplisit
## Ketik Evolusi Sistem
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

## Evolusi Dekorator
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Evolusi Konfigurasi
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Pertumbuhan Ekosistem
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Keputusan Desain Utama
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
