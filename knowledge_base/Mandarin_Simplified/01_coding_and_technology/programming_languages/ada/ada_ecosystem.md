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

# Ada — 生态系统和工具指南
本指南涵盖了 Ada 生态系统中的基本工具、库和基础设施。
---

## 编译器和实现
|编译器|类型 |笔记|
|----------|------|--------|
| **蚊虫** |开源|基于GCC，应用最广泛|
| **GNAT 社区** |免费| AdaCore 的免费版 |
| **GNAT Pro** |商业|安全认证，AdaCore |
| **对象Ada** |商业|窗户，安全关键 |
| **杰纳斯/艾达** |商业|嵌入式系统|
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## 构建系统和包管理
|工具|目的|
|------|---------|
| **阿里尔** |现代包管理器（推荐） |
| **GPR 构建** |项目构建工具 |
| **GPR（GNAT 项目）** |项目文件格式 |
| **制作** |经典构建 |
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

## 安全与验证
|工具|目的|
|------|---------|
| **GNAT证明** |形式验证|
| **火花** |安全关键子集 |
| **代码对等** |静态分析|
| **多空间** |运行时验证 |
| **覆盖率** |静态分析|
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

## 测试
|框架|目的|
|------------|---------|
| **A 单位** |单元测试框架|
| **阿文** |简单测试 |
| **GNAT测试** |基于代码的测试 |
| **gprbuild** |构建和测试 |
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

## 关键库
|图书馆 |目的|
|---------|---------|
| **Ada.Containers** |矢量、地图、集合 |
| **Ada.Strings** |字符串处理 |
| **Ada.Text_IO** |控制台 I/O |
| **Ada.日历** |日期/时间 |
| **GNATcoll** | GNAT 实用程序 |
| **AWS** | Ada 网络服务器 |
| **XML/Ada** | XML解析|
| **GID** |图像解码|
| **SDLAda** | SDL2 绑定 |
| **GLFW** | OpenGL 窗口 |
| **Cortex GNAT 运行时** |嵌入式（ARM）|
---

## 并发
|特色 |目的|
|---------|---------|
| **任务** |并发线程 |
| **受保护的对象** |同步数据 |
| **选择语句** |约会 |
| **入场电话** |同步|
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

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **GPS（GNAT 编程工作室）** | AdaCore 的 IDE |
| **VS 代码 + Ada** | Ada 语言支持 |
| **Emacs + ada 模式** |经典 Ada 环境 |
---

## 部署
|方法|笔记|
|--------|--------|
| **静态二进制** | GNAT 生成静态二进制文件 |
| **交叉编译** | GNAT交叉编译|
| **嵌入式** |裸机、RTOS (Ravenscar) |
| **码头工人** |集装箱式|
| **安全认证** | DO-178C、IEC 61508、通用标准 |
---

＃＃ 概括
Ada 的生态系统专为安全关键和高可靠性系统而构建。标准工具链是：用于编译的 **GNAT**（基于 GCC）、用于包管理的 **Alire**、用于构建的 **GPRbuild**、用于形式验证的 **GNATprove** 和 **SPARK** 以及用于测试的 **AUnit**。 Ada 在航空航天 (DO-178C)、国防、铁路、医疗设备以及任何正确性至关重要的领域表现出色。 Ada 的优势是强类型、并发性（任务、受保护对象）、形式验证（SPARK）和安全认证。该生态系统对于安全关键型嵌入式系统至关重要。