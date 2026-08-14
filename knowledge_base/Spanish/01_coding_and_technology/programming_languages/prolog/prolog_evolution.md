---
# Metadata
title: "Prolog — Version History & Evolution"
description: "Comprehensive version history and evolution of Prolog from origins to modern Prolog."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [prolog, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Prolog: Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| Pre-prólogo | 1965–70 | Q-systems de Colmerauer, procesamiento del lenguaje natural |
| Prólogo I | 1972 | **Primer prólogo** (Alain Colmerauer, Marsella) |
| DIC-10 | 1977 | Prólogo de Edimburgo de David Warren (compilador eficiente) |
| Prólogo ISO | 1995 | **Primera norma ISO** (ISO/IEC 13211-1) |
| SWI-Prólogo | 1987 | Jan Wielemaker: el prólogo de código abierto más popular |
| Prólogo de GNU | 1999 | Daniel Díaz — compilación nativa |
| ISO 2do | 2012 | Corrigendum 2 (corrección de errores, aclaraciones) |
| SWI 8.x | 2018 | Presentación, racionales, mejora del rendimiento |
| SWI 9.x | 2023 | **Tablación** (predeterminada), módulos mejorados, sistema de paquetes |
| Arúspice | 2018 | Prólogo moderno en Rust: compatible con ISO |
| Trealla | 2022 | Fast Prolog en C: implementación moderna |
## Hitos importantes
### Nacimiento del prólogo (1972)
- **1972**: Alain Colmerauer crea Prolog en la Universidad de Marsella
- **Nombre**: "PROgrammation en LOGique" (programación en lógica)
- **Objetivo**: Procesamiento del lenguaje natural: analizar oraciones en francés
- Basado en cláusulas y resolución de Horn (Robinson, 1965)
- Primera implementación: unificación + retroceso
### Prólogo de Edimburgo (1977)
- **1977**: David Warren crea DEC-10 Prolog en Edimburgo
- Compilador eficiente: Prolog se vuelve práctico
- Edinburgh Prolog se convierte en la implementación de referencia
- Influencias: cláusulas de cuerno, búsqueda en profundidad, operador de corte
### Estandarización ISO (1995)
- **1995**: Primera norma ISO (ISO/IEC 13211-1)
- Define: sintaxis, predicados integrados, aritmética, E/S
- Garantiza la portabilidad entre implementaciones.
### Prólogo moderno (década de 2000 hasta el presente)
- **SWI-Prolog**: Más utilizado: tabulación, módulos, subprocesos múltiples, web (Pengines)
- **GNU Prolog**: compilación nativa: ejecutables rápidos
- **Scryer Prolog**: moderno, basado en Rust, compatible con ISO
- **Trealla Prolog**: Rápido, ligero, basado en C
## Evolución de la sintaxis
```prolog
% Early Prolog (1970s): Basic logic programming
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Query: grandparent(tom, ann).  → true
% Query: grandparent(tom, X).    → X = ann ; X = bob

% Classic: List processing
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).

% ISO Prolog: Standardized built-ins
% Arithmetic
X is 2 + 3 * 4.          % X = 14
X =:= 14.                % true (arithmetic equality)
X =\= 15.                % true (arithmetic inequality)

% Constraint Logic Programming (CLP)
:- use_module(library(clpfd)).
sudoku(Rows) :-
    append(Rows, Vs), Vs ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Cols),
    maplist(all_distinct, Cols).

% Tabling (memoization) — SWI-Prolog 9.x
:- table fib/2.
fib(0, 0).
fib(1, 1).
fib(N, F) :- N > 1, N1 is N-1, N2 is N-2, fib(N1, F1), fib(N2, F2), F is F1+F2.

% Modules (ISO)
:- module(shapes, [area/2]).
area(circle(R), A) :- A is pi * R * R.
area(rect(W, H), A) :- A is W * H.

% DCG (Definite Clause Grammars) — natural language
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb, noun_phrase.
determiner --> [the].
noun --> [cat].
verb --> [chased].
```

## Evolución de funciones
```
1972: Basic Horn clauses, unification, backtracking
1977: DEC-10 Prolog — efficient compiler, cut operator
1980s: DCG (Definite Clause Grammars), difference lists
1990s: Constraint Logic Programming (CLP(FD), CLP(Q))
1995: ISO standard — portable Prolog
2000s: Tabling (memoization), modules, multi-threading
2010s: Tabling becomes default, pack systems, web integration
2020s: Modern implementations (Scryer, Trealla), improved performance
```

## Principios clave de diseño
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## Crecimiento del ecosistema
```
1972: Prolog created at Marseille — AI research
1977: DEC-10 Prolog — practical implementation
1980s: Japan's Fifth Generation Project — Prolog-based AI computers
1987: SWI-Prolog — open source, becomes most popular
1995: ISO standard — portability
1999: GNU Prolog — native compilation
2000s: Prolog in: expert systems, NLP, type inference, verification
2018: Scryer Prolog — modern Rust implementation
2022: Trealla Prolog — fast C implementation
2025: Prolog used in: IBM Watson (early), natural language processing,
       type systems, theorem proving, scheduling, rule engines
       SWI-Prolog is the reference implementation
```
