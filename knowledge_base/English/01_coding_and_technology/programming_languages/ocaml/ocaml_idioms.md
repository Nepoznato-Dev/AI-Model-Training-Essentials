<!--
---
# Metadata
title: "OCaml — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic OCaml code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [ocaml, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# OCaml — Idiomatic Patterns & Best Practices

This guide covers idiomatic patterns for writing clean, idiomatic OCaml code.

---

## Pattern Matching

```ocaml
(* ✅ Exhaustive matching *)
let describe = function
  | 0 -> "zero"
  | n when n > 0 -> "positive"
  | _ -> "negative"

(* ✅ Record patterns *)
let { name; email; age } = user in
Printf.printf "%s <%s>\n" name email

(* ✅ Option handling *)
let name = Option.value ~default:"Anonymous" (User.name user)
let result = Option.map String.length (find_user id)
```

---

## Modules & Functors

```ocaml
(* ✅ Module signatures *)
module type REPOSITORY = sig
  type t
  val find : int -> t option
  val save : t -> unit
end

(* ✅ Functor for parameterized modules *)
module MakeService (R : REPOSITORY) = struct
  let process id =
    match R.find id with
    | Some entity -> R.save entity
    | None -> raise Not_found
end
```

---

## Error Handling

```ocaml
(* ✅ Result type *)
let find_user id =
  if id > 0 then Ok { name = "Alice" }
  else Error "Invalid ID"

let process id =
  match find_user id with
  | Ok user -> Printf.printf "Found: %s\n" user.name
  | Error msg -> Printf.printf "Error: %s\n" msg

(* ✅ let* for Result chaining (with ppx) *)
let process id =
  let* user = find_user id in
  let* orders = get_orders user.id in
  Ok (user, orders)
```

---

## Summary

OCaml idioms emphasize: exhaustive pattern matching, modules and functors for abstraction, Result/Option for safety, and the pipe-first operator (`|>`). Follow `ocamlformat` for formatting and `ocaml-lsp` for IDE support. OCaml values type safety and mathematical precision.
