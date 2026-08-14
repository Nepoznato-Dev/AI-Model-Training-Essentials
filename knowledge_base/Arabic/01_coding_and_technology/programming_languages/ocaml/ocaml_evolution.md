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
# OCaml — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| كامل | 1985 | ** لغة الآلة المجردة الفئوية ** (INRIA) |
| كامل لايت | 1990 | كامل خفيف الوزن (كزافييه ليروي) |
| أوكامل 1.0 | 1996 | **الهدف الكامل** — يضيف OOP |
| أوكامل 3.0 | 2000 | **التخصص**: الطرق المتعددة الأشكال،`lazy`،`Obj`|
| أوكامل 3.05 | 2002 | تحسينات مترجم التعليمات البرمجية الأصلية |
| أوكامل 3.10 | 2007 |  روابط`module type of`و`let`في تعريفات الفئة |
| أوكامل 3.11 | 2008 |  التعليقات التوضيحية من النوع `private`،`module type of`|
| أوكامل 3.12 | 2010 | وحدات من الدرجة الأولى |
| أوكامل 4.00 | 2012 | **التخصص**: `module type of`،`val`في التوقيعات |
| أوكامل 4.01 | 2013 |  وحدة`Bytes`(سلاسل قابلة للتغيير مفصولة) |
| أوكامل 4.02 | 2014 |  وحدة `Float`، تحسينات`String`|
| أوكامل 4.03 | 2016 |  نوع `Result`،`Seq`(تسلسلات كسولة) |
| أوكامل 4.04 | 2017 | ملف تعريف الزمكان،`floatarray`|
| أوكامل 4.06 | 2018 |  روابط`let`في تعبيرات`module`|
| أوكامل 4.08 | 2019 |  تحسينات `Binding`، تحسينات`Seq`|
| أوكامل 4.10 | 2020 |  تحسينات`Bigarray`|
| أوكامل 4.12 | 2021 |  تحسينات`Stdlib`|
| أوكامل 4.14 | 2022 | **سلبيات وحدة الذيل** (TMC) |
| أوكامل 5.0 | 2022 | **التخصص**: معالجات التأثير، التوازي (بدون GIL) |
| أوكامل 5.1 | 2023 |  تحسينات `Domain`، تحسينات`Effect`|
| أوكامل 5.2 | 2024 | تحسين رسائل الخطأ، تحسينات`Domain`|
| أوكامل 5.3 | 2025 | التطوير المستمر |
## المعالم الرئيسية
### كامل (1985-1995)
- **1985**: أنشأ جيرار هويت شركة Caml في INRIA (فرنسا)
- **الاسم**: "لغة الآلة التجريدية القاطعة"
- **1990**: Caml Light — نسخة خفيفة الوزن من تصميم Xavier Leroy
- مطابقة الأنماط، استنتاج نوع هيندلي ميلنر
### OCaml 1.0–3.x: إضافة OOP (1996–2011)
- **1996**: OCaml (Objective Caml) — يضيف ميزات موجهة للكائنات
- **3.0 (2000)**: الطرق المتعددة الأشكال، تقييم `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **وحدات من الدرجة الأولى** — الوحدات كقيم
### OCaml 4.x: OCaml الحديث (2012–2021)
- **4.00 (2012)**: `module type of`، نظام الوحدة المحسّن
- **4.01 (2013)**: وحدة`Bytes`— سلاسل غير قابلة للتغيير افتراضيًا
- **4.03 (2016)**: نوع `Result`،`Seq`(تسلسلات كسولة)
- **4.08 (2019)**: تحسين رسائل الخطأ
- **4.14 (2022)**: سلبيات وحدة الذيل (TMC) — ذاكرة أفضل للمنشئات العودية
### OCaml 5.x: الثورة الموازية (2022 إلى الوقت الحاضر)
- **5.0 (2022)**: **معالجات التأثير**، **التوازي الحقيقي** (يزيل GIL للحصول على كود خالص)
  -`Domain`— خيوط نظام التشغيل للحساب المتوازي
  -`Effect`— معالجات التأثير الجبرية (تابع)
  - لا مزيد من قفل المترجم العالمي - OCaml حقيقي متعدد النواة
- **5.1 (2023)**: تحسينات المجال، وتحسينات معالج التأثير
- **5.2 (2024)**: رسائل خطأ أفضل، والمزيد من التحسينات
## تطور بناء الجملة
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

## نوع تطور النظام
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

## مبادئ التصميم الرئيسية
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## نمو النظام البيئي
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
