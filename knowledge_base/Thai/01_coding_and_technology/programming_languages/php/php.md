---
# Metadata
title: "PHP"
description: "Comprehensive reference for the PHP programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "AI Model Training Team"
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

#พีพีพี
PHP (Hypertext Preprocessor) เป็นภาษาสคริปต์ฝั่งเซิร์ฟเวอร์ที่สร้างขึ้นโดย Rasmus Lerdorf ในปี 1994 และเปิดตัวครั้งแรกในปี 1995 เดิมทีออกแบบมาเพื่อสร้างหน้าเว็บแบบไดนามิก PHP ได้พัฒนาเป็นภาษาอเนกประสงค์ที่มีคุณสมบัติครบถ้วน ขับเคลื่อนประมาณ 75% ของเว็บไซต์ทั้งหมดที่มีภาษาฝั่งเซิร์ฟเวอร์ที่รู้จัก รวมถึง WordPress, Facebook (เดิม), Wikipedia, Slack และเว็บไซต์อื่น ๆ นับล้าน
Modern PHP (8.x) เป็นภาษาที่แตกต่างจาก PHP ในช่วงต้นทศวรรษ 2000 มาก ขณะนี้มีคุณสมบัติการพิมพ์ นิพจน์การจับคู่ การแจงนับ ไฟเบอร์ คลาสแบบอ่านอย่างเดียว และระบบประเภทที่แข็งแกร่ง แม้จะมีชื่อเสียงในหมู่นักพัฒนา (มักถูกวิพากษ์วิจารณ์ถึงความไม่สอดคล้องกัน) แต่ PHP นั้นใช้งานได้จริง มีการนำไปใช้งานอย่างกว้างขวาง และปรับปรุงอย่างต่อเนื่อง
---

## ทำไม PHP ถึงมีความสำคัญ
- **การครอบงำเว็บ**: รัน ~75% ของเว็บไซต์ WordPress เพียงอย่างเดียวขับเคลื่อน 43% ของเว็บ
- **อุปสรรคในการเข้าต่ำ**: ปรับใช้โดยการอัพโหลดไฟล์ไปยังโฮสติ้งที่ใช้ร่วมกัน ไม่มีการรวบรวม ไม่มีขั้นตอนการสร้าง
- **ระบบนิเวศที่สมบูรณ์**: Composer (ผู้จัดการแพ็คเกจ), Laravel, Symfony — เครื่องมือที่ผ่านการทดสอบการต่อสู้แล้ว
- **ใช้งานได้จริง**: ทำให้เว็บไซต์ไดนามิกทำงานได้ภายในไม่กี่นาทีด้วยการตั้งค่าเพียงเล็กน้อย
- **การปรับปรุงอย่างต่อเนื่อง**: PHP 8.x ได้นำมาซึ่งการปรับปรุงคุณภาพชีวิตที่สำคัญ
- **ตลาดฟรีแลนซ์**: ความต้องการอย่างมากสำหรับนักพัฒนา WordPress, Laravel และอีคอมเมิร์ซ (WooCommerce, Magento)
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **การตั้งชื่อไม่สอดคล้องกัน** | `strpos`กับ`str_replace`,`array_key_exists`กับ`in_array`— ไม่มีแบบแผนที่สอดคล้องกัน | เรียนรู้ความไม่สอดคล้องกัน ใช้ IDE เติมข้อความอัตโนมัติ |
| **สัมภาระทางประวัติศาสตร์** | คุณสมบัติและรูปแบบเดิมจาก PHP 5 และรุ่นก่อนหน้า | ใช้ PHP สมัยใหม่ (8.2+); ปฏิบัติตามมาตรฐาน PSR |
| **ประสิทธิภาพ** | ช้ากว่า Go, Rust หรือ Java สำหรับงานที่ไม่ใช่เว็บ | ใช้ OPcache; พิจารณา Swoole สำหรับ async; ใช้ PHP-FPM |
| **ไม่เหมาะสำหรับผู้ที่ไม่ใช้เว็บ** | CLI, เดสก์ท็อป, อุปกรณ์เคลื่อนที่, วิทยาศาสตร์ข้อมูล — ไม่ใช่จุดแข็งของ PHP | ใช้ Python, Go หรือภาษาอื่นสำหรับงานที่ไม่ใช่เว็บ |
| **ชื่อเสียงด้านความปลอดภัย** | รหัส PHP รุ่นเก่ามีปัญหาด้านความปลอดภัยมากมาย | ใช้กรอบงานที่ทันสมัย ปฏิบัติตามแนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัย |
---

## พื้นฐานไวยากรณ์
### โครงสร้างพื้นฐาน
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

### ฟังก์ชั่นและประเภท
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

### ชั้นเรียนและ OOP
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

### จับคู่นิพจน์และโฟลว์การควบคุม
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

## ระบบนิเวศ
### กรอบงาน
| กรอบ | สไตล์ | ดีที่สุดสำหรับ |
|----------|-------|----------|
| **ลาร์ราเวล** | ไวยากรณ์แบบเต็มสแต็กที่สวยงาม | เว็บแอปพลิเคชั่นส่วนใหญ่ กรอบ PHP ที่ใหญ่ที่สุด |
| **ซิมโฟนี่** | องค์กรแบบอิงคอมโพเนนต์ | แอปพลิเคชันระดับองค์กรขนาดใหญ่ |
| **ผอม** | ไมโครเฟรมเวิร์ก | API และแอปพลิเคชันขนาดเล็ก |
| **เวิร์ดเพรส** | ซีเอ็มเอส | บล็อก ไซต์เนื้อหา เว็บไซต์ธุรกิจขนาดเล็ก |
### เครื่องมือสำคัญ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ผู้แต่ง** | ตัวจัดการการพึ่งพา (เช่น npm/pip) |
| **PHPUnit** | กรอบการทดสอบ |
| **PHPStan / สดุดี** | การวิเคราะห์แบบคงที่ (ค้นหาข้อบกพร่องโดยไม่ต้องรันโค้ด) |
| **Laravel Sail / Herd** | สภาพแวดล้อมการพัฒนาท้องถิ่น |
| **มาตรฐาน PSR** | รูปแบบการเข้ารหัสและมาตรฐานอินเทอร์เฟซ |
---

## ไวยากรณ์และรูปแบบขั้นสูง
### ข้อมูลทั่วไปผ่าน PHPDoc และเทมเพลต
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

### คุณสมบัติ (PHP 8.0+) — คำอธิบายประกอบแบบเนทิฟ
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

### การปิดและฟังก์ชันลำดับที่สูงกว่า
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

### Fibers (PHP 8.1+) — มัลติทาสกิ้งแบบร่วมมือกัน
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

### ลักษณะ - การใช้โค้ดแนวนอนซ้ำ
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

## การเห็นพ้องต้องกันและความเท่าเทียม
### เส้นใยเพื่อการเห็นพ้องของสหกรณ์
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

### Swoole - เห็นพ้องต้องกันตาม Coroutine
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

### ส่วนขยายแบบขนาน
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ (Laravel)
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

### composer.json - การจัดการการพึ่งพา
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

### คำสั่งการพึ่งพา
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
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

## การทดสอบ
### PHPUnit - กรอบการทดสอบ
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

### การทดสอบคุณสมบัติ Laravel
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

### ล้อเลียนด้วยการเยาะเย้ย
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

### คำสั่งทดสอบ
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## การทำงานร่วมกัน
### ส่วนขยาย C
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

### FFI - อินเทอร์เฟซฟังก์ชันต่างประเทศ (PHP 7.4+)
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

### มาตรฐาน PSR
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## รูปแบบการออกแบบ
### รูปแบบพื้นที่เก็บข้อมูล
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

### รูปแบบมิดเดิลแวร์
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

### คอนเทนเนอร์บริการ / การพึ่งพาการฉีด
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### เครื่องมือสร้างโปรไฟล์
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### เทคนิคการเพิ่มประสิทธิภาพ
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

## การปรับใช้
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

### การปรับใช้นักเทียบท่า
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

## เมื่อใดจึงควรใช้ PHP
| สถานการณ์ | ทำไมต้อง PHP | ทางเลือกที่ดีกว่า |
|----------|---------|-------------------|
| การพัฒนา WordPress | PHP เป็นตัวเลือกเดียว | — |
| การพัฒนาเว็บไซต์อิสระ | ตลาดขนาดใหญ่ ง่ายต่อการปรับใช้ | — |
| อีคอมเมิร์ซ (WooCommerce, Magento) | ก่อตั้งแพลตฟอร์ม PHP | — |
| การสร้างต้นแบบเว็บอย่างรวดเร็ว | การตั้งค่าต่ำ ปรับใช้ได้อย่างรวดเร็ว | Node.js, หลาม |
| เว็บไซต์ที่มีเนื้อหาหนัก | ระบบนิเวศ CMS เติบโตเต็มที่ | — |
| API และไมโครเซอร์วิส | เป็นไปได้ด้วย Laravel/Slim | ไป, Node.js, Python |
| เครื่องมือ CLI | เป็นไปได้แต่ไม่เหมาะ | ไปเถอะ Python สนิม |
| แอพพลิเคชั่นเรียลไทม์ | ไม่ใช่จุดแข็งของ PHP | Node.js ไป |
| วิทยาศาสตร์ข้อมูล / ML | ไม่ใช่ระบบนิเวศ | หลาม, อาร์ |
| แอพเดสก์ท็อป/มือถือ | ไม่เหมาะ | ใช้ภาษาพื้นเมือง |
---

## สรุป
PHP เป็นม้าที่ใช้งานจริงของเว็บ มันขับเคลื่อนเว็บไซต์ส่วนใหญ่ มีระบบนิเวศขนาดใหญ่ และ PHP สมัยใหม่ (8.x) เป็นภาษาที่ได้รับการออกแบบมาอย่างดีพร้อมด้วยประเภท การแจกแจง และไวยากรณ์ที่เหมาะสม ภาษานี้ไม่ใช่ภาษาที่หรูหราที่สุด และไม่เหมาะกับทุกโดเมน แต่สำหรับการพัฒนาเว็บไซต์ โดยเฉพาะการจัดการเนื้อหา อีคอมเมิร์ซ และฟรีแลนซ์ PHP ยังคงเป็นตัวเลือกที่ใช้งานได้จริงและใช้กันอย่างแพร่หลาย