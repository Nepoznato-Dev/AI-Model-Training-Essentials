---
# البيانات الوصفية
العنوان: "أوكامل"
الوصف: "مرجع شامل للغة برمجة OCaml يغطي النظرة العامة والمقايضات وأساسيات بناء الجملة والنظام البيئي ومتى يتم استخدامها."
الفئة: "البرمجة والتكنولوجيا"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
تمت المراجعة بواسطة: "فريق قاعدة معارف البرمجة والتكنولوجيا"
next_review: "2027-08-05"
# التصنيف
العلامات: [ocaml، لغة البرمجة، بناء الجملة، النظام البيئي، الترميز والتكنولوجيا]
مستوى الصعوبة: "متقدم"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "29 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
#أوكامل
OCaml (Objective Caml) هي لغة برمجة وظيفية تم تطويرها في INRIA في فرنسا، وتم إصدارها لأول مرة في عام 1996. وهي تجمع بين تعبير البرمجة الوظيفية والميزات العملية: نظام كتابة قوي مع استنتاج النوع (Hindley-Milner)، ومطابقة الأنماط، وأنواع البيانات الجبرية، والبرمجة الاختيارية الموجهة للكائنات. يقوم OCaml بتجميع التعليمات البرمجية الأصلية السريعة ويدعم أيضًا الرمز الثانوي.
أشهر تطبيق OCaml في العالم الحقيقي هو شركة **Jane Street** التجارية، والتي تستخدم OCaml في بنيتها التحتية التجارية بالكامل. كما أنه يستخدم أيضًا في تطوير المترجم (تم كتابة مترجم Rust في الأصل بلغة OCaml)، والتحقق الرسمي، والأنظمة المالية، وإثبات النظرية.
يقدم الأخ الجديد لـ OCaml **Reason** (الذي تم تطويره بواسطة Facebook/Meta) و**ReScript** (BuckleScript سابقًا) نظام كتابة OCaml وأدائه لتطوير الويب، وتجميعه إلى JavaScript.
---

## لماذا يهم OCaml
- **استدلال النوع**: يكتشف المترجم الأنواع تلقائيًا — لا حاجة إلى تعليقات توضيحية لمعظم التعليمات البرمجية.
- **أنواع البيانات الجبرية + مطابقة الأنماط**: نموذج المجالات المعقدة بدقة؛ يتحقق المترجم من تعاملك مع كل حالة.
- **الأداء**: يتم تجميعه إلى تعليمات برمجية أصلية تنافس لغة C++‎ في العديد من المعايير.
- **الثبات افتراضيًا**: القيم غير قابلة للتغيير ما لم يتم تحديد خلاف ذلك صراحةً. أخطاء أقل.
- **الوحدات والوظائف**: آليات تجريد قوية لبناء أنظمة كبيرة.
- **الطرق الرسمية**: تستخدم في مثبتات النظرية (Coq)، وفحص النماذج، والبرمجيات التي تم التحقق منها.
- **إنشاء المترجم**: ممتاز لبناء المترجمين والمترجمين الفوريين وأدوات اللغة.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| ** منحنى التعلم الحاد ** | البرمجة الوظيفية ونظام الكتابة وبناء الجملة غير مألوفة | ابدأ بمطابقة الأنماط وأدوات ADT؛ بناء تدريجيا |
| **سوق العمل الصغير** | المتخصصة - في المقام الأول التمويل (جين ستريت) والبحث | الاهتمام المتزايد بالأنظمة الآمنة من النوع |
| **نظام بيئي محدود على الويب** | ليست لغة ويب سائدة | استخدم ReScript (OCaml-to-JS) لتطوير الويب |
| **رسائل الخطأ** | يمكن أن تكون أخطاء الكتابة غامضة، خاصة مع الأنواع المعقدة | استخدم البرنامج المساعد Merlin IDE؛ تعلم قراءة نوع التوقيعات |
| **التزامن** | لا يوجد مزامنة/انتظار أو خيوط خضراء مدمجة | استخدم مكتبات Lwt أو Async؛ أضاف OCaml 5 دعمًا متعدد النواة |
| **التوثيق** | أقل ملاءمة للمبتدئين من الأنظمة البيئية Python أو Rust | العالم الحقيقي OCaml (كتاب) ممتاز |
---

## أساسيات بناء الجملة
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

## نظام الكتابة الخاص بـ OCaml قيد التنفيذ
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

## بناء الجملة والأنماط المتقدمة
### تواقيع الوحدة والوظائف
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

### وحدات من الدرجة الأولى
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

### مطابقة الأنماط المتقدمة
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

### متغيرات متعددة الأشكال
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

## التزامن والتوازي
### OCaml 5 متعدد النواة (المجالات)
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

### Lwt — التزامن التعاوني
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

## تكوين المشروع ونظام البناء
### هيكل المشروع (الكثيب)
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

### تكوين بناء الكثيب
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

### أوامر بناء المفاتيح
| الأمر | الوصف |
|---------|------------|
|  __محمي_0__ | إنشاء مشروع جديد |
|  __محمي_1__ | بناء المشروع |
|  __محمي_2__ | قم بتشغيل الملف القابل للتنفيذ |
|  __محمي_3__ | تشغيل الاختبارات |
|  __محمي_4__ | التحف البناء النظيف |
|  __محمي_5__ | ابدأ REPL مع تحميل المشروع |
|  __محمي_6__ | تثبيت التبعيات |
|  __محمي_7__ | رمز التنسيق |
|  __محمي_8__ | إنشاء محول OCaml 5.1 |
---

## الاختبار
### Alcotest — اختبار الوزن الخفيف
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

### QCheck — الاختبار المبني على الخاصية
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

## إمكانية التشغيل البيني
### واجهة الوظائف الأجنبية C
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

## أنماط التصميم
### نهائي بدون علامات في OCaml
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

### معالجة الأخطاء بالنتيجة
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

## الأداء والتحسين
### أدوات التنميط
| أداة | الغرض | الاستخدام |
|------|---------|------|
| **أوكاملبروف** | عدد التنفيذ التنميط |  __محمي_0__ ثم __محمي_1__ |
| **الأداء** | ملف تعريف نظام Linux |  __محمي_2__ |
| **الزمكان** | ملفات تعريف الذاكرة (4.x) |  __محمي_3__ |
| **المعيار** | القياس الجزئي |  __محمي_4__ الحزمة |
### تقنيات التحسين
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

## النشر
### بناء الثنائيات الأصلية
```bash
# Build with dune
dune build @install
dune build --force

# Create optimized native binary
dune build --release
# Output: _build/default/bin/main.exe
```

### نشر عامل الميناء
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

## متى يجب استخدام OCaml
| السيناريو | لماذا أوكامل | البديل الأفضل |
|----------|-------------------------|---|
| مترجم / أدوات اللغة | ممتاز لـ ASTs، وفحص النوع، وإنشاء التعليمات البرمجية | الصدأ للأدوات ذات الأداء الحيوي |
| الأنظمة المالية | أثبتت جين ستريت ذلك على نطاق واسع | C++، جافا، بايثون |
| التحقق الرسمي | نظام نوع قوي، نظرية تثبت الدعم | كوك، أجدا للبراهين الصرفة |
| نمذجة المجال | ADTs + نموذج مطابقة القواعد المعقدة بدقة | TypeScript لمجالات الويب |
| حوسبة عالية الأداء | توليد الكود الأصلي | C، C++، الصدأ، فورتران |
| تطوير الويب | ممكن مع ReScript/OCaml | تايب سكريبت، اذهب، بايثون |
| علم البيانات / تعلم الآلة | ليس النظام البيئي | بايثون، ر |
| تطبيقات الجوال | غير مناسب | سويفت، كوتلين، دارت |
| تطبيقات للأغراض العامة | ممكن ولكن المتخصصة | اذهب، بايثون، روست |
---

## ملخص
OCaml هي لغة تكافئك على التفكير بعناية في بياناتك. تجبرك أنواع البيانات الجبرية ومطابقة الأنماط الشاملة على النظر في كل حالة - ويصبح المترجم شريكًا في التصميم يكتشف الأخطاء قبل حدوثها. يعني استنتاج النوع أنك تحصل على مزايا الأمان هذه دون كتابة التعليقات التوضيحية للنوع في كل مكان. يظهر تأثير OCaml في Rust وF# وTypeScript وSwift، وجميعها مستعارة من نظام الكتابة الخاص بـ OCaml. على الرغم من أن سوق العمل في OCaml صغير، إلا أن تعلمه سيصقل مهاراتك في البرمجة بطرق يمكن نقلها إلى أي لغة.