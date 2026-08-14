<!--
---
# Metadata
title: "OCaml — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the OCaml ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ocaml, ecosystem, tooling, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "13 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# OCaml — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the OCaml ecosystem.

---

## OCaml Implementations

| Implementation | Notes |
|---------------|-------|
| **OCaml 5** | Current, with effects and parallelism |
| **OCaml 4.14** | Last 4.x (widely used) |
| **Reason** | Alternative syntax (Facebook) |
| **ReScript** | Modern Reason successor (BuckleScript) |
| **OCaml Native** | Compiled to native code |
| **js_of_ocaml** | Compile to JavaScript |

```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Build Tools & Package Management

| Tool | Purpose |
|------|---------|
| **Dune** | Build system (standard) |
| **opam** | Package manager |
| **ocamlfind** | Library finder |
| **dune-project** | Project configuration |
| **esy** | Alternative package manager |

```bash
# opam
opam init                 # initialize
opam install dune         # install package
opam list                 # list installed
opam update               # update index
opam upgrade              # upgrade packages

# Create project
dune init proj myapp      # new project
dune build                # build
dune runtest              # run tests
```

```lisp
;; dune-project
(lang dune 3.12)
(name myapp)
(generate_opam_files true)

;; dune (executable)
(executable
 (public_name myapp)
 (name main)
 (libraries core async cohttp-lwt-unix))

;; dune (library)
(library
 (name mylib)
 (public_name mylib)
 (libraries core))
```

```opam
# myapp.opam
opam-version: "2.0"
synopsis: "My OCaml application"
depends: [
  "ocaml" {>= "5.0"}
  "dune" {>= "3.0"}
  "core" {>= "v0.16"}
  "async" {>= "v0.16"}
]
```

---

## Web Frameworks

| Framework | Type | Best For |
|-----------|------|----------|
| **Dream** | Full-stack | Modern web (inspired by Express) |
| **Cohttp** | HTTP | HTTP client/server |
| **Opium** | Lightweight | Sinatra-like |
| **Ocsigen** | Full-stack | Eliom (client-server) |
| **Morph** | Lightweight | Web framework |
| **Lwt** | Async | Cooperative threading |
| **Async** | Async | Jane Street's async |

```ocaml
(* Dream example *)
let () =
  Dream.run
  @@ Dream.logger
  @@ Dream.router [
       Dream.get "/" (fun _ -> Dream.html "Hello, World!");
       Dream.get "/users/:id" (fun req ->
         let id = Dream.param "id" req in
         Dream.json {|{"id": "|} ^ id ^ {|"}|});
     ]
```

---

## Database

| Technology | Type |
|------------|------|
| **Caqti** | Type-safe database |
| **PG'OCaml** | PostgreSQL (type-safe) |
| **sqlite3-ocaml** | SQLite bindings |
| **mysql-ocaml** | MySQL bindings |
| **postgresql-ocaml** | PostgreSQL bindings |
| **Irmin** | Git-like database |

```ocaml
(* Caqti example *)
module Db = Caqti_connect_sig(S)

let find_user (module Db : Db) id =
  Db.find_opt
    (Caqti_type.(int ->! t2 int string)
       "SELECT id, name FROM users WHERE id = ?")
    id
```

---

## Testing

| Framework | Purpose |
|-----------|---------|
| **Alcotest** | Fast, colorful testing |
| **OUnit** | Unit testing (xUnit-style) |
| **QCheck** | Property-based testing |
| **Crowbar** | Fuzz testing |
| **ppx_expect** | Expect testing (Jane Street) |

```ocaml
(* Alcotest example *)
let test_find () =
  let service = UserService.create () in
  let user = UserService.find service 1 in
  Alcotest.(check (option string)) "found user" (Some "Alice") (Option.map User.name user)

let test_not_found () =
  let service = UserService.create () in
  let user = UserService.find service 999 in
  Alcotest.(check (option string)) "not found" None (Option.map User.name user)

let () =
  Alcotest.run "UserService" [
    "find", [
      Alcotest.test_case "finds user" `Quick test_find;
      Alcotest.test_case "not found" `Quick test_not_found;
    ];
  ]
```

---

## Code Quality

| Tool | Purpose |
|------|---------|
| **ocamlformat** | Code formatting |
| **ocp-indent** | Indentation |
| **ocaml-lsp** | Language server |
| **ppx** | Syntax extensions |
| **merlin** | IDE support (completions, types) |

```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Key Libraries

| Library | Purpose |
|---------|---------|
| **Core / Base** | Jane Street's standard library |
| **Stdlib** | OCaml standard library |
| **Result** | Error handling |
| **Containers** | Data structures |
| **Batteries** | Extended standard library |
| **Lwt** | Lightweight threads |
| **Async** | Async programming |
| **Eio** | Effects-based I/O (OCaml 5) |
| **Domain** | Parallelism (OCaml 5) |
| **ppx_deriving** | Derive functions |
| **ppx_yojson_conv** | JSON deriving |
| **yojson** | JSON parsing |
| **angstrom** | Parser combinators |
| **menhir** | Parser generator |
| **ocamlgraph** | Graph library |
| **Zarith** | Arbitrary precision |
| **OUnit** | Testing |

---

## Formal Methods

| Tool | Purpose |
|------|---------|
| **Coq** | Proof assistant (OCaml-written) |
| **Why3** | Program verification |
| **Alt-Ergo** | SMT solver |
| **OCaml + proofs** | Verified programs |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **VS Code + ocaml-platform** | Best OCaml LSP |
| **Emacs + tuareg + merlin** | Classic OCaml environment |
| **Vim + merlin** | Vim integration |
| **Neovim + ocaml-lsp** | Terminal-based |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Native binary** | `dune build` produces native binaries |
| **Static linking** | Fully static binaries |
| **Docker** | Containerized |
| **opam switch** | Multiple OCaml versions |
| **Cross-compile** | Cross-compilation |

---

## Summary

OCaml's ecosystem is centered on correctness, performance, and functional programming. The standard stack is: **OCaml 5** as runtime, **Dune** for builds, **opam** for packages, **Dream** or **Cohttp** for web, **Caqti** for databases, **Alcotest** for testing, **ocamlformat** for formatting, and **Merlin** for IDE support. OCaml excels at compilers, formal verification, financial systems, and anywhere correctness and performance matter. OCaml 5's effects system and parallelism (Domains) bring modern concurrency to the language. The ecosystem is essential for building compilers (Coq, F*), theorem provers, and high-assurance software.
