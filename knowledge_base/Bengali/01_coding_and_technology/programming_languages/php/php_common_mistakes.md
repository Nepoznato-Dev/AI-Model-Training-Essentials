---
# Metadata
title: "PHP — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in PHP with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
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
# PHP - সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি সংশোধন সহ পিএইচপি-তে সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে।
---

## 1. আলগা তুলনা (`==`) ক্ষতি
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

## 2. এসকিউএল ইনজেকশন
```php
// ❌ WRONG — direct string interpolation
$query = "SELECT * FROM users WHERE id = " . $_GET['id'];
$result = $pdo->query($query);

// ✅ CORRECT — prepared statements
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $_GET['id']]);
```

---

## 3. প্রকার ঘোষণা ব্যবহার করছেন না
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

## 4. পরিবর্তনশীল ভেরিয়েবল এবং ডায়নামিক অ্যাক্সেস
```php
// ❌ WRONG — confusing and unsafe
$name = "user";
$$name = "Alice";  // creates $user = "Alice"

// ✅ CORRECT — use arrays
$vars = [];
$vars["user"] = "Alice";
```

---

## 5. সঠিকভাবে ত্রুটি পরিচালনা না করা
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

## 6. গ্লোবাল স্টেট এবং সুপারগ্লোবালস
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

## 7. অ্যারে বনাম অবজেক্ট কনফিউশন
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

## 8. কম্পোজার অটোলোডিং ব্যবহার করছেন না
```php
// ❌ WRONG — manual requires
require_once 'vendor/some/package/src/Class.php';
require_once 'lib/MyClass.php';

// ✅ CORRECT — Composer autoloading
require_once 'vendor/autoload.php';
use App\Services\UserService;
```

---

## 9. সেশন সিকিউরিটি
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

## 10. অ্যান্টি-প্যাটার্ন: ভিউয়ে ব্যবসায়িক যুক্তি
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

## সারাংশ
পিএইচপি এর নমনীয়তা এর শক্তি এবং দুর্বলতা উভয়ই। মূল নিয়মগুলি: সর্বদা কঠোর তুলনা ব্যবহার করুন (`===`), SQL-এর জন্য প্রস্তুত বিবৃতি ব্যবহার করুন,`declare(strict_types=1)`সক্ষম করুন, স্বয়ংক্রিয় লোডিংয়ের জন্য কম্পোজার ব্যবহার করুন, প্রমাণীকরণের পরে সেশন আইডিগুলি পুনরায় তৈরি করুন এবং ব্যবসায়িক যুক্তিকে দৃষ্টির বাইরে রাখুন৷ কঠোর প্রকার, ইউনিয়নের ধরন, ম্যাচ এক্সপ্রেশন এবং নামযুক্ত আর্গুমেন্ট সহ আধুনিক PHP (8.x) PHP 5 থেকে অনেক দূরে - আধুনিক বৈশিষ্ট্যগুলিকে আলিঙ্গন করুন।