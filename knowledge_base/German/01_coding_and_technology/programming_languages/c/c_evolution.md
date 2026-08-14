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
# C – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| K&R C | 1972–78 | Original C (Kernighan & Ritchie) |
| C89/C90 | 1989/90 | Erster ANSI/ISO-Standard |
| C95 | 1995 | Änderung 1:`wchar.h`, Digraphen |
| C99 | 1999 | `//`Kommentare, `inline`, `bool`, VLAs, designierte Initialisierer |
| C11 | 2011 | Atomics, Threads,`_Static_assert`, anonyme Strukturen/Unions |
| C17 | 2018 | Fehlerbehebungen (keine neuen Funktionen) |
| C23 | 2024 |  `nullptr`, `typeof`, `constexpr`, `#embed`, Attribute |
## Wichtige Meilensteine
### K&R C (1972–1989)
- **1972**: Dennis Ritchie erstellt C in den Bell Labs für Unix
- **1978**: Kernighan & Ritchie veröffentlichen „The C Programming Language“
- Hauptmerkmale: `struct`, `int`, `char`, Zeiger, Funktionen,`#include`
- Kein `void`, kein `enum`, kein `unsigned`, kein `const`
### C89/C90 – Der Standard (1989)
- Erster ANSI-Standard (ANSI X3.159-1989)
- Hinzugefügt: `void`, `enum`, `const`, `volatile`, Funktionsprototypen,`signed`
- Das „goldene Zeitalter“ – tragbar, weit verbreitet
– Immer noch die Basis für viele eingebettete Systeme
### C99 – Modernes C (1999)
-`//`einzeilige Kommentare
- `inline`-Funktionen
-`bool`über`<stdbool.h>`
- Arrays variabler Länge (VLAs)
– Designierte Initialisierer:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`– Deklarationen in einer Schleife
-`<stdint.h>`:`int32_t`,`uint64_t`usw.
- Schlüsselwort `restrict`
- Variadische Makros
- Zusammengesetzte Literale
### C11 – Sicherheit und Parallelität (2011)
-`<stdatomic.h>`– atomare Operationen
-`<threads.h>`– Thread-Unterstützung
-`_Static_assert`– Behauptungen zur Kompilierungszeit
- Anonyme Strukturen/Unions in verschachtelten Strukturen
-`_Alignof`,`_Alignas`– Ausrichtungskontrolle
- Allgemeine Auswahl:`_Generic(x, int: ..., default: ...)`
- Unicode-Unterstützung:`<uchar.h>`
- Optionale VLA-Unterstützung (aufgrund eingebetteter Bedenken optional gemacht)
### C23 – Die Renaissance (2024)
-`nullptr`– Nullzeigerkonstante (ersetzt das Makro `NULL`)
-`typeof`– Typinferenz
-`constexpr`– konstante Ausdrücke
-`#embed`– Binärdaten zur Kompilierungszeit einbetten
- `[[attribute]]`-Syntax (Attribute im C23-Stil)
-`true`/`false`als Schlüsselwörter (`<stdbool.h>` wird nicht mehr benötigt)
- `auto`-Typinferenz
-`static_assert`(ohne Unterstrich)
-`alignof`(ohne Unterstrich)
– Standard-`int`-Rückgabe entfernt
## Standardprozess
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Kompatibilitätsphilosophie
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Präprozessorentwicklung
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Typsystementwicklung
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Auswirkungen auf das Ökosystem
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
