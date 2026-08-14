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
# OCaml - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| کیمل | 1985 | **کیٹیگوریکل خلاصہ مشینی زبان** (INRIA) |
| کیمل لائٹ | 1990 | ہلکا پھلکا Caml (Zavier Leroy) |
| OCaml 1.0 | 1996 | **Objective Caml** — OOP شامل کرتا ہے۔
| OCaml 3.0 | 2000 | **بڑا**: پولیمورفک طریقے،`lazy`,`Obj`|
| OCaml 3.05 | 2002 | مقامی کوڈ کمپائلر میں بہتری |
| OCaml 3.10 | 2007 | `module type of`,`let`کلاس کی تعریف میں بائنڈنگز |
| OCaml 3.11 | 2008 | `private`قسم کی تشریحات،`module type of`|
| OCaml 3.12 | 2010 | فرسٹ کلاس ماڈیولز |
| OCaml 4.00 | 2012 | **میجر**:`module type of`,`val`دستخطوں میں |
| OCaml 4.01 | 2013 | `Bytes`ماڈیول (میوٹ ایبل تاروں کو الگ کیا گیا) |
| OCaml 4.02 | 2014 | `Float`ماڈیول،`String`بہتری |
| OCaml 4.03 | 2016 | `Result`قسم،`Seq`(سست سلسلے) |
| OCaml 4.04 | 2017 | اسپیس ٹائم پروفائلر،`floatarray`|
| OCaml 4.06 | 2018 | `let``module` اظہار میں بائنڈنگز |
| OCaml 4.08 | 2019 | `Binding`بہتری،`Seq`بہتری |
| OCaml 4.10 | 2020 | `Bigarray`بہتری |
| OCaml 4.12 | 2021 | `Stdlib`بہتری |
| OCaml 4.14 | 2022 | **ٹیل-موڈولو-کونس** (TMC) |
| OCaml 5.0 | 2022 | **میجر**: ایفیکٹ ہینڈلرز، متوازی (کوئی GIL نہیں) |
| OCaml 5.1 | 2023 | `Domain`بہتری،`Effect`بہتری |
| OCaml 5.2 | 2024 | بہتر شدہ خرابی کے پیغامات،`Domain`بہتری |
| OCaml 5.3 | 2025 | جاری ترقی |
## اہم سنگ میل
### کیمل (1985–1995)
- **1985**: جیرارڈ ہیوٹ نے INRIA (فرانس) میں کیمل تخلیق کیا۔
- **نام**: "کیٹیگوریکل خلاصہ مشینی زبان"
- **1990**: کیمل لائٹ — زیویئر لیروئے کا ہلکا پھلکا ورژن
- پیٹرن کی مماثلت، ہندلی-ملنر قسم کا اندازہ
### OCaml 1.0–3.x: OOP شامل کرنا (1996–2011)
- **1996**: OCaml (Objective Caml) - آبجیکٹ پر مبنی خصوصیات شامل کرتا ہے
- **3.0 (2000)**: پولیمورفک طریقے،`lazy`تشخیص
- **3.10 (2007)**:`module type of`
- **3.12 (2010): **فرسٹ کلاس ماڈیول** — ماڈیولز بطور قدر
### OCaml 4.x: جدید OCaml (2012–2021)
- **4.00 (2012)**: `module type of`، بہتر ماڈیول سسٹم
- **4.01 (2013)**:`Bytes`ماڈیول — ڈیفالٹ کے لحاظ سے ناقابل تغیر تار
- **4.03 (2016)**:`Result`قسم،`Seq`(سست سلسلے)
- **4.08 (2019)**: خرابی کے بہتر پیغامات
- **4.14 (2022)**: Tail-modulo-cons (TMC) — تکرار کنسٹرکٹرز کے لیے بہتر میموری
### OCaml 5.x: متوازی انقلاب (2022–موجودہ)
- **5.0 (2022)**: **اثر ہینڈلرز**، **حقیقی ہم آہنگی** (خالص کوڈ کے لیے GIL کو ہٹاتا ہے)
  -`Domain`- متوازی حساب کے لیے OS تھریڈز
  -`Effect`- الجبری اثر ہینڈلر (جاری ہے)
  - مزید کوئی گلوبل انٹرپریٹر لاک نہیں - اصلی ملٹی کور OCaml
- **5.1 (2023)**: ڈومین میں بہتری، اثر ہینڈلر کی اصلاح
- **5.2 (2024): بہتر خرابی کے پیغامات، مزید بہتری
## نحوی ارتقاء
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

## ٹائپ سسٹم ارتقاء
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

## ڈیزائن کے کلیدی اصول
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## ماحولیاتی نظام کی نمو
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
