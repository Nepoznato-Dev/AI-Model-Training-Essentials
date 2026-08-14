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
# Prolog - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| پیش پرولوگ | 1965–70 | سیستم های Q Colmerauer، پردازش زبان طبیعی |
| پرولوگ I | 1972 | **اولین پرولوگ** (آلن کولمرائر، مارسی) |
| دسامبر-10 | 1977 | دیوید وارن Edinburgh Prolog (کامپایلر کارآمد) |
| ISO Prolog | 1995 | **اولین استاندارد ISO** (ISO/IEC 13211-1) |
| SWI-Prolog | 1987 | Jan Wielemaker — محبوب ترین منبع باز Prolog |
| پرولوگ گنو | 1999 | دانیل دیاز — گردآوری بومی |
| ISO 2 | 2012 | تصحیح 2 (رفع اشکال، توضیحات) |
| SWI 8.x | 2018 | جدول بندی، منطقی، بهبود عملکرد |
| SWI 9.x | 2023 | **جدول** (پیش فرض)، ماژول های بهبود یافته، سیستم بسته |
| اسکریر | 2018 | Prolog مدرن در Rust — سازگار با ISO |
| تریلا | 2022 | Fast Prolog در C — پیاده سازی مدرن |
## نقاط عطف اصلی
### تولد پرولوگ (1972)
- **1972**: آلن کولمرائر Prolog را در دانشگاه مارسی ایجاد کرد
- **نام**: "PROgrammation en LOGique" (برنامه نویسی در منطق)
- **هدف **: پردازش زبان طبیعی - جملات فرانسوی را تجزیه کنید
- بر اساس بندهای هورن و قطعنامه (رابینسون، 1965)
- اجرای اول: یکسان سازی + عقب نشینی
### Edinburgh Prolog (1977)
- **1977**: دیوید وارن DEC-10 Prolog را در ادینبورگ ایجاد کرد
- کامپایلر کارآمد - Prolog عملی می شود
- Edinburgh Prolog به پیاده سازی مرجع تبدیل می شود
- تأثیرات: بندهای شاخ، جستجوی اول عمق، عملگر برش
### استانداردسازی ISO (1995)
- **1995**: اولین استاندارد ISO (ISO/IEC 13211-1)
- تعریف می کند: نحو، محمولات داخلی، حساب، I/O
- قابلیت حمل در سراسر پیاده سازی ها را تضمین می کند
### مدرن Prolog (دهه 2000–اکنون)
- **SWI-Prolog**: پرکاربردترین - جدول گذاری، ماژول ها، چند رشته ای، وب (Pengines)
- **GNU Prolog**: کامپایل بومی — فایل های اجرایی سریع
- ** Scryer Prolog **: مدرن، مبتنی بر زنگ، سازگار با ISO
- **Trealla Prolog**: سریع، سبک وزن، مبتنی بر C
## تکامل نحو
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

## تکامل ویژگی
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

## اصول کلیدی طراحی
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## رشد اکوسیستم
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
