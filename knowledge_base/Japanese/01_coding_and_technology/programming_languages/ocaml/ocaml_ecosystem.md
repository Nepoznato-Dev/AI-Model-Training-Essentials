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
# OCaml — エコシステムとツールのガイド
このガイドでは、OCaml エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## OCaml の実装
|実装 |メモ |
|---------------|------|
| **OCaml 5** |現在、効果と並列処理を伴う |
| **OCaml 4.14** |最新の 4.x (広く使用されている) |
| **理由** |代替構文 (Facebook) |
| **再スクリプト** | Modern Reason の後継 (BuckleScript) |
| **OCaml ネイティブ** |ネイティブ コードにコンパイルされる |
| **js_of_ocaml** | JavaScript にコンパイルする |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## ビルドツールとパッケージ管理
|ツール |目的 |
|-----|----------|
| **砂丘** |ビルドシステム（標準） |
| **オパム** |パッケージマネージャー |
| **オカムファインド** |ライブラリファインダー |
| **砂丘プロジェクト** |プロジェクト構成 |
| **難しい** |代替パッケージマネージャー |
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

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **夢** |フルスタック |最新の Web (Express からインスピレーションを得た) |
| **共同http** | HTTP | HTTP クライアント/サーバー |
| **アヘン** |軽量 |シナトラっぽい |
| **オシジェン** |フルスタック | Eliom (クライアントサーバー) |
| **モーフ** |軽量 |ウェブフレームワーク |
| **軽度** |非同期 |連携スレッド |
| **非同期** |非同期 | Jane Street の非同期 |
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

## データベース
|テクノロジー |タイプ |
|-----------|------|
| **カクティ** |タイプセーフなデータベース |
| **PG'OCaml** | PostgreSQL (タイプセーフ) |
| **sqlite3-ocaml** | SQLite バインディング |
| **mysql-ocaml** | MySQL バインディング |
| **postgresql-ocaml** | PostgreSQL バインディング |
| **イルミン** | Git のようなデータベース |
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

## テスト
|フレームワーク |目的 |
|----------|----------|
| **アルコテスト** |高速でカラフルなテスト |
| **ユニット** |単体テスト (xUnit スタイル) |
| **Qチェック** |プロパティベースのテスト |
| **クローバー** |ファズテスト |
| **ppx_expect** |テストを期待する (ジェーン・ストリート) |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **ocaml形式** |コードのフォーマット |
| **ocp-インデント** |インデント |
| **ocaml-lsp** |言語サーバー |
| **ppx** |構文拡張 |
| **マーリン** | IDE サポート (補完、タイプ) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **コア/ベース** | Jane Street の標準ライブラリ |
| **標準ライブラリ** | OCaml標準ライブラリ |
| **結果** |エラー処理 |
| **コンテナ** |データ構造 |
| **バッテリー** |拡張標準ライブラリ |
| **軽度** |軽量スレッド |
| **非同期** |非同期プログラミング |
| **エイオ** |エフェクトベースの I/O (OCaml 5) |
| **ドメイン** |並列処理 (OCaml 5) |
| **ppx_deriving** |派生関数 |
| **ppx_yojson_conv** | JSON の導出 |
| **ヨジソン** | JSON 解析 |
| **オングストローム** |パーサーコンビネータ |
| **メンヒル** |パーサージェネレーター |
| **オカマルグラフ** |グラフライブラリ |
| **ザリス** |任意の精度 |
| **ユニット** |テスト |
---

## 形式的なメソッド
|ツール |目的 |
|-----|----------|
| **コック** |校正アシスタント (OCaml で作成) |
| **なぜ 3** |プログラムの検証 |
| **アルトエルゴ** | SMTソルバー |
| **OCaml + プルーフ** |検証済みプログラム |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + ocaml プラットフォーム** |ベスト OCaml LSP |
| **Emacs + トゥアレグ + マーリン** |クラシック OCaml 環境 |
| **ヴィム + マーリン** | Vim の統合 |
| **Neovim + ocaml-lsp** |ターミナルベース |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **ネイティブバイナリ** | `dune build`はネイティブ バイナリを生成します。
| **静的リンク** |完全に静的なバイナリ |
| **ドッカー** |コンテナ化 |
| **OPAM スイッチ** |複数の OCaml バージョン |
| **クロスコンパイル** |クロスコンパイル |
---

＃＃ まとめ
OCaml のエコシステムは、正確性、パフォーマンス、関数型プログラミングを中心としています。標準スタックは、ランタイムとして **OCaml 5**、ビルドに **Dune**、パッケージに **opam**、Web に **Dream** または **Cohttp**、データベースに **Caqti**、テストに **Alcotest**、フォーマットに**ocamlformat**、IDE サポートに **Merlin** です。 OCaml は、コンパイラ、形式的検証、金融システムなど、正確性とパフォーマンスが重要なあらゆる分野で優れています。 OCaml 5 のエフェクト システムと並列処理 (ドメイン) は、言語に最新の同時実行性をもたらします。エコシステムは、コンパイラー (Coq、F*)、定理証明者、および高保証ソフトウェアを構築するために不可欠です。