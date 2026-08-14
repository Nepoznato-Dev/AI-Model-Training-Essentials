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
# C – Histórico e evolução da versão
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| K&R C | 1972–78 | C original (Kernighan e Ritchie) |
| C89/C90 | 1989/90 | Primeiro padrão ANSI/ISO |
| C95 | 1995 | Alteração 1: `wchar.h`, dígrafos |
| C99 | 1999 |  Comentários `//`,`inline`,`bool`, VLAs, inicializadores designados |
| C11 | 2011 | Atômica, threads,`_Static_assert`, estruturas/uniões anônimas |
| C17 | 2018 | Correções de defeitos (sem novos recursos) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, atributos |
## Marcos importantes
### K&R C (1972–1989)
- **1972**: Dennis Ritchie cria C no Bell Labs para Unix
- **1978**: Kernighan & Ritchie publicam "The C Programming Language"
- Principais recursos: `struct`, `int`, `char`, ponteiros, funções,`#include`
- Sem `void`, sem `enum`, sem `unsigned`, sem `const`
### C89/C90 — O Padrão (1989)
- Primeiro padrão ANSI (ANSI X3.159-1989)
- Adicionado:`void`,`enum`,`const`,`volatile`, protótipos de função,`signed`
- A “era de ouro” – portátil, amplamente adotada
- Ainda é a base para muitos sistemas embarcados
### C99 – C moderno (1999)
- Comentários de linha única `//`
- Funções `inline`
-`bool`através de`<stdbool.h>`
- Matrizes de comprimento variável (VLAs)
- Inicializadores designados:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— declarações em loop
-`<stdint.h>`:`int32_t`,`uint64_t`, etc.
- Palavra-chave `restrict`
- Macros variáveis
- Literais compostos
### C11 — Segurança e simultaneidade (2011)
-`<stdatomic.h>`— operações atômicas
-`<threads.h>`— suporte a threads
-`_Static_assert`— asserções em tempo de compilação
- Estruturas/uniões anônimas em estruturas aninhadas
- `_Alignof`,`_Alignas`— controle de alinhamento
- Seleções genéricas:`_Generic(x, int: ..., default: ...)`
- Suporte Unicode:`<uchar.h>`
- Suporte opcional a VLA (tornado opcional devido a preocupações incorporadas)
### C23 — O Renascimento (2024)
-`nullptr`— constante de ponteiro nulo (substitui a macro `NULL`)
-`typeof`— inferência de tipo
-`constexpr`— expressões constantes
-`#embed`— incorpora dados binários em tempo de compilação
- Sintaxe`[[attribute]]`(atributos de estilo C23)
-`true`/`false`como palavras-chave (não precisa mais de `<stdbool.h>`)
- Inferência de tipo `auto`
-`static_assert`(sem sublinhado)
-`alignof`(sem sublinhado)
- Retorno`int`padrão removido
## Processo de padrões
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Filosofia de Compatibilidade
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Evolução do pré-processador
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Tipo Evolução do Sistema
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Impacto no ecossistema
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
