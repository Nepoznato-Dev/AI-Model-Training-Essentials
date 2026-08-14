<!--
---
# Metadata
title: "PHP — Cheat Sheet"
description: "Quick-reference cheat sheet for PHP syntax, arrays, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [php, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# PHP — Aide-mémoire
## Bases
```php
<?php
declare(strict_types=1);

// Variables
$name = "Alice";
$age = 30;
$pi = 3.14159;
$active = true;
const MAX = 100;
define('MIN', 0);

// Types
gettype($name);     // "string"
is_string($name);   // true
is_int($age);       // true
(int) "42";         // type cast to int
(string) 42;        // "42"
settype($var, "int");

// String interpolation
"Hello, $name!"
"Hello, {$name}!"
"Hello, " . $name . "!"  // concatenation
"Age: {$age}"
<<<EOT
Hello, $name!
Age: $age
EOT;

// String functions
strlen($name)
strtoupper($name)
strtolower($name)
trim($name)
str_contains($name, "lic")   // PHP 8+
str_replace("Alice", "Bob", $name)
substr($name, 0, 3)
explode(" ", "hello world")   // ["hello", "world"]
implode(", ", $arr)
sprintf("Hello, %s!", $name)
```

## Tableaux
```php
// Indexed array
$arr = [1, 2, 3];
$arr[] = 4;                    // push
$arr[0];
count($arr);
array_push($arr, 5);
array_pop($arr);
array_shift($arr);
array_unshift($arr, 0);
array_slice($arr, 1, 2);
array_merge($arr, [5, 6]);
in_array(3, $arr);

// Associative array (map)
$user = ['name' => 'Alice', 'age' => 30];
$user['email'] = 'a@b.com';
$user['name'];
$user['phone'] ?? 'N/A';      // null coalescing
array_keys($user);
array_values($user);
array_key_exists('name', $user);
isset($user['name']);
unset($user['age']);

// Array functions
array_map(fn($x) => $x * 2, $arr);
array_filter($arr, fn($x) => $x > 2);
array_reduce($arr, fn($carry, $x) => $carry + $x, 0);
array_walk($arr, fn(&$v) => $v *= 2);
usort($arr, fn($a, $b) => $a <=> $b);
array_combine($keys, $values);
array_column($users, 'name');

// Spread operator (PHP 7.4+)
$merged = [...$arr1, ...$arr2];
$extended = [...$arr, 4, 5];
```

## Flux de contrôle
```php
if ($condition) {
    // ...
} elseif ($other) {
    // ...
} else {
    // ...
}

// Ternary
$result = $condition ? "yes" : "no";

// Null coalescing
$value = $input ?? "default";
$value = $a ?? $b ?? $c;

// Match (PHP 8+)
$label = match ($status) {
    'active'   => 'Active user',
    'inactive' => 'Inactive user',
    default    => 'Unknown',
};

// Switch
switch ($day) {
    case 'Mon': case 'Tue':
        echo "early week"; break;
    default:
        echo "later"; break;
}

// Loops
foreach ($arr as $item) { ... }
foreach ($arr as $key => $value) { ... }
for ($i = 0; $i < 10; $i++) { ... }
while ($condition) { ... }
do { ... } while ($condition);
```

## Fonctions
```php
// Basic function
function add(int $a, int $b): int {
    return $a + $b;
}

// Default & named params
function greet(string $name, string $greeting = "Hello"): string {
    return "$greeting, $name!";
}
greet(greeting: "Hi", name: "Alice");  // named args (PHP 8+)

// Variadic
function sum(int ...$nums): int {
    return array_sum($nums);
}

// Arrow function (PHP 7.4+)
$double = fn($x) => $x * 2;

// Closure
$counter = function() {
    static $n = 0;
    return ++$n;
};

// First-class callable (PHP 8.1+)
$fn = strlen(...);
$fn("hello");  // 5
```

## Classes et énumérations
```php
// Class
class User {
    public function __construct(
        public readonly string $name,   // constructor promotion (PHP 8.1+)
        public int $age = 0,
    ) {}

    public function greet(): string {
        return "Hi, I'm {$this->name}";
    }
}

// Enum (PHP 8.1+)
enum Status: string {
    case Active = 'active';
    case Inactive = 'inactive';

    public function label(): string {
        return match($this) {
            self::Active => 'Active',
            self::Inactive => 'Inactive',
        };
    }
}

// Interface
interface Renderable {
    public function render(): string;
}

// Trait
trait Timestampable {
    public function getCreatedAt(): DateTimeImmutable {
        return $this->createdAt;
    }
}
```

## Gestion des erreurs
```php
try {
    $result = riskyOperation();
} catch (InvalidArgumentException $e) {
    echo "Bad arg: " . $e->getMessage();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
} finally {
    cleanup();
}

throw new RuntimeException("Something failed");

// Custom exception
class NotFoundException extends RuntimeException {}
```

## Modèles courants
```php
// Nullsafe operator (PHP 8+)
$city = $user?->getAddress()?->getCity();

// Named arguments
array_slice(array: $data, offset: 1, length: 5);

// Attributes (PHP 8+)
#[Route('/api/users', methods: ['GET'])]
public function index(): Response { ... }

// Fibers (PHP 8.1+)
$fiber = new Fiber(function(): void {
    $value = Fiber::suspend('paused');
    echo "Resumed with: $value";
});
$fiber->start();
$fiber->resume('hello');

// Readonly properties
class Point {
    public function __construct(public readonly float $x, public readonly float $y) {}
}
```
