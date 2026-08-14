<!--
---
# Metadata
title: "Dart — Version History & Evolution"
description: "Comprehensive version history and evolution of Dart from 1.0 to modern Dart."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [dart, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Dart — バージョンの歴史と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| 1.0 | 2013年 |初期リリース (Google、Lars Bak、Kasper Lund) |
| 1.2 | 2014年 | Dart2JS コンパイラの改善 |
| 1.3 | 2014年 | `async`/`await`サポート |
| 1.4 | 2014年 | `enum`、ミックスインの改善 |
| 1.5 | 2014年 |ジェネレーター (`sync*`、`async*`) |
| 1.6 | 2014年 | `Future`の改善 |
| 1.8 | 2014年 | `dart:io`の改善 |
| 1.9 | 2015年 |強力モード (オプトイン) |
| 1.11 | 2015年 | `Future.then`の改善 |
| 1.12 | 2015年 | **強力モード** が適用されました |
| 2.0 | 2018年 | **主な**: サウンド タイプ システム、`null` の安全準備、コレクションの書き換え |
| 2.1 | 2018年 | `int`/`double`統合、`await for` |
| 2.2 | 2019年 | `Set`リテラル、`const` コレクションの改善 |
| 2.3 | 2019年 |コレクション`if`、コレクション`for`、スプレッド演算子`...`|
| 2.6 | 2019年 |拡張メソッド |
| 2.7 | 2020年 |デフォルトの名前付きパラメータ |
| 2.10 | 2020年 | **サウンド ヌル セーフティ** (オプトイン) |
| 2.12 | 2021年 | **デフォルトでヌル安全性が有効になっています** |
| 2.13 | 2021年 |コンストラクターのティアオフ |
| 2.14 | 2021年 | `late`の改善、符号なし整数 |
| 2.15 | 2021年 |コンストラクターは安定した汎用関数型を切り離します。
| 2.17 | 2022年 | **スーパー パラメーター**、強化された列挙型 |
| 2.18 | 2022年 |強化された型推論 |
| 2.19 | 2023年 |レコードとパターン (プレビュー) |
| 3.0 | 2023年 | **主要**: レコード、パターン、クラス修飾子、`switch` 式 |
| 3.1 | 2023年 |パターンの改善、シールされたクラス |
| 3.2 | 2023年 |静的解析の改善 |
| 3.3 | 2024年 |拡張子の種類、`switch` 式の改善 |
| 3.4 | 2024年 | `if`要素、`case` の改善 |
| 3.5 | 2024年 |マクロ (プレビュー)、言語のさらなる改良 |
| 3.6 | 2025年 |進行中の開発 |
## 主要なマイルストーン
### Dart 1.x — 初期 (2013 ～ 2017)
- **2013**: Google、構造化 Web プログラミング用に設計された Dart をリリース
- **目標**: Web 開発のために JavaScript を置き換える (野心は後に方向転換)
- **1.0**: クラス、インターフェイス、アイソレート、オプションの型指定
- **1.3**:`async`/`await`のサポート
- **1.9**: 強力モード (厳密な型指定をオプトイン)
- Dart VM は Chromium で短期間使用され、その後削除されました
### フラッター ピボット (2017–2018)
- **2017**: Flutter フレームワークが発表 — Dart が UI 言語になる
- Dart はその目的を見つけました: クロスプラットフォームのモバイル/デスクトップ/Web 開発
- **2.0 (2018)**: 完全な書き直し — サウンド タイプ システム、最新のコレクション
### Dart 2.x — モダンダーツ (2018–2023)
- **2.0**: サウンド タイプ システム、デフォルトでは`dynamic`はなくなりました
- **2.3**: コレクション`if`/`for`、スプレッド演算子 - Flutter ウィジェット ツリーに最適
- **2.6**: 拡張メソッド
- **2.10**: サウンドヌルセーフティ (オプトイン)
- **2.12**: **デフォルトで Null 安全性が有効になっています** —`?`Null 許容型
- **2.17**: スーパーパラメータ (`super.x`)、強化された列挙型
### Dart 3.x — レコードとパターン (2023–現在)
- **3.0 (2023)**: **レコード** (匿名データキャリア)、**パターン** (構造化)、**クラス修飾子** (`sealed`、`final`、`interface`、`base`)、`switch`式
- **3.3 (2024)**: 拡張タイプ (ゼロコスト ラッパー)
- **3.5 (2024)**: マクロ プレビュー — コンパイル時のメタプログラミング
## 構文の進化
```dart
// Dart 1.x: Verbose, JavaScript-like
class Person {
  String name;
  int age;
  Person(this.name, this.age);
}

// Dart 2.0: Sound types
Person createPerson(String name, int age) {
  return Person(name, age);
}

// Dart 2.3: Collection if/for, spread
var widgets = [
  if (showHeader) HeaderWidget(),
  for (var item in items) ItemWidget(item),
  ...otherWidgets,
];

// Dart 2.6: Extension methods
extension StringX on String {
  String get shout => toUpperCase() + '!';
}

// Dart 2.12: Null safety
String? nullable;     // can be null
String nonNullable;   // cannot be null (enforced)

// Dart 2.17: Super parameters, enhanced enums
class NamedPerson extends Person {
  NamedPerson({super.name, super.age});  // pass to super constructor
}

enum Status {
  active('Active'),
  inactive('Inactive');
  final String label;
  const Status(this.label);
}

// Dart 3.0: Records and patterns
(String, int) getNameAndAge() => ('Alice', 30);

sealed class Shape {}
class Circle extends Shape { final double radius; Circle(this.radius); }
class Rect extends Shape { final double w, h; Rect(this.w, this.h); }

String describe(Shape s) => switch (s) {
  Circle(radius: var r) => 'Circle($r)',
  Rect(w: var w, h: var h) => 'Rect(${w}x${h})',
};
```

## 型システムの進化
```
Dart 1.0:  Optional types (annotations only)
Dart 1.9:  Strong mode (opt-in)
Dart 2.0:  Sound type system (enforced)
Dart 2.10: Sound null safety (opt-in)
Dart 2.12: Null safety by default (? nullable, ! assert)
Dart 2.15: Generic function types
Dart 3.0:  Records, sealed classes, patterns, class modifiers
Dart 3.3:  Extension types (zero-cost wrappers)
Dart 3.5:  Macros (compile-time metaprogramming)
```

## 主要な設計原則
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## エコシステムの成長
```
2013: Dart 1.0 released by Google
2015: AngularDart — Google uses Dart internally
2017: Flutter announced — Dart finds its purpose
2018: Dart 2.0 — sound type system
2021: Dart 2.12 — null safety
2022: Flutter 3 — iOS, Android, Web, Desktop, Embedded
2023: Dart 3.0 — records, patterns, sealed classes
2025: Flutter + Dart power apps from BMW, Alibaba, Google Pay, Toyota
       pub.dev hosts 30,000+ packages
       Dart runs on: mobile (Flutter), web (dart2wasm), server (dart:io), embedded
```
