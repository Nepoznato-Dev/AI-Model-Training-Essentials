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
# Prólogo
Prolog (Programación en Lógica) es un lenguaje de programación lógica creado en 1972 por Alain Colmerauer y Philippe Roussel. A diferencia de todos los demás idiomas de esta lista, Prolog no le dice a la computadora *cómo* resolver un problema: usted declara *qué* es verdadero (hechos y reglas) y el motor de inferencia de Prolog descubre la respuesta mediante deducción lógica.
Prolog fue el lenguaje elegido para los sistemas expertos, el procesamiento del lenguaje natural y la investigación de IA en la década de 1980. Impulsó el proyecto de sistema informático de quinta generación de Japón y se utilizó en Watson de IBM para la comprensión del lenguaje natural. Hoy en día, Prolog se utiliza en la resolución de restricciones, programación, inferencia de tipos, razonamiento legal y en cualquier lugar donde los problemas se expresen naturalmente como relaciones lógicas.
**Programación lógica de restricciones (CLP)** amplía Prolog con solucionadores de restricciones para programación, enrutamiento y asignación de recursos, problemas que son extremadamente difíciles en lenguajes imperativos.
---

## Por qué es importante el prólogo
- **Programación declarativa**: describe qué es verdad, no cómo calcularlo. El motor hace el trabajo.
- **Coincidencia y unificación de patrones**: el algoritmo de unificación de Prolog es más poderoso que la coincidencia de patrones en otros lenguajes.
- **Búsqueda de retroceso**: Explora automáticamente todas las soluciones posibles. No se necesitan algoritmos de búsqueda manual.
- **Natural para problemas de lógica**: sistemas expertos, motores de reglas, correctores de tipos, analizadores gramaticales: se asignan directamente a Prolog.
- **Resolución de restricciones**: CLP(FD) resuelve problemas de programación, asignación y combinatoria con elegancia.
- **Pensamiento diferente**: Learning Prolog cambia la forma en que aborda la resolución de problemas: comienza a pensar en las relaciones y limitaciones.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Paradigma muy diferente** | Sin variables (solo enlaces), sin bucles, sin asignaciones | Piense en relaciones y recursividad, no en cambios de estado |
| **Rendimiento** | Lento para cálculos numéricos y datos de gran tamaño | Úselo para razonar; delegar el cálculo a C/otros idiomas |
| **Dificultad de depuración** | Es difícil rastrear los fracasos de retroceso y unificación | Utilice herramientas de seguimiento/depuración; escribir predicados deterministas |
| **Operador de corte (!)** | Necesario para la eficiencia pero rompe la pureza lógica | Utilice if-then-else o evaluación presentada cuando sea posible |
| **Ecosistema limitado** | Pocas bibliotecas, marcos o recursos comunitarios | SWI-Prolog es la implementación más completa |
| **No para aplicaciones generales** | Web, dispositivos móviles y GUI: no son los puntos fuertes de Prolog | Úselo como motor de razonamiento detrás de una aplicación web |
---

## Fundamentos de sintaxis
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

## Sintaxis y patrones avanzados
### Análisis profundo de la unificación
La unificación es el mecanismo central de Prolog: es la forma en que Prolog "empareja" términos y vincula variables.
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

### Puntos de retroceso y elección
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

### Gramáticas de cláusulas definidas (DCG)
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

### Programación lógica de restricciones (CLP)
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

## Arquitectura y diseño de sistemas
### Paradigma de programación lógica
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

### Estructura típica del proyecto
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

### Sistema de módulos
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

## Configuración del proyecto y sistema de construcción
### Configuración de SWI-Prolog
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

### Ejecución de programas Prolog
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

### Configuración de compilación
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

## Pruebas y depuración
### Seguimiento incorporado
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

### Pruebas unitarias con PLUnit
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

### Patrones de depuración comunes
| Problema | Síntoma | Solución |
|---------|---------|----------|
| Recursión infinita | Desbordamiento de pila | Verifique el caso base; agregar condición de terminación |
| Sin soluciones | La consulta devuelve falso | Verifique el orden de creación de instancias de variables |
| Demasiadas soluciones | Duplicados inesperados | Agregue corte (!) o use`setof`|
| Unificación incorrecta | Variables enlazadas incorrectamente | Utilice`=`para probar; comprobar la aridad del funtor |
| Problema de rendimiento | Ejecución lenta | Agrega cortes; utilizar `table`; comprobar puntos de elección |
---

## Interoperabilidad
### Interfaz C (FFI)
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

### Integración de Python
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

## Patrones de diseño
### Patrón 1: Acumulador (Recursión de cola)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Patrón 2: subprocesamiento de estado```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Patrón 3: generar y probar```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Patrón 4: Listas de diferencias```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Rendimiento y optimización
### Optimización de corte
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Recursión de cola
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Lista de verificación de optimización
| Técnica | Impacto | Descripción |
|-----------|--------|-------------|
| **Recursión de cola** | Alto | Utilice acumuladores para un espacio de pila constante |
| **Corte (verde)** | Alto | Eliminar puntos de elección innecesarios |
| **Evaluación presentada** | Alto | `:- table pred/N`memoriza resultados |
| **Indexación** | Medio | Ponga primero el argumento discriminatorio |
| **Listas de diferencias** | Medio | O(1) concatenación de listas |
| **CLP(FD) sobre prueba de generación** | Muy Alto | Utilice restricciones en lugar de fuerza bruta |
---

## Implementación y uso en el mundo real
### Implementación de aplicaciones Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Aplicaciones del mundo real
| Dominio | Cómo se utiliza Prolog | Ejemplo |
|--------|-------------------|---------|
| **Sistemas expertos** | Diagnóstico médico, detección de fallos | MYCIN, XCON |
| **PNL** | Análisis gramatical, análisis semántico | Chatbots, sistemas de control de calidad |
| **Inferencia de tipos** | Comprobación de tipo Hindley-Milner | Prototipos Haskell/ML |
| **Programación** | Programación de empleados, horarios | Programación de tripulaciones de aerolíneas |
| **Razonamiento jurídico** | Análisis jurídico basado en reglas | Control de cumplimiento |
| **Consulta de base de datos** | Registro de datos para análisis de datos | Motor soufflé |
| **Verificación** | Comprobación de modelos | Verificación de hardware |
| **IBM Watson** | Comprensión del lenguaje natural | ¡Peligro! sistema |
| **Ericsson** | Gestión de telecomunicaciones | Validación de configuración de red |
---

## Cuándo utilizar el prólogo
| Escenario | ¿Por qué prolog | Mejor alternativa |
|----------|-----------|-------------------|
| Razonamiento basado en reglas | Prolog está diseñado para esto | Motores de reglas personalizados en Python/Java |
| Satisfacción de restricciones | CLP(FD) es elegante y eficiente | Solucionadores SAT, OR-Tools para instancias grandes |
| Análisis de gramática/lenguaje | DCG (Gramáticas de cláusulas definidas) son nativas | Generadores de analizadores (ANTLR, yacc) para producción |
| Sistemas expertos | Ajuste natural: hechos + reglas = sistema experto | Motores de reglas de negocio (Drools) |
| Programación / horarios | CLP los resuelve bien | Herramientas OR, OptaPlanner |
| Investigación de sistemas de tipos | La unificación es la base | Implementar en OCaml, Haskell, Rust |
| Aplicaciones web | No adecuado | Python, Node.js, Ir |
| Ciencia de datos / ML | No el ecosistema | Pitón, R |
| Código crítico para el rendimiento | Prolog es lento para el cálculo | C, C++, óxido |
| Programación de propósito general | Posible pero incómodo | Python, Ir, Java |
---

## Preguntas y respuestas sintéticas
### P1: ¿En qué se diferencia la unificación de Prolog de la asignación en otros idiomas?
**R:** La unificación es una coincidencia de patrones bidireccional, no una asignación:
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

### P2: ¿Cómo funciona el retroceso en Prolog?
**R:** Cuando un objetivo falla, Prolog retrocede hasta el último punto de elección e intenta la siguiente alternativa:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### P3: ¿Cómo trabajo con listas en Prolog?
**R:** Las listas utilizan la coincidencia de patrones de cabeza/cola:
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

### P4: ¿Cuándo debo usar Prolog en lugar de otros idiomas?
**R:** Prolog se destaca en:
- Satisfacción de restricciones (programación, acertijos)
- Sistemas basados en reglas (sistemas expertos, validación)
- Recorrido de gráfico/árbol
- Procesamiento del lenguaje natural
- Cálculo simbólico
- Cualquier problema expresable como relaciones lógicas.
### P5: ¿Cuáles son los errores comunes en Prolog?
**R:** Cuestiones clave:
- Recursividad infinita: siempre ponga primero el caso base
- Retroceso involuntario: use el corte`!`o`once/1`
- Se produce una verificación: bucles`X = f(X)`de forma predeterminada (use `unify_with_occurs_check`)
- Cortes verdes (optimización) frente a cortes rojos (cambiar significado): prefiera el verde
---

## Resolución de problemas mediante cadena de pensamiento
### Problema 1: Resolver el rompecabezas de N-Reinas
**Paso 1: Comprenda el problema**
Coloca N reinas en un tablero de ajedrez NxN para que no haya dos reinas que se ataquen entre sí.
**Paso 2: Identificar el enfoque**
Utilice generación basada en restricciones: coloque las reinas columna por columna, verificando la seguridad.
**Paso 3: Implementar**```prolog
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

**Paso 4: Verificar**
`?- n_queens(8, Qs).`debería encontrar 92 soluciones.
### Problema 2: creación de un sistema experto simple
**Paso 1: Comprenda el problema**
Diagnosticar problemas del automóvil según los síntomas.
**Paso 2: Identificar el enfoque**
Utilice reglas de Prolog para codificar el conocimiento de diagnóstico.
**Paso 3: Implementar**```prolog
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

**Paso 4: Extender**
Agregue puntuaciones de confianza, solicite síntomas al usuario de forma interactiva y encadene diagnósticos.
---

## Resumen
Prolog no se parece a ningún otro lenguaje de programación. En lugar de escribir instrucciones paso a paso, usted describe relaciones y limitaciones y el motor busca soluciones mediante inferencia lógica. Esto hace que Prolog sea ideal para problemas incómodos o detallados en lenguajes imperativos: sistemas expertos, programación, análisis gramatical, satisfacción de restricciones y cualquier cosa que involucre reglas lógicas. La mayoría de los programadores nunca usarán Prolog en producción, pero aprenderlo amplía su pensamiento sobre lo que puede ser la programación. La unificación, el retroceso y la especificación declarativa de problemas son conceptos que influyen en el diseño del lenguaje, la investigación de IA e incluso la optimización de consultas de bases de datos.
### Comparación de motores Prolog
| Característica | SWI-Prólogo | Prólogo de GNU | Prólogo de Tau |
|---------|-----------|------------|------------|
| **Licencia** | BSD (código abierto) | GPL (código abierto) | BSD (código abierto) |
| **Plataforma** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (navegador) |
| **CLP(FD)** | Biblioteca incorporada | Incorporado | No disponible |
| **Soporte DCG** | Completo | Completo | Limitado |
| **Presentación** | Sí | No | No |
| **FFI (llamadas C)** | Sí | Sí | A través de JavaScript |
| **Redes** | HTTP, TCP, TLS | TCP | A través de JavaScript |
| **Subprocesos múltiples** | Sí | No | No |
| **Administrador de paquetes** | `pack_install/1`| Ninguno | mpn |
| **Mejor para** | Producción, investigación | Resolución de restricciones | Aplicaciones web, educación |
### Aplicaciones Web con Pengines
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

### Metaprogramación con afirmación/retracción
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
