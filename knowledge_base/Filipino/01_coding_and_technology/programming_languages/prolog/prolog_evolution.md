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
# Prolog — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| Pre-Prolog | 1965–70 | Mga Q-system ng Colmerauer, natural na pagpoproseso ng wika |
| Prolog I | 1972 | **Unang Prolog** (Alain Colmerauer, Marseille) |
| DEC-10 | 1977 | Ang Edinburgh Prolog ni David Warren (mahusay na compiler) |
| ISO Prolog | 1995 | **Unang ISO standard** (ISO/IEC 13211-1) |
| SWI-Prolog | 1987 | Jan Wielemaker — pinakasikat na open-source na Prolog |
| Prolog ng GNU | 1999 | Daniel Diaz — katutubong compilation |
| ISO 2nd | 2012 | Corrigendum 2 (mga pag-aayos ng bug, paglilinaw) |
| SWI 8.x | 2018 | Tabling, rationals, pinahusay na pagganap |
| SWI 9.x | 2023 | **Tabling** (default), pinahusay na mga module, pack system |
| Scryer | 2018 | Modern Prolog in Rust — ISO-compatible |
| Trealla | 2022 | Mabilis na Prolog sa C — modernong pagpapatupad |
## Mga Pangunahing Milestone
### Kapanganakan ng Prolog (1972)
- **1972**: Gumawa si Alain Colmerauer ng Prolog sa Unibersidad ng Marseille
- **Pangalan**: "PROgrammation en LOGique" (programming in logic)
- **Layunin**: Natural na pagpoproseso ng wika — i-parse ang mga French na pangungusap
- Batay sa mga sugnay at resolusyon ng Horn (Robinson, 1965)
- Unang pagpapatupad: unification + backtracking
### Edinburgh Prolog (1977)
- **1977**: Gumawa si David Warren ng DEC-10 Prolog sa Edinburgh
- Efficient compiler — Nagiging praktikal ang Prolog
- Nagiging reference na pagpapatupad ang Edinburgh Prolog
- Mga Impluwensya: Horn clause, depth-first search, cut operator
### ISO Standardization (1995)
- **1995**: Unang pamantayan ng ISO (ISO/IEC 13211-1)
- Tinutukoy ang: syntax, built-in na predicates, arithmetic, I/O
- Tinitiyak ang portability sa mga pagpapatupad
### Modern Prolog (2000s–kasalukuyan)
- **SWI-Prolog**: Pinakalawak na ginagamit — tabling, modules, multi-threading, web (Pengines)
- **GNU Prolog**: Native compilation — mabilis na mga executable
- **Scryer Prolog**: Moderno, Rust-based, ISO-compatible
- **Trealla Prolog**: Mabilis, magaan, C-based
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

## Ebolusyon ng Tampok
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

## Pangunahing Prinsipyo ng Disenyo
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## Paglago ng Ecosystem
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
