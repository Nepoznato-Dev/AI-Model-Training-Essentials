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
# PHP — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| PHP/FI | 1995 |個人首頁工具 (Rasmus Lerdorf) |
| PHP 3.0 | PHP 3.0 1998 |第一個現代 PHP； Zeev Suraski 和 Andi Gutmans 重寫 |
| PHP 4.0 | PHP 4.0 2000 | 2000 Zend 引擎、會話支援、輸出緩衝 |
| PHP 5.0 | PHP 5.0 2004 | **OOP 模型**、PDO、SQLite、SOAP、迭代器 |
| PHP 5.1 | PHP 5.1 2005 | PDO擴展，效能改進|
| PHP 5.2 | PHP 5.2 2006 |`json_encode`/`json_decode`、`filter`擴充 |
| PHP 5.3 | PHP 5.3 2009 | **命名空間**、後期靜態綁定、閉包 |
| PHP 5.4 | PHP 5.4 2012 |短數組語法`[]`、特徵、內建 Web 伺服器 |
| PHP 5.5 | PHP 5.5 2013 |生成器、`yield` 、物件上的 `list()`、`::class` |
| PHP 5.6 | PHP 5.6 2014年|可變參數函數、常數標量表達式 |
| PHP 7.0 | PHP 7.0 2015 | 2015 **主要**：Zend Engine 3、標量類型提示、回傳類型、`??` |
| PHP 7.1 | PHP 7.1 2016 | 2016可空型別、`void` 回傳、可迭代、類別常數可見性 |
| PHP 7.2 | PHP 7.2 2017 | 2017`object`類型提示，參數類型加寬 |
| PHP 7.3 | PHP 7.3 2018 |函式呼叫中的尾隨逗號，`JsonException` |
| PHP 7.4 | PHP 7.4 2019 | 2019 **類型化屬性**、箭頭函數、空合併賦值 |
| PHP 8.0 | PHP 8.0 2020 | **主要**：JIT、命名參數、匹配表達式、聯合類型、屬性 |
| PHP 8.1 | PHP 8.1 2021 |枚舉、纖維、`readonly` 屬性、交集型 |
| PHP 8.2 | PHP 8.2 2022 | 2022`readonly`類別、DNF 型別、`null` /`false`/`true`作為獨立型別 |
| PHP 8.3 | PHP 8.3 2023 |型別類別常數、`#[\Override]` 屬性、`json_validate` |
| PHP 8.4 | PHP 8.4 2024 | 2024屬性掛鉤、`#[\Deprecated]` 屬性、不對稱可見性 |
## 主要里程碑
### PHP/FI 和 PHP 3 (1995–1999)
- **1995**：Rasmus Lerdorf 發布“個人主頁工具”
- **1998**：PHP 3 — 由 Suraski 和 Gutmans 完全重寫；成為一種腳本語言
- 主要功能：嵌入 HTML、表單處理、資料庫支持
### PHP 4 — Zend 引擎 (2000–2004)
- **Zend Engine 1**：編譯字節碼，速度更快
- 会话处理、输出缓冲、PEAR
- 第一个真正的Web开发框架时代
### PHP 5 — 物件導向的 PHP (2004–2014)
- **5.0**：完整的 OOP 重寫 — 類別、介面、異常、PDO
- **5.3**：命名空間（對於現代 PHP 至關重要）、閉包、後期靜態綁定
- **5.4**：特徵，短數組語法`[]`，內建 Web 伺服器
- **5.5**：生成器 (`yield`)、`finally`
### PHP 7 — 效能革命（2015-2019）
- **7.0**：Zend Engine 3 — **速度提高 2 倍**、標量類型聲明、返回類型聲明
- **7.1**：可為 Null 類型 (`?int`)，void 傳回類型
- **7.4**：類型化屬性，箭頭函數`fn() =>`，空合併賦值 `??=`
### PHP 8 — 現代 PHP（2020 年至今）
- **8.0**：JIT 編譯器、命名參數、匹配表達式、聯合型別、屬性 (`#[...]`)、空安全運算子 `?->`
- **8.1**：枚舉、纖程（輕量級並發）、唯讀屬性、交集類型
- **8.2**：唯讀類別、DNF 型別、`null` /`false`/`true`作為獨立型別類型
- **8.3**：類型化類別常數，`#[\Override]`， `json_validate()`
- **8.4**：屬性掛鉤，`#[\Deprecated]`，不對稱可見性
## 類型系統的演變
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

## 語法演變
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

## 關鍵設計原則
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## 生態系成長
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
