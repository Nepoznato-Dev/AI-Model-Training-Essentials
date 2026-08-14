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
# Ada — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|艾達 83 | 1983 | **第一個標準** (MIL-STD-1815A) — 以 Ada Lovelace 命名 |
|艾達 87 | 1987 |小修改（精確性、可訪問性規則）|
|艾達 95 | 1995 | **主要**：OOP（標記類型）、受保護物件、任務改進 |
|艾達 2005 | 2005 | **介面**、匿名存取類型、`for` /`while`循環改進 |
|艾達 2012 | 2012 | **面向方面的程式設計**、契約（前置/後置條件）、`iterator` |
|艾達 2022 | 2022 | 2022 **`with ghost`**，並行構造，即時改進 |
## 主要里程碑
### 艾達 83 — 誕生 (1983)
- **1983**：美國國防部強制要求嵌入式系統使用單一語言
- Jean Ichbiah 在 CII Honeywell Bull（法國）領導設計
- 以第一位電腦程式設計師艾達·洛夫萊斯 (Ada Lovelace) 的名字命名
- 主要功能：強型別、套件、任務（同時）、泛型、異常
- **目標**：安全關鍵系統－航空、國防、航太
### Ada 95 — 物件導向的 Ada (1995)
- **第一個 ISO 標準化的 OO 語言**（在 Java 標準化之前）
- 標記類型（類別）、類別範圍類型、動態調度
- 受保護的物件（安全並發資料存取）
- 子包（分層庫）
- 基於編譯指示的配置
### Ada 2005 — 改進 (2005)
- 介面（介面的多重繼承）
- 匿名存取類型（簡化指標）
-`for`循環改進
- 容器庫（雙向鍊錶、向量、地圖）
- 擴展`return`聲明
### Ada 2012 — 合約與面向 (2012)
- **面向方面的程式設計**：附加到宣告的`aspect`子句
- **合約**：`Pre`、`Post`、`Type_Invariant`— 內建形式驗證
- 迭代器支援（`for X of Container loop`）
-`overriding`指示器
- 表達式函數：`function F(X: Integer) return Integer is (X * 2);`
### 艾达 2022 — 平行与幽灵 (2022)
- **`with ghost`**：用于验证的 Ghost 代码（在生产中编译）
- **并行构造**：`parallel` 循环、`parallel` 块
- 即時改進
- 容器改進
-`Iterator`方面改进
## 語法演變
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

## 功能演變
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## 關鍵設計原則
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## 生態系成長
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
