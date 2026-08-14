---
# Metadata
title: "Prolog"
description: "Comprehensive reference for the Prolog programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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
#پرولوگ
پرولوگ (منطق میں پروگرامنگ) ایک منطقی پروگرامنگ زبان ہے جسے 1972 میں ایلین کولمراؤر اور فلپ روسل نے بنایا تھا۔ اس فہرست میں موجود ہر دوسری زبان کے برعکس، Prolog کمپیوٹر کو یہ نہیں بتاتا ہے کہ *کس طرح* کسی مسئلے کو حل کیا جائے — آپ اعلان کرتے ہیں کہ *کیا* سچ ہے (حقائق اور اصول)، اور پرولوگ کا انفرنس انجن منطقی کٹوتی کے ذریعے جواب کا پتہ لگاتا ہے۔
1980 کی دہائی میں ماہرین کے نظام، قدرتی زبان کی پروسیسنگ، اور AI تحقیق کے لیے پرولوگ پسند کی زبان تھی۔ اس نے جاپان کے ففتھ جنریشن کمپیوٹر سسٹم پروجیکٹ کو تقویت بخشی اور اسے قدرتی زبان کی سمجھ کے لیے IBM کے واٹسن میں استعمال کیا گیا۔ آج، Prolog کا استعمال رکاوٹوں کو حل کرنے، شیڈولنگ، قسم کا اندازہ، قانونی استدلال، اور کہیں بھی مسائل کو قدرتی طور پر منطقی تعلقات کے طور پر ظاہر کیا جاتا ہے۔
**کنسٹرائنٹ لاجک پروگرامنگ (سی ایل پی)** شیڈولنگ، روٹنگ، اور ریسورس ایلوکیشن کے لیے رکاوٹوں کو حل کرنے والے پرولوگ کو بڑھاتا ہے — ایسے مسائل جو ضروری زبانوں میں انتہائی مشکل ہوتے ہیں۔
---

## پرولوگ کیوں اہمیت رکھتا ہے۔
- **اعلاناتی پروگرامنگ**: بیان کریں کہ کیا سچ ہے، نہ کہ اس کی گنتی کیسے کی جائے۔ انجن کام کرتا ہے۔
- **پیٹرن میچنگ اور یونیفیکیشن**: پرولوگ کا یونیفکیشن الگورتھم دوسری زبانوں میں پیٹرن میچنگ سے زیادہ طاقتور ہے۔
- **بیک ٹریکنگ سرچ**: خود بخود تمام ممکنہ حل تلاش کرتا ہے۔ دستی تلاش کے الگورتھم کی ضرورت نہیں ہے۔
- **منطق کے مسائل کے لیے قدرتی**: ماہر نظام، اصول کے انجن، ٹائپ چیکرز، گرائمر پارسرز — یہ نقشہ براہ راست پرولوگ پر۔
- ** رکاوٹوں کو حل کرنا**: CLP(FD) شیڈولنگ، مختص اور مشترکہ مسائل کو خوبصورتی سے حل کرتا ہے۔
- **مختلف سوچ**: لرننگ پرولوگ تبدیل کرتا ہے کہ آپ کس طرح مسئلہ حل کرنے تک پہنچتے ہیں — آپ تعلقات اور رکاوٹوں میں سوچنا شروع کر دیتے ہیں۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **بہت مختلف نمونہ** | کوئی متغیر نہیں (صرف بائنڈنگز)، کوئی لوپ، کوئی اسائنمنٹ نہیں | تعلقات اور تکرار میں سوچیں، ریاست کی تبدیلیوں سے نہیں۔
| **کارکردگی** | عددی حساب اور بڑے ڈیٹا کے لیے سست | استدلال کے لیے استعمال کریں؛ C/دیگر زبانوں کو شماری تفویض کریں |
| **ڈیبگ کرنے میں دشواری** | بیک ٹریکنگ اور یونیفیکیشن کی ناکامیوں کا سراغ لگانا مشکل ہے | ٹریس/ڈیبگ ٹولز استعمال کریں۔ متعصبانہ پیش گوئیاں لکھیں |
| **کٹ آپریٹر (!)** | کارکردگی کی ضرورت ہے لیکن منطقی پاکیزگی کو توڑتا ہے | اگر ممکن ہو تو استعمال کریں یا پھر ٹیبل شدہ تشخیص |
| **محدود ماحولیاتی نظام** | کچھ لائبریریاں، فریم ورک، یا کمیونٹی وسائل | SWI-Prolog سب سے مکمل نفاذ ہے |
| **عام ایپس کے لیے نہیں** | ویب، موبائل، جی یو آئی - پرولوگ کی طاقت نہیں | ویب ایپ کے پیچھے استدلال کے انجن کے طور پر استعمال کریں۔
---

## نحوی بنیادی باتیں
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

## اعلی درجے کی نحو اور نمونے۔
### یونیفیکیشن گہرا غوطہ
یونیفیکیشن پرولوگ کا بنیادی طریقہ کار ہے - یہ اس طرح ہے کہ پرولوگ شرائط کو "مماثل" کرتا ہے اور متغیرات کو باندھتا ہے۔
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

### بیک ٹریکنگ اور چوائس پوائنٹس
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

### قطعی شق گرامر (DCGs)
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

### کنسٹرنٹ لاجک پروگرامنگ (CLP)
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

## آرکیٹیکچر اور سسٹم ڈیزائن
### لاجک پروگرامنگ پیراڈائم
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

### پراجیکٹ کا مخصوص ڈھانچہ
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

### ماڈیول سسٹم
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### SWI-Prolog کنفیگریشن
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

### پراولوگ پروگرام چلا رہے ہیں۔
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

### کنفیگریشن بنائیں
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

## ٹیسٹنگ اور ڈیبگنگ
### بلٹ ان ٹریسنگ
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

### PLUnit کے ساتھ یونٹ ٹیسٹنگ
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

### عام ڈیبگنگ پیٹرنز
| مسئلہ | علامت | حل |
|---------|---------|---------|
| لامحدود تکرار | اسٹیک اوور فلو | بیس کیس چیک کریں؛ برطرفی کی شرط شامل کریں |
| کوئی حل نہیں | سوال غلط لوٹاتا ہے | متغیر انسٹیٹیئشن آرڈر چیک کریں |
| بہت سارے حل | غیر متوقع ڈپلیکیٹس | کٹ (!) شامل کریں یا`setof`| استعمال کریں۔
| غلط اتحاد | متغیرات غلط طریقے سے پابند | ٹیسٹ کرنے کے لیے`=`استعمال کریں۔ فنیکٹر ارٹی چیک کریں |
| کارکردگی کا مسئلہ | آہستہ عملدرآمد | کٹ شامل کریں؛`table`استعمال کریں؛ انتخاب کے پوائنٹس کی جانچ پڑتال کریں |
---

## انٹرآپریبلٹی
### C انٹرفیس (FFI)
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

### ازگر کا انٹیگریشن
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

## ڈیزائن پیٹرن
### پیٹرن 1: جمع کرنے والا (دم کی تکرار)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### پیٹرن 2: اسٹیٹ تھریڈنگ```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### پیٹرن 3: بنائیں اور ٹیسٹ کریں۔```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### پیٹرن 4: فرق کی فہرستیں۔```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## کارکردگی اور اصلاح
### کٹ آپٹیمائزیشن
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### دم کی تکرار
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### آپٹیمائزیشن چیک لسٹ
| تکنیک | اثر | تفصیل |
|------------|---------|------------|
| **دم کی تکرار** | ہائی | مستقل اسٹیک اسپیس کے لیے جمع کرنے والے استعمال کریں۔
| **کٹ (سبز)** | ہائی | غیر ضروری انتخابی نکات کو ختم کریں |
| **ٹیبل شدہ تشخیص** | ہائی | `:- table pred/N`نتائج کو یاد کرتا ہے |
| **انڈیکسنگ** | میڈیم | امتیازی دلیل کو پہلے رکھیں |
| **فرق کی فہرستیں** | میڈیم | O(1) فہرست کا مجموعہ |
| **CLP(FD) اوور جنریٹ ٹیسٹ** | بہت اعلیٰ | brute-force کے بجائے رکاوٹوں کا استعمال کریں |
---

## تعیناتی اور حقیقی دنیا کا استعمال
### پرولوگ ایپلیکیشنز کو تعینات کرنا
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### حقیقی دنیا کی ایپلی کیشنز
| ڈومین | Prolog کیسے استعمال کیا جاتا ہے | مثال |
|---------|-------------------|---------|
| **ماہر نظام** | طبی تشخیص، غلطی کا پتہ لگانا | MYCIN, XCON |
| **NLP** | گرائمر پارسنگ، سیمنٹک تجزیہ | چیٹ بوٹس، کیو اے سسٹمز |
| **قسم کا اندازہ** | Hindley-Milner قسم کی جانچ پڑتال | ہاسکل/ایم ایل پروٹو ٹائپس |
| **شیڈیولنگ** | ملازمین کا شیڈولنگ، ٹائم ٹیبلنگ | ایئر لائن کے عملے کا شیڈولنگ |
| **قانونی استدلال** | اصول پر مبنی قانونی تجزیہ | تعمیل کی جانچ پڑتال |
| **ڈیٹا بیس استفسار** | ڈیٹا کے تجزیہ کے لیے ڈیٹالاگ | سوفل انجن |
| **تصدیق** | ماڈل چیکنگ | ہارڈ ویئر کی تصدیق |
| **IBM واٹسن** | فطری زبان کی تفہیم | خطرہ! نظام |
| **ایرکسن** | ٹیلی کام مینجمنٹ | نیٹ ورک کی تشکیل کی توثیق |
---

## پرولوگ کب استعمال کریں۔
| منظر نامہ | کیوں Prolog | بہتر متبادل |
|------------|------------|-------------------|
| اصول پر مبنی استدلال | Prolog اس کے لیے بنایا گیا ہے | Python/Java میں اپنی مرضی کے اصول کے انجن |
| پابندی اطمینان | CLP(FD) خوبصورت اور موثر ہے | بڑی مثالوں کے لیے SAT حل کرنے والے، یا ٹولز |
| گرامر / زبان کی تجزیہ | DCG (Definite Clause Grammars) مقامی ہیں | پیداوار کے لیے پارسر جنریٹرز (ANTLR، yacc) |
| ماہر نظام | قدرتی فٹ - حقائق + قواعد = ماہر نظام | کاروباری اصول کے انجن (ڈرولز) |
| شیڈولنگ / ٹائم ٹیبلنگ | CLP ان کو اچھی طرح حل کرتا ہے | OR-Tools, OptaPlanner |
| قسم کے نظام کی تحقیق | اتحاد کی بنیاد ہے | OCaml، Haskell، Rust میں لاگو کریں |
| ویب ایپلیکیشنز | مناسب نہیں | Python, Node.js, Go |
| ڈیٹا سائنس / ایم ایل | ماحولیاتی نظام نہیں | ازگر، آر |
| کارکردگی کا اہم کوڈ | پرولوگ حساب کے لیے سست ہے | C, C++, Rust |
| عام مقصد کی پروگرامنگ | ممکن لیکن عجیب | ازگر، گو، جاوا |
---

## مصنوعی سوال و جواب
### Q1: Prolog کا یونیفیکیشن دوسری زبانوں میں تفویض سے کیسے مختلف ہے؟
**A:** اتحاد دو طرفہ پیٹرن کی مماثلت ہے، تفویض نہیں:
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

### Q2: Prolog میں بیک ٹریکنگ کیسے کام کرتی ہے؟
**A:** جب کوئی مقصد ناکام ہو جاتا ہے، تو Prolog آخری انتخاب کے مقام پر پیچھے ہٹ جاتا ہے اور اگلے متبادل کو آزماتا ہے:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: میں Prolog میں فہرستوں کے ساتھ کیسے کام کروں؟
**A:** فہرستیں ہیڈ/ٹیل پیٹرن کی مماثلت کا استعمال کرتی ہیں:
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

### Q4: مجھے دوسری زبانوں کے بجائے Prolog کب استعمال کرنا چاہیے؟
**A:** پرولوگ اس پر سبقت لے جاتا ہے:
- رکاوٹ اطمینان (شیڈولنگ، پہیلیاں)
- اصول پر مبنی نظام (ماہر نظام، توثیق)
- گراف/درخت کا راستہ
- قدرتی زبان کی پروسیسنگ
- علامتی حساب کتاب
- منطقی تعلقات کے طور پر ظاہر ہونے والا کوئی بھی مسئلہ
### Q5: پرولوگ میں عام خرابیاں کیا ہیں؟
**A:** اہم مسائل:
- لامحدود تکرار - ہمیشہ بنیادی کیس کو پہلے رکھیں
- غیر ارادی بیک ٹریکنگ - کٹ`!`یا`once/1`کا استعمال کریں 
- ہوتا ہے چیک —`X = f(X)`بذریعہ ڈیفالٹ لوپس (`unify_with_occurs_check` استعمال کریں)
- گرین کٹس (اصلاح) بمقابلہ ریڈ کٹس (معنی تبدیل کریں) - سبز کو ترجیح دیں۔
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: N-Queens پہیلی کو حل کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
N رانیوں کو NxN بساط پر رکھیں تاکہ کوئی دو ملکہیں ایک دوسرے پر حملہ نہ کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
رکاوٹ پر مبنی نسل کا استعمال کریں: کوئینز کالم کو کالم کے حساب سے رکھیں، حفاظت کی جانچ کریں۔
**مرحلہ 3: نافذ کریں**```prolog
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

**مرحلہ 4: تصدیق کریں**
`?- n_queens(8, Qs).`کو 92 حل تلاش کرنے چاہئیں۔
### مسئلہ 2: ایک سادہ ماہرانہ نظام بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
علامات کی بنیاد پر کار کے مسائل کی تشخیص کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
تشخیصی علم کو انکوڈ کرنے کے لیے Prolog اصول استعمال کریں۔
**مرحلہ 3: نافذ کریں**```prolog
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

**مرحلہ 4: توسیع کریں**
اعتماد کے اسکورز شامل کریں، صارف سے انٹرایکٹو علامات کے لیے پوچھیں، اور سلسلہ کی تشخیص کریں۔
---

## خلاصہ
Prolog کسی بھی دوسری پروگرامنگ زبان کے برعکس ہے۔ مرحلہ وار ہدایات لکھنے کے بجائے، آپ رشتوں اور رکاوٹوں کو بیان کرتے ہیں — اور انجن منطقی اندازہ کے ذریعے حل تلاش کرتا ہے۔ یہ Prolog کو ان مسائل کے لیے مثالی بناتا ہے جو ضروری زبانوں میں عجیب و غریب ہیں: ماہر نظام، نظام الاوقات، گرامر پارسنگ، رکاوٹ اطمینان، اور منطقی اصولوں پر مشتمل کوئی بھی چیز۔ زیادہ تر پروگرامرز کبھی بھی پروڈکشن میں پرولوگ کا استعمال نہیں کریں گے، لیکن اسے سیکھنا آپ کی سوچ کو بڑھاتا ہے کہ پروگرامنگ کیا ہو سکتی ہے۔ یونیفیکیشن، بیک ٹریکنگ، اور اعلاناتی مسئلہ کی تفصیلات ایسے تصورات ہیں جو زبان کے ڈیزائن، AI تحقیق، اور یہاں تک کہ ڈیٹا بیس کے استفسار کی اصلاح کو متاثر کرتے ہیں۔
### پرولوگ انجن کا موازنہ
| خصوصیت | SWI-Prolog | GNU Prolog | Tau Prolog |
|---------|------------|------------|------------|
| **لائسنس** | BSD (اوپن سورس) | GPL (اوپن سورس) | BSD (اوپن سورس) |
| **پلیٹ فارم** | ونڈوز، لینکس، میکوس | ونڈوز، لینکس، میکوس | جاوا اسکرپٹ (براؤزر) |
| **CLP(FD)** | بلٹ ان لائبریری | بلٹ ان | دستیاب نہیں |
| **DCG سپورٹ** | مکمل | مکمل | محدود |
| **ٹیبلنگ** | جی ہاں | نہیں | نہیں |
| **FFI (C کالز)** | جی ہاں | جی ہاں | جاوا اسکرپٹ کے ذریعے |
| **نیٹ ورکنگ** | HTTP، TCP، TLS | TCP | جاوا اسکرپٹ کے ذریعے |
| **ملٹی تھریڈنگ** | جی ہاں | نہیں | نہیں |
| **پیکیج مینیجر** | `pack_install/1`| کوئی نہیں | npm |
| ** کے لیے بہترین ** | پیداوار، تحقیق | رکاوٹوں کو حل کرنا | ویب ایپس، تعلیم |
### پینگائنز کے ساتھ ویب ایپلیکیشنز
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

### دعوی / واپس لینے کے ساتھ میٹا پروگرامنگ
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
