<!--
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

-->
# Prolog — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| ما قبل البرولوج | 1965–70 | أنظمة Q كولميراور، معالجة اللغة الطبيعية |
| برولوج أنا | 1972 | **المقدمة الأولى** (آلان كولميراور، مرسيليا) |
| ديسمبر-10 | 1977 | ديفيد وارن إدنبره برولوج (مترجم فعال) |
| مقدمة ISO | 1995 | **معيار ISO الأول** (ISO/IEC 13211-1) |
| سوي برولوج | 1987 | جان ويليماكر — أشهر برولوج مفتوح المصدر |
| برولوج جنو | 1999 | دانيال دياز — تجميع أصلي |
| ايزو 2 | 2012 | التصويب 2 (إصلاحات الأخطاء، التوضيحات) |
| سوي 8.x | 2018 | الجدولة والعقلانية وتحسين الأداء |
| سوي 9.x | 2023 | **الجدولة** (افتراضي)، الوحدات المحسنة، نظام الحزم |
| سكراير | 2018 | Prolog الحديث في الصدأ - متوافق مع ISO |
| تريلا | 2022 | Fast Prolog في C — التنفيذ الحديث |
## المعالم الرئيسية
### ولادة برولوج (1972)
- **1972**: قام آلان كولميراور بإنشاء Prolog في جامعة مرسيليا
- **الاسم**: "PROgrammation en LOGique" (البرمجة في المنطق)
- **الهدف**: معالجة اللغة الطبيعية - تحليل الجمل الفرنسية
- بناءً على بنود هورن وقراره (روبنسون، 1965)
- التنفيذ الأول: التوحيد + التراجع
### برولوج إدنبرة (1977)
- **1977**: قام ديفيد وارن بإنشاء DEC-10 Prolog في إدنبرة
- مترجم فعال - يصبح Prolog عمليًا
- يصبح Edinburgh Prolog هو التنفيذ المرجعي
- المؤثرات: جمل القرن، بحث العمق الأول، عامل القطع
### توحيد معايير الأيزو (1995)
- **1995**: أول معيار ISO (ISO/IEC 13211-1)
- التعريف: بناء الجملة، المسندات المضمنة، الحساب، الإدخال/الإخراج
-يضمن إمكانية النقل عبر التطبيقات
### البرولوج الحديث (العقد الأول من القرن الحادي والعشرين إلى الوقت الحاضر)
- **SWI-Prolog**: الأكثر استخدامًا — الجداول، والوحدات النمطية، والخيوط المتعددة، والويب (Pengines)
- **GNU Prolog**: تجميع أصلي — ملفات تنفيذية سريعة
- **Scryer Prolog**: حديث، قائم على الصدأ، ومتوافق مع ISO
- **Trealla Prolog**: سريع وخفيف الوزن ومعتمد على لغة C
## تطور بناء الجملة
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

## تطور الميزة
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

## مبادئ التصميم الرئيسية
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## نمو النظام البيئي
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
