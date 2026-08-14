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
# 序言
Prolog（逻辑编程）是一种逻辑编程语言，由 Alain Colmerauer 和 Philippe Roussel 于 1972 年创建。与此列表中的所有其他语言不同，Prolog 不会告诉计算机“如何”解决问题 - 您声明“什么”是真实的（事实和规则），Prolog 的推理引擎通过逻辑演绎找出答案。
Prolog 是 20 世纪 80 年代专家系统、自然语言处理和人工智能研究的首选语言。它为日本第五代计算机系统项目提供了动力，并在 IBM 的 Watson 中用于自然语言理解。如今，Prolog 被用于约束求解、调度、类型推断、法律推理以及任何自然地表达为逻辑关系的问题。
**约束逻辑编程 (CLP)** 使用约束求解器扩展了 Prolog，用于调度、路由和资源分配 — 这些问题在命令式语言中极其困难。
---

## 为什么 Prolog 很重要
- **声明式编程**：描述什么是真实的，而不是如何计算它。发动机完成工作。
- **模式匹配和统一**：Prolog的统一算法比其他语言中的模式匹配更强大。
- **回溯搜索**：自动探索所有可能的解决方案。无需手动搜索算法。
- **自然适合逻辑问题**：专家系统、规则引擎、类型检查器、语法解析器 - 这些直接映射到 Prolog。
- **约束求解**：CLP(FD) 优雅地解决了调度、分配和组合问题。
- **不同的思维**：学习 Prolog 会改变您解决问题的方式 - 您开始思考关系和约束。
## 权衡
|限制|详情 |典型解决方法|
|------------|---------|--------------------|
| **非常不同的范式** |没有变量（只有绑定）、没有循环、没有赋值 |思考关系和递归，而不是状态变化 |
| **性能** |数值计算和大数据速度慢 |用于推理；将计算委托给 C/其他语言 |
| **调试难度** |回溯难、统一失败|使用跟踪/调试工具；编写确定性谓词 |
| **剪切运算符 (!)** |需要效率但破坏了逻辑纯度 |尽可能使用 if-then-else 或表格评估 |
| **有限的生态系统** |很少有库、框架或社区资源 | SWI-Prolog 是最完整的实现 |
| **不适用于一般应用程序** | Web、移动、GUI — 不是 Prolog 的强项 |用作网络应用程序背后的推理引擎 |
---

## 语法基础知识
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

## 高级语法和模式
### 统一深入探讨
统一是 Prolog 的核心机制——它是 Prolog “匹配”术语和绑定变量的方式。
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

### 回溯和选择点
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

### 定从句语法 (DCG)
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

### 约束逻辑编程 (CLP)
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

## 架构与系统设计
### 逻辑编程范式
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

### 典型的项目结构
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

### 模块系统
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

## 项目配置和构建系统
### SWI-Prolog 配置
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

### 运行 Prolog 程序
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

### 构建配置
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

## 测试和调试
### 内置跟踪
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

### 使用 PLUnit 进行单元测试
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

### 常见调试模式
|问题 |症状|解决方案 |
|---------|---------|----------|
|无限递归|堆栈溢出|检查基本情况；添加终止条件 |
|没有解决方案 |查询返回 false |检查变量实例化顺序 |
|解决方案太多 |意外重复 |添加剪切 (!) 或使用`setof`|
|错误的统一|变量绑定不正确 |使用`=`进行测试；检查函子数量 |
|性能问题|执行缓慢|添加削减；使用`table`；检查选择点|
---

## 互操作性
### C 接口 (FFI)
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

### Python 集成
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

## 设计模式
### 模式 1：累加器（尾递归）```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### 模式 2：状态线程```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### 模式 3：生成并测试```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### 模式 4：差异列表```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## 性能与优化
### 削减优化
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### 尾递归
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### 优化清单
|技术|影响 |描述 |
|------------|--------|-------------|
| **尾递归** |高|使用累加器获得恒定的堆栈空间 |
| **切割（绿色）** |高|消除不必要的选择点|
| **提交评估** |高| `:- table pred/N`记忆结果 |
| **索引** |中等|将区分性论证放在首位 |
| **差异列表** |中等| O(1) 列表串联 |
| **CLP(FD) 通过生成测试** |非常高 |使用约束而不是暴力 |
---

## 部署和实际使用
### 部署 Prolog 应用程序
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### 实际应用
|域名 | Prolog 如何使用 |示例|
|--------|--------------------|---------|
| **专家系统** |医疗诊断、故障检测|霉素、XCON |
| **自然语言处理** |语法解析、语义分析 |聊天机器人、QA 系统 |
| **类型推断** | Hindley-Milner 类型检查 | Haskell/ML 原型 |
| **日程安排** |员工排班、时间表|航空公司机组人员调度|
| **法律推理** |基于规则的法律分析|合规检查|
| **数据库查询** |用于数据分析的Datalog |舒芙蕾引擎|
| **验证** |模型检验 |硬件验证|
| **IBM 沃森** |自然语言理解 |危险！系统|
| **爱立信** |电信管理|网络配置验证 |
---

## 何时使用 Prolog
|场景|为什么选择 Prolog |更好的选择|
|----------|----------|--------------------|
|基于规则的推理 | Prolog 就是为此而构建的 | Python/Java 中的自定义规则引擎 |
|约束满足| CLP(FD)优雅高效 | SAT 求解器，适用于大型实例的 OR 工具 |
|语法/语言解析| DCG（定语从句语法）是原生的 |用于生产的解析器生成器（ANTLR、yacc）|
|专家系统|自然契合——事实+规则=专家系统|业务规则引擎（Drools）|
|日程安排/时间表| CLP很好地解决了这些问题 | OR-工具、OptaPlanner |
|类型系统研究|统一是基础|在 OCaml、Haskell、Rust 中实现 |
|网络应用程序|不适合| Python、Node.js、Go |
|数据科学/机器学习 |不是生态系统| Python、R |
|性能关键代码 | Prolog 的计算速度很慢 | C、C++、Rust |
|通用编程 |可能但尴尬| Python、Go、Java |
---

## 综合问答
### Q1：Prolog 的统一与其他语言的赋值有何不同？
**A:** 统一是双向模式匹配，而不是赋值：
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

### Q2：Prolog 中的回溯是如何工作的？
**A:** 当目标失败时，Prolog 回溯到上一个选择点并尝试下一个替代点：
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3：如何在 Prolog 中使用列表？
**A:** 列表使用头/尾模式匹配：
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

### Q4：什么时候应该使用Prolog而不是其他语言？
**答：** Prolog 擅长：
- 约束满足（调度、谜题）
- 基于规则的系统（专家系统、验证）
- 图/树遍历
- 自然语言处理
- 符号计算
- 任何可以表达为逻辑关系的问题
### Q5：Prolog 中常见的陷阱有哪些？
**答：** 关键问题：
- 无限递归——始终将基本情况放在第一位
- 意外回溯 — 使用剪切`!`或`once/1`
- 发生检查 — 默认情况下`X = f(X)`循环（使用`unify_with_occurs_check`）
- 绿色剪切（优化）与红色剪切（改变含义）——更喜欢绿色
---

## 解决问题的思路
### 问题 1：解决 N 皇后难题
**第 1 步：了解问题**
将 N 个皇后放在 NxN 棋盘上，这样两个皇后就不会互相攻击。
**第 2 步：确定方法**
使用基于约束的生成：逐列放置皇后，检查安全性。
**步骤 3：实施**```prolog
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

**第 4 步：验证**
`?- n_queens(8, Qs).`应该找到 92 个解决方案。
### 问题 2：构建一个简单的专家系统
**第 1 步：了解问题**
根据症状诊断汽车问题。
**第 2 步：确定方法**
使用 Prolog 规则对诊断知识进行编码。
**步骤 3：实施**```prolog
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

**第 4 步：扩展**
添加置信度分数，以交互方式询问用户症状，并进行连锁诊断。
---

＃＃ 概括
Prolog 不同于任何其他编程语言。您无需编写分步说明，而是描述关系和约束，并且引擎通过逻辑推理搜索解决方案。这使得 Prolog 成为解决命令式语言中棘手或冗长问题的理想选择：专家系统、调度、语法分析、约束满足以及任何涉及逻辑规则的问题。大多数程序员永远不会在生产中使用 Prolog，但是学习它可以扩展您对编程的思考。统一、回溯和声明性问题规范是影响语言设计、人工智能研究甚至数据库查询优化的概念。
### Prolog 引擎比较
|特色| SWI-Prolog | GNU 序言 | Tau 序言 |
|--------|---------|------------|------------|
| **许可证** | BSD（开源）| GPL（开源）| BSD（开源）|
| **平台** | Windows、Linux、macOS | Windows、Linux、macOS | JavaScript（浏览器）|
| **中电(FD)** |内置库|内置|不可用 |
| **DCG 支持** |完整|完整|有限公司|
| **表格** |是的 |没有 |没有 |
| **FFI（C 调用）** |是的 |是的 |通过 JavaScript |
| **网络** | HTTP、TCP、TLS | TCP |通过 JavaScript |
| **多线程** |是的 |没有 |没有 |
| **包管理器** | `pack_install/1`|无 | npm |
| **最适合** |生产、研究|约束求解|网络应用程序、教育 |
### 使用 Pengines 的 Web 应用程序
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

### 使用断言/撤回进行元编程
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
