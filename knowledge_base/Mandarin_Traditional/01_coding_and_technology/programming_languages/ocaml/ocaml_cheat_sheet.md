---
# Metadata
title: "OCaml — Cheat Sheet"
description: "Quick-reference cheat sheet for OCaml syntax, types, and functional patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [ocaml, functional, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# OCaml — 備忘單
## 基礎知識
```ocaml
(* Variables (immutable bindings) *)
let name = "Alice"
let age = 30
let pi = 3.14159
let active = true

(* Type annotations *)
let x : int = 42
let s : string = "hello"
let f : float = 3.14

(* String operations *)
String.length name          (* 5 *)
String.uppercase_ascii name (* "ALICE" *)
String.lowercase_ascii name
String.trim "  hi  "
String.contains name 'l'    (* true *)
String.sub name 0 3         (* "Ali" *)
name ^ " Smith"             (* concatenation *)
Printf.sprintf "Hello, %s!" name
int_of_string "42"
string_of_int 42
float_of_string "3.14"
```

## 類型和模式匹配
```ocaml
(* Algebraic types *)
type color = Red | Green | Blue
type shape =
  | Circle of float
  | Rectangle of float * float
  | Point

(* Pattern matching *)
let area = function
  | Circle r -> Float.pi *. r *. r
  | Rectangle (w, h) -> w *. h
  | Point -> 0.0

(* Option type *)
let find_user id =
  if id > 0 then Some "Alice" else None

match find_user 1 with
| Some name -> Printf.printf "Found: %s\n" name
| None -> print_endline "Not found"

(* Result type *)
let divide a b =
  if b = 0 then Error "division by zero"
  else Ok (a / b)

(* Records *)
type point = { x : float; y : float }
let p = { x = 1.0; y = 2.0 }
let { x; y } = p            (* destructuring *)
let p2 = { p with y = 3.0 } (* functional update *)

(* Tuples *)
let pair = (1, "hello")
let (x, s) = pair
```

## 清單和集合
```ocaml
(* Lists (immutable, linked) *)
let lst = [1; 2; 3; 4; 5]
let lst2 = 0 :: lst          (* prepend *)
let lst3 = lst @ [6; 7]      (* append *)
List.hd lst                   (* 1 *)
List.tl lst                   (* [2;3;4;5] *)
List.length lst               (* 5 *)
List.nth lst 2                (* 3 *)
List.rev lst                  (* reversed *)

(* List operations *)
List.map (fun x -> x * 2) lst
List.filter (fun x -> x > 2) lst
List.fold_left (+) 0 lst
List.fold_right (fun x acc -> x :: acc) lst []
List.iter (Printf.printf "%d ") lst
List.mem 3 lst                (* true *)
List.sort compare lst
List.exists (fun x -> x > 3) lst
List.for_all (fun x -> x > 0) lst

(* Arrays (mutable) *)
let arr = [| 1; 2; 3 |]
arr.(0)                       (* 1 *)
arr.(0) <- 99                 (* mutate *)
Array.length arr
Array.map (fun x -> x * 2) arr
Array.to_list arr
Array.of_list [1; 2; 3]

(* Hashtbl (mutable hash map) *)
let tbl = Hashtbl.create 10
Hashtbl.add tbl "alice" 90
Hashtbl.find tbl "alice"      (* 90 *)
Hashtbl.mem tbl "bob"         (* false *)

(* Map (immutable, ordered) *)
module StringMap = Map.Make(String)
let m = StringMap.empty
let m = StringMap.add "alice" 90 m
let m = StringMap.add "bob" 85 m
StringMap.find "alice" m      (* 90 *)
```

## 函數
```ocaml
(* Basic function *)
let add a b = a + b
let add (a : int) (b : int) : int = a + b

(* Anonymous function *)
let square = fun x -> x * x
List.map (fun x -> x * x) [1; 2; 3]

(* Partial application *)
let add5 = add 5
add5 3                        (* 8 *)

(* Pipe operator *)
let result =
  [1; 2; 3; 4; 5]
  |> List.filter (fun x -> x > 2)
  |> List.map (fun x -> x * x)
  |> List.fold_left (+) 0

(* Recursive *)
let rec factorial n =
  if n <= 1 then 1
  else n * factorial (n - 1)

(* Tail-recursive *)
let factorial n =
  let rec aux n acc =
    if n <= 1 then acc
    else aux (n - 1) (acc * n)
  in aux n 1

(* Labeled arguments *)
let greet ~name ~greeting =
  Printf.sprintf "%s, %s!" greeting name
greet ~name:"Alice" ~greeting:"Hello"

(* Optional arguments *)
let greet ?(greeting = "Hello") name =
  Printf.sprintf "%s, %s!" greeting name
```

## 模組
```ocaml
(* Module definition *)
module Stack = struct
  type 'a t = 'a list
  let empty = []
  let push x s = x :: s
  let pop = function
    | [] -> None
    | x :: xs -> Some (x, xs)
  let is_empty s = s = empty
end

(* Module type (signature) *)
module type PRINTABLE = sig
  type t
  val to_string : t -> string
end

(* Functor *)
module MakeSet (Elem : Map.OrderedType) = struct
  module M = Set.Make(Elem)
  include M
end

(* Open module *)
open List
map (fun x -> x * 2) [1; 2; 3]
```

## 錯誤處理
```ocaml
(* Exceptions *)
exception Not_found_custom of string
exception Invalid_input of string * int

let () =
  try
    let result = risky_operation () in
    Printf.printf "Result: %d\n" result
  with
  | Not_found_custom msg ->
    Printf.printf "Not found: %s\n" msg
  | Invalid_input (name, code) ->
    Printf.printf "Invalid %s: %d\n" name code
  | exn ->
    Printf.printf "Unknown: %s\n" (Printexc.to_string exn)

(* Option idiom (preferred) *)
let safe_divide a b =
  if b = 0 then None else Some (a / b)

(* Result idiom *)
let parse_input s =
  match int_of_string_opt s with
  | Some n when n > 0 -> Ok n
  | Some _ -> Error "must be positive"
  | None -> Error "not a number"
```
