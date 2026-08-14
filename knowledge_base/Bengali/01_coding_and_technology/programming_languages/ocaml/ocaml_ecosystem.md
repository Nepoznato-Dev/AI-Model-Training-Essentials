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
# OCaml — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি OCaml ইকোসিস্টেমের প্রয়োজনীয় টুলস, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## OCaml বাস্তবায়ন
| বাস্তবায়ন | নোট |
|---------------|---------|
| **OCaml 5** | বর্তমান, প্রভাব এবং সমান্তরাল সঙ্গে |
| **OCaml 4.14** | শেষ 4.x (ব্যাপকভাবে ব্যবহৃত) |
| **কারণ** | বিকল্প সিনট্যাক্স (ফেসবুক) |
| **পুনঃস্ক্রিপ্ট** | আধুনিক কারণ উত্তরসূরি (বাকলস্ক্রিপ্ট) |
| **OCaml নেটিভ** | নেটিভ কোডে সংকলিত |
| **js_of_ocaml** | জাভাস্ক্রিপ্টে কম্পাইল |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## টুলস এবং প্যাকেজ ম্যানেজমেন্ট তৈরি করুন
| টুল | উদ্দেশ্য |
|------|---------|
| **ডুন** | বিল্ড সিস্টেম (মান) |
| **ওপাম** | প্যাকেজ ম্যানেজার |
| **ওক্যামফাইন্ড** | লাইব্রেরি ফাইন্ডার |
| **ডুন-প্রকল্প** | প্রকল্প কনফিগারেশন |
| **esy** | বিকল্প প্যাকেজ ম্যানেজার |
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

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **স্বপ্ন** | ফুল-স্ট্যাক | আধুনিক ওয়েব (এক্সপ্রেস দ্বারা অনুপ্রাণিত) |
| **Cohttp** | HTTP | HTTP ক্লায়েন্ট/সার্ভার |
| **আফিম** | লাইটওয়েট | সিনাট্রা-সদৃশ |
| **অক্সিজেন** | ফুল-স্ট্যাক | এলিয়ম (ক্লায়েন্ট-সার্ভার) |
| **মর্ফ** | লাইটওয়েট | ওয়েব ফ্রেমওয়ার্ক |
| **Lwt** | অ্যাসিঙ্ক | সমবায় থ্রেডিং |
| **অসিঙ্ক** | অ্যাসিঙ্ক | জেন স্ট্রিটের অ্যাসিঙ্ক |
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

## ডাটাবেস
| প্রযুক্তি | প্রকার |
|------------|------|
| **ক্যাক্টি** | টাইপ-নিরাপদ ডাটাবেস |
| **PG'OCaml** | PostgreSQL (টাইপ-সেফ) |
| **sqlite3-ocaml** | SQLite বাইন্ডিং |
| **mysql-ocaml** | মাইএসকিউএল বাঁধাই |
| **postgresql-ocaml** | PostgreSQL বাইন্ডিং |
| **ইরমিন** | গিট-এর মত ডাটাবেস |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **অ্যালকোটেস্ট** | দ্রুত, রঙিন পরীক্ষা |
| **ইউনিট** | ইউনিট পরীক্ষা (xUnit-style) |
| **QCheck** | সম্পত্তি ভিত্তিক পরীক্ষা |
| **ক্রোবার** | ফাজ টেস্টিং |
| **ppx_প্রত্যাশিত** | পরীক্ষার প্রত্যাশা করুন (জেন স্ট্রিট) |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **ocamlformat** | কোড ফরম্যাটিং |
| **ocp-ইন্ডেন্ট** | ইন্ডেন্টেশন |
| **ocaml-lsp** | ভাষা সার্ভার |
| **ppx** | সিনট্যাক্স এক্সটেনশন |
| **মারলিন** | IDE সমর্থন (সম্পূর্ণতা, প্রকার) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **কোর/বেস** | জেন স্ট্রিটের স্ট্যান্ডার্ড লাইব্রেরি |
| **Stdlib** | OCaml স্ট্যান্ডার্ড লাইব্রেরি |
| **ফলাফল** | ত্রুটি পরিচালনা |
| **ধারক** | ডেটা স্ট্রাকচার |
| **ব্যাটারি** | বর্ধিত স্ট্যান্ডার্ড লাইব্রেরি |
| **Lwt** | লাইটওয়েট থ্রেড |
| **অসিঙ্ক** | অ্যাসিঙ্ক প্রোগ্রামিং |
| **ইও** | প্রভাব-ভিত্তিক I/O (OCaml 5) |
| **ডোমেন** | সমান্তরালতা (OCaml 5) |
| **ppx_deriving** | ফাংশন আহরণ |
| **ppx_yojson_conv** | JSON প্রাপ্ত |
| **যোজসন** | JSON পার্সিং |
| **অ্যাংস্ট্রম** | পার্সার কম্বিনেটর |
| **মেনহির** | পার্সার জেনারেটর |
| **ocamlgraph** | গ্রাফ লাইব্রেরি |
| **জরিথ** | নির্বিচারে নির্ভুলতা |
| **ইউনিট** | পরীক্ষা |
---

## আনুষ্ঠানিক পদ্ধতি
| টুল | উদ্দেশ্য |
|------|---------|
| **Coq** | প্রমাণ সহকারী (OCaml-লিখিত) |
| **কেন3** | প্রোগ্রাম যাচাইকরণ |
| **Alt-Ergo** | SMT সমাধানকারী |
| **OCaml + প্রমাণ** | যাচাইকৃত প্রোগ্রাম |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **ভিএস কোড + ocaml-প্ল্যাটফর্ম** | সেরা OCaml LSP |
| **Emacs + tuareg + merlin** | ক্লাসিক OCaml পরিবেশ |
| **ভিম + মারলিন** | ভিম ইন্টিগ্রেশন |
| **নিওভিম + ocaml-lsp** | টার্মিনাল ভিত্তিক |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **নেটিভ বাইনারি** | `dune build`নেটিভ বাইনারি তৈরি করে |
| **স্ট্যাটিক লিঙ্কিং** | সম্পূর্ণরূপে স্ট্যাটিক বাইনারি |
| **ডকার** | কন্টেইনারাইজড |
| **ওপাম সুইচ** | একাধিক OCaml সংস্করণ |
| **ক্রস-কম্পাইল** | ক্রস-সংকলন |
---

## সারাংশ
OCaml এর ইকোসিস্টেম সঠিকতা, কর্মক্ষমতা এবং কার্যকরী প্রোগ্রামিং এর উপর কেন্দ্রীভূত। স্ট্যান্ডার্ড স্ট্যাক হল: **Ocaml 5** রানটাইম হিসাবে, **Dune** বিল্ডের জন্য, **opam** প্যাকেজের জন্য, **Dream** বা **Cohttp** ওয়েবের জন্য, **Caqti** ডেটাবেসের জন্য, **Alcotest** পরীক্ষার জন্য, **ocamlformat** ফরম্যাট করার জন্য, এবং ID সমর্থনের জন্য **Merlin**। OCaml কম্পাইলার, আনুষ্ঠানিক যাচাইকরণ, আর্থিক ব্যবস্থা এবং যেকোন জায়গায় সঠিকতা এবং কার্যকারিতা বিষয়ক দক্ষতা অর্জন করে। OCaml 5 এর ইফেক্ট সিস্টেম এবং সমান্তরালতা (ডোমেন) ভাষাতে আধুনিক সঙ্গতি নিয়ে আসে। কম্পাইলার (Coq, F*), থিওরেম প্রোভারস এবং উচ্চ-আশ্বাস সফ্টওয়্যার তৈরির জন্য ইকোসিস্টেম অপরিহার্য।