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
# C — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| K&R C | 1972-78 | Original C (Kernighan et Ritchie) |
| C89/C90 | 1989/90 | Première norme ANSI/ISO |
| C95 | 1995 | Amendement 1 :`wchar.h`, digraphes |
| C99 | 1999 |  Commentaires `//`,`inline`,`bool`, VLA, initialiseurs désignés |
| C11 | 2011 | Atomiques, threads,`_Static_assert`, structures/unions anonymes |
| C17 | 2018 | Corrections de défauts (pas de nouvelles fonctionnalités) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, attributs |
## Étapes majeures
### K&R C (1972-1989)
- **1972** : Dennis Ritchie crée C aux Bell Labs pour Unix
- **1978** : Kernighan & Ritchie publient "The C Programming Language"
- Principales caractéristiques : `struct`, `int`, `char`, pointeurs, fonctions,`#include`
- Pas de`void`, pas de`enum`, pas de`unsigned`, pas de `const`
### C89/C90 — La norme (1989)
- Première norme ANSI (ANSI X3.159-1989)
- Ajouté :`void`,`enum`,`const`,`volatile`, prototypes de fonctions,`signed`
- "L'âge d'or" - portable, largement adopté
- Toujours la référence pour de nombreux systèmes embarqués
### C99 — Moderne C (1999)
- Commentaires sur une seule ligne `//`
-Fonctions `inline`
-`bool` via`<stdbool.h>`
- Matrices de longueur variable (VLA)
- Initialiseurs désignés :`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— déclarations en boucle
-`<stdint.h>`:`int32_t`,`uint64_t`, etc.
- Mot-clé `restrict`
- Macros variadiques
- Littéraux composés
### C11 — Sécurité et concurrence (2011)
-`<stdatomic.h>`— opérations atomiques
-`<threads.h>`— prise en charge des threads
-`_Static_assert`— assertions à la compilation
- Structures/unions anonymes dans des structures imbriquées
-`_Alignof`,`_Alignas`— contrôle d'alignement
- Sélections génériques :`_Generic(x, int: ..., default: ...)`
- Prise en charge Unicode :`<uchar.h>`
- Prise en charge VLA facultative (rendue facultative en raison de problèmes intégrés)
### C23 — La Renaissance (2024)
-`nullptr`— constante de pointeur nul (remplace la macro `NULL`)
-`typeof`— inférence de type
-`constexpr`— expressions constantes
-`#embed`— intègre des données binaires au moment de la compilation
- Syntaxe`[[attribute]]`(attributs de style C23)
-`true`/`false`comme mots-clés (plus besoin de `<stdbool.h>`)
- Inférence de type `auto`
-`static_assert`(sans trait de soulignement)
-`alignof`(sans trait de soulignement)
- Retour`int`par défaut supprimé
## Processus de normalisation
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Philosophie de compatibilité
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Évolution du préprocesseur
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Évolution du système de types
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Impact sur l'écosystème
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
