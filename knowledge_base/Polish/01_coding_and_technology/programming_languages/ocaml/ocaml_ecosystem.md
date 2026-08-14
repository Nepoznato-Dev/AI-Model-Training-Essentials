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
# OCaml — Przewodnik po ekosystemie i narzędziach
W tym przewodniku opisano podstawowe narzędzia, frameworki i infrastrukturę w ekosystemie OCaml.
---

## Implementacje OCaml
| Wdrożenie | Notatki |
|--------------|-------|
| **OCaml 5** | Aktualny, z efektami i równoległością |
| **OCaml 4.14** | Ostatnie 4.x (powszechnie używane) |
| **Powód** | Alternatywna składnia (Facebook) |
| **Reskrypt** | Następca Modern Reason (BuckleScript) |
| **Natywny OCaml** | Skompilowany do kodu natywnego |
| **js_of_ocaml** | Kompiluj do JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Narzędzia do budowania i zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **Wydma** | System kompilacji (standard) |
| **opam** | Menedżer pakietów |
| **ocamlfind** | Wyszukiwarka bibliotek |
| **projekt wydmowy** | Konfiguracja projektu |
| **tak** | Alternatywny menedżer pakietów |
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

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **Sen** | Pełny stos | Nowoczesna sieć internetowa (inspirowana Expressem) |
| **Cohttp** | HTTP | Klient/serwer HTTP |
| **Opium** | Lekki | Podobny do Sinatry |
| **Oksygen** | Pełny stos | Eliom (klient-serwer) |
| **Przemiana** | Lekki | Struktura internetowa |
| **Cóż** | Asynchroniczny | Wątkowanie kooperacyjne |
| **Asynchronizacja** | Asynchroniczny | Asynchronizacja Jane Street |
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

## Baza danych
| Technologia | Wpisz |
|------------|------|
| **Caqti** | Baza danych bezpieczna dla typów |
| **PG'OCaml** | PostgreSQL (bezpieczny typ) |
| **sqlite3-ocaml** | Powiązania SQLite |
| **mysql-ocaml** | Powiązania MySQL |
| **postgresql-ocaml** | Powiązania PostgreSQL |
| **Irmin** | Baza danych podobna do Gita |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **Alkotest** | Szybkie, kolorowe testowanie |
| **Ojednostka** | Testowanie jednostkowe (w stylu xUnit) |
| **QSprawdź** | Testowanie oparte na właściwościach |
| **Łom** | Testowanie fuzza |
| **ppx_expect** | Spodziewaj się testów (Jane Street) |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **format ocaml** | Formatowanie kodu |
| **ocp-wcięcie** | Wcięcie |
| **ocaml-lsp** | Serwer językowy |
| **ppx** | Rozszerzenia składni |
| **Merlinie** | Obsługa IDE (uzupełnienia, typy) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **Rdzeń / Baza** | Standardowa biblioteka Jane Street |
| **Stdlib** | Standardowa biblioteka OCaml |
| **Wynik** | Obsługa błędów |
| **Kontenery** | Struktury danych |
| **Baterie** | Rozszerzona biblioteka standardowa |
| **Cóż** | Lekkie nici |
| **Asynchronizacja** | Programowanie asynchroniczne |
| **Eio** | We/wy oparte na efektach (OCaml 5) |
| **Domena** | Równoległość (OCaml 5) |
| **pochodzenie_ppx** | Wyprowadź funkcje |
| **ppx_yojson_conv** | Wyprowadzenie JSON |
| **Yojson** | Analiza JSON |
| **angstrem** | Kombinatory parserów |
| **menhir** | Generator parsera |
| **ocamlgraf** | Biblioteka wykresów |
| **Zarith** | Dowolna precyzja |
| **Ojednostka** | Testowanie |
---

## Metody formalne
| Narzędzie | Cel |
|------|-------------|
| **Coq** | Asystent dowodu (napisany w OCaml) |
| **Dlaczego3** | Weryfikacja programu |
| **Alternatywnie** | Rozwiązanie SMT |
| **OCaml + dowody** | Sprawdzone programy |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS + platforma ocaml** | Najlepszy OCaml LSP |
| **Emacs + tuareg + Merlin** | Klasyczne środowisko OCaml |
| **Vim + Merlin** | Integracja z Vimem |
| **Neovim + ocaml-lsp** | Oparte na terminalu |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Natywny plik binarny** | `dune build`tworzy natywne pliki binarne |
| **Łączenie statyczne** | W pełni statyczne pliki binarne |
| **Doker** | Kontenerowy |
| **przełącznik Opama** | Wiele wersji OCaml |
| **Kompilacja krzyżowa** | Kompilacja krzyżowa |
---

## Streszczenie
Ekosystem OCaml koncentruje się na poprawności, wydajności i programowaniu funkcjonalnym. Standardowy stos to: **OCaml 5** jako środowisko wykonawcze, **Dune** do kompilacji, **opam** do pakietów, **Dream** lub **Cohttp** do Internetu, **Caqti** do baz danych, **Alcotest** do testowania, **ocamlformat** do formatowania i **Merlin** do obsługi IDE. OCaml przoduje w kompilatorach, weryfikacji formalnej, systemach finansowych i wszędzie tam, gdzie liczy się poprawność i wydajność. System efektów i równoległość (Domeny) OCaml 5 wprowadzają do języka nowoczesną współbieżność. Ekosystem jest niezbędny do tworzenia kompilatorów (Coq, F*), dowodzenia twierdzeń i oprogramowania o wysokiej pewności.