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
# OCaml – Versionsgeschichte und Entwicklung
## Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| Caml | 1985 | **Kategorische abstrakte Maschinensprache** (INRIA) |
| Caml Light | 1990 | Leichter Caml (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Objective Caml** – fügt OOP hinzu |
| OCaml 3.0 | 2000 | **Hauptsächlich**: Polymorphe Methoden,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | Verbesserungen des Native-Code-Compilers |
| OCaml 3.10 | 2007 | `module type of`,`let`Bindungen in Klassendefinitionen |
| OCaml 3.11 | 2008 | `private`Typanmerkungen,`module type of`|
| OCaml 3.12 | 2010 | Erstklassige Module |
| OCaml 4.00 | 2012 | **Major**:`module type of`,`val`in Signaturen |
| OCaml 4.01 | 2013 |  `Bytes`-Modul (veränderliche Zeichenfolgen getrennt) |
| OCaml 4.02 | 2014 |  `Float`-Modul, `String`-Verbesserungen |
| OCaml 4.03 | 2016 |  `Result`-Typ,`Seq`(Lazy-Sequenzen) |
| OCaml 4.04 | 2017 | Raumzeit-Profiler,`floatarray`|
| OCaml 4.06 | 2018 |  `let`-Bindungen in `module`-Ausdrücken |
| OCaml 4.08 | 2019 |  `Binding`-Verbesserungen, `Seq`-Verbesserungen |
| OCaml 4.10 | 2020 | `Bigarray`Verbesserungen |
| OCaml 4.12 | 2021 | `Stdlib`Verbesserungen |
| OCaml 4.14 | 2022 | **Tail-modulo-cons** (TMC) |
| OCaml 5.0 | 2022 | **Hauptsächlich**: Effekthandler, Parallelität (keine GIL) |
| OCaml 5.1 | 2023 |  `Domain`-Verbesserungen, `Effect`-Verbesserungen |
| OCaml 5.2 | 2024 | Verbesserte Fehlermeldungen,`Domain`Verbesserungen |
| OCaml 5.3 | 2025 | Kontinuierliche Entwicklung |
## Wichtige Meilensteine
### Caml (1985–1995)
- **1985**: Gérard Huet kreiert Caml bei INRIA (Frankreich)
- **Name**: „Kategorische abstrakte Maschinensprache“
- **1990**: Caml Light – leichte Version von Xavier Leroy
- Mustervergleich, Hindley-Milner-Typinferenz
### OCaml 1.0–3.x: OOP hinzufügen (1996–2011)
- **1996**: OCaml (Objective Caml) – fügt objektorientierte Funktionen hinzu
- **3.0 (2000)**: Polymorphe Methoden, `lazy`-Auswertung
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **Erstklassige Module** – Module als Werte
### OCaml 4.x: Modernes OCaml (2012–2021)
- **4.00 (2012)**:`module type of`, verbessertes Modulsystem
- **4.01 (2013)**: Modul`Bytes`– standardmäßig unveränderliche Zeichenfolgen
- **4.03 (2016)**: Typ `Result`,`Seq`(Lazy Sequences)
- **4.08 (2019)**: Verbesserte Fehlermeldungen
- **4.14 (2022)**: Tail-modulo-cons (TMC) – besserer Speicher für rekursive Konstruktoren
### OCaml 5.x: Die Parallelrevolution (2022–heute)
- **5.0 (2022)**: **Effekthandler**, **echte Parallelität** (entfernt GIL für reinen Code)
  -`Domain`– Betriebssystem-Threads für parallele Berechnungen
  -`Effect`– algebraische Effekthandler (Fortsetzungen)
  - Kein Global Interpreter Lock mehr – echtes Multicore-OCaml
- **5.1 (2023)**: Domänenverbesserungen, Verfeinerungen des Effekthandlers
- **5.2 (2024)**: Bessere Fehlermeldungen, weitere Verbesserungen
## Syntaxentwicklung
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

## Typsystementwicklung
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

## Wichtige Designprinzipien
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Ökosystemwachstum
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
