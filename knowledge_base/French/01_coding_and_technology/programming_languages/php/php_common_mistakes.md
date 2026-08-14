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
# PHP — Erreurs courantes et anti-modèles
Ce document répertorie les erreurs, pièges et anti-modèles les plus courants en PHP avec des corrections.
---

## 1. Pièges de la comparaison lâche (`==`)
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

## 2. Injection SQL
```php
// ❌ WRONG — direct string interpolation
$query = "SELECT * FROM users WHERE id = " . $_GET['id'];
$result = $pdo->query($query);

// ✅ CORRECT — prepared statements
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $_GET['id']]);
```

---

## 3. Ne pas utiliser de déclarations de type
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

## 4. Variables variables et accès dynamique
```php
// ❌ WRONG — confusing and unsafe
$name = "user";
$$name = "Alice";  // creates $user = "Alice"

// ✅ CORRECT — use arrays
$vars = [];
$vars["user"] = "Alice";
```

---

## 5. Ne pas gérer correctement les erreurs
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

## 6. État global et superglobales
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

## 7. Confusion tableau et objet
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

## 8. Ne pas utiliser le chargement automatique de Composer
```php
// ❌ WRONG — manual requires
require_once 'vendor/some/package/src/Class.php';
require_once 'lib/MyClass.php';

// ✅ CORRECT — Composer autoloading
require_once 'vendor/autoload.php';
use App\Services\UserService;
```

---

## 9. Sécurité des sessions
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

## 10. Anti-modèle : logique métier dans les vues
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

## Résumé
La flexibilité de PHP est à la fois sa force et sa faiblesse. Les règles cardinales : utilisez toujours une comparaison stricte (`===`), utilisez des instructions préparées pour SQL, activez`declare(strict_types=1)`, utilisez Composer pour le chargement automatique, régénérez les ID de session après l'authentification et gardez la logique métier hors des vues. PHP moderne (8.x) avec des types stricts, des types d'union, des expressions de correspondance et des arguments nommés est loin de PHP 5 - adoptez les fonctionnalités modernes.