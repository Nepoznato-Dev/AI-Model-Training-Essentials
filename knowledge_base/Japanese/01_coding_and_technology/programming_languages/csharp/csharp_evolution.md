---
# Metadata
title: "C# — Version History & Evolution"
description: "Comprehensive version history and evolution of C# from 1.0 to modern C#."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [csharp, dotnet, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# C# — バージョン履歴と進化
## タイムライン
|バージョン |年 | .NET |主要テーマ |
|----------|------|------|-----------|
| 1.0 | 2002年 | 1.0 |クラス、インターフェイス、デリゲート、イベント |
| 1.2 | 2003年 | 1.1 | `foreach`と`IDisposable`|
| 2.0 | 2005年 | 2.0 | **ジェネリック**、null許容型、匿名メソッド、イテレータ |
| 3.0 | 2007年 | 3.5 | **LINQ**、ラムダ式、拡張メソッド、`var`、匿名型 |
| 4.0 | 2010年 | 4.0 | `dynamic`、名前付き/オプションの引数、`Tuple<T>` |
| 5.0 | 2012年 | 4.5 | **`async/await`** |
| 6.0 | 2015年 | 4.6 | Null 条件付き`?.`、文字列補間、式本体のメンバー |
| 7.0 | 2017年 |コア2.0 |タプル、分解、パターン マッチング、`out var`、 ref は | を返します。
| 7.3 | 2018年 |コア2.1 |  式の`Span<T>`、`stackalloc`|
| 8.0 | 2019年 |コア3.0 | **NULL 許容参照型**、スイッチ式、範囲`..`|
| 9.0 | 2020年 | 5.0 | **`record`**、`init` プロパティ、パターン マッチングの改善 |
| 10.0 | 2021年 | 6.0 | **`record struct`**、グローバルな使用法、ファイル スコープの名前空間、ラムダの改善 |
| 11.0 | 2022年 | 7.0 | **`required`**、`raw string literals`、`file` タイプ、`ref` フィールド |
| 12.0 | 2023年 | 8.0 | **プライマリ コンストラクター**、コレクション式`[]`、インライン配列 |
| 13.0 | 2024年 | 9.0 | `params`コレクション、新しい`Lock<T>`、`field`キーワード |
## 主要なマイルストーン
### 初期の C# (2002 ～ 2007)
- **1.0 (2002)**: .NET 上のマネージ コード。ガベージコレクション。プロパティ、イベント、デリゲート
- **2.0 (2005)**: ジェネリック —`List<T>`、`Dictionary<K,V>`; null 許容型`int?`;イテレータ`yield return`
- **3.0 (2007)**: LINQ — クエリ構文、ラムダ式、拡張メソッド、`var`、匿名型、式ツリー
### 現代 (2012–2017)
- **5.0 (2012)**:`async/await`— 非同期プログラミング革命
- **6.0 (2015)**: Null 条件付き`?.`、文字列補間`$""`、自動プロパティ初期化子
- **7.0 (2017)**: タプル`(int, string)`、パターン マッチング、`out var`、ローカル関数
### 急速な進化 (2019–現在)
- **8.0 (2019)**: Null 許容参照型 — コンパイル時の null 安全性
- **9.0 (2020)**:`record`タイプ — 不変のデータ キャリア
- **10.0 (2021)**:`record struct`、グローバルな使用法、ファイル スコープの名前空間
- **11.0 (2022)**:`required`キーワード、生の文字列リテラル`"""..."""`
- **12.0 (2023)**: すべてのクラスのプライマリ コンストラクター、コレクション式`[1, 2, 3]`
- **13.0 (2024)**: 任意のコレクション タイプの `params`
## 機能の進化
```
Null Safety:
  2002: Reference types always nullable
  2005: Nullable value types (int?)
  2019: Nullable reference types (string?)
  2022: Required members

Pattern Matching:
  2017: Basic type/is patterns
  2019: Switch expressions, property patterns
  2020: Relational patterns, combinator patterns
  2021: List patterns, type patterns

Async:
  2012: async/await (Task-based)
  2017: async Main, async streams (IAsyncEnumerable)
  2020: Top-level statements
  2023: async disposables

Data Types:
  2002: Classes, structs, enums
  2005: Generics
  2020: record (class)
  2021: record struct
  2023: Primary constructors for all types
```

## .NET プラットフォームの進化
```
2002: .NET Framework 1.0 (Windows only)
2005: .NET Framework 2.0 (generics)
2012: .NET Framework 4.5 (async)
2016: .NET Core 1.0 (cross-platform!)
2019: .NET Core 3.0 (Windows desktop)
2020: .NET 5 (unified platform)
2021: .NET 6 (LTS, minimal APIs)
2022: .NET 7 (performance)
2023: .NET 8 (LTS, native AOT)
2024: .NET 9 (performance, hybridization)
2025: .NET 10 (LTS expected)
```

## 言語設計の哲学
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## エコシステムの成長
```
2002: .NET Framework, Windows Forms, ASP.NET Web Forms
2005: LINQ, Entity Framework
2010: MVVM, WPF, Silverlight
2016: .NET Core — cross-platform
2018: Blazor — C# in the browser (WebAssembly)
2020: .NET 5 — unified platform
2023: .NET 8 — native AOT, minimal APIs
2025: C# — top 5 most used language; dominant in enterprise, games (Unity), cloud (Azure)
```
