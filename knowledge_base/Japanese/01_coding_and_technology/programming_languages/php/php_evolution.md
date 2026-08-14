<!--
---
# Metadata
title: "PHP — Version History & Evolution"
description: "Comprehensive version history and evolution of PHP from 1.0 to modern PHP."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [php, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# PHP — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| PHP/FI | 1995年 |個人ホームページ ツール (Rasmus Lerdorf) |
| PHP3.0 | 1998年 |最初の最新の PHP。 Zeev Suraski と Andi Gutmans がリライト |
| PHP4.0 | 2000年 | Zend Engine、セッションサポート、出力バッファリング |
| PHP5.0 | 2004年 | **OOP モデル**、PDO、SQLite、SOAP、イテレータ |
| PHP5.1 | 2005年 | PDO 拡張、パフォーマンスの向上 |
| PHP5.2 | 2006年 | `json_encode`/`json_decode`、`filter`拡張子 |
| PHP5.3 | 2009年 | **名前空間**、遅延静的バインディング、クロージャ |
| PHP5.4 | 2012年 |短い配列構文`[]`、特性、組み込み Web サーバー |
| PHP5.5 | 2013年 |ジェネレーター、オブジェクトの`yield`、 `list()`、`::class` |
| PHP5.6 | 2014年 |可変長関数、定数スカラー式 |
| PHP7.0 | 2015年 | **主要**: Zend Engine 3、スカラー型ヒント、戻り値の型、`??` |
| PHP 7.1 | 2016年 | Null 許容型、`void` 戻り値、反復可能、クラス定数の可視性 |
| PHP 7.2 | 2017年 | `object`型ヒント、パラメータ型の拡張 |
| PHP7.3 | 2018年 |関数呼び出しの末尾のカンマ、`JsonException` |
| PHP 7.4 | 2019年 | **型付きプロパティ**、アロー関数、null 合体割り当て |
| PHP8.0 | 2020年 | **主要**: JIT、名前付き引数、一致式、共用体型、属性 |
| PHP8.1 | 2021年 |列挙型、ファイバー、`readonly` プロパティ、交差タイプ |
| PHP8.2 | 2022年 | `readonly`クラス、DNF タイプ、スタンドアロン タイプとしての`null`/`false`/`true`|
| PHP8.3 | 2023年 |型付きクラス定数、`#[\Override]` 属性、`json_validate` |
| PHP8.4 | 2024年 |プロパティ フック、`#[\Deprecated]` 属性、非対称可視性 |
## 主要なマイルストーン
### PHP/FI および PHP 3 (1995 ～ 1999)
- **1995**: Rasmus Lerdorf が「Personal Home Page Tools」をリリース
- **1998**: PHP 3 — Suraski と Gutmans による完全な書き直し。スクリプト言語になります
- 主な機能: HTML への埋め込み、フォーム処理、データベースのサポート
### PHP 4 — Zend エンジン (2000 ～ 2004)
- **Zend Engine 1**: コンパイルされたバイトコード、はるかに高速
- セッション処理、出力バッファリング、PEAR
- 最初の本格的な Web 開発フレームワーク時代
### PHP 5 — オブジェクト指向 PHP (2004 ～ 2014)
- **5.0**: 完全な OOP 書き換え — クラス、インターフェイス、例外、PDO
- **5.3**: 名前空間 (最新の PHP にとって重要)、クロージャ、後期静的バインディング
- **5.4**: 特性、短い配列構文`[]`、組み込み Web サーバー
- **5.5**: ジェネレーター (`yield`)、`finally`
### PHP 7 — パフォーマンス革命 (2015–2019)
- **7.0**: Zend Engine 3 — **2 倍高速**、スカラー型宣言、戻り値型宣言
- **7.1**: Null 許容型 (`?int`)、戻り値の型が void
- **7.4**: 型付きプロパティ、アロー関数`fn() =>`、null 結合代入 `??=`
### PHP 8 — 最新の PHP (2020–現在)
- **8.0**: JIT コンパイラ、名前付き引数、一致式、共用体型、属性 (`#[...]`)、nullsafe 演算子`?->`
- **8.1**: 列挙型、ファイバー (軽量同時実行)、読み取り専用プロパティ、交差タイプ
- **8.2**: 読み取り専用クラス、DNF タイプ、スタンドアロン タイプとしての`null`/`false`/ `true`
- **8.3**: 型付きクラス定数、`#[\Override]`、`json_validate()`
- **8.4**: プロパティ フック、`#[\Deprecated]`、非対称可視性
## 型システムの進化
```
PHP 4:    No type hints
PHP 5.0:  Class type hints
PHP 5.1:  Array type hint
PHP 7.0:  Scalar types (int, string, float, bool), return types
PHP 7.1:  Nullable types (?int), void, iterable
PHP 7.2:  object type
PHP 7.4:  Typed properties
PHP 8.0:  Union types (int|string), mixed
PHP 8.1:  Intersection types (A&B), never, first-class callable syntax
PHP 8.2:  DNF types ((A&B)|C), null/false/true standalone
PHP 8.3:  Typed class constants
PHP 8.4:  Property hooks (get/set)
```

## 構文の進化
```php
// PHP 3/4: Basic scripting
$users = array(1, 2, 3);

// PHP 5.4: Short array syntax
$users = [1, 2, 3];

// PHP 5.3: Namespaces
namespace App\Models;

// PHP 7.0: Scalar types
function add(int $a, int $b): int { return $a + $b; }

// PHP 7.4: Arrow functions
$doubled = array_map(fn($x) => $x * 2, $numbers);

// PHP 8.0: Named arguments, match
$result = process(value: $input, strict: true);
$label = match($status) { 0 => 'inactive', 1 => 'active', default => 'unknown' };

// PHP 8.1: Enums
enum Status: string { case Active = 'active'; case Inactive = 'inactive'; }

// PHP 8.4: Property hooks
class User {
    public string $name { get => strtoupper($this->name); set; }
}
```

## 主要な設計原則
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## エコシステムの成長
```
1995: PHP/FI — personal tool
2000: PHP 4 + PEAR — package management begins
2004: PHP 5 + OOP — enterprise adoption
2008: Composer (dependency management) — modern PHP ecosystem
2011: Laravel framework — elegant PHP
2015: PHP 7 — performance revolution
2020: PHP 8 — JIT, modern features
2025: PHP powers ~75% of websites with known server-side language
       WordPress, Wikipedia, Slack, Mailchimp all run on PHP
```
