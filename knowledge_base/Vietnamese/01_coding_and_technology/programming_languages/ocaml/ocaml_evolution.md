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
# OCaml — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| Caml | 1985 | **Ngôn ngữ máy trừu tượng phân loại** (INRIA) |
| Ánh sáng Caml | 1990 | Caml nhẹ (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Caml khách quan** — thêm OOP |
| OCaml 3.0 | 2000 | **Chính**: Phương pháp đa hình,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | Cải tiến trình biên dịch mã gốc |
| OCaml 3.10 | 2007 |  Các liên kết`module type of`,`let`trong định nghĩa lớp |
| OCaml 3.11 | 2008 |  Chú thích loại `private`,`module type of`|
| OCaml 3.12 | 2010 | Mô-đun hạng nhất |
| OCaml 4.00 | 2012 | **Chính**:`module type of`,`val`trong chữ ký |
| OCaml 4.01 | 2013 |  Mô-đun`Bytes`(tách các chuỗi có thể thay đổi) |
| OCaml 4.02 | 2014 |  Mô-đun `Float`, cải tiến`String`|
| OCaml 4.03 | 2016 |  Loại `Result`,`Seq`(trình tự lười biếng) |
| OCaml 4.04 | 2017 | Trình phân tích không thời gian,`floatarray`|
| OCaml 4.06 | 2018 |  Liên kết`let`trong biểu thức`module`|
| OCaml 4.08 | 2019 |  Cải tiến `Binding`, cải tiến`Seq`|
| OCaml 4.10 | 2020 |  Cải tiến`Bigarray`|
| OCaml 4.12 | 2021 |  Cải tiến`Stdlib`|
| OCaml 4.14 | 2022 | **Tail-modulo-nhược điểm** (TMC) |
| OCaml 5.0 | 2022 | **Chính**: Trình xử lý hiệu ứng, song song (không có GIL) |
| OCaml 5.1 | 2023 |  Cải tiến `Domain`, cải tiến`Effect`|
| OCaml 5.2 | 2024 | Cải thiện thông báo lỗi, cải tiến`Domain`|
| OCaml 5.3 | 2025 | Đang phát triển |
## Các cột mốc quan trọng
### Caml (1985–1995)
- **1985**: Gérard Huet tạo ra Caml tại INRIA (Pháp)
- **Tên**: "Ngôn ngữ máy trừu tượng phân loại"
- **1990**: Caml Light — phiên bản nhẹ của Xavier Leroy
- So khớp mẫu, suy luận kiểu Hindley-Milner
### OCaml 1.0–3.x: Thêm OOP (1996–2011)
- **1996**: OCaml (Caml mục tiêu) — thêm các tính năng hướng đối tượng
- **3.0 (2000)**: Phương pháp đa hình, đánh giá `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **Mô-đun hạng nhất** — mô-đun làm giá trị
### OCaml 4.x: OCaml hiện đại (2012–2021)
- **4.00 (2012)**:`module type of`, hệ thống mô-đun cải tiến
- **4.01 (2013)**: Mô-đun`Bytes`— chuỗi bất biến theo mặc định
- **4.03 (2016)**: loại `Result`,`Seq`(chuỗi lười)
- **4.08 (2019)**: Thông báo lỗi được cải thiện
- **4.14 (2022)**: Tail-modulo-cons (TMC) — bộ nhớ tốt hơn cho hàm tạo đệ quy
### OCaml 5.x: Cuộc cách mạng song song (2022–nay)
- **5.0 (2022)**: **Trình xử lý hiệu ứng**, **song song thực sự** (xóa GIL đối với mã thuần túy)
  -`Domain`— Các luồng hệ điều hành để tính toán song song
  -`Effect`— trình xử lý hiệu ứng đại số (phần tiếp theo)
  - Không còn Khóa phiên dịch toàn cầu nữa - OCaml đa lõi thực sự
- **5.1 (2023)**: Cải tiến miền, cải tiến trình xử lý hiệu ứng
- **5.2 (2024)**: Thông báo lỗi tốt hơn, cải tiến hơn nữa
## Tiến hóa cú pháp
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

## Loại tiến hóa hệ thống
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

## Nguyên tắc thiết kế chính
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Tăng trưởng hệ sinh thái
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
