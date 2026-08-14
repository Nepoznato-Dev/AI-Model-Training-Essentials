<!--
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

-->
# PHP - محاوراتی نمونے اور بہترین طرز عمل
یہ گائیڈ صاف، جدید پی ایچ پی (8.3+) کوڈ لکھنے کے لیے محاوراتی نمونوں اور بہترین طریقوں کا احاطہ کرتا ہے۔
---

## جدید پی ایچ پی نحو
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

## مماثل اظہار
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

## کالعدم حفاظت
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

## مجموعے اور صفیں۔
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

## کنسٹرکٹر پروموشن
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

## فائبرز (PHP 8.1+)
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

## ہینڈلنگ کی خرابی۔
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

## خلاصہ
پی ایچ پی کے جدید محاورے اس بات پر زور دیتے ہیں: ٹائپ ڈیکلریشنز، صرف پڑھنے کے لیے خواص، enums، میچ ایکسپریشنز، کنسٹرکٹر پروموشن، null-safe آپریٹر، نامزد دلائل، اور fibers۔ طرز کے لیے PSR-12، جامد تجزیہ کے لیے PHPStan، اور فارمیٹنگ کے لیے Laravel Pint یا PHP-CS-Fixer کی پیروی کریں۔ جدید پی ایچ پی (8.3+) ایک صاف ستھری، ٹائپ سیف لینگوئج ہے — نئی خصوصیات کو قبول کریں اور وراثت کے نمونوں سے بچیں۔