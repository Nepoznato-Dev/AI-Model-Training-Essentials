---
# Metadata
title: "PHP — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in PHP with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [php, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "20 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# PHP — 常见错误和反模式
本文档列出了 PHP 中最常见的错误、陷阱和反模式，并进行了更正。
---

## 1. 松散比较 (`==`) 陷阱
```php
// ❌ WRONG — loose comparison surprises
0 == "foo"       // true (pre-PHP 8)
0 == false        // true
null == false     // true
"" == null        // true
"0" == false      // true
"0" == null       // true (pre-PHP 8)

// ✅ CORRECT — always use strict comparison
0 === "foo"       // false
0 === false       // false
null === false    // false
```

---

## 2. SQL注入
```php
// ❌ WRONG — direct string interpolation
$query = "SELECT * FROM users WHERE id = " . $_GET['id'];
$result = $pdo->query($query);

// ✅ CORRECT — prepared statements
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $_GET['id']]);
```

---

## 3. 不使用类型声明
```php
// ❌ WRONG — no type safety
function add($a, $b) {
    return $a + $b;  // works with strings, arrays, etc.
}

// ✅ CORRECT — use type declarations (PHP 7+)
function add(int $a, int $b): int {
    return $a + $b;
}

// ✅ CORRECT — strict types
declare(strict_types=1);
function add(int $a, int $b): int {
    return $a + $b;
}
```

---

## 4.变量变量和动态访问
```php
// ❌ WRONG — confusing and unsafe
$name = "user";
$$name = "Alice";  // creates $user = "Alice"

// ✅ CORRECT — use arrays
$vars = [];
$vars["user"] = "Alice";
```

---

## 5. 没有正确处理错误
```php
// ❌ WRONG — suppressing errors
$result = @file_get_contents("nonexistent.json");
if ($result === false) { /* too late */ }

// ✅ CORRECT — proper error handling
try {
    $result = file_get_contents("nonexistent.json");
    if ($result === false) {
        throw new RuntimeException("Failed to read file");
    }
} catch (RuntimeException $e) {
    error_log($e->getMessage());
}
```

---

## 6. 全局状态和超全局
```php
// ❌ WRONG — relying on globals
function getUser() {
    global $db;
    return $db->query("SELECT * FROM users");
}

// ✅ CORRECT — dependency injection
function getUser(Database $db) {
    return $db->query("SELECT * FROM users");
}
```

---

## 7. 数组与对象的混淆
```php
// ❌ WRONG — mixing array and object access
$data = json_decode($jsonString);  // returns object
echo $data["name"];  // Error!

$data = json_decode($jsonString, true);  // returns array
echo $data->name;  // Error!

// ✅ CORRECT — be explicit
$data = json_decode($jsonString, true);  // array
echo $data["name"];

$data = json_decode($jsonString);  // object
echo $data->name;
```

---

## 8. 不使用 Composer 自动加载
```php
// ❌ WRONG — manual requires
require_once 'vendor/some/package/src/Class.php';
require_once 'lib/MyClass.php';

// ✅ CORRECT — Composer autoloading
require_once 'vendor/autoload.php';
use App\Services\UserService;
```

---

## 9. 会话安全
```php
// ❌ WRONG — not regenerating session ID
session_start();
$_SESSION['user_id'] = $userId;

// ✅ CORRECT — regenerate after authentication
session_start();
// ... validate credentials ...
session_regenerate_id(true);
$_SESSION['user_id'] = $userId;
```

---

## 10. 反模式：视图中的业务逻辑
```php
// ❌ WRONG — logic in templates
<?php foreach ($users as $user): ?>
    <?php if ($user['role'] === 'admin' && $user['active']): ?>
        <?php $total += $user['salary']; ?>
    <?php endif; ?>
<?php endforeach; ?>

// ✅ CORRECT — logic in controller/service, display in view
$activeAdminSalaries = $userService->getActiveAdminSalaries();
$total = array_sum($activeAdminSalaries);
```

---

＃＃ 概括
PHP 的灵活性既是它的优点，也是它的缺点。基本规则：始终使用严格比较 (`===`)、使用 SQL 准备语句、启用`declare(strict_types=1)`、使用 Composer 进行自动加载、身份验证后重新生成会话 ID，并将业务逻辑保留在视图之外。具有严格类型、联合类型、匹配表达式和命名参数的现代 PHP (8.x) 与 PHP 5 相去甚远 — 拥抱现代功能。