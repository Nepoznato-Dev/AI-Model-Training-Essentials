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
# OCaml — Histórico e evolução da versão
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| Caml | 1985 | **Linguagem de máquina abstrata categórica** (INRIA) |
| Caml Luz | 1990 | Caml leve (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Objective Caml** — adiciona OOP |
| OCaml 3.0 | 2000 | **Principal**: Métodos polimórficos,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | Melhorias no compilador de código nativo |
| OCaml 3.10 | 2007 |  Ligações`module type of`,`let`em definições de classe |
| OCaml 3.11 | 2008 |  Anotações de tipo `private`,`module type of`|
| OCaml 3.12 | 2010 | Módulos de primeira classe |
| OCaml 4.00 | 2012 | **Principal**:`module type of`,`val`em assinaturas |
| OCaml 4.01 | 2013 |  Módulo`Bytes`(sequências mutáveis ​​separadas) |
| OCaml 4.02 | 2014 |  Módulo `Float`, melhorias`String`|
| OCaml 4.03 | 2016 |  Tipo `Result`,`Seq`(sequências preguiçosas) |
| OCaml 4.04 | 2017 | Perfilador de espaço-tempo,`floatarray`|
| OCaml 4.06 | 2018 |  Ligações`let`em expressões`module`|
| OCaml 4.08 | 2019 |  Melhorias `Binding`, melhorias`Seq`|
| OCaml 4.10 | 2020 |  Melhorias`Bigarray`|
| OCaml 4.12 | 2021 |  Melhorias`Stdlib`|
| OCaml 4.14 | 2022 | **Módulo de cauda-cons** (TMC) |
| OCaml 5.0 | 2022 | **Principal**: Manipuladores de efeitos, paralelismo (sem GIL) |
| OCaml 5.1 | 2023 |  Melhorias `Domain`, melhorias`Effect`|
| OCaml 5.2 | 2024 | Mensagens de erro aprimoradas, melhorias no`Domain`|
| OCaml 5.3 | 2025 | Desenvolvimento contínuo |
## Marcos importantes
###Caml (1985–1995)
- **1985**: Gérard Huet cria Caml no INRIA (França)
- **Nome**: "Linguagem de máquina abstrata categórica"
- **1990**: Caml Light — versão leve de Xavier Leroy
- Correspondência de padrões, inferência do tipo Hindley-Milner
### OCaml 1.0–3.x: Adicionando OOP (1996–2011)
- **1996**: OCaml (Objective Caml) — adiciona recursos orientados a objetos
- **3.0 (2000)**: Métodos polimórficos, avaliação `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **Módulos de primeira classe** — módulos como valores
### OCaml 4.x: OCaml moderno (2012–2021)
- **4,00 (2012)**:`module type of`, sistema de módulo aprimorado
- **4.01 (2013)**: módulo`Bytes`— strings imutáveis por padrão
- **4.03 (2016)**: tipo `Result`,`Seq`(sequências lentas)
- **4.08 (2019)**: Mensagens de erro aprimoradas
- **4.14 (2022)**: Tail-modulo-cons (TMC) — melhor memória para construtores recursivos
### OCaml 5.x: A Revolução Paralela (2022-presente)
- **5.0 (2022)**: **Manipuladores de efeitos**, **paralelismo verdadeiro** (remove GIL para código puro)
  -`Domain`— Threads de SO para computação paralela
  -`Effect`— manipuladores de efeitos algébricos (continuações)
  - Chega de bloqueio global de intérprete - OCaml multicore real
- **5.1 (2023)**: Melhorias de domínio, refinamentos no manipulador de efeitos
- **5.2 (2024)**: Melhores mensagens de erro, melhorias adicionais
## Evolução da Sintaxe
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

## Tipo Evolução do Sistema
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

## Princípios-chave de design
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Crescimento do Ecossistema
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
