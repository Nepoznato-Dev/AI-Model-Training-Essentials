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
# PHP — 구문 참조
이 문서는 PHP(8.x)에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 철저한 구문 패턴, 최신 PHP 기능, 객체 지향 프로그래밍 및 실용적인 관용구에 중점을 두어 기본 PHP 참조를 보완합니다.
---

## 연산자 및 표현식
### 핵심 운영자
| 운영자 | 이름 | 예 | 메모 |
|------------|------|---------|-------|
| `+``-``*``/``%`| 산술 | `$a + $b`| |
| `**`| 지수화 | `2 ** 10`| `1024`|
| `==``!=``===``!==` | 평등 | `$a === $b`|  `===`도 유형을 확인합니다 |
| `<=>`| 우주선 | `$a <=> $b`| -1, 0 또는 1을 반환합니다. |
| `<``>``<=``>=` | 비교 | `$a >= $b`| |
| `&&``\|\|``!`| 논리적 | `$a && $b`| 단락 |
| `and``or``xor`| 논리적(낮은 우선순위) | `$a and $b`| 피하십시오 -`&&`/`\|\|`|를 사용하십시오.
| `??`| Null 병합 | `$a ?? 'default'`| `$a`가 null인 경우 `'default'`를 반환합니다. |
| `??=`| Null 병합 할당 | `$a ??= 'default'`| `$a`가 null인 경우에만 할당 |
| `?``:` | 삼항 | `$a ? $b : $c`| |
| `.`| 연결 | `$a . $b`| |
| `.=`| 연결 할당 | `$a .= $b`| |
| `=>`| 배열 할당 | `['key' => 'value']`| |
| `->`| 회원 액세스 | `$obj->method()`| |
| `?->`| Nullsafe 연산자 | `$obj?->method()`| `$obj`가 null인 경우 null을 반환합니다. |
| `::`| 정적 액세스 | `ClassName::method()`| |
| `instanceof`| 유형 확인 | `$obj instanceof ClassName`| |
| `clone`| 객체 복제 | `$copy = clone $obj`| 깊은 복사에는 `__clone()`가 필요합니다 |
### 유형 저글링
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

## 제어 흐름
### 조건부
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

### 루프
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

## 기능
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

## 배열 및 데이터 구조
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

## 객체지향 프로그래밍
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

## 오류 처리
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

## 네임스페이스 및 자동 로딩
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

## 고급 기능
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

## 요약
PHP의 구문은 스크립팅의 기원에서 현대적이고 유형이 안전한 언어로 극적으로 발전했습니다. PHP 8.x에서는 공용체 유형, 교차 유형, 열거형, 파이버, 읽기 전용 클래스, 속성 및 최고 수준의 호출 가능 항목을 도입하여 느슨한 유형의 스크립트 언어를 엄격한 소프트웨어 엔지니어링을 지원하는 언어로 변환했습니다. 언어의 장점은 여전히 ​​웹에 중점을 두고 있습니다. Laravel 및 Symfony와 같은 프레임워크, 대규모 생태계 및 거의 보편적인 호스팅 지원을 통해 PHP의 구문은 수백만 개의 애플리케이션을 지원합니다. 최신 PHP는 유형 시스템을 수용하고, 작성기 기반 자동 로딩을 사용하고, 깔끔한 객체 지향 코드를 작성하는 개발자에게 보상을 제공합니다.