<!--
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

-->
# OCaml: errores comunes y antipatrones
Este documento cataloga los errores, trampas y antipatrones más comunes en OCaml con correcciones.
---

## 1. Coincidencia de patrones no exhaustiva
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

## 2.`=`frente a `==`
```ocaml
(* ❌ WRONG — structural vs physical equality *)
"hello" == "hello"  (* false — different memory locations *)
[1;2] == [1;2]      (* false — different lists *)

(* ✅ CORRECT — use = for structural equality *)
"hello" = "hello"   (* true — same content *)
[1;2] = [1;2]       (* true — same content *)
```

---

## 3. División entera
```ocaml
(* ❌ WRONG — integer division truncates *)
1 / 2   (* 0, not 0.5 *)
7 / 3   (* 2, not 2.333 *)

(* ✅ CORRECT — use float division *)
1.0 /. 2.0  (* 0.5 *)
7.0 /. 3.0  (* 2.333... *)
```

---

## 4. No utilizar`Option`correctamente
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

## 5. Estado mutable en funciones recursivas
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

## Resumen
Trampas OCaml: coincidencia de patrones no exhaustiva (advierte el compilador),`=`es igualdad estructural mientras que`==`es física, la división de enteros se trunca, use`Option`en lugar de excepciones y evite el estado mutable a favor de la recursión de cola y los pliegues. El compilador de OCaml es su aliado: preste atención a sus advertencias.