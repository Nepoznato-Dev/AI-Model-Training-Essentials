<!--
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

-->
#プロローグ
Prolog (Programming in Logic) は、1972 年に Alain Colmerauer と Philippe Roussel によって作成された論理プログラミング言語です。このリストにある他の言語とは異なり、Prolog はコンピューターに問題を「どのように」解決するかを指示しません。ユーザーは「何が*」 (事実と規則) を宣言すると、Prolog の推論エンジンが論理的演繹を通じて答えを導き出します。
Prolog は、1980 年代のエキスパート システム、自然言語処理、AI 研究に選ばれた言語でした。これは日本の第 5 世代コンピュータ システム プロジェクトを推進し、自然言語理解のために IBM の Watson で使用されました。現在、Prolog は制約解決、スケジューリング、型推論、法的推論など、問題が論理関係として自然に表現されるあらゆる場所で使用されています。
**制約ロジック プログラミング (CLP)** は、命令型言語では非常に難しい問題である、スケジューリング、ルーティング、リソース割り当てのための制約ソルバーを使用して Prolog を拡張します。
---

## プロローグが重要な理由
- **宣言型プログラミング**: 真実を計算する方法ではなく、何が真実かを説明します。エンジンが仕事をしてくれます。
- **パターン マッチングと統合**: Prolog の統合アルゴリズムは、他の言語のパターン マッチングよりも強力です。
- **バックトラッキング検索**: 考えられるすべての解決策を自動的に探索します。手動の検索アルゴリズムは必要ありません。
- **論理問題には自然**: エキスパート システム、ルール エンジン、型チェッカー、文法パーサー - これらは Prolog に直接マッピングされます。
- **制約解決**: CLP(FD) は、スケジューリング、割り当て、および組み合わせの問題をエレガントに解決します。
- **異なる考え方**: Prolog を学ぶと、問題解決へのアプローチ方法が変わります。関係性や制約の中で考えるようになります。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **非常に異なるパラダイム** |変数なし (バインディングのみ)、ループなし、代入なし |状態変化ではなく関係と再帰で考える |
| **パフォーマンス** |数値計算や大きなデータの場合は遅い |推論に使用します。計算を C/その他の言語に委任する |
| **デバッグの難易度** |バックトラッキングと統合の失敗を追跡するのが困難 |トレース/デバッグ ツールを使用します。決定的述語を書く |
| **カット演算子 (!)** |効率化のためには必要ですが、論理的な純粋性は損なわれます。可能な場合は、if-then-else またはテーブル評価を使用します。
| **限られたエコシステム** |ライブラリ、フレームワーク、コミュニティ リソースが少ない | SWI-Prolog は最も完全な実装です |
| **一般的なアプリには使用できません** | Web、モバイル、GUI — Prolog の強みではない | Web アプリの背後にある推論エンジンとして使用する |
---

## 構文の基礎
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

## 高度な構文とパターン
### 統合の詳細
統一は Prolog の中核メカニズムです。これは、Prolog が用語を「照合」し、変数をバインドする方法です。
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

### バックトラッキングと選択のポイント
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

### 定節文法 (DCG)
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

### 制約ロジックプログラミング (CLP)
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

## アーキテクチャとシステム設計
### ロジックプログラミングパラダイム
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

### 一般的なプロジェクト構造
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

### モジュールシステム
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

## プロジェクトの構成とシステムの構築
### SWI-Prolog 構成
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

### Prolog プログラムの実行
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

### ビルド構成
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

## テストとデバッグ
### 組み込みトレース
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

### PLUnit を使用した単体テスト
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

### 一般的なデバッグ パターン
|問題 |症状 |ソリューション |
|----------|----------|----------|
|無限再帰 |スタックオーバーフロー |基本ケースを確認してください。終了条件を追加 |
|解決策はありません |クエリは false を返します |変数のインスタンス化順序を確認する |
|解決策が多すぎます |予期しない重複 |カット (!) を追加するか、`setof` | を使用します。
|間違った統合 |変数が正しくバインドされていません。`=`を使用してテストします。ファンクターのアリティをチェックする |
|パフォーマンスの問題 |実行が遅い |カットを追加します。`table`を使用します。選択ポイントをチェック |
---

## 相互運用性
### C インターフェイス (FFI)
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

### Python の統合
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

## デザインパターン
### パターン 1: アキュムレータ (末尾再帰)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### パターン 2: 状態のスレッド化```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### パターン 3: 生成とテスト```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### パターン 4: 相違点リスト```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## パフォーマンスと最適化
### カットの最適化
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### 末尾再帰
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### 最適化チェックリスト
|テクニック |影響 |説明 |
|----------|----------|---------------|
| **末尾再帰** |高 |一定のスタック領域にアキュムレータを使用する |
| **カット (グリーン)** |高 |不要な選択ポイントを排除 |
| **評価表** |高 | `:- table pred/N`は結果をメモ化します |
| **インデックス作成** |中 |差別的な議論を最初に置く |
| **相違点リスト** |中 | O(1) リスト連結 |
| **生成テスト上の CLP(FD)** |非常に高い |ブルート フォースの代わりに制約を使用する |
---

## 導入と実際の使用法
### Prolog アプリケーションのデプロイ
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### 現実世界のアプリケーション
|ドメイン | Prolog の使用方法 |例 |
|----------|--------|----------|
| **エキスパート システム** |医療診断、故障検出 |ミシン、XCON |
| **NLP** |文法解析、意味解析 |チャットボット、QA システム |
| **型推論** | Hindley-Milner 型チェック | Haskell/ML プロトタイプ |
| **スケジュール設定** |従業員のスケジュール設定、時間割 |航空会社の乗務員のスケジュール管理 |
| **法的推論** |ルールベースの法的分析 |コンプライアンスチェック |
| **データベースのクエリ** |データ分析のための Datalog |スフレエンジン |
| **検証** |モデルのチェック |ハードウェアの検証 |
| **IBM ワトソン** |自然言語理解 |危険！システム |
| **エリクソン** |通信管理 |ネットワーク構成の検証 |
---

## Prolog を使用する場合
|シナリオ |プロローグを選ぶ理由 |より良い代替案 |
|----------|-----------|--------|
|ルールベースの推論 | Prolog はこのために作られています | Python/Java のカスタム ルール エンジン |
|制約を満たす | CLP(FD) はエレガントで効率的です | SAT ソルバー、大規模インスタンス用の OR ツール |
|文法/言語解析 | DCG (Definite Clause Grammar) はネイティブです |実稼働用のパーサー ジェネレーター (ANTLR、yacc) |
|エキスパートシステム |自然な適合性 — 事実 + ルール = エキスパート システム |ビジネス ルール エンジン (Drools) |
|スケジュール/タイムテーブル作成 | CLP はこれらをうまく解決します | OR ツール、OptaPlanner |
|型システムの研究 |統一は基礎です | OCaml、Haskell、Rustで実装 |
|ウェブアプリケーション |適さない | Python、Node.js、Go |
|データ サイエンス / ML |エコシステムではありません |パイソン、R |
|パフォーマンスが重要なコード | Prolog は計算が遅い | C、C++、Rust |
|汎用プログラミング |可能だが厄介 | Python、Go、Java |
---

## 総合的な Q&A
### Q1: Prolog の統合は他の言語の割り当てとどう違うのですか?
**A:** 統合は双方向のパターン マッチングであり、割り当てではありません。
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

### Q2: Prolog ではバックトラッキングはどのように機能しますか?
**A:** 目標が失敗した場合、Prolog は最後の選択ポイントまで戻り、次の代替案を試みます。
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: Prolog でリストを操作するにはどうすればよいですか?
**A:** リストでは先頭/末尾のパターン マッチングが使用されます。
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

### Q4: 他の言語ではなく Prolog を使用する必要があるのはどのような場合ですか?
**A:** Prolog は次の点で優れています。
- 制約の満足度 (スケジュール、パズル)
- ルールベースのシステム (エキスパート システム、検証)
- グラフ/ツリーのトラバーサル
- 自然言語処理
- 記号計算
- 論理関係として表現できるあらゆる問題
### Q5: Prolog でよくある落とし穴は何ですか?
**A:** 主な問題:
- 無限再帰 — 常に基本ケースを最初に置きます
- 意図しないバックトラッキング — カット`!`または`once/1`を使用します 
- 発生チェック — デフォルトで`X = f(X)`ループ (`unify_with_occurs_check`を使用)
- 緑のカット (最適化) vs 赤のカット (意味の変更) — 緑を好む
---

## 思考連鎖による問題解決
### 問題 1: N-Queens パズルを解く
**ステップ 1: 問題を理解する**
2 人のクイーンが互いに攻撃しないように、N 個のクイーンを NxN チェス盤に配置します。
**ステップ 2: アプローチを特定する**
制約ベースの生成を使用します。安全性を確認しながら列ごとにクイーンを配置します。
**ステップ 3: 実装**```prolog
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

**ステップ 4: 確認**
`?- n_queens(8, Qs).`は 92 個の解を見つける必要があります。
### 問題 2: 単純なエキスパート システムの構築
**ステップ 1: 問題を理解する**
症状に基づいて車の問題を診断します。
**ステップ 2: アプローチを特定する**
Prolog ルールを使用して診断知識をエンコードします。
**ステップ 3: 実装**```prolog
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

**ステップ 4: 延長**
信頼度スコアを追加し、ユーザーにインタラクティブに症状を尋ね、診断を連鎖させます。
---

＃＃ まとめ
Prolog は他のプログラミング言語とは異なります。段階的な手順を記述する代わりに、関係と制約を記述すると、エンジンが論理推論を通じて解決策を検索します。このため、Prolog は、エキスパート システム、スケジューリング、文法解析、制約充足、および論理ルールに関係するあらゆる問題など、命令型言語で厄介な問題や冗長な問題に最適です。ほとんどのプログラマーは本番環境で Prolog を使用することはありませんが、Prolog を学ぶことで、プログラミングとは何なのかについての考えが広がります。統合、バックトラッキング、および宣言的問題仕様は、言語設計、AI 研究、さらにはデータベース クエリの最適化にさえ影響を与える概念です。
### Prolog エンジンの比較
|特集 | SWI-プロローグ | GNU プロローグ |タウ プロローグ |
|----------|-----------|---------------|---------------|
| **ライセンス** | BSD (オープンソース) | GPL (オープンソース) | BSD (オープンソース) |
| **プラットフォーム** | Windows、Linux、macOS | Windows、Linux、macOS | JavaScript（ブラウザ） |
| **CLP(FD)** |内蔵ライブラリ |内蔵 |利用できません |
| **DCG サポート** |フル |フル |限定 |
| **表作成** |はい |いいえ |いいえ |
| **FFI (C 呼び出し)** |はい |はい | JavaScript経由 |
| **ネットワーキング** | HTTP、TCP、TLS | TCP | JavaScript経由 |
| **マルチスレッド** |はい |いいえ |いいえ |
| **パッケージマネージャー** | `pack_install/1`|なし | npm |
| **こんな用途に最適** |生産・研究 |制約の解決 | Web アプリ、教育 |
### Pengines を使用した Web アプリケーション
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

### アサート/リトラクトを使用したメタプログラミング
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
