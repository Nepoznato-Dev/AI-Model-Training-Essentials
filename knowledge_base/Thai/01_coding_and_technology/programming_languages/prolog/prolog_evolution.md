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
# Prolog - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| พรีโปรล็อก | พ.ศ. 2508–70 | ระบบ Q ของ Colmerauer การประมวลผลภาษาธรรมชาติ
| อารัมภบท ฉัน | 1972 | **คำนำแรก** (Alain Colmerauer, Marseille) |
| ธ.ค.-10 | 2520 | Edinburgh Prolog ของ David Warren (คอมไพเลอร์ที่มีประสิทธิภาพ) |
| ISO คำนำ | 1995 | **มาตรฐาน ISO ฉบับแรก** (ISO/IEC 13211-1) |
| SWI-คำนำ | 1987 | Jan Wielemaker — Prolog | โอเพ่นซอร์สที่ได้รับความนิยมสูงสุด
| GNU เปิดฉาก | 1999 | Daniel Diaz — การรวบรวมพื้นเมือง |
| ISO 2 | 2555 | Corrigendum 2 (แก้ไขข้อบกพร่อง ชี้แจง) |
| SWI 8.x | 2018 | การทำตาราง เหตุผล ประสิทธิภาพที่ดีขึ้น |
| SWI 9.x | 2023 | **การทำตาราง** (ค่าเริ่มต้น), โมดูลที่ได้รับการปรับปรุง, ระบบแพ็ค |
| สครายเออร์ | 2018 | Modern Prolog in Rust — รองรับ ISO |
| เทรลลา | 2022 | Fast Prolog ใน C — การใช้งานที่ทันสมัย ​​|
## เหตุการณ์สำคัญที่สำคัญ
### กำเนิดอารัมภบท (1972)
- **1972**: Alain Colmerauer สร้าง Prolog ที่ University of Marseille
- **ชื่อ**: "PROgrammation en LOGique" (การเขียนโปรแกรมในตรรกะ)
- **เป้าหมาย**: การประมวลผลภาษาธรรมชาติ — แยกประโยคภาษาฝรั่งเศส
- ขึ้นอยู่กับคำสั่งและมติของ Horn (Robinson, 1965)
- การใช้งานครั้งแรก: การรวม + การย้อนรอย
### เอดินบะระอารัมภบท (1977)
- **1977**: David Warren สร้าง DEC-10 Prolog ที่เอดินบะระ
- คอมไพเลอร์ที่มีประสิทธิภาพ — Prolog ใช้งานได้จริง
- Edinburgh Prolog กลายเป็นการดำเนินการอ้างอิง
- อิทธิพล: ประโยคแตร, การค้นหาเชิงลึกก่อน, ตัวดำเนินการตัด
### การกำหนดมาตรฐาน ISO (1995)
- **1995**: มาตรฐาน ISO ฉบับแรก (ISO/IEC 13211-1)
- กำหนด: ไวยากรณ์, เพรดิเคตในตัว, เลขคณิต, I/O
- รับประกันความสะดวกในการพกพาในการใช้งาน
### บทนำสมัยใหม่ (2000-ปัจจุบัน)
- **SWI-Prolog**: ใช้กันอย่างแพร่หลาย — การทำตาราง, โมดูล, มัลติเธรด, เว็บ (Pengines)
- **GNU Prolog**: การคอมไพล์แบบเนทีฟ — ปฏิบัติการได้รวดเร็ว
- **Scryer Prolog**: ทันสมัย เป็นสนิม และเข้ากันได้กับ ISO
- **Trealla Prolog**: รวดเร็ว น้ำหนักเบา ใช้ภาษา C
## วิวัฒนาการไวยากรณ์
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

## วิวัฒนาการคุณสมบัติ
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

## หลักการออกแบบที่สำคัญ
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## การเติบโตของระบบนิเวศ
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
