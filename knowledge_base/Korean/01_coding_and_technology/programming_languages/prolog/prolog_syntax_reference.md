---
# Metadata
title: "Prolog — Syntax Reference"
description: "Detailed syntax reference for Prolog covering unification, backtracking, cut, DCGs, and logic programming patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [prolog, syntax-reference, unification, backtracking, logic-programming, dcg, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 프롤로그 — 구문 참조
이 문서는 Prolog에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 이는 철저한 구문 패턴, 통합, 역추적, DCG 및 논리 프로그래밍 관용구에 중점을 두어 기본 Prolog 참조를 보완합니다.
---

## 핵심 구문
```prolog
% Facts
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).

% Rules
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Queries (in the REPL)
?- parent(tom, bob).        % true
?- parent(tom, X).          % X = bob ; X = liz
?- grandparent(tom, ann).   % true
```

---

## 통일 & 매칭
```prolog
% = is unification (not assignment!)
?- X = hello.               % X = hello
?- f(X, b) = f(a, Y).       % X = a, Y = b
?- [H|T] = [1, 2, 3].       % H = 1, T = [2, 3]

% \= is not-unifiable
?- a \= b.                  % true
?- X \= 5.                  % error (X is unbound)

% Anonymous variable
?- f(a, _, c) = f(a, b, c). % true

% is for arithmetic evaluation
?- X is 2 + 3.              % X = 5
?- X = 2 + 3.               % X = 2+3 (unevaluated)
```

---

## 제어 및 역추적
```prolog
% Cut (!) — prevent backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).

% Fail — force backtracking
safe(X) :- X > 0, !.
safe(_).  % fallback

% Negation as failure
different(X, Y) :- X \= Y.

% If-then-else
classify(X, Result) :-
    ( X > 0 -> Result = positive
    ; X < 0 -> Result = negative
    ; Result = zero
    ).

% Find all solutions
?- findall(X, color(X), Colors).
% Colors = [red, green, blue]

?- bagof(X, parent(tom, X), Children).
% Children = [bob, liz]
```

---

## 목록 작업
```prolog
% Length
my_length([], 0).
my_length([_|T], N) :- my_length(T, N1), N is N1 + 1.

% Append
my_append([], L, L).
my_append([H|T], L, [H|R]) :- my_append(T, L, R).

% Member
my_member(X, [X|_]).
my_member(X, [_|T]) :- my_member(X, T).

% Last element
my_last([X], X).
my_last([_|T], X) :- my_last(T, X).

% Reverse
my_reverse([], []).
my_reverse([H|T], R) :-
    my_reverse(T, RT),
    my_append(RT, [H], R).

% Map
my_map(_, [], []).
my_map(F, [H|T], [FH|FT]) :-
    call(F, H, FH),
    my_map(F, T, FT).

% Fold
my_foldl(_, Acc, [], Acc).
my_foldl(Goal, Acc, [H|T], Result) :-
    call(Goal, Acc, H, NewAcc),
    my_foldl(Goal, NewAcc, T, Result).
```

---

## 정관사 문법(DCG)
```prolog
% Parse arithmetic expressions
expr --> term, ("+", expr | "").
term --> factor, ("*", term | "").
factor --> [N], { number(N) }.
factor --> "(", expr, ")".

% Parse natural language
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb.
verb_phrase --> verb, noun_phrase.

determiner --> [the] | [a].
noun --> [cat] | [dog] | [fish].
verb --> [chases] | [eats] | [sees].

% Query: phrase(sentence, [the, cat, chases, the, dog]).
```

---

## 요약
Prolog의 구문은 최소한의 사실, 규칙 및 쿼리입니다. 그 힘은 언어를 논리적 해결책을 위한 검색 엔진으로 바꾸는 통합과 역추적에서 나옵니다. DCG는 우아한 파서 생성을 제공합니다. 목록은 머리/꼬리 패턴 일치를 사용합니다. 제약 조건 충족, 전문가 시스템 및 기호 계산을 위해 Prolog의 선언적 접근 방식은 명령형 언어에서 장황한 문제를 해결합니다.