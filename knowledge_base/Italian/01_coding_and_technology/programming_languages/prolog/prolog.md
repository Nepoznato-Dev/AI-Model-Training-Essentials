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

# Prologo
Prolog (Programming in Logic) è un linguaggio di programmazione logica creato nel 1972 da Alain Colmerauer e Philippe Roussel. A differenza di ogni altro linguaggio in questo elenco, Prolog non dice al computer *come* risolvere un problema: dichiari *cosa* è vero (fatti e regole) e il motore di inferenza di Prolog calcola la risposta attraverso la deduzione logica.
Prolog è stato il linguaggio preferito per i sistemi esperti, l'elaborazione del linguaggio naturale e la ricerca sull'intelligenza artificiale negli anni '80. Ha alimentato il progetto giapponese del sistema informatico di quinta generazione ed è stato utilizzato in Watson di IBM per la comprensione del linguaggio naturale. Oggi Prolog viene utilizzato nella risoluzione di vincoli, nella pianificazione, nell'inferenza dei tipi, nel ragionamento legale e ovunque i problemi siano naturalmente espressi come relazioni logiche.
**Constraint Logic Programming (CLP)** estende Prolog con risolutori di vincoli per la pianificazione, il routing e l'allocazione delle risorse, problemi estremamente difficili nei linguaggi imperativi.
---

## Perché Prolog è importante
- **Programmazione dichiarativa**: descrivi ciò che è vero, non come calcolarlo. Il motore fa il lavoro.
- **Corrispondenza e unificazione dei modelli**: l'algoritmo di unificazione di Prolog è più potente del confronto dei modelli in altri linguaggi.
- **Ricerca a ritroso**: esplora automaticamente tutte le possibili soluzioni. Non sono necessari algoritmi di ricerca manuale.
- **Naturale per i problemi di logica**: sistemi esperti, motori di regole, controllori di tipo, parser grammaticali: questi si associano direttamente a Prolog.
- **Risoluzione di vincoli**: CLP(FD) risolve elegantemente problemi di pianificazione, allocazione e combinatoria.
- **Pensiero diverso**: Learning Prolog cambia il modo in cui ti avvicini alla risoluzione dei problemi: inizi a pensare in base a relazioni e vincoli.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Paradigma molto diverso** | Nessuna variabile (solo associazioni), nessun ciclo, nessuna assegnazione | Pensare in relazione e ricorsione, non in cambiamenti di stato |
| **Prestazioni** | Lento per il calcolo numerico e dati di grandi dimensioni | Utilizzare per il ragionamento; delegare il calcolo a C/altri linguaggi |
| **Difficoltà di debug** | Difficile rintracciare i fallimenti di backtracking e di unificazione | Utilizzare strumenti di traccia/debug; scrivere predicati deterministici |
| **Operatore di taglio (!)** | Necessario per l'efficienza ma rompe la purezza logica | Utilizzare la valutazione if-then-else o tabellata quando possibile |
| **Ecosistema limitato** | Poche librerie, framework o risorse della comunità | SWI-Prolog è l'implementazione più completa |
| **Non per app generiche** | Web, mobile, GUI: non il punto di forza di Prolog | Utilizzare come motore di ragionamento dietro un'app Web |
---

## Fondamenti di sintassi
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

## Sintassi e modelli avanzati
### Approfondimento sull'Unificazione
L'unificazione è il meccanismo principale di Prolog: è il modo in cui Prolog "abbina" i termini e lega le variabili.
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

### Backtracking e punti di scelta
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

### Grammatiche delle clausole definite (DCG)
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

### Programmazione logica con vincoli (CLP)
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

## Architettura e progettazione di sistemi
### Paradigma della programmazione logica
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

### Struttura tipica del progetto
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

### Sistema di moduli
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

## Configurazione del progetto e sistema di creazione
### Configurazione SWI-Prolog
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

### Esecuzione di programmi Prolog
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

### Crea configurazione
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

## Test e debug
### Tracciamento integrato
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

### Test unitari con PLUnit
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

### Modelli di debug comuni
| Problema | Sintomo | Soluzione |
|---------|---------|----------|
| Ricorsione infinita | Overflow dello stack | Controllare il caso base; aggiungi condizione di terminazione |
| Nessuna soluzione | La query restituisce falso | Controlla l'ordine di istanziazione delle variabili |
| Troppe soluzioni | Duplicati imprevisti | Aggiungi taglio (!) o usa`setof`|
| Unificazione sbagliata | Variabili legate in modo errato | Utilizzare`=`per testare; controlla l'arietà del funtore |
| Problema di prestazioni | Esecuzione lenta | Aggiungi tagli; usa`table`; controlla i punti di scelta |
---

## Interoperabilità
### Interfaccia C (FFI)
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

### Integrazione con Python
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

## Modelli di progettazione
### Modello 1: Accumulatore (ricorsione della coda)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Modello 2: threading degli stati```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Modello 3: Genera e testa```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Modello 4: Elenchi di differenze```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Prestazioni e ottimizzazione
### Ottimizzazione del taglio
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Ricorsione della coda
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Elenco di controllo per l'ottimizzazione
| Tecnica | Impatto | Descrizione |
|-----------|--------|-----|
| **Riricorsione della coda** | Alto | Utilizzare gli accumulatori per uno spazio di stack costante |
| **Taglia (verde)** | Alto | Eliminare i punti di scelta non necessari |
| **Valutazione tabellare** | Alto | `:- table pred/N`memorizza i risultati |
| **Indicizzazione** | Medio | Metti prima l'argomento discriminante |
| **Elenchi di differenze** | Medio | O(1) concatenazione di elenchi |
| **CLP(FD) su generazione-test** | Molto alto | Usa i vincoli invece della forza bruta |
---

## Distribuzione e utilizzo nel mondo reale
### Distribuzione delle applicazioni Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Applicazioni nel mondo reale
| Dominio | Come viene utilizzato Prolog | Esempio |
|--------|-----|---------|
| **Sistemi esperti** | Diagnosi medica, rilevamento guasti | MYCIN, XCON |
| **PNL** | Analisi grammaticale, analisi semantica | Chatbot, sistemi di controllo qualità |
| **Inferenza sul tipo** | Controllo del tipo Hindley-Milner | Prototipi Haskell/ML |
| **Programmazione** | Pianificazione dei dipendenti, orari | Programmazione dell'equipaggio della compagnia aerea |
| **Ragionamento giuridico** | Analisi giuridica basata su regole | Controllo di conformità |
| **Interrogazione del database** | Datalog per l'analisi dei dati | Motore per soufflé |
| **Verifica** | Controllo del modello | Verifica hardware |
| **IBM Watson** | Comprensione del linguaggio naturale | Pericolo! sistema |
| **Ericsson** | Gestione delle telecomunicazioni | Convalida della configurazione di rete |
---

## Quando utilizzare Prolog
| Scenario | Perchè Prolog | Alternativa migliore |
|----------|-----------|-------------|
| Ragionamento basato su regole | Prolog è stato creato per questo | Motori di regole personalizzate in Python/Java |
| Soddisfazione dei vincoli | CLP(FD) è elegante ed efficiente | Risolutori SAT, strumenti OR per istanze di grandi dimensioni |
| Analisi grammaticale/linguaggio | Le DCG (Definite Clause Grammars) sono native | Generatori parser (ANTLR, yacc) per la produzione |
| Sistemi esperti | Adattamento naturale: fatti + regole = sistema esperto | Motori per regole aziendali (Drools) |
| Pianificazione/orario | Il CLP risolve bene questi problemi | Strumenti di sala operatoria, OptaPlanner |
| Digitare ricerca di sistema | L'unificazione è il fondamento | Implementare in OCaml, Haskell, Rust |
| Applicazioni Web | Non adatto | Python, Node.js, Go |
| Scienza dei dati/ML | Non l'ecosistema | Pitone, R |
| Codice critico per le prestazioni | Prolog è lento nel calcolo | C, C++, Ruggine |
| Programmazione generica | Possibile ma imbarazzante | Python, Go, Java |
---

## Riepilogo
Prolog è diverso da qualsiasi altro linguaggio di programmazione. Invece di scrivere istruzioni passo passo, descrivi relazioni e vincoli e il motore cerca soluzioni attraverso l'inferenza logica. Ciò rende Prolog ideale per problemi scomodi o prolissi nei linguaggi imperativi: sistemi esperti, pianificazione, analisi grammaticale, soddisfazione dei vincoli e qualsiasi cosa coinvolga regole logiche. La maggior parte dei programmatori non utilizzerà mai Prolog in produzione, ma apprenderlo amplia le tue idee su cosa può essere la programmazione. Unificazione, backtracking e specificazione dichiarativa dei problemi sono concetti che influenzano la progettazione del linguaggio, la ricerca sull'intelligenza artificiale e persino l'ottimizzazione delle query del database.
### Confronto tra motori Prolog
| Caratteristica | Prologo SWI | Prologo GNU | Tau Prologo |
|---------|-----------|------------|------------|
| **Licenza** | BSD (open source) | GPL (open source) | BSD (open source) |
| **Piattaforma** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (browser) |
| **CLP(FD)** | Libreria integrata | Integrato | Non disponibile |
| **Supporto DCG** | Completo | Completo | Limitato |
| **Tabella** | Sì | No | No |
| **FFI (chiamate C)** | Sì | Sì | Tramite JavaScript |
| **Rete** | HTTP, TCP, TLS | TCP | Tramite JavaScript |
| **Multi-threading** | Sì | No | No |
| **Gestore pacchetti** | `pack_install/1`| Nessuno | npm |
| **Ideale per** | Produzione, ricerca | Risoluzione dei vincoli | App Web, istruzione |
### Applicazioni Web con Penengine
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

### Metaprogrammazione con assert/retract
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
