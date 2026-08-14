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
# OCaml - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| Caml | 1985 | **زبان ماشینی چکیده دسته بندی** (INRIA) |
| Caml Light | 1990 | Caml سبک (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Objective Caml** — OOP |
| OCaml 3.0 | 2000 | **عناوین**: روش های چند شکلی،`lazy`,`Obj`|
| OCaml 3.05 | 2002 | بهبود کامپایلر کد بومی |
| OCaml 3.10 | 2007 |  اتصالات `module type of`،`let`در تعاریف کلاس |
| OCaml 3.11 | 2008 |  حاشیه نویسی نوع `private`،`module type of`|
| OCaml 3.12 | 2010 | ماژول های درجه یک |
| OCaml 4.00 | 2012 | **رشته**:`module type of`,`val`در امضا |
| OCaml 4.01 | 2013 |  ماژول`Bytes`(رشته های قابل تغییر جدا شده اند) |
| OCaml 4.02 | 2014 |  ماژول `Float`، بهبودهای`String`|
| OCaml 4.03 | 2016 |  نوع `Result`،`Seq`(سکانس های تنبل) |
| OCaml 4.04 | 2017 | نمایه ساز Spacetime,`floatarray`|
| OCaml 4.06 | 2018 |  اتصالات`let`در عبارات`module`|
| OCaml 4.08 | 2019 |  بهبودهای `Binding`، بهبودهای`Seq`|
| OCaml 4.10 | 2020 |  بهبودهای`Bigarray`|
| OCaml 4.12 | 2021 |  بهبودهای`Stdlib`|
| OCaml 4.14 | 2022 | **Tail-modulo-cons** (TMC) |
| OCaml 5.0 | 2022 | **عمده**: کنترل کننده های اثر، موازی سازی (بدون GIL) |
| OCaml 5.1 | 2023 |  بهبودهای `Domain`، بهبودهای`Effect`|
| OCaml 5.2 | 2024 | پیام های خطای بهبود یافته، بهبودهای`Domain`|
| OCaml 5.3 | 2025 | توسعه در حال انجام |
## نقاط عطف اصلی
### Caml (1985–1995)
- **1985**: جرارد هوئت Caml را در INRIA (فرانسه) ایجاد کرد.
- **نام**: "زبان ماشینی انتزاعی دسته بندی"
- **1990**: Caml Light - نسخه سبک وزن توسط خاویر لروی
- تطبیق الگو، استنتاج نوع هیندلی-میلنر
### OCaml 1.0–3.x: افزودن OOP (1996–2011)
- **1996**: OCaml (Objective Caml) - ویژگی های شی گرا را اضافه می کند
- **3.0 (2000)**: روش های چند شکلی، ارزیابی `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **ماژول های درجه یک** — ماژول ها به عنوان مقادیر
### OCaml 4.x: OCaml مدرن (2012–2021)
- **4.00 (2012)**: `module type of`، سیستم ماژول بهبود یافته
- **4.01 (2013)**: ماژول`Bytes`- رشته های غیرقابل تغییر به طور پیش فرض
- **4.03 (2016)**: نوع `Result`،`Seq`(سکانس های تنبل)
- **4.08 (2019)**: پیام های خطای بهبود یافته
- **4.14 (2022)**: Tail-modulo-cons (TMC) - حافظه بهتر برای سازنده های بازگشتی
### OCaml 5.x: انقلاب موازی (2022–اکنون)
- **5.0 (2022)**: **کنترل کننده اثر**، **موازی واقعی** (GIL را برای کد خالص حذف می کند)
  -`Domain`- رشته های سیستم عامل برای محاسبات موازی
  -`Effect`- کنترل کننده های اثر جبری (ادامه)
  - دیگر خبری از قفل مترجم جهانی نیست - OCaml چند هسته ای واقعی
- **5.1 (2023)**: بهبود دامنه، اصلاحات کنترل کننده افکت
- **5.2 (2024)**: پیام های خطای بهتر، بهبودهای بیشتر
## تکامل نحو
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

## تایپ سیستم تکامل
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

## اصول کلیدی طراحی
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## رشد اکوسیستم
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
