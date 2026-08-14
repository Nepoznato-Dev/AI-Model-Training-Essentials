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

# OCaml — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| Caml | 1985 | **Langage machine abstrait catégorique** (INRIA) |
| Lumière Caml | 1990 | Caml léger (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Objective Caml** — ajoute la POO |
| OCaml 3.0 | 2000 | **Majeur** : Méthodes polymorphes,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | Améliorations du compilateur de code natif |
| OCaml 3.10 | 2007 |  Liaisons`module type of`,`let`dans les définitions de classe |
| OCaml 3.11 | 2008 |  Annotations de type `private`,`module type of`|
| OCaml 3.12 | 2010 | Modules de première classe |
| OCaml 4.00 | 2012 | **Majeur** :`module type of`,`val`dans les signatures |
| OCaml 4.01 | 2013 |  Module`Bytes`(chaînes mutables séparées) |
| OCaml 4.02 | 2014 |  Module `Float`, améliorations`String`|
| OCaml 4.03 | 2016 |  Type `Result`,`Seq`(séquences paresseuses) |
| OCaml 4.04 | 2017 | Profileur d'espace-temps,`floatarray`|
| OCaml 4.06 | 2018 |  Liaisons`let`dans les expressions`module`|
| OCaml 4.08 | 2019 |  Améliorations `Binding`, améliorations`Seq`|
| OCaml 4.10 | 2020 |  Améliorations`Bigarray`|
| OCaml 4.12 | 2021 |  Améliorations`Stdlib`|
| OCaml 4.14 | 2022 | **Queue-modulo-cons** (TMC) |
| OCaml 5.0 | 2022 | **Majeur** : gestionnaires d'effets, parallélisme (pas de GIL) |
| OCaml 5.1 | 2023 |  Améliorations `Domain`, améliorations`Effect`|
| OCaml 5.2 | 2024 | Messages d'erreur améliorés, améliorations`Domain`|
| OCaml 5.3 | 2025 | Développement en cours |
## Étapes majeures
###Caml (1985-1995)
- **1985** : Gérard Huet crée Caml à l'INRIA (France)
- **Nom** : "Langage machine abstrait catégorique"
- **1990** : Caml Light — version allégée de Xavier Leroy
- Correspondance de modèles, inférence de type Hindley-Milner
### OCaml 1.0–3.x : ajout de la POO (1996–2011)
- **1996** : OCaml (Objective Caml) — ajoute des fonctionnalités orientées objet
- **3.0 (2000)** : Méthodes polymorphes, évaluation `lazy`
- **3.10 (2007)** :`module type of`
- **3.12 (2010)** : **Modules de première classe** — modules comme valeurs
### OCaml 4.x : OCaml moderne (2012-2021)
- **4.00 (2012)** :`module type of`, système de modules amélioré
- **4.01 (2013)** : module`Bytes`— chaînes immuables par défaut
- **4.03 (2016)** : type `Result`,`Seq`(séquences paresseuses)
- **4.08 (2019)** : messages d'erreur améliorés
- **4.14 (2022)** : Tail-modulo-cons (TMC) — meilleure mémoire pour les constructeurs récursifs
### OCaml 5.x : La révolution parallèle (2022-présent)
- **5.0 (2022)** : **Gestionnaires d'effets**, **véritable parallélisme** (supprime GIL pour le code pur)
  -`Domain`— Threads du système d'exploitation pour le calcul parallèle
  -`Effect`— gestionnaires d'effets algébriques (suites)
  - Plus de verrouillage global de l'interprète - véritable OCaml multicœur
- **5.1 (2023)** : améliorations du domaine, améliorations du gestionnaire d'effets
- **5.2 (2024)** : meilleurs messages d'erreur, nouvelles améliorations
## Évolution de la syntaxe
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

## Évolution du système de types
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

## Principes de conception clés
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Croissance de l'écosystème
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
