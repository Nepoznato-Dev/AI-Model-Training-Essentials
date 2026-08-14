<!--
---
# Metadata
title: "OCaml — Syntax Reference"
description: "Detailed syntax reference for OCaml covering algebraic data types, pattern matching, modules, functors, and functional programming patterns."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [ocaml, syntax-reference, algebraic-data-types, pattern-matching, modules, functors, functional, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# OCaml — 语法参考
本文档为 OCaml (4.x/5.x) 提供全面、结构化的语法参考。它通过关注详尽的语法模式、代数数据类型、模式匹配、模块和函数式编程习惯来补充主要的 OCaml 参考。
---

## 核心语法
```ocaml
(* Bindings *)
let x = 42
let name = "Alice"
let pi = 3.14159

(* Functions *)
let add x y = x + y
let square x = x * x
let greet name = Printf.sprintf "Hello, %s!" name

(* Anonymous functions *)
let double = fun x -> x * 2
List.map (fun x -> x + 1) [1; 2; 3]

(* Recursive *)
let rec factorial n =
  if n <= 1 then 1
  else n * factorial (n - 1)

(* Tail-recursive *)
let factorial n =
  let rec aux n acc =
    if n <= 1 then acc
    else aux (n - 1) (n * acc)
  in aux n 1
```

---

## 类型和模式匹配
```ocaml
(* Algebraic data types *)
type color = Red | Green | Blue
type shape =
  | Circle of float
  | Rectangle of float * float
  | Triangle of float * float * float

(* Pattern matching — exhaustive! *)
let area = function
  | Circle r -> Float.pi *. r *. r
  | Rectangle (w, h) -> w *. h
  | Triangle (a, b, c) ->
      let s = (a +. b +. c) /. 2.0 in
      Float.sqrt (s *. (s -. a) *. (s -. b) *. (s -. c))

(* Option type *)
let safe_div x y =
  if y = 0.0 then None
  else Some (x /. y)

let result = match safe_div 10.0 3.0 with
  | Some v -> Printf.sprintf "Result: %f" v
  | None   -> "Division by zero"

(* Result type *)
let parse_int s =
  try Ok (int_of_string s)
  with _ -> Error "not a number"

(* Records *)
type person = {
  name : string;
  age : int;
  email : string;
}

let alice = { name = "Alice"; age = 30; email = "alice@example.com" }
let older = { alice with age = alice.age + 1 }

(* Tuples *)
let pair = (1, "hello")
let (x, y) = pair
```

---

## 列表和集合
```ocaml
(* Lists *)
let lst = [1; 2; 3; 4; 5]
let first = List.hd lst          (* 1 *)
let rest = List.tl lst           (* [2; 3; 4; 5] *)
let len = List.length lst        (* 5 *)

(* List operations *)
List.map (fun x -> x * 2) lst
List.filter (fun x -> x > 3) lst
List.fold_left (+) 0 lst
List.rev lst
List.sort compare lst
List.mem 3 lst                   (* true *)

(* Pattern matching on lists *)
let rec sum = function
  | [] -> 0
  | h :: t -> h + sum t

let rec last = function
  | [] -> failwith "empty"
  | [x] -> x
  | _ :: t -> last t

(* Hashtbl (mutable hash map) *)
let tbl = Hashtbl.create 16
Hashtbl.add tbl "key" "value"
Hashtbl.find tbl "key"

(* Map (immutable, ordered) *)
module StringMap = Map.Make(String)
let m = StringMap.empty
let m = StringMap.add "a" 1 m
let m = StringMap.add "b" 2 m
```

---

## 模块和函子
```ocaml
(* Module *)
module Stack = struct
  type 'a t = 'a list
  let empty = []
  let push x s = x :: s
  let pop = function
    | [] -> failwith "empty"
    | h :: t -> (h, t)
  let is_empty s = s = []
end

(* Module type (signature) *)
module type COMPARABLE = sig
  type t
  val compare : t -> t -> int
end

(* Functor — module-level function *)
module Set (Elem : COMPARABLE) = struct
  type elt = Elem.t
  type t = elt list
  let empty = []
  let mem x s = List.exists (fun y -> Elem.compare x y = 0) s
  let add x s = if mem x s then s else x :: s
  let of_list lst = List.fold_left (fun acc x -> add x acc) empty lst
end

(* Using the functor *)
module IntSet = Set(struct
  type t = int
  let compare = Int.compare
end)
```

---

## 错误处理和影响
```ocaml
(* Exceptions *)
exception Not_found of string
exception Invalid_input of string * int

let find_user id =
  if id > 0 then User(id)
  else raise (Invalid_input ("user", id))

(* try/with *)
let safe_find id =
  try find_user id
  with Invalid_input (msg, id) ->
    Printf.printf "Error: %s %d\n" msg id;
    None

(* Result monad *)
let (>>=) r f = match r with
  | Ok v -> f v
  | Error e -> Error e

let process id =
  find_user id >>= fun user ->
  validate_email user >>= fun email ->
  Ok (user, email)
```

---

＃＃ 概括
OCaml 的语法简洁且数学化。代数数据类型和详尽的模式匹配使得不可能的状态无法表示。具有函子的模块系统提供了强大的抽象，而无需运行时成本。类型推断意味着安全而不冗长。 OCaml 对 Rust、F#、TypeScript 和 Swift 的影响是不可否认的。对于系统编程、编译器和形式验证，OCaml 仍然是首选。