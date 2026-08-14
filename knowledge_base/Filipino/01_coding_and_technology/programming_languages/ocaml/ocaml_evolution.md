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

# OCaml — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| Caml | 1985 | **Categorical Abstract Machine Language** (INRIA) |
| Caml Light | 1990 | Magaang Caml (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Objective Caml** — nagdagdag ng OOP |
| OCaml 3.0 | 2000 | **Major**: Polymorphic na pamamaraan,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | Mga pagpapabuti ng native-code compiler |
| OCaml 3.10 | 2007 | `module type of`,`let`binding sa mga kahulugan ng klase |
| OCaml 3.11 | 2008 |  Mga anotasyon ng uri ng `private`,`module type of`|
| OCaml 3.12 | 2010 | Mga module sa unang klase |
| OCaml 4.00 | 2012 | **Major**:`module type of`,`val`sa mga lagda |
| OCaml 4.01 | 2013 | `Bytes`module (mga nababagong string na pinaghihiwalay) |
| OCaml 4.02 | 2014 | `Float`module,`String`mga pagpapabuti |
| OCaml 4.03 | 2016 |  Uri ng `Result`,`Seq`(mga tamad na pagkakasunud-sunod) |
| OCaml 4.04 | 2017 | Spacetime profiler,`floatarray`|
| OCaml 4.06 | 2018 | `let`na mga binding sa`module`na mga expression |
| OCaml 4.08 | 2019 | `Binding`mga pagpapabuti,`Seq`mga pagpapabuti |
| OCaml 4.10 | 2020 | `Bigarray`mga pagpapabuti |
| OCaml 4.12 | 2021 | `Stdlib`mga pagpapabuti |
| OCaml 4.14 | 2022 | **Tail-modulo-cons** (TMC) |
| OCaml 5.0 | 2022 | **Major**: Mga tagapangasiwa ng epekto, paralelismo (walang GIL) |
| OCaml 5.1 | 2023 | `Domain`mga pagpapabuti,`Effect`mga pagpapabuti |
| OCaml 5.2 | 2024 | Mga pinahusay na mensahe ng error, mga pagpapabuti ng`Domain`|
| OCaml 5.3 | 2025 | Patuloy na pag-unlad |
## Mga Pangunahing Milestone
### Caml (1985–1995)
- **1985**: Gumawa si Gérard Huet ng Caml sa INRIA (France)
- **Pangalan**: "Categorical Abstract Machine Language"
- **1990**: Caml Light — magaan na bersyon ni Xavier Leroy
- Pagtutugma ng pattern, hinuha ng uri ng Hindley-Milner
### OCaml 1.0–3.x: Pagdaragdag ng OOP (1996–2011)
- **1996**: OCaml (Objective Caml) — nagdaragdag ng mga feature na nakatuon sa object
- **3.0 (2000)**: Mga polymorphic na pamamaraan, pagsusuri ng `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **First-class na mga module** — mga module bilang mga value
### OCaml 4.x: Modernong OCaml (2012–2021)
- **4.00 (2012)**:`module type of`, pinahusay na module system
- **4.01 (2013)**:`Bytes`module — mga hindi nababagong string bilang default
- **4.03 (2016)**: Uri ng `Result`,`Seq`(mga tamad na pagkakasunud-sunod)
- **4.08 (2019)**: Mga pinahusay na mensahe ng error
- **4.14 (2022)**: Tail-modulo-cons (TMC) — mas mahusay na memorya para sa mga recursive constructor
### OCaml 5.x: The Parallel Revolution (2022–kasalukuyan)
- **5.0 (2022)**: **Mga humahawak ng epekto**, **true parallelism** (tinatanggal ang GIL para sa purong code)
  -`Domain`— Mga OS thread para sa parallel computation
  -`Effect`— mga humahawak ng algebraic effect (mga pagpapatuloy)
  - Wala nang Global Interpreter Lock — totoong multicore OCaml
- **5.1 (2023)**: Mga pagpapahusay ng domain, mga pagpipino ng effect handler
- **5.2 (2024)**: Mas mahusay na mga mensahe ng error, karagdagang pagpapahusay
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

## Uri ng System Evolution
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

## Pangunahing Prinsipyo ng Disenyo
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Paglago ng Ecosystem
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
