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
# OCaml: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Caml | 1985 | **Linguaggio macchina astratto categoriale** (INRIA) |
| Caml Luce | 1990 | Caml leggero (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Obiettivo Caml**: aggiunge OOP |
| OCaml 3.0 | 2000 | **Maggiore**: metodi polimorfici,`lazy`,`Obj`|
| OCaml 3.05 | 2002| Miglioramenti al compilatore del codice nativo |
| OCaml 3.10 | 2007| `module type of`,`let`associazioni nelle definizioni di classe |
| OCaml 3.11 | 2008|  Annotazioni di tipo `private`,`module type of`|
| OCaml 3.12 | 2010| Moduli di prima classe |
| OCaml 4.00 | 2012| **Maggiore**:`module type of`,`val`in firme |
| OCaml 4.01 | 2013|  Modulo`Bytes`(stringhe mutabili separate) |
| OCaml 4.02 | 2014|  Modulo `Float`, miglioramenti`String`|
| OCaml 4.03 | 2016|  Tipo `Result`,`Seq`(sequenze pigre) |
| OCaml 4.04 | 2017 | Profilatore spaziotemporale,`floatarray`|
| OCaml 4.06 | 2018 |  Associazioni`let`nelle espressioni`module`|
| OCaml 4.08 | 2019 |  Miglioramenti `Binding`, miglioramenti`Seq`|
| OCaml 4.10 | 2020 |  Miglioramenti`Bigarray`|
| OCaml 4.12 | 2021 | `Stdlib`miglioramenti |
| OCaml 4.14 | 2022 | **Modulo coda-contro** (TMC) |
| OCaml 5.0 | 2022 | **Maggiore**: gestori di effetti, parallelismo (no GIL) |
| OCaml 5.1 | 2023 |  Miglioramenti `Domain`, miglioramenti`Effect`|
| OCaml 5.2 | 2024 | Messaggi di errore migliorati, miglioramenti`Domain`|
| OCaml 5.3 | 2025 | Sviluppo continuo |
## Traguardi importanti
### Caml (1985–1995)
- **1985**: Gérard Huet crea Caml all'INRIA (Francia)
- **Nome**: "Linguaggio macchina astratto categoriale"
- **1990**: Caml Light — versione leggera di Xavier Leroy
- Patternmatching, inferenza di tipo Hindley-Milner
### OCaml 1.0–3.x: aggiunta di OOP (1996–2011)
- **1996**: OCaml (Objective Caml) — aggiunge funzionalità orientate agli oggetti
- **3.0 (2000)**: Metodi polimorfici, valutazione `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **Moduli di prima classe** — moduli come valori
### OCaml 4.x: OCaml moderno (2012–2021)
- **4.00 (2012)**: `module type of`, sistema di moduli migliorato
- **4.01 (2013)**: modulo `Bytes`: stringhe immutabili per impostazione predefinita
- **4.03 (2016)**: tipo `Result`,`Seq`(sequenze pigre)
- **4.08 (2019)**: messaggi di errore migliorati
- **4.14 (2022)**: Tail-modulo-cons (TMC): migliore memoria per costruttori ricorsivi
### OCaml 5.x: La rivoluzione parallela (2022-oggi)
- **5.0 (2022)**: **Gestori di effetti**, **parallelismo vero** (rimuove GIL per il codice puro)
  - `Domain`: thread del sistema operativo per il calcolo parallelo
  - `Effect`: gestori di effetti algebrici (continua)
  - Niente più blocco globale dell'interprete: vero OCaml multicore
- **5.1 (2023)**: miglioramenti del dominio, perfezionamenti del gestore degli effetti
- **5.2 (2024)**: messaggi di errore migliorati, ulteriori miglioramenti
## Evoluzione della sintassi
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

## Digitare Evoluzione del sistema
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

## Principi chiave di progettazione
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Crescita dell'ecosistema
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
