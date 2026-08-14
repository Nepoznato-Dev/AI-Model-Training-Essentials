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

#PHP
PHP (Bộ tiền xử lý siêu văn bản) là ngôn ngữ kịch bản phía máy chủ được Rasmus Lerdorf tạo ra vào năm 1994 và phát hành lần đầu tiên vào năm 1995. Ban đầu được thiết kế để tạo các trang web động, PHP đã phát triển thành một ngôn ngữ có mục đích chung đầy đủ tính năng. Nó hỗ trợ khoảng 75% tất cả các trang web có ngôn ngữ phía máy chủ đã biết, bao gồm WordPress, Facebook (ban đầu), Wikipedia, Slack và hàng triệu trang web khác.
PHP hiện đại (8.x) là một ngôn ngữ rất khác so với PHP đầu những năm 2000. Hiện tại nó có các thuộc tính được gõ, biểu thức khớp, enum, sợi, lớp chỉ đọc và một hệ thống kiểu mạnh mẽ. Bất chấp danh tiếng của nó trong giới phát triển (thường bị chỉ trích vì thiếu nhất quán), PHP vẫn thực tế, được triển khai rộng rãi và tiếp tục cải tiến.
---

## Tại sao PHP lại quan trọng
- **Sự thống trị của trang web**: Chạy ~75% số trang web. Chỉ riêng WordPress đã chiếm tới 43% trang web.
- **Rào cản gia nhập thấp**: Triển khai bằng cách tải tệp lên bất kỳ dịch vụ lưu trữ chia sẻ nào. Không biên dịch, không có bước xây dựng.
- **Hệ sinh thái trưởng thành**: Trình soạn thảo (trình quản lý gói), Laravel, Symfony — các công cụ trưởng thành, đã được thử nghiệm trong thực tế.
- **Thực tế**: Có được một trang web động chạy trong vài phút với thiết lập tối thiểu.
- **Cải tiến liên tục**: PHP 8.x đã mang lại những cải tiến đáng kể về chất lượng cuộc sống.
- **Thị trường làm việc tự do**: Nhu cầu lớn đối với các nhà phát triển WordPress, Laravel và thương mại điện tử (WooCommerce, Magento).
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Đặt tên không nhất quán** | `strpos`so với `str_replace`,`array_key_exists`so với`in_array`- không có quy ước nhất quán | Tìm hiểu sự không nhất quán; sử dụng tính năng tự động hoàn thành của IDE |
| **Hành trang lịch sử** | Các tính năng và mẫu kế thừa từ PHP 5 trở về trước | Sử dụng PHP hiện đại (8.2+); theo tiêu chuẩn PSR |
| **Hiệu suất** | Chậm hơn Go, Rust hoặc Java đối với các tác vụ không phải trên web | Sử dụng OPcache; xem xét Swoole cho tính không đồng bộ; sử dụng PHP-FPM |
| **Không lý tưởng cho những người không có web** | CLI, máy tính để bàn, thiết bị di động, khoa học dữ liệu — không phải thế mạnh của PHP | Sử dụng Python, Go hoặc các ngôn ngữ khác cho công việc không liên quan đến web |
| **An ninh uy tín** | Mã PHP kế thừa có nhiều vấn đề về bảo mật | Sử dụng các khuôn khổ hiện đại; tuân theo các biện pháp bảo mật tốt nhất |
---

##Cơ bản về cú pháp
###Cấu trúc cơ bản
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

### Hàm và kiểu
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

### Lớp và OOP
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

### So khớp biểu thức và luồng điều khiển
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

## Hệ sinh thái
### Khung
| Khung | Phong cách | Tốt nhất cho |
|----------|-------|----------|
| **Laravel** | Cú pháp đầy đủ, tinh tế | Hầu hết các ứng dụng web; khung PHP lớn nhất |
| **Symfony** | Doanh nghiệp, dựa trên thành phần | Ứng dụng doanh nghiệp lớn |
| **Mỏng** | Khung vi mô | API và ứng dụng nhỏ |
| **WordPress** | CMS | Blog, trang nội dung, trang web doanh nghiệp nhỏ |
### Công cụ cần thiết
| Công cụ | Mục đích |
|------|----------|
| **Nhà soạn nhạc** | Trình quản lý phụ thuộc (như npm/pip) |
| **PHPUnit** | Khung kiểm tra |
| **PHPStan / Thánh vịnh** | Phân tích tĩnh (tìm lỗi mà không cần chạy mã) |
| **Cánh buồm/Bầy đàn Laravel** | Môi trường phát triển địa phương |
| **Tiêu chuẩn PSR** | Phong cách mã hóa và tiêu chuẩn giao diện |
---

## Cú pháp & Mẫu nâng cao
### Generics thông qua PHPDoc và Mẫu
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

### Thuộc tính (PHP 8.0+) - Chú thích gốc
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

### Closure và các hàm bậc cao hơn
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

### Fibers (PHP 8.1+) — Đa nhiệm hợp tác
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

### Đặc điểm - Tái sử dụng mã ngang
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

## Đồng thời & Song song
### Sợi cho sự đồng thời hợp tác
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

### Swoole — Đồng thời dựa trên Coroutine
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

### Mở rộng song song
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án (Laravel)
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

### Composer.json — Quản lý phụ thuộc
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

### Lệnh phụ thuộc
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### Đường dẫn CI/CD (Hành động trên GitHub)
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

##Thử nghiệm
### PHPUnit — Khung kiểm thử
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

### Kiểm tra tính năng của Laravel
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

### Nhạo báng với sự nhạo báng
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

### Lệnh kiểm tra
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## Khả năng tương tác
### Phần mở rộng C
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

### FFI — Giao diện chức năng nước ngoài (PHP 7.4+)
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

### Tiêu chuẩn PSR
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## Mẫu thiết kế
### Mẫu kho lưu trữ
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

### Mẫu phần mềm trung gian
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

### Vùng chứa dịch vụ/Tiêm phụ thuộc
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

## Hiệu suất và Tối ưu hóa
### Công cụ lập hồ sơ
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### Kỹ thuật tối ưu hóa
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

## Triển khai
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

### Triển khai Docker
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

## Khi nào nên sử dụng PHP
| Kịch bản | Tại sao PHP | Thay thế tốt hơn |
|----------|----------|-------------------|
| Phát triển WordPress | PHP là lựa chọn duy nhất | — |
| Phát triển web tự do | Chợ lớn; dễ triển khai | — |
| Thương mại điện tử (WooC Commerce, Magento) | Nền tảng PHP được thành lập | — |
| Tạo mẫu web nhanh | Thiết lập thấp, triển khai nhanh | Node.js, Python |
| Trang web nặng về nội dung | Hệ sinh thái CMS đã trưởng thành | — |
| API và vi dịch vụ | Có thể với Laravel/Slim | Đi, Node.js, Python |
| công cụ CLI | Có thể nhưng không lý tưởng | Đi, Python, Rust |
| Ứng dụng thời gian thực | Không phải thế mạnh của PHP | Node.js, Đi |
| Khoa học dữ liệu / ML | Không phải hệ sinh thái | Python, R |
| Ứng dụng dành cho máy tính để bàn/thiết bị di động | Không phù hợp | Sử dụng ngôn ngữ bản địa |
---

## Hỏi đáp tổng hợp
### Câu 1: Sự khác biệt giữa`==`và`===`trong PHP là gì?
**A:**`==`là so sánh lỏng lẻo — nó thực hiện ép kiểu trước khi so sánh (`"0" == false`là`true`). `===`là so sánh nghiêm ngặt — nó kiểm tra cả giá trị và loại (`"0" === false`là`false`). Luôn sử dụng`===`trừ khi bạn đặc biệt cần ép buộc kiểu. Đây là một trong những nguồn lỗi phổ biến nhất của PHP.
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

### Câu 2: Không gian tên PHP và tính năng tự động tải hoạt động như thế nào?
**A:** Không gian tên ngăn ngừa xung đột tên lớp. Tự động tải PSR-4 ánh xạ cấu trúc không gian tên vào cấu trúc thư mục -`App\Controllers\UserController`ánh xạ tới`src/Controllers/UserController.php`. Trình soạn thảo xử lý việc tự động tải qua`composer.json`. Luôn sử dụng không gian tên và PSR-4 trong PHP hiện đại.
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

### Câu 3: Thuộc tính của PHP 8 là gì và chúng liên quan đến framework như thế nào?
**A:** Thuộc tính (PHP 8) là các chú thích siêu dữ liệu có cấu trúc cho các lớp, phương thức, thuộc tính và tham số. Chúng tương đương với PHP của các chú thích Java hoặc thuộc tính C#. Các framework như Laravel và Symfony sử dụng chúng một cách rộng rãi để định tuyến, xác thực và chèn phần phụ thuộc.
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

### Q4: Làm cách nào để xử lý lỗi đúng cách trong PHP hiện đại?
**A:** PHP có cả lỗi (E_WARNING, E_NOTICE) và ngoại lệ. PHP hiện đại chỉ sử dụng các ngoại lệ. Sử dụng thử/bắt cho các lỗi dự kiến, các lớp ngoại lệ tùy chỉnh cho lỗi miền và`set_error_handler`để chuyển lỗi thành ngoại lệ. PHP 7+`Throwable`là giao diện cơ bản cho cả lỗi và ngoại lệ.
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

### Câu 5: PHP Fiber là gì và chúng liên quan đến async như thế nào?
**A:** Fiber (PHP 8.1) là các luồng hợp tác nhẹ — chúng có thể tạm dừng và tiếp tục thực thi. Chúng là nền tảng cho PHP không đồng bộ nhưng ở mức độ thấp. Các khung như Amp và ReactPHP sử dụng các sợi bên trong. Đối với hầu hết các ứng dụng, hãy sử dụng khung không đồng bộ thay vì sợi thô.
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Xây dựng Middleware Pipeline
**Báo cáo vấn đề:** Triển khai quy trình phần mềm trung gian cho khung web PHP trong đó mỗi phần mềm trung gian có thể xử lý yêu cầu trước và sau phần mềm trung gian tiếp theo trong chuỗi.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) giao diện `Middleware`, (2) đường dẫn nối chuỗi phần mềm trung gian, (3) mỗi phần mềm trung gian nhận được yêu cầu và lệnh gọi lại `$next`, (4) phần mềm trung gian có thể sửa đổi cả yêu cầu (trước) và phản hồi (sau). Đây là mô hình củ hành được sử dụng bởi Laravel, PSR-15 và các khung tương tự.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Xác định`MiddlewareInterface`bằng `process(Request, RequestHandler): Response`.
- Sử dụng tính năng rút gọn mảng để kết hợp phần mềm trung gian thành một trình xử lý duy nhất.
- Mỗi phần mềm trung gian bao bọc phần mềm tiếp theo, tạo ra các lệnh gọi hàm lồng nhau.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Vấn đề thứ tự: đường ống đầu tiên = ngoài cùng (thực hiện đầu tiên theo yêu cầu, cuối cùng khi phản hồi).
- Mỗi phần mềm trung gian có thể đoản mạch bằng cách trả về Response mà không cần gọi`$next`.
- Sản xuất: sử dụng PSR-15`MiddlewareInterface`để có khả năng tương tác với bất kỳ khung PSR-15 nào.
### Vấn đề 2: Triển khai Kho lưu trữ với Trình tạo truy vấn
**Báo cáo vấn đề:** Xây dựng trình tạo truy vấn thông thạo để tạo SQL một cách an toàn với các truy vấn được tham số hóa, hỗ trợ xâu chuỗi và tích hợp với mẫu kho lưu trữ.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng ta cần: (1) lớp`QueryBuilder`với các phương thức có thể xâu chuỗi (`select`,`where`,`orderBy`,`limit`), (2) các truy vấn được tham số hóa để ngăn chặn việc chèn SQL, (3)`Repository`sử dụng trình tạo truy vấn để truy cập dữ liệu.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Builder tích lũy các đoạn và tham số SQL.
-`toSql()`tạo truy vấn cuối cùng với phần giữ chỗ.
-`getParameters()`trả về các giá trị giới hạn.
- Kho lưu trữ bao bọc trình xây dựng bằng các phương thức dành riêng cho miền.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Ngăn chặn việc tiêm SQL: tất cả các giá trị đều trải qua các truy vấn được tham số hóa (trình giữ chỗ `?`).
- API có thể kết nối: mỗi phương thức trả về`$this`để có bố cục trôi chảy.
- Sản xuất: sử dụng`illuminate/database`(trình tạo truy vấn của Laravel) hoặc`doctrine/dbal`để có giải pháp toàn diện, đã được thử nghiệm.
---

## Bản tóm tắt
PHP là công cụ thực dụng của web. Nó hỗ trợ phần lớn các trang web, có hệ sinh thái rộng lớn và PHP (8.x) hiện đại là ngôn ngữ được thiết kế tốt với các kiểu, enum phù hợp và cú pháp rõ ràng. Nó không phải là ngôn ngữ tao nhã nhất và không phù hợp với mọi miền - nhưng để phát triển web, đặc biệt là quản lý nội dung, thương mại điện tử và làm việc tự do, PHP vẫn là một lựa chọn thiết thực và được sử dụng rộng rãi.