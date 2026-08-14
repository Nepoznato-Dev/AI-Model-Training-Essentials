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
# OCaml — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| ক্যামল | 1985 | **শ্রেণীগত বিমূর্ত মেশিন ভাষা** (INRIA) |
| ক্যামল লাইট | 1990 | লাইটওয়েট ক্যামল (জেভিয়ার লেরয়) |
| OCaml 1.0 | 1996 | **উদ্দেশ্য Caml** — OOP যোগ করে |
| OCaml 3.0 | 2000 | **প্রধান**: বহুরূপী পদ্ধতি,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | নেটিভ-কোড কম্পাইলার উন্নতি |
| OCaml 3.10 | 2007 | `module type of`,`let`ক্লাস সংজ্ঞায় বাঁধাই |
| OCaml 3.11 | 2008 | `private`টাইপ টীকা,`module type of`|
| OCaml 3.12 | 2010 | প্রথম শ্রেণীর মডিউল |
| OCaml 4.00 | 2012 | **মেজর**:`module type of`,`val`স্বাক্ষরে |
| OCaml 4.01 | 2013 | `Bytes`মডিউল (পরিবর্তনযোগ্য স্ট্রিংগুলি পৃথক করা হয়েছে) |
| OCaml 4.02 | 2014 | `Float`মডিউল,`String`উন্নতি |
| OCaml 4.03 | 2016 | `Result`প্রকার,`Seq`(অলস ক্রম) |
| OCaml 4.04 | 2017 | স্পেসটাইম প্রোফাইলার,`floatarray`|
| OCaml 4.06 | 2018 | `module`এক্সপ্রেশনে`let`বাঁধাই |
| OCaml 4.08 | 2019 | `Binding`উন্নতি,`Seq`উন্নতি |
| OCaml 4.10 | 2020 | `Bigarray`উন্নতি |
| OCaml 4.12 | 2021 | `Stdlib`উন্নতি |
| OCaml 4.14 | 2022 | **টেইল-মডুলো-কনস** (TMC) |
| OCaml 5.0 | 2022 | **মেজর**: ইফেক্ট হ্যান্ডলার, সমান্তরালতা (কোন জিআইএল নেই) |
| OCaml 5.1 | 2023 | `Domain`উন্নতি,`Effect`উন্নতি |
| OCaml 5.2 | 2024 | উন্নত ত্রুটি বার্তা,`Domain`উন্নতি |
| OCaml 5.3 | 2025 | চলমান উন্নয়ন |
## প্রধান মাইলফলক
### ক্যামল (1985-1995)
- **1985**: জেরার্ড হুয়েট INRIA (ফ্রান্স) এ ক্যামল তৈরি করেন
- **নাম**: "শ্রেণীগত বিমূর্ত মেশিন ভাষা"
- **1990**: ক্যামল লাইট — জেভিয়ার লেরয় দ্বারা হালকা ওজনের সংস্করণ
- প্যাটার্ন ম্যাচিং, হিন্ডলি-মিলনার টাইপ ইনফারেন্স
### OCaml 1.0–3.x: OOP যোগ করা (1996-2011)
- **1996**: OCaml (উদ্দেশ্য Caml) — বস্তু-ভিত্তিক বৈশিষ্ট্য যোগ করে
- **3.0 (2000): পলিমরফিক পদ্ধতি,`lazy`মূল্যায়ন
- **3.10 (2007):`module type of`
- **3.12 (2010): **প্রথম শ্রেণীর মডিউল** — মান হিসাবে মডিউল
### OCaml 4.x: আধুনিক OCaml (2012–2021)
- **4.00 (2012): `module type of`, উন্নত মডিউল সিস্টেম
- **4.01 (2013):`Bytes`মডিউল — ডিফল্টরূপে অপরিবর্তনীয় স্ট্রিং
- **4.03 (2016):`Result`প্রকার,`Seq`(অলস ক্রম)
- **4.08 (2019): উন্নত ত্রুটি বার্তা
- **4.14 (2022)**: টেইল-মডুলো-কনস (টিএমসি) — রিকার্সিভ কনস্ট্রাক্টরদের জন্য আরও ভালো মেমরি
### OCaml 5.x: সমান্তরাল বিপ্লব (2022-বর্তমান)
- **5.0 (2022)**: **ইফেক্ট হ্যান্ডলার**, **সত্য সমান্তরালতা** (বিশুদ্ধ কোডের জন্য GIL সরিয়ে দেয়)
  -`Domain`— সমান্তরাল গণনার জন্য OS থ্রেড
  -`Effect`— বীজগণিত প্রভাব হ্যান্ডলার (চলবে)
  - আর কোন গ্লোবাল ইন্টারপ্রেটার লক নেই — বাস্তব মাল্টিকোর OCaml৷
- **5.1 (2023): ডোমেনের উন্নতি, প্রভাব হ্যান্ডলার পরিশোধন
- **5.2 (2024): আরও ভাল ত্রুটি বার্তা, আরও উন্নতি
## সিনট্যাক্স বিবর্তন
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

## টাইপ সিস্টেম বিবর্তন
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

## মূল ডিজাইনের নীতি
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## ইকোসিস্টেম বৃদ্ধি
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
