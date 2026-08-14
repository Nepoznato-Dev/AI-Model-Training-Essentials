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
# Prolog

Prolog (Programming in Logic) is a logic programming language created in 1972 by Alain Colmerauer and Philippe Roussel. Unlike every other language on this list, Prolog does not tell the computer *how* to solve a problem — you declare *what* is true (facts and rules), and Prolog's inference engine figures out the answer through logical deduction.

Prolog was the language of choice for expert systems, natural language processing, and AI research in the 1980s. It powered Japan's Fifth Generation Computer System project and was used in IBM's Watson for natural language understanding. Today, Prolog is used in constraint solving, scheduling, type inference, legal reasoning, and anywhere problems are naturally expressed as logical relationships.

**Constraint Logic Programming (CLP)** extends Prolog with constraint solvers for scheduling, routing, and resource allocation — problems that are extremely difficult in imperative languages.

---

## Why Prolog Matters

- **Declarative programming**: Describe what is true, not how to compute it. The engine does the work.
- **Pattern matching and unification**: Prolog's unification algorithm is more powerful than pattern matching in other languages.
- **Backtracking search**: Automatically explores all possible solutions. No manual search algorithms needed.
- **Natural for logic problems**: Expert systems, rule engines, type checkers, grammar parsers — these map directly to Prolog.
- **Constraint solving**: CLP(FD) solves scheduling, allocation, and combinatorial problems elegantly.
- **Different thinking**: Learning Prolog changes how you approach problem-solving — you start thinking in relationships and constraints.

## The Trade-offs

| Limitation | Details | Typical Workaround |
|-----------|---------|-------------------|
| **Very different paradigm** | No variables (only bindings), no loops, no assignments | Think in relations and recursion, not state changes |
| **Performance** | Slow for numerical computation and large data | Use for reasoning; delegate computation to C/other languages |
| **Debugging difficulty** | Hard to trace backtracking and unification failures | Use trace/debug tools; write deterministic predicates |
| **Cut operator (!)** | Needed for efficiency but breaks logical purity | Use if-then-else or tabled evaluation when possible |
| **Limited ecosystem** | Few libraries, frameworks, or community resources | SWI-Prolog is the most complete implementation |
| **Not for general apps** | Web, mobile, GUI — not Prolog's strength | Use as a reasoning engine behind a web app |

---

## Syntax Fundamentals

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

## Advanced Syntax & Patterns

### Unification Deep Dive

Unification is Prolog's core mechanism — it is how Prolog "matches" terms and binds variables.

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

### Backtracking and Choice Points

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

### Definite Clause Grammars (DCGs)

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

### Constraint Logic Programming (CLP)

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

## Architecture & System Design

### Logic Programming Paradigm

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

### Typical Project Structure

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

### Module System

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

## Project Configuration & Build System

### SWI-Prolog Configuration

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

### Running Prolog Programs

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

### Build Configuration

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

## Testing & Debugging

### Built-in Tracing

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

### Unit Testing with PLUnit

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

### Common Debugging Patterns

| Problem | Symptom | Solution |
|---------|---------|----------|
| Infinite recursion | Stack overflow | Check base case; add termination condition |
| No solutions | Query returns false | Check variable instantiation order |
| Too many solutions | Unexpected duplicates | Add cut (!) or use `setof` |
| Wrong unification | Variables bound incorrectly | Use `=` to test; check functor arity |
| Performance issue | Slow execution | Add cuts; use `table`; check choice points |

---

## Interoperability

### C Interface (FFI)

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

### Python Integration

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

## Design Patterns

### Pattern 1: Accumulator (Tail Recursion)
```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Pattern 2: State Threading
```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Pattern 3: Generate and Test
```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Pattern 4: Difference Lists
```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Performance & Optimization

### Cut Optimization

```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Tail Recursion

```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Optimization Checklist

| Technique | Impact | Description |
|-----------|--------|-------------|
| **Tail recursion** | High | Use accumulators for constant stack space |
| **Cut (green)** | High | Eliminate unnecessary choice points |
| **Tabled evaluation** | High | `:- table pred/N` memoizes results |
| **Indexing** | Medium | Put discriminating argument first |
| **Difference lists** | Medium | O(1) list concatenation |
| **CLP(FD) over generate-test** | Very High | Use constraints instead of brute-force |

---

## Deployment & Real-World Usage

### Deploying Prolog Applications

```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Real-World Applications

| Domain | How Prolog Is Used | Example |
|--------|-------------------|---------|
| **Expert systems** | Medical diagnosis, fault detection | MYCIN, XCON |
| **NLP** | Grammar parsing, semantic analysis | Chatbots, QA systems |
| **Type inference** | Hindley-Milner type checking | Haskell/ML prototypes |
| **Scheduling** | Employee scheduling, timetabling | Airline crew scheduling |
| **Legal reasoning** | Rule-based legal analysis | Compliance checking |
| **Database querying** | Datalog for data analysis | Soufflé engine |
| **Verification** | Model checking | Hardware verification |
| **IBM Watson** | Natural language understanding | Jeopardy! system |
| **Ericsson** | Telecom management | Network config validation |

---

## When to Use Prolog

| Scenario | Why Prolog | Better Alternative |
|----------|-----------|-------------------|
| Rule-based reasoning | Prolog is built for this | Custom rule engines in Python/Java |
| Constraint satisfaction | CLP(FD) is elegant and efficient | SAT solvers, OR-Tools for large instances |
| Grammar / language parsing | DCG (Definite Clause Grammars) are native | Parser generators (ANTLR, yacc) for production |
| Expert systems | Natural fit — facts + rules = expert system | Business rule engines (Drools) |
| Scheduling / timetabling | CLP solves these well | OR-Tools, OptaPlanner |
| Type system research | Unification is the foundation | Implement in OCaml, Haskell, Rust |
| Web applications | Not suited | Python, Node.js, Go |
| Data science / ML | Not the ecosystem | Python, R |
| Performance-critical code | Prolog is slow for computation | C, C++, Rust |
| General-purpose programming | Possible but awkward | Python, Go, Java |

---

## Synthetic Q&A

### Q1: How does Prolog's unification differ from assignment in other languages?

**A:** Unification is bidirectional pattern matching, not assignment:

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

### Q2: How does backtracking work in Prolog?

**A:** When a goal fails, Prolog backtracks to the last choice point and tries the next alternative:

```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: How do I work with lists in Prolog?

**A:** Lists use head/tail pattern matching:

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

### Q4: When should I use Prolog instead of other languages?

**A:** Prolog excels at:
- Constraint satisfaction (scheduling, puzzles)
- Rule-based systems (expert systems, validation)
- Graph/tree traversal
- Natural language processing
- Symbolic computation
- Any problem expressible as logical relations

### Q5: What are the common pitfalls in Prolog?

**A:** Key issues:
- Infinite recursion — always put the base case first
- Unintended backtracking — use cut `!` or `once/1`
- Occurs check — `X = f(X)` loops by default (use `unify_with_occurs_check`)
- Green cuts (optimization) vs red cuts (change meaning) — prefer green

---

## Chain-of-Thought Problem Solving

### Problem 1: Solving the N-Queens Puzzle

**Step 1: Understand the Problem**
Place N queens on an NxN chessboard so no two queens attack each other.

**Step 2: Identify the Approach**
Use constraint-based generation: place queens column by column, checking safety.

**Step 3: Implement**
```prolog
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

**Step 4: Verify**
`?- n_queens(8, Qs).` should find 92 solutions.

### Problem 2: Building a Simple Expert System

**Step 1: Understand the Problem**
Diagnose car problems based on symptoms.

**Step 2: Identify the Approach**
Use Prolog rules to encode diagnostic knowledge.

**Step 3: Implement**
```prolog
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

**Step 4: Extend**
Add confidence scores, ask the user for symptoms interactively, and chain diagnoses.

---

## Summary

Prolog is unlike any other programming language. Instead of writing step-by-step instructions, you describe relationships and constraints — and the engine searches for solutions through logical inference. This makes Prolog ideal for problems that are awkward or verbose in imperative languages: expert systems, scheduling, grammar parsing, constraint satisfaction, and anything involving logical rules. Most programmers will never use Prolog in production, but learning it expands your thinking about what programming can be. Unification, backtracking, and declarative problem specification are concepts that influence language design, AI research, and even database query optimization.

### Prolog Engines Comparison

| Feature | SWI-Prolog | GNU Prolog | Tau Prolog |
|---------|-----------|------------|------------|
| **License** | BSD (open source) | GPL (open source) | BSD (open source) |
| **Platform** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (browser) |
| **CLP(FD)** | Built-in library | Built-in | Not available |
| **DCG support** | Full | Full | Limited |
| **Tabling** | Yes | No | No |
| **FFI (C calls)** | Yes | Yes | Via JavaScript |
| **Networking** | HTTP, TCP, TLS | TCP | Via JavaScript |
| **Multi-threading** | Yes | No | No |
| **Package manager** | `pack_install/1` | None | npm |
| **Best for** | Production, research | Constraint solving | Web apps, education |

### Web Applications with Pengines

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

### Metaprogramming with assert/retract

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
