---
# Metadata
title: "PHP — Syntax Reference"
description: "Detailed syntax reference for PHP covering operators, control flow, functions, classes, traits, enums, fibers, and modern PHP 8.x features."
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
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [php, syntax-reference, operators, oop, traits, enums, fibers, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# PHP — 構文リファレンス
このドキュメントは、PHP (8.x) の包括的で構造化された構文リファレンスを提供します。網羅的な構文パターン、最新の PHP 機能、オブジェクト指向プログラミング、実用的なイディオムに焦点を当て、主要な PHP リファレンスを補完します。
---

## 演算子と式
### コアオペレーター
|オペレーター |名前 |例 |メモ |
|----------|------|----------|----------|
| `+``-``*``/``%`|算数 | `$a + $b`| |
| `**`|べき乗 | `2 ** 10`| `1024`|
| `==``!=``===``!==` |平等 | `$a === $b`| `===`はタイプもチェックします。
| `<=>`|宇宙船 | `$a <=> $b`| -1、0、または 1 を返します |
| `<``>``<=``>=` |比較 | `$a >= $b`| |
| `&&``\|\|``!`|論理 | `$a && $b`|短絡 |
| `and``or``xor`|論理 (優先順位が低い) | `$a and $b`|避けてください —`&&`/`\|\|`を使用してください |
| `??`|ヌル合体 | `$a ?? 'default'`|`$a`が null の場合は`'default'`を返します。
| `??=`| Null 合体割り当て | `$a ??= 'default'`|`$a`が null の場合にのみ割り当てます。
| `?``:` | 3進法 | `$a ? $b : $c`| |
| `.`|連結 | `$a . $b`| |
| `.=`| assign | を連結する `$a .= $b`| |
| `=>`|配列の代入 | `['key' => 'value']`| |
| `->`|メンバーアクセス | `$obj->method()`| |
|  XQZマーカー50XQZ | Nullsafe 演算子 | `$obj?->method()`|`$obj`が null の場合は null を返します。
| `::`|静的アクセス | `ClassName::method()`| |
| `instanceof`|タイプチェック | `$obj instanceof ClassName`| |
| `clone`|オブジェクトのクローン作成 | `$copy = clone $obj`|ディープ コピーには`__clone()`が必要です |
### タイプジャグリング
```php
// PHP automatically converts types in many contexts
"0" == false;       // true (loose comparison — avoid!)
"0" === false;      // false (strict comparison — always use this)
"" == false;         // true
null == false;       // true
0 == false;          // true
[] == false;         // true (PHP 8.0+: no longer — warning in 8.x)

// Explicit casting
(int) "42abc";       // 42
(float) "3.14";      // 3.14
(string) 42;         // "42"
(bool) 0;            // false
(bool) "";           // false
(bool) null;         // false
(array) $value;      // Cast to array
(object) $array;     // Cast to stdClass
```

---

## 制御フロー
### 条件文
```php
// if / elseif / else
if ($score >= 90) {
    $grade = 'A';
} elseif ($score >= 80) {
    $grade = 'B';
} else {
    $grade = 'F';
}

// Ternary operator
$status = $age >= 18 ? 'adult' : 'minor';

// Null coalescing
$name = $input['name'] ?? 'Anonymous';

// match expression (PHP 8.0+)
$label = match ($status) {
    'active'     => 'Currently active',
    'pending'    => 'Awaiting activation',
    'inactive'   => 'Disabled',
    default      => 'Unknown status',
};

// match with conditions
$description = match (true) {
    $score >= 90       => 'Excellent',
    $score >= 70       => 'Good',
    $score >= 50       => 'Pass',
    default            => 'Fail',
};
```

### ループ
```php
// for
for ($i = 0; $i < 10; $i++) {
    echo $i;
}

// while
while ($row = $stmt->fetch()) {
    process($row);
}

// do-while
do {
    $result = attempt();
} while ($result === null);

// foreach (the idiomatic PHP loop)
foreach ($items as $item) {
    echo $item;
}

// foreach with key
foreach ($array as $key => $value) {
    echo "$key: $value";
}

// foreach with reference
foreach ($array as &$value) {
    $value *= 2;
}
unset($value); // Important: break reference

// break and continue
foreach ($items as $item) {
    if ($item === 'skip') continue;
    if ($item === 'stop') break;
    process($item);
}

// Alternative syntax (for templates)
foreach ($items as $item): ?>
    <li><?= htmlspecialchars($item) ?></li>
<?php endforeach;
```

---

## 関数
```php
// Basic function
function add(int $a, int $b): int {
    return $a + $b;
}

// Default parameters
function greet(string $name = 'World'): string {
    return "Hello, $name!";
}

// Named arguments (PHP 8.0+)
function createUser(string $name, string $email, int $age = 0): array {
    return compact('name', 'email', 'age');
}
$user = createUser(name: 'Alice', email: 'alice@example.com', age: 30);

// Variadic parameters
function sum(int ...$numbers): int {
    return array_sum($numbers);
}
sum(1, 2, 3, 4); // 10

// Type declarations
function process(
    string $name,
    ?int $age,              // Nullable type
    array|string $data,     // Union type (PHP 8.0+)
): never {                  // never return (PHP 8.1+)
    throw new RuntimeException("Not implemented");
}

// Intersection types (PHP 8.1+)
function processItem(Countable&Iterator $item): void {
    foreach ($item as $key => $value) { /* ... */ }
}

// Return type covariance
interface Animal { function speak(): string; }
class Dog implements Animal { function speak(): string { return "Woof!"; } }

// Arrow functions (short closures)
$multiplier = fn($x) => $x * 2;
$doubled = array_map(fn($n) => $n * 2, [1, 2, 3]);

// Closures
$greet = function (string $name) use ($defaultGreeting): string {
    return "$defaultGreeting, $name!";
};

// First-class callable syntax (PHP 8.1+)
$strlen = strlen(...);
$strlen("hello"); // 5

// Generator functions
function fibonacci(): Generator {
    [$a, $b] = [0, 1];
    while (true) {
        yield $a;
        [$a, $b] = [$b, $a + $b];
    }
}

foreach (fibonacci() as $num) {
    if ($num > 100) break;
    echo "$num ";
}

// Generator with send/receive
function logger(): Generator {
    while (true) {
        $message = yield;
        echo "[LOG] $message\n";
    }
}
$log = logger();
$log->send("Starting");
$log->send("Processing");
```

---

## 配列とデータ構造
```php
// Indexed array
$fruits = ['apple', 'banana', 'cherry'];
$fruits[] = 'date';                    // Append
$fruits[0];                            // 'apple'

// Associative array
$user = [
    'name'  => 'Alice',
    'email' => 'alice@example.com',
    'age'   => 30,
];
$user['name'];                         // 'Alice'
$user['role'] ?? 'viewer';             // Null coalescing

// Array destructuring
['name' => $name, 'email' => $email] = $user;
[$first, $second, ...$rest] = $numbers;

// Spread operator (PHP 7.4+)
$merged = [...$array1, ...$array2];
$result = [...$items, 'extra'];

// Array functions
array_map(fn($x) => $x * 2, [1, 2, 3]);         // [2, 4, 6]
array_filter([1, 2, 3, 4], fn($x) => $x > 2);   // [3, 4] (preserves keys)
array_reduce([1, 2, 3], fn($carry, $x) => $carry + $x, 0); // 6
array_keys($user);                               // ['name', 'email', 'age']
array_values($user);                             // ['Alice', 'alice@...', 30]
array_combine(['a', 'b'], [1, 2]);               // ['a' => 1, 'b' => 2]
array_merge($arr1, $arr2);
array_slice($arr, 2, 3);
array_splice($arr, 2, 1, ['replacement']);
in_array('apple', $fruits, true);                // Strict search
array_search('banana', $fruits, true);           // Returns key or false
array_key_exists('name', $user);
usort($items, fn($a, $b) => $a['age'] <=> $b['age']);
array_column($records, 'name', 'id');            // Extract column
```

---

## オブジェクト指向プログラミング
```php
// Class with constructor promotion (PHP 8.0+)
class User {
    public function __construct(
        public readonly string $name,
        public readonly string $email,
        private int $age = 0,
    ) {}

    public function getAge(): int {
        return $this->age;
    }

    public function __toString(): string {
        return "User({$this->name}, {$this->email})";
    }
}

// Inheritance
class Admin extends User {
    public function __construct(
        string $name,
        string $email,
        int $age,
        private array $permissions = [],
    ) {
        parent::__construct($name, $email, $age);
    }
}

// Abstract class
abstract class Shape {
    abstract public function area(): float;
    abstract public function perimeter(): float;

    public function describe(): string {
        return sprintf("Area: %.2f, Perimeter: %.2f", $this->area(), $this->perimeter());
    }
}

// Interface
interface Serializable {
    public function serialize(): string;
    public static function deserialize(string $data): static;
}

// Trait — reusable behavior
trait Timestampable {
    private ?DateTimeImmutable $createdAt = null;
    private ?DateTimeImmutable $updatedAt = null;

    public function touch(): void {
        $this->updatedAt = new DateTimeImmutable();
        $this->createdAt ??= $this->updatedAt;
    }

    public function getCreatedAt(): ?DateTimeImmutable {
        return $this->createdAt;
    }
}

trait Loggable {
    public function log(string $message): void {
        error_log(sprintf("[%s] %s", date('Y-m-d H:i:s'), $message));
    }
}

// Using traits
class Article {
    use Timestampable, Loggable;

    public function __construct(
        public readonly string $title,
        public readonly string $content,
    ) {
        $this->touch();
    }
}

// Enum (PHP 8.1+)
enum Suit: string {
    case Hearts = 'H';
    case Diamonds = 'D';
    case Clubs = 'C';
    case Spades = 'S';

    public function color(): string {
        return match ($this) {
            self::Hearts, self::Diamonds => 'red',
            self::Clubs, self::Spades    => 'black',
        };
    }
}

$card = Suit::Hearts;
echo $card->value;     // 'H'
echo $card->color();   // 'red'
echo $card->name;      // 'Hearts'

// Pure enum (no backing type)
enum Status {
    case Active;
    case Pending;
    case Archived;
}

// Enum with methods
enum Priority: int {
    case Low = 1;
    case Medium = 2;
    case High = 3;

    public function label(): string {
        return match ($this) {
            self::Low    => 'Low Priority',
            self::Medium => 'Medium Priority',
            self::High   => 'High Priority',
        };
    }
}
```

---

## エラー処理
```php
// try / catch / finally
try {
    $result = riskyOperation();
} catch (SpecificException $e) {
    logger()->error($e->getMessage());
    throw new AppException("Operation failed", previous: $e);
} catch (AnotherException | YetAnother $e) {  // Multi-catch (PHP 7.1+)
    handleGracefully($e);
} finally {
    cleanup();
}

// Custom exceptions
class ValidationException extends RuntimeException {
    public function __construct(
        private array $errors,
        string $message = 'Validation failed',
        int $code = 422,
        ?Throwable $previous = null,
    ) {
        parent::__construct($message, $code, $previous);
    }

    public function getErrors(): array {
        return $this->errors;
    }
}

// Throwing
throw new ValidationException(
    errors: ['email' => 'Invalid email format'],
);

// set_error_handler for warnings/notices
set_error_handler(function (int $errno, string $errstr, string $file, int $line) {
    throw new ErrorException($errstr, 0, $errno, $file, $line);
});
```

---

## 名前空間と自動読み込み
```php
// Namespace declaration
namespace App\Services;

use App\Models\User;
use App\Contracts\RepositoryInterface;
use function App\Helpers\format_date;
use const App\Config\MAX_RETRIES;

class UserService implements RepositoryInterface {
    public function __construct(
        private readonly DatabaseConnection $db,
    ) {}

    public function find(int $id): ?User {
        return $this->db->query("SELECT * FROM users WHERE id = ?", [$id]);
    }
}
```

```php
// Composer autoloading (composer.json)
// {
//     "autoload": {
//         "psr-4": {
//             "App\\": "src/"
//         }
//     },
//     "autoload-dev": {
//         "psr-4": {
//             "App\\Tests\\": "tests/"
//         }
//     }
// }
```

---

## 高度な機能
```php
// Fibers (PHP 8.1+) — lightweight cooperative threads
$fiber = new Fiber(function (): void {
    $value = Fiber::suspend('computing...');
    echo "Got: $value\n";
    $result = Fiber::suspend('still working...');
    echo "Result: $result\n";
});

echo $fiber->start();      // 'computing...'
$fiber->resume('hello');    // Got: hello
echo $fiber->start();       // 'still working...' (after resume)
$fiber->resume('world');    // Result: world

// Attributes (PHP 8.0+) — structured metadata
#[Attribute(Attribute::TARGET_CLASS)]
class Table {
    public function __construct(public string $name) {}
}

#[Attribute(Attribute::TARGET_PROPERTY)]
class Column {
    public function __construct(
        public string $name,
        public bool $nullable = false,
    ) {}
}

#[Table('users')]
class UserEntity {
    #[Column('id')]
    public int $id;

    #[Column('name', nullable: false)]
    public string $name;
}

// Reflection with attributes
$ref = new ReflectionClass(UserEntity::class);
$tableAttr = $ref->getAttributes(Table::class)[0]->newInstance();
echo $tableAttr->name; // 'users'

// Readonly classes (PHP 8.2+)
readonly class Point3D {
    public function __construct(
        public float $x,
        public float $y,
        public float $z,
    ) {}
}

// Disjunctive Normal Form types (PHP 8.2+)
function process((A&B)|C $value): void { }

// Named arguments with spread
function configure(string $host, int $port, bool $ssl = true): void { /* ... */ }
$options = ['host' => 'localhost', 'port' => 8080];
configure(...$options);

// Anonymous classes
$logger = new class {
    public function log(string $message): void {
        echo "[LOG] $message\n";
    }
};

// Weak references and maps
$cache = new WeakMap();
$obj = new stdClass;
$cache[$obj] = "expensive data";
// When $obj is garbage collected, the entry is automatically removed
```

---

＃＃ まとめ
PHP の構文は、スクリプトの起源から現代のタイプセーフな言語へと劇的に進化しました。 PHP 8.x では、ユニオン型、交差型、列挙型、ファイバー、読み取り専用クラス、属性、およびファーストクラス呼び出し可能関数が導入され、緩やかに型付けされたスクリプト言語から厳密なソフトウェア エンジニアリングをサポートする言語に変換されました。この言語の強みは依然として Web に焦点を当てていることです。Laravel や Symfony のようなフレームワーク、大規模なエコシステム、およびほぼ普遍的なホスティング サポートにより、PHP の構文は何百万ものアプリケーションに対応します。最新の PHP は、その型システムを採用し、コンポーザーベースの自動ロードを使用し、クリーンなオブジェクト指向コードを作成する開発者に報酬を与えます。