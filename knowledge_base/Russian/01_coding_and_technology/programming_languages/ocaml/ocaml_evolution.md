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

# OCaml — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Камл | 1985 | **Категорический абстрактный машинный язык** (INRIA) |
| Камл Лайт | 1990 | Легкий вес Камл (Ксавье Лерой) |
| ОКамл 1.0 | 1996 | **Objective Caml** — добавляет ООП |
| ОКамл 3.0 | 2000 | **Основной**: Полиморфные методы,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | Улучшения компилятора машинного кода |
| OCaml 3.10 | 2007 |  Привязки `module type of`,`let`в определениях классов |
| OCaml 3.11 | 2008 |  Аннотации типа `private`,`module type of`|
| OCaml 3.12 | 2010 | Первоклассные модули |
| OCaml 4.00 | 2012 | **Основные**:`module type of`,`val`в подписях |
| ОКамл 4.01 | 2013 |  Модуль`Bytes`(изменяемые строки разделены) |
| ОКамл 4.02 | 2014 |  Модуль `Float`, улучшения`String`|
| ОКамл 4.03 | 2016 |  Тип `Result`,`Seq`(ленивые последовательности) |
| ОКамл 4.04 | 2017 | Профилировщик пространства-времени,`floatarray`|
| ОКамл 4.06 | 2018 |  Привязки`let`в выражениях`module`|
| ОКамл 4.08 | 2019 |  Улучшения `Binding`, улучшения`Seq`|
| OCaml 4.10 | 2020 |  Улучшения`Bigarray`|
| OCaml 4.12 | 2021 | `Stdlib`улучшения |
| OCaml 4.14 | 2022 | **Хвостовой модуль-минусы** (TMC) |
| ОКамл 5.0 | 2022 | **Основное**: обработчики эффектов, параллелизм (без GIL) |
| ОКамл 5.1 | 2023 |  Улучшения `Domain`, улучшения`Effect`|
| OCaml 5.2 | 2024 | Улучшены сообщения об ошибках, улучшения`Domain`|
| OCaml 5.3 | 2025 | Постоянное развитие |
## Основные вехи
### Камл (1985–1995)
- **1985**: Жерар Юэ создает Caml в INRIA (Франция).
- **Название**: «Категорический абстрактный машинный язык»
- **1990**: Caml Light — облегченная версия от Ксавье Лероя.
- Сопоставление с образцом, вывод типа Хиндли-Милнера
### OCaml 1.0–3.x: Добавление ООП (1996–2011)
- **1996**: OCaml (Objective Caml) — добавлены объектно-ориентированные функции.
- **3.0 (2000 г.)**: Полиморфные методы, оценка `lazy`.
- **3.10 (2007 г.)**:`module type of`
- **3.12 (2010 г.)**: **Первоклассные модули** — модули как ценности
### OCaml 4.x: современный OCaml (2012–2021 гг.)
- **4.00 (2012 г.)**: `module type of`, улучшенная система модулей.
- **4.01 (2013 г.)**: модуль`Bytes`— неизменяемые строки по умолчанию.
- **4.03 (2016 г.)**: тип `Result`,`Seq`(ленивые последовательности)
- **4.08 (2019 г.)**: улучшены сообщения об ошибках.
- **4.14 (2022 г.)**: Tail-modulo-cons (TMC) — улучшенная память для рекурсивных конструкторов.
### OCaml 5.x: параллельная революция (2022 г. – настоящее время)
- **5.0 (2022 г.)**: **Обработчики эффектов**, **истинный параллелизм** (удаляет GIL для чистого кода).
  -`Domain`— потоки ОС для параллельных вычислений.
  -`Effect`— обработчики алгебраических эффектов (продолжение)
  — Больше никакой глобальной блокировки интерпретатора — настоящий многоядерный OCaml.
- **5.1 (2023 г.)**: улучшения домена, усовершенствования обработчика эффектов.
- **5.2 (2024 г.)**: улучшенные сообщения об ошибках, дальнейшие улучшения.
## Эволюция синтаксиса
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

## Эволюция системы типов
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

## Ключевые принципы проектирования
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Рост экосистемы
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
