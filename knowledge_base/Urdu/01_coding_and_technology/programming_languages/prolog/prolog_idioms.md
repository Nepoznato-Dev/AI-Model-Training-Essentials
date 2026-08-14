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
# پرولوگ - محاوراتی نمونے اور بہترین طرز عمل
یہ گائیڈ صاف، محاوراتی پرولوگ کوڈ لکھنے کے لیے محاوراتی نمونوں کا احاطہ کرتا ہے۔
---

## پیٹرن میچنگ
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

## کٹوتیاں اور عزم
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

## خلاصہ
پرولوگ محاوروں پر زور دیا جاتا ہے: سروں میں پیٹرن کی مماثلت، جمع کرنے والوں کے ساتھ دم کی تکرار، کارکردگی کے لیے سبز کٹ، اور اعلانیہ انداز۔ پرولوگ طرز کے کنونشنز پر عمل کریں۔ پرولوگ منطقی پاکیزگی کی قدر کرتا ہے - "رشتہ پروگرام ہے۔"