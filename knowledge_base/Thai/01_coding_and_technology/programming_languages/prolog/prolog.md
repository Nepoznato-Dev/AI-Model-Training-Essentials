---
# Metadata
title: "Prolog"
description: "Comprehensive reference for the Prolog programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prolog, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

#โปรล็อก
Prolog (การเขียนโปรแกรมในลอจิก) เป็นภาษาโปรแกรมลอจิกที่สร้างขึ้นในปี 1972 โดย Alain Colmerauer และ Philippe Roussel ไม่เหมือนกับภาษาอื่นๆ ทุกภาษาในรายการนี้ Prolog ไม่ได้บอกคอมพิวเตอร์ *วิธี* ในการแก้ปัญหา — คุณประกาศว่า *อะไร* เป็นจริง (ข้อเท็จจริงและกฎเกณฑ์) และระบบอนุมานของ Prolog จะระบุคำตอบผ่านการอนุมานเชิงตรรกะ
Prolog เป็นภาษาทางเลือกสำหรับระบบผู้เชี่ยวชาญ การประมวลผลภาษาธรรมชาติ และการวิจัย AI ในทศวรรษ 1980 มันขับเคลื่อนโครงการระบบคอมพิวเตอร์รุ่นที่ห้าของญี่ปุ่นและใช้ในวัตสันของไอบีเอ็มเพื่อความเข้าใจภาษาธรรมชาติ ปัจจุบัน Prolog ใช้ในการแก้ไขข้อจำกัด การกำหนดเวลา การอนุมานประเภท การใช้เหตุผลทางกฎหมาย และปัญหาใดๆ ก็ตามที่แสดงออกมาเป็นความสัมพันธ์เชิงตรรกะโดยธรรมชาติ
**การเขียนโปรแกรมลอจิกข้อจำกัด (CLP)** ขยาย Prolog ด้วยตัวแก้ปัญหาข้อจำกัดสำหรับการกำหนดเวลา การกำหนดเส้นทาง และการจัดสรรทรัพยากร ซึ่งเป็นปัญหาที่ยากมากในภาษาที่จำเป็น
---

## ทำไมเรื่อง Prolog
- **การเขียนโปรแกรมเชิงประกาศ**: อธิบายว่าอะไรเป็นความจริง ไม่ใช่วิธีคำนวณ เครื่องยนต์ทำงานได้
- **การจับคู่รูปแบบและการรวมรูปแบบ**: อัลกอริธึมการรวมของ Prolog มีประสิทธิภาพมากกว่าการจับคู่รูปแบบในภาษาอื่น
- **การค้นหาแบบย้อนรอย**: สำรวจวิธีแก้ปัญหาที่เป็นไปได้ทั้งหมดโดยอัตโนมัติ ไม่จำเป็นต้องมีอัลกอริธึมการค้นหาด้วยตนเอง
- **โดยธรรมชาติสำหรับปัญหาตรรกะ**: ระบบผู้เชี่ยวชาญ เอ็นจิ้นกฎ ตัวตรวจสอบประเภท ตัวแยกวิเคราะห์ไวยากรณ์ - แมปเหล่านี้โดยตรงกับ Prolog
- **การแก้ไขข้อจำกัด**: CLP(FD) แก้ปัญหาการจัดกำหนดการ การจัดสรร และการผสมผสานอย่างสวยงาม
- **การคิดที่แตกต่าง**: คำนำการเรียนรู้จะเปลี่ยนวิธีการแก้ปัญหาของคุณ — คุณเริ่มคิดในความสัมพันธ์และข้อจำกัด
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **กระบวนทัศน์ต่างกันมาก** | ไม่มีตัวแปร (เฉพาะการเชื่อมโยง) ไม่มีการวนซ้ำ ไม่มีการกำหนด | คิดในความสัมพันธ์และการเรียกซ้ำ ไม่ใช่การเปลี่ยนแปลงสถานะ |
| **ประสิทธิภาพ** | ช้าสำหรับการคำนวณตัวเลขและข้อมูลขนาดใหญ่ | ใช้สำหรับการให้เหตุผล มอบหมายการคำนวณให้กับ C/ภาษาอื่น |
| **ความยากในการดีบัก** | ยากที่จะติดตามการย้อนรอยและความล้มเหลวในการรวมระบบ | ใช้เครื่องมือติดตาม/ดีบัก เขียนภาคแสดงกำหนด |
| **ตัวดำเนินการตัด (!)** | จำเป็นสำหรับประสิทธิภาพแต่ทำลายความบริสุทธิ์เชิงตรรกะ | ใช้การประเมินแบบ if-then-else หรือแบบตารางเมื่อเป็นไปได้ |
| **ระบบนิเวศมีจำกัด** | มีไลบรารี เฟรมเวิร์ก หรือทรัพยากรชุมชนน้อย SWI-Prolog เป็นการใช้งานที่สมบูรณ์แบบที่สุด |
| **ไม่ใช่สำหรับแอปทั่วไป** | เว็บ, มือถือ, GUI — ไม่ใช่จุดแข็งของ Prolog | ใช้เป็นเครื่องมือหาเหตุผลเบื้องหลังเว็บแอป |
---

## พื้นฐานไวยากรณ์
```prolog
% Facts (things that are true)
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).

male(tom).
male(bob).
female(liz).
female(ann).
female(pat).

% Rules (logical implications)
father(X, Y) :- parent(X, Y), male(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Recursion
my_length([], 0).
my_length([_|Tail], N) :-
    my_length(Tail, N1),
    N is N1 + 1.

% List processing
my_append([], L, L).
my_append([H|T1], L2, [H|T3]) :-
    my_append(T1, L2, T3).

my_member(X, [X|_]).
my_member(X, [_|Tail]) :- my_member(X, Tail).

% Negation as failure
dislikes(X, Y) :- \+ likes(X, Y).

% Cut (commit to choices)
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).

% Constraint Logic Programming
:- use_module(library(clpfd)).
solve_sudoku(Rows) :-
    append(Rows, Vs), Vs ins 1..9,
    maplist(all_different, Rows),
    columns(Rows, Cols),
    maplist(all_different, Cols),
    maplist(label, Rows).
```

---

## ไวยากรณ์และรูปแบบขั้นสูง
### เจาะลึกการรวมเป็นหนึ่งเดียว
การรวมเป็นกลไกหลักของ Prolog - เป็นวิธีที่ Prolog "จับคู่" เงื่อนไขและผูกตัวแปร
```prolog
% Unification rules:
% 1. Two constants unify if they are identical
%    ?- hello = hello.     -> true
%    ?- hello = world.     -> false
%
% 2. A variable unifies with anything (binding)
%    ?- X = hello.         -> X = hello
%    ?- X = Y.             -> X = Y (shared variable)
%
% 3. Complex terms unify if functors match and all args unify
%    ?- f(X, b) = f(a, Y). -> X = a, Y = b
%    ?- f(a, b) = f(a, c). -> false
%
% 4. Lists unify element by element
%    ?- [H|T] = [1, 2, 3]. -> H = 1, T = [2, 3]

% The == operator (structural equality, no binding)
% ?- X == X.      -> true
% ?- X == Y.      -> false (different variables)
% ?- X = Y, X == Y. -> true (after unification)
```

### การย้อนรอยและคะแนนตัวเลือก
```prolog
% Prolog creates choice points when multiple clauses can match
perm([], []).
perm(L, [H|T]) :-
    select(H, L, Rest),
    perm(Rest, T).

% ?- perm([1,2,3], P).
% P = [1,2,3] ; P = [1,3,2] ; P = [2,1,3] ; ...

% Collecting all solutions
?- findall(X, member(X, [1,2,3,4,5]), All).
% All = [1, 2, 3, 4, 5]

?- bagof(X, parent(Y, X), Children).
% Y = tom, Children = [bob, liz] ;
% Y = bob, Children = [ann, pat].

% Cut operator — prevents backtracking
classify(X, positive) :- X > 0, !.
classify(X, negative) :- X < 0, !.
classify(0, zero).
```

### ไวยากรณ์ประโยคที่ชัดเจน (DCG)
```prolog
% Simple sentence parser
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb.
verb_phrase --> verb, noun_phrase.

determiner --> [the].
determiner --> [a].
noun --> [cat].
noun --> [dog].
noun --> [mouse].
verb --> [chased].
verb --> [ate].

% ?- phrase(sentence, [the, cat, chased, the, mouse]).
% true

% DCG with parse tree construction
sentence(s(NP, VP)) --> noun_phrase(NP), verb_phrase(VP).
noun_phrase(np(Det, N)) --> determiner(Det), noun(N).
verb_phrase(vp(V, NP)) --> verb(V), noun_phrase(NP).
verb_phrase(vp(V)) --> verb(V).

determiner(det(the)) --> [the].
noun(noun(cat)) --> [cat].
verb(verb(chased)) --> [chased].
```

### การเขียนโปรแกรมลอจิกข้อจำกัด (CLP)
```prolog
:- use_module(library(clpfd)).

% SEND + MORE = MONEY puzzle
send_more_money([S,E,N,D,M,O,R,Y]) :-
    Vars = [S,E,N,D,M,O,R,Y],
    Vars ins 0..9,
    all_different(Vars),
    S #> 0, M #> 0,
      S*1000 + E*100 + N*10 + D
    + M*1000 + O*100 + R*10 + E
    #= M*10000 + O*1000 + N*100 + E*10 + Y,
    label(Vars).

% N-Queens problem
n_queens(N, Qs) :-
    length(Qs, N),
    Qs ins 1..N,
    all_different(Qs),
    safe_queens(Qs),
    label(Qs).

safe_queens([]).
safe_queens([Q|Qs]) :-
    no_attack(Q, Qs, 1),
    safe_queens(Qs).

no_attack(_, [], _).
no_attack(Q, [Q1|Qs], D) :-
    Q #\= Q1 + D,
    Q #\= Q1 - D,
    D1 is D + 1,
    no_attack(Q, Qs, D1).
```

---

## สถาปัตยกรรมและการออกแบบระบบ
### กระบวนทัศน์การเขียนโปรแกรมลอจิก
```
+---------------------------------------------+
|              Prolog Program                  |
+---------------------------------------------+
|  Facts:     parent(tom, bob).                |
|             color(red).                      |
+---------------------------------------------+
|  Rules:     grandparent(X, Z) :-             |
|               parent(X, Y), parent(Y, Z).    |
+---------------------------------------------+
|  Queries:   ?- grandparent(tom, X).          |
|             -> X = ann ; X = pat.            |
+---------------------------------------------+
```

### โครงสร้างโครงการทั่วไป
```
prolog-project/
├── src/
│   ├── main.pl              * Entry point
│   ├── rules.pl             * Domain rules
│   ├── facts.pl             * Knowledge base
│   ├── utils.pl             * Utility predicates
│   └── grammar.pl           * DCG definitions
├── tests/
│   ├── test_rules.pl        * Unit tests
│   └── test_grammar.pl      * Grammar tests
├── data/
│   └── knowledge_base.pl    * Fact database
├── Makefile
└── README.md
```

### ระบบโมดูล
```prolog
:- module(validator, [
    validate_user/2,
    validate_email/1,
    check_password/1
]).

% Private predicate
is_valid_length(Str, Min, Max) :-
    string_length(Str, Len),
    Len >= Min, Len =< Max.

% Public predicates
validate_user(User, Errors) :-
    findall(Error, validate_field(User, Error), Errors).

validate_field(user(Name, Email, _), Error) :-
    \+ is_valid_length(Name, 2, 50),
    Error = 'Name must be 2-50 characters'.
validate_field(user(_, Email, _), Error) :-
    \+ validate_email(Email),
    Error = 'Invalid email format'.

validate_email(Email) :-
    atom_string(Email, Str),
    sub_string(Str, _, _, _, @).
```
---

## การกำหนดค่าโครงการ & ระบบการสร้าง
### การกำหนดค่า SWI-Prolog
```prolog
:- set_prolog_flag(verbose, silent).
:- set_prolog_stack(global, limit(2*10**9)).

:- use_module(library(clpfd)).
:- use_module(library(lists)).
:- use_module(library(apply)).

:- dynamic fact_cache/2.

:- table fibonacci/2.
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, F) :-
    N > 1, N1 is N - 1, N2 is N - 2,
    fibonacci(N1, F1), fibonacci(N2, F2),
    F is F1 + F2.
```

### การรันโปรแกรม Prolog
```bash
# Interactive mode
swipl
?- [main].
?- halt.

# Run query from command line
swipl -g "solve(X), write(X), nl, halt" -s main.pl

# Compile to standalone executable
swipl -o solver -g main -c main.pl

# Run tests
swipl -g "run_tests, halt" -s tests/test_rules.pl
```

### การกำหนดค่าการสร้าง
```makefile
SWIPL    = swipl
TARGET   = solver
SOURCES  = src/main.pl src/rules.pl src/utils.pl

$(TARGET): $(SOURCES)
	$(SWIPL) -o $(TARGET) -g main -c $(SOURCES)

test:
	$(SWIPL) -g "run_tests, halt" -s tests/test_rules.pl

run:
	$(SWIPL) -s src/main.pl

clean:
	rm -f $(TARGET)

.PHONY: test run clean
```

---

## การทดสอบและการดีบัก
### การติดตามในตัว
```prolog
?- trace.
?- grandparent(tom, X).
[trace]  Call: (10) grandparent(tom, _1234)
[trace]  Call: (11) parent(tom, _1256)
[trace]  Exit: (11) parent(tom, bob)
[trace]  Exit: (10) grandparent(tom, ann)
X = ann.
?- notrace.

?- spy parent/2.
?- nospy parent/2.
```

### การทดสอบหน่วยด้วย PLUnit
```prolog
:- begin_tests(family).

test(father_basic) :-
    father(tom, bob),
    \+ father(liz, bob).

test(grandparent, set(X == [ann, pat])) :-
    findall(X, grandparent(tom, X), Xs),
    member(X, Xs).

test(list_length) :-
    my_length([], 0),
    my_length([a], 1),
    my_length([1,2,3,4], 4).

:- end_tests(family).
```

### รูปแบบการดีบักทั่วไป
| ปัญหา | อาการ | โซลูชั่น |
|---------|---------|----------|
| การเรียกซ้ำแบบไม่มีที่สิ้นสุด | สแต็กโอเวอร์โฟลว์ | ตรวจสอบกรณีฐาน เพิ่มเงื่อนไขการสิ้นสุด |
| ไม่มีวิธีแก้ปัญหา | แบบสอบถามส่งกลับค่าเท็จ | ตรวจสอบลำดับการสร้างอินสแตนซ์ของตัวแปร |
| วิธีแก้ปัญหามากเกินไป | รายการที่ซ้ำกันโดยไม่คาดคิด | เพิ่มการตัด (!) หรือใช้`setof`|
| การรวมไม่ถูกต้อง | ตัวแปรถูกผูกไว้ไม่ถูกต้อง | ใช้`=`เพื่อทดสอบ ตรวจสอบฟังก์ชัน arity |
| ปัญหาด้านประสิทธิภาพ | ดำเนินการช้า | เพิ่มการตัด; ใช้`table`; ตรวจสอบคะแนนตัวเลือก |
---

## การทำงานร่วมกัน
### อินเทอร์เฟซ C (FFI)
```c
/* fast_math.c */
#include <SWI-Prolog.h>
static foreign_t pl_fast_add(term_t A, term_t B, term_t Result) {
    long a, b;
    if (PL_get_long(A, &a) && PL_get_long(B, &b))
        return PL_unify_long(Result, a + b);
    return FALSE;
}
install_t install_fast_math() {
    PL_register_foreign("fast_add", 3, pl_fast_add, 0);
}
```

```prolog
:- load_foreign_library(fast_math).
```

### บูรณาการหลาม
```prolog
:- use_module(library(unix)).
call_python(Expression, Result) :-
    process_create(path(python3),
        ['-c', atom_concat('print(', Expression, Cmd))],
        [stdout(pipe(Out))]),
    read_line_to_codes(Out, Codes),
    close(Out), number_codes(Result, Codes).
```

---

## รูปแบบการออกแบบ
### รูปแบบ 1: ตัวสะสม (การเรียกซ้ำส่วนท้าย)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### รูปแบบ 2: เธรดสถานะ```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### รูปแบบ 3: สร้างและทดสอบ```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### รูปแบบ 4: รายการความแตกต่าง```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### การเพิ่มประสิทธิภาพการตัด
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### การเรียกซ้ำหาง
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### รายการตรวจสอบการเพิ่มประสิทธิภาพ
| เทคนิค | ผลกระทบ | คำอธิบาย |
|----------|--------|-------------|
| **การเรียกซ้ำหาง** | สูง | ใช้ตัวสะสมสำหรับพื้นที่สแต็กคงที่ |
| **ตัด (สีเขียว)** | สูง | กำจัดจุดตัวเลือกที่ไม่จำเป็น |
| **การประเมินแบบตาราง** | สูง | `:- table pred/N`บันทึกผลลัพธ์ |
| **การจัดทำดัชนี** | ปานกลาง | ใส่ข้อโต้แย้งที่แบ่งแยกก่อน |
| **รายการความแตกต่าง** | ปานกลาง | O(1) การต่อรายการ |
| **CLP(FD) มากกว่าการทดสอบการสร้าง** | สูงมาก | ใช้ข้อจำกัดแทนการใช้ brute-force |
---

## การปรับใช้และการใช้งานในโลกแห่งความเป็นจริง
### การปรับใช้แอปพลิเคชัน Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### แอปพลิเคชันในโลกแห่งความเป็นจริง
| โดเมน | วิธีใช้ Prolog | ตัวอย่าง |
|--------|-------------------|---------|
| **ระบบผู้เชี่ยวชาญ** | การวินิจฉัยทางการแพทย์ การตรวจจับข้อบกพร่อง | MYCIN, XCON |
| **NLP** | การแยกวิเคราะห์ไวยากรณ์ การวิเคราะห์ความหมาย | แชทบอท ระบบประกันคุณภาพ |
| **ประเภทการอนุมาน** | การตรวจสอบประเภทฮินด์ลีย์-มิลเนอร์ | ต้นแบบ Haskell/ML |
| **กำหนดการ** | การตั้งเวลาพนักงาน, ตารางเวลา | ตารางลูกเรือของสายการบิน |
| **การให้เหตุผลทางกฎหมาย** | การวิเคราะห์ทางกฎหมายตามกฎเกณฑ์ | การตรวจสอบการปฏิบัติตามข้อกำหนด |
| **การสอบถามฐานข้อมูล** | Datalog สำหรับการวิเคราะห์ข้อมูล | เครื่องยนต์ซูเฟล่ |
| **การยืนยัน** | การตรวจสอบโมเดล | การตรวจสอบฮาร์ดแวร์ |
| **ไอบีเอ็ม วัตสัน** | ความเข้าใจภาษาธรรมชาติ | อันตราย! ระบบ |
| **อีริคสัน** | การจัดการโทรคมนาคม | การตรวจสอบการกำหนดค่าเครือข่าย |
---

## เมื่อใดควรใช้ Prolog
| สถานการณ์ | ทำไมต้องเปิดเทอม | ทางเลือกที่ดีกว่า |
|----------|-----------|-------------------|
| การใช้เหตุผลตามกฎ | Prolog ถูกสร้างขึ้นเพื่อสิ่งนี้ | เอ็นจิ้นกฎแบบกำหนดเองใน Python/Java |
| ความพึงพอใจที่จำกัด | CLP(FD) มีความหรูหราและมีประสิทธิภาพ | ตัวแก้ปัญหา SAT หรือเครื่องมือสำหรับอินสแตนซ์ขนาดใหญ่ |
| การแยกวิเคราะห์ไวยากรณ์ / ภาษา | DCG (Definite Clause Grammars) เป็นภาษาท้องถิ่น | เครื่องกำเนิดพาร์เซอร์ (ANTLR, yacc) สำหรับการผลิต |
| ระบบผู้เชี่ยวชาญ | ความพอดีตามธรรมชาติ — ข้อเท็จจริง + กฎ = ระบบผู้เชี่ยวชาญ | กลไกกฎธุรกิจ (Drools) |
| การตั้งเวลา/ตารางเวลา | CLP แก้ปัญหาเหล่านี้ได้ดี | หรือ-เครื่องมือ OptaPlanner |
| พิมพ์วิจัยระบบ | การรวมกันเป็นรากฐาน | นำไปใช้ใน OCaml, Haskell, Rust |
| เว็บแอปพลิเคชั่น | ไม่เหมาะ | Python, Node.js, ไป |
| วิทยาศาสตร์ข้อมูล / ML | ไม่ใช่ระบบนิเวศ | หลาม, อาร์ |
| รหัสที่มีความสำคัญต่อประสิทธิภาพ | Prolog ช้าสำหรับการคำนวณ | C, C++, สนิม |
| การเขียนโปรแกรมเอนกประสงค์ | เป็นไปได้แต่น่าอึดอัด | Python, Go, Java |
---

## คำถามและคำตอบสังเคราะห์
### Q1: การรวม Prolog แตกต่างจากการมอบหมายในภาษาอื่นอย่างไร
**ตอบ:** การรวมเป็นการจับคู่รูปแบบแบบสองทิศทาง ไม่ใช่การกำหนด:
```prolog
% Unification (=) tries to make both sides equal
X = 5.              % X is now 5
5 = X.              % same thing — X is 5
f(X, b) = f(a, Y).  % X = a, Y = b

% Once bound, a variable cannot change (in the same scope)
X = 1, X = 2.      % FAILS — X is already 1

% Anonymous variable _ matches anything
f(a, _) = f(a, b).  % true — _ matches b
```

### Q2: การย้อนรอยทำงานอย่างไรใน Prolog
**ตอบ:** เมื่อเป้าหมายล้มเหลว Prolog จะย้อนกลับไปที่จุดตัวเลือกสุดท้ายและลองทางเลือกถัดไป:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: ฉันจะทำงานกับรายการใน Prolog ได้อย่างไร
**ก:** รายการใช้การจับคู่รูปแบบหัว/ท้าย:
```prolog
% Pattern matching on lists
[X|Xs] = [1, 2, 3].  % X = 1, Xs = [2, 3]

% Common list predicates
my_length([], 0).
my_length([_|T], N) :- my_length(T, N1), N is N1 + 1.

my_append([], L, L).
my_append([H|T], L, [H|R]) :- my_append(T, L, R).

my_member(X, [X|_]).
my_member(X, [_|T]) :- my_member(X, T).
```

### Q4: เมื่อใดที่ฉันควรใช้ Prolog แทนภาษาอื่น?
**A:** Prolog เก่งที่:
- ความพึงพอใจที่จำกัด (การกำหนดเวลา ปริศนา)
- ระบบตามกฎ (ระบบผู้เชี่ยวชาญ การตรวจสอบ)
- กราฟ/การสำรวจต้นไม้
- การประมวลผลภาษาธรรมชาติ
- การคำนวณเชิงสัญลักษณ์
- ปัญหาใด ๆ ที่แสดงออกมาเป็นความสัมพันธ์เชิงตรรกะ
### Q5: อะไรคือข้อผิดพลาดทั่วไปใน Prolog?
**ก:** ประเด็นสำคัญ:
- การเรียกซ้ำแบบไม่มีที่สิ้นสุด - ใส่กรณีพื้นฐานไว้ก่อนเสมอ
- การย้อนรอยโดยไม่ได้ตั้งใจ — ใช้การตัด`!`หรือ`once/1`
- เกิดการตรวจสอบ —`X = f(X)`วนซ้ำตามค่าเริ่มต้น (ใช้`unify_with_occurs_check`)
- การตัดสีเขียว (การเพิ่มประสิทธิภาพ) เทียบกับการตัดสีแดง (เปลี่ยนความหมาย) — ชอบสีเขียว
---

## การแก้ปัญหาลูกโซ่แห่งความคิด
### ปัญหาที่ 1: การไขปริศนา N-Queens
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
วางราชินี N บนกระดานหมากรุก NxN เพื่อไม่ให้ราชินีสองคนโจมตีกัน
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้การสร้างตามข้อจำกัด: วางราชินีทีละคอลัมน์ ตรวจสอบความปลอดภัย
**ขั้นตอนที่ 3: นำไปใช้**```prolog
n_queens(N, Qs) :-
    length(Qs, N),
    numlist(1, N, Rows),
    permutation(Rows, Qs),
    safe_queens(Qs).

safe_queens([]).
safe_queens([Q|Qs]) :-
    no_attack(Q, Qs, 1),
    safe_queens(Qs).

no_attack(_, [], _).
no_attack(Q, [Q1|Qs], D) :-
    Q =\= Q1,
    abs(Q - Q1) =\= D,
    D1 is D + 1,
    no_attack(Q, Qs, D1).
```

**ขั้นตอนที่ 4: ยืนยัน**
`?- n_queens(8, Qs).`ควรค้นหาวิธีแก้ปัญหา 92 รายการ
### ปัญหาที่ 2: การสร้างระบบผู้เชี่ยวชาญอย่างง่าย
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
วินิจฉัยปัญหารถตามอาการ
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้กฎ Prolog เพื่อเข้ารหัสความรู้ในการวินิจฉัย
**ขั้นตอนที่ 3: นำไปใช้**```prolog
% Facts about symptoms
symptom(car_wont_start).
symptom(clicking_sound).

% Rules
diagnosis(battery_dead) :-
    symptom(car_wont_start),
    symptom(clicking_sound).

diagnosis(starter_motor) :-
    symptom(car_wont_start),
    symptom(single_click),
    \+ symptom(clicking_sound).

diagnosis(out_of_fuel) :-
    symptom(engine_cranks),
    symptom(engine_wont_catch).

% Query
?- diagnosis(X).
```

**ขั้นตอนที่ 4: ขยาย**
เพิ่มคะแนนความมั่นใจ ถามอาการของผู้ใช้แบบโต้ตอบ และวินิจฉัยแบบต่อเนื่อง
---

## สรุป
Prolog ไม่เหมือนกับภาษาโปรแกรมอื่นๆ แทนที่จะเขียนคำแนะนำทีละขั้นตอน คุณจะอธิบายความสัมพันธ์และข้อจำกัด และกลไกจะค้นหาวิธีแก้ไขผ่านการอนุมานเชิงตรรกะ สิ่งนี้ทำให้ Prolog เหมาะสำหรับปัญหาที่น่าอึดอัดใจหรือละเอียดในภาษาที่จำเป็น เช่น ระบบผู้เชี่ยวชาญ การกำหนดเวลา การแยกวิเคราะห์ไวยากรณ์ ความพึงพอใจที่มีข้อจำกัด และอะไรก็ตามที่เกี่ยวข้องกับกฎเชิงตรรกะ โปรแกรมเมอร์ส่วนใหญ่จะไม่ใช้ Prolog ในการผลิต แต่การเรียนรู้มันจะช่วยให้คุณขยายความคิดเกี่ยวกับการเขียนโปรแกรมได้ การรวม การย้อนรอย และการระบุปัญหาที่ประกาศเป็นแนวคิดที่มีอิทธิพลต่อการออกแบบภาษา การวิจัย AI และแม้แต่การเพิ่มประสิทธิภาพการสืบค้นฐานข้อมูล
### เปรียบเทียบเครื่องยนต์ Prolog
| คุณสมบัติ | SWI-คำนำ | GNU เปิดฉาก | เอก อารัมภบท |
|---------|-----------|------------|------------|
| **ใบอนุญาต** | BSD (โอเพ่นซอร์ส) | GPL (โอเพ่นซอร์ส) | BSD (โอเพ่นซอร์ส) |
| **แพลตฟอร์ม** | วินโดวส์, ลินุกซ์, macOS | วินโดวส์, ลินุกซ์, macOS | จาวาสคริปต์ (เบราว์เซอร์) |
| **ซีแอลพี(FD)** | ห้องสมุดในตัว | ในตัว | ไม่สามารถใช้ได้ |
| **รองรับ DCG** | เต็ม | เต็ม | จำกัด |
| **การจัดโต๊ะ** | ใช่ | ไม่ | ไม่ |
| **FFI (สาย C)** | ใช่ | ใช่ | ผ่านจาวาสคริปต์ |
| **ระบบเครือข่าย** | HTTP, TCP, TLS | TCP | ผ่านจาวาสคริปต์ |
| **มัลติเธรด** | ใช่ | ไม่ | ไม่ |
| **ผู้จัดการแพ็คเกจ** | `pack_install/1`| ไม่มี | เวลา 12.00 น. |
| **ดีที่สุดสำหรับ** | การผลิต การวิจัย | การแก้ไขข้อจำกัด | เว็บแอป การศึกษา |
### เว็บแอปพลิเคชันพร้อม Pengines
```prolog
% SWI-Prolog Pengines — server-side Prolog accessible from web
:- use_module(library(http/http_server)).
:- use_module(library(pengines)).
:- use_module(library(pengines/apps/sandbox)).

:- http_handler(root(.), http_reply_from_files(web, []), [prefix]).
:- http_handler(root(pengines), pengine_application(sandbox)).

:- server(8080).

% Client-side JavaScript calls Prolog predicates via HTTP
% <script>
% new Pengine({
%   server: "/pengines",
%   ask: "grandparent(tom, X)",
%   ondata: function(data) { console.log(data); }
% });
% </script>
```

### การเขียนโปรแกรมเมตาด้วยการยืนยัน / ถอนกลับ
```prolog
% Dynamic knowledge base modification
:- dynamic student/2.

% Add facts at runtime
add_student(Name, Grade) :-
    assert(student(Name, Grade)).

% Remove facts
remove_student(Name) :-
    retract(student(Name, _)).

% Query and modify
promote_students :-
    forall(
        student(Name, Grade),
        (   Grade < 12,
            NewGrade is Grade + 1,
            retract(student(Name, Grade)),
            assert(student(Name, NewGrade))
        )
    ).

% findall + assert pattern (batch operations)
copy_passing_students :-
    findall(Name, (student(Name, Grade), Grade >= 50), PassList),
    forall(member(Name, PassList),
        assert(passed(Name))).
```
