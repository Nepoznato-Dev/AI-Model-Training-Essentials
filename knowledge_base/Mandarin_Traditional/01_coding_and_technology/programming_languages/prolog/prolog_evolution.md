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

# Prolog — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|前序言 | 1965–70 | Colmerauer 的 Q 系統，自然語言處理 |
|序我| 1972 | **第一序**（Alain Colmerauer，馬賽）|
| 10 月 10 日 | 1977 | David Warren 的 Edinburgh Prolog（高效編譯器）|
| ISO 序文 | 1995 | **第一 ISO 標準** (ISO/IEC 13211-1) |
| SWI-Prolog | 1987 | Jan Wielemaker — 最受歡迎的開源 Prolog |
| GNU 前言 | 1999 | Daniel Diaz — 原生編譯 |
| ISO第二| 2012 |勘誤表 2（錯誤修復、澄清）|
| SWI 8.x | 2018 |表格、合理性、改進的性能 |
| SWI 9.x | 2023 | **表格**（預設），改進的模組，包系統|
|占卜者 | 2018 | Rust 中的現代 Prolog — ISO 相容 |
|特雷拉| 2022 | 2022 C 語言中的 Fast Prolog — 現代實作 |
## 主要里程碑
### Prolog 的誕生 (1972)
- **1972**：Alain Colmerauer 在馬賽大學創立了 Prolog
- **名稱**：「PROgrammation en LOGique」（邏輯程式設計）
- **目標**：自然語言處理－解析法文句子
- 基於霍恩條款與決議（Robinson，1965）
- 第一次實現：統一+回溯
### 愛丁堡序言 (1977)
- **1977**：David Warren 在愛丁堡創建了 DEC-10 Prolog
- 高效率的編譯器－Prolog變得實用
- Edinburgh Prolog 成為參考實現
- 影響：Horn 子句、深度優先搜尋、剪切運算符
### ISO 標準化 (1995)
- **1995**：第一個 ISO 標準 (ISO/IEC 13211-1)
- 定義：語法、內建謂詞、算術、I/O
- 確保跨實施的可移植性
### 現代 Prolog（2000 年代至今）
- **SWI-Prolog**：使用最廣泛 - 表格、模組、多執行緒、Web (Pengines)
- **GNU Prolog**：本機編譯 — 快速執行檔
- **Scryer Prolog**：現代、基於 Rust、ISO 相容
- **Trealla Prolog**：快速、輕量級、基於 C
## 語法演變
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

## 功能演變
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

## 關鍵設計原則
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## 生態系成長
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
