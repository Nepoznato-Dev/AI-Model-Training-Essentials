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

# Prolog — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
|前序言 | 1965–70 | Colmerauer 的 Q 系统，自然语言处理 |
|序言我| 1972 | **第一序言**（Alain Colmerauer，马赛）|
| 10 月 10 日 | 1977 | David Warren 的 Edinburgh Prolog（高效编译器）|
| ISO 序言 | 1995 | **第一个 ISO 标准** (ISO/IEC 13211-1) |
| SWI-Prolog | 1987 | Jan Wielemaker — 最受欢迎的开源 Prolog |
| GNU 序言 | 1999 | Daniel Diaz — 原生编译 |
| ISO第二| 2012 |勘误表 2（错误修复、澄清）|
| SWI 8.x | 2018 |表格、合理性、改进的性能 |
| SWI 9.x | 2023 | **表格**（默认），改进的模块，包系统|
|占卜者 | 2018 | Rust 中的现代 Prolog — ISO 兼容 |
|特雷拉| 2022 | 2022 C 语言中的 Fast Prolog — 现代实现 |
## 主要里程碑
### Prolog 的诞生 (1972)
- **1972**：Alain Colmerauer 在马赛大学创建了 Prolog
- **名称**：“PROgrammation en LOGique”（逻辑编程）
- **目标**：自然语言处理——解析法语句子
- 基于霍恩条款和决议（Robinson，1965）
- 第一次实现：统一+回溯
### 爱丁堡序言 (1977)
- **1977**：David Warren 在爱丁堡创建了 DEC-10 Prolog
- 高效的编译器——Prolog变得实用
- Edinburgh Prolog 成为参考实现
- 影响：Horn 子句、深度优先搜索、剪切运算符
### ISO 标准化 (1995)
- **1995**：第一个 ISO 标准 (ISO/IEC 13211-1)
- 定义：语法、内置谓词、算术、I/O
- 确保跨实施的可移植性
### 现代 Prolog（2000 年代至今）
- **SWI-Prolog**：使用最广泛 - 表格、模块、多线程、Web (Pengines)
- **GNU Prolog**：本机编译 — 快速可执行文件
- **Scryer Prolog**：现代、基于 Rust、ISO 兼容
- **Trealla Prolog**：快速、轻量级、基于 C
## 语法演变
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

## 功能演变
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

## 关键设计原则
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## 生态系统增长
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
