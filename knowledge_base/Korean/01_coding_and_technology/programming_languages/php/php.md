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
# PHP
PHP(Hypertext Preprocessor)는 Rasmus Lerdorf가 1994년에 개발하여 1995년에 처음 출시된 서버측 스크립팅 언어입니다. 원래 동적 웹 페이지 생성용으로 설계된 PHP는 모든 기능을 갖춘 범용 언어로 발전했습니다. WordPress, Facebook(원래), Wikipedia, Slack 및 기타 수백만 사이트를 포함하여 알려진 서버측 언어를 사용하는 모든 웹사이트의 약 75%를 지원합니다.
최신 PHP(8.x)는 2000년대 초반의 PHP와는 매우 다른 언어입니다. 이제 유형이 지정된 속성, 일치 표현식, 열거형, 파이버, 읽기 전용 클래스 및 강력한 유형 시스템이 있습니다. 개발자들 사이에서 명성이 높음에도 불구하고(종종 불일치로 인해 비판을 받음) PHP는 실용적이고 널리 배포되며 지속적으로 개선되고 있습니다.
---

## PHP가 중요한 이유
- **웹 지배력**: 웹사이트의 ~75%를 실행합니다. 워드프레스(WordPress)만으로도 웹의 43%를 장악하고 있습니다.
- **낮은 진입 장벽**: 공유 호스팅에 파일을 업로드하여 배포합니다. 컴파일이나 빌드 단계가 없습니다.
- **성숙한 생태계**: Composer(패키지 관리자), Laravel, Symfony — 성숙하고 전투 테스트를 거친 도구입니다.
- **실용성**: 최소한의 설정으로 몇 분 만에 동적 웹사이트를 실행할 수 있습니다.
- **지속적인 개선**: PHP 8.x는 삶의 질을 크게 향상시켰습니다.
- **프리랜서 시장**: WordPress, Laravel 및 전자상거래(WooCommerce, Magento) 개발자에 대한 수요가 높습니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **일관되지 않은 명명** | `strpos`대`str_replace`,`array_key_exists`대`in_array`— 일관된 규칙 없음 | 불일치를 배우십시오. IDE 자동 완성 사용 |
| **역사적 수하물** | PHP 5 및 이전 버전의 레거시 기능 및 패턴 | 최신 PHP(8.2+)를 사용하세요. PSR 표준을 따르세요 |
| **성능** | 웹이 아닌 작업의 경우 Go, Rust 또는 Java보다 느림 | OPcache를 사용하세요. 비동기를 위해 Swoole을 고려하십시오. PHP-FPM 사용 |
| **웹이 아닌 경우에는 적합하지 않음** | CLI, 데스크탑, 모바일, 데이터 과학 - PHP의 강점은 아님 | 웹 작업이 아닌 작업에 Python, Go 또는 기타 언어 사용 |
| **보안 평판** | 레거시 PHP 코드에는 많은 보안 문제가 있습니다 | 최신 프레임워크를 사용하세요. 보안 모범 사례 준수 |
---

## 구문 기본 사항
### 기본 구조
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

### 기능 및 유형
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

### 클래스와 OOP
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

### 일치 표현식 및 제어 흐름
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

## 생태계
### 프레임워크
| 프레임워크 | 스타일 | 최고의 대상 |
|------------|-------|----------|
| **라라벨** | 풀스택, 우아한 구문 | 대부분의 웹 애플리케이션; 가장 큰 PHP 프레임워크 |
| **심포니** | 엔터프라이즈, 구성 요소 기반 | 대기업 애플리케이션 |
| **슬림** | 마이크로 프레임워크 | API 및 소규모 애플리케이션 |
| **워드프레스** | CMS | 블로그, 콘텐츠 사이트, 중소기업 웹사이트 |
### 필수 도구
| 도구 | 목적 |
|------|---------|
| **작곡가** | 종속성 관리자(예: npm/pip) |
| **PHP유닛** | 테스트 프레임워크 |
| **PHPStan / 시편** | 정적 분석(코드를 실행하지 않고 버그 찾기) |
| **라라벨 항해/무리** | 로컬 개발 환경 |
| **PSR 표준** | 코딩 스타일 및 인터페이스 표준 |
---

## 고급 구문 및 패턴
### PHPDoc 및 템플릿을 통한 제네릭
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

### 속성(PHP 8.0+) — 기본 주석
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

### 클로저와 고차 함수
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

### Fibers(PHP 8.1+) — 협력적 멀티태스킹
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

### 특성 — 수평적 코드 재사용
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

## 동시성 및 병렬성
### 협력적 동시성을 위한 파이버
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

### Swoole — 코루틴 기반 동시성
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

### 병렬 확장
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조(Laravel)
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

### 작곡가.json — 종속성 관리
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

### 종속성 명령
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### CI/CD 파이프라인(GitHub 작업)
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

## 테스트
### PHPUnit — 테스트 프레임워크
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

### Laravel 기능 테스트
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

### 조롱으로 조롱하기
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

### 테스트 명령
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## 상호 운용성
### C 확장
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

### FFI — 외부 함수 인터페이스(PHP 7.4+)
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

### PSR 표준
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## 디자인 패턴
### 저장소 패턴
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

### 미들웨어 패턴
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

### 서비스 컨테이너 / 종속성 주입
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

## 성능 및 최적화
### 프로파일링 도구
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### 최적화 기술
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

## 배포
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

### 도커 배포
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

## PHP를 사용해야 하는 경우
| 시나리오 | 왜 PHP인가 | 더 나은 대안 |
|----------|---------|------|
| 워드프레스 개발 | PHP가 유일한 옵션입니다 | — |
| 프리랜서 웹 개발 | 거대한 시장; 배포가 용이함 | — |
| 전자상거래(WooCommerce, Magento) | PHP 플랫폼 구축 | — |
| 신속한 웹 프로토타이핑 | 낮은 설정, 빠른 배포 | Node.js, 파이썬 |
| 콘텐츠가 많은 웹사이트 | CMS 생태계가 성숙해졌습니다 | — |
| API 및 마이크로서비스 | Laravel/Slim에서 가능 | Go, Node.js, Python |
| CLI 도구 | 가능하지만 이상적이지는 않음 | Go, 파이썬, 러스트 |
| 실시간 애플리케이션 | PHP의 강점이 아니다 | Node.js, 이동 |
| 데이터 과학 / ML | 생태계가 아니다 | 파이썬, R |
| 데스크탑/모바일 앱 | 적합하지 않음 | 모국어 사용 |
---

## 요약
PHP는 웹의 실용적인 도구입니다. 이는 대부분의 웹사이트를 지원하고 대규모 생태계를 갖추고 있으며 최신 PHP(8.x)는 적절한 유형, 열거형 및 깔끔한 구문을 갖춘 잘 설계된 언어입니다. 가장 우아한 언어는 아니며 모든 도메인에 적합하지는 않습니다. 하지만 웹 개발, 특히 콘텐츠 관리, 전자 상거래 및 프리랜서의 경우 PHP는 여전히 실용적이고 널리 사용되는 선택입니다.