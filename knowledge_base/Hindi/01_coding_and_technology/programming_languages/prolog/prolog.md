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
# प्रोलॉग
प्रोलॉग (प्रोग्रामिंग इन लॉजिक) एक लॉजिक प्रोग्रामिंग भाषा है जिसे 1972 में एलेन कोलमेरॉयर और फिलिप रूसेल द्वारा बनाया गया था। इस सूची की हर दूसरी भाषा के विपरीत, प्रोलॉग कंप्यूटर को यह नहीं बताता कि किसी समस्या को कैसे हल किया जाए - आप घोषणा करते हैं कि *क्या* सत्य है (तथ्य और नियम), और प्रोलॉग का अनुमान इंजन तार्किक कटौती के माध्यम से उत्तर का पता लगाता है।
1980 के दशक में प्रोलॉग विशेषज्ञ प्रणालियों, प्राकृतिक भाषा प्रसंस्करण और एआई अनुसंधान के लिए पसंद की भाषा थी। इसने जापान की पांचवीं पीढ़ी के कंप्यूटर सिस्टम प्रोजेक्ट को संचालित किया और प्राकृतिक भाषा को समझने के लिए आईबीएम के वॉटसन में इसका उपयोग किया गया। आज, प्रोलॉग का उपयोग बाधा समाधान, शेड्यूलिंग, प्रकार अनुमान, कानूनी तर्क में किया जाता है, और कहीं भी समस्याओं को स्वाभाविक रूप से तार्किक संबंधों के रूप में व्यक्त किया जाता है।
**बाधा तर्क प्रोग्रामिंग (सीएलपी)** शेड्यूलिंग, रूटिंग और संसाधन आवंटन के लिए बाधा समाधानकर्ताओं के साथ प्रोलॉग का विस्तार करती है - ऐसी समस्याएं जो अनिवार्य भाषाओं में बेहद कठिन हैं।
---

## प्रोलॉग क्यों मायने रखता है
- **घोषणात्मक प्रोग्रामिंग**: जो सत्य है उसका वर्णन करें, न कि इसकी गणना कैसे करें। इंजन काम करता है.
- **पैटर्न मिलान और एकीकरण**: प्रोलॉग का एकीकरण एल्गोरिदम अन्य भाषाओं में पैटर्न मिलान की तुलना में अधिक शक्तिशाली है।
- **बैकट्रैकिंग सर्च**: स्वचालित रूप से सभी संभावित समाधानों का पता लगाता है। किसी मैन्युअल खोज एल्गोरिदम की आवश्यकता नहीं है.
- **तर्क समस्याओं के लिए स्वाभाविक**: विशेषज्ञ प्रणाली, नियम इंजन, प्रकार चेकर्स, व्याकरण पार्सर - ये सीधे प्रोलॉग पर मैप होते हैं।
- **बाधा समाधान**: सीएलपी(एफडी) शेड्यूलिंग, आवंटन और कॉम्बिनेटरियल समस्याओं को सुरुचिपूर्ण ढंग से हल करता है।
- **अलग सोच**: प्रोलॉग सीखने से समस्या-समाधान के प्रति आपके दृष्टिकोण में बदलाव आता है - आप रिश्तों और बाधाओं के बारे में सोचना शुरू करते हैं।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **बहुत अलग प्रतिमान** | कोई वेरिएबल नहीं (केवल बाइंडिंग), कोई लूप नहीं, कोई असाइनमेंट नहीं | संबंध और प्रत्यावर्तन में सोचो, अवस्था परिवर्तन में नहीं |
| **प्रदर्शन** | संख्यात्मक गणना और बड़े डेटा के लिए धीमा | तर्क के लिए उपयोग करें; सी/अन्य भाषाओं में गणना सौंपें |
| **डिबगिंग कठिनाई** | बैकट्रैकिंग और एकीकरण विफलताओं का पता लगाना कठिन है | ट्रेस/डीबग टूल का उपयोग करें; नियतिवादी विधेय लिखें |
| **कट ऑपरेटर (!)** | कार्यकुशलता के लिए आवश्यक है लेकिन तार्किक शुद्धता को तोड़ता है | जब संभव हो तो यदि-तब-अन्यथा या सारणीबद्ध मूल्यांकन का उपयोग करें |
| **सीमित पारिस्थितिकी तंत्र** | कुछ पुस्तकालय, ढाँचे, या सामुदायिक संसाधन | एसडब्ल्यूआई-प्रोलॉग सबसे पूर्ण कार्यान्वयन है |
| **सामान्य ऐप्स के लिए नहीं** | वेब, मोबाइल, जीयूआई - प्रोलॉग की ताकत नहीं | वेब ऐप के पीछे तर्क इंजन के रूप में उपयोग करें |
---

## सिंटेक्स बुनियादी बातें
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

## उन्नत सिंटैक्स और पैटर्न
### एकीकरण गहरा गोता
एकीकरण प्रोलॉग का मुख्य तंत्र है - यह इस प्रकार है कि प्रोलॉग शब्दों को "मिलान" करता है और चर को बांधता है।
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

### बैकट्रैकिंग और चॉइस पॉइंट
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

### निश्चित खंड व्याकरण (डीसीजी)
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

### बाधा तर्क प्रोग्रामिंग (सीएलपी)
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

## वास्तुकला एवं सिस्टम डिज़ाइन
### तर्क प्रोग्रामिंग प्रतिमान
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

### विशिष्ट परियोजना संरचना
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

### मॉड्यूल सिस्टम
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### एसडब्ल्यूआई-प्रोलॉग कॉन्फ़िगरेशन
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

### प्रोलॉग प्रोग्राम चलाना
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

### कॉन्फ़िगरेशन बनाएँ
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

## परीक्षण एवं डिबगिंग
### बिल्ट-इन ट्रेसिंग
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

### PLUnit के साथ यूनिट परीक्षण
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

### सामान्य डिबगिंग पैटर्न
| समस्या | लक्षण | समाधान |
|---------|---------|----------|
| अनंत प्रत्यावर्तन | ढेर अतिप्रवाह | आधार मामले की जाँच करें; समाप्ति शर्त जोड़ें |
| कोई समाधान नहीं | क्वेरी झूठी आती है | परिवर्तनीय तात्कालिकता क्रम की जाँच करें |
| बहुत सारे समाधान | अप्रत्याशित डुप्लिकेट | कट (!) जोड़ें या`setof`| का उपयोग करें
| ग़लत एकीकरण | वेरिएबल गलत तरीके से बंधे हैं | परीक्षण करने के लिए`=`का उपयोग करें; फ़ैक्टर एरीटी की जाँच करें |
| प्रदर्शन मुद्दा | धीमा निष्पादन | कटौती जोड़ें;`table`का उपयोग करें; चयन बिंदुओं की जांच करें |
---

## अंतरसंचालनीयता
### सी इंटरफ़ेस (एफएफआई)
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

### पायथन एकीकरण
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

## डिज़ाइन पैटर्न
### पैटर्न 1: संचायक (पूंछ पुनरावृत्ति)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### पैटर्न 2: स्टेट थ्रेडिंग```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### पैटर्न 3: उत्पन्न करें और परीक्षण करें```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### पैटर्न 4: अंतर सूचियाँ```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## प्रदर्शन एवं अनुकूलन
### कट अनुकूलन
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### पूँछ प्रत्यावर्तन
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### अनुकूलन चेकलिस्ट
| तकनीक | प्रभाव | विवरण |
|----|-------|----|
| **पूंछ प्रत्यावर्तन** | उच्च | स्थिर स्टैक स्थान के लिए संचायक का उपयोग करें |
| **कट (हरा)** | उच्च | अनावश्यक विकल्प बिंदुओं को हटा दें |
| **सारणीबद्ध मूल्यांकन** | उच्च | `:- table pred/N`परिणाम याद रखता है |
| **अनुक्रमण** | मध्यम | भेदभावपूर्ण तर्क को पहले रखें |
| **अंतर सूचियाँ** | मध्यम | O(1) सूची संयोजन |
| **सीएलपी(एफडी) ओवर जनरेट-टेस्ट** | बहुत ऊँचा | पाशविक बल के स्थान पर बाधाओं का प्रयोग करें |
---

## परिनियोजन और वास्तविक दुनिया में उपयोग
### प्रोलॉग एप्लिकेशन परिनियोजित करना
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### वास्तविक दुनिया के अनुप्रयोग
| डोमेन | प्रोलॉग का उपयोग कैसे किया जाता है | उदाहरण |
|--------|-----|----|
| **विशेषज्ञ प्रणालियाँ** | चिकित्सा निदान, दोष का पता लगाना | माइसीन, एक्सकॉन |
| **एनएलपी** | व्याकरण विश्लेषण, शब्दार्थ विश्लेषण | चैटबॉट्स, क्यूए सिस्टम |
| **प्रकार का अनुमान** | हिंडले-मिलनर प्रकार की जाँच | हास्केल/एमएल प्रोटोटाइप |
| **शेड्यूलिंग** | कर्मचारी शेड्यूलिंग, समय सारिणी | एयरलाइन क्रू शेड्यूलिंग |
| **कानूनी तर्क** | नियम आधारित कानूनी विश्लेषण | अनुपालन जांच |
| **डेटाबेस क्वेरी** | डेटा विश्लेषण के लिए डेटालॉग | सूफले इंजन |
| **सत्यापन** | मॉडल चेकिंग | हार्डवेयर सत्यापन |
| **आईबीएम वॉटसन** | प्राकृतिक भाषा समझ | ख़तरे में! सिस्टम |
| **एरिक्सन** | दूरसंचार प्रबंधन | नेटवर्क कॉन्फ़िगरेशन सत्यापन |
---

## प्रोलॉग का उपयोग कब करें
| परिदृश्य | प्रोलॉग क्यों | बेहतर विकल्प |
|---|----|-----|
| नियम आधारित तर्क | इसके लिए प्रोलॉग बनाया गया है | पायथन/जावा में कस्टम नियम इंजन |
| बाधा संतुष्टि | सीएलपी(एफडी) सुंदर और कुशल है | बड़े उदाहरणों के लिए SAT सॉल्वर, OR-टूल्स |
| व्याकरण/भाषा विश्लेषण | डीसीजी (निश्चित खंड व्याकरण) मूल निवासी हैं | उत्पादन के लिए पार्सर जेनरेटर (एएनटीएलआर, वाईएसीसी) |
| विशेषज्ञ प्रणालियाँ | प्राकृतिक फिट - तथ्य + नियम = विशेषज्ञ प्रणाली | बिजनेस रूल इंजन (ड्रोल्स) |
| शेड्यूलिंग / समय सारिणी | सीएलपी इन्हें अच्छे से हल करता है | OR-टूल्स, ऑप्टाप्लानर |
| सिस्टम रिसर्च टाइप करें | एकीकरण ही बुनियाद है | OCaml, हास्केल, रस्ट में लागू करें |
| वेब अनुप्रयोग | अनुकूल नहीं | पायथन, नोड.जेएस, गो |
| डेटा साइंस/एमएल | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
| प्रदर्शन-महत्वपूर्ण कोड | गणना के लिए प्रोलॉग धीमा है | सी, सी++, जंग |
| सामान्य प्रयोजन प्रोग्रामिंग | संभव लेकिन अजीब | पायथन, गो, जावा |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: प्रोलॉग का एकीकरण अन्य भाषाओं में असाइनमेंट से कैसे भिन्न है?
**ए:** एकीकरण द्विदिशात्मक पैटर्न मिलान है, असाइनमेंट नहीं:
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

### Q2: प्रोलॉग में बैकट्रैकिंग कैसे काम करती है?
**ए:** जब कोई लक्ष्य विफल हो जाता है, तो प्रोलॉग अंतिम विकल्प बिंदु पर वापस जाता है और अगले विकल्प का प्रयास करता है:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: मैं प्रोलॉग में सूचियों के साथ कैसे काम करूं?
**ए:** सूचियाँ हेड/टेल पैटर्न मिलान का उपयोग करती हैं:
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

### Q4: मुझे अन्य भाषाओं के बजाय प्रोलॉग का उपयोग कब करना चाहिए?
**ए:** प्रोलॉग यहां उत्कृष्ट है:
- बाधा संतुष्टि (शेड्यूलिंग, पहेलियाँ)
- नियम-आधारित प्रणालियाँ (विशेषज्ञ प्रणालियाँ, सत्यापन)
- ग्राफ़/वृक्ष ट्रैवर्सल
- प्राकृतिक भाषा प्रसंस्करण
- प्रतीकात्मक गणना
- तार्किक संबंधों के रूप में व्यक्त की जाने वाली कोई भी समस्या
### Q5: प्रोलॉग में आम खामियाँ क्या हैं?
**ए:** मुख्य मुद्दे:
- अनंत पुनरावर्तन - हमेशा आधार केस को पहले रखें
- अनपेक्षित बैकट्रैकिंग - कट`!`या`once/1`का उपयोग करें 
- चेक होता है - डिफ़ॉल्ट रूप से`X = f(X)`लूप (`unify_with_occurs_check` का उपयोग करें)
- हरा कट (अनुकूलन) बनाम लाल कट (अर्थ परिवर्तन) - हरे रंग को प्राथमिकता दें
---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एन-क्वींस पहेली को हल करना
**चरण 1: समस्या को समझें**
N रानियों को NxN शतरंज की बिसात पर रखें ताकि कोई भी दो रानियाँ एक दूसरे पर हमला न करें।
**चरण 2: दृष्टिकोण को पहचानें**
बाधा-आधारित पीढ़ी का उपयोग करें: सुरक्षा की जाँच करते हुए, क्वींस कॉलम को कॉलम द्वारा रखें।
**चरण 3: कार्यान्वयन**```prolog
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

**चरण 4: सत्यापित करें**
`?- n_queens(8, Qs).`को 92 समाधान खोजने चाहिए।
### समस्या 2: एक सरल विशेषज्ञ प्रणाली का निर्माण
**चरण 1: समस्या को समझें**
लक्षणों के आधार पर कार की समस्याओं का निदान करें।
**चरण 2: दृष्टिकोण को पहचानें**
नैदानिक ज्ञान को एन्कोड करने के लिए प्रोलॉग नियमों का उपयोग करें।
**चरण 3: कार्यान्वयन**```prolog
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

**चरण 4: विस्तार करें**
आत्मविश्वास स्कोर जोड़ें, उपयोगकर्ता से लक्षणों के बारे में अंतःक्रियात्मक रूप से पूछें, और श्रृंखलाबद्ध निदान करें।
---

## सारांश
प्रोलॉग किसी भी अन्य प्रोग्रामिंग भाषा से भिन्न है। चरण-दर-चरण निर्देश लिखने के बजाय, आप रिश्तों और बाधाओं का वर्णन करते हैं - और इंजन तार्किक अनुमान के माध्यम से समाधान खोजता है। यह प्रोलॉग को उन समस्याओं के लिए आदर्श बनाता है जो अनिवार्य भाषाओं में अजीब या वाचाल हैं: विशेषज्ञ प्रणाली, शेड्यूलिंग, व्याकरण पार्सिंग, बाधा संतुष्टि, और तार्किक नियमों से जुड़ी कोई भी चीज़। अधिकांश प्रोग्रामर उत्पादन में कभी भी प्रोलॉग का उपयोग नहीं करेंगे, लेकिन इसे सीखने से प्रोग्रामिंग क्या हो सकती है, इसके बारे में आपकी सोच का विस्तार होता है। एकीकरण, बैकट्रैकिंग और घोषणात्मक समस्या विनिर्देश ऐसी अवधारणाएं हैं जो भाषा डिजाइन, एआई अनुसंधान और यहां तक ​​कि डेटाबेस क्वेरी अनुकूलन को प्रभावित करती हैं।
### प्रोलॉग इंजन तुलना
| फ़ीचर | SWI-प्रोलॉग | जीएनयू प्रोलॉग | ताऊ प्रोलॉग |
|--|----||--|---||
| **लाइसेंस** | बीएसडी (खुला स्रोत) | जीपीएल (खुला स्रोत) | बीएसडी (खुला स्रोत) |
| **मंच** | विंडोज़, लिनक्स, मैकओएस | विंडोज़, लिनक्स, मैकओएस | जावास्क्रिप्ट (ब्राउज़र) |
| **सीएलपी(एफडी)** | अंतर्निर्मित पुस्तकालय | अंतर्निर्मित | उपलब्ध नहीं है |
| **डीसीजी समर्थन** | पूर्ण | पूर्ण | सीमित |
| **टेबलिंग** | हाँ | नहीं | नहीं |
| **एफएफआई (सी कॉल)** | हाँ | हाँ | जावास्क्रिप्ट के माध्यम से |
| **नेटवर्किंग** | HTTP, टीसीपी, टीएलएस | टीसीपी | जावास्क्रिप्ट के माध्यम से |
| **मल्टी-थ्रेडिंग** | हाँ | नहीं | नहीं |
| **पैकेज मैनेजर** | `pack_install/1`| कोई नहीं | एनपीएम |
| **के लिए सर्वश्रेष्ठ** | उत्पादन, अनुसंधान | बाधा निवारण | वेब ऐप्स, शिक्षा |
### पेंगिन्स के साथ वेब एप्लिकेशन
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

### जोर देने/वापस लेने के साथ मेटाप्रोग्रामिंग
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
