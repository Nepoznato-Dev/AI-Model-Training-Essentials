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
# OCaml – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im OCaml-Ökosystem.
---

## OCaml-Implementierungen
| Umsetzung | Notizen |
|---------------|-------|
| **OCaml 5** | Aktuell, mit Effekten und Parallelität |
| **OCaml 4.14** | Letzte 4.x (weit verbreitet) |
| **Grund** | Alternative Syntax (Facebook) |
| **ReScript** | Modern Reason-Nachfolger (BuckleScript) |
| **OCaml Native** | Kompiliert zu nativem Code |
| **js_of_ocaml** | In JavaScript kompilieren |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Build-Tools und Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **Düne** | Build-System (Standard) |
| **opam** | Paketmanager |
| **ocamlfind** | Bibliotheksfinder |
| **Dünenprojekt** | Projektkonfiguration |
| **esy** | Alternativer Paketmanager |
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

## Web-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **Traum** | Full-Stack | Modernes Web (inspiriert von Express) |
| **Cohttp** | HTTP | HTTP-Client/Server |
| **Opium** | Leicht | Sinatra-artig |
| **Ocsigen** | Full-Stack | Eliom (Client-Server) |
| **Morph** | Leicht | Web-Framework |
| **Lwt** | Asynchron | Kooperatives Einfädeln |
| **Asynchron** | Asynchron | Jane Streets asynchrones |
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

## Datenbank
| Technologie | Geben Sie | ein
|------------|------|
| **Caqti** | Typsichere Datenbank |
| **PG'OCaml** | PostgreSQL (typsicher) |
| **sqlite3-ocaml** | SQLite-Bindungen |
| **mysql-ocaml** | MySQL-Bindungen |
| **postgresql-ocaml** | PostgreSQL-Bindungen |
| **Irmin** | Git-ähnliche Datenbank |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **Alkotest** | Schnelles, farbenfrohes Testen |
| **OUnit** | Unit-Tests (xUnit-Stil) |
| **QCheck** | Eigenschaftsbasiertes Testen |
| **Brecheisen** | Fuzz-Test |
| **ppx_expect** | Erwarten Sie Tests (Jane Street) |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **ocamlformat** | Codeformatierung |
| **ocp-indent** | Einrückung |
| **ocaml-lsp** | Sprachserver |
| **ppx** | Syntaxerweiterungen |
| **merlin** | IDE-Unterstützung (Vervollständigungen, Typen) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Kern / Basis** | Standardbibliothek von Jane Street |
| **Stdlib** | OCaml-Standardbibliothek |
| **Ergebnis** | Fehlerbehandlung |
| **Container** | Datenstrukturen |
| **Batterien** | Erweiterte Standardbibliothek |
| **Lwt** | Leichte Fäden |
| **Asynchron** | Asynchrone Programmierung |
| **Eio** | Effektbasierte I/O (OCaml 5) |
| **Domäne** | Parallelität (OCaml 5) |
| **ppx_deriving** | Funktionen ableiten |
| **ppx_yojson_conv** | JSON-Ableitung |
| **yojson** | JSON-Analyse |
| **Angström** | Parser-Kombinatoren |
| **Hinkelstein** | Parser-Generator |
| **ocamlgraph** | Diagrammbibliothek |
| **Zarith** | Beliebige Präzision |
| **OUnit** | Testen |
---

## Formale Methoden
| Werkzeug | Zweck |
|------|---------|
| **Coq** | Proof-Assistent (OCaml-geschrieben) |
| **Warum3** | Programmüberprüfung |
| **Alt-Ergo** | SMT-Löser |
| **OCaml + Beweise** | Verifizierte Programme |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **VS-Code + Ocaml-Plattform** | Bester OCaml LSP |
| **Emacs + Tuareg + Merlin** | Klassische OCaml-Umgebung |
| **Vim + Merlin** | Vim-Integration |
| **Neovim + ocaml-lsp** | Terminalbasiert |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Native Binärdatei** | `dune build`erzeugt native Binärdateien |
| **Statische Verlinkung** | Vollständig statische Binärdateien |
| **Docker** | Containerisiert |
| **Opam-Schalter** | Mehrere OCaml-Versionen |
| **Cross-Kompilierung** | Cross-Compilation |
---

## Zusammenfassung
Das Ökosystem von OCaml konzentriert sich auf Korrektheit, Leistung und funktionale Programmierung. Der Standard-Stack ist: **OCaml 5** als Laufzeit, **Dune** für Builds, **opam** für Pakete, **Dream** oder **Cohttp** für Web, **Caqti** für Datenbanken, **Alcotest** für Tests, **ocamlformat** für Formatierung und **Merlin** für IDE-Unterstützung. OCaml zeichnet sich durch Compiler, formale Verifizierung, Finanzsysteme und überall dort aus, wo es auf Korrektheit und Leistung ankommt. Das Effektsystem und die Parallelität (Domänen) von OCaml 5 bringen moderne Parallelität in die Sprache. Das Ökosystem ist für die Erstellung von Compilern (Coq, F*), Theoremprüfern und hochsicherer Software von wesentlicher Bedeutung.