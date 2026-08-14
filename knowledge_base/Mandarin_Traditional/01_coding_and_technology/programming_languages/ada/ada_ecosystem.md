<!--
---
# Metadata
title: "Ada — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ada ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Ada — 生態系與工具指南
本指南涵蓋了 Ada 生態系統中的基本工具、庫和基礎設施。
---

## 編譯器和實現
|編譯器|類型 |筆記|
|----------|------|--------|
| **蚊蟲** |開源|基於GCC，應用最廣泛|
| **GNAT 社群** |免費| AdaCore 的免費版本 |
| **GNAT Pro** |商業|安全認證，AdaCore |
| **物件Ada** |商業|窗戶，安全關鍵 |
| **傑納斯/艾達** |商業|嵌入式系統|
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## 建置系統與套件管理
|工具|目的|
|------|---------|
| **阿里爾** |現代套件管理器（建議） |
| **GPR 建構** |專案建構工具 |
| **GPR（GNAT 專案）** |專案文件格式 |
| **製作** |經典構建 |
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

## 安全性與驗證
|工具|目的|
|------|---------|
| **GNAT證明** |形式驗證|
| **火花** |安全關鍵子集 |
| **程式碼對等** |靜態分析|
| **多空間** |運行時驗證 |
| **覆蓋率** |靜態分析|
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

## 測試
|框架|目的|
|------------|---------|
| **A 單位** |單元測試框架|
| **阿文** |簡單測試 |
| **GNAT測試** |基於程式碼的測試 |
| **gprbuild** |建置與測試 |
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

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **Ada.Containers** |向量、地圖、集合 |
| **Ada.Strings** |字串處理 |
| **Ada.Text_IO** |控制台 I/O |
| **Ada.日曆** |日期/時間 |
| **GNATcoll** | GNAT 實用程式 |
| **AWS** | Ada 網路伺服器 |
| **XML/Ada** | XML解析|
| **GID** |圖像解碼|
| **SDLAda** | SDL2 綁定 |
| **GLFW** | OpenGL 視窗 |
| **Cortex GNAT 運行時** |嵌入式（ARM）|
---

## 並行
|特色 |目的|
|---------|---------|
| **任務** |並發線程|
| **受保護的物件** |同步資料|
| **選擇語句** |約會|
| **入場電話** |同步|
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

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **GPS（GNAT 程式設計工作室）** | AdaCore 的 IDE |
| **VS 代碼 + Ada** | Ada 語言支援 |
| **Emacs + ada 模式** |經典 Ada 環境 |
---

## 部署
|方法|筆記|
|--------|--------|
| **靜態二進位** | GNAT 產生靜態二進位檔案 |
| **交叉編譯** | GNAT交叉編譯|
| **嵌入式** |裸機、RTOS (Ravenscar) |
| **碼頭工人** |貨櫃式|
| **安全認證** | DO-178C、IEC 61508、通用標準 |
---

＃＃ 概括
Ada 的生態系統專為安全關鍵和高可靠性系統而建置。標準工具鏈是：用於編譯的 **GNAT**（基於 GCC）、用於套件管理的 **Alire**、用於構建的 **GPRbuild**、用於形式驗證的 **GNATprove** 和 **SPARK** 以及用於測試的 **AUnit**。 Ada 在航空航太 (DO-178C)、國防、鐵路、醫療設備以及任何正確性至關重要的領域表現出色。 Ada 的優勢是強型別、並發性（任務、受保護物）、形式驗證（SPARK）和安全認證。此生態系統對於安全關鍵型嵌入式系統至關重要。