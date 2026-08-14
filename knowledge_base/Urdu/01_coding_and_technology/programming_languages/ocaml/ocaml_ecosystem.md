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
# OCaml — ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ OCaml ایکو سسٹم میں ضروری ٹولز، فریم ورک، اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## OCaml نفاذ
| نفاذ | نوٹس |
|---------------|---------|
| **OCaml 5** | موجودہ، اثرات اور متوازی کے ساتھ |
| **OCaml 4.14** | آخری 4.x (بڑے پیمانے پر استعمال کیا جاتا ہے) |
| **وجہ** | متبادل نحو (فیس بک) |
| **دوبارہ اسکرپٹ** | جدید وجہ جانشین (بکل اسکرپٹ) |
| **OCaml مقامی** | مقامی کوڈ پر مرتب |
| **js_of_ocaml** | جاوا اسکرپٹ پر مرتب کریں |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## ٹولز اور پیکیج مینجمنٹ بنائیں
| ٹول | مقصد |
|------|---------|
| **تیلا** | نظام کی تعمیر (معیاری) |
| **opam** | پیکیج مینیجر |
| **ocamlfind** | لائبریری تلاش کرنے والا |
| **ٹیلا پروجیکٹ** | پروجیکٹ کی ترتیب |
| **esy** | متبادل پیکیج مینیجر |
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

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **خواب** | مکمل اسٹیک | جدید ویب (ایکسپریس سے متاثر) |
| **Cohttp** | HTTP | HTTP کلائنٹ/سرور |
| **افیون** | ہلکا پھلکا | سناترا کی طرح |
| **آکسیجن** | مکمل اسٹیک | ایلیوم (کلائنٹ سرور) |
| **مورف** | ہلکا پھلکا | ویب فریم ورک |
| **Lwt** | Async | کوآپریٹو تھریڈنگ |
| **Async** | Async | جین سٹریٹ کی async |
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

## ڈیٹا بیس
| ٹیکنالوجی | قسم |
|------------|------|
| **Caqti** | ٹائپ سیف ڈیٹا بیس |
| **PG'OCaml** | PostgreSQL (ٹائپ سیف) |
| **sqlite3-ocaml** | SQLite بائنڈنگز |
| **mysql-ocaml** | MySQL پابندیاں |
| **postgresql-ocaml** | PostgreSQL پابندیاں |
| **ارمین** | گٹ جیسا ڈیٹا بیس |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **الکوٹیسٹ** | تیز، رنگین ٹیسٹنگ |
| **اوونٹ** | یونٹ ٹیسٹنگ (xUnit-style) |
| **QCheck** | جائیداد کی بنیاد پر جانچ |
| **کروبار** | فز ٹیسٹنگ |
| **ppx_expect** | ٹیسٹنگ کی توقع کریں (جین اسٹریٹ) |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **ocamlformat** | کوڈ فارمیٹنگ |
| **ocp-indent** | انڈینٹیشن |
| **ocaml-lsp** | زبان کا سرور |
| **ppx** | نحو کی توسیع |
| **مرلن** | IDE سپورٹ (تکمیل، اقسام) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **کور/بیس** | جین سٹریٹ کی معیاری لائبریری |
| **Stdlib** | OCaml معیاری لائبریری |
| **نتیجہ** | خرابی سے نمٹنے |
| **کنٹینرز** | ڈیٹا ڈھانچے |
| **بیٹریاں** | توسیعی معیاری لائبریری |
| **Lwt** | ہلکے دھاگے |
| **Async** | Async پروگرامنگ |
| **Eio** | اثرات پر مبنی I/O (OCaml 5) |
| **ڈومین** | متوازی (OCaml 5) |
| **ppx_deriving** | اخذ افعال |
| **ppx_yojson_conv** | JSON اخذ |
| **یوجسن** | JSON پارسنگ |
| **اینگسٹروم** | پارسر کمبینیٹرز |
| **منہیر** | پارسر جنریٹر |
| **ocamlgraph** | گراف لائبریری |
| **زریت** | صوابدیدی صحت سے متعلق |
| **اوونٹ** | ٹیسٹنگ |
---

## رسمی طریقے
| ٹول | مقصد |
|------|---------|
| **Coq** | پروف اسسٹنٹ (OCaml لکھا ہوا) |
| **کیوں3** | پروگرام کی تصدیق |
| **Alt-Ergo** | ایس ایم ٹی حل کرنے والا |
| **OCaml + ثبوت** | تصدیق شدہ پروگرامز |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **VS کوڈ + ocaml-Plateform** | بہترین OCaml LSP |
| **Emacs + tuareg + merlin** | کلاسک OCaml ماحول |
| **ویم + مرلن** | Vim انضمام |
| **Neovim + ocaml-lsp** | ٹرمینل پر مبنی |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **مقامی بائنری** | `dune build`مقامی بائنریز تیار کرتا ہے |
| **جامد لنکنگ** | مکمل طور پر جامد بائنریز |
| **ڈوکر** | کنٹینرائزڈ |
| **opam سوئچ** | متعدد OCaml ورژن |
| **کراس کمپائل** | کراس تالیف |
---

## خلاصہ
OCaml کا ماحولیاتی نظام درستگی، کارکردگی اور فنکشنل پروگرامنگ پر مرکوز ہے۔ معیاری اسٹیک یہ ہے: **Ocaml 5** بطور رن ٹائم، **Dune** تعمیرات کے لیے، **opam** پیکجز کے لیے، **Dream** یا **Cohttp** ویب کے لیے، **Caqti** ڈیٹا بیس کے لیے، **Alcotest** ٹیسٹنگ کے لیے، **ocamlformat** فارمیٹنگ کے لیے، اور **Merlin** ID کے لیے سپورٹ۔ OCaml کمپائلرز، رسمی توثیق، مالیاتی نظام، اور کہیں بھی درستگی اور کارکردگی کے لحاظ سے بہترین ہے۔ OCaml 5 کے اثرات کا نظام اور متوازی (Domains) زبان میں جدید ہم آہنگی لاتے ہیں۔ ایکو سسٹم کمپائلرز (Coq, F*)، تھیوریم پرورز، اور ہائی ایشورنس سافٹ ویئر بنانے کے لیے ضروری ہے۔