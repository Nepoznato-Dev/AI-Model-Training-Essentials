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

# Prolog - اشتباهات رایج و ضد الگوها
این سند رایج ترین اشتباهات، تله ها و ضد الگوها را در Prolog با اصلاحات فهرست می کند.
---

## 1.`=`در مقابل`==`در مقابل `is`
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

## 2. عدم استفاده صحیح از برش (`!`)
```prolog
% ❌ WRONG — cut in wrong place causes missed solutions
max(X, Y, X) :- X >= Y.
max(X, Y, Y).  % always tries second clause too

% ✅ CORRECT — cut prevents unnecessary backtracking
max(X, _, X) :- X >= 0, !.
max(_, Y, Y).
```

---

## 3. بازگشت بی نهایت
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

## 4. عدم درک اتفاق می افتد بررسی کنید
```prolog
% ❌ WRONG — X = f(X) creates infinite term
?- X = f(X).
% In most Prologs: succeeds (X = f(f(f(f(...)))))
% With occurs check: fails (correct behavior)

% ✅ CORRECT — enable occurs check
% SWI-Prolog: set_prolog_flag(occurs_check, true).
```

---

## 5. عملیات بدون انباشته را فهرست کنید
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

## خلاصه
الگوی برنامه نویسی منطقی Prolog تله های منحصر به فردی ایجاد می کند: گیج کننده`=`(یکسان سازی)،`==`(برابری)، و`is`(حساب). قرار دادن برش نادرست؛ بازگشت بی نهایت بدون ردیابی بازدید شده. و رخ می دهد بررسی کنید. راه پرولوگ این است: یکپارچگی را عمیقاً درک کنید، از برش به مقدار کم و درست استفاده کنید، از انباشته‌کننده‌ها برای ایجاد فهرست کارآمد استفاده کنید و همیشه خاتمه را در نظر بگیرید.