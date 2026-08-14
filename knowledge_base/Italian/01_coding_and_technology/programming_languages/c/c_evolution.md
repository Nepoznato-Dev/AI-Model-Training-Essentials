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
# C: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| K&R C | 1972–78 | Originale C (Kernighan & Ritchie) |
| C89/C90 | 1989/90| Primo standard ANSI/ISO |
| C95 | 1995 | Emendamento 1:`wchar.h`, digrafi |
| C99 | 1999 |  Commenti `//`,`inline`,`bool`, VLA, inizializzatori designati |
| C11 | 2011 | Atomici, thread,`_Static_assert`, strutture/unioni anonime |
| C17 | 2018 | Correzioni di difetti (nessuna nuova funzionalità) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, attributi |
## Traguardi importanti
### K&R C (1972-1989)
- **1972**: Dennis Ritchie crea C presso i Bell Labs per Unix
- **1978**: Kernighan & Ritchie pubblicano "The C Programming Language"
- Caratteristiche principali: `struct`, `int`, `char`, puntatori, funzioni,`#include`
- Niente `void`, niente `enum`, niente `unsigned`, niente `const`
### C89/C90 — Lo standard (1989)
- Primo standard ANSI (ANSI X3.159-1989)
- Aggiunto:`void`,`enum`,`const`,`volatile`, prototipi di funzioni,`signed`
- L'"età dell'oro": portatile, ampiamente adottata
- Ancora la base di riferimento per molti sistemi embedded
### C99 — Do moderno (1999)
-`//`commenti a riga singola
- Funzioni `inline`
-`bool`tramite`<stdbool.h>`
- Array a lunghezza variabile (VLA)
- Inizializzatori designati:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— dichiarazioni in loop
-`<stdint.h>`: `int32_t`, `uint64_t`, ecc.
- Parola chiave `restrict`
- Macro variadici
- Letterali composti
### C11 — Sicurezza e concorrenza (2011)
-`<stdatomic.h>`— operazioni atomiche
-`<threads.h>`— supporto per filettatura
- `_Static_assert`: asserzioni in fase di compilazione
- Strutture/unioni anonime in strutture nidificate
-`_Alignof`,`_Alignas`— controllo dell'allineamento
- Selezioni generiche:`_Generic(x, int: ..., default: ...)`
- Supporto Unicode:`<uchar.h>`
- Supporto VLA opzionale (reso opzionale a causa di problemi incorporati)
### C23 — Il Rinascimento (2024)
- `nullptr`: costante puntatore nullo (sostituisce la macro `NULL`)
- `typeof`: tipo di inferenza
-`constexpr`— espressioni costanti
- `#embed`: incorpora dati binari in fase di compilazione
- Sintassi`[[attribute]]`(attributi in stile C23)
-`true`/`false`come parole chiave (non è più necessario `<stdbool.h>`)
- Inferenza di tipo `auto`
-`static_assert`(senza carattere di sottolineatura)
-`alignof`(senza carattere di sottolineatura)
- Rimosso il ritorno`int`predefinito
## Processo di standardizzazione
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Filosofia della compatibilità
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Evoluzione del preprocessore
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Digitare Evoluzione del sistema
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Impatto sull'ecosistema
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
