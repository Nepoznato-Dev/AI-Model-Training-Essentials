---
# Metadata
title: "OCaml"
description: "Comprehensive reference for the OCaml programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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
OCaml (Objective Caml) ایک فنکشنل پروگرامنگ لینگویج ہے جو فرانس میں INRIA میں تیار کی گئی تھی، جو پہلی بار 1996 میں ریلیز ہوئی تھی۔ یہ فنکشنل پروگرامنگ کے اظہار کو عملی خصوصیات کے ساتھ جوڑتی ہے: ایک طاقتور قسم کا نظام جس میں ٹائپ انفرنس (Hindley-Milner)، پیٹرن میچنگ، الجبری ڈیٹا کی اقسام، اور اختیاری آبجیکٹ پر مبنی پروگرامنگ ہے۔ OCaml تیز مقامی کوڈ پر مرتب کرتا ہے اور بائیک کوڈ کو بھی سپورٹ کرتا ہے۔
OCaml کی حقیقی دنیا کی سب سے مشہور ایپلی کیشن **Jane Street** ٹریڈنگ فرم ہے، جو اپنے پورے تجارتی انفراسٹرکچر کے لیے OCaml کا استعمال کرتی ہے۔ یہ کمپائلر ڈویلپمنٹ میں بھی استعمال ہوتا ہے (رسٹ کمپائلر اصل میں OCaml میں لکھا گیا تھا)، رسمی تصدیق، مالیاتی نظام، اور تھیوری ثابت کرنے میں۔
OCaml کے نئے بہن بھائی **Reason** (Facebook/Meta کے ذریعے تیار کردہ) اور **ReScript** (سابقہ ​​BuckleScript) OCaml کے ٹائپ سسٹم اور کارکردگی کو ویب ڈویلپمنٹ میں لاتے ہیں، جاوا اسکرپٹ پر مرتب کرتے ہیں۔
---

## OCaml کیوں اہمیت رکھتا ہے۔
- **قسم کا اندازہ**: مرتب کرنے والا خود بخود اقسام کا پتہ لگاتا ہے — زیادہ تر کوڈ کے لیے تشریحات کی ضرورت نہیں ہے۔
- **الجبری ڈیٹا کی اقسام + پیٹرن کی مماثلت**: پیچیدہ ڈومینز کو ٹھیک ٹھیک ماڈل بنائیں؛ کمپائلر چیک کرتا ہے کہ آپ نے ہر معاملے کو سنبھالا۔
- **کارکردگی**: مقامی کوڈ پر مرتب کرتا ہے جو بہت سے معیارات میں C++ کا مقابلہ کرتا ہے۔
- **بذریعہ ڈیفالٹ **: قدریں ناقابل تغیر ہوتی ہیں جب تک کہ واضح طور پر دوسری صورت میں نشان زد نہ کیا جائے۔ کم کیڑے۔
- **ماڈیولز اور فنکٹرز**: بڑے سسٹمز کی تعمیر کے لیے طاقتور تجریدی میکانزم۔
- **رسمی طریقے**: تھیوریم پرورز (Coq)، ماڈل چیکنگ، اور تصدیق شدہ سافٹ ویئر میں استعمال کیا جاتا ہے۔
- **کمپیلر کنسٹرکشن**: کمپائلرز، ترجمانوں، اور زبان کے اوزار بنانے کے لیے بہترین۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **کھڑا سیکھنے کا وکر** | فنکشنل پروگرامنگ، ٹائپ سسٹم، اور نحو ناواقف ہیں | پیٹرن میچنگ اور ADTs کے ساتھ شروع کریں؛ آہستہ آہستہ تعمیر |
| **چھوٹی نوکری کی منڈی** | طاق - بنیادی طور پر فنانس (جین اسٹریٹ) اور تحقیق | ٹائپ سیف سسٹمز میں بڑھتی ہوئی دلچسپی |
| **محدود ویب ماحولیاتی نظام** | مرکزی دھارے کی ویب زبان نہیں ہے | ویب ڈویلپمنٹ کے لیے ReScript (OCaml-to-JS) استعمال کریں۔
| **خرابی کے پیغامات** | قسم کی غلطیاں خفیہ ہو سکتی ہیں، خاص طور پر پیچیدہ اقسام کے ساتھ | مرلن IDE پلگ ان استعمال کریں۔ ٹائپ دستخط پڑھنا سیکھیں |
| **ہم آہنگی** | کوئی بلٹ ان async/انتظار یا سبز دھاگوں | Lwt یا Async لائبریریوں کا استعمال کریں؛ OCaml 5 نے ملٹی کور سپورٹ شامل کیا |
| **دستاویزات** | ازگر یا زنگ ماحولیاتی نظام سے کم ابتدائی دوست | حقیقی دنیا OCaml (کتاب) بہترین ہے |
---

## نحوی بنیادی باتیں
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

## OCaml کا ٹائپ سسٹم ان ایکشن
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

## اعلی درجے کی نحو اور نمونے۔
### ماڈیول کے دستخط اور فنیکٹر
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

### فرسٹ کلاس ماڈیولز
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

### ایڈوانس پیٹرن میچنگ
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

### پولیمورفک متغیرات
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

## ہم آہنگی اور ہم آہنگی
### OCaml 5 ملٹی کور (ڈومینز)
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

### Lwt - کوآپریٹو کنکرنسی
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ (ٹیلا)
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

### ڈیون بلڈ کنفیگریشن
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

### کلیدی بلڈ کمانڈز
| کمانڈ | تفصیل |
|---------|---------------|
| `dune init project my_app`| نیا پروجیکٹ بنائیں |
| `dune build`| منصوبے کی تعمیر |
| `dune exec ./bin/main.exe`| قابل عمل چلائیں |
| `dune test`| ٹیسٹ چلائیں |
| `dune clean`| تعمیراتی نمونے صاف کریں |
| `dune utop`| بھری ہوئی پروجیکٹ کے ساتھ REPL شروع کریں |
| `opam install . --deps-only`| انحصار انسٹال کریں |
| `dune build @fmt`| فارمیٹ کوڈ |
| `opam switch create 5.1`| OCaml 5.1 سوئچ بنائیں |
---

## ٹیسٹنگ
### Alcotest — ہلکے وزن کی جانچ
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

### QCheck — پراپرٹی پر مبنی جانچ
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

## انٹرآپریبلٹی
### C غیر ملکی فنکشن انٹرفیس
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

## ڈیزائن پیٹرن
### OCaml میں ٹیگ لیس فائنل
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

### رزلٹ کے ساتھ ہینڈلنگ کی خرابی۔
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
| ٹول | مقصد | استعمال |
|------|---------|------|
| **ocamlprof** | پھانسی کی گنتی کی پروفائلنگ | `ocamlc -p`پھر`ocamlprof`|
| **perf** | لینکس سسٹم پروفائلر | `perf record ./program`|
| **اسپیس ٹائم** | میموری پروفائلنگ (4.x) | `OCAML_SPACETIME_INTERVAL=1000 ./program`|
| ** بینچ مارک** | مائیکرو بینچ مارکنگ | `ocaml-benchmark`پیکیج |
### اصلاح کی تکنیک
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

## تعیناتی۔
### مقامی بائنریز بنانا
```bash
# Build with dune
dune build @install
dune build --force

# Create optimized native binary
dune build --release
# Output: _build/default/bin/main.exe
```

### ڈاکر کی تعیناتی۔
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

## OCaml کب استعمال کریں۔
| منظر نامہ | کیوں OCaml | بہتر متبادل |
|------------|------------|-------------------|
| مرتب / زبان کے اوزار | ASTs کے لیے بہترین، ٹائپ چیکنگ، کوڈ جنریشن | کارکردگی کے اہم اوزار کے لئے مورچا |
| مالیاتی نظام | جین اسٹریٹ نے اسے پیمانے پر ثابت کیا | C++, Java, Python |
| رسمی تصدیق | مضبوط قسم کا نظام، تھیوریم ثابت کر رہا ہے سپورٹ | Coq، Agda خالص ثبوتوں کے لیے |
| ڈومین ماڈلنگ | ADTs + پیٹرن مماثل ماڈل کے پیچیدہ قواعد واضح طور پر | ویب ڈومینز کے لیے ٹائپ اسکرپٹ |
| اعلی کارکردگی کمپیوٹنگ | مقامی کوڈ جنریشن | C, C++, Rust, Fortran |
| ویب ڈویلپمنٹ | ReScript/OCaml کے ساتھ ممکن ہے۔ TypeScript, Go, Python |
| ڈیٹا سائنس / ایم ایل | ماحولیاتی نظام نہیں | ازگر، آر |
| موبائل ایپس | مناسب نہیں | سوئفٹ، کوٹلن، ڈارٹ |
| عام مقصد کی ایپلی کیشنز | ممکن لیکن طاق | جاؤ، ازگر، مورچا |
---

## مصنوعی سوال و جواب
### Q1: OCaml کی قسم کا اندازہ کیسے کام کرتا ہے؟
**A:** OCaml کا Hindley-Milner قسم کا نظام تشریحات کے بغیر اقسام کا اندازہ لگاتا ہے:
```ocaml
let add x y = x + y        (* inferred: int -> int -> int *)
let map f lst = List.map f lst  (* inferred: ('a -> 'b) -> 'a list -> 'b list *)
let length lst = List.length lst (* inferred: 'a list -> int *)
```

### Q2: الجبری ڈیٹا کی اقسام کیا ہیں اور وہ طاقتور کیوں ہیں؟
**A:** ADTs مصنوعات کی اقسام (ریکارڈز) اور رقم کی اقسام (مختلف حالتوں) کو یکجا کرتے ہیں:
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

### Q3: ماڈیولز اور فنیکٹر کیسے کام کرتے ہیں؟
**A:** ماڈیولز کوڈ کو منظم کرتے ہیں؛ فنیکٹرز ماڈیولز سے ماڈیول تک افعال ہیں:
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

### Q4: OCaml کو کیا تیز کرتا ہے؟
**A:** OCaml موثر مقامی کوڈ پر مرتب کرتا ہے:
- ٹائپ ایریزر - کوئی رن ٹائم ٹائپ چیک نہیں۔
- ان باکس شدہ فلوٹس اور انٹیجرز
- پیٹرن میچنگ ٹیبل کودنے کے لیے مرتب کرتا ہے۔
- ٹیل کال کی اصلاح
- کوئی کوڑا اٹھانے والا توقف نہیں کرتا (بڑھتی ہوئی GC)
### Q5: OCaml دیگر ML-فیملی زبانوں سے کیسے موازنہ کرتا ہے؟
**A:** OCaml عملییت اور پاکیزگی کو متوازن کرتا ہے:
- بمقابلہ ہاسکل: OCaml میں لازمی خصوصیات، تغیر پذیر حالت، اور تیز تر تالیف ہے
- بمقابلہ F#: OCaml میں زیادہ پختہ ماڈیول سسٹم اور بہتر کراس پلیٹ فارم سپورٹ ہے۔
- بمقابلہ زنگ: OCaml کے پاس GC ہے (کوئی ملکیت نہیں)، لیکن زنگ بہتر FFI اور ماحولیاتی نظام رکھتا ہے
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ایک قسم کے محفوظ ترجمان کو نافذ کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
سادہ اظہار کی زبان کے لیے ایک ترجمان بنائیں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
تشخیص کے لیے تاثرات اور پیٹرن کے ملاپ کے لیے الجبری ڈیٹا کی اقسام کا استعمال کریں۔
**مرحلہ 3: نافذ کریں**```ocaml
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

**مرحلہ 4: توسیع کریں**
مزید مکمل زبان کے لیے`Let`,`If`,`Lambda`شامل کریں۔
### مسئلہ 2: Combinators کے ساتھ ایک سادہ پارسر بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
تجزیہ کار کمبینیٹرز کا استعمال کرتے ہوئے ریاضی کے تاثرات کو پارس کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
چھوٹے پارسر بنائیں اور انہیں کمپوز کریں۔
**مرحلہ 3: نافذ کریں**```ocaml
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

**مرحلہ 4: تحریر کریں**
`map`، `seq`، `alt`، اور`many`کے ساتھ تجزیہ کاروں کو مکمل اظہار کو پارس کرنے کے لیے جوڑیں۔
---

## خلاصہ
OCaml ایک ایسی زبان ہے جو آپ کو اپنے ڈیٹا کے بارے میں احتیاط سے سوچنے پر انعام دیتی ہے۔ اس کی الجبری ڈیٹا کی اقسام اور مکمل پیٹرن کی مماثلت آپ کو ہر معاملے پر غور کرنے پر مجبور کرتی ہے — مرتب کرنے والا ایک ڈیزائن پارٹنر بن جاتا ہے جو غلطیوں کے ہونے سے پہلے ہی پکڑ لیتا ہے۔ ٹائپ انفرنس کا مطلب ہے کہ آپ کو یہ حفاظتی فوائد ہر جگہ ٹائپ اینوٹیشن لکھے بغیر حاصل ہوتے ہیں۔ OCaml کا اثر Rust, F#, TypeScript اور Swift میں نظر آتا ہے - ان سبھی نے OCaml کے ٹائپ سسٹم سے آئیڈیاز لیے ہیں۔ اگرچہ OCaml کی جاب مارکیٹ چھوٹی ہے، لیکن اسے سیکھنا آپ کی پروگرامنگ کی مہارتوں کو ان طریقوں سے تیز کرے گا جو کسی بھی زبان میں منتقل ہوتے ہیں۔