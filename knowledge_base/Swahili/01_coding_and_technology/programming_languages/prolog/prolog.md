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

# Prolog
Prolog (Programing in Logic) ni lugha ya programu ya kimantiki iliyoundwa mnamo 1972 na Alain Colmerauer na Philippe Roussel. Tofauti na lugha nyingine zote kwenye orodha hii, Prolog haiambii kompyuta *jinsi* ya kutatua tatizo — unatangaza *kile* ni kweli (ukweli na sheria), na injini ya uelekezaji ya Prolog hutafuta jibu kupitia makato ya kimantiki.
Prolog ilikuwa lugha ya chaguo kwa mifumo ya wataalamu, usindikaji wa lugha asilia, na utafiti wa AI katika miaka ya 1980. Iliendesha mradi wa Mfumo wa Kompyuta wa Kizazi cha Tano wa Japani na ilitumiwa katika Watson ya IBM kwa uelewa wa lugha asilia. Leo, Prolog inatumika katika kutatua vizuizi, kuratibu, aina ya makisio, hoja za kisheria, na mahali popote matatizo yanaonyeshwa kama mahusiano ya kimantiki.
**Upangaji wa Mantiki ya Vikwazo (CLP)** huongeza Prolog na vitatuzi vya vikwazo vya kuratibu, kuelekeza na kugawa rasilimali - matatizo ambayo ni magumu sana katika lugha za lazima.
---

## Kwa Nini Utangulizi Ni Muhimu
- **Programu za kutangaza**: Eleza kilicho kweli, si jinsi ya kukikokotoa. Injini hufanya kazi.
- **Ulinganishaji wa muundo na muunganisho**: Kanuni ya muunganisho ya Prolog ina nguvu zaidi kuliko kulinganisha muundo katika lugha zingine.
- **Utafutaji wa nyuma**: Huchunguza kiotomatiki masuluhisho yote yanayowezekana. Hakuna algoriti za utafutaji unaohitajika.
- **Asili kwa matatizo ya mantiki**: Mifumo ya kitaalam, injini za sheria, vikagua aina, vichanganuzi vya sarufi - ramani hizi moja kwa moja kwenye Prolog.
- **Utatuzi wa vikwazo**: CLP(FD) hutatua kuratibu, ugawaji na matatizo ya ujumuishaji kwa umaridadi.
- **Kufikiri tofauti**: Hoja ya Kujifunza inabadilisha jinsi unavyoshughulikia utatuzi wa matatizo - unaanza kufikiria katika mahusiano na vikwazo.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Mtazamo tofauti sana** | Hakuna vigezo (vifungo pekee), hakuna vitanzi, hakuna kazi | Fikiria katika mahusiano na kujirudia, si mabadiliko ya hali |
| **Utendaji** | Polepole kwa hesabu za nambari na data kubwa | Tumia kwa hoja; tuma hesabu kwa C/lugha zingine |
| **Ugumu wa kurekebisha** | Ni vigumu kufuatilia kurudi nyuma na kushindwa kuungana | Tumia zana za kufuatilia/kutatua; andika viambishi bainishi |
| **Kata opereta (!)** | Inahitajika kwa ufanisi lakini inavunja usafi wa kimantiki | Tumia kama-basi-mwingine au tathmini iliyowasilishwa kwenye meza inapowezekana |
| **Mfumo mdogo wa ikolojia** | Maktaba chache, mifumo, au rasilimali za jumuiya | SWI-Prolog ndio utekelezaji kamili zaidi |
| **Si kwa programu za jumla** | Wavuti, rununu, GUI - sio nguvu ya Prolog | Tumia kama injini ya hoja nyuma ya programu ya wavuti |
---

## Misingi ya Sintaksia
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

## Sintaksia na Miundo ya Kina
### Dive ya Kuunganisha Kina
Kuunganisha ni utaratibu wa msingi wa Prolog - ni jinsi Prolog "inalingana" na masharti na kuunganisha vigezo.
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

### Ufuatiliaji Nyuma na Pointi za Chaguo
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

### Sarufi za Kifungu Dhahiri (DCGs)
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

### Upangaji wa Mantiki ya Vikwazo (CLP)
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

## Usanifu na Usanifu wa Mfumo
### Kielelezo cha Kuandaa Mantiki
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

### Muundo wa Kawaida wa Mradi
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

### Mfumo wa Moduli
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Usanidi wa SWI-Prolog
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

### Kuendesha Programu za Prog
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

### Unda Usanidi
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

## Majaribio na Utatuzi
### Ufuatiliaji Uliojengwa ndani
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

### Jaribio la Kitengo na PLUnit
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

### Miundo ya Kawaida ya Utatuzi
| Tatizo | Dalili | Suluhisho |
|---------|---------------------|
| Urudiaji usio na kikomo | Kufurika kwa rafu | Angalia kesi ya msingi; ongeza hali ya kusitisha |
| Hakuna suluhu | Hoja inarejesha sivyo | Angalia mpangilio wa instantiation tofauti |
| Suluhu nyingi mno | Nakala zisizotarajiwa | Ongeza kata (!) au tumia`setof`|
| Muungano usio sahihi | Vigezo vimefungwa vibaya | Tumia`=`kujaribu; angalia kazi ya kiutendaji |
| Suala la utendaji | Utekelezaji wa polepole | Ongeza kupunguzwa; tumia`table`; angalia alama za chaguo |
---

## Kuingiliana
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

### Muunganisho wa Chatu
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

## Miundo ya Kubuni
### Mchoro wa 1: Kikusanyaji (Kurudisha Mkia)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Mchoro wa 2: Ubadilishaji wa Hali```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Mchoro wa 3: Tengeneza na Ujaribu```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Mchoro wa 4: Orodha za Tofauti```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Utendaji na Uboreshaji
### Kata Uboreshaji
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Kujirudia kwa Mkia
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Orodha ya Hakiki ya Uboreshaji
| Mbinu | Athari | Maelezo |
|-----------|--------|-------------|
| **Marudio ya mkia** | Juu | Tumia vilimbikizi kwa nafasi ya kutundika kila wakati |
| **Kata (kijani)** | Juu | Ondoa alama za chaguo zisizo za lazima |
| **Tathmini ya jedwali** | Juu | `:- table pred/N`hukariri matokeo |
| **Kuashiria** | Kati | Weka hoja ya kibaguzi kwanza |
| **Orodha za tofauti** | Kati | O(1) muunganisho wa orodha |
| **CLP(FD) juu ya jaribio la kuzalisha** | Juu Sana | Tumia vizuizi badala ya brute-force |
---

## Usambazaji na Matumizi Halisi ya Ulimwenguni
### Inapeleka Programu za Prog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Maombi ya Ulimwengu Halisi
| Kikoa | Jinsi Prolog Inatumika | Mfano |
|--------|------------------------------|
| **Mifumo ya kitaalam** | Utambuzi wa kimatibabu, utambuzi wa makosa | MYCIN, XCON |
| **NLP** | Uchanganuzi wa sarufi, uchanganuzi wa kisemantiki | Chatbots, mifumo ya QA |
| **Aina ya makisio** | aina ya Hindley-Milner kuangalia | Prototypes za Haskell/ML |
| **Kuratibu** | Ratiba ya wafanyikazi, ratiba | Ratiba ya wafanyakazi wa shirika la ndege |
| **Mawazo ya kisheria** | Uchambuzi wa kisheria unaotegemea kanuni | Ukaguzi wa kufuata |
| **Kuuliza kwenye hifadhidata** | Datalogi kwa uchambuzi wa data | Injini ya Souffle |
| **Uthibitishaji** | Kuangalia mfano | Uthibitishaji wa maunzi |
| **IBM Watson** | Uelewa wa lugha asilia | Hatari! mfumo |
| **Ericsson** | Usimamizi wa mawasiliano ya simu | Uthibitishaji wa usanidi wa mtandao |
---

## Wakati wa kutumia Prolog
| Hali | Kwa nini Prolog | Mbadala Bora |
|----------|-----------|-------------------|
| Mawazo yanayotegemea kanuni | Prolog imeundwa kwa hii | Injini za sheria maalum katika Python/Java |
| Kuridhika kwa vikwazo | CLP(FD) ni maridadi na bora | Vitatuzi vya SAT, AU-Zana kwa matukio makubwa |
| Sarufi / uchanganuzi wa lugha | DCG (Sarufi Dhahiri za Kifungu) ni asili | Jenereta za vichanganuzi (ANTLR, yacc) kwa ajili ya uzalishaji |
| Mifumo ya kitaalam | Inafaa asili - ukweli + sheria = mfumo wa kitaalam | Injini za sheria za biashara (Drools) |
| Kupanga/kuweka ratiba | CLP hutatua haya vizuri | AU-Zana, OptaPlanner |
| Andika utafiti wa mfumo | Umoja ni msingi | Tekeleza katika OCaml, Haskell, Rust |
| Programu za wavuti | Haifai | Python, Node.js, Nenda |
| Sayansi ya data / ML | Sio mfumo wa ikolojia | Chatu, R |
| Msimbo muhimu wa utendaji | Prolog ni polepole kwa hesabu | C, C++, Kutu |
| Upangaji wa madhumuni ya jumla | Inawezekana lakini mbaya | Python, Nenda, Java |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Je, muunganisho wa Prolog unatofautiana vipi na mgawo katika lugha zingine?
**J:** Muunganisho ni ulinganifu wa muundo wa pande mbili, si kazi:
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

### Q2: Kurudisha nyuma kunafanyaje kazi katika Prolog?
**J:** Lengo linaposhindikana, Prolog inarudi nyuma hadi chaguo la mwisho na kujaribu njia mbadala ifuatayo:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: Je, ninafanyaje kazi na orodha katika Prolog?
**J:** Orodha hutumia ulinganifu wa muundo wa kichwa/mkia:
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

### Q4: Je, ni lini nitumie Prolog badala ya lugha zingine?
**A:** Prolog inafaulu katika:
- Kuridhika kwa kizuizi (ratiba, mafumbo)
- Mifumo ya msingi (mifumo ya kitaalam, uthibitisho)
- Upitishaji wa grafu/mti
- Usindikaji wa lugha asilia
- Mahesabu ya ishara
- Shida yoyote inayoonyeshwa kama uhusiano wa kimantiki
### Q5: Je, ni mitego gani ya kawaida katika Prolog?
**J:** Masuala muhimu:
- Urejeshaji usio na mwisho - kila wakati weka kesi ya msingi kwanza
- Urejeshaji nyuma usiotarajiwa - tumia kata`!`au`once/1`
- Hutokea hundi -`X = f(X)`vitanzi kwa chaguo-msingi (tumia `unify_with_occurs_check`)
- Vipunguzo vya kijani (kuboresha) dhidi ya vipunguzi vyekundu (badilisha maana) - pendelea kijani
---

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Kutatua Fumbo la N-Queens
**Hatua ya 1: Elewa Tatizo**
Weka N malkia kwenye ubao wa chess wa NxN ili malkia wawili wasishambuliane.
**Hatua ya 2: Tambua Mbinu**
Tumia kizazi kinachotegemea vikwazo: weka safu kwa safu wima, angalia usalama.
**Hatua ya 3: Tekeleza**```prolog
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

**Hatua ya 4: Thibitisha**
`?- n_queens(8, Qs).`inapaswa kupata suluhu 92.
### Tatizo la 2: Kujenga Mfumo Rahisi wa Kitaalam
**Hatua ya 1: Elewa Tatizo**
Tambua matatizo ya gari kulingana na dalili.
**Hatua ya 2: Tambua Mbinu**
Tumia sheria za Prolog kusimba maarifa ya uchunguzi.
**Hatua ya 3: Tekeleza**```prolog
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

**Hatua ya 4: Panua**
Ongeza alama za kujiamini, muulize mtumiaji dalili kwa maingiliano, na utambuzi wa msururu.
---

## Muhtasari
Prolog ni tofauti na lugha nyingine yoyote ya programu. Badala ya kuandika maagizo ya hatua kwa hatua, unaelezea uhusiano na vikwazo - na injini hutafuta suluhu kupitia uelekezaji wa kimantiki. Hii inafanya Prolog bora kwa matatizo ambayo ni ya kutatanisha au kitenzi katika lugha muhimu: mifumo ya wataalamu, uratibu, uchanganuzi wa sarufi, utoshelevu wa kikwazo, na chochote kinachohusisha sheria za kimantiki. Watengenezaji programu wengi hawatawahi kutumia Prolog katika uzalishaji, lakini kujifunza kunapanua mawazo yako juu ya programu inaweza kuwa nini. Muunganisho, urejeshaji nyuma, na ubainishaji wa tatizo la kutangaza ni dhana zinazoathiri muundo wa lugha, utafiti wa AI, na hata uboreshaji wa hoja za hifadhidata.
### Prolog Engines Comparison
| Kipengele | SWI-Prolog | Utangulizi wa GNU | Tau Prolog |
|---------|-----------|------------|------------|
| **Leseni** | BSD (chanzo wazi) | GPL (chanzo wazi) | BSD (chanzo wazi) |
| **Jukwaa** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (kivinjari) |
| **CLP(FD)** | Maktaba iliyojengwa ndani | Imejengwa ndani | Haipatikani |
| **Msaada wa DCG** | Kamili | Kamili | Kidogo |
| **Kuweka meza** | Ndiyo | Hapana | Hapana |
| **FFI (Simu C)** | Ndiyo | Ndiyo | Kupitia JavaScript |
| **Mtandao** | HTTP, TCP, TLS | TCP | Kupitia JavaScript |
| **Nyezi nyingi** | Ndiyo | Hapana | Hapana |
| **Kidhibiti kifurushi** | `pack_install/1`| Hakuna | npm |
| **Bora kwa** | Uzalishaji, utafiti | Utatuzi wa vikwazo | Programu za wavuti, elimu |
### Programu za Wavuti zilizo na Pengines
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

### Kupanga programu kwa kusisitiza/kataa
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
