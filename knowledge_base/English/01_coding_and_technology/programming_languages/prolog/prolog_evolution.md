<!--
---
# Metadata
title: "Prolog — Version History & Evolution"
description: "Comprehensive version history and evolution of Prolog from origins to modern Prolog."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Prolog — Version History & Evolution

## Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| Pre-Prolog | 1965–70 | Colmerauer's Q-systems, natural language processing |
| Prolog I   | 1972 | **First Prolog** (Alain Colmerauer, Marseille) |
| DEC-10   | 1977 | David Warren's Edinburgh Prolog (efficient compiler) |
| ISO Prolog | 1995 | **First ISO standard** (ISO/IEC 13211-1) |
| SWI-Prolog | 1987 | Jan Wielemaker — most popular open-source Prolog |
| GNU Prolog | 1999 | Daniel Diaz — native compilation |
| ISO 2nd  | 2012 | Corrigendum 2 (bug fixes, clarifications) |
| SWI 8.x  | 2018 | Tabling, rationals, improved performance |
| SWI 9.x  | 2023 | **Tabling** (default), improved modules, pack system |
| Scryer   | 2018 | Modern Prolog in Rust — ISO-compatible |
| Trealla  | 2022 | Fast Prolog in C — modern implementation |

## Major Milestones

### Birth of Prolog (1972)
- **1972**: Alain Colmerauer creates Prolog at University of Marseille
- **Name**: "PROgrammation en LOGique" (programming in logic)
- **Goal**: Natural language processing — parse French sentences
- Based on Horn clauses and resolution (Robinson, 1965)
- First implementation: unification + backtracking

### Edinburgh Prolog (1977)
- **1977**: David Warren creates DEC-10 Prolog at Edinburgh
- Efficient compiler — Prolog becomes practical
- Edinburgh Prolog becomes the reference implementation
- Influences: Horn clauses, depth-first search, cut operator

### ISO Standardization (1995)
- **1995**: First ISO standard (ISO/IEC 13211-1)
- Defines: syntax, built-in predicates, arithmetic, I/O
- Ensures portability across implementations

### Modern Prolog (2000s–present)
- **SWI-Prolog**: Most widely used — tabling, modules, multi-threading, web (Pengines)
- **GNU Prolog**: Native compilation — fast executables
- **Scryer Prolog**: Modern, Rust-based, ISO-compatible
- **Trealla Prolog**: Fast, lightweight, C-based

## Syntax Evolution

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

## Feature Evolution

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

## Key Design Principles

```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## Ecosystem Growth

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
