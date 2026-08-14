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
# Prolog
Prolog (Programming in Logic) to język programowania logicznego stworzony w 1972 roku przez Alaina Colmerauera i Philippe'a Roussela. W przeciwieństwie do wszystkich innych języków na tej liście, Prolog nie mówi komputerowi *jak* rozwiązać problem — deklarujesz, *co* jest prawdą (fakty i reguły), a silnik wnioskowania Prologu znajduje odpowiedź poprzez logiczną dedukcję.
Prolog był językiem wybieranym w latach 80. w systemach ekspertowych, przetwarzaniu języka naturalnego i badaniach nad sztuczną inteligencją. Zasilał japoński projekt systemu komputerowego piątej generacji i był używany w komputerze Watson firmy IBM do rozumienia języka naturalnego. Obecnie Prolog jest używany do rozwiązywania ograniczeń, planowania, wnioskowania o typach, rozumowania prawnego i wszędzie tam, gdzie problemy są naturalnie wyrażane w postaci relacji logicznych.
**Constraint Logic Programming (CLP)** rozszerza Prolog o narzędzia do rozwiązywania ograniczeń do planowania, routingu i alokacji zasobów – problemy, które są niezwykle trudne w językach imperatywnych.
---

## Dlaczego Prolog ma znaczenie
- **Programowanie deklaratywne**: Opisz, co jest prawdą, a nie jak to obliczyć. Silnik robi robotę.
- **Dopasowywanie i unifikacja wzorców**: Algorytm unifikacji Prologu jest potężniejszy niż dopasowywanie wzorców w innych językach.
- **Wyszukiwanie wstecz**: Automatycznie bada wszystkie możliwe rozwiązania. Nie są potrzebne żadne ręczne algorytmy wyszukiwania.
- **Naturalne w przypadku problemów logicznych**: Systemy ekspertowe, silniki reguł, moduły sprawdzania typów, analizatory gramatyki — te mapują się bezpośrednio do Prologu.
- **Rozwiązywanie ograniczeń**: CLP(FD) elegancko rozwiązuje problemy związane z planowaniem, alokacją i kombinatoryką.
- **Inne myślenie**: Nauka Prologu zmienia sposób, w jaki podchodzisz do rozwiązywania problemów — zaczynasz myśleć w kategoriach relacji i ograniczeń.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Bardzo inny paradygmat** | Żadnych zmiennych (tylko powiązania), żadnych pętli, żadnych przypisań | Myśl w kategoriach relacji i rekurencji, a nie zmian stanu |
| **Wydajność** | Powolne w przypadku obliczeń numerycznych i dużych danych | Użyj do rozumowania; delegowanie obliczeń do C/innych języków |
| **Trudność debugowania** | Trudno wyśledzić błędy związane z wycofywaniem się i unifikacją | Użyj narzędzi do śledzenia/debugowania; zapisz predykaty deterministyczne |
| **Operator cięcia (!)** | Potrzebne dla wydajności, ale łamie logiczną czystość | Jeśli to możliwe, użyj oceny typu „jeśli-to-else” lub złożonej |
| **Ograniczony ekosystem** | Niewiele bibliotek, frameworków lub zasobów społeczności | SWI-Prolog jest najbardziej kompletną implementacją |
| **Nie dla aplikacji ogólnych** | Sieć, urządzenia mobilne, GUI — nie mocna strona Prologu | Użyj jako silnika wnioskowania aplikacji internetowej |
---

## Podstawy składni
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

## Zaawansowana składnia i wzorce
### Głębokie nurkowanie zjednoczone
Ujednolicenie jest podstawowym mechanizmem Prologa — w ten sposób Prolog „dopasowuje” terminy i wiąże zmienne.
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

### Cofanie się i punkty wyboru
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

### Gramatyki zdań oznaczonych (DCG)
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

### Programowanie logiczne z ograniczeniami (CLP)
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

## Architektura i projektowanie systemów
### Paradygmat programowania logicznego
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

### Typowa struktura projektu
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

### System modułowy
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

## Konfiguracja projektu i budowanie systemu
### Konfiguracja SWI-Prolog
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

### Uruchamianie programów Prolog
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

### Utwórz konfigurację
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

## Testowanie i debugowanie
### Wbudowane śledzenie
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

### Testowanie jednostkowe za pomocą PLUnit
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

### Typowe wzorce debugowania
| Problem | Objaw | Rozwiązanie |
|--------|---------|---------|
| Nieskończona rekurencja | Przepełnienie stosu | Sprawdź obudowę podstawową; dodaj warunek zakończenia |
| Brak rozwiązań | Zapytanie zwraca fałsz | Sprawdź kolejność instancji zmiennej |
| Za dużo rozwiązań | Nieoczekiwane duplikaty | Dodaj wycięcie (!) lub użyj`setof`|
| Błędne zjednoczenie | Zmienne powiązane niepoprawnie | Użyj`=`do przetestowania; sprawdź arność funktora |
| Problem z wydajnością | Powolna realizacja | Dodaj kawałki; użyj`table`; sprawdź punkty wyboru |
---

## Interoperacyjność
### Interfejs C (FFI)
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

### Integracja z Pythonem
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

## Wzorce projektowe
### Wzorzec 1: Akumulator (rekurencja ogona)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Wzorzec 2: Wątkowanie stanu```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Wzorzec 3: Generuj i testuj```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Wzór 4: Listy różnic```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Wydajność i optymalizacja
### Optymalizacja cięcia
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Rekurencja ogona
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Lista kontrolna optymalizacji
| Technika | Wpływ | Opis |
|---------------|--------|------------|
| **Rekursja ogona** | Wysoki | Użyj akumulatorów dla stałej przestrzeni stosu |
| **Cięcie (zielony)** | Wysoki | Wyeliminuj niepotrzebne punkty wyboru |
| **Przedstawiona ocena** | Wysoki | `:- table pred/N`zapamiętuje wyniki |
| **Indeksowanie** | Średni | Na pierwszym miejscu umieść argument różnicujący |
| **Listy różnic** | Średni | Konkatenacja list O(1) |
| **CLP(FD) podczas testu generowania** | Bardzo wysoki | Użyj ograniczeń zamiast brutalnej siły |
---

## Wdrożenie i użytkowanie w świecie rzeczywistym
### Wdrażanie aplikacji Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Aplikacje w świecie rzeczywistym
| Domena | Jak używany jest Prolog | Przykład |
|--------|---------|--------|
| **Systemy eksperckie** | Diagnostyka medyczna, wykrywanie usterek | MYCYNA, XCON |
| **NLP** | Analiza gramatyczna, analiza semantyczna | Chatboty, systemy kontroli jakości |
| **Wnioskowanie o typie** | Sprawdzanie typu Hindley-Milner | Prototypy Haskell/ML |
| **Planowanie** | Planowanie pracy pracowników, harmonogram | Harmonogram pracy załogi linii lotniczych |
| **Uzasadnienie prawne** | Analiza prawna oparta na zasadach | Sprawdzanie zgodności |
| **Zapytanie bazy danych** | Datalog do analizy danych | Silnik sufletowy |
| **Weryfikacja** | Sprawdzanie modelu | Weryfikacja sprzętu |
| **IBM Watson** | Rozumienie języka naturalnego | Niebezpieczeństwo! systemu |
| **Ericsson** | Zarządzanie telekomunikacją | Weryfikacja konfiguracji sieci |
---

## Kiedy używać Prologu
| Scenariusz | Dlaczego Prolog | Lepsza alternatywa |
|---------|-----------|--------------------------------|
| Rozumowanie oparte na regułach | Prolog jest do tego stworzony | Niestandardowe silniki reguł w Pythonie/Java |
| Spełnienie ograniczeń | CLP(FD) jest elegancki i wydajny | Solvery SAT, narzędzia OR dla dużych instancji |
| Analiza gramatyki / języka | DCG (gramatyki zdań oznaczonych) są natywne | Generatory parserów (ANTLR, yacc) na produkcję |
| Systemy ekspertowe | Naturalne dopasowanie — fakty + zasady = system ekspertowy | Silniki reguł biznesowych (Drools) |
| Planowanie / harmonogram | CLP dobrze je rozwiązuje | Narzędzia OR, OptaPlanner |
| Wpisz badania systemowe | Ujednolicenie to podstawa | Zaimplementuj w OCaml, Haskell, Rust |
| Aplikacje internetowe | Nie nadaje się | Python, Node.js, Go |
| Nauka o danych / ML | Nie ekosystem | Python, R |
| Kod krytyczny dla wydajności | Prolog jest powolny w obliczeniach | C, C++, rdza |
| Programowanie ogólnego przeznaczenia | Możliwe, ale niezręczne | Python, Go, Java |
---

## Syntetyczne pytania i odpowiedzi
### P1: Czym różni się ujednolicenie w Prologu od przypisania w innych językach?
**O:** Ujednolicenie to dwukierunkowe dopasowywanie wzorców, a nie przypisywanie:
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

### P2: Jak działa backtracking w Prologu?
**A:** Kiedy cel nie powiedzie się, Prolog cofa się do ostatniego punktu wyboru i wypróbowuje następną alternatywę:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### P3: Jak pracować z listami w Prologu?
**A:** Listy wykorzystują dopasowanie wzorca głowy/ogona:
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

### P4: Kiedy powinienem używać Prologu zamiast innych języków?
**A:** Prolog wyróżnia się w:
- Spełnianie ograniczeń (harmonogram, łamigłówki)
- Systemy oparte na regułach (systemy eksperckie, walidacja)
- Przechodzenie przez wykres/drzewo
- Przetwarzanie języka naturalnego
- Obliczenia symboliczne
- Dowolny problem, który można wyrazić w postaci relacji logicznych
### P5: Jakie są typowe pułapki w Prologu?
**O:** Kluczowe kwestie:
- Nieskończona rekurencja — zawsze stawiaj przypadek podstawowy na pierwszym miejscu
- Niezamierzone cofanie się — użyj cięcia`!`lub`once/1`
- Występuje sprawdzenie — domyślnie pętle`X = f(X)`(użyj`unify_with_occurs_check`)
- Zielone cięcia (optymalizacja) vs czerwone cięcia (zmiana znaczenia) - preferuj kolor zielony
---

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Rozwiązanie zagadki N-królowych
**Krok 1: Zrozum problem**
Umieść N hetmanów na szachownicy NxN, tak aby żadne dwie hetmany nie atakowały się nawzajem.
**Krok 2: Zidentyfikuj podejście**
Użyj generowania opartego na ograniczeniach: umieszczaj królowe kolumna po kolumnie, sprawdzając bezpieczeństwo.
**Krok 3: Wdróż**```prolog
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

**Krok 4: Zweryfikuj**
`?- n_queens(8, Qs).`powinien znaleźć 92 rozwiązania.
### Problem 2: Budowa prostego systemu ekspertowego
**Krok 1: Zrozum problem**
Diagnozuj problemy z samochodem na podstawie objawów.
**Krok 2: Zidentyfikuj podejście**
Użyj reguł Prologu do kodowania wiedzy diagnostycznej.
**Krok 3: Wdróż**```prolog
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

**Krok 4: Przedłuż**
Dodawaj oceny pewności, interaktywnie pytaj użytkownika o objawy i diagnozuj łańcuchowo.
---

## Streszczenie
Prolog różni się od innych języków programowania. Zamiast pisać instrukcje krok po kroku, opisujesz zależności i ograniczenia, a silnik szuka rozwiązań poprzez logiczne wnioskowanie. To sprawia, że ​​Prolog jest idealny do problemów, które są niewygodne lub szczegółowe w językach imperatywnych: systemy ekspertowe, planowanie, analiza gramatyczna, spełnianie ograniczeń i wszystko, co wymaga reguł logicznych. Większość programistów nigdy nie użyje Prologu w środowisku produkcyjnym, ale poznanie go poszerza Twoje myślenie o tym, czym może być programowanie. Ujednolicenie, wycofywanie się i deklaratywna specyfikacja problemu to koncepcje, które wpływają na projektowanie języków, badania nad sztuczną inteligencją, a nawet optymalizację zapytań do baz danych.
### Porównanie silników Prologu
| Funkcja | SWI-Prolog | Prolog GNU | Tau Prolog |
|--------|-----------|------------|------------|
| **Licencja** | BSD (otwarte oprogramowanie) | GPL (otwarte oprogramowanie) | BSD (otwarte oprogramowanie) |
| **Platforma** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (przeglądarka) |
| **CLP(FD)** | Wbudowana biblioteka | Wbudowany | Niedostępne |
| **Wsparcie DCG** | Pełny | Pełny | ograniczona |
| **Składanie** | Tak | Nie | Nie |
| **FFI (połączenia C)** | Tak | Tak | Przez JavaScript |
| **Sieć** | HTTP, TCP, TLS | TCP | Przez JavaScript |
| **Wielowątkowość** | Tak | Nie | Nie |
| **Menedżer pakietów** | `pack_install/1`| Brak | npm |
| **Najlepsze dla** | Produkcja, badania | Rozwiązywanie ograniczeń | Aplikacje internetowe, edukacja |
### Aplikacje internetowe z Penginami
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

### Metaprogramowanie z potwierdzeniem/wycofaniem
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
