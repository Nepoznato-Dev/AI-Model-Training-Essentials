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
# Prolog: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Pre-Prologo | 1965–70 | Sistemi Q di Colmerauer, elaborazione del linguaggio naturale |
| Prologo I | 1972 | **Primo Prologo** (Alain Colmerauer, Marsiglia) |
| DIC-10 | 1977 | Edinburgh Prolog (compilatore efficiente) di David Warren |
| Prologo ISO | 1995 | **Prima norma ISO** (ISO/IEC 13211-1) |
| Prologo SWI | 1987 | Jan Wielemaker — il Prolog open source più popolare |
| Prologo GNU | 1999 | Daniel Diaz - compilazione nativa |
| ISO 2° | 2012| Rettifica 2 (correzioni di bug, chiarimenti) |
| SWI 8.x | 2018 | Tabella, razionali, prestazioni migliorate |
| SWI 9.x | 2023 | **Tabella** (predefinita), moduli migliorati, sistema di pack |
| Veggente | 2018 | Modern Prolog in Rust — compatibile ISO |
| Trella | 2022 | Fast Prolog in C: implementazione moderna |
## Traguardi importanti
### Nascita di Prolog (1972)
- **1972**: Alain Colmerauer crea Prolog all'Università di Marsiglia
- **Nome**: "PROgrammation en LOGique" (programmazione in logica)
- **Obiettivo**: elaborazione del linguaggio naturale: analizzare frasi francesi
- Basato su clausole e risoluzioni di Horn (Robinson, 1965)
- Prima implementazione: unificazione + backtracking
### Prologo di Edimburgo (1977)
- **1977**: David Warren crea il DEC-10 Prolog a Edimburgo
- Compilatore efficiente: Prolog diventa pratico
- Edinburgh Prolog diventa l'implementazione di riferimento
- Influenze: clausole di corno, ricerca in profondità, operatore di taglio
### Standardizzazione ISO (1995)
- **1995**: Primo standard ISO (ISO/IEC 13211-1)
- Definisce: sintassi, predicati incorporati, aritmetica, I/O
- Garantisce la portabilità tra le implementazioni
### Prologo moderno (anni 2000-oggi)
- **SWI-Prolog**: il più utilizzato: tabelle, moduli, multi-threading, web (Pengines)
- **GNU Prolog**: compilazione nativa: eseguibili veloci
- **Scryer Prolog**: moderno, basato su Rust, compatibile ISO
- **Trealla Prolog**: veloce, leggero, basato su C
## Evoluzione della sintassi
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

## Evoluzione delle funzionalità
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

## Principi chiave di progettazione
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## Crescita dell'ecosistema
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
