---
# Metadata
title: "OCaml — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in OCaml with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [ocaml, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# OCaml - Makosa ya Kawaida & Miundo ya Kupambana
Hati hii inaorodhesha makosa ya kawaida, mitego, na mifumo ya kupingana katika OCaml na masahihisho.
---

## 1. Ulinganishaji wa Miundo Isiyo Kamili
```ocaml
(* ❌ WRONG — missing cases *)
let get_name = function
  | Circle r -> Printf.sprintf "Circle(%f)" r
  (* forgot Rectangle, Triangle — Warning 8! *)

(* ✅ CORRECT — exhaustive matching *)
let get_name = function
  | Circle r -> Printf.sprintf "Circle(%f)" r
  | Rectangle (w, h) -> Printf.sprintf "Rect(%f,%f)" w h
  | Triangle (a, b, c) -> Printf.sprintf "Tri(%f,%f,%f)" a b c
```

---

## 2.`=`vs `==`
```ocaml
(* ❌ WRONG — structural vs physical equality *)
"hello" == "hello"  (* false — different memory locations *)
[1;2] == [1;2]      (* false — different lists *)

(* ✅ CORRECT — use = for structural equality *)
"hello" = "hello"   (* true — same content *)
[1;2] = [1;2]       (* true — same content *)
```

---

## 3. Mgawanyiko Nambari
```ocaml
(* ❌ WRONG — integer division truncates *)
1 / 2   (* 0, not 0.5 *)
7 / 3   (* 2, not 2.333 *)

(* ✅ CORRECT — use float division *)
1.0 /. 2.0  (* 0.5 *)
7.0 /. 3.0  (* 2.333... *)
```

---

## 4. Kutotumia`Option`Vizuri
```ocaml
(* ❌ WRONG — using exceptions for control flow *)
let find lst key =
  try List.assoc key lst
  with Not_found -> -1

(* ✅ CORRECT — use Option *)
let find lst key =
  List.assoc_opt key lst
(* Returns 'a option — None if not found *)
```

---

## 5. Hali Inayoweza Kubadilika katika Shughuli za Kujirudia
```ocaml
(* ❌ WRONG — using ref for accumulation *)
let sum lst =
  let acc = ref 0 in
  List.iter (fun x -> acc := !acc + x) lst;
  !acc

(* ✅ CORRECT — use tail recursion *)
let sum lst =
  let rec aux acc = function
    | [] -> acc
    | h :: t -> aux (acc + h) t
  in aux 0 lst

(* ✅ CORRECT — use List.fold_left *)
let sum = List.fold_left (+) 0
```

---

## Muhtasari
Mitego ya OCaml: ulinganishaji wa muundo usio kamili (mkusanyaji anaonya),`=`ni usawa wa muundo wakati`==`ni ya kimwili, yenye mgawanyiko kamili, tumia`Option`badala ya vighairi, na epuka hali inayoweza kubadilika ikipendelea kujirudia kwa mkia na kukunjwa. Mkusanyaji wa OCaml ni mshirika wako - zingatia maonyo yake.