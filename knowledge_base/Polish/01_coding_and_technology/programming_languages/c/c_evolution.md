<!--
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

-->
# C — Historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| K&R C | 1972–78 | Oryginał C (Kernighan & Ritchie) |
| C89/C90 | 1989/90 | Pierwsza norma ANSI/ISO |
| C95 | 1995 | Poprawka 1: `wchar.h`, dwuznaki |
| C99 | 1999 |  Komentarze `//`,`inline`,`bool`, VLA, wyznaczone inicjatory |
| C11 | 2011 | Atomy, wątki, `_Static_assert`, anonimowe struktury/unie |
| C17 | 2018 | Naprawa usterek (brak nowych funkcji) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, atrybuty |
## Główne kamienie milowe
### K&R C (1972–1989)
- **1972**: Dennis Ritchie tworzy język C w Bell Labs dla systemu Unix
- **1978**: Kernighan i Ritchie publikują „Język programowania C”
- Kluczowe funkcje:`struct`,`int`,`char`, wskaźniki, funkcje,`#include`
- Nie `void`, nie `enum`, nie `unsigned`, nie `const`
### C89/C90 — Standard (1989)
- Pierwsza norma ANSI (ANSI X3.159-1989)
- Dodano:`void`,`enum`,`const`,`volatile`, prototypy funkcji,`signed`
- „Złoty wiek” — przenośny, powszechnie przyjęty
- Nadal stanowi podstawę dla wielu systemów wbudowanych
### C99 — Nowoczesne C (1999)
- Komentarze jednowierszowe `//`
- Funkcje `inline`
-`bool`przez`<stdbool.h>`
- Tablice o zmiennej długości (VLA)
- Wyznaczone inicjatory:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— deklaracje w pętli
- `<stdint.h>`: `int32_t`,`uint64_t`itp.
- Słowo kluczowe `restrict`
- Makra wariadyczne
- Literały złożone
### C11 — Bezpieczeństwo i współbieżność (2011)
-`<stdatomic.h>`— operacje atomowe
-`<threads.h>`— obsługa wątków
-`_Static_assert`— asercje w czasie kompilacji
- Anonimowe struktury/unie w strukturach zagnieżdżonych
-`_Alignof`,`_Alignas`– kontrola wyrównania
- Wybór ogólny:`_Generic(x, int: ..., default: ...)`
- Obsługa Unicode:`<uchar.h>`
- Opcjonalna obsługa VLA (opcjonalna ze względu na wbudowane problemy)
### C23 — Renesans (2024)
-`nullptr`— stała wskaźnika zerowego (zastępuje makro `NULL`)
-`typeof`— wnioskowanie typu
-`constexpr`— wyrażenia stałe
-`#embed`— osadza dane binarne w czasie kompilacji
- Składnia`[[attribute]]`(atrybuty w stylu C23)
-`true`/`false`jako słowa kluczowe (nie potrzeba już `<stdbool.h>`)
- Wnioskowanie typu `auto`
-`static_assert`(bez podkreślenia)
-`alignof`(bez podkreślenia)
- Usunięto domyślny zwrot `int`
## Proces standaryzacji
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Filozofia kompatybilności
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Ewolucja preprocesora
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Wpisz ewolucję systemu
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Wpływ na ekosystem
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
