---
# Metadata
title: "Prolog — Cheat Sheet"
description: "Quick-reference cheat sheet for Prolog syntax, pattern matching, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [prolog, logic-programming, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "8 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Prólogo - Hoja de referencia
## Conceptos básicos
```prolog
% Facts
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).

% Rules
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

% Variables (uppercase)
?- parent(tom, X).           % X = bob ; X = liz
?- grandparent(tom, Who).    % Who = ann ; Who = pat

% Atoms (lowercase)
% Numbers
% Structures: functor(arg1, arg2)

% Comparison
X = Y          % unification
X \= Y         % not unifiable
X == Y         % strict equality
X \== Y        % strict not equal
X is Expr      % arithmetic evaluation
X =:= Y        % numeric equal
X =\= Y        % numeric not equal
X < Y, X > Y
X >= Y, X =< Y
```

## Listas
```prolog
% List syntax
[]                    % empty list
[a, b, c]             % list of atoms
[1, 2, 3]             % list of numbers
[H | T]               % head | tail

% Pattern matching
?- [a, b, c] = [H | T].     % H = a, T = [b, c]
?- [a, b, c] = [A, B | R].  % A = a, B = b, R = [c]

% Common predicates
member(X, [X | _]).
member(X, [_ | T]) :- member(X, T).

length([], 0).
length([_ | T], N) :- length(T, N1), N is N1 + 1.

append([], L, L).
append([H | T], L, [H | R]) :- append(T, L, R).

reverse([], []).
reverse([H | T], R) :- reverse(T, RT), append(RT, [H], R).

% Maplist
maplist(Goal, List).
maplist(plus(1), [1,2,3], Result).  % Result = [2,3,4]

% Findall
?- findall(X, parent(tom, X), Children).
% Children = [bob, liz]

% Sort
?- sort([3,1,4,1,5], Sorted).
% Sorted = [1, 3, 4, 5]
```

## Controlar el flujo
```prolog
% Conjunction (AND)
goal1, goal2, goal3

% Disjunction (OR)
(goal1 ; goal2 ; goal3)

% If-then-else
(Condition -> Then ; Else)

% Negation as failure
\+ goal              % true if goal fails

% Cut
!                    % commit to choices before cut

% Fail
fail                 % always fails (backtrack)

% Repeat
repeat, ...          % infinite loop until cut/fail

% Forall
forall(member(X, List), process(X))

% Once (try once)
once(goal)           % succeed at most once
```

## Aritmética y acumuladores
```prolog
% Arithmetic
X is 2 + 3.          % X = 5
X is 10 mod 3.       % X = 1
X is 2 ** 10.        % X = 1024

% Tail-recursive factorial with accumulator
factorial(N, F) :- factorial(N, 1, F).
factorial(0, Acc, Acc).
factorial(N, Acc, F) :-
    N > 0,
    N1 is N - 1,
    Acc1 is Acc * N,
    factorial(N1, Acc1, F).

% Sum of list
sum_list([], 0).
sum_list([H | T], Sum) :-
    sum_list(T, Rest),
    Sum is H + Rest.

% Tail-recursive sum
sum_list(L, Sum) :- sum_list(L, 0, Sum).
sum_list([], Acc, Acc).
sum_list([H | T], Acc, Sum) :-
    Acc1 is Acc + H,
    sum_list(T, Acc1, Sum).
```

## DCG (Gramáticas de cláusulas definidas)
```prolog
% Grammar rules
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb.
verb_phrase --> verb, noun_phrase.

determiner --> [the].
determiner --> [a].
noun --> [cat].
noun --> [mouse].
verb --> [chases].

% Parse
?- phrase(sentence, [the, cat, chases, the, mouse]).
% true
```

## Módulos y E/S
```prolog
% Module
:- module(my_module, [fact/2, rule/3]).
fact(a, 1).
rule(X, Y, Z) :- ...

% I/O
write('Hello'), nl.
read(X).
format('~w is ~d years old~n', [Name, Age]).

% File I/O
open('file.txt', read, Stream),
read_line_to_codes(Stream, Codes),
close(Stream).

% Assert / retract (dynamic)
:- dynamic fact/1.
assert(fact(hello)).
retract(fact(hello)).
```
