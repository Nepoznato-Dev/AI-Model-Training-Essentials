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
# OCaml — 生態系與工具指南
本指南涵蓋了 OCaml 生態系統中的基本工具、框架和基礎設施。
---

## OCaml 實現
|實施 |筆記|
|----------------|--------|
| **OCaml 5** |當前，具有效果和並行性|
| **OCaml 4.14** |最後 4.x（廣泛使用）|
| **原因** |替代語法 (Facebook) |
| **重寫** | Modern Reason 後繼者 (BuckleScript) |
| **OCaml Native** |編譯為本機程式碼 |
| **js_of_ocaml** |編譯為 JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## 建置工具與套件管理
|工具|目的|
|------|---------|
| **沙丘** |建構系統（標準）|
| **opam** |套件管理器 |
| **ocamlfind** |圖書館查找器 |
| **沙丘專案** |專案配置|
| **esy** |替代套件管理器 |
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **夢想** |全端|現代網路（受 Express 啟發）|
| **Cohttp** | HTTP | HTTP 用戶端/伺服器 |
| **鴉片** |輕量化|類似西納特拉 |
| **奧西根** |全端| Eliom（客戶端-伺服器）|
| **變形** |輕量化|網頁框架|
| **輕重量** |非同步 |協作執行緒 |
| **非同步** |非同步 | Jane Street 的非同步 |
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

## 資料庫
|技術 |類型 |
|------------|------|
| **卡克提** |類型安全資料庫 |
| **PG'OCaml** | PostgreSQL（型別安全）|
| **sqlite3-ocaml** | SQLite 綁定 |
| **mysql-ocaml** | MySQL 綁定 |
| **postgresql-ocaml** | PostgreSQL 綁定 |
| **埃爾明** |類似Git的資料庫|
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

## 測試
|框架|目的|
|------------|---------|
| **酒精測試** |快速、多彩的測試 |
| **OUnit** |單元測試（xUnit 風格）|
| **Q檢查** |基於屬性的測試 |
| **撬棍** |模糊測驗|
| **ppx_expect** |期待測試（簡街）|
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

## 程式碼品質
|工具|目的|
|------|---------|
| **ocaml 格式** |程式碼格式化 |
| **ocp 縮排** |縮排 |
| **ocaml-lsp** |語言伺服器|
| **ppx** |語法擴充 |
| **梅林** | IDE 支援（完成、類型）|
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **核心/基礎** | Jane Street 的標準庫 |
| **標準函式庫** | OCaml 標準函式庫 |
| **結果** |錯誤處理 |
| **容器** |資料結構 |
| **電池** |擴充標準庫 |
| **輕重量** |輕量級線程 |
| **非同步** |非同步程式設計|
| **Eio** |基於效果的 I/O (OCaml 5) |
| **網域名稱** |並行性 (OCaml 5) |
| **ppx_deriving** |匯出函數 |
| **ppx_yojson_conv** | JSON 派生 |
| **yojson** | JSON解析|
| **埃** |解析器組合器 |
| **立柱** |解析器產生器 |
| **ocamlgraph** |圖庫|
| **札里斯** |任意精度|
| **OUnit** |測試|
---

## 形式化方法
|工具|目的|
|------|---------|
| **Coq** |證明助手（OCaml 編寫）|
| **為什麼3** |程式驗證|
| **另類爾格** | SMT 解算器 |
| **OCaml + 證明** |已驗證的程式 |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS Code + ocaml 平台** |最佳 OCaml LSP |
| **Emacs + tuareg + merlin** |經典 OCaml 環境 |
| **Vim + 梅林** | Vim 整合 |
| **Neovim + ocaml-lsp** |基於終端 |
---

## 部署
|方法|筆記|
|--------|--------|
| **本機二進位** |`dune build`生成本機二進位檔案 |
| **靜態連結** |完全靜態的二進位檔案 |
| **碼頭工人** |貨櫃式|
| **opam 開關** |多個 OCaml 版本 |
| **交叉編譯** |交叉編譯 |
---

＃＃ 概括
OCaml 的生態系統以正確性、性能和函數式編程為中心。標準堆疊是：**OCaml 5** 作為運行時、**Dune** 用於建置、**opam** 用於套件、**Dream** 或 **Cohttp** 用於 Web、**Caqti** 用於資料庫、**Alcotest** 用於測試、**ocamlformat** 用於格式化，以及 **Merlin** 用於 IDE 支援。 OCaml 擅長編譯器、形式驗證、財務系統以及任何涉及正確性和效能的領域。 OCaml 5 的效果系統和並行性（域）為該語言帶來了現代並發性。此生態系統對於建立編譯器（Coq、F*）、定理證明器和高保證軟體至關重要。