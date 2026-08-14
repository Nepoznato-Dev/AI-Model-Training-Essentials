---
# Metadata
title: "Prolog — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Prolog with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [prolog, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# প্রোলগ — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ Prolog-এ সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্ন ক্যাটালগ করে।
---

## 1.`=`বনাম`==`বনাম `is`
```prolog
% ❌ WRONG — confusing unification with equality
X = 5.          % unifies X with 5
X == 5.         % strict equality (no unification)
X is 2 + 3.     % arithmetic evaluation

% ✅ CORRECT — understand the difference
% = is unification (pattern matching)
% == is strict equality (both sides must be identical)
% is evaluates arithmetic on the right side
```

---

## 2. কাট (`!`) সঠিকভাবে ব্যবহার না করা
```prolog
% ❌ WRONG — cut in wrong place causes missed solutions
max(X, Y, X) :- X >= Y.
max(X, Y, Y).  % always tries second clause too

% ✅ CORRECT — cut prevents unnecessary backtracking
max(X, _, X) :- X >= 0, !.
max(_, Y, Y).
```

---

## 3. অসীম পুনরাবৃত্তি
```prolog
% ❌ WRONG — no base case or wrong order
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
% If parent has cycles, this loops forever

% ✅ CORRECT — track visited nodes
ancestor(X, Y, Visited) :-
    parent(X, Y),
    \+ member(X, Visited).
ancestor(X, Y, Visited) :-
    parent(X, Z),
    \+ member(Z, Visited),
    ancestor(Z, Y, [Z|Visited]).
```

---

## 4. বোঝা যাচ্ছে না চেক হয়
```prolog
% ❌ WRONG — X = f(X) creates infinite term
?- X = f(X).
% In most Prologs: succeeds (X = f(f(f(f(...)))))
% With occurs check: fails (correct behavior)

% ✅ CORRECT — enable occurs check
% SWI-Prolog: set_prolog_flag(occurs_check, true).
```

---

## 5. Accumulators ছাড়া অপারেশন তালিকা
```prolog
% ❌ WRONG — inefficient list append
my_append([], L, L).
my_append([H|T], L, [H|R]) :- my_append(T, L, R).
% O(n) per call, O(n²) for building list

% ✅ CORRECT — use accumulator for building lists
reverse(List, Reversed) :- reverse(List, [], Reversed).
reverse([], Acc, Acc).
reverse([H|T], Acc, Reversed) :- reverse(T, [H|Acc], Reversed).
```

---

## সারাংশ
Prolog এর লজিক প্রোগ্রামিং প্যারাডাইম অনন্য ফাঁদ তৈরি করে: বিভ্রান্তিকর`=`(একীকরণ),`==`(সমতা), এবং`is`(পাটিগণিত); ভুল কাটা বসানো; পরিদর্শন ট্র্যাকিং ছাড়া অসীম পুনরাবৃত্তি; এবং চেক ঘটে। প্রোলগ উপায় হল: একীকরণকে গভীরভাবে বুঝুন, সংক্ষিপ্তভাবে এবং সঠিকভাবে কাটা ব্যবহার করুন, দক্ষ তালিকা তৈরির জন্য সঞ্চয়কারী ব্যবহার করুন এবং সর্বদা সমাপ্তি বিবেচনা করুন।