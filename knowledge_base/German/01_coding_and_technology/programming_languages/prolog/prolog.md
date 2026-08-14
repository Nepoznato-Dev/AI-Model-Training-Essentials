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
Prolog (Programming in Logic) ist eine logische Programmiersprache, die 1972 von Alain Colmerauer und Philippe Roussel entwickelt wurde. Im Gegensatz zu allen anderen Sprachen auf dieser Liste sagt Prolog dem Computer nicht, *wie* er ein Problem lösen soll – Sie erklären, *was* wahr ist (Fakten und Regeln), und die Inferenz-Engine von Prolog ermittelt die Antwort durch logische Schlussfolgerung.
Prolog war in den 1980er Jahren die Sprache der Wahl für Expertensysteme, die Verarbeitung natürlicher Sprache und die KI-Forschung. Es trieb Japans Projekt zum Computersystem der fünften Generation voran und wurde in IBMs Watson für das Verständnis natürlicher Sprache verwendet. Heutzutage wird Prolog zum Lösen von Einschränkungen, zur Terminplanung, zur Typinferenz, zum rechtlichen Denken und überall dort verwendet, wo Probleme auf natürliche Weise als logische Beziehungen ausgedrückt werden.
**Constraint Logic Programming (CLP)** erweitert Prolog um Constraint-Löser für Planung, Routing und Ressourcenzuweisung – Probleme, die in imperativen Sprachen äußerst schwierig sind.
---

## Warum Prolog wichtig ist
- **Deklarative Programmierung**: Beschreiben Sie, was wahr ist, nicht wie man es berechnet. Der Motor erledigt die Arbeit.
- **Mustervergleich und -vereinheitlichung**: Der Vereinheitlichungsalgorithmus von Prolog ist leistungsfähiger als der Mustervergleich in anderen Sprachen.
- **Backtracking-Suche**: Erkundet automatisch alle möglichen Lösungen. Keine manuellen Suchalgorithmen erforderlich.
- **Natürlich für Logikprobleme**: Expertensysteme, Regel-Engines, Typprüfer, Grammatikparser – diese werden direkt auf Prolog abgebildet.
- **Constraint-Lösung**: CLP(FD) löst Planungs-, Zuordnungs- und kombinatorische Probleme auf elegante Weise.
- **Anderes Denken**: Das Erlernen von Prolog verändert Ihre Herangehensweise an die Problemlösung – Sie beginnen, in Beziehungen und Zwängen zu denken.
## Die Kompromisse
| Einschränkung | Einzelheiten | Typische Problemumgehung |
|-----------|---------|-----|
| **Sehr anderes Paradigma** | Keine Variablen (nur Bindungen), keine Schleifen, keine Zuweisungen | Denken Sie in Beziehungen und Rekursion, nicht in Zustandsänderungen |
| **Leistung** | Langsam für numerische Berechnungen und große Datenmengen | Zur Begründung verwenden; Berechnung an C/andere Sprachen delegieren |
| **Debugging-Schwierigkeit** | Rückschritte und Vereinheitlichungsfehler sind schwer nachzuvollziehen | Verwenden Sie Trace-/Debug-Tools. deterministische Prädikate schreiben |
| **Cut-Operator (!)** | Wird für die Effizienz benötigt, bricht aber die logische Reinheit | Wenn möglich, if-then-else oder tabellarische Auswertung verwenden |
| **Begrenztes Ökosystem** | Wenige Bibliotheken, Frameworks oder Community-Ressourcen | SWI-Prolog ist die vollständigste Implementierung |
| **Nicht für allgemeine Apps** | Web, Mobil, GUI – nicht die Stärke von Prolog | Verwendung als Argumentationsmotor hinter einer Web-App |
---

## Syntax-Grundlagen
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

## Erweiterte Syntax und Muster
### Deep Dive zur Vereinigung
Die Vereinheitlichung ist der Kernmechanismus von Prolog. Auf diese Weise „vergleicht“ Prolog Begriffe und bindet Variablen.
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

### Backtracking und Auswahlpunkte
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

### Definite-Satz-Grammatiken (DCGs)
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

### Constraint-Logic-Programmierung (CLP)
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

## Architektur und Systemdesign
### Logisches Programmierparadigma
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

### Typische Projektstruktur
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

### Modulsystem
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

## Projektkonfiguration und Build-System
### SWI-Prolog-Konfiguration
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

### Prolog-Programme ausführen
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

### Build-Konfiguration
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

## Testen und Debuggen
### Integrierte Ablaufverfolgung
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

### Unit-Test mit PLUnit
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

### Gängige Debugging-Muster
| Problem | Symptom | Lösung |
|---------|---------|----------|
| Unendliche Rekursion | Stapelüberlauf | Basisfall prüfen; Beendigungsbedingung hinzufügen |
| Keine Lösungen | Die Abfrage gibt „false“ zurück | Überprüfen Sie die Instanziierungsreihenfolge der Variablen |
| Zu viele Lösungen | Unerwartete Duplikate | Cut (!) hinzufügen oder`setof`| verwenden
| Falsche Vereinigung | Variablen falsch gebunden | Verwenden Sie`=`zum Testen. Funktionsarität prüfen |
| Leistungsproblem | Langsame Ausführung | Schnitte hinzufügen; verwenden Sie`table`; Auswahlpunkte prüfen |
---

## Interoperabilität
### C-Schnittstelle (FFI)
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

### Python-Integration
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

## Designmuster
### Muster 1: Akkumulator (Endrekursion)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Muster 2: State Threading```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Muster 3: Generieren und testen```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Muster 4: Differenzlisten```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Leistung und Optimierung
### Schnittoptimierung
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Schwanzrekursion
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Optimierungs-Checkliste
| Technik | Auswirkungen | Beschreibung |
|-----------|--------|-------------|
| **Tail-Rekursion** | Hoch | Verwenden Sie Akkumulatoren für konstanten Stapelplatz |
| **Schnitt (grün)** | Hoch | Eliminieren Sie unnötige Auswahlpunkte |
| **Tabellenbewertung** | Hoch | `:- table pred/N`speichert Ergebnisse |
| **Indizierung** | Mittel | Das diskriminierende Argument an die erste Stelle setzen |
| **Differenzlisten** | Mittel | O(1)-Listenverkettung |
| **CLP(FD) über Generate-Test** | Sehr hoch | Verwenden Sie Einschränkungen statt Brute-Force |
---

## Bereitstellung und reale Nutzung
### Bereitstellen von Prolog-Anwendungen
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Anwendungen aus der Praxis
| Domäne | Wie Prolog verwendet wird | Beispiel |
|--------|-----|---------|
| **Expertensysteme** | Medizinische Diagnose, Fehlererkennung | MYCIN, XCON |
| **NLP** | Grammatikanalyse, semantische Analyse | Chatbots, QS-Systeme |
| **Typinferenz** | Hindley-Milner-Typprüfung | Haskell/ML-Prototypen |
| **Planung** | Mitarbeitereinsatzplanung, Stundenplanerstellung | Planung der Flugbesatzung |
| **Rechtliche Begründung** | Regelbasierte Rechtsanalyse | Compliance-Prüfung |
| **Datenbankabfrage** | Datalog zur Datenanalyse | Soufflé-Motor |
| **Verifizierung** | Modellprüfung | Hardwareüberprüfung |
| **IBM Watson** | Verständnis natürlicher Sprache | Gefahr! System |
| **Ericsson** | Telekommunikationsmanagement | Validierung der Netzwerkkonfiguration |
---

## Wann man Prolog verwenden sollte
| Szenario | Warum Prolog | Bessere Alternative |
|----------|-----------|-------------------|
| Regelbasiertes Denken | Prolog wurde dafür entwickelt | Benutzerdefinierte Regel-Engines in Python/Java |
| Zufriedenheit mit Einschränkungen | CLP(FD) ist elegant und effizient | SAT-Löser, OR-Tools für große Instanzen |
| Grammatik-/Sprachanalyse | DCG (Definite Clause Grammars) sind nativ | Parser-Generatoren (ANTLR, yacc) für die Produktion |
| Expertensysteme | Natürliche Passform – Fakten + Regeln = Expertensystem | Geschäftsregel-Engines (Drools) |
| Terminplanung / Stundenplanerstellung | CLP löst diese gut | OP-Tools, OptaPlanner |
| Typsystemforschung | Vereinigung ist die Grundlage | Implementierung in OCaml, Haskell, Rust |
| Webanwendungen | Nicht geeignet | Python, Node.js, Go |
| Datenwissenschaft / ML | Nicht das Ökosystem | Python, R |
| Leistungskritischer Code | Prolog ist langsam für die Berechnung | C, C++, Rust |
| Allgemeine Programmierung | Möglich, aber umständlich | Python, Go, Java |
---

## Synthetische Fragen und Antworten
### F1: Wie unterscheidet sich die Vereinheitlichung von Prolog von der Zuweisung in anderen Sprachen?
**A:** Bei der Vereinheitlichung handelt es sich um einen bidirektionalen Mustervergleich, nicht um eine Zuweisung:
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

### F2: Wie funktioniert Backtracking in Prolog?
**A:** Wenn ein Ziel fehlschlägt, kehrt Prolog zum letzten Auswahlpunkt zurück und versucht die nächste Alternative:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### F3: Wie arbeite ich mit Listen in Prolog?
**A:** Listen verwenden Kopf-/Schwanzmustervergleich:
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

### F4: Wann sollte ich Prolog anstelle anderer Sprachen verwenden?
**A:** Prolog zeichnet sich aus durch:
- Zufriedenheit mit Einschränkungen (Terminplanung, Rätsel)
- Regelbasierte Systeme (Expertensysteme, Validierung)
- Graph-/Baumdurchquerung
- Verarbeitung natürlicher Sprache
- Symbolische Berechnung
- Jedes Problem, das als logische Beziehungen ausgedrückt werden kann
### F5: Was sind die häufigsten Fallstricke in Prolog?
**A:** Hauptthemen:
- Unendliche Rekursion – Stellen Sie immer den Basisfall an die erste Stelle
- Unbeabsichtigtes Backtracking – verwenden Sie den Schnitt`!`oder`once/1`
- Tritt bei der Prüfung auf – `X = f(X)`-Schleifen standardmäßig (verwenden Sie`unify_with_occurs_check`)
- Grüne Schnitte (Optimierung) vs. rote Schnitte (Bedeutung ändern) – bevorzugen Sie Grün
---

## Problemlösung in der Gedankenkette
### Problem 1: Das N-Queens-Rätsel lösen
**Schritt 1: Verstehen Sie das Problem**
Platzieren Sie N Damen auf einem NxN-Schachbrett, damit sich nicht zwei Damen gegenseitig angreifen.
**Schritt 2: Identifizieren Sie den Ansatz**
Verwenden Sie eine auf Einschränkungen basierende Generierung: Platzieren Sie die Königinnen Spalte für Spalte und überprüfen Sie die Sicherheit.
**Schritt 3: Implementieren**```prolog
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

**Schritt 4: Überprüfen**
`?- n_queens(8, Qs).`sollte 92 Lösungen finden.
### Problem 2: Aufbau eines einfachen Expertensystems
**Schritt 1: Verstehen Sie das Problem**
Diagnostizieren Sie Autoprobleme anhand der Symptome.
**Schritt 2: Identifizieren Sie den Ansatz**
Verwenden Sie Prolog-Regeln, um Diagnosewissen zu kodieren.
**Schritt 3: Implementieren**```prolog
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

**Schritt 4: Erweitern**
Fügen Sie Konfidenzwerte hinzu, fragen Sie den Benutzer interaktiv nach Symptomen und verketten Sie Diagnosen.
---

## Zusammenfassung
Prolog ist anders als jede andere Programmiersprache. Anstatt Schritt-für-Schritt-Anleitungen zu schreiben, beschreiben Sie Beziehungen und Einschränkungen – und die Engine sucht durch logische Schlussfolgerungen nach Lösungen. Dies macht Prolog ideal für Probleme, die in imperativen Sprachen umständlich oder ausführlich sind: Expertensysteme, Zeitplanung, Grammatikanalyse, Erfüllung von Einschränkungen und alles, was mit logischen Regeln zu tun hat. Die meisten Programmierer werden Prolog nie in der Produktion verwenden, aber das Erlernen von Prolog erweitert Ihr Denken darüber, was Programmieren sein kann. Vereinheitlichung, Backtracking und deklarative Problemspezifikation sind Konzepte, die das Sprachdesign, die KI-Forschung und sogar die Optimierung von Datenbankabfragen beeinflussen.
### Vergleich der Prolog-Engines
| Funktion | SWI-Prolog | GNU-Prolog | Tau-Prolog |
|---------|-----------|------------|------------|
| **Lizenz** | BSD (Open Source) | GPL (Open Source) | BSD (Open Source) |
| **Plattform** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (Browser) |
| **CLP(FD)** | Integrierte Bibliothek | Eingebaut | Nicht verfügbar |
| **DCG-Unterstützung** | Voll | Voll | Begrenzt |
| **Tablegung** | Ja | Nein | Nein |
| **FFI (C-Anrufe)** | Ja | Ja | Über JavaScript |
| **Netzwerk** | HTTP, TCP, TLS | TCP | Über JavaScript |
| **Multi-Threading** | Ja | Nein | Nein |
| **Paketmanager** | `pack_install/1`| Keine | npm |
| **Am besten für** | Produktion, Forschung | Einschränkungslösung | Web-Apps, Bildung |
### Webanwendungen mit Pengines
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

### Metaprogrammierung mit Assert/Retract
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
