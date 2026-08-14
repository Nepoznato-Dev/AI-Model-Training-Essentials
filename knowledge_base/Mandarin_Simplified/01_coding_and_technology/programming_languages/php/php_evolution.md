---
# Metadata
title: "PHP — Version History & Evolution"
description: "Comprehensive version history and evolution of PHP from 1.0 to modern PHP."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# PHP — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| PHP/FI | 1995 |个人主页工具 (Rasmus Lerdorf) |
| PHP 3.0 | PHP 3.0 1998 |第一个现代 PHP； Zeev Suraski 和 Andi Gutmans 重写 |
| PHP 4.0 | PHP 4.0 2000 | 2000 Zend 引擎、会话支持、输出缓冲 |
| PHP 5.0 | PHP 5.0 2004 | **OOP 模型**、PDO、SQLite、SOAP、迭代器 |
| PHP 5.1 | PHP 5.1 2005 | PDO扩展，性能改进|
| PHP 5.2 | PHP 5.2 2006 | `json_encode`/`json_decode`、`filter`扩展 |
| PHP 5.3 | PHP 5.3 2009 | **命名空间**、后期静态绑定、闭包 |
| PHP 5.4 | PHP 5.4 2012 |短数组语法`[]`、特征、内置 Web 服务器 |
| PHP 5.5 | PHP 5.5 2013 |生成器、`yield` 、对象上的 `list()`、`::class` |
| PHP 5.6 | PHP 5.6 2014年|可变参数函数、常量标量表达式 |
| PHP 7.0 | PHP 7.0 2015 | 2015 **主要**：Zend Engine 3、标量类型提示、返回类型、`??` |
| PHP 7.1 | PHP 7.1 2016 | 2016可空类型、`void` 返回、可迭代、类常量可见性 |
| PHP 7.2 | PHP 7.2 2017 | 2017 `object`类型提示，参数类型加宽 |
| PHP 7.3 | PHP 7.3 2018 |函数调用中的尾随逗号，`JsonException` |
| PHP 7.4 | PHP 7.4 2019 | 2019 **类型化属性**、箭头函数、空合并赋值 |
| PHP 8.0 | PHP 8.0 2020 | **主要**：JIT、命名参数、匹配表达式、联合类型、属性 |
| PHP 8.1 | PHP 8.1 2021 |枚举、纤维、`readonly` 属性、交集类型 |
| PHP 8.2 | PHP 8.2 2022 | 2022 `readonly`类别、DNF 类型、`null` /`false`/`true`作为独立类型 |
| PHP 8.3 | PHP 8.3 2023 |类型化类常量、`#[\Override]` 属性、`json_validate` |
| PHP 8.4 | PHP 8.4 2024 | 2024属性挂钩、`#[\Deprecated]` 属性、不对称可见性 |
## 主要里程碑
### PHP/FI 和 PHP 3 (1995–1999)
- **1995**：Rasmus Lerdorf 发布“个人主页工具”
- **1998**：PHP 3 — 由 Suraski 和 Gutmans 完全重写；成为一种脚本语言
- 主要功能：嵌入 HTML、表单处理、数据库支持
### PHP 4 — Zend 引擎 (2000–2004)
- **Zend Engine 1**：编译字节码，速度更快
- 会话处理、输出缓冲、PEAR
- 第一个真正的Web开发框架时代
### PHP 5 — 面向对象的 PHP (2004–2014)
- **5.0**：完整的 OOP 重写 — 类、接口、异常、PDO
- **5.3**：命名空间（对于现代 PHP 至关重要）、闭包、后期静态绑定
- **5.4**：特征，短数组语法`[]`，内置 Web 服务器
- **5.5**：生成器 (`yield`)、`finally`
### PHP 7 — 性能革命（2015-2019）
- **7.0**：Zend Engine 3 — **速度提高 2 倍**、标量类型声明、返回类型声明
- **7.1**：可为 Null 类型 (`?int`)，void 返回类型
- **7.4**：类型化属性，箭头函数`fn() =>`，空合并赋值 `??=`
### PHP 8 — 现代 PHP（2020 年至今）
- **8.0**：JIT 编译器、命名参数、匹配表达式、联合类型、属性 (`#[...]`)、空安全运算符`?->`
- **8.1**：枚举、纤程（轻量级并发）、只读属性、交集类型
- **8.2**：只读类、DNF 类型、`null` /`false`/`true`作为独立类型
- **8.3**：类型化类常量，`#[\Override]`，`json_validate()`
- **8.4**：属性挂钩，`#[\Deprecated]`，不对称可见性
## 类型系统的演变
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

## 语法演变
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

## 关键设计原则
```
1. "Pragmatic" — solve real web problems
2. "Progressive enhancement" — easy to start, deep to master
3. "Backward compatibility" — old code keeps working
4. "Batteries included" — extensive standard library
5. "Community-driven" — RFC process for language changes
6. "Performance matters" — PHP 7/8 focus on speed
```

## 生态系统增长
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
