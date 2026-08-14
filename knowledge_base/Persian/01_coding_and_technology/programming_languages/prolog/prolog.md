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

# پرولوگ
Prolog (برنامه نویسی در منطق) یک زبان برنامه نویسی منطقی است که در سال 1972 توسط آلن کولمراور و فیلیپ روسل ایجاد شد. برخلاف هر زبان دیگری در این لیست، Prolog به رایانه نمی‌گوید *چگونه* یک مسئله را حل کند - شما اعلام می‌کنید که *چه چیزی درست است (حقایق و قوانین) و موتور استنتاج Prolog پاسخ را از طریق استنتاج منطقی می‌یابد.
Prolog زبان انتخابی برای سیستم های خبره، پردازش زبان طبیعی و تحقیقات هوش مصنوعی در دهه 1980 بود. این پروژه سیستم کامپیوتری نسل پنجم ژاپن را تقویت کرد و در واتسون IBM برای درک زبان طبیعی استفاده شد. امروزه از Prolog در حل محدودیت، زمان‌بندی، استنتاج نوع، استدلال قانونی و هر جایی که مشکلات به طور طبیعی به صورت روابط منطقی بیان می‌شوند استفاده می‌شود.
**برنامه‌نویسی منطقی محدودیت (CLP)** Prolog را با حل‌کننده‌های محدودیت برای زمان‌بندی، مسیریابی و تخصیص منابع گسترش می‌دهد - مشکلاتی که در زبان‌های ضروری بسیار دشوار هستند.
---

## چرا Prolog مهم است
- **برنامه نویسی اعلانی**: آنچه درست است را توصیف کنید، نه نحوه محاسبه آن. موتور کار را انجام می دهد.
- **تطبیق و یکسان سازی الگو**: الگوریتم یکسان سازی Prolog از تطبیق الگو در زبان های دیگر قدرتمندتر است.
- **جستجوی بازگشتی **: به طور خودکار تمام راه حل های ممکن را بررسی می کند. هیچ الگوریتم جستجوی دستی مورد نیاز نیست.
- **طبیعی برای مشکلات منطقی**: سیستم های خبره، موتورهای قانون، چک کننده های تایپ، تجزیه کننده های گرامری - این ها مستقیماً به Prolog نگاشت می شوند.
- **حل محدودیت**: CLP(FD) زمان بندی، تخصیص و مسائل ترکیبی را به زیبایی حل می کند.
- **تفکر متفاوت**: یادگیری Prolog نحوه رویکرد شما به حل مسئله را تغییر می دهد - شما شروع به فکر کردن در روابط و محدودیت ها می کنید.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **پارادایم بسیار متفاوت** | بدون متغیر (فقط اتصالات)، بدون حلقه، بدون تخصیص | در روابط و بازگشت فکر کنید، نه تغییرات حالت |
| **عملکرد** | کندی برای محاسبات عددی و داده های بزرگ | استفاده برای استدلال؛ محاسبات را به C/زبان های دیگر واگذار کنید |
| **مشکل اشکال زدایی** | ردیابی عقب نشینی و شکست های یکپارچه سازی سخت است | از ابزارهای ردیابی/اشکال‌زدایی استفاده کنید. گزاره های قطعی بنویسید |
| **اپراتور کات (!)** | برای کارایی لازم است اما خلوص منطقی را می شکند | در صورت امکان از ارزیابی if-then-else یا جدولی استفاده کنید |
| **اکوسیستم محدود** | تعداد کمی کتابخانه، چارچوب یا منابع جامعه | SWI-Prolog کامل ترین پیاده سازی |
| **برای برنامه های عمومی نیست** | وب، موبایل، رابط کاربری گرافیکی - نه قدرت Prolog | استفاده به عنوان موتور استدلال در پشت برنامه وب |
---

## اصول نحو
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

## نحو و الگوهای پیشرفته
### Unification Deep Dive
یکپارچه سازی مکانیسم اصلی Prolog است - پرولوگ چگونه شرایط را مطابقت می دهد و متغیرها را متصل می کند.
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

### عقبگرد و امتیاز انتخاب
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

### گرامرهای بند معین (DCG)
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

### برنامه نویسی منطقی محدودیت (CLP)
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

## معماری و طراحی سیستم
### پارادایم برنامه نویسی منطقی
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

### ساختار پروژه معمولی
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

### سیستم ماژول
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

## پیکربندی پروژه و سیستم ساخت
### پیکربندی SWI-Prolog
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

### اجرای برنامه های Prolog
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

### پیکربندی ساخت
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

## تست و اشکال زدایی
### ردیابی داخلی
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

### تست واحد با PLUnit
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

### الگوهای رایج اشکال زدایی
| مشکل | علامت | راه حل |
|---------|---------|----------|
| بازگشت بی نهایت | سرریز پشته | چک کردن مورد پایه؛ اضافه کردن شرط خاتمه |
| بدون راه حل | پرس و جو false | سفارش نمونه سازی متغیر را بررسی کنید |
| راه حل های بسیار زیاد | موارد تکراری غیرمنتظره | برش (!) را اضافه کنید یا از`setof`|
| یکسان سازی اشتباه | متغیرها به اشتباه قید شده اند | برای تست از`=`استفاده کنید. بررسی تابع آریتی |
| موضوع عملکرد | اجرای آهسته | اضافه کردن برش؛ از`table`استفاده کنید. بررسی نقاط انتخاب |
---

## قابلیت همکاری
### رابط C (FFI)
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

### ادغام پایتون
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

## الگوهای طراحی
### الگوی 1: انباشته (بازگشت دم)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### الگوی 2: حالت رشته```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### الگوی 3: تولید و آزمایش```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### الگوی 4: لیست های تفاوت```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## عملکرد و بهینه سازی
### برش بهینه سازی
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### بازگشت دم
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### چک لیست بهینه سازی
| تکنیک | تاثیر | توضیحات |
|-----------|--------|-------------|
| ** بازگشت دم ** | بالا | استفاده از انباشته برای فضای پشته ثابت |
| **برش (سبز)** | بالا | حذف نقاط انتخاب غیر ضروری |
| **ارزیابی جدولی** | بالا | `:- table pred/N`نتایج را حفظ می کند |
| **نمایه سازی** | متوسط ​​| بحث تمایز را در درجه اول قرار دهید |
| **لیست های تفاوت** | متوسط ​​| O(1) الحاق لیست |
| **CLP(FD) بیش از تولید-تست ** | خیلی بالا | استفاده از محدودیت ها به جای brute-force |
---

## استقرار و استفاده در دنیای واقعی
### استقرار برنامه های Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### برنامه های کاربردی در دنیای واقعی
| دامنه | نحوه استفاده از Prolog | مثال |
|--------|------------------|---------|
| **سیستم های خبره** | تشخیص پزشکی، تشخیص عیب | MYCIN، XCON |
| **NLP** | تجزیه گرامر، تحلیل معنایی | چت بات ها، سیستم های QA |
| **استنتاج نوع** | بررسی نوع هیندلی میلنر | نمونه های اولیه Haskell/ML |
| **زمان بندی** | زمان بندی کارمندان، جدول زمانی | برنامه ریزی خدمه هواپیمایی |
| **استدلال حقوقی** | تحلیل حقوقی مبتنی بر قانون | بررسی انطباق |
| **پرس و جو از پایگاه داده** | دیتالوگ برای تجزیه و تحلیل داده ها | موتور سوفله |
| **تأیید ** | بررسی مدل | تایید سخت افزار |
| **IBM Watson** | درک زبان طبیعی | خطر! سیستم |
| **اریکسون** | مدیریت مخابرات | اعتبار سنجی پیکربندی شبکه |
---

## چه زمانی از Prolog استفاده کنیم
| سناریو | چرا Prolog | جایگزین بهتر |
|----------|----------|------------------|
| استدلال مبتنی بر قانون | Prolog برای این ساخته شده است | موتورهای قوانین سفارشی در پایتون/جاوا |
| رضایت محدودیت | CLP(FD) ظریف و کارآمد است | حل کننده های SAT، OR-Tools برای نمونه های بزرگ |
| گرامر / تجزیه زبان | DCG (گرامرهای بند معین) بومی | ژنراتورهای تجزیه کننده (ANTLR, yacc) برای تولید |
| سیستم های خبره | تناسب طبیعی - حقایق + قوانین = سیستم خبره | موتورهای قانون تجارت (Drools) |
| برنامه ریزی / جدول زمانی | CLP اینها را به خوبی حل می کند | OR-Tools، OptaPlanner |
| تحقیق سیستم نوع | اتحاد پایه است | پیاده سازی در OCaml, Haskell, Rust |
| برنامه های کاربردی وب | مناسب نیست | Python، Node.js، Go |
| علم داده / ML | نه اکوسیستم | پایتون، R |
| کد حیاتی عملکرد | Prolog برای محاسبه کند است | C, C++, Rust |
| برنامه نویسی همه منظوره | ممکن اما ناجور | پایتون، برو، جاوا |
---

## پرسش و پاسخ مصنوعی
### Q1: یکسان سازی Prolog چه تفاوتی با انتساب در زبان های دیگر دارد؟
**A:** یکسان سازی تطبیق الگوی دو طرفه است، نه تخصیص:
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

### Q2: چگونه عقبگرد در Prolog کار می کند؟
**A:** هنگامی که یک هدف شکست می خورد، Prolog به آخرین نقطه انتخاب برمی گردد و جایگزین بعدی را امتحان می کند:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: چگونه با لیست ها در Prolog کار کنم؟
**A:** لیست ها از تطبیق الگوی سر/دم استفاده می کنند:
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

### Q4: چه زمانی باید از Prolog به جای زبان های دیگر استفاده کنم؟
**A:** Prolog در:
- رضایت از محدودیت (برنامه ریزی، پازل)
- سیستم های مبتنی بر قوانین (سیستم های خبره، اعتبارسنجی)
- پیمایش نمودار/درخت
- پردازش زبان طبیعی
- محاسبات نمادین
- هر مشکلی که به صورت روابط منطقی قابل بیان باشد
### Q5: مشکلات رایج در Prolog چیست؟
**A:** مسائل کلیدی:
- بازگشت بی نهایت - همیشه مورد پایه را در اولویت قرار دهید
- عقبگرد ناخواسته - از برش`!`یا`once/1`استفاده کنید 
- بررسی رخ می دهد -`X = f(X)`به طور پیش فرض حلقه می شود (از`unify_with_occurs_check`استفاده کنید)
- برش های سبز (بهینه سازی) در مقابل برش های قرمز (تغییر معنی) - سبز را ترجیح دهید
---

## حل مسئله زنجیره ای از فکر
### مسئله 1: حل معمای N-Queens
**مرحله 1: مشکل را درک کنید**
N ملکه را روی صفحه شطرنج NxN قرار دهید تا دو ملکه به یکدیگر حمله نکنند.
**مرحله 2: رویکرد را شناسایی کنید**
از تولید مبتنی بر محدودیت استفاده کنید: ملکه ها را ستون به ستون قرار دهید و ایمنی را بررسی کنید.
**مرحله 3: پیاده سازی **```prolog
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

**مرحله 4: تایید **
`?- n_queens(8, Qs).`باید 92 راه حل پیدا کند.
### مسئله 2: ساختن یک سیستم خبره ساده
**مرحله 1: مشکل را درک کنید**
مشکلات خودرو را بر اساس علائم تشخیص دهید.
**مرحله 2: رویکرد را شناسایی کنید**
از قوانین Prolog برای رمزگذاری دانش تشخیصی استفاده کنید.
**مرحله 3: پیاده سازی **```prolog
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

**مرحله 4: تمدید**
امتیازهای اطمینان را اضافه کنید، علائم را به صورت تعاملی از کاربر بخواهید، و تشخیص های زنجیره ای را انجام دهید.
---

## خلاصه
Prolog شبیه هیچ زبان برنامه نویسی دیگری نیست. به جای نوشتن دستورالعمل های گام به گام، شما روابط و محدودیت ها را توصیف می کنید - و موتور از طریق استنتاج منطقی به دنبال راه حل می گردد. این امر Prolog را برای مسائلی که در زبان‌های ضروری نامناسب یا پرمخاطب هستند ایده‌آل می‌کند: سیستم‌های خبره، زمان‌بندی، تجزیه دستور زبان، رضایت محدودیت‌ها و هر چیزی که شامل قوانین منطقی باشد. اکثر برنامه نویسان هرگز از Prolog در تولید استفاده نمی کنند، اما یادگیری آن تفکر شما را در مورد برنامه نویسی گسترش می دهد. یکپارچه سازی، عقب نشینی و مشخص کردن مشکل اعلانی مفاهیمی هستند که بر طراحی زبان، تحقیقات هوش مصنوعی و حتی بهینه سازی پرس و جو پایگاه داده تأثیر می گذارند.
### مقایسه موتورهای Prolog
| ویژگی | SWI-Prolog | پرولوگ گنو | تاو پرولوگ |
|---------|-----------|-----------|------------|
| **مجوز** | BSD (متن باز) | GPL (متن باز) | BSD (متن باز) |
| **پلتفرم** | ویندوز، لینوکس، macOS | ویندوز، لینوکس، macOS | جاوا اسکریپت (مرورگر) |
| **CLP(FD)** | کتابخانه داخلی | داخلی | در دسترس نیست |
| **پشتیبانی از DCG** | کامل | کامل | محدود |
| **جدول** | بله | نه | نه |
| **FFI (C calls)** | بله | بله | از طریق جاوا اسکریپت |
| **شبکه** | HTTP، TCP، TLS | TCP | از طریق جاوا اسکریپت |
| **چند نخی** | بله | نه | نه |
| **مدیر بسته** | `pack_install/1`| هیچکدام | npm |
| **بهترین برای** | تولید، تحقیق | حل محدودیت | برنامه های وب، آموزش |
### برنامه های وب با پنگین
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

### فرابرنامه نویسی با اظهار / پس گرفتن
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
