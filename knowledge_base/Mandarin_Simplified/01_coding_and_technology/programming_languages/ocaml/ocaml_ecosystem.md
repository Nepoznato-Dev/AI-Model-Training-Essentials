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
# OCaml — 生态系统和工具指南
本指南涵盖了 OCaml 生态系统中的基本工具、框架和基础设施。
---

## OCaml 实现
|实施 |笔记|
|----------------|--------|
| **OCaml 5** |当前，具有效果和并行性|
| **OCaml 4.14** |最后 4.x（广泛使用）|
| **原因** |替代语法 (Facebook) |
| **重写** | Modern Reason 后继者 (BuckleScript) |
| **OCaml Native** |编译为本机代码 |
| **js_of_ocaml** |编译为 JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## 构建工具和包管理
|工具|目的|
|------|---------|
| **沙丘** |构建系统（标准）|
| **opam** |包管理器 |
| **ocamlfind** |图书馆查找器 |
| **沙丘项目** |项目配置|
| **esy** |替代包管理器 |
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

## 网络框架
|框架|类型 |最适合 |
|------------|------|----------|
| **梦想** |全栈|现代网络（受 Express 启发）|
| **Cohttp** | HTTP | HTTP 客户端/服务器 |
| **鸦片** |轻量化|类似西纳特拉 |
| **奥西根** |全栈| Eliom（客户端-服务器）|
| **变形** |轻量化|网页框架|
| **轻重量** |异步 |协作线程 |
| **异步** |异步 | Jane Street 的异步 |
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

＃＃ 数据库
|技术 |类型 |
|------------|------|
| **卡克提** |类型安全数据库 |
| **PG'OCaml** | PostgreSQL（类型安全）|
| **sqlite3-ocaml** | SQLite 绑定 |
| **mysql-ocaml** | MySQL 绑定 |
| **postgresql-ocaml** | PostgreSQL 绑定 |
| **埃尔明** |类似Git的数据库|
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

## 测试
|框架|目的|
|------------|---------|
| **酒精测试** |快速、多彩的测试 |
| **OUnit** |单元测试（xUnit 风格）|
| **Q检查** |基于属性的测试 |
| **撬棍** |模糊测试|
| **ppx_expect** |期待测试（简街）|
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

## 代码质量
|工具|目的|
|------|---------|
| **ocaml 格式** |代码格式化 |
| **ocp 缩进** |缩进 |
| **ocaml-lsp** |语言服务器|
| **ppx** |语法扩展 |
| **梅林** | IDE 支持（完成、类型）|
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## 关键库
|图书馆 |目的|
|---------|---------|
| **核心/基础** | Jane Street 的标准库 |
| **标准库** | OCaml 标准库 |
| **结果** |错误处理 |
| **容器** |数据结构 |
| **电池** |扩展标准库 |
| **轻重量** |轻量级线程 |
| **异步** |异步编程|
| **Eio** |基于效果的 I/O (OCaml 5) |
| **域名** |并行性 (OCaml 5) |
| **ppx_deriving** |导出函数 |
| **ppx_yojson_conv** | JSON 派生 |
| **yojson** | JSON解析|
| **埃** |解析器组合器 |
| **立柱** |解析器生成器 |
| **ocamlgraph** |图库|
| **扎里斯** |任意精度|
| **OUnit** |测试|
---

## 形式化方法
|工具|目的|
|------|---------|
| **Coq** |证明助手（OCaml 编写）|
| **为什么3** |程序验证|
| **另类尔格** | SMT 求解器 |
| **OCaml + 证明** |已验证的程序 |
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **VS Code + ocaml 平台** |最佳 OCaml LSP |
| **Emacs + tuareg + merlin** |经典 OCaml 环境 |
| **Vim + 梅林** | Vim 集成 |
| **Neovim + ocaml-lsp** |基于终端 |
---

## 部署
|方法|笔记|
|--------|--------|
| **本机二进制** | `dune build`生成本机二进制文件 |
| **静态链接** |完全静态的二进制文件 |
| **码头工人** |集装箱式|
| **opam 开关** |多个 OCaml 版本 |
| **交叉编译** |交叉编译 |
---

＃＃ 概括
OCaml 的生态系统以正确性、性能和函数式编程为中心。标准堆栈是：**OCaml 5** 作为运行时、**Dune** 用于构建、**opam** 用于包、**Dream** 或 **Cohttp** 用于 Web、**Caqti** 用于数据库、**Alcotest** 用于测试、**ocamlformat** 用于格式化，以及 **Merlin** 用于 IDE 支持。 OCaml 擅长编译器、形式验证、财务系统以及任何涉及正确性和性能的领域。 OCaml 5 的效果系统和并行性（域）为该语言带来了现代并发性。该生态系统对于构建编译器（Coq、F*）、定理证明器和高保证软件至关重要。