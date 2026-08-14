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
# OCaml — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem OCaml.
---

## Implementasi OCaml
| Implementasi | Catatan |
|---------------|-------|
| **OCaml 5** | Saat ini, dengan efek dan paralelisme |
| **OCaml 4.14** | 4.x terakhir (banyak digunakan) |
| **Alasan** | Sintaks alternatif (Facebook) |
| **Skrip Ulang** | Penerus Alasan Modern (BuckleScript) |
| **OCaml Asli** | Dikompilasi ke kode asli |
| **js_of_ocaml** | Kompilasi ke JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Bangun Alat & Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **Bukit pasir** | Membangun sistem (standar) |
| **opam** | Manajer paket |
| **ocamlftemukan** | Penemu perpustakaan |
| **proyek bukit pasir** | Konfigurasi proyek |
| **esy** | Manajer paket alternatif |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Mimpi** | Tumpukan penuh | Web modern (terinspirasi oleh Express) |
| **Cohttp** | HTTP | klien/server HTTP |
| **Candu** | Ringan | Seperti Sinatra |
| **Ocsigen** | Tumpukan penuh | Eliom (server-klien) |
| **Morf** | Ringan | Kerangka web |
| **Lwt** | Asinkron | Threading kooperatif |
| **Asinkron** | Asinkron | Asinkron Jane Street |
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

## Basis Data
| Teknologi | Ketik |
|------------|------|
| **Caqti** | Basis data yang aman untuk tipe |
| **PG'OCaml** | PostgreSQL (aman untuk tipe) |
| **sqlite3-ocaml** | Pengikatan SQLite |
| **mysql-ocaml** | Ikatan MySQL |
| **postgresql-ocaml** | Pengikatan PostgreSQL |
| **Irmin** | Basis data seperti Git |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Tes Alkohol** | Pengujian cepat dan penuh warna |
| **Unit** | Pengujian unit (gaya xUnit) |
| **Periksa Q** | Pengujian berbasis properti |
| **Linggis** | Pengujian bulu halus |
| **ppx_harapan** | Harapkan pengujian (Jane Street) |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **format ocaml** | Pemformatan kode |
| **ocp-indentasi** | Indentasi |
| **ocaml-lsp** | Server bahasa |
| **ppx** | Ekstensi sintaks |
| **merlin** | Dukungan IDE (penyelesaian, tipe) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Inti / Basis** | Perpustakaan standar Jane Street |
| **Stdlib** | Pustaka standar OCaml |
| **Hasil** | Penanganan kesalahan |
| **Wadah** | Struktur data |
| **Baterai** | Perpustakaan standar yang diperluas |
| **Lwt** | Benang ringan |
| **Asinkron** | Pemrograman asinkron |
| **Eio** | I/O berbasis efek (OCaml 5) |
| **Domain** | Paralelisme (OCaml 5) |
| **ppx_deriving** | Turunkan fungsi |
| **ppx_yojson_conv** | Turunan JSON |
| **yojson** | Penguraian JSON |
| **angstrom** | Kombinator parser |
| **menhir** | Generator pengurai |
| **ocamlgraf** | Perpustakaan grafik |
| **Zarit** | Presisi sewenang-wenang |
| **Unit** | Pengujian |
---

## Metode Formal
| Alat | Tujuan |
|------|---------|
| **Coq** | Asisten pembuktian (ditulis OCaml) |
| **Mengapa3** | Verifikasi program |
| **Alt-Ergo** | Pemecah SMT |
| **OCaml + bukti** | Program terverifikasi |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + platform ocaml** | LSP OCaml Terbaik |
| **Emacs + tuareg + merlin** | Lingkungan OCaml klasik |
| **Vim + merlin** | Integrasi Vim |
| **Neovim + ocaml-lsp** | Berbasis terminal |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Biner asli** | `dune build`menghasilkan biner asli |
| **Tautan statis** | Biner yang sepenuhnya statis |
| **Buruh pelabuhan** | dalam kontainer |
| ** saklar opam ** | Beberapa versi OCaml |
| **Kompilasi silang** | Kompilasi silang |
---

## Ringkasan
Ekosistem OCaml berpusat pada kebenaran, kinerja, dan pemrograman fungsional. Tumpukan standarnya adalah: **OCaml 5** sebagai runtime, **Dune** untuk build, **opam** untuk paket, **Dream** atau **Cohttp** untuk web, **Caqti** untuk database, **Alcotest** untuk pengujian, **ocamlformat** untuk pemformatan, dan **Merlin** untuk dukungan IDE. OCaml unggul dalam kompiler, verifikasi formal, sistem keuangan, dan di mana pun kebenaran dan kinerja penting. Sistem efek dan paralelisme (Domain) OCaml 5 menghadirkan konkurensi modern ke dalam bahasa tersebut. Ekosistem sangat penting untuk membangun kompiler (Coq, F*), pembukti teorema, dan perangkat lunak dengan jaminan tinggi.