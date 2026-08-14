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
# OCaml — ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| คาเมล | 1985 | **ภาษาเครื่องที่เป็นนามธรรมเชิงหมวดหมู่** (INRIA) |
| แสงแคมล์ | 1990 | Caml น้ำหนักเบา (Xavier Leroy) |
| OCaml 1.0 | 1996 | **วัตถุประสงค์ Caml** — เพิ่ม OOP |
| OCaml 3.0 | 2000 | **หลัก**: วิธีโพลีมอร์ฟิก`lazy`,`Obj`|
| OCaml 3.05 | 2545 | การปรับปรุงคอมไพเลอร์โค้ดเนทิฟ |
| OCaml 3.10 | 2550 | `module type of`,`let`การเชื่อมโยงในคำจำกัดความของคลาส |
| OCaml 3.11 | 2551 |  คำอธิบายประกอบประเภท `private`,`module type of`|
| OCaml 3.12 | 2010 | โมดูลชั้นหนึ่ง |
| OCaml 4.00 | 2555 | **หลัก**:`module type of`,`val`ในลายเซ็น |
| OCaml 4.01 | 2013 |  โมดูล`Bytes`(แยกสตริงที่ไม่แน่นอน) |
| OCaml 4.02 | 2014 |  โมดูล`Float`การปรับปรุง`String`|
| OCaml 4.03 | 2559 |  ประเภท `Result`,`Seq`(ลำดับแบบขี้เกียจ) |
| OCaml 4.04 | 2017 | เครื่องมือสร้างโปรไฟล์กาลอวกาศ`floatarray`|
| OCaml 4.06 | 2018 | `let`การเชื่อมโยงในนิพจน์`module`|
| OCaml 4.08 | 2019 |  การปรับปรุง `Binding`, การปรับปรุง`Seq`|
| OCaml 4.10 | 2020 |  การปรับปรุง`Bigarray`|
| OCaml 4.12 | 2021 |  การปรับปรุง`Stdlib`|
| OCaml 4.14 | 2022 | **Tail-modulo-cons** (TMC) |
| OCaml 5.0 | 2022 | **หลัก**: ตัวจัดการเอฟเฟกต์ ความเท่าเทียม (ไม่มี GIL) |
| OCaml 5.1 | 2023 |  การปรับปรุง `Domain`, การปรับปรุง`Effect`|
| OCaml 5.2 | 2024 | ปรับปรุงข้อความแสดงข้อผิดพลาด ปรับปรุง`Domain`|
| OCaml 5.3 | 2025 | การพัฒนาอย่างต่อเนื่อง |
## เหตุการณ์สำคัญที่สำคัญ
### คาเมล (1985–1995)
- **1985**: Gérard Huet สร้าง Caml ที่ INRIA (ฝรั่งเศส)
- **ชื่อ**: "ภาษาเครื่องที่เป็นนามธรรมเชิงหมวดหมู่"
- **1990**: Caml Light — เวอร์ชันน้ำหนักเบาโดย Xavier Leroy
- การจับคู่รูปแบบ การอนุมานประเภทฮินด์ลีย์-มิลเนอร์
### OCaml 1.0–3.x: การเพิ่ม OOP (1996–2011)
- **1996**: OCaml (Objective Caml) — เพิ่มฟีเจอร์เชิงวัตถุ
- **3.0 (2000)**: วิธีโพลีมอร์ฟิก, การประเมิน `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **โมดูลชั้นหนึ่ง** — โมดูลเป็นค่า
### OCaml 4.x: OCaml สมัยใหม่ (2012–2021)
- **4.00 (2012)**:`module type of`ปรับปรุงระบบโมดูล
- **4.01 (2013)**: โมดูล`Bytes`— สตริงที่ไม่เปลี่ยนรูปตามค่าเริ่มต้น
- **4.03 (2016)**: ประเภท `Result`,`Seq`(ลำดับแบบขี้เกียจ)
- **4.08 (2019)**: ปรับปรุงข้อความแสดงข้อผิดพลาด
- **4.14 (2022)**: Tail-modulo-cons (TMC) — หน่วยความจำที่ดีกว่าสำหรับคอนสตรัคเตอร์แบบเรียกซ้ำ
### OCaml 5.x: การปฏิวัติคู่ขนาน (2022–ปัจจุบัน)
- **5.0 (2022)**: **ตัวจัดการเอฟเฟกต์**, **ความขนานที่แท้จริง** (ลบ GIL สำหรับโค้ดบริสุทธิ์)
  -`Domain`— เธรด OS สำหรับการคำนวณแบบขนาน
  -`Effect`- ตัวจัดการเอฟเฟกต์พีชคณิต (ต่อ)
  - ไม่มีการล็อคล่ามทั่วโลกอีกต่อไป - OCaml แบบมัลติคอร์จริง
- **5.1 (2023)**: การปรับปรุงโดเมน การปรับแต่งตัวจัดการเอฟเฟกต์
- **5.2 (2024)**: ข้อความแสดงข้อผิดพลาดที่ดีขึ้น การปรับปรุงเพิ่มเติม
## วิวัฒนาการไวยากรณ์
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

## ประเภทวิวัฒนาการของระบบ
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

## หลักการออกแบบที่สำคัญ
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## การเติบโตของระบบนิเวศ
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
