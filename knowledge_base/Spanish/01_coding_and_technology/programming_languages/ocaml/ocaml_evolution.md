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
# OCaml: Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| Camilla | 1985 | **Lenguaje de máquina abstracto categórico** (INRIA) |
| Luz de cámara | 1990 | Caml ligero (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Objective Caml** — agrega programación orientada a objetos |
| OCaml 3.0 | 2000 | **Principal**: métodos polimórficos, `lazy`,`Obj`|
| OCaml 3.05 | 2002 | Mejoras en el compilador de código nativo |
| OCaml 3.10 | 2007 |  Enlaces `module type of`,`let`en definiciones de clases |
| OCaml 3.11 | 2008 |  Anotaciones de tipo `private`,`module type of`|
| OCaml 3.12 | 2010 | Módulos de primera clase |
| OCaml 4.00 | 2012 | **Principal**: `module type of`,`val`en firmas |
| OCaml 4.01 | 2013 |  Módulo`Bytes`(cadenas mutables separadas) |
| OCaml 4.02 | 2014 |  Módulo `Float`, mejoras`String`|
| OCaml 4.03 | 2016 |  Tipo `Result`,`Seq`(secuencias diferidas) |
| OCaml 4.04 | 2017 | Perfilador de espacio-tiempo,`floatarray`|
| OCaml 4.06 | 2018 |  Enlaces`let`en expresiones`module`|
| OCaml 4.08 | 2019 |  Mejoras `Binding`, mejoras`Seq`|
| OCaml 4.10 | 2020 |  Mejoras`Bigarray`|
| OCaml 4.12 | 2021 |  Mejoras`Stdlib`|
| OCaml 4.14 | 2022 | **Contras del módulo de cola** (TMC) |
| OCaml 5.0 | 2022 | **Principal**: Manejadores de efectos, paralelismo (sin GIL) |
| OCaml 5.1 | 2023 |  Mejoras `Domain`, mejoras`Effect`|
| OCaml 5.2 | 2024 | Mensajes de error mejorados, mejoras`Domain`|
| OCaml 5.3 | 2025 | Desarrollo continuo |
## Hitos importantes
### Camll (1985-1995)
- **1985**: Gérard Huet crea Caml en INRIA (Francia)
- **Nombre**: "Lenguaje de máquina abstracto categórico"
- **1990**: Caml Light — versión ligera de Xavier Leroy
- Coincidencia de patrones, inferencia de tipo Hindley-Milner
### OCaml 1.0–3.x: Agregar programación orientada a objetos (1996–2011)
- **1996**: OCaml (Objective Caml): agrega funciones orientadas a objetos
- **3.0 (2000)**: Métodos polimórficos, evaluación `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **Módulos de primera clase** — módulos como valores
### OCaml 4.x: OCaml moderno (2012-2021)
- **4.00 (2012)**: `module type of`, sistema de módulos mejorado
- **4.01 (2013)**: módulo `Bytes`: cadenas inmutables de forma predeterminada
- **4.03 (2016)**: tipo `Result`,`Seq`(secuencias diferidas)
- **4.08 (2019)**: mensajes de error mejorados
- **4.14 (2022)**: Tail-modulo-cons (TMC): mejor memoria para constructores recursivos
### OCaml 5.x: La revolución paralela (2022-presente)
- **5.0 (2022)**: **Manejadores de efectos**, **paralelismo verdadero** (elimina GIL para código puro)
  - `Domain`: subprocesos del sistema operativo para cálculo paralelo
  -`Effect`— manejadores de efectos algebraicos (continuación)
  - No más bloqueo global de intérprete: OCaml multinúcleo real
- **5.1 (2023)**: mejoras en el dominio, refinamientos en el controlador de efectos
- **5.2 (2024)**: mejores mensajes de error, más mejoras
## Evolución de la sintaxis
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

## Evolución del sistema tipo
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

## Principios clave de diseño
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Crecimiento del ecosistema
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
