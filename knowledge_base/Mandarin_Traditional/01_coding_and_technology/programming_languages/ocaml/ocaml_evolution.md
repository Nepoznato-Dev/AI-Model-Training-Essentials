<!--
---
# Metadata
title: "OCaml — Version History & Evolution"
description: "Comprehensive version history and evolution of OCaml from Caml to modern OCaml."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# OCaml — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|卡梅爾 | 1985 | **分類抽象機器語言** (INRIA) |
|駱駝燈| 1990 |輕量級 Caml（Xavier Leroy）|
| OCaml 1.0 | 1996 | **Objective Caml** — 新增 OOP |
| OCaml 3.0 | 2000 | 2000 **主要**：多型方法，`lazy`，`Obj`|
| OCaml 3.05 | 2002 |本機程式碼編譯器改進 |
| OCaml 3.10 | 2007 | 類別定義中的`module type of`、`let`綁定 |
| OCaml 3.11 | 2008 |`private`型別註解、`module type of` |
| OCaml 3.12 | 2010 |一流的模組 |
| OCaml 4.00 | 2012 | **主要**：簽名中的`module type of`、`val`|
| OCaml 4.01 | 2013 |`Bytes`模組（可變字串分隔）|
| OCaml 4.02 | 2014 |`Float`模組、`String` 改進 |
| OCaml 4.03 | 2016 | 2016`Result`型態、`Seq`（惰性序列）|
| OCaml 4.04 | 2017 | 2017時空剖面儀，`floatarray` |
| OCaml 4.06 | 2018 |`module`表達式中的`let`綁定 |
| OCaml 4.08 | 2019 | 2019`Binding`改進、`Seq` 改進 |
| OCaml 4.10 | 2020 |`Bigarray`改進 |
| OCaml 4.12 | 2021 |`Stdlib`改進 |
| OCaml 4.14 | 2022 | 2022 **尾模cons** (TMC) |
| OCaml 5.0 | 2022 | 2022 **主要**：效果處理程序、並行性（無 GIL）|
| OCaml 5.1 | 2023 |`Domain`改進、`Effect` 改進 |
| OCaml 5.2 | 2024 | 2024改進了錯誤訊息，`Domain` 改進 |
| OCaml 5.3 | 2025 | 2025持續發展|
## 主要里程碑
### 卡梅爾 (1985–1995)
- **1985**：Gérard Huet 在 INRIA（法國）創立 Caml
- **名稱**：“分類抽象機器語言”
- **1990**：Caml Light — Xavier Leroy 的輕量版本
- 模式匹配、Hindley-Milner 類型推斷
### OCaml 1.0–3.x：新增 OOP (1996–2011)
- **1996**：OCaml (Objective Caml) — 新增物件導向的功能
- **3.0 (2000)**：多態性方法，`lazy` 評估
- **3.10 (2007)**：`module type of`
- **3.12 (2010)**：**一流模組** — 模組作為值
### OCaml 4.x：現代 OCaml (2012–2021)
- **4.00 (2012)**：`module type of`，改進的模組系統
- **4.01 (2013)**：`Bytes` 模組 — 預設情況下不可變字串
- **4.03 (2016)**：`Result` 類型、`Seq`（惰性序列）
- **4.08 (2019)**：改進了錯誤訊息
- **4.14 (2022)**：Tail-modulo-cons (TMC) — 更好的遞歸建構函式內存
### OCaml 5.x：並行革命（2022 年至今）
- **5.0 (2022)**：**效果處理程序**，**真正的並行性**（刪除純程式碼的 GIL）
  -`Domain`— 用於平行運算的作業系統線程
  -`Effect`— 代數效果處理程序（延續）
  - 不再有全域解釋器鎖 - 真正的多核心 OCaml
- **5.1 (2023)**：域改進、效果處理程序改進
- **5.2 (2024)**：更好的錯誤訊息，進一步改進
## 語法演變
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

## 類型系統的演變
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

## 關鍵設計原則
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## 生態系成長
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
