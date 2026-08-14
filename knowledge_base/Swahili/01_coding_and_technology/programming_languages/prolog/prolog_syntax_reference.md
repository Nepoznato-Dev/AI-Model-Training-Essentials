---
# Metadata
title: "Prolog — Syntax Reference"
description: "Detailed syntax reference for Prolog covering unification, backtracking, cut, DCGs, and logic programming patterns."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [prolog, syntax-reference, unification, backtracking, logic-programming, dcg, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Prolog - Rejeleo la Sintaksia
Hati hii inatoa rejeleo la kina, lenye muundo wa sintaksia kwa Prolog. Inakamilisha rejeleo kuu la Prolog kwa kuangazia mifumo kamili ya sintaksia, kuunganisha, kurudi nyuma, DCG na nahau za kupanga programu.
---

## Sintaksia ya Msingi
```prolog
% Facts
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).

% Rules
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Queries (in the REPL)
?- parent(tom, bob).        % true
?- parent(tom, X).          % X = bob ; X = liz
?- grandparent(tom, ann).   % true
```

---

## Kuunganisha na Kulinganisha
```prolog
% = is unification (not assignment!)
?- X = hello.               % X = hello
?- f(X, b) = f(a, Y).       % X = a, Y = b
?- [H|T] = [1, 2, 3].       % H = 1, T = [2, 3]

% \= is not-unifiable
?- a \= b.                  % true
?- X \= 5.                  % error (X is unbound)

% Anonymous variable
?- f(a, _, c) = f(a, b, c). % true

% is for arithmetic evaluation
?- X is 2 + 3.              % X = 5
?- X = 2 + 3.               % X = 2+3 (unevaluated)
```

---

## Kudhibiti na Kurudisha nyuma
```prolog
% Cut (!) — prevent backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).

% Fail — force backtracking
safe(X) :- X > 0, !.
safe(_).  % fallback

% Negation as failure
different(X, Y) :- X \= Y.

% If-then-else
classify(X, Result) :-
    ( X > 0 -> Result = positive
    ; X < 0 -> Result = negative
    ; Result = zero
    ).

% Find all solutions
?- findall(X, color(X), Colors).
% Colors = [red, green, blue]

?- bagof(X, parent(tom, X), Children).
% Children = [bob, liz]
```

---

#Orodhesha Operesheni
```prolog
% Length
my_length([], 0).
my_length([_|T], N) :- my_length(T, N1), N is N1 + 1.

% Append
my_append([], L, L).
my_append([H|T], L, [H|R]) :- my_append(T, L, R).

% Member
my_member(X, [X|_]).
my_member(X, [_|T]) :- my_member(X, T).

% Last element
my_last([X], X).
my_last([_|T], X) :- my_last(T, X).

% Reverse
my_reverse([], []).
my_reverse([H|T], R) :-
    my_reverse(T, RT),
    my_append(RT, [H], R).

% Map
my_map(_, [], []).
my_map(F, [H|T], [FH|FT]) :-
    call(F, H, FH),
    my_map(F, T, FT).

% Fold
my_foldl(_, Acc, [], Acc).
my_foldl(Goal, Acc, [H|T], Result) :-
    call(Goal, Acc, H, NewAcc),
    my_foldl(Goal, NewAcc, T, Result).
```

---

## Sarufi za Kifungu Dhahiri (DCGs)
```prolog
% Parse arithmetic expressions
expr --> term, ("+", expr | "").
term --> factor, ("*", term | "").
factor --> [N], { number(N) }.
factor --> "(", expr, ")".

% Parse natural language
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb.
verb_phrase --> verb, noun_phrase.

determiner --> [the] | [a].
noun --> [cat] | [dog] | [fish].
verb --> [chases] | [eats] | [sees].

% Query: phrase(sentence, [the, cat, chases, the, dog]).
```

---

## Muhtasari
Syntax ya Prolog ni ndogo - ukweli, sheria, na maswali. Nguvu hutoka kwa kuunganisha na kurudi nyuma, ambayo hugeuza lugha kuwa injini ya utafutaji kwa ufumbuzi wa kimantiki. DCGs hutoa kizazi cha kifahari cha uchanganuzi. Orodha hutumia ulinganifu wa muundo wa kichwa/mkia. Kwa utoshelevu wa kikwazo, mifumo ya wataalamu, na ukokotoaji wa ishara, mbinu ya tamko ya Prolog hutatua matatizo ambayo ni ya kitenzi katika lugha za lazima.