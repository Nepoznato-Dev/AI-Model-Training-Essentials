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
# OCaml — Version History & Evolution

## Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| Caml    | 1985 | **Categorical Abstract Machine Language** (INRIA) |
| Caml Light | 1990 | Lightweight Caml (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Objective Caml** — adds OOP |
| OCaml 3.0 | 2000 | **Major**: Polymorphic methods, `lazy`, `Obj` |
| OCaml 3.05 | 2002 | Native-code compiler improvements |
| OCaml 3.10 | 2007 | `module type of`, `let` bindings in class definitions |
| OCaml 3.11 | 2008 | `private` type annotations, `module type of` |
| OCaml 3.12 | 2010 | First-class modules |
| OCaml 4.00 | 2012 | **Major**: `module type of`, `val` in signatures |
| OCaml 4.01 | 2013 | `Bytes` module (mutable strings separated) |
| OCaml 4.02 | 2014 | `Float` module, `String` improvements |
| OCaml 4.03 | 2016 | `Result` type, `Seq` (lazy sequences) |
| OCaml 4.04 | 2017 | Spacetime profiler, `floatarray` |
| OCaml 4.06 | 2018 | `let` bindings in `module` expressions |
| OCaml 4.08 | 2019 | `Binding` improvements, `Seq` improvements |
| OCaml 4.10 | 2020 | `Bigarray` improvements |
| OCaml 4.12 | 2021 | `Stdlib` improvements |
| OCaml 4.14 | 2022 | **Tail-modulo-cons** (TMC) |
| OCaml 5.0  | 2022 | **Major**: Effect handlers, parallelism (no GIL) |
| OCaml 5.1  | 2023 | `Domain` improvements, `Effect` improvements |
| OCaml 5.2  | 2024 | Improved error messages, `Domain` improvements |
| OCaml 5.3  | 2025 | Ongoing development |

## Major Milestones

### Caml (1985–1995)
- **1985**: Gérard Huet creates Caml at INRIA (France)
- **Name**: "Categorical Abstract Machine Language"
- **1990**: Caml Light — lightweight version by Xavier Leroy
- Pattern matching, Hindley-Milner type inference

### OCaml 1.0–3.x: Adding OOP (1996–2011)
- **1996**: OCaml (Objective Caml) — adds object-oriented features
- **3.0 (2000)**: Polymorphic methods, `lazy` evaluation
- **3.10 (2007)**: `module type of`
- **3.12 (2010)**: **First-class modules** — modules as values

### OCaml 4.x: Modern OCaml (2012–2021)
- **4.00 (2012)**: `module type of`, improved module system
- **4.01 (2013)**: `Bytes` module — immutable strings by default
- **4.03 (2016)**: `Result` type, `Seq` (lazy sequences)
- **4.08 (2019)**: Improved error messages
- **4.14 (2022)**: Tail-modulo-cons (TMC) — better memory for recursive constructors

### OCaml 5.x: The Parallel Revolution (2022–present)
- **5.0 (2022)**: **Effect handlers**, **true parallelism** (removes GIL for pure code)
  - `Domain` — OS threads for parallel computation
  - `Effect` — algebraic effect handlers (continuations)
  - No more Global Interpreter Lock — real multicore OCaml
- **5.1 (2023)**: Domain improvements, effect handler refinements
- **5.2 (2024)**: Better error messages, further improvements

## Syntax Evolution

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

## Type System Evolution

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

## Key Design Principles

```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Ecosystem Growth

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
