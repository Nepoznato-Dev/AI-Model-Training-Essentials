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

# برولوج
برولوج (البرمجة في المنطق) هي لغة برمجة منطقية تم إنشاؤها في عام 1972 من قبل آلان كولميراور وفيليب روسيل. على عكس كل اللغات الأخرى في هذه القائمة، لا يخبر Prolog الكمبيوتر *كيفية* حل مشكلة ما - فأنت تعلن *ما هو* الصحيح (الحقائق والقواعد)، ويكتشف محرك الاستدلال الخاص بـ Prolog الإجابة من خلال الاستنتاج المنطقي.
كانت Prolog هي اللغة المفضلة للأنظمة المتخصصة ومعالجة اللغات الطبيعية وأبحاث الذكاء الاصطناعي في الثمانينيات. لقد دعم مشروع نظام الكمبيوتر للجيل الخامس في اليابان وتم استخدامه في نظام Watson التابع لشركة IBM لفهم اللغة الطبيعية. اليوم، يتم استخدام Prolog في حل القيود، والجدولة، واستدلال النوع، والتفكير القانوني، وفي أي مكان يتم التعبير عن المشاكل بشكل طبيعي كعلاقات منطقية.
**برمجة منطق القيد (CLP)** تعمل على توسيع Prolog باستخدام أدوات حل القيود للجدولة والتوجيه وتخصيص الموارد - وهي مشكلات صعبة للغاية في اللغات الضرورية.
---

## لماذا يهم Prolog
- **البرمجة التعريفية**: وصف ما هو صحيح، وليس كيفية حسابه. المحرك يقوم بالعمل.
- **مطابقة الأنماط وتوحيدها**: تعد خوارزمية التوحيد في Prolog أقوى من مطابقة الأنماط في اللغات الأخرى.
- **البحث التراجعي**: يستكشف جميع الحلول الممكنة تلقائيًا. لا حاجة لخوارزميات البحث اليدوي.
- **طبيعي للمشكلات المنطقية**: الأنظمة المتخصصة، ومحركات القواعد، ومدققي الكتابة، والمحللي النحوي — يتم ربطها مباشرةً بـ Prolog.
- **حل القيود**: يعمل CLP(FD) على حل مشاكل الجدولة والتخصيص والاندماج بشكل أنيق.
- **تفكير مختلف**: يُغير برنامج Learning Prolog الطريقة التي تتعامل بها مع حل المشكلات - حيث تبدأ في التفكير في العلاقات والقيود.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **نموذج مختلف جدًا** | لا توجد متغيرات (ارتباطات فقط)، ولا حلقات، ولا مهام | فكر في العلاقات والتكرار، وليس تغييرات الحالة |
| **الأداء** | بطيء في الحساب العددي والبيانات الكبيرة | استخدام للاستدلال. تفويض الحساب إلى C/لغات أخرى |
| ** صعوبة التصحيح ** | من الصعب تتبع التراجع وفشل التوحيد | استخدم أدوات التتبع/التصحيح؛ كتابة المسندات الحتمية |
| **عامل القطع (!)** | مطلوب للكفاءة ولكنه يكسر النقاء المنطقي | استخدم إذا كان الأمر كذلك أو التقييم المجدول عندما يكون ذلك ممكنًا |
| **نظام بيئي محدود** | عدد قليل من المكتبات أو الأطر أو موارد المجتمع | SWI-Prolog هو التنفيذ الأكثر اكتمالا |
| **ليس للتطبيقات العامة** | الويب والهاتف المحمول وواجهة المستخدم الرسومية — ليست قوة Prolog | الاستخدام كمحرك تفكير وراء تطبيق ويب |
---

## أساسيات بناء الجملة
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

## بناء الجملة والأنماط المتقدمة
### التوحيد الغوص العميق
التوحيد هو الآلية الأساسية لـ Prolog - وهي الطريقة التي يطابق بها Prolog المصطلحات ويربط المتغيرات.
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

### التراجع ونقاط الاختيار
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

### القواعد النحوية للجمل المحددة (DCGs)
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

### البرمجة المنطقية المقيدة (CLP)
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

## الهندسة المعمارية وتصميم النظام
### نموذج البرمجة المنطقية
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

### هيكل المشروع النموذجي
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

### نظام الوحدة
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

## تكوين المشروع ونظام البناء
### تكوين SWI-Prolog
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

### تشغيل برامج برولوج
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

### تكوين التكوين
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

## الاختبار والتصحيح
### تتبع مدمج
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

### اختبار الوحدة باستخدام PLUnit
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

### أنماط التصحيح الشائعة
| مشكلة | العَرَض | الحل |
|---------|--------|----------|
| العودية اللانهائية | تجاوز سعة المكدس | تحقق من الحالة الأساسية؛ إضافة شرط الإنهاء |
| لا حلول | الاستعلام يُرجع خطأ | تحقق من ترتيب إنشاء مثيل متغير |
| الحلول كثيرة جداً | التكرارات غير المتوقعة | أضف قطعًا (!) أو استخدم`setof`|
| التوحيد الخاطئ | المتغيرات مرتبطة بشكل غير صحيح | استخدم`=`للاختبار؛ تحقق من وظيفة العامل |
| مشكلة الأداء | تنفيذ بطيء | إضافة تخفيضات. استخدم `table`؛ تحقق من نقاط الاختيار |
---

## إمكانية التشغيل البيني
### واجهة C (FFI)
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

### تكامل بايثون
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

## أنماط التصميم
### النموذج 1: التراكمي (العودة الخلفية)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### النمط 2: ترابط الحالة```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### النموذج 3: الإنشاء والاختبار```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### النموذج 4: قوائم الفرق```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## الأداء والتحسين
### قطع الأمثل
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### العودية الذيلية
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### قائمة التحقق من التحسين
| تقنية | التأثير | الوصف |
|-----------|-------|-------------|
| ** العودية الذيل ** | عالية | استخدم المراكم لمساحة المكدس الثابتة |
| **قص (أخضر)** | عالية | تخلص من نقاط الاختيار غير الضرورية |
| **التقييم المقدم** | عالية | `:- table pred/N`يحفظ النتائج |
| **الفهرسة** | متوسطة | ضع حجة التمييز أولاً |
| **قوائم الفروق** | متوسطة | O(1) قائمة التسلسل |
| **CLP(FD) عبر اختبار الإنشاء** | عالية جدًا | استخدم القيود بدلاً من القوة الغاشمة |
---

## النشر والاستخدام في العالم الحقيقي
### نشر تطبيقات Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### تطبيقات العالم الحقيقي
| المجال | كيف يتم استخدام البرولوج | مثال |
|--------|-------------------|---------|
| **الأنظمة الخبيرة** | التشخيص الطبي وكشف الأخطاء | مايسين، إكسكون |
| ** البرمجة اللغوية العصبية ** | التحليل النحوي والتحليل الدلالي | روبوتات الدردشة وأنظمة ضمان الجودة |
| **اكتب الاستدلال** | فحص نوع هيندلي ميلنر | نماذج هاسكل/ML |
| **الجدولة** | جدولة الموظف، الجدول الزمني | جدولة طاقم الطيران |
| **الاستدلال القانوني** | التحليل القانوني المبني على القواعد | فحص الامتثال |
| ** الاستعلام عن قاعدة البيانات ** | Datalog لتحليل البيانات | محرك سوفليه |
| **التحقق** | فحص النموذج | التحقق من الأجهزة |
| ** آي بي إم واتسون ** | فهم اللغة الطبيعية | خطر! النظام |
| **إريكسون** | إدارة الاتصالات | التحقق من صحة تكوين الشبكة |
---

## متى يجب استخدام Prolog
| السيناريو | لماذا برولوج | البديل الأفضل |
|----------|---------|------------------|
| الاستدلال المبني على القواعد | تم إنشاء Prolog لهذا | محركات القواعد المخصصة في Python/Java |
| رضا القيد | CLP(FD) أنيق وفعال | حلول SAT، أدوات OR للمثيلات الكبيرة |
| النحو / تحليل اللغة | DCG (قواعد النحو المحددة) أصلية | مولدات المحلل اللغوي (ANTLR, yacc) للإنتاج |
| الأنظمة الخبيرة | الملاءمة الطبيعية – حقائق + قواعد = نظام خبير | محركات قواعد الأعمال (Drools) |
| الجدولة / الجدول الزمني | CLP يحل هذه الأمور بشكل جيد | أدوات أو، OptaPlanner |
| نوع بحث النظام | التوحيد هو الأساس | التنفيذ في OCaml، Haskell، Rust |
| تطبيقات الويب | غير مناسب | بايثون، Node.js، اذهب |
| علم البيانات / تعلم الآلة | ليس النظام البيئي | بايثون، ر |
| كود الأداء الحرج | Prolog بطيء في الحساب | C، C++، الصدأ |
| برمجة للأغراض العامة | ممكن ولكن محرج | بايثون، جو، جافا |
---

## أسئلة وأجوبة اصطناعية
### س1: كيف يختلف توحيد Prolog عن التوحيد في اللغات الأخرى؟
**أ:** التوحيد هو مطابقة الأنماط ثنائية الاتجاه، وليس التعيين:
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

### السؤال الثاني: كيف يعمل التراجع في Prolog؟
**أ:** عندما يفشل أحد الأهداف، يتراجع Prolog إلى نقطة الاختيار الأخيرة ويحاول البديل التالي:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: كيف يمكنني العمل مع القوائم في Prolog؟
**أ:** تستخدم القوائم مطابقة نمط الرأس/الذيل:
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

### س4: متى يجب علي استخدام Prolog بدلاً من اللغات الأخرى؟
**أ:** يتفوق Prolog في:
- رضا القيد (الجدولة، والألغاز)
- الأنظمة القائمة على القواعد (أنظمة الخبراء، التحقق من الصحة)
- الرسم البياني / اجتياز الشجرة
- معالجة اللغة الطبيعية
- الحساب الرمزي
- أي مشكلة يمكن التعبير عنها بالعلاقات المنطقية
### س5: ما هي الأخطاء الشائعة في Prolog؟
**أ:** القضايا الرئيسية:
- التكرار اللانهائي - ضع دائمًا الحالة الأساسية أولاً
- التراجع غير المقصود - استخدم القطع`!`أو`once/1`
- التحقق من حدوث — حلقات`X = f(X)`بشكل افتراضي (استخدم`unify_with_occurs_check`)
- القطع الخضراء (التحسين) مقابل القطع الحمراء (تغيير المعنى) - تفضل اللون الأخضر
---

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة الأولى: حل لغز N-Queens
**الخطوة الأولى: فهم المشكلة**
ضع ملكات N على رقعة الشطرنج NxN حتى لا تهاجم ملكتان بعضهما البعض.
**الخطوة 2: تحديد النهج**
استخدم التوليد القائم على القيود: ضع الملكات عمودًا تلو الآخر، مع التحقق من السلامة.
**الخطوة 3: التنفيذ**```prolog
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

**الخطوة 4: التحقق**
 يجب أن يجد`?- n_queens(8, Qs).`92 حلاً.
### المشكلة الثانية: بناء نظام خبير بسيط
**الخطوة الأولى: فهم المشكلة**
تشخيص مشاكل السيارة بناء على الأعراض.
**الخطوة 2: تحديد النهج**
استخدم قواعد Prolog لترميز المعرفة التشخيصية.
**الخطوة 3: التنفيذ**```prolog
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

**الخطوة 4: تمديد**
أضف درجات الثقة، واطلب من المستخدم الأعراض بشكل تفاعلي، وقم بالتشخيص المتسلسل.
---

## ملخص
Prolog لا يشبه أي لغة برمجة أخرى. بدلاً من كتابة تعليمات خطوة بخطوة، يمكنك وصف العلاقات والقيود - ويبحث المحرك عن الحلول من خلال الاستدلال المنطقي. وهذا يجعل Prolog مثاليًا للمشكلات غير الملائمة أو المطولة في اللغات الأمرية: الأنظمة المتخصصة، والجدولة، والتحليل النحوي، وتلبية القيود، وأي شيء يتضمن قواعد منطقية. لن يستخدم معظم المبرمجين برنامج Prolog أبدًا في الإنتاج، لكن تعلمه يوسع تفكيرك حول ماهية البرمجة. يعد التوحيد والتتبع وتحديد المشكلة التصريحية من المفاهيم التي تؤثر على تصميم اللغة وأبحاث الذكاء الاصطناعي وحتى تحسين استعلام قاعدة البيانات.
### مقارنة محركات Prolog
| ميزة | سوي برولوج | برولوج جنو | تاو برولوج |
|---------|----------|------------|------------|
| **الترخيص** | بي إس دي (مفتوح المصدر) | جي بي إل (مفتوحة المصدر) | بي إس دي (مفتوح المصدر) |
| **المنصة** | ويندوز، لينكس، ماك | ويندوز، لينكس، ماك | جافا سكريبت (متصفح) |
| **CLP(FD)** | مكتبة مدمجة | مدمج | غير متوفر |
| ** دعم DCG ** | كامل | كامل | محدودة |
| **الجدولة** | نعم | لا | لا |
| **FFI (مكالمات C)** | نعم | نعم | عبر جافا سكريبت |
| **الشبكات** | HTTP، TCP، TLS | برنامج التعاون الفني | عبر جافا سكريبت |
| ** متعدد الخيوط ** | نعم | لا | لا |
| ** مدير الحزم ** | `pack_install/1`| لا شيء | نبم |
| **الأفضل لـ** | إنتاج وأبحاث | حل القيد | تطبيقات الويب والتعليم |
### تطبيقات الويب مع Pengines
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

### البرمجة الفوقية مع التأكيد/التراجع
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
