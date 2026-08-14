---
# Metadata
title: "OCaml"
description: "Comprehensive reference for the OCaml programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ocaml, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# OCaml
OCaml (Objective Caml) یک زبان برنامه نویسی تابعی است که در INRIA در فرانسه توسعه یافته و اولین بار در سال 1996 منتشر شد. این زبان بیانی بودن برنامه نویسی تابعی را با ویژگی های عملی ترکیب می کند: یک سیستم نوع قدرتمند با استنتاج نوع (Hindley-Milner)، تطبیق الگو، انواع داده های جبری، و برنامه نویسی شی گرا اختیاری. OCaml به کد بومی سریع کامپایل می شود و همچنین از بایت کد پشتیبانی می کند.
معروف ترین برنامه واقعی OCaml شرکت تجاری **Jane Street** است که از OCaml برای کل زیرساخت تجاری خود استفاده می کند. همچنین در توسعه کامپایلر (کامپایلر Rust در اصل در OCaml نوشته شده بود)، تأیید رسمی، سیستم های مالی و اثبات قضیه استفاده می شود.
خواهر و برادر جدیدتر OCaml **Reason** (توسعه یافته توسط Facebook/Meta) و **ReScript** (قبلا BuckleScript) سیستم نوع و عملکرد OCaml را به توسعه وب و کامپایل کردن به جاوا اسکریپت می آورند.
---

## چرا OCaml مهم است
- **استنتاج نوع **: کامپایلر انواع را به طور خودکار تشخیص می دهد - برای اکثر کدها نیازی به حاشیه نویسی نیست.
- ** انواع داده های جبری + تطبیق الگو **: دامنه های پیچیده را به طور دقیق مدل سازی کنید. کامپایلر هر موردی را که شما مدیریت کرده اید بررسی می کند.
- **عملکرد**: به کدهای بومی که در بسیاری از معیارها با C++ رقابت می کند، کامپایل می شود.
- **تغییرناپذیری به صورت پیش‌فرض**: مقادیر غیرقابل تغییر هستند، مگر اینکه به طور صریح دیگری علامت‌گذاری شده باشند. اشکالات کمتر.
- **ماژول ها و تابع ها**: مکانیزم های انتزاعی قدرتمند برای ساختن سیستم های بزرگ.
- **روش های رسمی**: در اثبات قضیه (Coq)، بررسی مدل و نرم افزار تایید شده استفاده می شود.
- **ساخت کامپایلر**: برای ساخت کامپایلرها، مفسرها و ابزارهای زبان عالی است.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **منحنی یادگیری شیب دار** | برنامه نویسی تابعی، نوع سیستم و نحو ناآشنا هستند | با تطبیق الگو و ADT ها شروع کنید. ایجاد به تدریج |
| **بازار کار کوچک** | طاقچه — در درجه اول امور مالی (خیابان جین) و تحقیقات | علاقه روزافزون به سیستم های ایمن نوع |
| **اکوسیستم وب محدود** | یک زبان اصلی وب نیست | از ReScript (OCaml-to-JS) برای توسعه وب استفاده کنید |
| **پیام های خطا** | خطاهای نوع می تواند مرموز باشد، به خصوص با انواع پیچیده | از پلاگین Merlin IDE استفاده کنید. یاد بگیرید تایپ امضا را بخوانید |
| **همزمان** | بدون async/wait یا رشته سبز داخلی | از کتابخانه های Lwt یا Async استفاده کنید. OCaml 5 پشتیبانی چند هسته ای را اضافه کرد |
| **مستندات** | برای مبتدیان کمتر از اکوسیستم پایتون یا Rust | دنیای واقعی OCaml (کتاب) عالی است |
---

## اصول نحو
```ocaml
(* Variables — immutable by default *)
let name = "Alice"
let age = 30
let pi = 3.14159

(* Mutable variables (explicit) *)
let counter = ref 0
counter := !counter + 1

(* Functions *)
let add a b = a + b
let greet name = Printf.sprintf "Hello, %s!" name

(* Type inference — the compiler figures this out *)
let double x = x * 2        (* inferred: int -> int *)
let length s = String.length s  (* inferred: string -> int *)

(* Pattern matching (OCaml's superpower) *)
type shape =
  | Circle of float
  | Rectangle of float * float
  | Triangle of float * float * float

let area = function
  | Circle r -> Float.pi *. r *. r
  | Rectangle (w, h) -> w *. h
  | Triangle (a, b, c) ->
      let s = (a +. b +. c) /. 2.0 in
      Float.sqrt (s *. (s -. a) *. (s -. b) *. (s -. c))

(* Option type — no null references *)
let find_user id =
  if id > 0 then Some { name = "Alice"; id }
  else None

match find_user 1 with
| Some user -> Printf.sprintf "Found: %s" user.name
| None -> "User not found"

(* Algebraic data types *)
type 'a list =
  | Empty
  | Cons of 'a * 'a list

let rec length = function
  | Empty -> 0
  | Cons (_, rest) -> 1 + length rest

(* Records *)
type user = {
  name: string;
  age: int;
  email: string;
}

let alice = { name = "Alice"; age = 30; email = "alice@example.com" }
let older_alice = { alice with age = 31 }  (* Immutable update *)

(* Higher-order functions *)
let numbers = [1; 2; 3; 4; 5]
let doubled = List.map (fun x -> x * 2) numbers
let evens = List.filter (fun x -> x mod 2 = 0) numbers
let sum = List.fold_left (+) 0 numbers

(* Pipe operator *)
let result =
  numbers
  |> List.map (fun x -> x * x)
  |> List.filter (fun x -> x > 5)
  |> List.fold_left (+) 0

(* Result type for error handling *)
type ('a, 'b) result =
  | Ok of 'a
  | Error of 'b

let divide a b =
  if b = 0 then Error "Division by zero"
  else Ok (a / b)

(* Modules *)
module Stack = struct
  type 'a t = 'a list
  let empty = []
  let push x s = x :: s
  let pop = function
    | [] -> None
    | x :: rest -> Some (x, rest)
end

(* Parametric polymorphism (generics) *)
let rec map f = function
  | [] -> []
  | x :: rest -> f x :: map f rest

(* OCaml 5: Multicore / parallelism *)
let domains = List.init 4 (fun i ->
  Domain.spawn (fun () ->
    Printf.printf "Domain %d running\n%!" i
  )
)
List.iter Domain.join domains
```

---

## OCaml's Type System در عمل
```ocaml
(* The compiler catches bugs at compile time *)

(* Exhaustiveness checking *)
type color = Red | Green | Blue
let describe = function
  | Red -> "warm"
  | Green -> "cool"
  (* Compiler warning: missing Blue case! *)

(* GADTs — advanced type-level programming *)
type _ expr =
  | Int : int -> int expr
  | Bool : bool -> bool expr
  | Add : int expr * int expr -> int expr
  | If : bool expr * 'a expr * 'a expr -> 'a expr

(* Type-safe evaluators *)
let rec eval : type a. a expr -> a = function
  | Int n -> n
  | Bool b -> b
  | Add (a, b) -> eval a + eval b
  | If (cond, t, f) -> if eval cond then eval t else eval f
```


---

## نحو و الگوهای پیشرفته
### امضاها و کارکردهای ماژول
```ocaml
(* Module signatures — interfaces for modules *)
module type COMPARABLE = sig
  type t
  val compare : t -> t -> int
end

module type SET = sig
  type elt
  type t
  val empty : t
  val add : elt -> t -> t
  val mem : elt -> t -> bool
  val elements : t -> elt list
end

(* Functor — a module parameterized by another module *)
module MakeSet (Ord : COMPARABLE) : SET with type elt = Ord.t = struct
  type elt = Ord.t
  type t = elt list

  let empty = []

  let rec add x = function
    | [] -> [x]
    | h :: t as s ->
        let c = Ord.compare x h in
        if c = 0 then s
        else if c < 0 then x :: s
        else h :: add x t

  let rec mem x = function
    | [] -> false
    | h :: t ->
        let c = Ord.compare x h in
        if c = 0 then true
        else if c < 0 then false
        else mem x t

  let elements s = s
end

(* Use the functor *)
module IntSet = MakeSet(struct
  type t = int
  let compare = Int.compare
end)

let s = IntSet.(empty |> add 3 |> add 1 |> add 2)
IntSet.mem 2 s  (* true *)
IntSet.elements s  (* [1; 2; 3] *)
```

### ماژول های درجه یک
```ocaml
(* Pack a module as a value *)
module type PRINTER = sig
  type t
  val print : t -> unit
end

let int_printer =
  (module struct
    type t = int
    let print = Printf.printf "%d\n"
  end : PRINTER with type t = int)

(* Unpack and use *)
let use_printer (type a) (module P : PRINTER with type t = a) (x : a) =
  P.print x

let () = use_printer int_printer 42
```

### تطبیق الگوی پیشرفته
```ocaml
(* Or-patterns *)
let is_weekend = function
  | `Saturday | `Sunday -> true
  | _ -> false

(* Alias patterns *)
let describe_point = function
  | (0, 0) as origin -> Printf.sprintf "Origin: %s" (string_of_int (fst origin))
  | (x, 0) -> Printf.sprintf "On x-axis at %d" x
  | (0, y) -> Printf.sprintf "On y-axis at %d" y
  | (x, y) -> Printf.sprintf "Point (%d, %d)" x y

(* When guards *)
let classify = function
  | x when x < 0 -> "negative"
  | 0 -> "zero"
  | x when x <= 100 -> "small positive"
  | _ -> "large positive"

(* Exception patterns *)
let safe_divide a b =
  try Some (a / b)
  with Division_by_zero -> None
```

### انواع چند شکلی
```ocaml
(* More flexible than regular variants — no type declaration needed *)
let to_string = function
  | `Red -> "red"
  | `Green -> "green"
  | `Blue -> "blue"

(* Open variants — functions accept superset *)
let describe_color = function
  | `Red -> "warm"
  | `Green -> "cool"
  | `Blue -> "calm"
  | `Custom (r, g, b) -> Printf.sprintf "rgb(%d,%d,%d)" r g b

(* Variant subtyping *)
type basic_color = [ `Red | `Green | `Blue ]
type extended_color = [ basic_color | `Custom of int * int * int ]
```


---

## همزمانی و موازی
### OCaml 5 چند هسته ای (دامنه ها)
```ocaml
(* Domains — true parallelism on multicore hardware *)
let parallel_map f list =
  let domains = List.map (fun item ->
    Domain.spawn (fun () -> f item)
  ) list in
  List.map Domain.join domains

(* Example: parallel computation *)
let results = parallel_map (fun n ->
  (* CPU-intensive work *)
  let rec fib = function 0 | 1 -> 1 | n -> fib (n-1) + fib (n-2) in
  fib n
) [35; 36; 37; 38]

(* Atomic references for shared state *)
let shared_counter = Atomic.make 0

let increment () =
  Atomic.fetch_and_add shared_counter 1

(* Domains all increment concurrently *)
let domains = List.init 4 (fun _ ->
  Domain.spawn (fun () ->
    for _ = 1 to 1000 do increment () done
  )
)
List.iter Domain.join domains
Atomic.get shared_counter  (* 4000 *)
```

### Lwt - همزمانی تعاونی
```ocaml
(* Lwt promises — cooperative (single-threaded) async *)
open Lwt

(* Creating promises *)
let fetch_data url =
  Lwt_io.with_file ~mode:Lwt_io.input url (fun ic ->
    Lwt_io.read ic
  )

(* Composing promises *)
let process () =
  let%lwt data1 = fetch_data "file1.txt" in
  let%lwt data2 = fetch_data "file2.txt" in
  Lwt.return (data1 ^ data2)

(* Running concurrently *)
let fetch_all urls =
  Lwt_list.map_p (fun url -> fetch_data url) urls

(* Error handling *)
let safe_fetch url =
  Lwt.catch
    (fun () -> fetch_data url)
    (fun ex -> Lwt.return ("Error: " ^ Printexc.to_string ex))
```

---

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه (تلماسه)
```
my-ocaml-project/
├── bin/
│   ├── dune
│   └── main.ml              # Entry point
├── lib/
│   ├── dune
│   ├── my_project.ml        # Library root
│   ├── types.ml
│   └── service.ml
├── test/
│   ├── dune
│   └── test_my_project.ml
├── dune-project             # Project metadata
├── my-ocaml-project.opam    # Package description
└── README.md
```

### پیکربندی Dune Build
```lisp
; dune-project
(lang dune 3.0)
(name my-ocaml-project)
(generate_opam_files true)
(source (github user/my-ocaml-project))
(license MIT)
(authors "Developer Name")
(package
 (name my-ocaml-project)
 (synopsis "A sample OCaml project")
 (depends
  (ocaml (>= 5.0))
  (dune (>= 3.0))
  lwt
  cohttp-lwt-unix
  ppx_let
  core))
```

```lisp
; lib/dune
(library
 (name my_project)
 (public_name my-ocaml-project.lib)
 (libraries core lwt)
 (preprocess (pps ppx_let)))

; bin/dune
(executable
 (name main)
 (public_name my-ocaml-project)
 (libraries my_project.core core lwt cohttp-lwt-unix)
 (preprocess (pps ppx_let)))

; test/dune
(test
 (name test_my_project)
 (libraries my_project.core core alcotest)
 (preprocess (pps ppx_let)))
```

### دستورات ساخت کلید
| فرمان | توضیحات |
|---------|-------------|
| `dune init project my_app`| ایجاد پروژه جدید |
| `dune build`| ساخت پروژه |
| `dune exec ./bin/main.exe`| اجرای |
| `dune test`| اجرای تست ها |
| `dune clean`| مصنوعات ساخت تمیز |
| `dune utop`| شروع REPL با پروژه بارگذاری شده |
| `opam install . --deps-only`| نصب وابستگی ها |
| `dune build @fmt`| کد قالب |
| `opam switch create 5.1`| ایجاد سوئیچ OCaml 5.1 |
---

## تست
### Alcotest - تست سبک وزن
```ocaml
open Alcotest

let test_add () =
  check int "2 + 3 = 5" 5 (MyProject.Math.add 2 3);
  check int "0 + 0 = 0" 0 (MyProject.Math.add 0 0);
  check int "negative" (-3) (MyProject.Math.add (-1) (-2))

let test_factorial () =
  check int "0! = 1" 1 (MyProject.Math.factorial 0);
  check int "5! = 120" 120 (MyProject.Math.factorial 5);
  check int "10! = 3628800" 3628800 (MyProject.Math.factorial 10)

let test_suite =
  [ "Math", [
      test_case "add" `Quick test_add;
      test_case "factorial" `Quick test_factorial;
    ]
  ]

let () = run "MyProject" test_suite
```

### QCheck - تست مبتنی بر ویژگی
```ocaml
open QCheck

(* Properties to verify *)
let reverse_involutive =
  make (list int)
  ~name:"reverse is involutive"
  (fun lst -> List.rev (List.rev lst) = lst)

let sort_idempotent =
  make (list int)
  ~name:"sort is idempotent"
  (fun lst -> List.sort compare (List.sort compare lst) = List.sort compare lst)

let map_preserves_length =
  make (list int)
  ~name:"map preserves length"
  (fun lst -> List.length (List.map (fun x -> x * 2) lst) = List.length lst)

(* Run all properties *)
let () =
  QCheck_runner.run_tests_main [
    reverse_involutive;
    sort_idempotent;
    map_preserves_length;
  ]
```


---

## قابلیت همکاری
### C رابط عملکرد خارجی
```ocaml
(* Calling C from OCaml *)
external c_strlen : string -> int = "caml_strlen"

(* In C file (stubs.c): *)
(* #include <caml/mlvalues.h>
   #include <string.h>
   CAMLprim value caml_strlen(value s) {
     return Val_int(strlen(String_val(s)));
   }
*)

(* Calling standard C library *)
external c_system : string -> int = "caml_system"

(* Working with C types *)
external c_malloc : int -> nativeint = "caml_malloc"
external c_free : nativeint -> unit = "caml_free"

(* Bigarray for sharing memory with C *)
open Bigarray
let shared_buffer = Array1.create float64 c_layout 1024
```

### JavaScript Interop (js_of_ocaml / ReScript)
```ocaml
(* js_of_ocaml — compile OCaml to JavaScript *)
(* Access browser APIs *)
let () =
  let doc = Dom_html.document in
  let elem = Dom_html.getElementById_exn "app" in
  elem##.innerHTML := Js.string "Hello from OCaml!"
```

---

## الگوهای طراحی
### فینال بدون برچسب در OCaml
```ocaml
(* Define the DSL as a module type *)
module type EXPR = sig
  type 'a t
  val lit : int -> int t
  val add : int t -> int t -> int t
  val mul : int t -> int t -> int t
  val ifz : int t -> 'a t -> 'a t -> 'a t
end

(* Interpretation 1: Direct evaluation *)
module Eval : EXPR with type 'a t = 'a = struct
  type 'a t = 'a
  let lit n = n
  let add a b = a + b
  let mul a b = a * b
  let ifz c t f = if c = 0 then t else f
end

(* Interpretation 2: Pretty printing *)
module Pretty : EXPR with type 'a t = string = struct
  type 'a t = string
  let lit n = string_of_int n
  let add a b = "(" ^ a ^ " + " ^ b ^ ")"
  let mul a b = "(" ^ a ^ " * " ^ b ^ ")"
  let ifz c t f = "(if " ^ c ^ " = 0 then " ^ t ^ " else " ^ f ^ ")"
end

(* Same expression, different interpretations *)
module MakeExpr (E : EXPR) = struct
  open E
  let example = add (lit 3) (mul (lit 4) (lit 5))
end

module EvalExpr = MakeExpr(Eval)
module PrettyExpr = MakeExpr(Pretty)

let () =
  Printf.printf "Eval: %d\n" EvalExpr.example;       (* 23 *)
  Printf.printf "Pretty: %s\n" PrettyExpr.example     (* (3 + (4 * 5)) *)
```

### مدیریت خطا با نتیجه
```ocaml
(* Composable error handling *)
let ( let* ) = Result.bind

type user = { name: string; age: int }
type error = NotFound of string | ValidationError of string

let validate_age age =
  if age < 0 then Error (ValidationError "Age cannot be negative")
  else if age > 150 then Error (ValidationError "Age too large")
  else Ok age

let find_user_by_id id =
  if id > 0 then Ok { name = "Alice"; age = 30 }
  else Error (NotFound (string_of_int id))

let process_user id =
  let* user = find_user_by_id id in
  let* _age = validate_age user.age in
  Ok (Printf.sprintf "%s is %d years old" user.name user.age)
```

---

## عملکرد و بهینه سازی
### ابزارهای پروفایل
| ابزار | هدف | استفاده |
|------|---------|-------|
| **ocamlprof** | پروفایل تعداد اعدام | `ocamlc -p`سپس`ocamlprof`|
| **پرف** | پروفایلر سیستم لینوکس | `perf record ./program`|
| **فضا-زمان** | پروفایل حافظه (4.x) | `OCAML_SPACETIME_INTERVAL=1000 ./program`|
| **معیار** | میکرو بنچمارک |  بسته`ocaml-benchmark`|
### تکنیک های بهینه سازی
```ocaml
(* 1. Unboxed floats — avoid allocation *)
let[@inline] fast_dot (a : float) (b : float) (c : float) (d : float) =
  a *. c +. b *. d

(* 2. Unboxed types (OCaml 5) *)
type point = Point of (float[@unboxed]) * (float[@unboxed])

(* 3. Tail recursion — the compiler optimizes tail calls *)
let rec sum_tail acc = function
  | [] -> acc
  | x :: rest -> sum_tail (acc + x) rest

let sum lst = sum_tail 0 lst

(* 4. Strict fields to avoid indirection *)
type config = {
  timeout: int;
  retries: int;
  name: string;
}

(* 5. Specialize with [@specialize] or [@inline] attributes *)
let[@inline always] max_int a b = if a >= b then a else b

(* 6. Compile flags for performance *)
(* ocamlopt -O3 -unbox-closures -o program *)
```

---

## استقرار
### ساخت باینری های بومی
```bash
# Build with dune
dune build @install
dune build --force

# Create optimized native binary
dune build --release
# Output: _build/default/bin/main.exe
```

### استقرار داکر
```dockerfile
FROM ocaml/opam:ubuntu-22.04-ocaml-5.1 AS builder
WORKDIR /app
COPY --chown=opam . .
RUN opam install . --deps-only --with-test
RUN opam exec -- dune build --force

FROM ubuntu:22.04
WORKDIR /app
COPY --from=builder /app/_build/default/bin/main.exe ./app
RUN apt-get update && apt-get install -y libgmp10 && rm -rf /var/lib/apt/lists/*
EXPOSE 8080
ENTRYPOINT ["./app"]
```

---

## چه زمانی از OCaml استفاده کنیم
| سناریو | چرا OCaml | جایگزین بهتر |
|----------|---------|-------------------|
| کامپایلر / ابزار زبان | عالی برای AST ها، بررسی نوع، تولید کد | زنگ برای ابزارهای حیاتی عملکرد |
| سیستم های مالی | جین استریت آن را در مقیاس | C++، جاوا، پایتون |
| تایید رسمی | سیستم نوع قوی، پشتیبانی اثبات قضیه | Coq، Agda برای اثبات محض |
| مدل سازی دامنه | ADTs + الگوی تطبیق مدل قوانین پیچیده دقیقا | TypeScript برای دامنه های وب |
| محاسبات با کارایی بالا | تولید کد بومی | C، C++، Rust، Fortran |
| توسعه وب | امکان با ReScript/OCaml | TypeScript، Go، Python |
| علم داده / ML | نه اکوسیستم | پایتون، R |
| برنامه های موبایل | مناسب نیست | سویفت، کاتلین، دارت |
| برنامه های کاربردی همه منظوره | ممکن است اما طاقچه | برو، پایتون، زنگ |
---

## پرسش و پاسخ مصنوعی
### Q1: استنتاج نوع OCaml چگونه کار می کند؟
**A:** سیستم نوع Hindley-Milner OCaml انواع را بدون حاشیه نویسی استنباط می کند:
```ocaml
let add x y = x + y        (* inferred: int -> int -> int *)
let map f lst = List.map f lst  (* inferred: ('a -> 'b) -> 'a list -> 'b list *)
let length lst = List.length lst (* inferred: 'a list -> int *)
```

### Q2: انواع داده های جبری چیست و چرا قدرتمند هستند؟
**A:** ADT ها انواع محصول (سوابق) و انواع مجموع (انواع) را ترکیب می کنند:
```ocaml
type shape =
  | Circle of float
  | Rectangle of float * float
  | Triangle of float * float * float

let area = function
  | Circle r -> Float.pi *. r *. r
  | Rectangle (w, h) -> w *. h
  | Triangle (a, b, c) ->
      let s = (a +. b +. c) /. 2.0 in
      sqrt (s *. (s -. a) *. (s -. b) *. (s -. c))
(* Compiler warns if you forget a case! *)
```

### Q3: ماژول ها و تابع ها چگونه کار می کنند؟
**A:** ماژول ها کد را سازماندهی می کنند. تابع ها توابعی از ماژول ها به ماژول ها هستند:
```ocaml
module type COMPARABLE = sig
  type t
  val compare : t -> t -> int
end

module Set (Elem : COMPARABLE) = struct
  type elt = Elem.t
  type t = elt list
  let empty = []
  let mem x s = List.exists (fun y -> Elem.compare x y = 0) s
  let add x s = if mem x s then s else x :: s
end
```

### Q4: چه چیزی OCaml را سریع می کند؟
**A:** OCaml به کد بومی کارآمد کامپایل می‌شود:
- پاک کردن نوع - بدون بررسی نوع زمان اجرا
- شناورها و اعداد صحیح جعبه نشده
- تطبیق الگو برای پرش جداول کامپایل می شود
- بهینه سازی دم تماس
- بدون مکث زباله جمع کن (GC افزایشی)
### Q5: OCaml چگونه با سایر زبان های خانواده ML مقایسه می شود؟
**A:** OCaml عملی و خلوص را متعادل می کند:
- در مقابل Haskell: OCaml دارای ویژگی های ضروری، حالت تغییرپذیر و کامپایل سریعتر است.
- در مقابل F#: OCaml دارای یک سیستم ماژول بالغ تر و پشتیبانی از پلتفرم های مختلف است
- در مقابل Rust: OCaml دارای GC (بدون مالکیت)، اما Rust دارای FFI و اکوسیستم بهتری است
---

## حل مسئله زنجیره ای از فکر
### مشکل 1: پیاده سازی یک مترجم تایپ ایمن
**مرحله 1: مشکل را درک کنید**
یک مترجم برای یک زبان بیان ساده بسازید.
**مرحله 2: رویکرد را شناسایی کنید**
از انواع داده های جبری برای عبارات و تطبیق الگو برای ارزیابی استفاده کنید.
**مرحله 3: پیاده سازی **```ocaml
type expr =
  | Num of float
  | Add of expr * expr
  | Mul of expr * expr
  | Var of string

type env = (string * float) list

let rec eval (env : env) = function
  | Num n -> n
  | Add (a, b) -> eval env a +. eval env b
  | Mul (a, b) -> eval env a *. eval env b
  | Var name -> List.assoc name env

let env = [("x", 3.0); ("y", 4.0)]
let result = eval env (Add (Mul (Var "x", Var "x"), Mul (Var "y", Var "y")))
(* 3*3 + 4*4 = 25.0 *)
```

**مرحله 4: تمدید**
برای یک زبان کامل تر، `Let`، `If`،`Lambda`را اضافه کنید.
### مسئله 2: ساختن یک تجزیه کننده ساده با ترکیب کننده ها
**مرحله 1: مشکل را درک کنید**
عبارات حسابی را با استفاده از ترکیب کننده های تجزیه کننده تجزیه کنید.
**مرحله 2: رویکرد را شناسایی کنید**
تجزیه کننده های کوچک بسازید و آنها را بنویسید.
**مرحله 3: پیاده سازی **```ocaml
type 'a parser = string -> ('a * string) option

let return x s = Some (x, s)
let fail _s = None
let bind p f s = match p s with
  | None -> None
  | Some (a, rest) -> f a rest

let char c s = match s with
  | "" -> None
  | s' when s'.[0] = c -> Some (c, String.sub s' 1 (String.length s' - 1))
  | _ -> None

let digit s = match s with
  | "" -> None
  | s' when s'.[0] >= '0' && s'.[0] <= '9' ->
      Some (int_of_char s'.[0] - int_of_char '0',
            String.sub s' 1 (String.length s' - 1))
  | _ -> None
```

**مرحله 4: نوشتن**
تجزیه کننده ها را با `map`، `seq`، `alt`، و`many`ترکیب کنید تا عبارات کامل را تجزیه کنید.
---

## خلاصه
OCaml زبانی است که به شما برای تفکر دقیق در مورد داده های خود پاداش می دهد. انواع داده‌های جبری و تطبیق الگوی جامع آن، شما را مجبور می‌کند تا هر موردی را در نظر بگیرید - کامپایلر به یک شریک طراحی تبدیل می‌شود که اشتباهات را قبل از وقوع آنها تشخیص می‌دهد. استنتاج نوع به این معنی است که شما بدون نوشتن یادداشت‌های نوع در همه جا، از این مزایای ایمنی برخوردار می‌شوید. تأثیر OCaml در Rust، F#، TypeScript و Swift قابل مشاهده است – که همگی ایده‌هایی را از سیستم نوع OCaml به عاریت گرفته‌اند. در حالی که بازار کار OCaml کوچک است، یادگیری آن مهارت های برنامه نویسی شما را به روش هایی که به هر زبانی منتقل می شود، تقویت می کند.