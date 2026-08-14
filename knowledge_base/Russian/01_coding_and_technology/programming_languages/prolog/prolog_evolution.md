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
# Пролог — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Пре-Пролог | 1965–70 | Q-системы Кольмерауэра, обработка естественного языка |
| Пролог I | 1972 | **Первый Пролог** (Ален Кольмерауэр, Марсель) |
| ДЕКАБРЬ-10 | 1977 | Эдинбургский Пролог Дэвида Уоррена (эффективный компилятор) |
| ISO Пролог | 1995 | **Первый стандарт ISO** (ISO/IEC 13211-1) |
| SWI-Пролог | 1987 | Ян Вилемейкер — самый популярный Пролог с открытым исходным кодом |
| GNU Пролог | 1999 | Дэниел Диас — родная компиляция |
| ИСО 2-й | 2012 | Исправление 2 (исправление ошибок, уточнения) |
| SWI 8.x | 2018 | Таблицы, обоснование, улучшение производительности |
| SWI 9.x | 2023 | **Таблица** (по умолчанию), улучшенные модули, система пакетов |
| Скраер | 2018 | Современный Пролог в Rust — ISO-совместим |
| Трелла | 2022 | Быстрый Пролог на C — современная реализация |
## Основные вехи
### Рождение Пролога (1972)
- **1972**: Ален Кольмерауэр создает Пролог в Университете Марселя.
- **Название**: «PROgrammation en LOGique» (логическое программирование)
– **Цель**: обработка естественного языка — анализ французских предложений.
- На основе положений и резолюции Хорна (Робинсон, 1965 г.)
- Первая реализация: унификация + возврат
### Эдинбургский Пролог (1977)
- **1977**: Дэвид Уоррен создает Пролог DEC-10 в Эдинбурге.
- Эффективный компилятор — Пролог становится практичным
- Эдинбургский Пролог становится эталонной реализацией.
- Влияния: предложения Horn, поиск в глубину, оператор вырезания.
### Стандартизация ISO (1995)
- **1995**: Первый стандарт ISO (ISO/IEC 13211-1).
- Определяет: синтаксис, встроенные предикаты, арифметику, ввод-вывод.
- Обеспечивает переносимость между реализациями.
### Современный Пролог (2000-е – настоящее время)
- **SWI-Prolog**: наиболее широко используется — таблицы, модули, многопоточность, Интернет (Pengines).
- **GNU Prolog**: собственная компиляция — быстрые исполняемые файлы.
- **Scryer Prolog**: современный, основанный на Rust, совместимый с ISO.
- **Trealla Prolog**: быстрый, легкий, на основе C.
## Эволюция синтаксиса
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

## Эволюция функций
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

## Ключевые принципы проектирования
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## Рост экосистемы
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
