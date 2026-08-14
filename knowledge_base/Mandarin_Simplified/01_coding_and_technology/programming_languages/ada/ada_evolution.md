<!--
---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ada, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Ada — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
|艾达 83 | 1983 | **第一个标准** (MIL-STD-1815A) — 以 Ada Lovelace 命名 |
|艾达 87 | 1987 |小修改（精确性、可访问性规则）|
|艾达 95 | 1995 | **主要**：OOP（标记类型）、受保护对象、任务改进 |
|艾达 2005 | 2005 | **接口**、匿名访问类型、`for` /`while`循环改进 |
|艾达 2012 | 2012 | **面向方面的编程**、契约（前置/后置条件）、`iterator` |
|艾达 2022 | 2022 | 2022 **`with ghost`**，并行构造，实时改进 |
## 主要里程碑
### 艾达 83 — 诞生 (1983)
- **1983**：美国国防部强制要求嵌入式系统使用单一语言
- Jean Ichbiah 在 CII Honeywell Bull（法国）领导设计
- 以第一位计算机程序员艾达·洛夫莱斯 (Ada Lovelace) 的名字命名
- 主要功能：强类型、包、任务（并发）、泛型、异常
- **目标**：安全关键系统——航空、国防、航天
### Ada 95 — 面向对象的 Ada (1995)
- **第一个 ISO 标准化的 OO 语言**（在 Java 标准化之前）
- 标记类型（类）、类范围类型、动态调度
- 受保护的对象（安全并发数据访问）
- 子包（分层库）
- 基于编译指示的配置
### Ada 2005 — 改进 (2005)
- 接口（接口的多重继承）
- 匿名访问类型（简化指针）
-`for`循环改进
- 容器库（双向链表、向量、地图）
- 扩展`return`声明
### Ada 2012 — 合同与方面 (2012)
- **面向方面的编程**：附加到声明的`aspect`子句
- **合约**：`Pre`、`Post`、`Type_Invariant`— 内置形式验证
- 迭代器支持（`for X of Container loop`）
-`overriding`指示器
- 表达式函数：`function F(X: Integer) return Integer is (X * 2);`
### 艾达 2022 — 平行与幽灵 (2022)
- **`with ghost`**：用于验证的 Ghost 代码（在生产中编译）
- **并行构造**：`parallel` 循环、`parallel` 块
- 实时改进
- 容器改进
-`Iterator`方面改进
## 语法演变
```ada
-- Ada 83: Package-based design
package Stack is
   procedure Push(Item : in Integer);
   function Pop return Integer;
   Stack_Empty : exception;
end Stack;

package body Stack is
   Max : constant := 100;
   Data : array(1..Max) of Integer;
   Top : Integer range 0..Max := 0;

   procedure Push(Item : in Integer) is
   begin
      Top := Top + 1;
      Data(Top) := Item;
   end Push;

   function Pop return Integer is
      Result : Integer;
   begin
      if Top = 0 then raise Stack_Empty; end if;
      Result := Data(Top);
      Top := Top - 1;
      return Result;
   end Pop;
end Stack;

-- Ada 95: Object-oriented
type Shape is tagged record
   X, Y : Float;
end record;

function Area(S : Shape) return Float is
begin
   return 0.0;
end Area;

type Circle is new Shape with record
   Radius : Float;
end record;

function Area(C : Circle) return Float is
begin
   return 3.14159 * C.Radius ** 2;
end Area;

-- Ada 2012: Contracts and aspects
type Temperature is new Float
   with Dynamic_Predicate => Temperature >= -273.15;

procedure Set_Temp(T : in out Temperature)
   with Pre  => T >= -273.15,
        Post => T'Old < T;  -- temperature must increase

-- Expression functions (Ada 2012)
function Double(X : Integer) return Integer is (X * 2);

-- Ada 2022: Parallel constructs
parallel
   for I in Data'Range loop
      Data(I) := Compute(I);
   end loop;

-- Ada 2022: Ghost code for verification
procedure Process(X : in out Integer)
   with Ghost => True,
        Pre   => X > 0,
        Post  => X > X'Old;
```

## 功能演变
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## 关键设计原则
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## 生态系统增长
```
1983: Ada 83 — DoD mandate, defense/aviation adoption
1987: Ada 87 — minor fixes
1995: Ada 95 — OOP, ISO standard
1995: GNAT (GNU NYU Ada Translator) — open source compiler
2005: Ada 2005 — interfaces, containers
2012: Ada 2012 — contracts, aspects
2015: SPARK 2014 — formal verification for Ada
2022: Ada 2022 — parallel, ghost code
2025: Ada used in: aviation (DO-178C), space (ESA), rail, defense
       Compilers: GNAT (open source), ObjectAda, AdaCore tools
       SPARK subset used for formal verification of critical code
```
