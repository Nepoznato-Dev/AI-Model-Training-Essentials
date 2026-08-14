<!--
---
# Metadata
title: "Prolog — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic Prolog code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [prolog, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "8 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# 프롤로그 — 관용적 패턴 및 모범 사례
이 가이드는 깔끔하고 관용적인 프롤로그 코드를 작성하기 위한 관용적인 패턴을 다룹니다.
---

## 패턴 매칭
```prolog
% ✅ Head matching for clarity
factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

% ✅ List patterns
my_length([], 0).
my_length([_|T], N) :-
    my_length(T, N1),
    N is N1 + 1.

% ✅ Guard clauses
classify(N, positive) :- N > 0.
classify(0, zero).
classify(N, negative) :- N < 0.
```

---

## 컷 및 결정론
```prolog
% ✅ Green cut (remove unnecessary choicepoints)
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).

% ✅ Avoid red cuts (changing semantics)
% ✅ Use -> (if-then-else) instead
classify(N) ->
    ( N > 0 -> positive
    ; N =:= 0 -> zero
    ; negative
    ).
```

---

## 요약
프롤로그 관용구는 머리의 패턴 일치, 누산기를 사용한 꼬리 재귀, 효율성을 위한 녹색 컷 및 선언적 스타일을 강조합니다. Prolog 스타일 규칙을 따르세요. 프롤로그는 논리적 순수성을 중요시합니다. "관계는 프로그램입니다."