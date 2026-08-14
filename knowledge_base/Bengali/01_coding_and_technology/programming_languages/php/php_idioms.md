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
# PHP — ইডিওম্যাটিক প্যাটার্নস এবং সেরা অনুশীলন
এই গাইডটি পরিষ্কার, আধুনিক PHP (8.3+) কোড লেখার জন্য বাহাদুরি প্যাটার্ন এবং সর্বোত্তম অনুশীলনগুলি কভার করে।
---

## আধুনিক পিএইচপি সিনট্যাক্স
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

## মিলিত অভিব্যক্তি
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

## শূন্য নিরাপত্তা
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

## সংগ্রহ এবং অ্যারে
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

## কনস্ট্রাক্টর প্রমোশন
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

## ফাইবার (PHP 8.1+)
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

## ত্রুটি হ্যান্ডলিং
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

## সারাংশ
আধুনিক PHP ইডিয়মগুলি জোর দেয়: টাইপ ডিক্লেয়ারেশন, শুধুমাত্র পঠনযোগ্য বৈশিষ্ট্য, enums, ম্যাচ এক্সপ্রেশন, কনস্ট্রাক্টর প্রচার, নাল-সেফ অপারেটর, নামযুক্ত আর্গুমেন্ট এবং ফাইবার। শৈলীর জন্য PSR-12, স্ট্যাটিক বিশ্লেষণের জন্য PHPStan এবং বিন্যাসের জন্য Laravel Pint বা PHP-CS-Fixer অনুসরণ করুন। আধুনিক PHP (8.3+) হল একটি পরিষ্কার, টাইপ-নিরাপদ ভাষা — নতুন বৈশিষ্ট্যগুলিকে আলিঙ্গন করুন এবং উত্তরাধিকারী নিদর্শনগুলি এড়িয়ে চলুন৷