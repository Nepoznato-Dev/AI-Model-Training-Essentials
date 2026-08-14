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
# OCaml — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
|卡梅尔 | 1985 | **分类抽象机器语言** (INRIA) |
|骆驼灯| 1990 |轻量级 Caml（Xavier Leroy）|
| OCaml 1.0 | 1996 | **Objective Caml** — 添加 OOP |
| OCaml 3.0 | 2000 | 2000 **主要**：多态方法，`lazy`，`Obj`|
| OCaml 3.05 | 2002 |本机代码编译器改进 |
| OCaml 3.10 | 2007 |  类定义中的`module type of`、`let`绑定 |
| OCaml 3.11 | 2008 | `private`类型注释、`module type of` |
| OCaml 3.12 | 2010 |一流的模块 |
| OCaml 4.00 | 2012 | **主要**：签名中的`module type of`、`val`|
| OCaml 4.01 | 2013 | `Bytes`模块（可变字符串分隔）|
| OCaml 4.02 | 2014年| `Float`模块、`String` 改进 |
| OCaml 4.03 | 2016 | 2016 `Result`类型、`Seq`（惰性序列）|
| OCaml 4.04 | 2017 | 2017时空剖面仪，`floatarray` |
| OCaml 4.06 | 2018 | `module`表达式中的`let`绑定 |
| OCaml 4.08 | 2019 | 2019 `Binding`改进、`Seq` 改进 |
| OCaml 4.10 | 2020 | `Bigarray`改进 |
| OCaml 4.12 | 2021 | `Stdlib`改进 |
| OCaml 4.14 | 2022 | 2022 **尾模cons** (TMC) |
| OCaml 5.0 | 2022 | 2022 **主要**：效果处理程序、并行性（无 GIL）|
| OCaml 5.1 | 2023 | `Domain`改进、`Effect` 改进 |
| OCaml 5.2 | 2024 | 2024改进了错误消息，`Domain` 改进 |
| OCaml 5.3 | 2025 | 2025持续发展|
## 主要里程碑
### 卡梅尔 (1985–1995)
- **1985**：Gérard Huet 在 INRIA（法国）创建 Caml
- **名称**：“分类抽象机器语言”
- **1990**：Caml Light — Xavier Leroy 的轻量级版本
- 模式匹配、Hindley-Milner 类型推断
### OCaml 1.0–3.x：添加 OOP (1996–2011)
- **1996**：OCaml (Objective Caml) — 添加面向对象的功能
- **3.0 (2000)**：多态性方法，`lazy` 评估
- **3.10 (2007)**：`module type of` 
- **3.12 (2010)**：**一流模块** — 模块作为值
### OCaml 4.x：现代 OCaml (2012–2021)
- **4.00 (2012)**：`module type of`，改进的模块系统
- **4.01 (2013)**：`Bytes` 模块 — 默认情况下不可变字符串
- **4.03 (2016)**：`Result` 类型、`Seq`（惰性序列）
- **4.08 (2019)**：改进了错误消息
- **4.14 (2022)**：Tail-modulo-cons (TMC) — 更好的递归构造函数内存
### OCaml 5.x：并行革命（2022 年至今）
- **5.0 (2022)**：**效果处理程序**，**真正的并行性**（删除纯代码的 GIL）
  -`Domain`— 用于并行计算的操作系统线程
  -`Effect`— 代数效果处理程序（延续）
  - 不再有全局解释器锁 - 真正的多核 OCaml
- **5.1 (2023)**：域改进、效果处理程序改进
- **5.2 (2024)**：更好的错误消息，进一步改进
## 语法演变
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

## 类型系统的演变
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

## 关键设计原则
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## 生态系统增长
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
