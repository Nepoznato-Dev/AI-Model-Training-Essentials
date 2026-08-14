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

# Prolog — 常見錯誤與反模式
本文檔列出了 Prolog 中最常見的錯誤、陷阱和反模式，並進行了修正。
---

## 1.`=`vs`==`vs `is`
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

## 2. 未正確使用剪切 (`!`)
```prolog
% ❌ WRONG — cut in wrong place causes missed solutions
max(X, Y, X) :- X >= Y.
max(X, Y, Y).  % always tries second clause too

% ✅ CORRECT — cut prevents unnecessary backtracking
max(X, _, X) :- X >= 0, !.
max(_, Y, Y).
```

---

## 3.無限遞迴
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

## 4. 不理解發生檢查
```prolog
% ❌ WRONG — X = f(X) creates infinite term
?- X = f(X).
% In most Prologs: succeeds (X = f(f(f(f(...)))))
% With occurs check: fails (correct behavior)

% ✅ CORRECT — enable occurs check
% SWI-Prolog: set_prolog_flag(occurs_check, true).
```

---

## 5. 不使用累加器的列表操作
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

＃＃ 概括
Prolog的邏輯程式設計範式創造了獨特的陷阱：混淆`=`（統一）、`==`（相等）和`is`（算術）；切割位置不正確；無限遞歸，無需存取追蹤；並進行檢查。 Prolog 的方式是：深入理解統一，謹慎且正確地使用 cut，使用累加器進行高效的列表構建，並始終考慮終止。