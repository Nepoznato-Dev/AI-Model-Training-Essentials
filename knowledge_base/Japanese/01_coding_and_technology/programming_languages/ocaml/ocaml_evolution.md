---
# Metadata
title: "OCaml — Version History & Evolution"
description: "Comprehensive version history and evolution of OCaml from Caml to modern OCaml."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ocaml, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# OCaml — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|キャメル | 1985年 | **カテゴリカル抽象機械言語** (INRIA) |
|キャムライト | 1990年 |ライトウェイト キャメル (ザビエル・ルロワ) |
| OCaml 1.0 | 1996年 | **Objective Caml** — OOP を追加します |
| OCaml 3.0 | 2000年 | **主要**: ポリモーフィック メソッド、`lazy`、`Obj`|
| OCaml 3.05 | 2002年 |ネイティブ コード コンパイラの改善 |
| OCaml 3.10 | 2007年 |  クラス定義内の`module type of`、`let`バインディング |
| OCaml 3.11 | 2008年 | `private`型の注釈、`module type of` |
| OCaml 3.12 | 2010年 |ファーストクラスのモジュール |
| OCaml 4.00 | 2012年 | **主要**: 署名内の`module type of`、`val`|
| OCaml 4.01 | 2013年 | `Bytes`モジュール (可変文字列を分離) |
| OCaml 4.02 | 2014年 | `Float`モジュール、`String` の改善 |
| OCaml 4.03 | 2016年 | `Result`タイプ、`Seq` (遅延シーケンス) |
| OCaml 4.04 | 2017年 |時空プロファイラー、`floatarray` |
| OCaml 4.06 | 2018年 | `module`式の`let`バインディング
| OCaml 4.08 | 2019年 | `Binding`の改善、`Seq` の改善 |
| OCaml 4.10 | 2020年 | `Bigarray`の改善 |
| OCaml 4.12 | 2021年 | `Stdlib`の改善 |
| OCaml 4.14 | 2022年 | **テールモジュロコン** (TMC) |
| OCaml 5.0 | 2022年 | **主要**: エフェクト ハンドラー、並列処理 (GIL なし) |
| OCaml 5.1 | 2023年 | `Domain`の改善、`Effect` の改善 |
| OCaml 5.2 | 2024年 |エラー メッセージの改善、`Domain` の改善 |
| OCaml 5.3 | 2025年 |進行中の開発 |
## 主要なマイルストーン
### キャメル (1985–1995)
- **1985**: ジェラール ユエが INRIA (フランス) で Caml を作成
- **名前**: 「カテゴリカル抽象マシン言語」
- **1990**: Caml Light — ザビエル・ルロワによる軽量バージョン
- パターンマッチング、Hindley-Milner 型推論
### OCaml 1.0–3.x: OOP の追加 (1996–2011)
- **1996**: OCaml (Objective Caml) — オブジェクト指向機能を追加
- **3.0 (2000)**: 多態性メソッド、`lazy` 評価
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **ファーストクラス モジュール** — 値としてのモジュール
### OCaml 4.x: 最新の OCaml (2012–2021)
- **4.00 (2012)**:`module type of`、モジュール システムの改善
- **4.01 (2013)**:`Bytes`モジュール — デフォルトで不変の文字列
- **4.03 (2016)**:`Result`タイプ、`Seq` (遅延シーケンス)
- **4.08 (2019)**: エラー メッセージを改善しました
- **4.14 (2022)**: Tail-modulo-cons (TMC) — 再帰的コンストラクターのメモリの向上
### OCaml 5.x: パラレル革命 (2022 ～現在)
- **5.0 (2022)**: **エフェクト ハンドラー**、**真の並列処理** (純粋なコードの GIL を削除)
  -`Domain`— 並列計算用の OS スレッド
  -`Effect`— 代数効果ハンドラー (続き)
  - グローバル インタプリタ ロックはもう不要 — 本物のマルチコア OCaml
- **5.1 (2023)**: ドメインの改善、エフェクト ハンドラーの改良
- **5.2 (2024)**: エラー メッセージの改善、さらなる改善
## 構文の進化
```ocaml
(* OCaml 3.x: Pattern matching, modules *)
type shape =
  | Circle of float
  | Rectangle of float * float

let area = function
  | Circle r -> Float.pi *. r *. r
  | Rectangle (w, h) -> w *. h

(* OCaml 3.12: First-class modules *)
module type Printable = sig
  val to_string : t -> string
end

let print (module M : Printable) x =
  print_endline (M.to_string x)

(* OCaml 4.03: Result type *)
let safe_divide x y =
  if y = 0 then Error "division by zero"
  else Ok (x / y)

(* OCaml 4.08: Better error messages *)
let x = 1 +. 2
(* Error: This expression has type int but an expression was expected of type float *)

(* OCaml 5.0: Effect handlers *)
type _ Effect.t += Read : string Effect.t

let with_input input f =
  Effect.Deep.try_with f ()
    { effc = fun (type a) (eff : a Effect.t) ->
        match eff with
        | Read -> Some (fun (k : (a, _) Effect.Deep.continuation) ->
            Effect.Deep.continue k input)
        | _ -> None }

(* OCaml 5.0: Parallelism with Domain *)
let parallel_map f list =
  let domains = List.map (fun x ->
    Domain.spawn (fun () -> f x)
  ) list in
  List.map Domain.join domains

(* OCaml: Functor (module parameter) *)
module MakeSet (Ord : Map.OrderedType) = Set.Make(Ord)
module IntSet = MakeSet(struct type t = int let compare = compare end)
```

## 型システムの進化
```
Caml (1985):       Hindley-Milner type inference, pattern matching
Caml Light (1990): Modules, functors
OCaml 1.0 (1996):  Objects, classes, inheritance
OCaml 3.0 (2000):  Polymorphic methods, lazy
OCaml 3.12 (2010): First-class modules
OCaml 4.03 (2016): Result, Seq
OCaml 4.14 (2022): Tail-modulo-cons
OCaml 5.0 (2022):  Effect handlers, Domain (parallelism)
```

## 主要な設計原則
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## エコシステムの成長
```
1985: Caml created at INRIA (France)
1990: Caml Light — lightweight version
1996: OCaml — adds OOP
2002: Jane Street adopts OCaml — financial trading
2010: First-class modules
2012: OPAM package manager
2016: OCaml 4.03 — Result type
2022: OCaml 5.0 — effect handlers, parallelism
2025: OCaml used in:
       - Jane Street (financial trading, largest OCaml shop)
       - Facebook/Flow (JavaScript type checker)
       - Tezos (blockchain)
       - Coq (theorem prover)
       - Infer (Facebook's static analyzer)
       - Ocsigen (web framework)
       Compilers: ocamlc (bytecode), ocamlopt (native)
       Tools: dune (build), opam (packages), merlin (IDE)
```
