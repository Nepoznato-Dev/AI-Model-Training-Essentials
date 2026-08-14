<!--
---
# Metadata
title: "Prolog — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic Prolog code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [prolog, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "8 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# प्रोलॉग - मुहावरेदार पैटर्न और सर्वोत्तम अभ्यास
यह मार्गदर्शिका स्वच्छ, मुहावरेदार प्रोलॉग कोड लिखने के लिए मुहावरेदार पैटर्न को कवर करती है।
---

## पैटर्न मिलान
```prolog
% ✅ Head matching for clarity
factorial(0, 1).
factorial(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

% ✅ List patterns
my_length([], 0).
my_length([_|T], N) :-
    my_length(T, N1),
    N is N1 + 1.

% ✅ Guard clauses
classify(N, positive) :- N > 0.
classify(0, zero).
classify(N, negative) :- N < 0.
```

---

## कटौती और नियतिवाद
```prolog
% ✅ Green cut (remove unnecessary choicepoints)
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).

% ✅ Avoid red cuts (changing semantics)
% ✅ Use -> (if-then-else) instead
classify(N) ->
    ( N > 0 -> positive
    ; N =:= 0 -> zero
    ; negative
    ).
```

---

## सारांश
प्रोलॉग मुहावरे जोर देते हैं: सिर में पैटर्न मिलान, संचायक के साथ पूंछ पुनरावृत्ति, दक्षता के लिए हरे रंग की कटौती, और घोषणात्मक शैली। प्रोलॉग शैली परंपराओं का पालन करें। प्रोलॉग तार्किक शुद्धता को महत्व देता है - "संबंध ही कार्यक्रम है।"