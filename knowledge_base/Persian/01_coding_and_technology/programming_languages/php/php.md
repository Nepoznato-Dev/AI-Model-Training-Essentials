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
# PHP
PHP (پیش پردازشگر فرامتن) یک زبان برنامه نویسی سمت سرور است که توسط Rasmus Lerdorf در سال 1994 ایجاد شد و اولین بار در سال 1995 منتشر شد. PHP که در ابتدا برای تولید صفحات وب پویا طراحی شده بود، به یک زبان همه منظوره با امکانات کامل تبدیل شده است. تقریباً 75٪ از تمام وب سایت ها با زبان سمت سرور شناخته شده، از جمله WordPress، Facebook (در اصل)، Wikipedia، Slack و میلیون ها سایت دیگر را تامین می کند.
PHP مدرن (8.x) یک زبان بسیار متفاوت از PHP در اوایل دهه 2000 است. اکنون دارای ویژگی‌های تایپ شده، عبارات مطابقت، enums، فیبرها، کلاس‌های فقط خواندنی و یک سیستم نوع قوی است. علیرغم شهرت آن در میان توسعه دهندگان (اغلب به دلیل ناسازگاری مورد انتقاد قرار می گیرد)، PHP عملی است، به طور گسترده مستقر شده است و همچنان در حال بهبود است.
---

## چرا PHP مهم است
- **تسلط بر وب**: 75% از وب سایت ها را اجرا می کند. وردپرس به تنهایی 43 درصد از وب را در اختیار دارد.
- **موانع کم برای ورود **: با آپلود فایل ها در هر هاست اشتراکی مستقر می شود. بدون کامپایل، بدون مرحله ساخت.
- **اکوسیستم بالغ**: آهنگساز (مدیر بسته)، Laravel، Symfony - ابزارهای بالغ و آزمایش شده در نبرد.
- **عملی**: یک وب سایت پویا را در عرض چند دقیقه با حداقل راه اندازی اجرا کنید.
- **بهبود مستمر**: PHP 8.x بهبودهای قابل توجهی در کیفیت زندگی به ارمغان آورده است.
- **بازار فریلنسینگ**: تقاضای زیاد برای توسعه دهندگان وردپرس، لاراول و تجارت الکترونیک (ووکامرس، مجنتو).
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **نامگذاری ناسازگار** | `strpos`در مقابل`str_replace`,`array_key_exists`در مقابل`in_array`— بدون قرارداد منسجم | ناسازگاری ها را بیاموزید؛ استفاده از IDE تکمیل خودکار |
| **توشه تاریخی** | ویژگی ها و الگوهای قدیمی از PHP 5 و پیش از آن | استفاده از PHP مدرن (8.2+)؛ پیروی از استانداردهای PSR |
| **عملکرد** | کندتر از Go، Rust یا Java برای کارهای غیر وب | از OPcache استفاده کنید. Swoole را برای async در نظر بگیرید. استفاده از PHP-FPM |
| **برای غیر وب ایده آل نیست** | CLI، دسکتاپ، موبایل، علم داده – نه نقاط قوت PHP | از Python، Go یا زبان های دیگر برای کارهای غیر وب استفاده کنید |
| **شهرت امنیتی** | کد PHP قدیمی دارای مشکلات امنیتی بسیاری است | استفاده از چارچوب های مدرن؛ بهترین شیوه های امنیتی را دنبال کنید |
---

## اصول نحو
### ساختار اساسی
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

### توابع و انواع
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

### کلاس ها و OOP
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

### تطبیق عبارت و جریان کنترل
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

## اکوسیستم
### چارچوب
| چارچوب | سبک | بهترین برای |
|-----------|-------|----------|
| **لاراول** | سینتکس کامل و زیبا | اکثر برنامه های کاربردی وب؛ بزرگترین فریم ورک پی اچ پی |
| **سیمفونی** | سازمانی، مبتنی بر جزء | برنامه های کاربردی سازمانی بزرگ |
| **لاغر** | میکرو فریمورک | API ها و برنامه های کاربردی کوچک |
| **وردپرس** | CMS | وبلاگ ها، سایت های محتوا، وب سایت های کسب و کار کوچک |
### ابزارهای ضروری
| ابزار | هدف |
|------|---------|
| **آهنگساز** | مدیر وابستگی (مانند npm/pip) |
| **PHPUnit** | چارچوب تست |
| **PHPStan / Psalm** | تجزیه و تحلیل استاتیک (باگ ها را بدون کد در حال اجرا پیدا می کند) |
| **بادبان لاراول / گله** | محیط های توسعه محلی |
| **استانداردهای PSR** | استانداردهای سبک کدنویسی و رابط |
---

## نحو و الگوهای پیشرفته
### ژنریک از طریق PHPDoc و الگوها
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

### ویژگی ها (PHP 8.0+) - حاشیه نویسی های بومی
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

### بسته شدن و عملکردهای بالاتر
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

### فیبرها (PHP 8.1+) - چندوظیفه ای مشترک
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

### صفات - استفاده مجدد از کد افقی
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

## همزمانی و موازی
### فیبرها برای همزمانی تعاونی
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

### Swoole - همزمانی مبتنی بر کوروتین
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

### پسوند موازی
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه (لاراول)
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

### composer.json — مدیریت وابستگی
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

### دستورات وابستگی
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### PHPUnit - چارچوب تست
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

### تست های ویژگی لاراول
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

### تمسخر با تمسخر
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

### دستورات تست
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## قابلیت همکاری
### برنامه های افزودنی C
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

### FFI - رابط عملکرد خارجی (PHP 7.4+)
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

### استانداردهای PSR
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## الگوهای طراحی
### الگوی مخزن
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

### الگوی میان افزار
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

### ظرف خدمات / تزریق وابستگی
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### تکنیک های بهینه سازی
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

## استقرار
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

### استقرار داکر
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

## چه زمانی از PHP استفاده کنیم
| سناریو | چرا PHP | جایگزین بهتر |
|----------|---------|-------------------|
| توسعه وردپرس | PHP تنها گزینه | — |
| توسعه وب آزاد | بازار بزرگ؛ آسان برای استقرار | — |
| تجارت الکترونیک (ووکامرس، مجنتو) | پلتفرم های پی اچ پی تاسیس شد | — |
| نمونه سازی سریع وب | راه اندازی کم، سریع برای استقرار | Node.js، Python |
| وب سایت های پر محتوا | اکوسیستم CMS بالغ است | — |
| API ها و میکروسرویس ها | با لاراول/اسلیم امکان پذیر است | برو، Node.js، پایتون |
| ابزارهای CLI | ممکن است اما ایده آل نیست | برو، پایتون، زنگ |
| برنامه های بلادرنگ | نه قدرت PHP | Node.js، برو |
| علم داده / ML | نه اکوسیستم | پایتون، R |
| برنامه های دسکتاپ/موبایل | مناسب نیست | استفاده از زبان های مادری |
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت`==`و`===`در PHP چیست؟
**الف:**`==`یک مقایسه ضعیف است - قبل از مقایسه، نوع اجبار را انجام می دهد (`"0" == false``true`است). `===`مقایسه دقیقی است - هم مقدار و هم نوع را بررسی می کند (`"0" === false``false`است). همیشه از`===`استفاده کنید مگر اینکه به طور خاص به اجبار نوع نیاز داشته باشید. این یکی از رایج ترین منابع PHP برای اشکالات است.
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

### Q2: فضاهای نام PHP و بارگذاری خودکار چگونه کار می کنند؟
**A:** فضای نام از برخورد نام کلاس جلوگیری می کند. PSR-4 نقشه های بارگذاری خودکار ساختار فضای نام به ساختار دایرکتوری — نقشه های`App\Controllers\UserController`به `src/Controllers/UserController.php`. Composer بارگیری خودکار را از طریق`composer.json`انجام می دهد. همیشه از فضاهای نام و PSR-4 در PHP مدرن استفاده کنید.
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

### Q3: ویژگی های PHP 8 چیست و چگونه با فریمورک ها ارتباط دارند؟
**A:** ویژگی ها (PHP 8) حاشیه نویسی های فراداده ساختار یافته برای کلاس ها، روش ها، ویژگی ها و پارامترها هستند. آنها معادل PHP حاشیه نویسی جاوا یا ویژگی های C# هستند. فریم ورک هایی مانند Laravel و Symfony به طور گسترده از آنها برای مسیریابی، اعتبارسنجی و تزریق وابستگی استفاده می کنند.
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

### Q4: چگونه خطاها را به درستی در PHP مدرن مدیریت کنم؟
**A:** PHP هم خطا دارد (E_WARNING، E_NOTICE) و هم استثنا. PHP مدرن منحصراً از استثناها استفاده می کند. از try/catch برای خرابی های مورد انتظار، کلاس های استثنای سفارشی برای خطاهای دامنه و`set_error_handler`برای تبدیل خطاها به استثنا استفاده کنید. PHP 7+`Throwable`رابط پایه برای خطاها و استثناها است.
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

### Q5: فیبرهای PHP چیست و چگونه با async ارتباط دارند؟
**A:** فیبرها (PHP 8.1) رشته های همکاری سبک وزن هستند - آنها می توانند اجرا را به حالت تعلیق درآورند و از سر بگیرند. آنها پایه و اساس PHP غیر همگام هستند اما سطح پایینی دارند. فریم ورک هایی مانند Amp و ReactPHP از فیبرها به صورت داخلی استفاده می کنند. برای اکثر برنامه ها، به جای الیاف خام، از یک چارچوب غیر همگام استفاده کنید.
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: یک خط لوله میان افزار بسازید
**بیانیه مشکل:** یک خط لوله میان افزار برای یک چارچوب وب PHP اجرا کنید که در آن هر میان افزار می تواند درخواست را قبل و بعد از میان افزار بعدی در زنجیره پردازش کند.
** مرحله 1 - مشکل را درک کنید:**
ما به این موارد نیاز داریم: (1) یک رابط `Middleware`، (2) یک خط لوله که میان افزار را زنجیره می کند، (3) هر میان افزار یک درخواست دریافت می کند و یک پاسخ تماس `$next`، (4) میان افزار می تواند درخواست (قبل) و پاسخ (بعد) را تغییر دهد. این مدل پیاز مورد استفاده لاراول، PSR-15 و فریمورک های مشابه است.
** مرحله 2 - شناسایی رویکرد: **
-`MiddlewareInterface`را با`process(Request, RequestHandler): Response`تعریف کنید.
- از کاهش آرایه برای ترکیب میان افزار به یک کنترل کننده استفاده کنید.
- هر میان افزار بعدی را پیچیده می کند و فراخوانی های تابع تو در تو را ایجاد می کند.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- موارد سفارش: اولین لوله = بیرونی ترین (اول در صورت درخواست اجرا می شود، آخرین در پاسخ).
- هر میان افزاری می تواند با بازگرداندن یک پاسخ بدون فراخوانی`$next`اتصال کوتاه کند.
- تولید: از PSR-15`MiddlewareInterface`برای قابلیت همکاری با هر چارچوب PSR-15 استفاده کنید.
### مشکل 2: یک مخزن با Query Builder پیاده سازی کنید
**بیانیه مشکل:** یک سازنده پرس و جو روان بسازید که SQL را به صورت ایمن با پرس و جوهای پارامتری تولید می کند، از زنجیره زدن پشتیبانی می کند و با الگوی مخزن ادغام می شود.
** مرحله 1 - مشکل را درک کنید:**
ما به این موارد نیاز داریم: (1) یک کلاس`QueryBuilder`با متدهای زنجیره‌ای (`select`، `where`، `orderBy`، `limit`)، (2) پرس‌و‌جوهای پارامتری شده برای جلوگیری از تزریق SQL، (3) که از داده‌ساز برای دسترسی به XQZ استفاده می‌کند.
** مرحله 2 - شناسایی رویکرد: **
- Builder قطعات و پارامترهای SQL را جمع می کند.
-`toSql()`پرس و جو نهایی را با متغیرهایی تولید می کند.
-`getParameters()`مقادیر محدود شده را برمی گرداند.
- Repository سازنده را با روش های خاص دامنه می پوشاند.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- جلوگیری از تزریق SQL: همه مقادیر از طریق پرس‌و‌جوهای پارامتری شده (جای‌بان‌های `?`) عبور می‌کنند.
- Chainable API: هر روش`$this`را برای ترکیب روان برمی گرداند.
- تولید: از`illuminate/database`(سازنده پرس و جو لاراول) یا`doctrine/dbal`برای یک راه حل جامع و آزمایش شده استفاده کنید.
---

## خلاصه
پی‌اچ‌پی ابزار عملگرایانه وب است. اکثر وب‌سایت‌ها را قدرت می‌دهد، اکوسیستم عظیمی دارد و PHP مدرن (8.x) یک زبان خوب طراحی شده با انواع مناسب، enums و نحو تمیز است. این زبان ظریف‌ترین زبان نیست، و برای هر دامنه مناسب نیست – اما برای توسعه وب، به‌ویژه مدیریت محتوا، تجارت الکترونیک و مشاغل آزاد، PHP یک انتخاب عملی و پرکاربرد باقی می‌ماند.