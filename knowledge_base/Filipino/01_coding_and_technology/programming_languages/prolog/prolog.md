<!--
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

-->
# Prolog
Ang Prolog (Programming in Logic) ay isang logic programming language na nilikha noong 1972 nina Alain Colmerauer at Philippe Roussel. Hindi tulad ng lahat ng iba pang wika sa listahang ito, hindi sinasabi ng Prolog sa computer *kung paano* lulutasin ang isang problema — idineklara mo *ano* ang totoo (mga katotohanan at panuntunan), at ang inference engine ng Prolog ay nagtatatag ng sagot sa pamamagitan ng lohikal na pagbabawas.
Ang Prolog ay ang piniling wika para sa mga expert system, natural na pagpoproseso ng wika, at pananaliksik sa AI noong 1980s. Pinalakas nito ang proyekto ng Fifth Generation Computer System ng Japan at ginamit sa Watson ng IBM para sa natural na pag-unawa sa wika. Ngayon, ang Prolog ay ginagamit sa paglutas ng hadlang, pag-iskedyul, uri ng hinuha, legal na pangangatwiran, at kahit saan ang mga problema ay natural na ipinahayag bilang mga lohikal na relasyon.
Ang **Constraint Logic Programming (CLP)** ay nagpapalawak ng Prolog gamit ang mga constraint solver para sa pag-iskedyul, pagruruta, at paglalaan ng mapagkukunan — mga problemang napakahirap sa mga kinakailangang wika.
---

## Bakit Mahalaga ang Prolog
- **Declarative programming**: Ilarawan kung ano ang totoo, hindi kung paano ito kalkulahin. Ginagawa ng makina ang trabaho.
- **Pagtutugma ng pattern at pag-iisa**: Ang algorithm ng unification ng Prolog ay mas malakas kaysa sa pagtutugma ng pattern sa ibang mga wika.
- **Backtracking na paghahanap**: Awtomatikong ginalugad ang lahat ng posibleng solusyon. Walang kinakailangang mga algorithm ng manu-manong paghahanap.
- **Natural para sa mga problema sa lohika**: Mga ekspertong system, rule engine, type checker, grammar parser — ang mga ito ay direktang nagmamapa sa Prolog.
- **Paglutas ng hadlang**: Malulutas ng CLP(FD) ang mga problema sa pag-iiskedyul, paglalaan, at kombinatoryal.
- **Iba't ibang pag-iisip**: Binabago ng Learning Prolog ang paraan ng pagharap mo sa paglutas ng problema — magsisimula kang mag-isip sa mga relasyon at mga hadlang.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Very different paradigm** | Walang mga variable (mga binding lamang), walang mga loop, walang mga takdang-aralin | Mag-isip sa mga relasyon at recursion, hindi pagbabago ng estado |
| **Pagganap** | Mabagal para sa numerical computation at malaking data | Gamitin para sa pangangatwiran; italaga ang computation sa C/ibang mga wika |
| **Hirap sa pag-debug** | Mahirap masubaybayan ang mga pagkabigo sa backtracking at unification | Gumamit ng mga tool sa pagsubaybay/debug; sumulat ng mga tiyak na panaguri |
| **Cut operator (!)** | Kailangan para sa kahusayan ngunit sinisira ang lohikal na kadalisayan | Gumamit ng if-then-else o tabled evaluation kapag posible |
| **Limitadong ecosystem** | Ilang mga aklatan, balangkas, o mapagkukunan ng komunidad | Ang SWI-Prolog ay ang pinakakumpletong pagpapatupad |
| **Hindi para sa mga pangkalahatang app** | Web, mobile, GUI — hindi ang lakas ng Prolog | Gamitin bilang reasoning engine sa likod ng isang web app |
---

## Syntax Fundamentals
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

## Advanced na Syntax at Mga Pattern
### Unification Deep Dive
Ang Unification ay ang pangunahing mekanismo ng Prolog — ito ay kung paano "tumutugma" ang Prolog sa mga termino at nagbubuklod ng mga variable.
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

### Mga Puntos sa Pag-backtrack at Pagpipilian
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

### Definite Clause Grammar (Mga DCG)
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

### Constraint Logic Programming (CLP)
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

## Arkitektura at Disenyo ng System
### Logic Programming Paradigm
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

### Karaniwang Istraktura ng Proyekto
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

### Sistema ng Module
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

## Project Configuration at Build System
### SWI-Prolog Configuration
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

### Tumatakbo ng Prolog Programs
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

### Build Configuration
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

## Pagsubok at Pag-debug
### Built-in na Pagsubaybay
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

### Pagsubok ng Unit gamit ang PLUnit
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

### Mga Karaniwang Pattern ng Pag-debug
| Problema | Sintomas | Solusyon |
|---------|---------|----------|
| Walang katapusang recursion | Stack overflow | Suriin ang base case; magdagdag ng kondisyon ng pagwawakas |
| Walang solusyon | Ang query ay nagbabalik ng false | Suriin ang variable instantiation order |
| Masyadong maraming solusyon | Mga hindi inaasahang duplicate | Magdagdag ng cut (!) o gumamit ng`setof`|
| Maling pagkakaisa | Mali ang pagkakatali ng mga variable | Gamitin ang`=`upang subukan; suriin ang functionor arity |
| Isyu sa pagganap | Mabagal na pagpapatupad | Magdagdag ng mga pagbawas; gumamit ng`table`; suriin ang mga pagpipiliang puntos |
---

## Interoperability
### C Interface (FFI)
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

### Pagsasama ng Python
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

## Mga Pattern ng Disenyo
### Pattern 1: Accumulator (Tail Recursion)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Pattern 2: State Threading```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Pattern 3: Bumuo at Subukan```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Pattern 4: Mga Listahan ng Pagkakaiba```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Pagganap at Pag-optimize
### Cut Optimization
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Buntot Recursion
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Checklist ng Pag-optimize
| Teknik | Epekto | Paglalarawan |
|-----------|--------|-------------|
| **Tail recursion** | Mataas | Gumamit ng mga accumulator para sa patuloy na espasyo ng stack |
| **Gupitin (berde)** | Mataas | Tanggalin ang mga hindi kinakailangang pagpipiliang puntos |
| **Tabled evaluation** | Mataas |  Ang`:- table pred/N`ay nagme-memoize ng mga resulta |
| **Pag-i-index** | Katamtaman | Ilagay muna ang mapang-akit na argumento |
| **Mga listahan ng pagkakaiba** | Katamtaman | O(1) list concatenation |
| **CLP(FD) over generate-test** | Napakataas | Gumamit ng mga hadlang sa halip na brute-force |
---

## Deployment at Real-World na Paggamit
### Pag-deploy ng Mga Prolog na Application
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Mga Real-World na Application
| Domain | Paano Ginagamit ang Prolog | Halimbawa |
|--------|--------------------|---------|
| **Mga ekspertong system** | Medikal na pagsusuri, pagtuklas ng kasalanan | MYCIN, XCON |
| **NLP** | Grammar parsing, semantic analysis | Chatbots, QA system |
| **Uri ng hinuha** | Pagsusuri ng uri ng Hindley-Milner | Haskell/ML prototypes |
| **Pag-iiskedyul** | Pag-iiskedyul ng empleyado, timetabling | Pag-iskedyul ng crew ng airline |
| **Legal na pangangatwiran** | Batay sa panuntunan legal na pagsusuri | Pagsusuri ng pagsunod |
| **Pagtatanong sa database** | Datalog para sa pagsusuri ng data | Soufflé engine |
| **Pagpapatunay** | Pagsusuri ng modelo | Pag-verify ng hardware |
| **IBM Watson** | Natural na pag-unawa sa wika | Panganib! sistema |
| **Ericsson** | Pamamahala ng telecom | Pagpapatunay ng network config |
---

## Kailan Gamitin ang Prolog
| Sitwasyon | Bakit Prolog | Mas mahusay na Alternatibo |
|----------|-----------|-------------------|
| Batay sa panuntunan na pangangatwiran | Ang prolog ay binuo para dito | Mga custom na rule engine sa Python/Java |
| Pinipigilang kasiyahan | Ang CLP(FD) ay elegante at mahusay | Mga solver ng SAT, OR-Tools para sa malalaking pagkakataon |
| Grammar / pag-parse ng wika | Ang DCG (Definite Clause Grammar) ay katutubong | Mga generator ng parser (ANTLR, yacc) para sa produksyon |
| Mga dalubhasang sistema | Natural na akma — mga katotohanan + panuntunan = sistema ng dalubhasa | Mga makina ng panuntunan sa negosyo (Drools) |
| Pag-iiskedyul / timetabling | Mahusay na nalutas ng CLP ang mga ito | OR-Tools, OptaPlanner |
| Uri ng system research | Ang pagkakaisa ay ang pundasyon | Ipatupad sa OCaml, Haskell, Rust |
| Mga web application | Hindi angkop | Python, Node.js, Go |
| Data science / ML | Hindi ang ecosystem | Python, R |
| Code na kritikal sa pagganap | Ang prolog ay mabagal para sa pagkalkula | C, C++, kalawang |
| Pangkalahatang layunin na programming | Posible ngunit awkward | Python, Go, Java |
---

## Synthetic na Q&A
### Q1: Paano naiiba ang pagkakaisa ng Prolog sa pagtatalaga sa ibang mga wika?
**A:** Ang pag-iisa ay bidirectional pattern na pagtutugma, hindi pagtatalaga:
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

### Q2: Paano gumagana ang backtracking sa Prolog?
**A:** Kapag nabigo ang isang layunin, babalik ang Prolog sa huling pagpipiliang punto at susubukan ang susunod na alternatibo:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: Paano ako gagana sa mga listahan sa Prolog?
**A:** Gumagamit ang mga listahan na tumutugma sa pattern ng ulo/buntot:
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

### Q4: Kailan ko dapat gamitin ang Prolog sa halip na ibang mga wika?
**A:** Mahusay ang prolog sa:
- Kasiyahan sa pagpilit (pag-iskedyul, mga palaisipan)
- Mga sistemang nakabatay sa panuntunan (mga sistema ng eksperto, pagpapatunay)
- Graph/paglalakbay sa puno
- Natural na pagproseso ng wika
- Simbolikong pagkalkula
- Anumang problema na maipahayag bilang lohikal na relasyon
### Q5: Ano ang mga karaniwang pitfalls sa Prolog?
**S:** Mga pangunahing isyu:
- Infinite recursion — laging unahin ang base case
- Hindi sinasadyang backtracking — gamitin ang cut`!`o`once/1`
- Nangyayari ang pagsusuri —`X = f(X)`loops bilang default (gamitin ang`unify_with_occurs_check`)
- Green cuts (optimization) vs red cuts (change meaning) — mas gusto ang green
---

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Paglutas ng N-Queens Puzzle
**Hakbang 1: Unawain ang Problema**
Ilagay ang N reyna sa isang NxN chessboard para walang dalawang reyna ang mag-atake sa isa't isa.
**Hakbang 2: Tukuyin ang Diskarte**
Gumamit ng henerasyong nakabatay sa hadlang: ilagay ang mga reyna sa bawat hanay, pagsuri sa kaligtasan.
**Hakbang 3: Ipatupad**```prolog
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

**Hakbang 4: I-verify**
 Ang`?- n_queens(8, Qs).`ay dapat makahanap ng 92 na solusyon.
### Problema 2: Pagbuo ng Simple Expert System
**Hakbang 1: Unawain ang Problema**
I-diagnose ang mga problema sa sasakyan batay sa mga sintomas.
**Hakbang 2: Tukuyin ang Diskarte**
Gumamit ng mga panuntunan sa Prolog para i-encode ang kaalaman sa diagnostic.
**Hakbang 3: Ipatupad**```prolog
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

**Hakbang 4: Palawakin**
Magdagdag ng mga marka ng kumpiyansa, magtanong sa user ng mga sintomas nang interactive, at mga chain diagnose.
---

## Buod
Ang prolog ay hindi katulad ng ibang programming language. Sa halip na magsulat ng sunud-sunod na mga tagubilin, inilalarawan mo ang mga relasyon at mga hadlang — at ang makina ay naghahanap ng mga solusyon sa pamamagitan ng lohikal na hinuha. Ginagawa nitong perpekto ang Prolog para sa mga problemang awkward o verbose sa mga mahahalagang wika: mga sistema ng eksperto, pag-iiskedyul, pag-parse ng grammar, kasiyahan sa pagpilit, at anumang may kinalaman sa mga lohikal na panuntunan. Karamihan sa mga programmer ay hindi kailanman gagamit ng Prolog sa produksyon, ngunit ang pag-aaral nito ay nagpapalawak ng iyong pag-iisip tungkol sa kung ano ang maaaring maging programming. Ang unification, backtracking, at declarative problem specification ay mga konseptong nakakaimpluwensya sa disenyo ng wika, AI research, at maging sa database query optimization.
### Paghahambing ng Prolog Engine
| Tampok | SWI-Prolog | Prolog ng GNU | Tau Prolog |
|---------|-----------|------------|------------|
| **Lisensya** | BSD (open source) | GPL (open source) | BSD (open source) |
| **Platform** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (browser) |
| **CLP(FD)** | Built-in na library | Built-in | Hindi magagamit |
| **Suporta ng DCG** | Buong | Buong | Limitado |
| **Tabling** | Oo | Hindi | Hindi |
| **FFI (C na mga tawag)** | Oo | Oo | Sa pamamagitan ng JavaScript |
| **Networking** | HTTP, TCP, TLS | TCP | Sa pamamagitan ng JavaScript |
| **Multi-threading** | Oo | Hindi | Hindi |
| **Package manager** | `pack_install/1`| Wala | npm |
| **Pinakamahusay para sa** | Produksyon, pananaliksik | Paglutas ng hadlang | Web apps, edukasyon |
### Mga Web Application na may Pengines
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

### Metaprogramming na may assert/retract
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
