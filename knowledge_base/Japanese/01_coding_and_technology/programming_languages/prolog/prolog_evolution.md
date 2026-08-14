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

# Prolog — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|プロローグ前 | 1965 ～ 1970 年 | Colmerauer の Q システム、自然言語処理 |
|プロローグ I | 1972年 | **最初のプロローグ** (アラン・コルメラウアー、マルセイユ) |
| 12 月 10 日 | 1977年 | David Warren の Edinburgh Prolog (効率的なコンパイラー) |
| ISO プロローグ | 1995年 | **最初の ISO 規格** (ISO/IEC 13211-1) |
| SWI-プロローグ | 1987年 | Jan Wielemaker — 最も人気のあるオープンソース Prolog |
| GNU プロローグ | 1999年 |ダニエル・ディアス — ネイティブ・コンピレーション |
| ISO 2 | 2012年 |正誤表 2 (バグ修正、明確化) |
| SWI 8.x | 2018年 |テーブル作成、理論的根拠、パフォーマンスの向上 |
| SWI 9.x | 2023年 | **テーブル** (デフォルト)、改良されたモジュール、パック システム |
|スクライヤー | 2018年 | Rust の最新 Prolog — ISO 互換 |
|トレアラ | 2022年 | C での高速 Prolog — 最新の実装 |
## 主要なマイルストーン
### プロローグ誕生 (1972)
- **1972**: アラン・コルメラウアーがマルセイユ大学でプロローグを作成
- **名前**: "PROgrammation en LOGique" (ロジックでのプログラミング)
- **目標**: 自然言語処理 — フランス語の文章を解析する
- ホーン条項と決議に基づく (ロビンソン、1965 年)
- 最初の実装: 統合 + バックトラッキング
### エディンバラ プロローグ (1977)
- **1977**: David Warren がエディンバラで DEC-10 Prolog を作成
- 効率的なコンパイラ — Prolog が実用的になります
- Edinburgh Prolog がリファレンス実装になります
- 影響: ホーン節、深さ優先検索、カット演算子
### ISO標準化(1995年)
- **1995**: 最初の ISO 規格 (ISO/IEC 13211-1)
- 定義: 構文、組み込み述語、算術演算、I/O
- 実装間での移植性を確保
### 現代のプロローグ (2000 年代～現在)
- **SWI-Prolog**: 最も広く使用されている — テーブル作成、モジュール、マルチスレッド、Web (Pengines)
- **GNU プロローグ**: ネイティブ コンパイル — 高速実行可能ファイル
- **Scryer Prolog**: 最新、Rust ベース、ISO 互換
- **Trealla Prolog**: 高速、軽量、C ベース
## 構文の進化
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

## 機能の進化
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

## 主要な設計原則
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## エコシステムの成長
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
