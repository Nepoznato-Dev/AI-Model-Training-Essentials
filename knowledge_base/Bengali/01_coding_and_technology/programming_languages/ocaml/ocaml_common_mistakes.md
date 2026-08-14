---
# Metadata
title: "OCaml — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in OCaml with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# OCaml — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি সংশোধন সহ OCaml-এ সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্ন ক্যাটালগ করে।
---

## 1. অ-সম্পূর্ণ প্যাটার্ন ম্যাচিং
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

## 2.`=`বনাম `==`
```ocaml
(* ❌ WRONG — structural vs physical equality *)
"hello" == "hello"  (* false — different memory locations *)
[1;2] == [1;2]      (* false — different lists *)

(* ✅ CORRECT — use = for structural equality *)
"hello" = "hello"   (* true — same content *)
[1;2] = [1;2]       (* true — same content *)
```

---

## 3. পূর্ণসংখ্যা বিভাগ
```ocaml
(* ❌ WRONG — integer division truncates *)
1 / 2   (* 0, not 0.5 *)
7 / 3   (* 2, not 2.333 *)

(* ✅ CORRECT — use float division *)
1.0 /. 2.0  (* 0.5 *)
7.0 /. 3.0  (* 2.333... *)
```

---

## 4.`Option`সঠিকভাবে ব্যবহার করা হচ্ছে না
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

## 5. রিকারসিভ ফাংশনে পরিবর্তনযোগ্য অবস্থা
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

## সারাংশ
OCaml ফাঁদ: অ-সম্পূর্ণ প্যাটার্ন ম্যাচিং (কম্পাইলার সতর্ক করে),`=`হল কাঠামোগত সমতা যখন`==`হল শারীরিক, পূর্ণসংখ্যা বিভাজন ছেঁটে যায়, ব্যতিক্রমগুলির পরিবর্তে`Option`ব্যবহার করুন এবং টেইল রিকারশনের পক্ষে পরিবর্তনযোগ্য অবস্থা এড়িয়ে চলুন। OCaml-এর কম্পাইলার হল আপনার মিত্র — এর সতর্কতাগুলি মেনে চলুন।