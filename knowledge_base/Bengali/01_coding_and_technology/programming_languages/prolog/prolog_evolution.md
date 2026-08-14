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
# প্রোলগ — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| প্রি-প্রোলগ | 1965-70 | Colmerauer এর Q-সিস্টেম, প্রাকৃতিক ভাষা প্রক্রিয়াকরণ |
| Prolog I | 1972 | **প্রথম প্রলোগ** (অ্যালাইন কলমেরউয়ার, মার্সেই) |
| DEC-10 | 1977 | ডেভিড ওয়ারেনের এডিনবার্গ প্রোলগ (দক্ষ কম্পাইলার) |
| ISO প্রোলগ | 1995 | **প্রথম ISO মান** (ISO/IEC 13211-1) |
| SWI-Prolog | 1987 | Jan Wielemaker — সবচেয়ে জনপ্রিয় ওপেন সোর্স প্রোলগ |
| GNU Prolog | 1999 | ড্যানিয়েল দিয়াজ — দেশীয় সংকলন |
| ISO 2য় | 2012 | সংশোধনী 2 (বাগ সংশোধন, স্পষ্টীকরণ) |
| SWI 8.x | 2018 | টেবিল, যুক্তি, উন্নত কর্মক্ষমতা |
| SWI 9.x | 2023 | **টেবিলিং** (ডিফল্ট), উন্নত মডিউল, প্যাক সিস্টেম |
| স্ক্রিয়ার | 2018 | মরিচায় আধুনিক প্রোলগ — ISO- সামঞ্জস্যপূর্ণ |
| ত্রেলা | 2022 | C-তে দ্রুত প্রোলগ — আধুনিক বাস্তবায়ন |
## প্রধান মাইলফলক
### প্রোলগের জন্ম (1972)
- **1972**: অ্যালাইন কলমেরউয়ার মার্সেই বিশ্ববিদ্যালয়ে প্রোলগ তৈরি করেন
- **নাম**: "প্রোগ্রামেশন এন লজিক" (লজিকে প্রোগ্রামিং)
- **লক্ষ্য**: প্রাকৃতিক ভাষা প্রক্রিয়াকরণ — ফরাসি বাক্য পার্স করুন
- হর্ন ক্লজ এবং রেজোলিউশনের উপর ভিত্তি করে (রবিনসন, 1965)
- প্রথম বাস্তবায়ন: একীকরণ + ব্যাকট্র্যাকিং
### এডিনবার্গ প্রোলগ (1977)
- **1977**: ডেভিড ওয়ারেন এডিনবার্গে DEC-10 প্রোলগ তৈরি করেছেন
- দক্ষ কম্পাইলার - প্রোলগ ব্যবহারিক হয়ে ওঠে
- এডিনবার্গ প্রোলগ রেফারেন্স বাস্তবায়ন হয়ে যায়
- প্রভাব: হর্ন ক্লজ, গভীরতা-প্রথম অনুসন্ধান, কাটা অপারেটর
### ISO স্ট্যান্ডার্ডাইজেশন (1995)
- **1995**: প্রথম ISO স্ট্যান্ডার্ড (ISO/IEC 13211-1)
- সংজ্ঞায়িত করে: সিনট্যাক্স, অন্তর্নির্মিত পূর্বাভাস, পাটিগণিত, I/O
- বাস্তবায়ন জুড়ে বহনযোগ্যতা নিশ্চিত করে
### আধুনিক প্রোলগ (2000-বর্তমান)
- **SWI-Prolog**: সর্বাধিক ব্যবহৃত — টেবিলিং, মডিউল, মাল্টি-থ্রেডিং, ওয়েব (পেনজিন)
- **GNU প্রোলগ**: নেটিভ কম্পাইলেশন — দ্রুত এক্সিকিউটেবল
- **স্ক্রাইয়ার প্রোলগ**: আধুনিক, মরিচা-ভিত্তিক, ISO-সামঞ্জস্যপূর্ণ
- **Trealla Prolog**: দ্রুত, লাইটওয়েট, C-ভিত্তিক
## সিনট্যাক্স বিবর্তন
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

## বৈশিষ্ট্য বিবর্তন
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

## মূল ডিজাইনের নীতি
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## ইকোসিস্টেম বৃদ্ধি
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
