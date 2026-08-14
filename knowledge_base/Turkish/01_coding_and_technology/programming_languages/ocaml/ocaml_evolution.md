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
# OCaml — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| Caml | 1985 | **Kategorik Soyut Makine Dili** (INRIA) |
| Caml Işık | 1990 | Hafif Caml (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Objective Caml** — OOP ekler |
| OCaml 3.0 | 2000 | **Ana**: Polimorfik yöntemler,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | Yerel kod derleyici iyileştirmeleri |
| OCaml 3.10 | 2007 | `module type of`, sınıf tanımlarında`let`bağlamaları |
| OCaml 3.11 | 2008 | `private`türü ek açıklamalar,`module type of`|
| OCaml 3.12 | 2010 | Birinci sınıf modüller |
| OCaml 4.00 | 2012 | **Binbaşı**:`module type of`, imzalarda`val`|
| OCaml 4.01 | 2013 | `Bytes`modülü (değişebilir dizeler ayrılmış) |
| OCaml 4.02 | 2014 | `Float`modülü,`String`iyileştirmeleri |
| OCaml 4.03 | 2016 | `Result`türü,`Seq`(tembel diziler) |
| OCaml 4.04 | 2017 | Uzay-zaman profili oluşturucu,`floatarray`|
| OCaml 4.06 | 2018 | `module`ifadelerinde`let`bağlamaları |
| OCaml 4.08 | 2019 | `Binding`iyileştirmeleri,`Seq`iyileştirmeleri |
| OCaml 4.10 | 2020 | `Bigarray`iyileştirmeleri |
| OCaml 4.12 | 2021 | `Stdlib`iyileştirmeleri |
| OCaml 4.14 | 2022 | **Kuyruk modül eksileri** (TMC) |
| OCaml 5.0 | 2022 | **Ana**: Efekt işleyicileri, paralellik (GIL yok) |
| OCaml 5.1 | 2023 | `Domain`iyileştirmeleri,`Effect`iyileştirmeleri |
| OCaml 5.2 | 2024 | Geliştirilmiş hata mesajları,`Domain`iyileştirmeleri |
| OCaml 5.3 | 2025 | Devam eden geliştirme |
## Önemli Kilometre Taşları
### Caml (1985–1995)
- **1985**: Gérard Huet, INRIA'da (Fransa) Caml'ı yarattı
- **Ad**: "Kategorik Soyut Makine Dili"
- **1990**: Caml Light — Xavier Leroy'un hafif versiyonu
- Desen eşleştirme, Hindley-Milner tipi çıkarım
### OCaml 1.0–3.x: OOP Ekleme (1996–2011)
- **1996**: OCaml (Objective Caml) — nesne yönelimli özellikler ekler
- **3.0 (2000)**: Polimorfik yöntemler,`lazy`değerlendirmesi
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **Birinci sınıf modüller** — değer olarak modüller
### OCaml 4.x: Modern OCaml (2012–2021)
- **4.00 (2012)**: `module type of`, geliştirilmiş modül sistemi
- **4.01 (2013)**:`Bytes`modülü — varsayılan olarak değişmez dizeler
- **4.03 (2016)**:`Result`türü,`Seq`(tembel diziler)
- **4.08 (2019)**: İyileştirilmiş hata mesajları
- **4.14 (2022)**: Tail-modulo-cons (TMC) — özyinelemeli oluşturucular için daha iyi bellek
### OCaml 5.x: Paralel Devrim (2022-günümüz)
- **5.0 (2022)**: **Efekt işleyicileri**, **gerçek paralellik** (saf kod için GIL'yi kaldırır)
  -`Domain`— Paralel hesaplama için işletim sistemi iş parçacıkları
  -`Effect`— cebirsel etki işleyicileri (devam)
  - Artık Küresel Tercüman Kilidi yok - gerçek çok çekirdekli OCaml
- **5.1 (2023)**: Etki alanı iyileştirmeleri, efekt işleyicide iyileştirmeler
- **5.2 (2024)**: Daha iyi hata mesajları, daha fazla iyileştirme
## Söz Dizimi Gelişimi
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

## Tür Sistem Gelişimi
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

## Temel Tasarım İlkeleri
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Ekosistem Büyümesi
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
