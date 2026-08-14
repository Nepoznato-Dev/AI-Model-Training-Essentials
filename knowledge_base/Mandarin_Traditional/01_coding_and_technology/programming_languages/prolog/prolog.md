---
# Metadata
title: "Prolog"
description: "Comprehensive reference for the Prolog programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "AI Model Training Team"
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
Prolog（邏輯程式設計）是一種邏輯程式語言，由 Alain Colmerauer 和 Philippe Roussel 於 1972 年創建。與此列表中的所有其他語言不同，Prolog 不會告訴計算機“如何”解決問題 - 您聲明“什麼”是真實的（事實和規則），Prolog 的推理引擎通過邏輯演繹找出答案。
Prolog 是 20 世紀 80 年代專家系統、自然語言處理和人工智慧研究的首選語言。它為日本第五代電腦系統專案提供了動力，並在 IBM 的 Watson 中用於自然語言理解。如今，Prolog 被用於約束求解、調度、類型推斷、法律推理以及任何自然地表達為邏輯關係的問題。
**約束邏輯程式設計 (CLP)** 使用約束求解器擴展了 Prolog，用於調度、路由和資源分配 — 這些問題在命令式語言中極其困難。
---

## 為什麼 Prolog 很重要
- **声明式编程**：描述什么是真实的，而不是如何计算它。引擎完成工作。
- **模式匹配和统一**：Prolog的统一算法比其他语言中的模式匹配更强大。
- **回溯搜索**：自动探索所有可能的解决方案。無需手動搜尋演算法。
- **自然适合逻辑问题**：专家系统、规则引擎、类型检查器、语法解析器 - 这些直接映射到 Prolog。
- **约束求解**：CLP(FD) 优雅地解决了调度、分配和组合问题。
- **不同的思维**：学习 Prolog 会改变您解决问题的方式 - 您开始思考关系和约束。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **非常不同的範式** |沒有變數（只有綁定）、沒有循環、沒有賦值 |思考關係和遞歸，而不是狀態變化 |
| **效能** |數值計算與大數據速度慢 |用於推理；將計算委託給 C/其他語言 |
| **調試難度** |回溯難、統一失敗|使用追蹤/調試工具；編寫確定性謂詞 |
| **剪切運算子 (!)** |需要效率但破壞了邏輯純度 |盡可能使用 if-then-else 或表格評估 |
| **有限的生態系統** |很少有函式庫、框架或社群資源 | SWI-Prolog 是最完整的實作 |
| **不適用於一般應用程式** | Web、行動、GUI — 不是 Prolog 的強項 |用作網頁應用程式背後的推理引擎 |
---

## 文法基礎知識
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

## 進階語法和模式
### 統一深入探討
統一是 Prolog 的核心機制——它是 Prolog 「匹配」術語和綁定變數的方式。
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

### 回溯與選擇點
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

### 定子句語法 (DCG)
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

### 約束邏輯程式設計 (CLP)
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

## 架構與系統設計
### 邏輯程式設計範式
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

### 典型的專案結構
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

### 模組系統
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

## 專案配置與建置系統
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

### 執行 Prolog 程式
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

### 建置配置
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

## 測試和調試
### 內建追蹤
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

### 使用 PLUnit 進行單元測試
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

### 常見偵錯模式
|問題 |症狀|解決方案 |
|---------|---------|----------|
|无限递归|堆栈溢出|检查基本情况；添加终止条件 |
|没有解决方案 |查询返回 false |检查变量实例化顺序 |
|解决方案太多 |意外重复 |添加剪切 (!) 或使用`setof`|
|错误的统一|变量绑定不正确 |使用`=`进行测试；检查函子数量 |
|性能问题|执行缓慢|添加削减；使用`table`；检查选择点|
---

## 互通性
### C 介面 (FFI)
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

## 設計模式
### 模式 1：累加器（尾遞歸）```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### 模式 2：狀態執行緒```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### 模式 3：產生並測試```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### 模式 4：差異列表```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## 效能與最佳化
### 削減優化
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### 尾遞迴
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### 優化清單
|技術|影響 |描述 |
|------------|--------|-------------|
| **尾遞歸** |高|使用累加器獲得恆定的堆疊空間 |
| **切割（綠）** |高|消除不必要的選擇點|
| **提交評估** |高|`:- table pred/N`記憶結果 |
| **索引** |中|將區分論證放在第一位 |
| **差異列表** |中| O(1) 列表串聯 |
| **CLP(FD) 通過產生測試** |非常高 |使用約束而不是暴力 |
---

## 部署和實際使用
### 部署 Prolog 應用程式
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### 實際應用
|網域 | Prolog 如何使用 |範例|
|--------|--------------------|---------|
| **專家系統** |醫療診斷、故障檢測|黴素、XCON |
| **自然語言處理** |語法解析、語意分析 |聊天機器人、QA 系統 |
| **類型推論** | Hindley-Milner 類型檢查 | Haskell/ML 原型 |
| **日程安排** |員工排班、時間表|航空公司機組人員調度|
| **法律推理** |基於規則的法律分析|合規檢查|
| **資料庫查詢** |用於資料分析的Datalog |舒芙蕾引擎|
| **驗證** |模型檢驗 |硬體驗證|
| **IBM 沃森** |自然語言理解 |危險！系統|
| **愛立信** |電信管理|網路設定驗證 |
---

## 何時使用 Prolog
|場景|為什麼選擇 Prolog |更好的選擇|
|----------|----------|--------------------|
|基於規則的推理 | Prolog 就是為此而構建的 | Python/Java 中的自訂規則引擎 |
|約束滿足| CLP(FD)優雅高效 | SAT 求解器，適用於大型實例的 OR 工具 |
|語法/語言解析| DCG（定語子句語法）是原生的 |用於生產的解析器產生器（ANTLR、yacc）|
|專家系統|自然契合－事實+規則=專家系統|業務規則引擎（Drools）|
|日程安排/時間表| CLP很好地解決了這些問題 | OR-工具、OptaPlanner |
|類型系統研究|統一是基礎|在 OCaml、Haskell、Rust 中實現 |
|網頁應用程式|不適合| Python、Node.js、Go |
|資料科學/機器學習 |不是生態系| Python、R |
|效能關鍵程式碼 | Prolog 的運算速度很慢 | C、C++、Rust |
|通用程式設計 |可能但尷尬| Python、Go、Java |
---

## 綜合問答
### Q1：Prolog 的統一與其他語言的賦值有何不同？
**A:** 統一是雙向模式匹配，而不是賦值：
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

### Q2：Prolog 中的回溯是如何運作的？
**A:** 當目標失敗時，Prolog 回溯到上一個選擇點並嘗試下一個替代點：
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3：如何在 Prolog 中使用清單？
**A:** 清單使用頭/尾模式匹配：
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

### Q4：什麼時候應該使用Prolog而不是其他語言？
**答：** Prolog 擅長：
- 約束滿足（調度、謎題）
- 基於規則的系統（專家系統、驗證）
- 圖/樹遍歷
- 自然語言處理
- 符號計算
- 任何可以表達為邏輯關係的問題
### Q5：Prolog 中常見的陷阱有哪些？
**答：** 關鍵問題：
- 無限遞歸－永遠將基本情況放在第一位
- 意外回溯 — 使用剪切`!`或 `once/1`
- 發生檢查 — 預設情況下`X = f(X)`循環（使用`unify_with_occurs_check`）
- 綠色剪切（優化）與紅色剪切（改變含義）—更喜歡綠色
---

## 解決問題的思路
### 問題 1：解決 N 皇后難題
**第 1 步：了解問題**
將 N 個皇后放在 NxN 棋盤上，這樣兩個皇后就不會互相攻擊。
**第 2 步：確定方法**
使用基於約束的生成：逐列放置皇后，檢查安全性。
**步驟 3：實施**```prolog
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

**第 4 步：驗證**
`?- n_queens(8, Qs).`應該找到 92 個解決方案。
### 問題 2：建立一個簡單的專家系統
**第 1 步：了解問題**
根據症狀診斷汽車問題。
**第 2 步：確定方法**
使用 Prolog 規則對診斷知識進行編碼。
**步驟 3：實施**```prolog
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

**第 4 步：擴充**
新增置信度分數，以互動方式詢問使用者症狀，並進行連鎖診斷。
---

＃＃ 概括
Prolog 有別於任何其他程式語言。您無需編寫逐步說明，而是描述關係和約束，並且引擎透過邏輯推理搜尋解決方案。這使得 Prolog 成為解決命令式語言中棘手或冗長問題的理想選擇：專家系統、調度、語法分析、約束滿足以及任何涉及邏輯規則的問題。大多數程式設計師永遠不會在生產中使用 Prolog，但是學習它可以擴展您對程式設計的思考。統一、回溯和聲明性問題規範是影響語言設計、人工智慧研究甚至資料庫查詢最佳化的概念。
### Prolog 引擎比較
|特色| SWI-Prolog | GNU 序言 | Tau 序言 |
|--------|---------|------------|------------|
| **許可證** | BSD（開源）| GPL（開源）| BSD（開源）|
| **平台** | Windows、Linux、macOS | Windows、Linux、macOS | JavaScript（瀏覽器）|
| **中電(FD)** |內建庫|內建|不可用 |
| **DCG 支援** |完整|完整|有限公司|
| **表格** |是的 |沒有 |沒有 |
| **FFI（C 呼叫）** |是的 |是的 |透過 JavaScript |
| **網路** | HTTP、TCP、TLS | TCP |透過 JavaScript |
| **多執行緒** |是的 |沒有 |沒有 |
| **套件管理器** |`pack_install/1`|無 | npm |
| **最適合** |生產、研究|約束求解|網路應用程式、教育 |
### 使用 Pengines 的 Web 應用程式
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

### 使用斷言/撤回進行元編程
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
