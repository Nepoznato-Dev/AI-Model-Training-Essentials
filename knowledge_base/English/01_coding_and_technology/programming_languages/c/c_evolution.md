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
# C — Version History & Evolution

## Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| K&R C   | 1972–78 | Original C (Kernighan & Ritchie) |
| C89/C90 | 1989/90 | First ANSI/ISO standard |
| C95     | 1995    | Amendment 1: `wchar.h`, digraphs |
| C99     | 1999    | `//` comments, `inline`, `bool`, VLAs, designated initializers |
| C11     | 2011    | Atomics, threads, `_Static_assert`, anonymous structs/unions |
| C17     | 2018    | Defect fixes (no new features) |
| C23     | 2024    | `nullptr`, `typeof`, `constexpr`, `#embed`, attributes |

## Major Milestones

### K&R C (1972–1989)
- **1972**: Dennis Ritchie creates C at Bell Labs for Unix
- **1978**: Kernighan & Ritchie publish "The C Programming Language"
- Key features: `struct`, `int`, `char`, pointers, functions, `#include`
- No `void`, no `enum`, no `unsigned`, no `const`

### C89/C90 — The Standard (1989)
- First ANSI standard (ANSI X3.159-1989)
- Added: `void`, `enum`, `const`, `volatile`, function prototypes, `signed`
- The "golden age" — portable, widely adopted
- Still the baseline for many embedded systems

### C99 — Modern C (1999)
- `//` single-line comments
- `inline` functions
- `bool` via `<stdbool.h>`
- Variable-length arrays (VLAs)
- Designated initializers: `struct Point p = {.x = 1, .y = 2};`
- `for (int i = 0; ...)` — declarations in loop
- `<stdint.h>`: `int32_t`, `uint64_t`, etc.
- `restrict` keyword
- Variadic macros
- Compound literals

### C11 — Safety & Concurrency (2011)
- `<stdatomic.h>` — atomic operations
- `<threads.h>` — thread support
- `_Static_assert` — compile-time assertions
- Anonymous structs/unions in nested structs
- `_Alignof`, `_Alignas` — alignment control
- Generic selections: `_Generic(x, int: ..., default: ...)`
- Unicode support: `<uchar.h>`
- Optional VLA support (made optional due to embedded concerns)

### C23 — The Renaissance (2024)
- `nullptr` — null pointer constant (replaces `NULL` macro)
- `typeof` — type inference
- `constexpr` — constant expressions
- `#embed` — embed binary data at compile time
- `[[attribute]]` syntax (C23-style attributes)
- `true`/`false` as keywords (no longer need `<stdbool.h>`)
- `auto` type inference
- `static_assert` (without underscore)
- `alignof` (without underscore)
- Default `int` return removed

## Standards Process

```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Compatibility Philosophy

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

## Type System Evolution

```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Ecosystem Impact

```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
