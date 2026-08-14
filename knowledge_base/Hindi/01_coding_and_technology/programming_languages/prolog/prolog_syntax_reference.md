<!--
---
# Metadata
title: "Prolog — Syntax Reference"
description: "Detailed syntax reference for Prolog covering unification, backtracking, cut, DCGs, and logic programming patterns."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
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

-->
# प्रोलॉग - सिंटैक्स संदर्भ
यह दस्तावेज़ प्रोलॉग के लिए एक व्यापक, संरचित वाक्यविन्यास संदर्भ प्रदान करता है। यह संपूर्ण सिंटैक्स पैटर्न, एकीकरण, बैकट्रैकिंग, डीसीजी और लॉजिक प्रोग्रामिंग मुहावरों पर ध्यान केंद्रित करके मुख्य प्रोलॉग संदर्भ को पूरक करता है।
---

## कोर सिंटैक्स
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

## एकीकरण एवं मिलान
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

## नियंत्रण एवं पीछे हटना
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

## सूची संचालन
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

## निश्चित खंड व्याकरण (डीसीजी)
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

## सारांश
प्रोलॉग का वाक्यविन्यास न्यूनतम है - तथ्य, नियम और प्रश्न। शक्ति एकीकरण और बैकट्रैकिंग से आती है, जो भाषा को तार्किक समाधानों के लिए एक खोज इंजन में बदल देती है। डीसीजी सुंदर पार्सर पीढ़ी प्रदान करते हैं। सूचियाँ हेड/टेल पैटर्न मिलान का उपयोग करती हैं। बाधा संतुष्टि, विशेषज्ञ प्रणालियों और प्रतीकात्मक गणना के लिए, प्रोलॉग का घोषणात्मक दृष्टिकोण उन समस्याओं को हल करता है जो अनिवार्य भाषाओं में क्रियात्मक हैं।