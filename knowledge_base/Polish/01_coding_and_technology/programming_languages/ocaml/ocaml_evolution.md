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
# OCaml — Historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| Caml | 1985 | **Kategoryczny abstrakcyjny język maszynowy** (INRIA) |
| Caml Light | 1990 | Lekki Caml (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Obiektyw Caml** — dodaje OOP |
| OCaml 3.0 | 2000 | **Główne**: Metody polimorficzne,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | Ulepszenia kompilatora kodu natywnego |
| OCaml 3.10 | 2007 |  Powiązania`module type of`,`let`w definicjach klas |
| OCaml 3.11 | 2008 |  Adnotacje typu `private`,`module type of`|
| OCaml 3.12 | 2010 | Moduły najwyższej klasy |
| OCaml 4,00 | 2012 | **Główne**:`module type of`,`val`w sygnaturach |
| OCaml 4.01 | 2013 |  Moduł`Bytes`(oddzielone zmienne ciągi znaków) |
| OCaml 4.02 | 2014 |  Moduł `Float`, ulepszenia`String`|
| OCaml 4.03 | 2016 |  Typ `Result`,`Seq`(sekwencje leniwe) |
| OCaml 4.04 | 2017 | Profiler czasoprzestrzeni,`floatarray`|
| OCaml 4.06 | 2018 |  Powiązania`let`w wyrażeniach`module`|
| OCaml 4.08 | 2019 |  Ulepszenia `Binding`, ulepszenia`Seq`|
| OCaml 4.10 | 2020 |  Ulepszenia`Bigarray`|
| OCaml 4.12 | 2021 |  Ulepszenia`Stdlib`|
| OCaml 4.14 | 2022 | **Wady modulo-ogonowe** (TMC) |
| OCaml 5.0 | 2022 | **Główne**: Obsługa efektów, równoległość (bez GIL) |
| OCaml 5.1 | 2023 |  Ulepszenia `Domain`, ulepszenia`Effect`|
| OCaml 5.2 | 2024 | Ulepszone komunikaty o błędach, ulepszenia`Domain`|
| OCaml 5.3 | 2025 | Ciągły rozwój |
## Główne kamienie milowe
### Caml (1985–1995)
- **1985**: Gérard Huet tworzy Caml w INRIA (Francja)
- **Nazwa**: „Kategoryczny abstrakcyjny język maszynowy”
- **1990**: Caml Light – lekka wersja autorstwa Xaviera Leroya
- Dopasowywanie wzorców, wnioskowanie typu Hindleya-Milnera
### OCaml 1.0–3.x: Dodawanie OOP (1996–2011)
- **1996**: OCaml (Objective Caml) — dodaje funkcje obiektowe
- **3.0 (2000)**: Metody polimorficzne, ocena `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **Moduły pierwszej klasy** — moduły jako wartości
### OCaml 4.x: Nowoczesny OCaml (2012–2021)
- **4,00 (2012)**:`module type of`, ulepszony system modułowy
- **4.01 (2013)**: moduł`Bytes`— domyślnie ciągi niezmienne
- **4.03 (2016)**: typ `Result`,`Seq`(sekwencje leniwe)
- **4.08 (2019)**: Poprawione komunikaty o błędach
- **4.14 (2022)**: Tail-modulo-cons (TMC) — lepsza pamięć dla konstruktorów rekurencyjnych
### OCaml 5.x: Rewolucja równoległa (2022 – obecnie)
- **5.0 (2022)**: **Procedury obsługi efektów**, **prawdziwa równoległość** (usuwa GIL dla czystego kodu)
  -`Domain`— wątki systemu operacyjnego do obliczeń równoległych
  -`Effect`— obsługa efektów algebraicznych (kontynuacja)
  - Koniec z globalną blokadą interpretera — prawdziwy wielordzeniowy OCaml
- **5.1 (2023)**: Ulepszenia domeny, udoskonalenia obsługi efektów
- **5.2 (2024)**: Lepsze komunikaty o błędach, dalsze ulepszenia
## Ewolucja składni
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

## Wpisz ewolucję systemu
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

## Kluczowe zasady projektowania
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Rozwój ekosystemu
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
