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

# OCaml — دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية التحتية الأساسية في نظام OCaml البيئي.
---

## تطبيقات OCaml
| التنفيذ | ملاحظات |
|---------------|-------|
| **أوكامل 5** | التيار مع التأثيرات والتوازي |
| **أوكامل 4.14** | آخر 4.x (مستخدم على نطاق واسع) |
| **السبب** | بناء الجملة البديل (الفيسبوك) |
| **إعادة كتابة** | خليفة العقل الحديث (BuckleScript) |
| **OCaml أصلي** | تم تجميعها إلى الكود الأصلي |
| **js_of_ocaml** | ترجمة إلى جافا سكريبت |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## أدوات البناء وإدارة الحزم
| أداة | الغرض |
|------|---------|
| **الكثيب** | نظام البناء (قياسي) |
| **أوبام** | مدير الحزم |
| **أوكاملفيند** | مكتشف المكتبة |
| **مشروع الكثبان** | تكوين المشروع |
| **esy** | مدير الحزم البديل |
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

## أطر الويب
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| **الحلم** | مكدس كامل | الويب الحديث (مستوحى من اكسبريس) |
| ** كوتب ** | HTTP | عميل/خادم HTTP |
| ** الأفيون ** | خفيف الوزن | مثل سيناترا |
| ** أوكسيجين ** | مكدس كامل | إليوم (خادم العميل) |
| ** مورف ** | خفيف الوزن | إطار الويب |
| ** لوت ** | غير متزامن | الخيوط التعاونية |
| **غير متزامن** | غير متزامن | جين ستريت غير المتزامن |
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

##قاعدة البيانات
| تكنولوجيا | اكتب |
|------------|------|
| **ققطي** | قاعدة بيانات آمنة من النوع |
| **PG'OCaml** | PostgreSQL (النوع الآمن) |
| **sqlite3-ocaml** | روابط SQLite |
| **mysql-ocaml** | روابط MySQL |
| **postgresql-ocaml** | روابط PostgreSQL |
| **ايرمين** | قاعدة بيانات تشبه بوابة |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **الكوتيست** | اختبار سريع وملون |
| ** الوحدة ** | اختبار الوحدة (نمط xUnit) |
| ** كيو تشيك ** | الاختبار على أساس الملكية |
| **المخل** | اختبار الزغب |
| **ppx_expect** | توقع الاختبار (شارع جين) |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **تنسيق أوكامل** | تنسيق الكود |
| ** مسافة بادئة لـ ocp ** | المسافة البادئة |
| **ocaml-lsp** | خادم اللغة |
| **بكسل** | ملحقات بناء الجملة |
| **ميرلين** | دعم IDE (الإكمالات والأنواع) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **الأساسية/الأساسية** | مكتبة جين ستريت القياسية |
| **ستدلب** | مكتبة OCaml القياسية |
| **النتيجة** | معالجة الأخطاء |
| **حاويات** | هياكل البيانات |
| **بطاريات** | المكتبة القياسية الموسعة |
| ** لوت ** | خيوط خفيفة الوزن |
| **غير متزامن** | برمجة غير متزامنة |
| **إيو** | الإدخال/الإخراج القائم على التأثيرات (OCaml 5) |
| **المجال** | التوازي (أوكامل 5) |
| **ppx_deriving** | اشتقاق الدوال |
| **ppx_yojson_conv** | اشتقاق JSON |
| **يوجسون** | تحليل JSON |
| **انجستروم** | مجمعات المحلل اللغوي |
| **منهير** | مولد المحلل اللغوي |
| **أوكاملغراف** | مكتبة الرسم البياني |
| **زاريث** | الدقة التعسفية |
| ** الوحدة ** | اختبار |
---

## الطرق الرسمية
| أداة | الغرض |
|------|---------|
| ** كوك ** | مساعد الإثبات (OCaml مكتوب) |
| **لماذا3** | التحقق من البرنامج |
| ** البديل إرجو ** | سمت حلالا |
| **أوكامل + براهين** | برامج تم التحقق منها |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **رمز VS + منصة ocaml** | أفضل OCaml LSP |
| **إيماكس + طوارق + ميرلين** | بيئة OCaml الكلاسيكية |
| ** فيم + ميرلين ** | تكامل فيم |
| **نيوفيم + اوكامل-lsp** | القائم على المحطة الطرفية |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **ثنائي أصلي** | `dune build`ينتج ثنائيات أصلية |
| **الربط الثابت** | ثنائيات ثابتة بالكامل |
| ** عامل الميناء ** | في حاويات |
| **مفتاح أوبام** | إصدارات أوكامل متعددة |
| ** الترجمة المتقاطعة ** | التجميع المتقاطع |
---

## ملخص
يتمحور النظام البيئي لـ OCaml حول الصحة والأداء والبرمجة الوظيفية. المكدس القياسي هو: **OCaml 5** كوقت تشغيل، **Dune** للإنشاءات، **opam** للحزم، **Dream** أو **Cohttp** للويب، **Caqti** لقواعد البيانات، **Alcotest** للاختبار، **ocamlformat** للتنسيق، و **Merlin** لدعم IDE. تتفوق OCaml في المترجمين، والتحقق الرسمي، والأنظمة المالية، وفي أي مكان يهم الصحة والأداء. يوفر نظام التأثيرات والتوازي (المجالات) الخاص بـ OCaml 5 التزامن الحديث للغة. يعد النظام البيئي ضروريًا لبناء المترجمين (Coq، F*)، ومثبتات النظرية، وبرامج الضمان العالي.