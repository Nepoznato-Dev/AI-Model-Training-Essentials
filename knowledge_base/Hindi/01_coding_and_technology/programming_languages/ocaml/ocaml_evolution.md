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
# OCaml - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| कैमल | 1985 | **श्रेणीबद्ध सार मशीन भाषा** (INRIA) |
| कैमल लाइट | 1990 | लाइटवेट कैमल (जेवियर लेरॉय) |
| ओकैमल 1.0 | 1996 | **उद्देश्य कैमल** - ओओपी जोड़ता है |
| ओकैमल 3.0 | 2000 | **प्रमुख**: बहुरूपी विधियाँ,`lazy`,`Obj`|
| ओकैमल 3.05 | 2002 | नेटिव-कोड कंपाइलर सुधार |
| ओकैमल 3.10 | 2007 |  कक्षा परिभाषाओं में`module type of`,`let`बाइंडिंग |
| ओकैमल 3.11 | 2008 | `private`प्रकार के एनोटेशन,`module type of`|
| ओकैमल 3.12 | 2010 | प्रथम श्रेणी के मॉड्यूल |
| ओकैमल 4.00 | 2012 | **प्रमुख**: हस्ताक्षर में`module type of`,`val`|
| ओकैमल 4.01 | 2013 | `Bytes`मॉड्यूल (परिवर्तनशील तार अलग) |
| ओकैमल 4.02 | 2014 | `Float`मॉड्यूल,`String`सुधार |
| ओकैमल 4.03 | 2016 | `Result`प्रकार,`Seq`(आलसी अनुक्रम) |
| ओकैमल 4.04 | 2017 | स्पेसटाइम प्रोफाइलर,`floatarray`|
| ओकैमल 4.06 | 2018 | `module`अभिव्यक्तियों में`let`बाइंडिंग |
| ओकैमल 4.08 | 2019 | `Binding`सुधार,`Seq`सुधार |
| ओकैमल 4.10 | 2020 | `Bigarray`सुधार |
| ओकैमल 4.12 | 2021 | `Stdlib`सुधार |
| ओकैमल 4.14 | 2022 | **टेल-मॉड्यूलो-कंस** (टीएमसी) |
| ओकैमल 5.0 | 2022 | **प्रमुख**: प्रभाव संचालक, समानता (कोई जीआईएल नहीं) |
| ओकैमल 5.1 | 2023 | `Domain`सुधार,`Effect`सुधार |
| ओकैमल 5.2 | 2024 | बेहतर त्रुटि संदेश,`Domain`सुधार |
| ओकैमल 5.3 | 2025 | निरंतर विकास |
## प्रमुख मील के पत्थर
### कैमल (1985-1995)
- **1985**: जेरार्ड ह्यूट ने आईएनआरआईए (फ्रांस) में कैमल बनाया
- **नाम**: "श्रेणीबद्ध सार मशीन भाषा"
- **1990**: कैमल लाइट - जेवियर लेरॉय द्वारा हल्का संस्करण
- पैटर्न मिलान, हिंडले-मिलनर प्रकार का अनुमान
### OCaml 1.0-3.x: OOP जोड़ना (1996-2011)
- **1996**: OCaml (ऑब्जेक्टिव कैमल) - ऑब्जेक्ट-ओरिएंटेड सुविधाएँ जोड़ता है
- **3.0 (2000)**: बहुरूपी विधियाँ,`lazy`मूल्यांकन
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **प्रथम श्रेणी के मॉड्यूल** — मान के रूप में मॉड्यूल
### OCaml 4.x: आधुनिक OCaml (2012-2021)
- **4.00 (2012)**: `module type of`, बेहतर मॉड्यूल सिस्टम
- **4.01 (2013)**:`Bytes`मॉड्यूल - डिफ़ॉल्ट रूप से अपरिवर्तनीय स्ट्रिंग्स
- **4.03 (2016)**:`Result`प्रकार,`Seq`(आलसी अनुक्रम)
- **4.08 (2019)**: बेहतर त्रुटि संदेश
- **4.14 (2022)**: टेल-मॉड्यूलो-कंस (टीएमसी) - पुनरावर्ती कंस्ट्रक्टर के लिए बेहतर मेमोरी
### OCaml 5.x: समानांतर क्रांति (2022-वर्तमान)
- **5.0 (2022)**: **प्रभाव संचालक**, **सच्ची समानता** (शुद्ध कोड के लिए जीआईएल हटाता है)
  -`Domain`- समानांतर गणना के लिए ओएस थ्रेड
  -`Effect`- बीजगणितीय प्रभाव संचालक (निरंतरता)
  - अब कोई ग्लोबल इंटरप्रेटर लॉक नहीं - वास्तविक मल्टीकोर OCaml
- **5.1 (2023)**: डोमेन सुधार, प्रभाव हैंडलर परिशोधन
- **5.2 (2024)**: बेहतर त्रुटि संदेश, और सुधार
## सिंटेक्स इवोल्यूशन
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

## टाइप सिस्टम इवोल्यूशन
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

## मुख्य डिज़ाइन सिद्धांत
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## पारिस्थितिकी तंत्र का विकास
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
