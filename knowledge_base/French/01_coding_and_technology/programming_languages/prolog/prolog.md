---
# Métadonnées
titre : "Prologue"
description : "Référence complète pour le langage de programmation Prolog couvrant la présentation, les compromis, les principes fondamentaux de la syntaxe, l'écosystème et quand l'utiliser."
catégorie : "Codage et technologie"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances en matière de codage et de technologie"
next_review : "2027-08-05"
#Classement
balises : [prologue, langage de programmation, syntaxe, écosystème, codage et technologie]
niveau de difficulté : "avancé"
prérequis : []
estimate_reading_time : "25 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Prologue
Prolog (Programming in Logic) est un langage de programmation logique créé en 1972 par Alain Colmerauer et Philippe Roussel. Contrairement à tous les autres langages de cette liste, Prolog ne dit pas à l'ordinateur *comment* résoudre un problème — vous déclarez *ce* qui est vrai (faits et règles), et le moteur d'inférence de Prolog trouve la réponse par déduction logique.
Prolog était le langage de choix pour les systèmes experts, le traitement du langage naturel et la recherche sur l'IA dans les années 1980. Il a alimenté le projet japonais de système informatique de cinquième génération et a été utilisé dans Watson d'IBM pour la compréhension du langage naturel. Aujourd'hui, Prolog est utilisé dans la résolution de contraintes, la planification, l'inférence de types, le raisonnement juridique et partout où les problèmes sont naturellement exprimés sous forme de relations logiques.
**Constraint Logic Programming (CLP)** étend Prolog avec des solveurs de contraintes pour la planification, le routage et l'allocation de ressources — des problèmes extrêmement difficiles dans les langages impératifs.
---

## Pourquoi Prolog est important
- **Programmation déclarative** : Décrivez ce qui est vrai, pas comment le calculer. Le moteur fait le travail.
- **Correspondance de modèles et unification** : l'algorithme d'unification de Prolog est plus puissant que la correspondance de modèles dans d'autres langages.
- **Recherche de retour en arrière** : explore automatiquement toutes les solutions possibles. Aucun algorithme de recherche manuelle n'est nécessaire.
- **Naturel pour les problèmes de logique** : systèmes experts, moteurs de règles, vérificateurs de types, analyseurs de grammaire — ceux-ci sont directement mappés à Prolog.
- **Résolution de contraintes** : CLP(FD) résout les problèmes de planification, d'allocation et combinatoires avec élégance.
- **Pensée différente** : l'apprentissage de Prolog change votre façon d'aborder la résolution de problèmes : vous commencez à penser en termes de relations et de contraintes.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Paradigme très différent** | Pas de variables (uniquement des liaisons), pas de boucles, pas d'affectations | Pensez aux relations et à la récursion, pas aux changements d'état |
| **Performances** | Lent pour le calcul numérique et les données volumineuses | Utiliser pour le raisonnement ; déléguer le calcul à C/autres langages |
| **Difficulté de débogage** | Difficile de retracer les retours en arrière et les échecs de l'unification | Utiliser les outils de trace/débogage ; écrire des prédicats déterministes |
| **Opérateur de coupe (!)** | Nécessaire pour l'efficacité mais brise la pureté logique | Utilisez if-then-else ou une évaluation déposée lorsque cela est possible |
| **Écosystème limité** | Peu de bibliothèques, de frameworks ou de ressources communautaires | SWI-Prolog est l'implémentation la plus complète |
| **Pas pour les applications générales** | Web, mobile, interface graphique : ce n'est pas la force de Prolog | Utiliser comme moteur de raisonnement derrière une application web |
---

## Fondamentaux de la syntaxe
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

## Syntaxe et modèles avancés
### Analyse approfondie de l'unification
L'unification est le mécanisme principal de Prolog — c'est ainsi que Prolog « fait correspondre » les termes et lie les variables.
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

### Points de retour en arrière et de choix
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

### Grammaires de clauses définies (DCG)
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

### Programmation logique par contraintes (CLP)
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

## Architecture et conception de systèmes
### Paradigme de programmation logique
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

### Structure typique du projet
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

### Système de modules
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

## Configuration du projet et système de construction
### Configuration du prologue SWI
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

### Exécution de programmes Prolog
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

### Construire la configuration
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

## Tests et débogage
### Traçage intégré
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

### Tests unitaires avec PLUnit
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

### Modèles de débogage courants
| Problème | Symptôme | Solutions |
|---------|---------|--------------|
| Récursivité infinie | Débordement de pile | Vérifiez le cas de base ; ajouter une condition de résiliation |
| Aucune solution | La requête renvoie false | Vérifier l'ordre d'instanciation des variables |
| Trop de solutions | Doublons inattendus | Ajoutez une coupe (!) ou utilisez`setof`|
| Mauvaise unification | Variables liées de manière incorrecte | Utilisez`=`pour tester ; vérifier l'arité du foncteur |
| Problème de performances | Exécution lente | Ajoutez des coupes ; utilisez`table`; vérifier les points de choix |
---

## Interopérabilité
### Interface C (FFI)
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

### Intégration Python
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

## Modèles de conception
### Modèle 1 : Accumulateur (récursion de queue)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Modèle 2 : threading d'état```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Modèle 3 : Générer et tester```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Modèle 4 : Listes de différences```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Performances et optimisation
### Optimisation des coupes
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Récursion de queue
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Liste de contrôle d'optimisation
| Techniques | Impact | Descriptif |
|---------------|--------|-------------|
| **Récursion de queue** | Élevé | Utiliser des accumulateurs pour un espace de pile constant |
| **Coupé (vert)** | Élevé | Éliminez les points de choix inutiles |
| **Évaluation déposée** | Élevé | `:- table pred/N`mémorise les résultats |
| **Indexation** | Moyen | Donner la priorité aux arguments discriminatoires |
| **Listes de différences** | Moyen | O(1) concaténation de liste |
| **CLP(FD) sur générer-test** | Très élevé | Utilisez des contraintes au lieu de la force brute |
---

## Déploiement et utilisation dans le monde réel
### Déploiement d'applications Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Applications du monde réel
| Domaine | Comment Prolog est utilisé | Exemple |
|--------|---------|---------|
| **Systèmes experts** | Diagnostic médical, détection de défauts | MYCINE, XCON |
| **PNL** | Analyse grammaticale, analyse sémantique | Chatbots, systèmes d'assurance qualité |
| **Inférence de type** | Vérification de type Hindley-Milner | Prototypes Haskell/ML |
| **Planification** | Planification des employés, emploi du temps | Planification des équipages des compagnies aériennes |
| **Raisonnement juridique** | Analyse juridique basée sur des règles | Contrôle de conformité |
| **Interrogation de base de données** | Journal de données pour l'analyse des données | Moteur soufflé |
| **Vérification** | Vérification du modèle | Vérification du matériel |
| **IBM Watson** | Compréhension du langage naturel | Péril! système |
| **Éricsson** | Gestion des télécommunications | Validation de la configuration réseau |
---

## Quand utiliser Prolog
| Scénario | Pourquoi Prolog | Meilleure alternative |
|----------|-----------|-------------------|
| Raisonnement basé sur des règles | Prolog est conçu pour cela | Moteurs de règles personnalisés en Python/Java |
| Satisfaction des contraintes | CLP(FD) est élégant et efficace | Solveurs SAT, outils OR pour grandes instances |
| Grammaire/analyse linguistique | Les DCG (Definite Clause Grammars) sont natives | Générateurs d'analyseurs (ANTLR, yacc) pour la production |
| Systèmes experts | Ajustement naturel — faits + règles = système expert | Moteurs de règles métier (Drools) |
| Planification / emploi du temps | CLP résout bien ces problèmes | Outils OR, OptaPlanner |
| Recherche de systèmes de types | L'unification est le fondement | Implémenter dans OCaml, Haskell, Rust |
| Applications Web | Ne convient pas | Python, Node.js, Go |
| Science des données / ML | Pas l'écosystème | Python, R |
| Code critique pour les performances | Prolog est lent pour le calcul | C, C++, Rouille |
| Programmation générale | Possible mais gênant | Python, Go, Java |
---

## Résumé
Prolog ne ressemble à aucun autre langage de programmation. Au lieu d'écrire des instructions étape par étape, vous décrivez les relations et les contraintes, et le moteur recherche des solutions par inférence logique. Cela rend Prolog idéal pour les problèmes délicats ou verbeux dans les langages impératifs : systèmes experts, planification, analyse grammaticale, satisfaction de contraintes et tout ce qui implique des règles logiques. La plupart des programmeurs n'utiliseront jamais Prolog en production, mais l'apprendre élargit votre réflexion sur ce que peut être la programmation. L'unification, le retour en arrière et la spécification déclarative des problèmes sont des concepts qui influencent la conception du langage, la recherche sur l'IA et même l'optimisation des requêtes de base de données.
### Comparaison des moteurs Prolog
| Fonctionnalité | SWI-Prologue | Prologue GNU | Prologue Tau |
|---------|-----------|------------|------------|
| **Licence** | BSD (open source) | GPL (open source) | BSD (open source) |
| **Plateforme** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (navigateur) |
| **CLP(FD)** | Bibliothèque intégrée | Intégré | Non disponible |
| **Support DCG** | Complet | Complet | Limité |
| **Dépôt** | Oui | Non | Non |
| **FFI (appels C)** | Oui | Oui | Via Javascript |
| **Réseau** | HTTP, TCP, TLS | TCP | Via Javascript |
| **Multi-thread** | Oui | Non | Non |
| **Gestionnaire de paquets** | `pack_install/1`| Aucun | npm |
| **Idéal pour** | Production, recherche | Résolution de contraintes | Applications Web, éducation |
### Applications Web avec Pengines
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

### Métaprogrammation avec assert/retract
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
