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
# OCaml — 慣用模式與最佳實踐
本指南涵蓋了編寫乾淨、慣用的 OCaml 程式碼的慣用模式。
---

## 模式匹配
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

## 模組和函子
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

## 錯誤處理
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

＃＃ 概括
OCaml 習語強調：詳盡的模式匹配、用於抽象的模組和函子、用於安全的結果/選項以及管道優先運算符 (`|>`)。依照`ocamlformat`進行格式化，並依照`ocaml-lsp`進行 IDE 支援。 OCaml 重視型別安全性和數學精度。