---
# Metadata
title: "Prolog — Version History & Evolution"
description: "Comprehensive version history and evolution of Prolog from origins to modern Prolog."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [prolog, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# प्रोलॉग - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| प्री-प्रोलॉग | 1965-70 | कोलमेरॉयर के क्यू-सिस्टम, प्राकृतिक भाषा प्रसंस्करण |
| प्रोलॉग I | 1972 | **पहला प्रस्तावना** (एलेन कोलमेरॉयर, मार्सिले) |
| दिसंबर-10 | 1977 | डेविड वॉरेन का एडिनबर्ग प्रोलॉग (कुशल संकलक) |
| आईएसओ प्रोलॉग | 1995 | **पहला आईएसओ मानक** (आईएसओ/आईईसी 13211-1) |
| SWI-प्रोलॉग | 1987 | जन विलेमेकर - सबसे लोकप्रिय ओपन-सोर्स प्रोलॉग |
| जीएनयू प्रोलॉग | 1999 | डैनियल डियाज़ - मूल संकलन |
| आईएसओ द्वितीय | 2012 | शुद्धिपत्र 2 (बग समाधान, स्पष्टीकरण) |
| एसडब्ल्यूआई 8.एक्स | 2018 | टेबलिंग, तर्कसंगतता, बेहतर प्रदर्शन |
| एसडब्ल्यूआई 9.एक्स | 2023 | **टेबलिंग** (डिफ़ॉल्ट), बेहतर मॉड्यूल, पैक सिस्टम |
| स्क्रीयर | 2018 | जंग में आधुनिक प्रोलॉग - आईएसओ-संगत |
| ट्रेल्ला | 2022 | सी में फास्ट प्रोलॉग - आधुनिक कार्यान्वयन |
## प्रमुख मील के पत्थर
### प्रोलॉग का जन्म (1972)
- **1972**: एलेन कोलमेरॉयर ने मार्सिले विश्वविद्यालय में प्रोलॉग बनाया
- **नाम**: "प्रोग्रामेशन एन लॉजिक" (तर्क में प्रोग्रामिंग)
- **लक्ष्य**: प्राकृतिक भाषा प्रसंस्करण - फ्रेंच वाक्यों को पार्स करें
- हॉर्न क्लॉज़ और रिज़ॉल्यूशन पर आधारित (रॉबिन्सन, 1965)
- पहला कार्यान्वयन: एकीकरण + पीछे हटना
### एडिनबर्ग प्रोलॉग (1977)
- **1977**: डेविड वॉरेन ने एडिनबर्ग में डीईसी-10 प्रोलॉग बनाया
- कुशल संकलक - प्रोलॉग व्यावहारिक हो जाता है
- एडिनबर्ग प्रोलॉग संदर्भ कार्यान्वयन बन जाता है
- प्रभाव: हॉर्न क्लॉज, गहराई-पहली खोज, कट ऑपरेटर
### आईएसओ मानकीकरण (1995)
- **1995**: पहला आईएसओ मानक (आईएसओ/आईईसी 13211-1)
- परिभाषित करता है: वाक्यविन्यास, अंतर्निहित विधेय, अंकगणित, I/O
- कार्यान्वयन में पोर्टेबिलिटी सुनिश्चित करता है
### आधुनिक प्रोलॉग (2000-वर्तमान)
- **एसडब्ल्यूआई-प्रोलॉग**: सबसे व्यापक रूप से उपयोग किया जाने वाला - टेबलिंग, मॉड्यूल, मल्टी-थ्रेडिंग, वेब (पेंगिन्स)
- **जीएनयू प्रोलॉग**: मूल संकलन - तेज़ निष्पादन योग्य
- **स्क्राइर प्रोलॉग**: आधुनिक, जंग-आधारित, आईएसओ-संगत
- **ट्रेला प्रोलॉग**: तेज़, हल्का, सी-आधारित
## सिंटेक्स इवोल्यूशन
```prolog
% Early Prolog (1970s): Basic logic programming
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Query: grandparent(tom, ann).  → true
% Query: grandparent(tom, X).    → X = ann ; X = bob

% Classic: List processing
append([], L, L).
append([H|T], L, [H|R]) :- append(T, L, R).

% ISO Prolog: Standardized built-ins
% Arithmetic
X is 2 + 3 * 4.          % X = 14
X =:= 14.                % true (arithmetic equality)
X =\= 15.                % true (arithmetic inequality)

% Constraint Logic Programming (CLP)
:- use_module(library(clpfd)).
sudoku(Rows) :-
    append(Rows, Vs), Vs ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Cols),
    maplist(all_distinct, Cols).

% Tabling (memoization) — SWI-Prolog 9.x
:- table fib/2.
fib(0, 0).
fib(1, 1).
fib(N, F) :- N > 1, N1 is N-1, N2 is N-2, fib(N1, F1), fib(N2, F2), F is F1+F2.

% Modules (ISO)
:- module(shapes, [area/2]).
area(circle(R), A) :- A is pi * R * R.
area(rect(W, H), A) :- A is W * H.

% DCG (Definite Clause Grammars) — natural language
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb, noun_phrase.
determiner --> [the].
noun --> [cat].
verb --> [chased].
```

## फ़ीचर इवोल्यूशन
```
1972: Basic Horn clauses, unification, backtracking
1977: DEC-10 Prolog — efficient compiler, cut operator
1980s: DCG (Definite Clause Grammars), difference lists
1990s: Constraint Logic Programming (CLP(FD), CLP(Q))
1995: ISO standard — portable Prolog
2000s: Tabling (memoization), modules, multi-threading
2010s: Tabling becomes default, pack systems, web integration
2020s: Modern implementations (Scryer, Trealla), improved performance
```

## मुख्य डिज़ाइन सिद्धांत
```
1. "Logic programming" — declare WHAT is true, not HOW to compute
2. "Unification" — pattern matching + variable binding
3. "Backtracking" — automatic search through possibilities
4. "Declarative" — programs are logical theories
5. "Relational" — relations, not functions
6. "Composable" — small rules, combine freely
```

## पारिस्थितिकी तंत्र का विकास
```
1972: Prolog created at Marseille — AI research
1977: DEC-10 Prolog — practical implementation
1980s: Japan's Fifth Generation Project — Prolog-based AI computers
1987: SWI-Prolog — open source, becomes most popular
1995: ISO standard — portability
1999: GNU Prolog — native compilation
2000s: Prolog in: expert systems, NLP, type inference, verification
2018: Scryer Prolog — modern Rust implementation
2022: Trealla Prolog — fast C implementation
2025: Prolog used in: IBM Watson (early), natural language processing,
       type systems, theorem proving, scheduling, rule engines
       SWI-Prolog is the reference implementation
```
