<!--
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

-->
#ओकैमल
OCaml (ऑब्जेक्टिव कैमल) फ्रांस में INRIA में विकसित एक कार्यात्मक प्रोग्रामिंग भाषा है, जिसे पहली बार 1996 में जारी किया गया था। यह व्यावहारिक विशेषताओं के साथ कार्यात्मक प्रोग्रामिंग की अभिव्यक्ति को जोड़ती है: प्रकार अनुमान (हिंडले-मिलनर), पैटर्न मिलान, बीजगणितीय डेटा प्रकार और वैकल्पिक ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग के साथ एक शक्तिशाली प्रकार की प्रणाली। OCaml तेज़ देशी कोड को संकलित करता है और बाइटकोड का भी समर्थन करता है।
OCaml का सबसे प्रसिद्ध वास्तविक दुनिया एप्लिकेशन **जेन स्ट्रीट** ट्रेडिंग फर्म है, जो अपने संपूर्ण ट्रेडिंग इंफ्रास्ट्रक्चर के लिए OCaml का उपयोग करता है। इसका उपयोग कंपाइलर विकास (रस्ट कंपाइलर मूल रूप से OCaml में लिखा गया था), औपचारिक सत्यापन, वित्तीय प्रणाली और प्रमेय सिद्ध करने में भी किया जाता है।
OCaml का नया भाई **Reason** (Facebook/Meta द्वारा विकसित) और **ReScript** (पूर्व में BuckleScript) OCaml के टाइप सिस्टम और प्रदर्शन को जावास्क्रिप्ट में संकलित करके वेब विकास में लाता है।
---

## OCaml क्यों मायने रखता है
- **प्रकार का अनुमान**: कंपाइलर स्वचालित रूप से प्रकारों का पता लगाता है - अधिकांश कोड के लिए किसी एनोटेशन की आवश्यकता नहीं होती है।
- **बीजगणितीय डेटा प्रकार + पैटर्न मिलान**: जटिल डोमेन को सटीक रूप से मॉडल करें; कंपाइलर जाँचता है कि आपने हर मामले को संभाला है।
- **प्रदर्शन**: मूल कोड को संकलित करता है जो कई बेंचमार्क में C++ को टक्कर देता है।
- **डिफ़ॉल्ट रूप से अपरिवर्तनीयता**: मान अपरिवर्तनीय हैं जब तक कि स्पष्ट रूप से अन्यथा चिह्नित न किया गया हो। कम बग.
- **मॉड्यूल और फ़ैक्टर**: बड़े सिस्टम के निर्माण के लिए शक्तिशाली अमूर्त तंत्र।
- **औपचारिक तरीके**: प्रमेय कहावत (सीओक्यू), मॉडल जांच और सत्यापित सॉफ़्टवेयर में उपयोग किया जाता है।
- **कंपाइलर निर्माण**: कंपाइलर, दुभाषिए और भाषा उपकरण बनाने के लिए उत्कृष्ट।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **सीखने की तीव्र अवस्था** | कार्यात्मक प्रोग्रामिंग, प्रकार प्रणाली और वाक्यविन्यास अपरिचित हैं | पैटर्न मिलान और एडीटी से प्रारंभ करें; धीरे-धीरे निर्माण करें |
| **लघु नौकरी बाज़ार** | आला - मुख्य रूप से वित्त (जेन स्ट्रीट) और अनुसंधान | टाइप-सुरक्षित प्रणालियों में बढ़ती रुचि |
| **सीमित वेब पारिस्थितिकी तंत्र** | मुख्यधारा की वेब भाषा नहीं | वेब विकास के लिए रीस्क्रिप्ट (OCaml-to-JS) का उपयोग करें |
| **त्रुटि संदेश** | प्रकार की त्रुटियाँ रहस्यमय हो सकती हैं, विशेष रूप से जटिल प्रकारों के साथ | मर्लिन आईडीई प्लगइन का उपयोग करें; टाइप हस्ताक्षर पढ़ना सीखें |
| **संगामिति** | कोई अंतर्निहित एसिंक/प्रतीक्षा या हरे धागे नहीं | Lwt या Async लाइब्रेरीज़ का उपयोग करें; OCaml 5 ने मल्टीकोर सपोर्ट जोड़ा |
| **दस्तावेज़ीकरण** | पायथन या रस्ट इकोसिस्टम की तुलना में कम शुरुआती-अनुकूल | रियल वर्ल्ड OCaml (पुस्तक) उत्कृष्ट है |
---

## सिंटेक्स बुनियादी बातें
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

## OCaml का टाइप सिस्टम क्रियान्वित
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

## उन्नत सिंटैक्स और पैटर्न
### मॉड्यूल हस्ताक्षर और फ़ैक्टर
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

### प्रथम श्रेणी के मॉड्यूल
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

### उन्नत पैटर्न मिलान
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

### बहुरूपी वेरिएंट
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

## समवर्ती एवं समांतरता
### OCaml 5 मल्टीकोर (डोमेन)
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

### Lwt - सहकारी समवर्ती
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना (ड्यून)
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

### ड्यून बिल्ड कॉन्फ़िगरेशन
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

### कुंजी निर्माण आदेश
| आदेश | विवरण |
|---------|-----------------|
| `dune init project my_app`| नया प्रोजेक्ट बनाएं |
| `dune build`| प्रोजेक्ट बनाएं |
| `dune exec ./bin/main.exe`| निष्पादन योग्य चलाएँ |
| `dune test`| परीक्षण चलाएँ |
| `dune clean`| स्वच्छ निर्मित कलाकृतियाँ |
| `dune utop`| लोड किए गए प्रोजेक्ट के साथ आरईपीएल प्रारंभ करें |
| `opam install . --deps-only`| निर्भरताएँ स्थापित करें |
| `dune build @fmt`| प्रारूप कोड |
| `opam switch create 5.1`| OCaml 5.1 स्विच बनाएं |
---

## परीक्षण
### अल्कोटेस्ट - हल्का परीक्षण
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

### क्यूचेक - संपत्ति-आधारित परीक्षण
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

## अंतरसंचालनीयता
### सी विदेशी फ़ंक्शन इंटरफ़ेस
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

### जावास्क्रिप्ट इंटरऑप (js_of_ocaml / ReScript)
```ocaml
(* js_of_ocaml — compile OCaml to JavaScript *)
(* Access browser APIs *)
let () =
  let doc = Dom_html.document in
  let elem = Dom_html.getElementById_exn "app" in
  elem##.innerHTML := Js.string "Hello from OCaml!"
```

---

## डिज़ाइन पैटर्न
### OCaml में टैग रहित फ़ाइनल
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

### परिणाम के साथ त्रुटि प्रबंधन
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
| उपकरण | उद्देश्य | उपयोग |
|------|------|-------|
| **ocamlprof** | निष्पादन गिनती प्रोफाइलिंग | `ocamlc -p`फिर`ocamlprof`|
| **परफ** | लिनक्स सिस्टम प्रोफाइलर | `perf record ./program`|
| **स्पेसटाइम** | मेमोरी प्रोफाइलिंग (4.x) | `OCAML_SPACETIME_INTERVAL=1000 ./program`|
| **बेंचमार्क** | माइक्रो-बेंचमार्किंग | `ocaml-benchmark`पैकेज |
### अनुकूलन तकनीकें
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

## तैनाती
### नेटिव बायनेरिज़ का निर्माण
```bash
# Build with dune
dune build @install
dune build --force

# Create optimized native binary
dune build --release
# Output: _build/default/bin/main.exe
```

### डॉकर परिनियोजन
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

## OCaml का उपयोग कब करें
| परिदृश्य | ओकैमल क्यों | बेहतर विकल्प |
|---|---|-----|
| संकलक/भाषा उपकरण | एएसटी, टाइप चेकिंग, कोड जेनरेशन के लिए उत्कृष्ट | प्रदर्शन-महत्वपूर्ण उपकरणों के लिए जंग |
| वित्तीय प्रणालियाँ | जेन स्ट्रीट ने इसे बड़े पैमाने पर साबित किया | सी++, जावा, पायथन |
| औपचारिक सत्यापन | मजबूत प्रकार की प्रणाली, प्रमेय सिद्ध समर्थन | शुद्ध प्रमाण के लिए कॉक, अगडा |
| डोमेन मॉडलिंग | एडीटी + पैटर्न मिलान मॉडल जटिल नियम सटीक रूप से | वेब डोमेन के लिए टाइपस्क्रिप्ट |
| उच्च-प्रदर्शन कंप्यूटिंग | मूल कोड जनरेशन | सी, सी++, रस्ट, फोरट्रान |
| वेब विकास | रीस्क्रिप्ट/OCaml के साथ संभव | टाइपस्क्रिप्ट, गो, पायथन |
| डेटा साइंस/एमएल | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
| मोबाइल ऐप्स | अनुकूल नहीं | स्विफ्ट, कोटलिन, डार्ट |
| सामान्य प्रयोजन अनुप्रयोग | संभव लेकिन आला | जाओ, अजगर, जंग |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: OCaml का प्रकार अनुमान कैसे काम करता है?
**ए:** ओकैमल का हिंडले-मिलनर प्रकार का सिस्टम एनोटेशन के बिना प्रकार का अनुमान लगाता है:
```ocaml
let add x y = x + y        (* inferred: int -> int -> int *)
let map f lst = List.map f lst  (* inferred: ('a -> 'b) -> 'a list -> 'b list *)
let length lst = List.length lst (* inferred: 'a list -> int *)
```

### Q2: बीजगणितीय डेटा प्रकार क्या हैं और वे शक्तिशाली क्यों हैं?
**ए:** एडीटी उत्पाद प्रकार (रिकॉर्ड) और योग प्रकार (वेरिएंट) को जोड़ते हैं:
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

### Q3: मॉड्यूल और फ़ैक्टर कैसे काम करते हैं?
**ए:** मॉड्यूल कोड व्यवस्थित करते हैं; फ़ैक्टर मॉड्यूल से मॉड्यूल तक के फ़ंक्शन हैं:
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

### Q4: OCaml को तेज़ क्या बनाता है?
**ए:** OCaml कुशल देशी कोड को संकलित करता है:
- प्रकार मिटाना - कोई रनटाइम प्रकार की जाँच नहीं
- अनबॉक्स्ड फ़्लोट्स और पूर्णांक
- पैटर्न मिलान तालिकाओं को जंप करने के लिए संकलित करता है
- टेल-कॉल अनुकूलन
- कोई कचरा संग्रहकर्ता रुकता नहीं (वृद्धिशील जीसी)
### Q5: OCaml की तुलना अन्य ML-पारिवारिक भाषाओं से कैसे की जाती है?
**ए:** ओकैमल व्यावहारिकता और शुद्धता को संतुलित करता है:
- बनाम हास्केल: OCaml में अनिवार्य विशेषताएं, परिवर्तनशील स्थिति और तेज़ संकलन है
- बनाम F#: OCaml में अधिक परिपक्व मॉड्यूल प्रणाली और बेहतर क्रॉस-प्लेटफ़ॉर्म समर्थन है
- बनाम रस्ट: OCaml के पास GC (कोई स्वामित्व नहीं) है, लेकिन रस्ट के पास बेहतर FFI और पारिस्थितिकी तंत्र है
---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक प्रकार-सुरक्षित दुभाषिया लागू करना
**चरण 1: समस्या को समझें**
सरल अभिव्यक्ति भाषा के लिए एक दुभाषिया बनाएँ।
**चरण 2: दृष्टिकोण को पहचानें**
मूल्यांकन के लिए अभिव्यक्ति और पैटर्न मिलान के लिए बीजगणितीय डेटा प्रकारों का उपयोग करें।
**चरण 3: कार्यान्वयन**```ocaml
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

**चरण 4: विस्तार करें**
अधिक संपूर्ण भाषा के लिए`Let`,`If`,`Lambda`जोड़ें।
### समस्या 2: कॉम्बिनेटर के साथ एक सरल पार्सर बनाना
**चरण 1: समस्या को समझें**
पार्सर कॉम्बिनेटर का उपयोग करके अंकगणितीय अभिव्यक्तियों को पार्स करें।
**चरण 2: दृष्टिकोण को पहचानें**
छोटे पार्सर बनाएं और उन्हें लिखें।
**चरण 3: कार्यान्वयन**```ocaml
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

**चरण 4: लिखें**
पूर्ण अभिव्यक्तियों को पार्स करने के लिए पार्सर्स को`map`,`seq`,`alt`, और`many`के साथ संयोजित करें।
---

## सारांश
OCaml एक ऐसी भाषा है जो आपके डेटा के बारे में सावधानी से सोचने के लिए आपको पुरस्कृत करती है। इसके बीजगणितीय डेटा प्रकार और विस्तृत पैटर्न मिलान आपको हर मामले पर विचार करने के लिए मजबूर करता है - कंपाइलर एक डिज़ाइन भागीदार बन जाता है जो गलतियों को होने से पहले ही पकड़ लेता है। प्रकार अनुमान का अर्थ है कि आपको हर जगह प्रकार की टिप्पणियाँ लिखे बिना ये सुरक्षा लाभ मिलते हैं। OCaml का प्रभाव रस्ट, F#, टाइपस्क्रिप्ट और स्विफ्ट में दिखाई देता है - इन सभी ने OCaml के टाइप सिस्टम से विचार उधार लिए हैं। जबकि OCaml का जॉब मार्केट छोटा है, इसे सीखने से आपके प्रोग्रामिंग कौशल को किसी भी भाषा में स्थानांतरित करने के तरीके में निखार आएगा।