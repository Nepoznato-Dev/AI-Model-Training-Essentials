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
# OCaml - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่สำคัญในระบบนิเวศของ OCaml
---

## การใช้งาน OCaml
| การนำไปปฏิบัติ | หมายเหตุ |
|---------|-------|
| **OCaml 5** | ปัจจุบันมีเอฟเฟกต์และความเท่าเทียม |
| **OCaml 4.14** | Last 4.x (ใช้กันอย่างแพร่หลาย) |
| **เหตุผล** | ไวยากรณ์ทางเลือก (Facebook) |
| **เขียนใหม่** | ผู้สืบทอดเหตุผลสมัยใหม่ (BuckleScript) |
| **OCaml พื้นเมือง** | คอมไพล์เป็นโค้ดเนทีฟ |
| **js_of_ocaml** | คอมไพล์เป็น JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## สร้างเครื่องมือและการจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ดูน** | สร้างระบบ (มาตรฐาน) |
| **โอแพม** | ผู้จัดการแพ็คเกจ |
| **ocamlfind** | ค้นหาห้องสมุด |
| **โครงการเนินทราย** | การกำหนดค่าโครงการ |
| **อีซี่** | ตัวจัดการแพ็คเกจสำรอง |
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

## กรอบงานเว็บ
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **ความฝัน** | เต็มกอง | เว็บสมัยใหม่ (ได้แรงบันดาลใจจาก Express) |
| **โคhttp** | HTTP | ไคลเอนต์ HTTP / เซิร์ฟเวอร์ |
| **ฝิ่น** | น้ำหนักเบา | เหมือนซินาตร้า |
| **อ็อกซิเกน** | เต็มกอง | Eliom (ไคลเอนต์ - เซิร์ฟเวอร์) |
| **มอร์ฟ** ​​| น้ำหนักเบา | กรอบงานเว็บ |
| **Lwt** | อะซิงก์ | การทำเกลียวแบบร่วมมือ |
| **อะซิงโครนัส** | อะซิงก์ | async ของ Jane Street |
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

## ฐานข้อมูล
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **กาคติ** | ฐานข้อมูลประเภทปลอดภัย |
| **PG'OCaml** | PostgreSQL (ประเภทปลอดภัย) |
| **sqlite3-ocaml** | การผูก SQLite |
| **mysql-ocaml** | การผูก MySQL |
| **postgresql-ocaml** | การผูก PostgreSQL |
| **ไอร์มิน** | ฐานข้อมูลเหมือน Git |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **การทดสอบแอลกอฮอล์** | การทดสอบที่รวดเร็วและมีสีสัน |
| **หน่วย** | การทดสอบหน่วย (สไตล์ xUnit) |
| **คิวเช็ค** | การทดสอบตามคุณสมบัติ |
| **ชะแลง** | การทดสอบฟัซซี |
| **ppx_expect** | คาดว่าจะมีการทดสอบ (Jane Street) |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ocamlformat** | การจัดรูปแบบโค้ด |
| **ocp-เยื้อง** | การเยื้อง |
| **ocaml-lsp** | เซิร์ฟเวอร์ภาษา |
| **ppx** | นามสกุลไวยากรณ์ |
| **เมอร์ลิน** | รองรับ IDE (เสร็จสิ้น, ประเภท) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **แกน/ฐาน** | ห้องสมุดมาตรฐานของ Jane Street |
| **Stdlib** | ไลบรารีมาตรฐาน OCaml |
| **ผลลัพธ์** | การจัดการข้อผิดพลาด |
| **ตู้คอนเทนเนอร์** | โครงสร้างข้อมูล |
| **แบตเตอรี่** | ไลบรารีมาตรฐานเพิ่มเติม |
| **Lwt** | ด้ายน้ำหนักเบา |
| **อะซิงโครนัส** | การเขียนโปรแกรมแบบอะซิงก์ |
| **อีโอ** | I/O ตามเอฟเฟกต์ (OCaml 5) |
| **โดเมน** | ความเท่าเทียม (OCaml 5) |
| **ppx_deriving** | สืบทอดฟังก์ชัน |
| **ppx_yojson_conv** | JSON ที่ได้รับ |
| **ยอจสัน** | การแยกวิเคราะห์ JSON |
| **อังสตรอม** | ตัวรวมพาร์เซอร์ |
| **เมนเฮียร์** | เครื่องกำเนิดพาร์เซอร์ |
| **ocamlgraph** | ไลบรารีกราฟ |
| **ซาริธ** | ความแม่นยำโดยพลการ |
| **หน่วย** | การทดสอบ |
---

## วิธีการอย่างเป็นทางการ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **โค้ก** | ผู้ช่วยพิสูจน์อักษร (เขียนโดย OCaml) |
| **ทำไม3** | การตรวจสอบโปรแกรม |
| **อัลท์-เออร์โก** | ตัวแก้ปัญหา SMT |
| **OCaml + หลักฐาน** | โปรแกรมที่ตรวจสอบแล้ว |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **รหัส VS + แพลตฟอร์ม ocaml** | สุดยอด OCaml LSP |
| **Emacs + ทัวเร็ก + เมอร์ลิน** | สภาพแวดล้อม OCaml แบบคลาสสิก |
| **วิม + เมอร์ลิน** | การรวมเป็นกลุ่ม |
| **นีโอวิม + ocaml-lsp** | บนเทอร์มินัล |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **ไบนารีดั้งเดิม** | `dune build`สร้างไบนารีดั้งเดิม |
| **การเชื่อมโยงแบบคงที่** | ไบนารีคงที่โดยสมบูรณ์ |
| **นักเทียบท่า** | บรรจุในตู้คอนเทนเนอร์ |
| **สวิตช์ opam** | OCaml หลายเวอร์ชัน |
| **ข้ามคอมไพล์** | การรวบรวมข้าม |
---

## สรุป
ระบบนิเวศของ OCaml มุ่งเน้นไปที่ความถูกต้อง ประสิทธิภาพ และการเขียนโปรแกรมเชิงฟังก์ชัน สแต็กมาตรฐานคือ: **OCaml 5** สำหรับรันไทม์, **Dune** สำหรับบิลด์, **opam** สำหรับแพ็คเกจ, **Dream** หรือ **Cohttp** สำหรับเว็บ, **Caqti** สำหรับฐานข้อมูล, **Alcotest** สำหรับการทดสอบ, **ocamlformat** สำหรับการจัดรูปแบบ และ **Merlin** สำหรับการสนับสนุน IDE OCaml เป็นเลิศในด้านคอมไพเลอร์ การตรวจสอบอย่างเป็นทางการ ระบบการเงิน และความถูกต้องและประสิทธิภาพในทุกที่ ระบบเอฟเฟกต์ของ OCaml 5 และความเท่าเทียม (โดเมน) นำการทำงานพร้อมกันที่ทันสมัยมาสู่ภาษา ระบบนิเวศเป็นสิ่งจำเป็นสำหรับการสร้างคอมไพเลอร์ (Coq, F*) การพิสูจน์ทฤษฎีบท และซอฟต์แวร์ที่มีความเชื่อมั่นสูง