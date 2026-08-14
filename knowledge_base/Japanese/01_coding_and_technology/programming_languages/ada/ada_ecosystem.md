---
# Metadata
title: "Ada — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ada ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ada, ecosystem, tooling, compilers, safety-critical, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ada — エコシステムとツールのガイド
このガイドでは、Ada エコシステムの重要なツール、ライブラリ、インフラストラクチャについて説明します。
---

## コンパイラと実装
|コンパイラ |タイプ |メモ |
|----------|------|----------|
| **GNAT** |オープンソース | GCC ベース、最も広く使用されている |
| **GNAT コミュニティ** |無料 | AdaCore の無料版 |
| **GNAT プロ** |コマーシャル |安全性認定済み、AdaCore |
| **オブジェクトエイダ** |コマーシャル | Windows、安全性が重要 |
| **ヤヌス/エイダ** |コマーシャル |組み込みシステム |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## ビルド システムとパッケージ管理
|ツール |目的 |
|-----|----------|
| **アリレ** |最新のパッケージ マネージャー (推奨) |
| **GPRビルド** |プロジェクト構築ツール |
| **GPR (GNAT プロジェクト)** |プロジェクトファイル形式 |
| **作る** |クラシック ビルド |
```toml
# alire.toml
name = "myapp"
description = "My Ada application"
version = "0.1.0"

[[depends-on]]
gnat = "^13"
gnatcoll = "^24"

[[pins]]
```

```bash
alr init --bin myapp      # create project
alr build                 # build
alr run                   # run
alr get --build gnatcoll  # get dependency
alr search                # search packages
alr index                 # update index
```

```gpr
-- myproject.gpr
project Myproject is
   for Source_Dirs use ("src/**");
   for Object_Dir use "obj";
   for Main use ("main.adb");
   
   package Compiler is
      for Default_Switches ("Ada") use ("-gnatwa", "-gnatVa", "-O2");
   end Compiler;
   
   package Binder is
      for Default_Switches ("Ada") use ("-E");  -- store exceptions
   end Binder;
end Myproject;
```

---

## 安全性と検証
|ツール |目的 |
|-----|----------|
| **GNATprove** |正式な検証 |
| **スパーク** |セーフティクリティカルなサブセット |
| **コードピア** |静的解析 |
| **ポリスペース** |実行時検証 |
| **カバー範囲** |静的解析 |
```ada
-- SPARK example
package Stack with
   SPARK_Mode
is
   type Bounded_Stack (Capacity : Positive) is tagged private;
   
   procedure Push (S : in out Bounded_Stack; Element : Integer)
      with Pre  => not S.Is_Full,
           Post => not S.Is_Empty and S.Top = Element;
   
   function Is_Full (S : Bounded_Stack) return Boolean;
   function Is_Empty (S : Bounded_Stack) return Boolean;
   
private
   type Bounded_Stack (Capacity : Positive) is tagged record
      Data : array (1 .. Capacity) of Integer;
      Top_Index : Natural := 0;
   end record;
end Stack;
```

---

## テスト
|フレームワーク |目的 |
|----------|----------|
| **Aユニット** |単体テストフレームワーク |
| **アーベン** |簡単なテスト |
| **GNATtest** |コードベースのテスト |
| **gprbuild** |ビルドとテスト |
```ada
with AUnit.Simple_Test_Cases;
with AUnit.Test_Suites;
with AUnit.Run;
with AUnit.Reporter.Text;

package Stack_Test is
   type Test_Case is new AUnit.Simple_Test_Cases.Test_Case with null record;
   
   function Name (T : Test_Case) return AUnit.Message_String;
   procedure Run_Test (T : in out Test_Case);
end Stack_Test;

package body Stack_Test is
   function Name (T : Test_Case) return AUnit.Message_String is
   begin
      return new String'("Stack Tests");
   end Name;
   
   procedure Run_Test (T : in out Test_Case) is
      S : Bounded_Stack (10);
   begin
      Push (S, 42);
      AUnit.Assertions.Assert (Top (S) = 42, "Top should be 42");
      AUnit.Assertions.Assert (not Is_Empty (S), "Should not be empty");
   end Run_Test;
end Stack_Test;
```

---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **Ada.コンテナ** |ベクトル、マップ、セット |
| **Ada.Strings** |文字列の処理 |
| **Ada.Text_IO** |コンソール I/O |
| **エイダカレンダー** |日付/時刻 |
| **GNATcoll** | GNAT ユーティリティ |
| **AWS** | Ada Web サーバー |
| **XML/Ada** | XML 解析 |
| **性同一性障害** |画像デコード |
| **SDLAda** | SDL2 バインディング |
| **GLFW** | OpenGL ウィンドウ処理 |
| **Cortex GNAT ランタイム** |組み込み (ARM) |
---

## 同時実行性
|特集 |目的 |
|----------|----------|
| **タスク** |同時スレッド |
| **保護されたオブジェクト** |同期されたデータ |
| **ステートメントを選択** |ランデブー |
| **エントリーコール** |同期 |
```ada
task type Worker is
   entry Do_Work (Item : in Integer);
end Worker;

task body Worker is
   Value : Integer;
begin
   loop
      select
         accept Do_Work (Item : in Integer) do
            Value := Item;
         end Do_Work;
         Process (Value);
      or
         terminate;
      end select;
   end loop;
end Worker;
```

---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **GPS (GNAT プログラミング スタジオ)** | AdaCore の IDE |
| **VS コード + エイダ** | Ada 言語サポート |
| **Emacs + ada-mode** |クラシック Ada 環境 |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **静的バイナリ** | GNAT は静的バイナリを生成します。
| **クロスコンパイル** | GNAT クロスコンパイル |
| **埋め込み** |ベアメタル、RTOS (Ravenscar) |
| **ドッカー** |コンテナ化 |
| **安全認証** | DO-178C、IEC 61508、共通基準 |
---

＃＃ まとめ
Ada のエコシステムは、セーフティ クリティカルで信頼性の高いシステム専用に構築されています。標準ツールチェーンは、コンパイル用の **GNAT** (GCC ベース)、パッケージ管理用の **Alire**、ビルド用の **GPRbuild**、正式な検証用の **GNATprove** および **SPARK**、テスト用の **AUnit** です。 Ada は、航空宇宙 (DO-178C)、防衛、鉄道、医療機器、および正確さが最優先されるあらゆる分野で優れています。 Ada の強みは、強力な型指定、同時実行性 (タスク、保護されたオブジェクト)、形式的検証 (SPARK)、および安全性認証です。エコシステムは、安全性が重要な組み込みシステムにとって不可欠です。