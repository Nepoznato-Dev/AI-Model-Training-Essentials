---
# Metadata
title: "PHP — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern PHP code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [php, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# PHP — 惯用模式和最佳实践
本指南涵盖了编写干净、现代的 PHP (8.3+) 代码的惯用模式和最佳实践。
---

## 现代 PHP 语法
```php
// ✅ Type declarations everywhere
function createUser(string $name, string $email, int $age): User
{
    return new User($name, $email, $age);
}

// ✅ Readonly properties (PHP 8.1+)
class User
{
    public function __construct(
        public readonly string $name,
        public readonly string $email,
    ) {}
}

// ✅ Enums (PHP 8.1+)
enum Status: string
{
    case Active = 'active';
    case Inactive = 'inactive';
    case Pending = 'pending';
    
    public function label(): string
    {
        return match($this) {
            self::Active => 'Active',
            self::Inactive => 'Inactive',
            self::Pending => 'Pending Review',
        };
    }
}

// ✅ Named arguments
$user = new User(
    name: 'Alice',
    email: 'alice@example.com',
    age: 30,
);
```

---

## 匹配表达式
```php
// ✅ match instead of switch
$label = match($status) {
    'active' => 'Active',
    'inactive' => 'Inactive',
    'pending' => 'Pending Review',
    default => 'Unknown',
};

// ✅ match with conditions
$description = match(true) {
    $age < 13 => 'child',
    $age < 18 => 'teenager',
    $age < 65 => 'adult',
    default => 'senior',
};
```

---

## 空安全
```php
// ✅ Null-safe operator (PHP 8.0+)
$city = $user?->getAddress()?->getCity();

// ✅ Null coalescing
$name = $input['name'] ?? 'Anonymous';

// ✅ Null coalescing assignment
$config['debug'] ??= false;

// ✅ isset vs null check
if (isset($array['key'])) { ... }
if ($value !== null) { ... }
```

---

## 集合和数组
```php
// ✅ Array unpacking
$merged = [...$defaults, ...$overrides];
$combined = [...$arr1, ...$arr2, 'extra'];

// ✅ Named array keys (associative)
$config = [
    'host' => 'localhost',
    'port' => 8080,
    'debug' => true,
];

// ✅ Spread in function calls
$result = array_merge([...$arr1, ...$arr2]);

// ✅ Array functions
$names = array_map(fn(User $u) => $u->name, $users);
$adults = array_filter($users, fn(User $u) => $u->age >= 18);
$found = array_find($users, fn(User $u) => $u->id === $targetId); // PHP 8.4+
$total = array_reduce($items, fn(int $carry, Item $i) => $carry + $i->price, 0);
$exists = in_array($value, $array, true); // strict comparison

// ✅ First-class callable syntax (PHP 8.1+)
$lengths = array_map(strlen(...), $strings);
```

---

## 构造函数提升
```php
// ✅ Constructor property promotion (PHP 8.0+)
class User
{
    public function __construct(
        public readonly string $name,
        public readonly string $email,
        private readonly PasswordHasher $hasher = new PasswordHasher(),
    ) {}
}

// ✅ Named arguments with defaults
function configure(
    string $host = 'localhost',
    int $port = 8080,
    bool $debug = false,
): Config {
    return new Config($host, $port, $debug);
}
```

---

## 纤维 (PHP 8.1+)
```php
// ✅ Fibers for cooperative multitasking
$fiber = new Fiber(function (): void {
    $value = Fiber::suspend('computing...');
    echo "Got: $value";
});

$result = $fiber->start();  // 'computing...'
$fiber->resume('hello');    // Got: hello
```

---

## 错误处理
```php
// ✅ Throw expressions (PHP 8.0+)
$value = $input ?? throw new InvalidArgumentException('Missing input');

// ✅ Custom exceptions
class ValidationException extends RuntimeException
{
    public function __construct(
        public readonly string $field,
        string $message = '',
    ) {
        parent::__construct("$field: $message");
    }
}

// ✅ try/catch with multiple exceptions
try {
    $result = $service->process($data);
} catch (ValidationException $e) {
    return response()->json(['error' => $e->field], 422);
} catch (DatabaseException $e) {
    Log::error('Database error', ['exception' => $e]);
    return response()->json(['error' => 'Internal error'], 500);
}
```

---

＃＃ 概括
现代 PHP 习惯用法强调：类型声明、只读属性、枚举、匹配表达式、构造函数提升、空安全运算符、命名参数和纤程。样式遵循 PSR-12，静态分析遵循 PHPStan，格式化遵循 Laravel Pint 或 PHP-CS-Fixer。现代 PHP (8.3+) 是一种干净、类型安全的语言 — 拥抱新功能并避免遗留模式。