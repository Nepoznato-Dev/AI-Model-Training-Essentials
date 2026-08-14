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
# OCaml — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz OCaml ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## OCaml Uygulamaları
| Uygulama | Notlar |
|---------------|----------|
| **OCaml 5** | Etkileri ve paralelliği olan güncel |
| **OCaml 4.14** | Son 4.x (yaygın olarak kullanılır) |
| **Sebep** | Alternatif sözdizimi (Facebook) |
| **ReScript** | Modern Reason'un halefi (BuckleScript) |
| **OCaml Yerli** | Yerel koda göre derlendi |
| **js_of_ocaml** | JavaScript'e Derle |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Araçlar ve Paket Yönetimi Oluşturma
| Araç | Amaç |
|------|------------|
| **Kumul** | Yapı sistemi (standart) |
| **opam** | Paket yöneticisi |
| **ocamlfind** | Kütüphane bulucu |
| **kumul projesi** | Proje konfigürasyonu |
| **esy** | Alternatif paket yöneticisi |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Rüya** | Tam yığın | Modern web (Express'ten esinlenilmiştir) |
| **Cohttp** | HTTP | HTTP istemcisi/sunucusu |
| **Afyon** | Hafif | Sinatra benzeri |
| **Oksijen** | Tam yığın | Eliom (istemci-sunucu) |
| **Dönüşüm** | Hafif | Web çerçevesi |
| **Lwt** | Eşzamansız | İşbirliğine dayalı diş açma |
| **Asenkron** | Eşzamansız | Jane Street'in zaman uyumsuzluğu |
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

## Veritabanı
| Teknoloji | Tür |
|---------------|------|
| **Caqti** | Tür açısından güvenli veritabanı |
| **PG'OCaml** | PostgreSQL (tür açısından güvenli) |
| **sqlite3-ocaml** | SQLite bağlamaları |
| **mysql-ocaml** | MySQL bağlamaları |
| **postgresql-ocaml** | PostgreSQL bağlamaları |
| **İrmin** | Git benzeri veritabanı |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **Alkotest** | Hızlı, renkli testler |
| **Birim** | Birim testi (xUnit tarzı) |
| **QKontrol** | Mülkiyet bazlı testler |
| **Kazayağı** | Fuzz testi |
| **ppx_expect** | Testi bekliyoruz (Jane Street) |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **ocamlformat** | Kod biçimlendirme |
| **ocp-girinti** | Girinti |
| **ocaml-lsp** | Dil sunucusu |
| **ppx** | Sözdizimi uzantıları |
| **merlin** | IDE desteği (tamamlamalar, türler) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **Çekirdek / Taban** | Jane Street'in standart kütüphanesi |
| **Stdlib** | OCaml standart kütüphanesi |
| **Sonuç** | Hata işleme |
| **Konteynerler** | Veri yapıları |
| **Piller** | Genişletilmiş standart kütüphane |
| **Lwt** | Hafif iplikler |
| **Asenkron** | Asenkron programlama |
| **Eio** | Efekt tabanlı G/Ç (OCaml 5) |
| **Alan adı** | Paralellik (OCaml 5) |
| **ppx_deriving** | Türetme işlevleri |
| **ppx_yojson_conv** | JSON türetme |
| **yojson** | JSON ayrıştırma |
| **angström** | Ayrıştırıcı birleştiriciler |
| **menhir** | Ayrıştırıcı oluşturucu |
| **ocamlgraph** | Grafik kütüphanesi |
| **Zarith** | Keyfi hassasiyet |
| **Birim** | Test |
---

## Biçimsel Yöntemler
| Araç | Amaç |
|------|------------|
| **Coq** | İspat asistanı (OCaml-yazılı) |
| **Neden3** | Program doğrulaması |
| **Alt-Ergo** | SMT çözücü |
| **OCaml + provalar** | Doğrulanmış programlar |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + ocaml platformu** | En İyi OCaml LSP |
| **Emacs + tuareg + merlin** | Klasik OCaml ortamı |
| **Vim + merlin** | Vim entegrasyonu |
| **Neovim + ocaml-lsp** | Terminal tabanlı |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Yerel ikili** | `dune build`yerel ikili dosyalar üretir |
| **Statik bağlantı** | Tamamen statik ikili dosyalar |
| **Docker** | Konteynerde |
| **opam anahtarı** | Çoklu OCaml sürümleri |
| **Çapraz derleme** | Çapraz derleme |
---

## Özet
OCaml'in ekosistemi doğruluk, performans ve işlevsel programlamaya odaklanmıştır. Standart yığın şudur: Çalışma zamanı olarak **OCaml 5**, derlemeler için **Dune**, paketler için **opam**, web için **Dream** veya **Cohttp**, veritabanları için **Caqti**, test için **Alcotest**, biçimlendirme için **ocamlformat** ve IDE desteği için **Merlin**. OCaml, derleyiciler, resmi doğrulama, finansal sistemler ve doğruluk ve performansın önemli olduğu her yerde mükemmeldir. OCaml 5'in efekt sistemi ve paralellik (Etki Alanları), dile modern eşzamanlılık getirir. Ekosistem, derleyiciler (Coq, F*), teorem kanıtlayıcılar ve yüksek güvenceli yazılımlar oluşturmak için gereklidir.