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

# 프롤로그 — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 프롤로그 전 | 1965~70 | Colmerauer의 Q-시스템, 자연어 처리 |
| 프롤로그 I | 1972 | **첫 번째 프롤로그** (Alain Colmerauer, 마르세유) |
| 12월 10일 | 1977 | David Warren의 Edinburgh Prolog(효율적인 컴파일러) |
| ISO 프롤로그 | 1995 | **최초의 ISO 표준** (ISO/IEC 13211-1) |
| SWI-프롤로그 | 1987 | Jan Wielemaker — 가장 인기 있는 오픈 소스 Prolog |
| GNU 프롤로그 | 1999 | 다니엘 디아즈 — 네이티브 컴파일 |
| ISO 2위 | 2012 | 정오표 2(버그 수정, 설명) |
| SWI 8.x | 2018 | 표 작성, 근거, 성능 향상 |
| SWI 9.x | 2023년 | **테이블링**(기본값), 향상된 모듈, 팩 시스템 |
| 점술가 | 2018 | Rust의 최신 프롤로그 — ISO 호환 |
| 트렐라 | 2022 | C의 빠른 프롤로그 — 현대적인 구현 |
## 주요 이정표
### 프롤로그의 탄생(1972)
- **1972**: 알랭 콜메라우어(Alain Colmerauer)가 마르세유 대학교에서 프롤로그를 만듭니다.
- **이름**: "PROgrammation en LOGique"(로직 프로그래밍)
- **목표**: 자연어 처리 - 프랑스어 문장 구문 분석
- Horn 조항 및 결의안을 바탕으로 함(Robinson, 1965)
- 첫 번째 구현: 통합 + 역추적
### 에든버러 프롤로그(1977)
- **1977**: David Warren이 에든버러에서 DEC-10 프롤로그를 작성함
- 효율적인 컴파일러 — 프롤로그가 실용적이 됩니다
- Edinburgh Prolog가 참조 구현이 됨
- 영향: 혼 절, 깊이 우선 검색, 절단 연산자
### ISO 표준화(1995)
- **1995**: 최초의 ISO 표준(ISO/IEC 13211-1)
- 정의: 구문, 내장 조건자, 산술, I/O
- 구현 전반에 걸쳐 이식성을 보장합니다.
### 모던 프롤로그(2000년대~현재)
- **SWI-Prolog**: 가장 널리 사용됨 — 테이블링, 모듈, 멀티스레딩, 웹(Pengines)
- **GNU 프롤로그**: 기본 컴파일 — 빠른 실행 파일
- **Scryer 프롤로그**: 최신, Rust 기반, ISO 호환
- **Tralla Prolog**: 빠르고 가벼우며 C 기반
## 구문 진화
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

## 기능 진화
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

## 주요 디자인 원칙
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## 생태계 성장
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
