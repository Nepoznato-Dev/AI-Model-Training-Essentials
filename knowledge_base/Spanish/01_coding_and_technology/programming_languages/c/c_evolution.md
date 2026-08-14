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

# C - Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| K&R C | 1972–78 | Original C (Kernighan y Ritchie) |
| C89/C90 | 1989/90 | Primera norma ANSI/ISO |
| C95 | 1995 | Enmienda 1:`wchar.h`, dígrafos |
| C99 | 1999 |  Comentarios `//`, `inline`, `bool`, VLA, inicializadores designados |
| C11 | 2011 | Atómica, subprocesos, `_Static_assert`, estructuras/uniones anónimas |
| C17 | 2018 | Correcciones de defectos (sin características nuevas) |
| C23 | 2024 |  `nullptr`, `typeof`, `constexpr`, `#embed`, atributos |
## Hitos importantes
### K&R C (1972–1989)
- **1972**: Dennis Ritchie crea C en Bell Labs para Unix
- **1978**: Kernighan & Ritchie publican "El lenguaje de programación C"
- Características clave: `struct`, `int`, `char`, punteros, funciones,`#include`
- Sin `void`, sin `enum`, sin `unsigned`, sin `const`
### C89/C90 — El estándar (1989)
- Primer estándar ANSI (ANSI X3.159-1989)
- Agregado: `void`, `enum`, `const`, `volatile`, prototipos de funciones,`signed`
- La "edad de oro": portátil, ampliamente adoptada
- Sigue siendo la base para muchos sistemas integrados.
### C99 — C moderno (1999)
- Comentarios de una sola línea `//`
- Funciones `inline`
-`bool`vía`<stdbool.h>`
- Arreglos de longitud variable (VLA)
- Inicializadores designados:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— declaraciones en bucle
-`<stdint.h>`:`int32_t`,`uint64_t`, etc.
- Palabra clave `restrict`
- Macros variadas
- Literales compuestos
### C11 — Seguridad y simultaneidad (2011)
-`<stdatomic.h>`— operaciones atómicas
-`<threads.h>`— soporte de hilo
-`_Static_assert`— afirmaciones en tiempo de compilación
- Estructuras/uniones anónimas en estructuras anidadas
- `_Alignof`,`_Alignas`— control de alineación
- Selecciones genéricas:`_Generic(x, int: ..., default: ...)`
- Soporte Unicode:`<uchar.h>`
- Soporte VLA opcional (opcional debido a preocupaciones integradas)
### C23 — El Renacimiento (2024)
-`nullptr`— constante de puntero nulo (reemplaza la macro `NULL`)
-`typeof`— inferencia de tipos
-`constexpr`— expresiones constantes
- `#embed`: incrusta datos binarios en tiempo de compilación
- Sintaxis`[[attribute]]`(atributos de estilo C23)
-`true`/`false`como palabras clave (ya no es necesario `<stdbool.h>`)
- Inferencia de tipo `auto`
-`static_assert`(sin guión bajo)
-`alignof`(sin guión bajo)
- Se eliminó el retorno`int`predeterminado
## Proceso de estándares
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Filosofía de compatibilidad
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Evolución del preprocesador
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Evolución del sistema tipo
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Impacto en el ecosistema
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
