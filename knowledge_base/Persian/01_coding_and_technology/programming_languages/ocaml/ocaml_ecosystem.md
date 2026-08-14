---
# Metadata
title: "OCaml — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the OCaml ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# OCaml - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم OCaml را پوشش می‌دهد.
---

## پیاده سازی OCaml
| پیاده سازی | یادداشت ها |
|---------------|-------|
| **OCaml 5** | جریان، با اثرات و موازی |
| **OCaml 4.14** | آخرین 4.x (به طور گسترده استفاده می شود) |
| **دلیل** | نحو جایگزین (فیس بوک) |
| **ReScript** | جانشین عقل مدرن (BuckleScript) |
| **OCaml Native** | کامپایل شده به کد بومی |
| **js_of_ocaml** | کامپایل به جاوا اسکریپت |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## ابزارهای ساخت و مدیریت بسته
| ابزار | هدف |
|------|---------|
| **تلماسه** | سیستم ساخت (استاندارد) |
| **اپام** | مدیر بسته |
| **ocamlfind** | کتابخانه یاب |
| **پروژه تپه** | پیکربندی پروژه |
| **esy** | مدیر بسته جایگزین |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **رویا** | تمام پشته | وب مدرن (با الهام از Express) |
| **Cohttp** | HTTP | سرویس گیرنده/سرور HTTP |
| **تریاک** | سبک | سیناترا مانند |
| **Ocsigen** | تمام پشته | Eliom (مشتری-سرور) |
| **مورف ** | سبک | چارچوب وب |
| **Lwt** | همگام | نخ تعاونی |
| **ناهمگام** | همگام | جین استریت همگام |
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

## پایگاه داده
| فناوری | نوع |
|------------|------|
| **Caqti** | پایگاه داده ایمن تایپ |
| **PG'OCaml** | PostgreSQL (نوع امن) |
| **sqlite3-ocaml** | اتصالات SQLite |
| **mysql-ocaml** | اتصالات MySQL |
| **postgresql-ocaml** | اتصالات PostgreSQL |
| **ایرمین** | پایگاه داده Git مانند |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **الکوتست** | تست سریع و رنگارنگ |
| **یونیت** | تست واحد (xUnit-style) |
| **QCheck** | تست مبتنی بر اموال |
| **کلاغ** | تست فاز |
| **ppx_expect** | انتظار تست (خیابان جین) |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **ocamlformat** | قالب بندی کد |
| **ocp-indent** | تورفتگی |
| **ocaml-lsp** | سرور زبان |
| **ppx** | پسوندهای نحوی |
| **مرلین** | پشتیبانی IDE (تکمیل، انواع) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **هسته / پایه** | کتابخانه استاندارد جین استریت |
| **Stdlib** | کتابخانه استاندارد OCaml |
| **نتیجه** | رسیدگی به خطا |
| **ظروف** | ساختار داده |
| **باتری** | کتابخانه استاندارد توسعه یافته |
| **Lwt** | نخ های سبک |
| **ناهمگام** | برنامه نویسی Async |
| **Eio** | I/O مبتنی بر جلوه ها (OCaml 5) |
| **دامنه** | موازی سازی (OCaml 5) |
| **ppx_deriving** | توابع استخراج |
| **ppx_yojson_conv** | استخراج JSON |
| **یوجسون** | تجزیه JSON |
| **انگستروم** | ترکیبات تجزیه کننده |
| **منهیر** | مولد تجزیه کننده |
| **ocamlgraph** | کتابخانه نمودار |
| **زرث** | دقت دلخواه |
| **یونیت** | تست |
---

## روش های رسمی
| ابزار | هدف |
|------|---------|
| **Coq** | دستیار اثبات (OCaml-نوشته) |
| **چرا3** | تایید برنامه |
| **Alt-Ergo** | حل کننده SMT |
| **OCaml + اثبات** | برنامه های تایید شده |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + ocaml-platform** | بهترین OCaml LSP |
| **ایمکس + توارگ + مرلین** | محیط کلاسیک Ocaml |
| **ویم + مرلین** | ادغام Vim |
| **Neovim + ocaml-lsp** | مبتنی بر ترمینال |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **دودویی بومی** | `dune build`باینری های بومی |
| **پیوند استاتیک** | باینری کاملا ثابت |
| **داکر** | کانتینری |
| **سوئیچ opam** | چند نسخه OCaml |
| **تقاطع کامپایل** | تالیف متقابل |
---

## خلاصه
اکوسیستم OCaml بر صحت، عملکرد و برنامه ریزی کاربردی متمرکز است. پشته استاندارد عبارتند از: **OCaml 5** به عنوان زمان اجرا، **Dune** برای ساخت، **opam** برای بسته ها، **Dream** یا **Cohttp** برای وب، **Caqti** برای پایگاه های داده، **Alcotest** برای آزمایش، **ocamlformat** برای قالب بندی، و **Merlin** برای پشتیبانی از IDE. OCaml در کامپایلرها، تأیید رسمی، سیستم های مالی و هر جایی که صحت و عملکرد مهم باشد، برتری دارد. سیستم اثرات OCaml 5 و موازی سازی (Domains) همزمانی مدرن را به زبان می آورد. اکوسیستم برای ساخت کامپایلرها (Coq، F*)، اثبات کننده قضیه و نرم افزارهای با اطمینان بالا ضروری است.