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

# پی ایچ پی
پی ایچ پی (ہائپر ٹیکسٹ پری پروسیسر) ایک سرور سائیڈ اسکرپٹنگ لینگویج ہے جسے 1994 میں Rasmus Lerdorf نے بنایا تھا اور پہلی بار 1995 میں ریلیز کیا گیا تھا۔ اصل میں متحرک ویب صفحات بنانے کے لیے ڈیزائن کیا گیا تھا، PHP ایک مکمل خصوصیات والی عام مقصد کی زبان میں تیار ہوا ہے۔ یہ تقریباً 75% تمام ویب سائٹس کو ایک معروف سرور سائیڈ لینگویج کے ساتھ طاقت دیتا ہے، بشمول ورڈپریس، فیس بک (اصل میں)، ویکیپیڈیا، سلیک، اور لاکھوں دیگر سائٹس۔
جدید پی ایچ پی (8.x) ابتدائی 2000 کی پی ایچ پی سے بہت مختلف زبان ہے۔ اب اس میں ٹائپ شدہ خصوصیات، میچ ایکسپریشنز، اینوم، فائبرز، صرف پڑھنے کی کلاسز، اور ایک مضبوط قسم کا نظام ہے۔ ڈویلپرز کے درمیان اس کی ساکھ کے باوجود (اکثر تضادات کی وجہ سے تنقید کی جاتی ہے)، پی ایچ پی عملی ہے، وسیع پیمانے پر تعینات ہے، اور بہتری کی طرف گامزن ہے۔
---

## کیوں پی ایچ پی کی اہمیت ہے۔
- **ویب کا غلبہ**: ~75% ویب سائٹس چلاتا ہے۔ ورڈپریس اکیلے ویب کے 43% کو طاقت دیتا ہے۔
- **داخلے میں کم رکاوٹ**: کسی بھی مشترکہ ہوسٹنگ پر فائلیں اپ لوڈ کرکے تعینات کریں۔ کوئی تالیف، کوئی تعمیراتی قدم نہیں۔
- **بالغ ماحولیاتی نظام**: کمپوزر (پیکیج مینیجر)، لاراول، سیمفونی — بالغ، جنگ کے ٹیسٹ ٹولز۔
- **عملی**: کم سے کم سیٹ اپ کے ساتھ منٹوں میں چلنے والی ایک متحرک ویب سائٹ حاصل کریں۔
- **مسلسل بہتری**: PHP 8.x نے زندگی کے معیار میں نمایاں بہتری لائی ہے۔
- **فری لانسنگ مارکیٹ**: ورڈپریس، لاراول، اور ای کامرس (WooCommerce، Magento) ڈویلپرز کی بہت زیادہ مانگ۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **متضاد نام** | `strpos`بمقابلہ`str_replace`,`array_key_exists`بمقابلہ`in_array`- کوئی مستقل کنونشن نہیں | تضادات سیکھیں؛ IDE خودکار تکمیل کا استعمال کریں |
| **تاریخی سامان** | PHP 5 اور اس سے پہلے کے لیجیسی خصوصیات اور پیٹرن | جدید پی ایچ پی استعمال کریں (8.2+)؛ PSR معیارات پر عمل کریں |
| **کارکردگی** | غیر ویب کاموں کے لیے Go، Rust، یا Java سے آہستہ | OPcache استعمال کریں؛ async کے لیے Swoole پر غور کریں؛ استعمال کریں PHP-FPM |
| **غیر ویب کے لیے مثالی نہیں** | CLI، ڈیسک ٹاپ، موبائل، ڈیٹا سائنس - پی ایچ پی کی طاقت نہیں۔ غیر ویب کام کے لیے Python، Go، یا دوسری زبانیں استعمال کریں۔
| **سیکیورٹی ساکھ** | لیگیسی پی ایچ پی کوڈ میں سیکیورٹی کے بہت سے مسائل ہیں۔ جدید فریم ورک استعمال کریں؛ سیکورٹی کے بہترین طریقوں پر عمل کریں |
---

## نحوی بنیادی باتیں
### بنیادی ڈھانچہ
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

### افعال اور اقسام
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

### کلاسز اور او او پی
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

### مماثل اظہار اور کنٹرول فلو
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

## ماحولیاتی نظام
### فریم ورک
| فریم ورک | انداز | کے لیے بہترین |
|------------|-------|------------|
| **لاراول** | مکمل اسٹیک، خوبصورت نحو | زیادہ تر ویب ایپلیکیشنز؛ سب سے بڑا پی ایچ پی فریم ورک |
| **سمفونی** | انٹرپرائز، اجزاء پر مبنی | بڑے انٹرپرائز ایپلی کیشنز |
| **پتلا** | مائیکرو فریم ورک | APIs اور چھوٹی ایپلی کیشنز |
| **ورڈپریس** | CMS | بلاگز، مواد کی سائٹس، چھوٹے کاروباری ویب سائٹس |
### ضروری ٹولز
| ٹول | مقصد |
|------|---------|
| **موسیقار** | انحصار مینیجر (جیسے npm/pip) |
| **PHPUnit** | جانچ کا فریم ورک |
| **PHPStan / زبور** | جامد تجزیہ (کوڈ چلائے بغیر کیڑے تلاش کرتا ہے) |
| **لاریول سیل / ریوڑ** | مقامی ترقی کے ماحول |
| **PSR معیارات** | کوڈنگ سٹائل اور انٹرفیس کے معیارات |
---

## اعلی درجے کی نحو اور نمونے۔
### PHPDoc اور ٹیمپلیٹس کے ذریعے جنرک
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

### اوصاف (PHP 8.0+) — مقامی تشریحات
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

### بندش اور اعلی آرڈر کے افعال
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

### فائبرز (PHP 8.1+) - کوآپریٹو ملٹی ٹاسکنگ
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

### خصائص — افقی کوڈ دوبارہ استعمال کریں۔
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

## ہم آہنگی اور ہم آہنگی
### کوآپریٹو ہم آہنگی کے لیے فائبر
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

### سوول — کوروٹائن پر مبنی ہم آہنگی۔
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

### متوازی توسیع
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ (Laravel)
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

### composer.json — انحصار کا انتظام
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

### انحصار کے احکامات
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### PHPUnit - ٹیسٹنگ فریم ورک
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

### لاریول فیچر ٹیسٹ
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

### طنز کے ساتھ طنز
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

### ٹیسٹ کمانڈز
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## انٹرآپریبلٹی
### C ایکسٹینشنز
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

### FFI — غیر ملکی فنکشن انٹرفیس (PHP 7.4+)
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

### PSR معیارات
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## ڈیزائن پیٹرن
### ذخیرہ پیٹرن
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

### مڈل ویئر پیٹرن
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

### سروس کنٹینر / انحصار انجیکشن
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### اصلاح کی تکنیک
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

## تعیناتی۔
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

### ڈاکر کی تعیناتی۔
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

## پی ایچ پی کب استعمال کریں۔
| منظر نامہ | کیوں پی ایچ پی | بہتر متبادل |
|------------|---------|-------------------|
| ورڈپریس کی ترقی | پی ایچ پی ہی واحد آپشن ہے۔ - |
| فری لانس ویب ڈویلپمنٹ | بڑی مارکیٹ؛ تعینات کرنے کے لئے آسان | - |
| ای کامرس (WooCommerce, Magento) | پی ایچ پی پلیٹ فارمز کا قیام - |
| ریپڈ ویب پروٹو ٹائپنگ | کم سیٹ اپ، تعینات کرنے کے لیے تیز | Node.js, Python |
| مواد سے بھرپور ویب سائٹس | CMS ماحولیاتی نظام بالغ ہے | - |
| APIs اور مائیکرو سروسز | Laravel/Slim کے ساتھ ممکن ہے | Go, Node.js, Python |
| CLI ٹولز | ممکن ہے لیکن مثالی نہیں | جاؤ، ازگر، مورچا |
| ریئل ٹائم ایپلی کیشنز | پی ایچ پی کی طاقت نہیں | Node.js, Go |
| ڈیٹا سائنس / ایم ایل | ماحولیاتی نظام نہیں | ازگر، آر |
| ڈیسک ٹاپ/موبائل ایپس | مناسب نہیں | مقامی زبانیں استعمال کریں |
---

## مصنوعی سوال و جواب
### Q1: PHP میں`==`اور`===`میں کیا فرق ہے؟
**A:**`==`ڈھیلا موازنہ ہے — یہ موازنہ کرنے سے پہلے قسم کا جبر کرتا ہے (`"0" == false``true`ہے)۔ `===`سخت موازنہ ہے — یہ قدر اور قسم دونوں کو چیک کرتا ہے (`"0" === false``false`ہے)۔ ہمیشہ`===`استعمال کریں جب تک کہ آپ کو خاص طور پر قسم کے جبر کی ضرورت نہ ہو۔ یہ پی ایچ پی کے کیڑے کے سب سے عام ذرائع میں سے ایک ہے۔
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

### Q2: PHP نام کی جگہیں اور آٹو لوڈنگ کیسے کام کرتی ہیں؟
**A:** نام کی جگہیں کلاس کے ناموں کے تصادم کو روکتی ہیں۔ PSR-4 آٹو لوڈنگ نقشوں کے نام کی جگہ کے ڈھانچے کو ڈائرکٹری ڈھانچے میں کرتا ہے —`App\Controllers\UserController`نقشے کو`src/Controllers/UserController.php`میں۔ کمپوزر`composer.json`کے ذریعے آٹو لوڈنگ کو ہینڈل کرتا ہے۔ جدید پی ایچ پی میں ہمیشہ نام کی جگہیں اور PSR-4 استعمال کریں۔
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

### Q3: PHP 8 کی خصوصیات کیا ہیں، اور وہ فریم ورک سے کیسے متعلق ہیں؟
**A:** صفات (PHP 8) کلاسز، طریقوں، خصوصیات اور پیرامیٹرز کے لیے ساختی میٹا ڈیٹا تشریحات ہیں۔ وہ جاوا تشریحات یا C# صفات کے PHP کے برابر ہیں۔ Laravel اور Symfony جیسے فریم ورک انہیں روٹنگ، توثیق اور انحصار انجیکشن کے لیے بڑے پیمانے پر استعمال کرتے ہیں۔
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

### Q4: میں جدید پی ایچ پی میں غلطیوں کو صحیح طریقے سے کیسے ہینڈل کروں؟
**A:** PHP میں دونوں غلطیاں (E_WARNING, E_NOTICE) اور مستثنیات ہیں۔ جدید پی ایچ پی مستثنیات کو خصوصی طور پر استعمال کرتا ہے۔ متوقع ناکامیوں کے لیے ٹرائی/کیچ، ڈومین کی غلطیوں کے لیے حسب ضرورت استثنائی کلاسز، اور غلطیوں کو مستثنیات میں تبدیل کرنے کے لیے`set_error_handler`کا استعمال کریں۔ PHP 7+`Throwable`غلطیوں اور استثناء دونوں کے لیے بنیادی انٹرفیس ہے۔
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

### Q5: PHP فائبرز کیا ہیں، اور ان کا async سے کیا تعلق ہے؟
**A:** فائبرز (PHP 8.1) ہلکے وزن والے کوآپریٹو تھریڈز ہیں — وہ معطل اور عملدرآمد کو دوبارہ شروع کر سکتے ہیں۔ وہ async PHP کی بنیاد ہیں لیکن کم درجے کے ہیں۔ Amp اور ReactPHP جیسے فریم ورک اندرونی طور پر فائبر کا استعمال کرتے ہیں۔ زیادہ تر ایپلیکیشنز کے لیے، خام ریشوں کے بجائے ایک async فریم ورک استعمال کریں۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ایک مڈل ویئر پائپ لائن بنائیں
**مسئلہ کا بیان:** پی ایچ پی ویب فریم ورک کے لیے ایک مڈل ویئر پائپ لائن لاگو کریں جہاں ہر مڈل ویئر سلسلہ میں اگلے مڈل ویئر سے پہلے اور بعد میں درخواست پر کارروائی کرسکتا ہے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) ایک`Middleware`انٹرفیس، (2) ایک پائپ لائن جو مڈل ویئر کو زنجیروں میں جکڑتی ہے، (3) ہر مڈل ویئر کو ایک درخواست موصول ہوتی ہے اور ایک`$next`کال بیک، (4) مڈل ویئر درخواست (پہلے) اور جواب (بعد) دونوں میں ترمیم کر سکتا ہے۔ یہ پیاز کا ماڈل ہے جو Laravel، PSR-15، اور اسی طرح کے فریم ورک کے ذریعے استعمال کیا جاتا ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
-`MiddlewareInterface`کی وضاحت`process(Request, RequestHandler): Response`کے ساتھ کریں۔
- ایک ہی ہینڈلر میں مڈل ویئر کو تحریر کرنے کے لیے سرنی میں کمی کا استعمال کریں۔
- ہر مڈل ویئر اگلے کو لپیٹتا ہے، نیسٹڈ فنکشن کالز بناتا ہے۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- آرڈر کے معاملات: پہلا پائپڈ = سب سے باہر (درخواست پر پہلے پھانسی دی گئی، جواب پر آخری)۔
- ہر مڈل ویئر`$next`کو کال کیے بغیر جواب دے کر شارٹ سرکٹ کر سکتا ہے۔
- پیداوار: کسی بھی PSR-15 فریم ورک کے ساتھ انٹرآپریبلٹی کے لیے PSR-15`MiddlewareInterface`استعمال کریں۔
### مسئلہ 2: Query Builder کے ساتھ ایک ذخیرہ نافذ کریں۔
**مسئلہ کا بیان:** ایک روانی سے استفسار کرنے والا تیار کریں جو پیرامیٹرائزڈ استفسارات کے ساتھ محفوظ طریقے سے SQL تیار کرتا ہے، چیننگ کو سپورٹ کرتا ہے، اور ریپوزٹری پیٹرن کے ساتھ مربوط ہوتا ہے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) ایک`QueryBuilder`کلاس جس میں سلسلہ بندی کے طریقوں (`select`,`where`,`orderBy`,`limit`)، (2) SQL انجیکشن کو روکنے کے لیے پیرامیٹرائزڈ سوالات، (3) ایک XQZQERK5 ڈیٹا تک رسائی کے لیے استعمال کرتا ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- بلڈر ایس کیو ایل کے ٹکڑے اور پیرامیٹرز جمع کرتا ہے۔
-`toSql()`پلیس ہولڈرز کے ساتھ حتمی سوال پیدا کرتا ہے۔
-`getParameters()`پابند اقدار واپس کرتا ہے۔
- ذخیرہ ڈومین کے مخصوص طریقوں سے بلڈر کو لپیٹ دیتا ہے۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- SQL انجیکشن کی روک تھام: تمام اقدار پیرامیٹرائزڈ سوالات (`?` پلیس ہولڈرز) سے گزرتی ہیں۔
- Chainable API: ہر طریقہ روانی کی ساخت کے لیے`$this`لوٹاتا ہے۔
- پیداوار: ایک جامع، آزمائشی حل کے لیے`illuminate/database`(Laravel's query builder) یا`doctrine/dbal`استعمال کریں۔
---

## خلاصہ
پی ایچ پی ویب کا عملی کام کرنے والا ہارس ہے۔ یہ ویب سائٹس کی اکثریت کو طاقت دیتا ہے، اس کا ایک بہت بڑا ماحولیاتی نظام ہے، اور جدید پی ایچ پی (8.x) ایک اچھی طرح سے ڈیزائن کی گئی زبان ہے جس میں مناسب اقسام، انوم، اور صاف نحو ہے۔ یہ سب سے خوبصورت زبان نہیں ہے، اور یہ ہر ڈومین کے لیے موزوں نہیں ہے — لیکن ویب ڈویلپمنٹ، خاص طور پر مواد کے انتظام، ای کامرس، اور فری لانسنگ کے لیے، PHP ایک عملی اور وسیع پیمانے پر ملازمت کا انتخاب ہے۔