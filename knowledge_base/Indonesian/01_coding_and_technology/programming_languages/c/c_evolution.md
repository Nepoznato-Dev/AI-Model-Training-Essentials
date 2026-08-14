---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [c, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| K&R C | 1972–78 | C Asli (Kernighan & Ritchie) |
| Bab 89/C90 | 1989/90 | Standar ANSI/ISO pertama |
| Bab 95 | 1995 | Amandemen 1:`wchar.h`, digraf |
| Bab 99 | 1999 |  Komentar `//`,`inline`,`bool`, VLA, inisialisasi yang ditunjuk |
| C11 | 2011 | Atom, utas,`_Static_assert`, struct/union anonim |
| C17 | 2018 | Perbaikan cacat (tidak ada fitur baru) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, atribut |
## Tonggak Penting
### K&RC (1972–1989)
- **1972**: Dennis Ritchie menciptakan C di Bell Labs untuk Unix
- **1978**: Kernighan & Ritchie menerbitkan "Bahasa Pemrograman C"
- Fitur utama: `struct`, `int`, `char`, pointer, fungsi,`#include`
- Tidak ada `void`, tidak ada `enum`, tidak ada `unsigned`, tidak ada `const`
### C89/C90 — Standar (1989)
- Standar ANSI pertama (ANSI X3.159-1989)
- Ditambahkan: `void`, `enum`, `const`, `volatile`, prototipe fungsi,`signed`
- "Zaman Keemasan" — portabel, diadopsi secara luas
- Masih menjadi dasar bagi banyak sistem tertanam
### C99 — C Modern (1999)
- Komentar satu baris `//`
- Fungsi `inline`
-`bool`melalui`<stdbool.h>`
- Array dengan panjang variabel (VLA)
- Inisialisasi yang ditunjuk:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— deklarasi dalam lingkaran
-`<stdint.h>`:`int32_t`,`uint64_t`, dll.
- Kata kunci `restrict`
- Makro variadik
- Literal majemuk
### C11 — Keamanan & Konkurensi (2011)
-`<stdatomic.h>`— operasi atom
-`<threads.h>`— dukungan utas
-`_Static_assert`— pernyataan waktu kompilasi
- Struktur/gabungan anonim dalam struktur bersarang
-`_Alignof`,`_Alignas`— kontrol penyelarasan
- Pilihan umum:`_Generic(x, int: ..., default: ...)`
- Dukungan Unicode:`<uchar.h>`
- Dukungan VLA opsional (dijadikan opsional karena masalah yang melekat)
### C23 — Renaisans (2024)
-`nullptr`— konstanta penunjuk nol (menggantikan makro `NULL`)
-`typeof`— ketik inferensi
-`constexpr`— ekspresi konstan
-`#embed`— menyematkan data biner pada waktu kompilasi
- Sintaks`[[attribute]]`(atribut gaya C23)
-`true`/`false`sebagai kata kunci (tidak lagi memerlukan`<stdbool.h>`)
- Inferensi tipe `auto`
-`static_assert`(tanpa garis bawah)
-`alignof`(tanpa garis bawah)
- Pengembalian`int`default dihapus
## Standar Proses
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Filosofi Kompatibilitas
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Evolusi Praprosesor
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Ketik Evolusi Sistem
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Dampak Ekosistem
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
