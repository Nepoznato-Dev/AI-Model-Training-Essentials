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
# OCaml — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, framework, at imprastraktura sa OCaml ecosystem.
---

## Mga Pagpapatupad ng OCaml
| Pagpapatupad | Mga Tala |
|--------------|-------|
| **OCaml 5** | Kasalukuyan, may mga epekto at paralelismo |
| **OCaml 4.14** | Huling 4.x (malawakang ginagamit) |
| **Dahilan** | Alternatibong syntax (Facebook) |
| **Rescript** | Kapalit ng Makabagong Dahilan (BuckleScript) |
| **OCaml Native** | Naipon sa katutubong code |
| **js_of_ocaml** | Mag-compile sa JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Bumuo ng Mga Tool at Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **Dune** | Bumuo ng system (standard) |
| **opam** | Tagapamahala ng package |
| **ocamlfind** | Tagahanap ng library |
| **dune-project** | Configuration ng proyekto |
| **esy** | Alternatibong manager ng package |
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

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **Pangarap** | Full-stack | Modern web (inspirasyon ng Express) |
| **Cohttp** | HTTP | HTTP client/server |
| **Opyo** | Magaan | Parang sinatra |
| **Ocsigen** | Full-stack | Eliom (client-server) |
| **Morp** | Magaan | Web framework |
| **Lwt** | Async | Cooperative threading |
| **Async** | Async | Async ng Jane Street |
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
| Teknolohiya | Uri |
|------------|------|
| **Caqti** | Ligtas na uri ng database |
| **PG'OCaml** | PostgreSQL (type-safe) |
| **sqlite3-ocaml** | SQLite bindings |
| **mysql-ocaml** | MySQL bindings |
| **postgresql-ocaml** | PostgreSQL bindings |
| **Irmin** | database na parang Git |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **Alcotest** | Mabilis, makulay na pagsubok |
| **OUnit** | Pagsubok ng unit (estilo ng xUnit) |
| **QCheck** | Pagsubok na nakabatay sa ari-arian |
| **Crowbar** | Fuzz testing |
| **ppx_expect** | Asahan ang pagsubok (Jane Street) |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **ocamlformat** | Pag-format ng code |
| **ocp-indent** | Indentation |
| **ocaml-lsp** | Server ng wika |
| **ppx** | Mga extension ng syntax |
| **merlin** | Suporta sa IDE (mga pagkumpleto, mga uri) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **Core / Base** | Karaniwang aklatan ng Jane Street |
| **Stdlib** | OCaml karaniwang library |
| **Resulta** | Error sa pangangasiwa |
| **Mga lalagyan** | Mga istruktura ng data |
| **Mga Baterya** | Pinalawak na karaniwang library |
| **Lwt** | Magaan na mga thread |
| **Async** | Async programming |
| **Eio** | I/O na nakabatay sa mga epekto (OCaml 5) |
| **Domain** | Paralelismo (OCaml 5) |
| **ppx_deriving** | Kunin ang mga function |
| **ppx_yojson_conv** | JSON deriving |
| **yojson** | Pag-parse ng JSON |
| **angstrom** | Mga parser combinator |
| **menhir** | generator ng parser |
| **ocamlgraph** | library ng graph |
| **Zarith** | Arbitraryong katumpakan |
| **OUnit** | Pagsubok |
---

## Mga Pormal na Pamamaraan
| Tool | Layunin |
|------|---------|
| **Coq** | Patunay na katulong (OCaml-written) |
| **Bakit3** | Pag-verify ng programa |
| **Alt-Ergo** | SMT solver |
| **OCaml + proofs** | Mga na-verify na programa |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code + ocaml-platform** | Pinakamahusay na OCaml LSP |
| **Emacs + tuareg + merlin** | Klasikong kapaligiran ng OCaml |
| **Vim + merlin** | Pagsasama ng Vim |
| **Neovim + ocaml-lsp** | Nakabatay sa terminal |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Native binary** | `dune build`ay gumagawa ng mga katutubong binary |
| **Static linking** | Ganap na static na binary |
| **Docker** | Naka-container |
| **opam switch** | Maramihang bersyon ng OCaml |
| **Cross-compile** | Cross-compilation |
---

## Buod
Ang ecosystem ng OCaml ay nakasentro sa kawastuhan, pagganap, at functional na programming. Ang karaniwang stack ay: **OCaml 5** bilang runtime, **Dune** para sa mga build, **opam** para sa mga package, **Dream** o **Cohttp** para sa web, **Caqti** para sa mga database, **Alcotest** para sa pagsubok, **ocamlformat** para sa pag-format, at **Merlin** para sa suporta sa IDE. Ang OCaml ay mahusay sa mga compiler, pormal na pag-verify, mga sistema ng pananalapi, at kahit saan mahalaga ang kawastuhan at pagganap. Ang mga effect system ng OCaml 5 at parallelism (Domains) ay nagdadala ng modernong pagkakatugma sa wika. Ang ecosystem ay mahalaga para sa pagbuo ng mga compiler (Coq, F*), theorem provers, at high-assurance software.