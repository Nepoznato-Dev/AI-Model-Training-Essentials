---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Ada — バージョンの歴史と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|エイダ83 | 1983年 | **最初の規格** (MIL-STD-1815A) — エイダ・ラブレスにちなんで命名 |
|エイダ87 | 1987年 |マイナーリビジョン (精度、アクセシビリティルール) |
|エイダ95 | 1995年 | **主な**: OOP (タグ付きタイプ)、保護されたオブジェクト、タスクの改善 |
|エイダ 2005 | 2005年 | **インターフェイス**、匿名アクセス タイプ、`for` /`while`ループの改善 |
|エイダ 2012 | 2012年 | **アスペクト指向プログラミング**、コントラクト (事前条件/事後条件)、`iterator` |
|エイダ 2022 | 2022年 | **`with ghost`**、並列構造、リアルタイムの改善 |
## 主要なマイルストーン
### エイダ 83 — 誕生 (1983)
- **1983**: 米国国防総省、組み込みシステムに単一言語を義務付ける
- Jean Ichbiah は CII Honeywell Bull (フランス) でデザインをリードします
- 最初のコンピュータープログラマー、エイダ・ラブレスにちなんで名付けられました
- 主な機能: 強い型指定、パッケージ、タスク (同時実行)、ジェネリック、例外
- **目標**: 安全性が重要なシステム - 航空、防衛、宇宙
### Ada 95 — オブジェクト指向の Ada (1995)
- **最初の ISO 標準化された OO 言語** (Java が標準化される前)
- タグ付き型 (クラス)、クラス全体の型、動的ディスパッチ
- 保護されたオブジェクト (安全な同時データ アクセス)
- 子パッケージ（階層ライブラリ）
- プラグマベースの構成
### Ada 2005 — 改良 (2005)
- インターフェース (インターフェースの多重継承)
- 匿名アクセス タイプ (簡略化されたポインタ)
-`for`ループの改善
- コンテナ ライブラリ (二重リンク リスト、ベクトル、マップ)
- 拡張`return`ステートメント
### Ada 2012 — 契約と側面 (2012)
- **アスペクト指向プログラミング**: 宣言に付けられた`aspect`句
- **契約**:`Pre`、`Post`、`Type_Invariant`— 正式な検証が組み込まれています
- イテレータのサポート (`for X of Container loop`)
- `overriding`インジケーター
- 式関数: `function F(X: Integer) return Integer is (X * 2);`
### エイダ 2022 — パラレル & ゴースト (2022)
- **`with ghost`**: 検証用のゴースト コード (本番環境でコンパイルアウト)
- **並列構造**:`parallel`ループ、`parallel` ブロック
- リアルタイムの改善
- コンテナの改善
-`Iterator`アスペクトの改良
## 構文の進化
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

## 機能の進化
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## 主要な設計原則
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## エコシステムの成長
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
