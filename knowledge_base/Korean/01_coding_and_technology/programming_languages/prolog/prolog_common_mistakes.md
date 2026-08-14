---
# Metadata
title: "Prolog — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Prolog with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [prolog, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# 프롤로그 — 일반적인 실수 및 안티 패턴
이 문서에는 Prolog의 가장 일반적인 실수, 함정 및 방지 패턴이 수정되어 목록화되어 있습니다.
---

## 1.`=`대`==`대 `is`
```prolog
% ❌ WRONG — confusing unification with equality
X = 5.          % unifies X with 5
X == 5.         % strict equality (no unification)
X is 2 + 3.     % arithmetic evaluation

% ✅ CORRECT — understand the difference
% = is unification (pattern matching)
% == is strict equality (both sides must be identical)
% is evaluates arithmetic on the right side
```

---

## 2. 컷(`!`)을 올바르게 사용하지 않음
```prolog
% ❌ WRONG — cut in wrong place causes missed solutions
max(X, Y, X) :- X >= Y.
max(X, Y, Y).  % always tries second clause too

% ✅ CORRECT — cut prevents unnecessary backtracking
max(X, _, X) :- X >= 0, !.
max(_, Y, Y).
```

---

## 3. 무한 재귀
```prolog
% ❌ WRONG — no base case or wrong order
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
% If parent has cycles, this loops forever

% ✅ CORRECT — track visited nodes
ancestor(X, Y, Visited) :-
    parent(X, Y),
    \+ member(X, Visited).
ancestor(X, Y, Visited) :-
    parent(X, Z),
    \+ member(Z, Visited),
    ancestor(Z, Y, [Z|Visited]).
```

---

## 4. 이해가 되지 않는 현상이 발생하는지 확인
```prolog
% ❌ WRONG — X = f(X) creates infinite term
?- X = f(X).
% In most Prologs: succeeds (X = f(f(f(f(...)))))
% With occurs check: fails (correct behavior)

% ✅ CORRECT — enable occurs check
% SWI-Prolog: set_prolog_flag(occurs_check, true).
```

---

## 5. 누산기 없이 목록 작업
```prolog
% ❌ WRONG — inefficient list append
my_append([], L, L).
my_append([H|T], L, [H|R]) :- my_append(T, L, R).
% O(n) per call, O(n²) for building list

% ✅ CORRECT — use accumulator for building lists
reverse(List, Reversed) :- reverse(List, [], Reversed).
reverse([], Acc, Acc).
reverse([H|T], Acc, Reversed) :- reverse(T, [H|Acc], Reversed).
```

---

## 요약
Prolog의 논리 프로그래밍 패러다임은 `=`(통합), `==`(동등) 및 `is`(산술)를 혼동하는 독특한 함정을 만듭니다. 잘못된 컷 배치; 방문 추적 없는 무한 재귀; 그리고 발생 확인이 이루어집니다. Prolog 방식은 통합을 깊이 이해하고, 컷을 아껴서 올바르게 사용하고, 효율적인 목록 작성을 위해 누산기를 사용하고, 항상 종료를 고려하는 것입니다.