---
# Metadata
title: "PHP"
description: "Comprehensive reference for the PHP programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [php, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "34 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# পিএইচপি
পিএইচপি (হাইপারটেক্সট প্রিপ্রসেসর) হল একটি সার্ভার-সাইড স্ক্রিপ্টিং ভাষা যা 1994 সালে রাসমাস লারডর্ফ দ্বারা তৈরি করা হয়েছিল এবং 1995 সালে প্রথম প্রকাশিত হয়েছিল। মূলত গতিশীল ওয়েব পৃষ্ঠাগুলি তৈরি করার জন্য ডিজাইন করা হয়েছে, পিএইচপি একটি সম্পূর্ণ বৈশিষ্ট্যযুক্ত সাধারণ-উদ্দেশ্য ভাষায় বিকশিত হয়েছে। এটি ওয়ার্ডপ্রেস, Facebook (মূলত), উইকিপিডিয়া, স্ল্যাক এবং অন্যান্য লক্ষ লক্ষ সাইট সহ একটি পরিচিত সার্ভার-সাইড ভাষা সহ সমস্ত ওয়েবসাইটের প্রায় 75% ক্ষমতা দেয়৷
আধুনিক পিএইচপি (8.x) হল 2000 এর দশকের প্রথম দিকের পিএইচপি থেকে খুব আলাদা একটি ভাষা। এটিতে এখন টাইপ করা বৈশিষ্ট্য, ম্যাচ এক্সপ্রেশন, enums, ফাইবার, শুধুমাত্র পাঠযোগ্য ক্লাস এবং একটি শক্তিশালী টাইপ সিস্টেম রয়েছে। ডেভেলপারদের মধ্যে এর খ্যাতি সত্ত্বেও (প্রায়শই অসঙ্গতির জন্য সমালোচিত), পিএইচপি ব্যবহারিক, ব্যাপকভাবে স্থাপন করা হয়েছে এবং উন্নতি অব্যাহত রয়েছে।
---

## কেন পিএইচপি গুরুত্বপূর্ণ
- **ওয়েবের আধিপত্য**: ~75% ওয়েবসাইট চালায়। ওয়ার্ডপ্রেস একাই ওয়েবের 43% ক্ষমতা রাখে।
- **প্রবেশে কম বাধা**: যেকোনো শেয়ার করা হোস্টিং-এ ফাইল আপলোড করে স্থাপন করুন। কোন সংকলন, কোন বিল্ড পদক্ষেপ.
- **পরিপক্ক ইকোসিস্টেম**: সুরকার (প্যাকেজ ম্যানেজার), লারাভেল, সিমফনি — পরিণত, যুদ্ধ-পরীক্ষিত সরঞ্জাম।
- **ব্যবহারিক**: ন্যূনতম সেটআপ সহ মিনিটের মধ্যে চলমান একটি গতিশীল ওয়েবসাইট পান।
- **নিরন্তর উন্নতি**: PHP 8.x জীবনের মানের উল্লেখযোগ্য উন্নতি এনেছে।
- **ফ্রিল্যান্সিং মার্কেট**: ওয়ার্ডপ্রেস, লারাভেল এবং ই-কমার্স (WooCommerce, Magento) ডেভেলপারদের বিপুল চাহিদা।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **অসঙ্গত নামকরণ** | `strpos`বনাম`str_replace`,`array_key_exists`বনাম`in_array`— কোন সামঞ্জস্যপূর্ণ সম্মেলন নেই | অসঙ্গতি শিখুন; IDE স্বয়ংসম্পূর্ণ ব্যবহার করুন |
| **ঐতিহাসিক লাগেজ** | PHP 5 এবং তার আগের থেকে উত্তরাধিকার বৈশিষ্ট্য এবং নিদর্শন | আধুনিক পিএইচপি ব্যবহার করুন (8.2+); পিএসআর মান অনুসরণ করুন |
| **পারফরম্যান্স** | নন-ওয়েব কাজের জন্য Go, Rust, বা Java এর চেয়ে ধীর OPcache ব্যবহার করুন; অ্যাসিঙ্কের জন্য Swoole বিবেচনা করুন; PHP-FPM ব্যবহার করুন |
| **নন-ওয়েবের জন্য আদর্শ নয়** | CLI, ডেস্কটপ, মোবাইল, ডেটা সায়েন্স — পিএইচপি এর শক্তি নয় | নন-ওয়েব কাজের জন্য পাইথন, গো, বা অন্যান্য ভাষা ব্যবহার করুন |
| **নিরাপত্তা খ্যাতি** | লিগ্যাসি পিএইচপি কোডে অনেক নিরাপত্তা সমস্যা আছে | আধুনিক কাঠামো ব্যবহার করুন; নিরাপত্তা সর্বোত্তম অনুশীলন অনুসরণ করুন |
---

## সিনট্যাক্স মৌলিক
### মৌলিক কাঠামো
```php
<?php
declare(strict_types=1);

// Variables (always prefixed with $)
$name = "Alice";
$age = 30;
$score = 9.5;
$active = true;
$items = [1, 2, 3];

// String interpolation
echo "Hello, $name! You are $age years old.";
echo "Score: {$score}";

// Arrays (both indexed and associative)
$fruits = ["apple", "banana", "cherry"];
$user = [
    "name" => "Alice",
    "age" => 30,
    "email" => "alice@example.com",
];

echo $user["name"];  // "Alice"
```

### ফাংশন এবং প্রকার
```php
// Typed functions (PHP 7+)
function add(int $a, int $b): int {
    return $a + $b;
}

function greet(string $name, string $greeting = "Hello"): string {
    return "$greeting, $name!";
}

// Nullable types
function findUser(int $id): ?array {
    return $id > 0 ? ["id" => $id, "name" => "Alice"] : null;
}

// Union types (PHP 8.0+)
function formatId(int|string $id): string {
    return "ID: $id";
}

// Named arguments (PHP 8.0+)
function createUser(string $name, int $age, string $role = "viewer"): array {
    return compact("name", "age", "role");
}

$user = createUser(name: "Alice", age: 30, role: "admin");

// Spread operator
$defaults = ["timeout" => 30, "retries" => 3];
$config = [...$defaults, "timeout" => 60];  // ["timeout" => 60, "retries" => 3]
```

### ক্লাস এবং ওওপি
```php
// Class with typed properties
class Animal {
    public function __construct(
        protected readonly string $name,
    ) {}

    public function speak(): string {
        return "{$this->name} makes a sound";
    }

    public function getName(): string {
        return $this->name;
    }
}

class Dog extends Animal {
    public function speak(): string {
        return "{$this->name} says woof";
    }
}

// Interface
interface Serializable {
    public function toJson(): string;
}

// Enum (PHP 8.1+)
enum Status: string {
    case Active = 'active';
    case Inactive = 'inactive';
    case Pending = 'pending';

    public function label(): string {
        return match($this) {
            Status::Active => 'Active',
            Status::Inactive => 'Inactive',
            Status::Pending => 'Pending Review',
        };
    }
}

$status = Status::Active;
echo $status->label();  // "Active"
```

### মিল এক্সপ্রেশন এবং কন্ট্রোল ফ্লো
```php
// Match expression (PHP 8.0+) — like switch but returns a value
$label = match($status) {
    'active' => 'Active User',
    'inactive' => 'Inactive User',
    'pending' => 'Pending Review',
    default => 'Unknown Status',
};

// Null coalescing
$name = $user['name'] ?? 'Guest';

// Nullsafe operator (PHP 8.0+)
$country = $user?->getAddress()?->getCountry()?->getName();

// Arrow functions (short closures)
$doubled = array_map(fn($n) => $n * 2, [1, 2, 3, 4, 5]);

// Named arguments + spread
$config = [...$defaults, ...$overrides];
```

---

## ইকোসিস্টেম
### ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | শৈলী | জন্য সেরা |
|------------|-------|----------|
| **লারাভেল** | ফুল-স্ট্যাক, মার্জিত সিনট্যাক্স | বেশিরভাগ ওয়েব অ্যাপ্লিকেশন; বৃহত্তম পিএইচপি ফ্রেমওয়ার্ক |
| **সিমফনি** | এন্টারপ্রাইজ, উপাদান ভিত্তিক | বড় এন্টারপ্রাইজ অ্যাপ্লিকেশন |
| **স্লিম** | মাইক্রো-ফ্রেমওয়ার্ক | API এবং ছোট অ্যাপ্লিকেশন |
| **ওয়ার্ডপ্রেস** | সিএমএস | ব্লগ, বিষয়বস্তু সাইট, ছোট ব্যবসা ওয়েবসাইট |
### প্রয়োজনীয় সরঞ্জাম
| টুল | উদ্দেশ্য |
|------|---------|
| **সুরকার** | নির্ভরতা ম্যানেজার (যেমন npm/pip) |
| **PHPUnit** | পরীক্ষার কাঠামো |
| **পিএইচপিস্টান / সাম** | স্ট্যাটিক বিশ্লেষণ (কোড ছাড়াই বাগ খুঁজে বের করে) |
| **লারাভেল পাল/পাল** | স্থানীয় উন্নয়ন পরিবেশ |
| **PSR মান** | কোডিং শৈলী এবং ইন্টারফেস মান |
---

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### PHPDoc এবং টেমপ্লেটের মাধ্যমে জেনেরিক
```php
<?php
declare(strict_types=1);

/**
 * @template T
 */
interface Repository {
    /** @param T $entity */
    public function save(object $entity): void;

    /** @return T|null */
    public function find(int $id): ?object;

    /** @return array<T> */
    public function findAll(): array;
}

/**
 * @implements Repository<User>
 */
class UserRepository implements Repository {
    public function save(object $entity): void { /* ... */ }
    public function find(int $id): ?object { return null; }
    public function findAll(): array { return []; }
}

// PHPStan/Psalm enforce generic constraints via @template annotations
```

### বৈশিষ্ট্য (PHP 8.0+) — নেটিভ টীকা
```php
// Built-in and custom attributes
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

#[Table(name: "users")]
class User {
    #[Column(name: "user_name")]
    public string $name;

    #[Column(name: "user_email", nullable: true)]
    public ?string $email;
}

// Reading attributes via reflection
$ref = new ReflectionClass(User::class);
$tableAttrs = $ref->getAttributes(Table::class);
$tableName = $tableAttrs[0]->newInstance()->name;  // "users"
```

### বন্ধ এবং উচ্চ ক্রম ফাংশন
```php
// Closures with use (capture variables)
$multiplier = 3;
$multiply = fn($x) => $x * $multiplier;
echo $multiply(5);  // 15

// Returning closures
function makeGreeter(string $greeting): Closure {
    return fn(string $name) => "$greeting, $name!";
}

$hello = makeGreeter("Hello");
echo $hello("Alice");  // "Hello, Alice!"

// Array reduce with closures
$users = [
    ["name" => "Alice", "age" => 30],
    ["name" => "Bob", "age" => 25],
    ["name" => "Charlie", "age" => 35],
];

$totalAge = array_reduce($users, fn(int $sum, array $u) => $sum + $u["age"], 0);
$names = array_map(fn($u) => $u["name"], $users);
$adults = array_filter($users, fn($u) => $u["age"] >= 30);
```

### ফাইবার (PHP 8.1+) — সমবায় মাল্টিটাস্কিং
```php
// Fibers — low-level cooperative concurrency
$fiber = new Fiber(function (): void {
    echo "Step 1\n";
    $value = Fiber::suspend("paused");
    echo "Step 2 with: $value\n";
    Fiber::suspend("paused again");
    echo "Step 3\n";
});

$fiber->start();              // Step 1
$resumed = $fiber->resume("hello");  // Step 2 with: hello
$fiber->resume("world");      // Step 3

// Fibers power async frameworks like Swoole and Revolt
```

### বৈশিষ্ট্য — অনুভূমিক কোড পুনঃব্যবহার
```php
// Traits — reusable method collections (PHP's solution to single inheritance)
trait HasTimestamps {
    public function createdAt(): string {
        return $this->created_at->format("Y-m-d H:i:s");
    }

    public function updatedAt(): string {
        return $this->updated_at->format("Y-m-d H:i:s");
    }
}

trait HasUuid {
    public function generateUuid(): string {
        return sprintf(
            "%04x%04x-%04x-%04x-%04x-%04x%04x%04x",
            mt_rand(0, 0xffff), mt_rand(0, 0xffff),
            mt_rand(0, 0xffff),
            mt_rand(0, 0x0fff) | 0x4000,
            mt_rand(0, 0x3fff) | 0x8000,
            mt_rand(0, 0xffff), mt_rand(0, 0xffff), mt_rand(0, 0xffff)
        );
    }
}

class Post {
    use HasTimestamps, HasUuid;

    public DateTime $created_at;
    public DateTime $updated_at;
    public string $id;

    public function __construct() {
        $this->id = $this->generateUuid();
        $this->created_at = new DateTime();
        $this->updated_at = new DateTime();
    }
}

$post = new Post();
echo $post->id;            // UUID string
echo $post->createdAt();   // "2024-01-15 14:30:00"
```

---

## সামঞ্জস্য এবং সমান্তরালতা
### সমবায় সমবায়ের জন্য ফাইবার
```php
// Fiber-based async with Revolt event loop
use Revolt\EventLoop;

EventLoop::queue(function () {
    $response = file_get_contents("https://api.example.com/users");
    echo "Users: " . strlen($response) . " bytes\n";
});

EventLoop::queue(function () {
    $response = file_get_contents("https://api.example.com/posts");
    echo "Posts: " . strlen($response) . " bytes\n";
});

EventLoop::run();
```

### Swoole — করুটিন-ভিত্তিক সঙ্গতি
```php
// Swoole enables Go-like concurrency in PHP
use Swoole\Coroutine;
use Swoole\Coroutine\Http\Client;

Coroutine\run(function () {
    // Concurrent HTTP requests
    $results = [];

    Coroutine::create(function () use (&$results) {
        $client = new Client("api.example.com", 443, true);
        $client->get("/users");
        $results["users"] = $client->body;
    });

    Coroutine::create(function () use (&$results) {
        $client = new Client("api.example.com", 443, true);
        $client->get("/posts");
        $results["posts"] = $client->body;
    });
});
```

### সমান্তরাল এক্সটেনশন
```php
// ext-parallel — true OS-level parallelism
use parallel\Runtime;
use parallel\Channel;

$runtime = new Runtime();

$future = $runtime->run(function(int $value): int {
    // This runs in a separate thread
    return $value * $value;
}, [42]);

$result = $future->value();  // 1764
echo $result;
```

---

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো (লারাভেল)
```
my-laravel-app/
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   ├── Middleware/
│   │   └── Requests/
│   ├── Models/
│   ├── Services/
│   └── Repositories/
├── config/
├── database/
│   ├── migrations/
│   ├── seeders/
│   └── factories/
├── resources/
│   ├── views/
│   └── css/
├── routes/
│   ├── web.php
│   └── api.php
├── tests/
│   ├── Feature/
│   └── Unit/
├── composer.json
├── composer.lock
├── phpunit.xml
├── .env
└── artisan
```

### composer.json — নির্ভরতা ব্যবস্থাপনা
```json
{
    "name": "my/app",
    "type": "project",
    "require": {
        "php": "^8.2",
        "laravel/framework": "^11.0",
        "guzzlehttp/guzzle": "^7.8",
        "predis/predis": "^2.2"
    },
    "require-dev": {
        "phpunit/phpunit": "^11.0",
        "phpstan/phpstan": "^1.10",
        "laravel/pint": "^1.14",
        "mockery/mockery": "^1.6"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/"
        }
    },
    "scripts": {
        "test": "phpunit",
        "analyse": "phpstan analyse",
        "format": "pint"
    }
}
```

### নির্ভরতা কমান্ড
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
```yaml
name: PHP CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_DATABASE: testing
          MYSQL_ROOT_PASSWORD: password
        ports: ["3306:3306"]
    steps:
      - uses: actions/checkout@v4
      - uses: shivammathur/setup-php@v2
        with:
          php-version: '8.3'
          extensions: mbstring, pdo_mysql
      - run: composer install --prefer-dist
      - run: php artisan migrate --env=testing
      - run: vendor/bin/phpunit
      - run: vendor/bin/phpstan analyse
      - run: vendor/bin/pint --test
```
---

## পরীক্ষা
### PHPUnit — টেস্টিং ফ্রেমওয়ার্ক
```php
<?php
declare(strict_types=1);

namespace Tests\Unit;

use PHPUnit\Framework\TestCase;
use App\Models\User;
use App\Services\UserService;

class UserServiceTest extends TestCase
{
    private UserService $service;

    protected function setUp(): void
    {
        $this->service = new UserService();
    }

    public function test_creates_user_with_valid_data(): void
    {
        $user = $this->service->create("Alice", "alice@example.com");

        $this->assertInstanceOf(User::class, $user);
        $this->assertEquals("Alice", $user->name);
    }

    public function test_throws_on_duplicate_email(): void
    {
        $this->service->create("Alice", "alice@example.com");

        $this->expectException(DuplicateEmailException::class);
        $this->service->create("Bob", "alice@example.com");
    }
}
```

### লারাভেল ফিচার টেস্ট
```php
<?php

namespace Tests\Feature;

use Tests\TestCase;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;

class UserApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_can_list_users(): void
    {
        User::factory()->count(3)->create();

        $response = $this->getJson("/api/users");

        $response->assertStatus(200)
                 ->assertJsonCount(3, "data");
    }

    public function test_can_create_user(): void
    {
        $response = $this->postJson("/api/users", [
            "name" => "Alice",
            "email" => "alice@example.com",
            "password" => "secret123",
        ]);

        $response->assertStatus(201)
                 ->assertJsonFragment(["name" => "Alice"]);

        $this->assertDatabaseHas("users", ["email" => "alice@example.com"]);
    }
}
```

### ঠাট্টা-বিদ্রুপ
```php
<?php

use Mockery;
use App\Services\PaymentService;
use App\Repositories\StripeRepository;

class PaymentServiceTest extends TestCase
{
    public function test_processes_payment(): void
    {
        $stripeMock = Mockery::mock(StripeRepository::class);
        $stripeMock->shouldReceive("charge")
            ->with(5000, "tok_visa")
            ->once()
            ->andReturn(["id" => "ch_123", "status" => "succeeded"]);

        $service = new PaymentService($stripeMock);
        $result = $service->process(5000, "tok_visa");

        $this->assertEquals("succeeded", $result["status"]);
    }

    protected function tearDown(): void
    {
        Mockery::close();
    }
}
```

### টেস্ট কমান্ড
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## ইন্টারঅপারেবিলিটি
### সি এক্সটেনশন
```php
// PHP extensions are written in C
// config.m4
PHP_ARG_ENABLE(myext, [Enable myext support])
if test "$PHP_MYEXT" != "no"; then
  PHP_NEW_EXTENSION(myext, myext.c, $ext_shared)
fi

// myext.c (simplified)
PHP_FUNCTION(myext_fast_hash) {
    char *data;
    size_t data_len;
    if (zend_parse_parameters(ZEND_NUM_ARGS(), "s", &data, &data_len) == FAILURE) {
        return;
    }
    unsigned long hash = 5381;
    for (size_t i = 0; i < data_len; i++) {
        hash = ((hash << 5) + hash) + data[i];
    }
    RETURN_LONG(hash);
}
```

### FFI — ফরেন ফাংশন ইন্টারফেস (PHP 7.4+)
```php
// PHP FFI — call C libraries without writing extensions
$ffi = FFI::cdef(
    "int printf(const char *format, ...);
     double sqrt(double x);",
    "libc.so.6"
);

$ffi->printf("Hello from C! %d\n", 42);
echo $ffi->sqrt(144.0);  // 12.0
```

### পিএসআর স্ট্যান্ডার্ড
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## ডিজাইন প্যাটার্ন
### ভান্ডার প্যাটার্ন
```php
interface UserRepositoryInterface {
    public function findById(int $id): ?User;
    public function findAll(): array;
    public function save(User $user): User;
}

class EloquentUserRepository implements UserRepositoryInterface {
    public function findById(int $id): ?User { return User::find($id); }
    public function findAll(): array { return User::all()->toArray(); }
    public function save(User $user): User { $user->save(); return $user; }
}

class UserController {
    public function __construct(private UserRepositoryInterface $repo) {}
    public function show(int $id): JsonResponse {
        return response()->json($this->repo->findById($id));
    }
}
```

### মিডলওয়্যার প্যাটার্ন
```php
class AuthenticationMiddleware {
    public function handle(ServerRequestInterface $request, callable $next): ResponseInterface {
        $token = $request->getHeaderLine("Authorization");
        if (empty($token) || !$this->validateToken($token)) {
            return new Response(401, body: "Unauthorized");
        }
        return $next($request);
    }
}
```

### সার্ভিস কন্টেইনার / ডিপেন্ডেন্সি ইনজেকশন
```php
class OrderService {
    public function __construct(
        private PaymentGateway $payment,
        private OrderRepository $orders,
        private Mailer $mailer,
    ) {}

    public function placeOrder(OrderRequest $request): Order {
        $order = $this->orders->create($request->toArray());
        $this->payment->charge($order->total, $request->token);
        $this->mailer->send(new OrderConfirmation($order));
        return $order;
    }
}

Route::post("/orders", function (OrderService $service, Request $request) {
    return $service->placeOrder(OrderRequest::from($request));
});
```
---

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### অপ্টিমাইজেশন কৌশল
```php
// 1. OPcache - bytecode caching (2-3x speedup)
// 2. Eager loading - avoid N+1 queries
$users = User::with("posts", "comments")->get();
// 3. Lazy collections for large datasets
// 4. Cache expensive operations
$value = Cache::remember("key", 3600, fn() => expensiveComputation());
// 5. PHP 8.x JIT: opcache.jit=1255
```

---

## স্থাপনা
### PHP-FPM + Nginx
```nginx
server {
    listen 80;
    server_name example.com;
    root /var/www/myapp/public;
    index index.php;
    location / { try_files $uri $uri/ /index.php?$query_string; }
    location ~ \.php$ {
        fastcgi_pass unix:/run/php/php8.3-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include fastcgi_params;
    }
}
```

### ডকার স্থাপনা
```dockerfile
FROM php:8.3-fpm-alpine
RUN docker-php-ext-install pdo pdo_mysql opcache
WORKDIR /var/www/html
COPY composer.json composer.lock ./
RUN composer install --no-dev --optimize-autoloader
COPY . .
EXPOSE 9000
CMD ["php-fpm"]
```
---

## কখন পিএইচপি ব্যবহার করবেন
| দৃশ্যকল্প | কেন পিএইচপি | ভাল বিকল্প |
|------------|---------|---------|
| ওয়ার্ডপ্রেস ডেভেলপমেন্ট | পিএইচপি একমাত্র বিকল্প | — |
| ফ্রিল্যান্স ওয়েব ডেভেলপমেন্ট | বিশাল বাজার; স্থাপন করা সহজ | — |
| ই-কমার্স (WooCommerce, Magento) | প্রতিষ্ঠিত PHP প্ল্যাটফর্ম | — |
| দ্রুত ওয়েব প্রোটোটাইপিং | কম সেটআপ, স্থাপন করতে দ্রুত | Node.js, Python |
| বিষয়বস্তু-ভারী ওয়েবসাইট | CMS ইকোসিস্টেম পরিপক্ক | — |
| APIs এবং microservices | লারাভেল/স্লিম দিয়ে সম্ভব | Go, Node.js, Python |
| CLI টুলস | সম্ভব কিন্তু আদর্শ নয় | যান, পাইথন, মরিচা |
| রিয়েল-টাইম অ্যাপ্লিকেশন | পিএইচপি এর শক্তি নয় | Node.js, Go |
| ডেটা সায়েন্স / এমএল | বাস্তুতন্ত্র নয় | পাইথন, আর |
| ডেস্কটপ/মোবাইল অ্যাপস | উপযুক্ত নয় | স্থানীয় ভাষা ব্যবহার করুন |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: PHP-তে`==`এবং`===`এর মধ্যে পার্থক্য কী?
**A:**`==`হল আলগা তুলনা — এটি তুলনা করার আগে টাইপ জবরদস্তি করে (`"0" == false`হল `true`)। `===`হল কঠোর তুলনা — এটি মান এবং প্রকার উভয়ই পরীক্ষা করে (`"0" === false` হল `false`)। সর্বদা`===`ব্যবহার করুন যদি না আপনার বিশেষভাবে টাইপ জবরদস্তির প্রয়োজন হয়। এটি PHP এর সবচেয়ে সাধারণ বাগগুলির একটি।
```php
// Loose comparison — type coercion (avoid)
var_dump(0 == "foo");     // true (PHP 7) — "foo" coerced to 0
var_dump(0 == "");        // true
var_dump(null == false);   // true
var_dump("" == null);      // true

// Strict comparison — no coercion (always prefer this)
var_dump(0 === "foo");    // false
var_dump(null === false);  // false
var_dump("" === null);     // false
var_dump(1 === 1);         // true
```

### প্রশ্ন 2: পিএইচপি নেমস্পেস এবং অটোলোডিং কীভাবে কাজ করে?
**A:** নেমস্পেস শ্রেণী নামের সংঘর্ষ প্রতিরোধ করে। PSR-4 অটোলোডিং ম্যাপস নেমস্পেস স্ট্রাকচার টু ডাইরেক্টরি স্ট্রাকচার —`App\Controllers\UserController`ম্যাপস to `src/Controllers/UserController.php`। কম্পোজার`composer.json`এর মাধ্যমে অটোলোডিং পরিচালনা করে। আধুনিক PHP-তে সর্বদা নেমস্পেস এবং PSR-4 ব্যবহার করুন।
```json
// composer.json
{
    "autoload": {
        "psr-4": {
            "App\\": "src/"
        }
    }
}
```

```php
// src/Controllers/UserController.php
namespace App\Controllers;

use App\Services\UserService;
use App\Models\User;

class UserController {
    public function __construct(
        private readonly UserService $userService
    ) {}

    public function show(string $id): User {
        return $this->userService->find($id);
    }
}
```

```bash
composer dump-autoload  # Regenerate autoloader after changes
```

### প্রশ্ন 3: PHP 8 অ্যাট্রিবিউটগুলি কী কী এবং সেগুলি কীভাবে ফ্রেমওয়ার্কের সাথে সম্পর্কিত?
**A:** বৈশিষ্ট্যগুলি (PHP 8) হল ক্লাস, পদ্ধতি, বৈশিষ্ট্য এবং প্যারামিটারগুলির জন্য কাঠামোগত মেটাডেটা টীকা৷ তারা জাভা টীকা বা C# বৈশিষ্ট্যের সমতুল্য পিএইচপি। Laravel এবং Symfony এর মতো ফ্রেমওয়ার্কগুলি রাউটিং, বৈধতা এবং নির্ভরতা ইনজেকশনের জন্য ব্যাপকভাবে ব্যবহার করে।
```php
use Attribute;

// Define a custom attribute
#[Attribute(Attribute::TARGET_METHOD)]
class Route {
    public function __construct(
        public readonly string $path,
        public readonly string $method = 'GET'
    ) {}
}

// Use attribute on controller method
class UserController {
    #[Route('/users/{id}', method: 'GET')]
    public function show(int $id): JsonResponse {
        $user = User::findOrFail($id);
        return new JsonResponse($user->toArray());
    }

    #[Route('/users', method: 'POST')]
    public function store(#[Validate(CreateUserRequest::class)] $request): JsonResponse {
        $user = User::create($request->validated());
        return new JsonResponse($user->toArray(), 201);
    }
}

// Read attributes via reflection
$ref = new ReflectionMethod(UserController::class, 'show');
$attrs = $ref->getAttributes(Route::class);
$route = $attrs[0]->newInstance();
echo $route->path;   // "/users/{id}"
echo $route->method; // "GET"
```

### প্রশ্ন 4: আধুনিক পিএইচপি-তে আমি কীভাবে ত্রুটিগুলি সঠিকভাবে পরিচালনা করব?
**A:** PHP-এ উভয় ত্রুটি (E_WARNING, E_NOTICE) এবং ব্যতিক্রম রয়েছে। আধুনিক পিএইচপি একচেটিয়াভাবে ব্যতিক্রম ব্যবহার করে। প্রত্যাশিত ব্যর্থতার জন্য চেষ্টা/ক্যাচ, ডোমেন ত্রুটির জন্য কাস্টম ব্যতিক্রম ক্লাস এবং ত্রুটিগুলিকে ব্যতিক্রমগুলিতে রূপান্তর করতে`set_error_handler`ব্যবহার করুন। PHP 7+`Throwable`হল ত্রুটি এবং ব্যতিক্রম উভয়ের জন্যই বেস ইন্টারফেস।
```php
// Custom exception hierarchy
class AppException extends \Exception {}
class NotFoundException extends AppException {}
class ValidationException extends AppException {
    public function __construct(
        public readonly array $errors,
        string $message = 'Validation failed'
    ) {
        parent::__construct($message);
    }
}

// Structured error handling
try {
    $user = $service->createUser($data);
} catch (ValidationException $e) {
    return response()->json(['errors' => $e->errors], 422);
} catch (NotFoundException $e) {
    return response()->json(['error' => $e->getMessage()], 404);
} catch (\Throwable $e) {
    Log::error('Unexpected error', ['exception' => $e]);
    return response()->json(['error' => 'Internal error'], 500);
}

// Convert PHP errors to exceptions
set_error_handler(function (int $severity, string $message, string $file, int $line) {
    throw new \ErrorException($message, 0, $severity, $file, $line);
});
```

### প্রশ্ন 5: পিএইচপি ফাইবারগুলি কী এবং তারা কীভাবে অ্যাসিঙ্কের সাথে সম্পর্কিত?
**A:** ফাইবারগুলি (PHP 8.1) হল হালকা ওজনের সমবায় থ্রেড - এগুলি স্থগিত করতে পারে এবং পুনরায় শুরু করতে পারে৷ তারা async PHP এর ভিত্তি কিন্তু নিম্ন-স্তরের। Amp এবং ReactPHP এর মত ফ্রেমওয়ার্ক অভ্যন্তরীণভাবে ফাইবার ব্যবহার করে। বেশিরভাগ অ্যাপ্লিকেশনের জন্য, কাঁচা ফাইবারের পরিবর্তে একটি অ্যাসিঙ্ক ফ্রেমওয়ার্ক ব্যবহার করুন।
```php
// Fiber basics
$fiber = new Fiber(function (): void {
    $value = Fiber::suspend('paused');  // Suspend, return value to caller
    echo "Resumed with: $value\n";
});

$result = $fiber->start();        // Runs until suspend — "paused"
$fiber->resume('hello');          // Resumes — "Resumed with: hello"

// Practical: non-blocking I/O simulation
function asyncRead(string $path): Fiber {
    return new Fiber(function () use ($path) {
        // Simulate async operation
        $data = Fiber::suspend();  // Yield control
        return $data;              // Resume with data
    });
}
```

---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি মিডলওয়্যার পাইপলাইন তৈরি করুন
**সমস্যা বিবৃতি:** একটি PHP ওয়েব ফ্রেমওয়ার্কের জন্য একটি মিডলওয়্যার পাইপলাইন প্রয়োগ করুন যেখানে প্রতিটি মিডলওয়্যার চেইনের পরবর্তী মিডলওয়্যারের আগে এবং পরে অনুরোধটি প্রক্রিয়া করতে পারে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) একটি`Middleware`ইন্টারফেস, (2) একটি পাইপলাইন যা মিডলওয়্যারকে চেইন করে, (3) প্রতিটি মিডলওয়্যার একটি অনুরোধ গ্রহণ করে এবং একটি`$next`কলব্যাক, (4) মিডলওয়্যার অনুরোধ (আগে) এবং প্রতিক্রিয়া (পরে) উভয়ই পরিবর্তন করতে পারে৷ এটি লারাভেল, PSR-15 এবং অনুরূপ কাঠামো দ্বারা ব্যবহৃত পেঁয়াজের মডেল।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
-`MiddlewareInterface`কে`process(Request, RequestHandler): Response`দিয়ে সংজ্ঞায়িত করুন।
- একটি একক হ্যান্ডলারে মিডলওয়্যার রচনা করতে অ্যারে হ্রাস ব্যবহার করুন।
- প্রতিটি মিডলওয়্যার পরেরটি মোড়ানো, নেস্টেড ফাংশন কল তৈরি করে।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
```php
<?php

interface MiddlewareInterface {
    public function process(Request $request, callable $next): Response;
}

class Pipeline {
    private array $middleware = [];

    public function pipe(MiddlewareInterface $middleware): self {
        $this->middleware[] = $middleware;
        return $this;
    }

    public function handle(Request $request, callable $destination): Response {
        $handler = array_reduce(
            array_reverse($this->middleware),
            fn(callable $next, MiddlewareInterface $mw) =>
                fn(Request $req) => $mw->process($req, $next),
            fn(Request $req) => $destination($req)
        );

        return $handler($request);
    }
}

// Middleware implementations
class CorsMiddleware implements MiddlewareInterface {
    public function process(Request $request, callable $next): Response {
        $response = $next($request);
        return $response
            ->withHeader('Access-Control-Allow-Origin', '*')
            ->withHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    }
}

class AuthMiddleware implements MiddlewareInterface {
    public function process(Request $request, callable $next): Response {
        $token = $request->getHeader('Authorization');
        if (!$token || !$this->validateToken($token)) {
            return new Response(401, body: json_encode(['error' => 'Unauthorized']));
        }
        $request = $request->withAttribute('user', $this->getUser($token));
        return $next($request);
    }

    private function validateToken(string $token): bool { /* ... */ return true; }
    private function getUser(string $token): array { return ['id' => 1, 'name' => 'Alice']; }
}

class LoggingMiddleware implements MiddlewareInterface {
    public function process(Request $request, callable $next): Response {
        $start = microtime(true);
        $response = $next($request);
        $duration = round((microtime(true) - $start) * 1000, 2);
        error_log("{$request->method()} {$request->path()} — {$response->status} ({$duration}ms)");
        return $response;
    }
}

// Usage
$pipeline = new Pipeline();
$pipeline
    ->pipe(new LoggingMiddleware())
    ->pipe(new CorsMiddleware())
    ->pipe(new AuthMiddleware());

$response = $pipeline->handle($request, function (Request $req): Response {
    return new Response(200, body: json_encode(['message' => 'Hello, World!']));
});
```

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- অর্ডারের বিষয়গুলি: প্রথম পাইপড = সবচেয়ে বাইরের (অনুরোধে প্রথমে কার্যকর করা হয়, প্রতিক্রিয়ায় শেষ)।
- প্রতিটি মিডলওয়্যার`$next`কল না করে একটি প্রতিক্রিয়া প্রদান করে শর্ট-সার্কিট করতে পারে৷
- উৎপাদন: যেকোনো PSR-15 ফ্রেমওয়ার্কের সাথে ইন্টারঅপারেবিলিটির জন্য PSR-15`MiddlewareInterface`ব্যবহার করুন।
### সমস্যা 2: ক্যোয়ারী বিল্ডারের সাথে একটি সংগ্রহস্থল প্রয়োগ করুন
**সমস্যা বিবৃতি:** একটি সাবলীল ক্যোয়ারী বিল্ডার তৈরি করুন যা প্যারামিটারাইজড ক্যোয়ারী সহ নিরাপদে SQL তৈরি করে, চেইনিং সমর্থন করে এবং একটি রিপোজিটরি প্যাটার্নের সাথে একীভূত করে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) চেইনযোগ্য পদ্ধতি সহ একটি`QueryBuilder`ক্লাস (`select`,`where`,`orderBy`,`limit`), (2) SQL ইনজেকশন প্রতিরোধ করার জন্য প্যারামিটারাইজড প্রশ্ন, (3) একটি XQZQKER5 ডেটা ব্যবহার করে যা XQZMARK5 তৈরি করে৷
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- বিল্ডার SQL টুকরা এবং পরামিতি জমা করে।
-`toSql()`স্থানধারকদের সাথে চূড়ান্ত প্রশ্ন তৈরি করে।
-`getParameters()`আবদ্ধ মান প্রদান করে।
- রিপোজিটরি ডোমেন-নির্দিষ্ট পদ্ধতির সাথে নির্মাতাকে মোড়ানো।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
```php
class QueryBuilder {
    private string $table;
    private array $columns = ['*'];
    private array $wheres = [];
    private array $params = [];
    private array $orderBy = [];
    private ?int $limit = null;
    private ?int $offset = null;

    public function __construct(string $table) { $this->table = $table; }

    public function select(string ...$columns): self {
        $this->columns = $columns;
        return $this;
    }

    public function where(string $column, string $operator, mixed $value): self {
        $this->wheres[] = "$column $operator ?";
        $this->params[] = $value;
        return $this;
    }

    public function whereEquals(string $column, mixed $value): self {
        return $this->where($column, '=', $value);
    }

    public function whereIn(string $column, array $values): self {
        $placeholders = implode(', ', array_fill(0, count($values), '?'));
        $this->wheres[] = "$column IN ($placeholders)";
        $this->params = array_merge($this->params, $values);
        return $this;
    }

    public function orderBy(string $column, string $direction = 'ASC'): self {
        $direction = strtoupper($direction) === 'DESC' ? 'DESC' : 'ASC';
        $this->orderBy[] = "$column $direction";
        return $this;
    }

    public function limit(int $limit): self { $this->limit = $limit; return $this; }
    public function offset(int $offset): self { $this->offset = $offset; return $this; }

    public function toSql(): string {
        $sql = "SELECT " . implode(', ', $this->columns) . " FROM {$this->table}";
        if ($this->wheres) $sql .= " WHERE " . implode(' AND ', $this->wheres);
        if ($this->orderBy) $sql .= " ORDER BY " . implode(', ', $this->orderBy);
        if ($this->limit !== null) $sql .= " LIMIT {$this->limit}";
        if ($this->offset !== null) $sql .= " OFFSET {$this->offset}";
        return $sql;
    }

    public function getParameters(): array { return $this->params; }
}

// Repository using the query builder
class UserRepository {
    public function __construct(private PDO $db) {}

    public function findActiveUsers(string $role, int $limit = 50): array {
        $query = (new QueryBuilder('users'))
            ->select('id', 'name', 'email')
            ->whereEquals('active', true)
            ->whereEquals('role', $role)
            ->orderBy('name')
            ->limit($limit);

        $stmt = $this->db->prepare($query->toSql());
        $stmt->execute($query->getParameters());
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}

// Generated SQL: SELECT id, name, email FROM users WHERE active = ? AND role = ? ORDER BY name ASC LIMIT 50
// Parameters: [true, "admin"]
```

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- এসকিউএল ইনজেকশন প্রতিরোধ: সমস্ত মান প্যারামিটারাইজড কোয়েরির মধ্য দিয়ে যায় (`?`স্থানধারক)।
- চেইনেবল API: প্রতিটি পদ্ধতি সাবলীল রচনার জন্য`$this`প্রদান করে।
- উত্পাদন: একটি ব্যাপক, পরীক্ষিত সমাধানের জন্য`illuminate/database`(Laravel এর ক্যোয়ারী নির্মাতা) বা`doctrine/dbal`ব্যবহার করুন৷
---

## সারাংশ
PHP হল ওয়েবের বাস্তবসম্মত ওয়ার্কহরস। এটি বেশিরভাগ ওয়েবসাইটকে ক্ষমতা দেয়, এর একটি বিশাল ইকোসিস্টেম রয়েছে এবং আধুনিক PHP (8.x) সঠিক প্রকার, এনাম এবং পরিষ্কার বাক্য গঠন সহ একটি সু-পরিকল্পিত ভাষা। এটি সবচেয়ে মার্জিত ভাষা নয়, এবং এটি প্রতিটি ডোমেনের জন্য উপযুক্ত নয় — তবে ওয়েব ডেভেলপমেন্ট, বিশেষ করে কন্টেন্ট ম্যানেজমেন্ট, ই-কমার্স এবং ফ্রিল্যান্সিংয়ের জন্য, PHP একটি ব্যবহারিক এবং ব্যাপকভাবে নিযুক্ত পছন্দ হিসেবে রয়ে গেছে।