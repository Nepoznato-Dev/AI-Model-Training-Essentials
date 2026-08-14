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
# প্রোলগ
প্রোলগ (লজিকে প্রোগ্রামিং) হল একটি লজিক প্রোগ্রামিং ভাষা যা 1972 সালে অ্যালাইন কলমেরউয়ার এবং ফিলিপ রাউসেল দ্বারা তৈরি করা হয়েছিল। এই তালিকার অন্যান্য ভাষার মত নয়, প্রোলগ কম্পিউটারকে *কীভাবে* একটি সমস্যা সমাধান করতে হবে তা বলে না — আপনি *কী* সত্য (তথ্য এবং নিয়ম) ঘোষণা করেন এবং প্রোলগের ইনফরেন্স ইঞ্জিন লজিক্যাল ডিডাকশনের মাধ্যমে উত্তর বের করে।
1980 এর দশকে বিশেষজ্ঞ সিস্টেম, প্রাকৃতিক ভাষা প্রক্রিয়াকরণ এবং এআই গবেষণার জন্য প্রোলগ ছিল পছন্দের ভাষা। এটি জাপানের পঞ্চম প্রজন্মের কম্পিউটার সিস্টেম প্রকল্পকে চালিত করেছিল এবং প্রাকৃতিক ভাষা বোঝার জন্য আইবিএম-এর ওয়াটসনে ব্যবহৃত হয়েছিল। আজ, প্রোলগ সীমাবদ্ধতা সমাধান, সময়সূচী, টাইপ ইনফরেন্স, আইনি যুক্তিতে ব্যবহৃত হয় এবং যেকোনো জায়গায় সমস্যাগুলি স্বাভাবিকভাবেই যৌক্তিক সম্পর্ক হিসাবে প্রকাশ করা হয়।
**কনস্ট্রেন্ট লজিক প্রোগ্রামিং (সিএলপি)** সময়সূচী, রাউটিং এবং রিসোর্স অ্যালোকেশনের জন্য সীমাবদ্ধতা সমাধানকারীর সাথে প্রোলগকে প্রসারিত করে — যে সমস্যাগুলি অপরিহার্য ভাষায় অত্যন্ত কঠিন।
---

## কেন প্রোলগ ব্যাপার
- **ঘোষণামূলক প্রোগ্রামিং**: সত্য কী তা বর্ণনা করুন, কীভাবে গণনা করবেন তা নয়। ইঞ্জিন কাজ করে।
- **প্যাটার্ন ম্যাচিং এবং ইউনিফিকেশন**: প্রোলগের ইউনিফিকেশন অ্যালগরিদম অন্যান্য ভাষায় প্যাটার্ন ম্যাচিং এর চেয়ে বেশি শক্তিশালী।
- **ব্যাকট্র্যাকিং অনুসন্ধান**: স্বয়ংক্রিয়ভাবে সমস্ত সম্ভাব্য সমাধান অন্বেষণ করে। কোন ম্যানুয়াল অনুসন্ধান অ্যালগরিদম প্রয়োজন.
- **লজিক সমস্যার জন্য প্রাকৃতিক**: বিশেষজ্ঞ সিস্টেম, নিয়ম ইঞ্জিন, টাইপ চেকার, ব্যাকরণ পার্সার — এই ম্যাপ সরাসরি প্রোলগে।
- **সীমাবদ্ধতা সমাধান**: CLP(FD) সময়সূচী, বরাদ্দকরণ এবং সমন্বিত সমস্যাগুলি সুন্দরভাবে সমাধান করে।
- **ভিন্ন চিন্তা**: শেখার প্রোলগ পরিবর্তন করে যে আপনি কীভাবে সমস্যা সমাধানের দিকে যান — আপনি সম্পর্ক এবং সীমাবদ্ধতার বিষয়ে ভাবতে শুরু করেন।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **খুব ভিন্ন দৃষ্টান্ত** | কোন ভেরিয়েবল নেই (শুধু বাইন্ডিং), কোন লুপ নেই, কোন অ্যাসাইনমেন্ট নেই | সম্পর্ক এবং পুনরাবৃত্তি চিন্তা করুন, রাষ্ট্র পরিবর্তন নয় |
| **পারফরম্যান্স** | সংখ্যাগত গণনা এবং বড় ডেটার জন্য ধীর | যুক্তির জন্য ব্যবহার করুন; সি/অন্যান্য ভাষায় গণনা অর্পণ করে |
| **ডিবাগিং অসুবিধা** | ব্যাকট্র্যাকিং এবং একীকরণ ব্যর্থতা ট্রেস করা কঠিন | ট্রেস/ডিবাগ টুল ব্যবহার করুন; নির্ধারক পূর্বাভাস লিখুন |
| **কাট অপারেটর (!)** | দক্ষতার জন্য প্রয়োজন কিন্তু যৌক্তিক বিশুদ্ধতা ভঙ্গ করে | যদি সম্ভব হয় তাহলে-অন্যথা বা টেবিল মূল্যায়ন ব্যবহার করুন |
| **সীমিত ইকোসিস্টেম** | কিছু লাইব্রেরি, ফ্রেমওয়ার্ক, বা কমিউনিটি রিসোর্স | SWI-Prolog হল সবচেয়ে সম্পূর্ণ বাস্তবায়ন |
| **সাধারণ অ্যাপের জন্য নয়** | ওয়েব, মোবাইল, GUI — প্রোলগের শক্তি নয় | একটি ওয়েব অ্যাপের পিছনে যুক্তি ইঞ্জিন হিসাবে ব্যবহার করুন |
---

## সিনট্যাক্স মৌলিক
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### একীকরণ গভীর ডুব
একীকরণ হল প্রোলগ এর মূল প্রক্রিয়া — এটি হল যেভাবে প্রোলগ পদগুলিকে "মেলে" এবং ভেরিয়েবলগুলিকে আবদ্ধ করে৷
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

### ব্যাকট্র্যাকিং এবং চয়েস পয়েন্ট
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

### নির্দিষ্ট ধারা ব্যাকরণ (DCGs)
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

### সীমাবদ্ধতা লজিক প্রোগ্রামিং (CLP)
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

## আর্কিটেকচার এবং সিস্টেম ডিজাইন
### লজিক প্রোগ্রামিং প্যারাডাইম
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

### সাধারণ প্রকল্প কাঠামো
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

### মডিউল সিস্টেম
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### SWI-Prolog কনফিগারেশন
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

### চলমান প্রোলগ প্রোগ্রাম
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

### কনফিগারেশন তৈরি করুন
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

## পরীক্ষা এবং ডিবাগিং
### অন্তর্নির্মিত ট্রেসিং
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

### PLUnit সহ ইউনিট পরীক্ষা
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

### সাধারণ ডিবাগিং প্যাটার্ন
| সমস্যা | উপসর্গ | সমাধান |
|---------|---------|----------|
| অসীম পুনরাবৃত্তি | স্ট্যাক ওভারফ্লো | বেস কেস চেক করুন; সমাপ্তি শর্ত যোগ করুন |
| কোন সমাধান নেই | প্রশ্ন মিথ্যা ফেরত | পরিবর্তনশীল ইনস্ট্যান্টিয়েশন অর্ডার চেক করুন |
| অনেক সমাধান | অপ্রত্যাশিত সদৃশ | কাটা যোগ করুন (!) অথবা`setof`| ব্যবহার করুন
| ভুল একীকরণ | ভেরিয়েবল ভুলভাবে আবদ্ধ | পরীক্ষা করতে`=`ব্যবহার করুন; ফাংশন আরটি চেক করুন |
| কর্মক্ষমতা সমস্যা | ধীর মৃত্যুদন্ড | কাটা যোগ করুন;`table`ব্যবহার করুন; পছন্দের পয়েন্ট চেক করুন |
---

## ইন্টারঅপারেবিলিটি
### সি ইন্টারফেস (এফএফআই)
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

### পাইথন ইন্টিগ্রেশন
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

## ডিজাইন প্যাটার্ন
### প্যাটার্ন ১: অ্যাকিউমুলেটর (টেইল রিকারশন)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### প্যাটার্ন 2: স্টেট থ্রেডিং```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### প্যাটার্ন 3: তৈরি করুন এবং পরীক্ষা করুন```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### প্যাটার্ন 4: পার্থক্য তালিকা```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### কাট অপটিমাইজেশন
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### লেজের পুনরাবৃত্তি
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### অপ্টিমাইজেশান চেকলিস্ট
| টেকনিক | প্রভাব | বর্ণনা |
|------------|---------|---------------|
| **টেইল রিকারশন** | উচ্চ | ধ্রুব স্ট্যাক স্পেসের জন্য সঞ্চয়কারী ব্যবহার করুন |
| **কাট (সবুজ)** | উচ্চ | অপ্রয়োজনীয় পছন্দ পয়েন্ট বাদ দিন |
| **টেবিল মূল্যায়ন** | উচ্চ | `:- table pred/N`ফলাফল মুখস্থ করে |
| **সূচীকরণ** | মাঝারি | বৈষম্যমূলক যুক্তি আগে রাখুন |
| **পার্থক্য তালিকা** | মাঝারি | O(1) তালিকা সংযোজন |
| **সিএলপি(এফডি) ওভার জেনারেট-টেস্ট** | খুব উচ্চ | পাশবিক শক্তির পরিবর্তে সীমাবদ্ধতা ব্যবহার করুন |
---

## স্থাপনা এবং বাস্তব-বিশ্ব ব্যবহার
### প্রোলগ অ্যাপ্লিকেশন স্থাপন করা হচ্ছে
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### বাস্তব-বিশ্বের অ্যাপ্লিকেশন
| ডোমেন | কিভাবে Prolog ব্যবহার করা হয় | উদাহরণ |
|---------|---------|---------|
| **বিশেষজ্ঞ সিস্টেম** | চিকিৎসা নির্ণয়, ত্রুটি সনাক্তকরণ | MYCIN, XCON |
| **NLP** | ব্যাকরণ পার্সিং, শব্দার্থিক বিশ্লেষণ | চ্যাটবট, QA সিস্টেম |
| **প্রকার অনুমান** | হিন্ডলি-মিলনার টাইপ চেকিং | হাস্কেল/এমএল প্রোটোটাইপ |
| **শিডিউলিং** | কর্মচারী সময়সূচী, সময়সূচী | এয়ারলাইন ক্রু শিডিউলিং |
| **আইনি যুক্তি** | নিয়ম ভিত্তিক আইনি বিশ্লেষণ | কমপ্লায়েন্স চেকিং |
| **ডাটাবেস অনুসন্ধান** | ডেটা বিশ্লেষণের জন্য ডেটালগ | Soufflé ইঞ্জিন |
| **যাচাই** | মডেল চেকিং | হার্ডওয়্যার যাচাইকরণ |
| **আইবিএম ওয়াটসন** | প্রাকৃতিক ভাষা বোঝার | বিপদ! সিস্টেম |
| **এরিকসন** | টেলিকম ব্যবস্থাপনা | নেটওয়ার্ক কনফিগারেশন যাচাইকরণ |
---

## কখন প্রোলগ ব্যবহার করবেন
| দৃশ্যকল্প | কেন Prolog | ভাল বিকল্প |
|------------|------------|---------|
| নিয়ম ভিত্তিক যুক্তি | প্রোলগ এই জন্য নির্মিত হয় | পাইথন/জাভাতে কাস্টম নিয়ম ইঞ্জিন |
| সীমাবদ্ধতা সন্তুষ্টি | CLP(FD) মার্জিত এবং দক্ষ | বড় উদাহরণের জন্য SAT সমাধানকারী, OR- টুলস |
| ব্যাকরণ / ভাষা পার্সিং | DCG (Definite Clause Grammars) নেটিভ | উৎপাদনের জন্য পার্সার জেনারেটর (ANTLR, yacc) |
| বিশেষজ্ঞ সিস্টেম | প্রাকৃতিক উপযুক্ত — তথ্য + নিয়ম = বিশেষজ্ঞ সিস্টেম | ব্যবসায়িক নিয়ম ইঞ্জিন (Drools) |
| সময়সূচী / সময়সূচী | সিএলপি এগুলো ভালোভাবে সমাধান করে | OR-Tools, OptaPlanner |
| টাইপ সিস্টেম গবেষণা | একীকরণের ভিত্তি | OCaml, Haskell, Rust এ প্রয়োগ করুন |
| ওয়েব অ্যাপ্লিকেশন | উপযুক্ত নয় | Python, Node.js, Go |
| ডেটা সায়েন্স / এমএল | বাস্তুতন্ত্র নয় | পাইথন, আর |
| কর্মক্ষমতা-সমালোচনা কোড | প্রোলগ গণনার জন্য ধীর | C, C++, মরিচা |
| সাধারণ-উদ্দেশ্য প্রোগ্রামিং | সম্ভব কিন্তু বিশ্রী | পাইথন, গো, জাভা |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: প্রোলগের একীকরণ অন্যান্য ভাষার অ্যাসাইনমেন্ট থেকে কীভাবে আলাদা?
**A:** একীকরণ হল দ্বিমুখী প্যাটার্ন ম্যাচিং, অ্যাসাইনমেন্ট নয়:
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

### প্রশ্ন 2: প্রোলগে ব্যাকট্র্যাকিং কীভাবে কাজ করে?
**A:** একটি লক্ষ্য ব্যর্থ হলে, Prolog শেষ পছন্দের পয়েন্টে ফিরে যায় এবং পরবর্তী বিকল্প চেষ্টা করে:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### প্রশ্ন 3: প্রোলগে আমি কীভাবে তালিকা নিয়ে কাজ করব?
**A:** তালিকাগুলি হেড/টেইল প্যাটার্ন ম্যাচিং ব্যবহার করে:
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

### প্রশ্ন 4: আমি কখন অন্যান্য ভাষার পরিবর্তে প্রোলগ ব্যবহার করব?
**A:** প্রোলগ এখানে এক্সেল:
- সীমাবদ্ধতা সন্তুষ্টি (নির্ধারণ, ধাঁধা)
- নিয়ম-ভিত্তিক সিস্টেম (বিশেষজ্ঞ সিস্টেম, বৈধতা)
- গ্রাফ/ট্রি ট্রাভার্সাল
- প্রাকৃতিক ভাষা প্রক্রিয়াকরণ
- প্রতীকী গণনা
- যৌক্তিক সম্পর্ক হিসাবে প্রকাশযোগ্য যে কোনও সমস্যা
### প্রশ্ন 5: প্রোলগের সাধারণ অসুবিধাগুলি কী কী?
**A:** মূল সমস্যা:
- অসীম পুনরাবৃত্তি — সর্বদা বেস কেসটি প্রথমে রাখুন
- অনিচ্ছাকৃত ব্যাকট্র্যাকিং - কাট`!`বা`once/1`ব্যবহার করুন 
- সংঘটিত চেক —`X = f(X)`ডিফল্টরূপে লুপ (`unify_with_occurs_check` ব্যবহার করুন)
- সবুজ কাট (অপ্টিমাইজেশান) বনাম লাল কাট (অর্থ পরিবর্তন করুন) - সবুজ পছন্দ করুন
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: এন-কুইন্স ধাঁধা সমাধান করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি NxN চেসবোর্ডে N রানী রাখুন যাতে কোন দুই রানী একে অপরকে আক্রমণ না করে।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
সীমাবদ্ধতা-ভিত্তিক প্রজন্ম ব্যবহার করুন: কলাম দ্বারা রাণী কলাম রাখুন, নিরাপত্তা পরীক্ষা করুন।
**ধাপ 3: প্রয়োগ করুন**```prolog
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

**পদক্ষেপ 4: যাচাই করুন**
`?- n_queens(8, Qs).`এর 92টি সমাধান খুঁজে পাওয়া উচিত।
### সমস্যা 2: একটি সাধারণ বিশেষজ্ঞ সিস্টেম তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
উপসর্গের ভিত্তিতে গাড়ির সমস্যা নির্ণয় করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
ডায়াগনস্টিক জ্ঞান এনকোড করতে Prolog নিয়ম ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```prolog
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

**ধাপ 4: প্রসারিত করুন**
আত্মবিশ্বাসের স্কোর যোগ করুন, ব্যবহারকারীকে ইন্টারেক্টিভভাবে লক্ষণগুলির জন্য জিজ্ঞাসা করুন এবং চেইন রোগ নির্ণয় করুন।
---

## সারাংশ
প্রোলগ অন্য কোন প্রোগ্রামিং ভাষার মত নয়। ধাপে ধাপে নির্দেশনা লেখার পরিবর্তে, আপনি সম্পর্ক এবং সীমাবদ্ধতা বর্ণনা করেন — এবং ইঞ্জিন যৌক্তিক অনুমানের মাধ্যমে সমাধান অনুসন্ধান করে। এটি প্রয়োজনীয় ভাষায় বিশ্রী বা শব্দসমস্যার সমস্যাগুলির জন্য প্রোলগকে আদর্শ করে তোলে: বিশেষজ্ঞ সিস্টেম, সময়সূচী, ব্যাকরণ পার্সিং, সীমাবদ্ধতা সন্তুষ্টি, এবং যৌক্তিক নিয়ম জড়িত কিছু। বেশিরভাগ প্রোগ্রামার কখনোই প্রোলগ প্রোডাকশনে ব্যবহার করবেন না, কিন্তু এটি শেখার ফলে প্রোগ্রামিং কী হতে পারে সে সম্পর্কে আপনার চিন্তাভাবনা প্রসারিত হয়। একীকরণ, ব্যাকট্র্যাকিং, এবং ঘোষণামূলক সমস্যা স্পেসিফিকেশন এমন ধারণা যা ভাষা ডিজাইন, এআই গবেষণা এবং এমনকি ডাটাবেস কোয়েরি অপ্টিমাইজেশানকে প্রভাবিত করে।
### প্রোলগ ইঞ্জিন তুলনা
| বৈশিষ্ট্য | SWI-Prolog | GNU Prolog | Tau Prolog |
|---------|------------|------------|------------|
| **লাইসেন্স** | বিএসডি (ওপেন সোর্স) | GPL (ওপেন সোর্স) | বিএসডি (ওপেন সোর্স) |
| **প্ল্যাটফর্ম** | Windows, Linux, macOS | Windows, Linux, macOS | জাভাস্ক্রিপ্ট (ব্রাউজার) |
| **CLP(FD)** | অন্তর্নির্মিত লাইব্রেরি | অন্তর্নির্মিত | উপলব্ধ নয় |
| **DCG সমর্থন** | পূর্ণ | পূর্ণ | লিমিটেড |
| **টেবিলিং** | হ্যাঁ | না | না |
| **এফএফআই (সি কল)** | হ্যাঁ | হ্যাঁ | জাভাস্ক্রিপ্টের মাধ্যমে |
| **নেটওয়ার্কিং** | HTTP, TCP, TLS | TCP | জাভাস্ক্রিপ্টের মাধ্যমে |
| **মাল্টি-থ্রেডিং** | হ্যাঁ | না | না |
| **প্যাকেজ ম্যানেজার** | `pack_install/1`| কোনটিই না | npm |
| **এর জন্য সেরা** | উৎপাদন, গবেষণা | সীমাবদ্ধতা সমাধান | ওয়েব অ্যাপস, শিক্ষা |
### পেঙ্গিন সহ ওয়েব অ্যাপ্লিকেশন
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

### দাবি/প্রত্যাহার সহ মেটাপ্রোগ্রামিং
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
