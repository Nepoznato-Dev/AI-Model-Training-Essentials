---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| K&R C | 1972–78 | Orihinal na C (Kernighan at Ritchie) |
| C89/C90 | 1989/90 | Unang pamantayan ng ANSI/ISO |
| C95 | 1995 | Susog 1:`wchar.h`, mga digraph |
| C99 | 1999 | `//`komento,`inline`,`bool`, VLAs, itinalagang mga initializer |
| C11 | 2011 | Atomics, thread,`_Static_assert`, anonymous na mga istruktura/unyon |
| C17 | 2018 | Mga pag-aayos ng depekto (walang mga bagong feature) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, mga katangian |
## Mga Pangunahing Milestone
### K&R C (1972–1989)
- **1972**: Lumikha si Dennis Ritchie ng C sa Bell Labs para sa Unix
- **1978**: Inilathala ni Kernighan at Ritchie ang "The C Programming Language"
- Mga pangunahing tampok:`struct`,`int`,`char`, mga pointer, function,`#include`
- Walang`void`, walang`enum`, walang`unsigned`, walang `const`
### C89/C90 — Ang Pamantayan (1989)
- Unang pamantayan ng ANSI (ANSI X3.159-1989)
- Idinagdag:`void`,`enum`,`const`,`volatile`, mga prototype ng function,`signed`
- Ang "golden age" — portable, malawakang pinagtibay
- Pa rin ang baseline para sa maraming naka-embed na system
### C99 — Modern C (1999)
-`//`iisang linyang komento
- Mga function ng `inline`
-`bool`sa pamamagitan ng`<stdbool.h>`
- Variable-length arrays (mga VLA)
- Mga itinalagang initializer:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— mga deklarasyon sa loop
-`<stdint.h>`:`int32_t`,`uint64_t`, atbp.
-`restrict`keyword
- Variadic macros
- Tambalang literal
### C11 — Kaligtasan at Concurrency (2011)
-`<stdatomic.h>`— atomic operations
-`<threads.h>`— suporta sa thread
-`_Static_assert`— compile-time assertions
- Mga anonymous na struct/unions sa mga nested struct
-`_Alignof`,`_Alignas`— kontrol sa pagkakahanay
- Mga generic na pagpipilian:`_Generic(x, int: ..., default: ...)`
- Suporta sa Unicode:`<uchar.h>`
- Opsyonal na suporta sa VLA (ginawang opsyonal dahil sa mga naka-embed na alalahanin)
### C23 — The Renaissance (2024)
-`nullptr`— null pointer constant (pinapalitan ang`NULL`macro)
-`typeof`— uri ng hinuha
-`constexpr`— mga pare-parehong expression
-`#embed`— mag-embed ng binary data sa oras ng pag-compile
-`[[attribute]]`syntax (C23-style na mga katangian)
-`true`/`false`bilang mga keyword (hindi na kailangan ng`<stdbool.h>`)
-`auto`uri ng hinuha
-`static_assert`(walang underscore)
-`alignof`(walang underscore)
- Inalis ang Default na`int`return
## Proseso ng Pamantayan
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Pilosopiya ng Pagkatugma
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Preprocessor Evolution
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Uri ng System Evolution
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Epekto sa Ecosystem
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
