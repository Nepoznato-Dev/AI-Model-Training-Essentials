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
PHP (препроцессор гипертекста) — это серверный язык сценариев, созданный Расмусом Лердорфом в 1994 году и впервые выпущенный в 1995 году. Первоначально предназначенный для создания динамических веб-страниц, PHP превратился в полнофункциональный язык общего назначения. Он поддерживает примерно 75% всех веб-сайтов с известным серверным языком, включая WordPress, Facebook (изначально), Wikipedia, Slack и миллионы других сайтов.
Современный PHP (8.x) сильно отличается от PHP начала 2000-х годов. Теперь в нем есть типизированные свойства, выражения соответствия, перечисления, волокна, классы только для чтения и надежная система типов. Несмотря на свою репутацию среди разработчиков (часто критикуемую за непоследовательность), PHP практичен, широко распространен и продолжает совершенствоваться.
---

## Почему PHP важен
- **Доминирование в сети**: работает около 75% веб-сайтов. Только WordPress обеспечивает 43% сети.
- **Низкий порог входа**: развертывание путем загрузки файлов на любой общий хостинг. Никакой компиляции, никакого этапа сборки.
- **Развитая экосистема**: Composer (менеджер пакетов), Laravel, Symfony — зрелые, проверенные в боях инструменты.
- **Практично**: создайте динамический веб-сайт за считанные минуты с минимальной настройкой.
- **Постоянное улучшение**: PHP 8.x значительно улучшил качество жизни.
- **Рынок фриланса**: огромный спрос на разработчиков WordPress, Laravel и электронной коммерции (WooCommerce, Magento).
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Несогласованное название** | `strpos`против`str_replace`,`array_key_exists`против`in_array`— нет согласованного соглашения | Узнать несоответствия; использовать автозаполнение IDE |
| **Исторический багаж** | Устаревшие функции и шаблоны PHP 5 и более ранних версий | Используйте современный PHP (8.2+); следовать стандартам PSR |
| **Производительность** | Медленнее, чем Go, Rust или Java для задач, не связанных с Интернетом | Используйте OPcache; рассмотрите Swoole для асинхронности; использовать PHP-FPM |
| **Не идеально подходит для пользователей, не использующих Интернет** | CLI, десктоп, мобильные устройства, обработка данных — не сильные стороны PHP | Используйте Python, Go или другие языки для работы вне Интернета |
| **Репутация безопасности** | Устаревший PHP-код имеет множество проблем с безопасностью | Используйте современные фреймворки; следуйте лучшим практикам безопасности |
---

## Основы синтаксиса
### Базовая структура
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

### Функции и типы
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

### Классы и ООП
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

### Сопоставление выражения и потока управления
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

## Экосистема
### Фреймворки
| Рамочная | Стиль | Лучшее для |
|-----------|-------|----------|
| **Ларавель** | Полный стек, элегантный синтаксис | Большинство веб-приложений; крупнейший PHP-фреймворк |
| **Симфония** | Предприятие, на основе компонентов | Крупные корпоративные приложения |
| **Тонкий** | Микро-фреймворк | API и небольшие приложения |
| **WordPress** | Система управления контентом | Блоги, информационные сайты, сайты для малого бизнеса |
### Основные инструменты
| Инструмент | Цель |
|------|---------|
| **Композитор** | Менеджер зависимостей (например, npm/pip) |
| **PHPUUnit** | Платформа тестирования |
| **PHPStan / Псалом** | Статический анализ (находит ошибки без запуска кода) |
| **Парус Laravel/Стадо** | Местная среда разработки |
| **Стандарты PSR** | Стиль кодирования и стандарты интерфейса |
---

## Расширенный синтаксис и шаблоны
### Дженерики через PHPDoc и шаблоны
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

### Атрибуты (PHP 8.0+) — встроенные аннотации
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

### Замыкания и функции высшего порядка
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

### Fibers (PHP 8.1+) — совместная многозадачность
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

### Traits — горизонтальное повторное использование кода
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

## Параллелизм и параллелизм
### Файберы для кооперативного параллелизма
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

### Swoole — параллелизм на основе сопрограмм
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

### Параллельное расширение
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

## Конфигурация проекта и система сборки
### Структура проекта (Laravel)
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

### композитор.json — Управление зависимостями
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

### Команды зависимостей
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### Конвейер CI/CD (действия GitHub)
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

## Тестирование
### PHPUnit — среда тестирования
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

### Функциональные тесты Laravel
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

### Издевательство с издевательством
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

### Тестовые команды
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## Совместимость
### Расширения C
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

### FFI — интерфейс внешних функций (PHP 7.4+)
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

### Стандарты PSR
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## Шаблоны проектирования
### Шаблон репозитория
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

### Шаблон промежуточного программного обеспечения
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

### Сервисный контейнер/внедрение зависимостей
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

## Производительность и оптимизация
### Инструменты профилирования
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### Методы оптимизации
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

## Развертывание
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

### Развертывание Docker
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

## Когда использовать PHP
| Сценарий | Почему PHP | Лучшая альтернатива |
|----------|---------|-------------------|
| Разработка WordPress | PHP — единственный вариант | — |
| Внештатная веб-разработка | Огромный рынок; легко развернуть | — |
| Электронная коммерция (WooCommerce, Magento) | Установленные платформы PHP | — |
| Быстрое веб-прототипирование | Простая настройка, быстрое развертывание | Node.js, Python |
| Веб-сайты с большим содержанием контента | Экосистема CMS является зрелой | — |
| API и микросервисы | Возможно с Laravel/Slim | Go, Node.js, Python |
| Инструменты CLI | Возможно, но не идеально | Го, Питон, Ржавчина |
| Приложения реального времени | Не сила PHP | Node.js, Go |
| Наука о данных / ML | Не экосистема | Питон, Р |
| Настольные/мобильные приложения | Не подходит | Используйте родные языки |
---

## Синтетические вопросы и ответы
### Q1: В чем разница между`==`и`===`в PHP?
**A:**`==`— это свободное сравнение — перед сравнением выполняется приведение типов (`"0" == false`— это`true`). `===`— это строгое сравнение — оно проверяет как значение, так и тип (`"0" === false` — это `false`). Всегда используйте `===`, если только вам не требуется приведение типов. Это один из наиболее распространенных источников ошибок PHP.
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

### Вопрос 2. Как работают пространства имен PHP и автозагрузка?
**О:** Пространства имен предотвращают конфликты имен классов. Автозагрузка PSR-4 сопоставляет структуру пространства имен со структурой каталогов —`App\Controllers\UserController`сопоставляется с `src/Controllers/UserController.php`. Composer обрабатывает автозагрузку через `composer.json`. Всегда используйте пространства имен и PSR-4 в современном PHP.
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

### Вопрос 3: Что такое атрибуты PHP 8 и как они связаны с платформами?
**A:** Атрибуты (PHP 8) — это структурированные аннотации метаданных для классов, методов, свойств и параметров. Они являются PHP-эквивалентом аннотаций Java или атрибутов C#. Такие фреймворки, как Laravel и Symfony, широко используют их для маршрутизации, проверки и внедрения зависимостей.
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

### Вопрос 4: Как правильно обрабатывать ошибки в современном PHP?
**О:** В PHP есть как ошибки (E_WARNING, E_NOTICE), так и исключения. Современный PHP использует исключительно исключения. Используйте try/catch для ожидаемых сбоев, специальные классы исключений для ошибок домена и`set_error_handler`для преобразования ошибок в исключения. PHP 7+`Throwable`— это базовый интерфейс для ошибок и исключений.
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

### Вопрос 5: Что такое PHP-волокна и как они связаны с асинхронностью?
**О:** Файберы (PHP 8.1) — это легкие кооперативные потоки, которые могут приостанавливать и возобновлять выполнение. Они являются основой асинхронного PHP, но являются низкоуровневыми. Такие фреймворки, как Amp и ReactPHP, используют волокна внутри себя. Для большинства приложений используйте асинхронную структуру, а не необработанные волокна.
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

## Решение проблем с цепочкой мыслей
### Проблема 1. Создание конвейера промежуточного программного обеспечения
**Постановка задачи.** Реализуйте конвейер промежуточного программного обеспечения для веб-платформы PHP, в котором каждое промежуточное программное обеспечение может обрабатывать запрос до и после следующего промежуточного программного обеспечения в цепочке.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) интерфейс `Middleware`, (2) конвейер, который объединяет промежуточное программное обеспечение, (3) каждое промежуточное программное обеспечение получает запрос и обратный вызов `$next`, (4) промежуточное программное обеспечение может изменять как запрос (до), так и ответ (после). Это луковая модель, используемая Laravel, PSR-15 и подобными фреймворками.
**Шаг 2. Определите подход:**
- Определите`MiddlewareInterface`с помощью `process(Request, RequestHandler): Response`.
- Используйте сокращение массива, чтобы объединить промежуточное ПО в один обработчик.
- Каждое промежуточное программное обеспечение оборачивает следующее, создавая вложенные вызовы функций.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
- Порядок имеет значение: первый по конвейеру = самый внешний (выполняется первым по запросу, последним по ответу).
— Каждое промежуточное ПО может выполнить короткое замыкание, вернув ответ без вызова `$next`.
- Производство: используйте PSR-15`MiddlewareInterface`для совместимости с любой платформой PSR-15.
### Проблема 2. Реализация репозитория с помощью Query Builder
**Постановка задачи.** Создайте гибкий построитель запросов, который безопасно генерирует SQL с помощью параметризованных запросов, поддерживает цепочки и интегрируется с шаблоном репозитория.
**Шаг 1. Поймите проблему:**
Нам нужны: (1) класс`QueryBuilder`с цепочками методов (`select`,`where`,`orderBy`,`limit`), (2) параметризованные запросы для предотвращения SQL-инъекций, (3) `Repository`, который использует построитель запросов для доступа к данным.
**Шаг 2. Определите подход:**
- Builder аккумулирует фрагменты и параметры SQL.
-`toSql()`генерирует окончательный запрос с заполнителями.
-`getParameters()`возвращает связанные значения.
- Репозиторий оборачивает построитель методами, специфичными для предметной области.
**Шаг 3. Реализация решения:**
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

**Шаг 4. Проверка и оптимизация:**
— Предотвращение SQL-инъекций: все значения проходят через параметризованные запросы (заполнители `?`).
- Цепной API: каждый метод возвращает`$this`для плавной композиции.
- Производство: используйте`illuminate/database`(построитель запросов Laravel) или`doctrine/dbal`для комплексного, проверенного решения.
---

## Краткое содержание
PHP — прагматичная рабочая лошадка Интернета. На нем работает большинство веб-сайтов, он имеет обширную экосистему, а современный PHP (8.x) — это хорошо продуманный язык с правильными типами, перечислениями и чистым синтаксисом. Это не самый элегантный язык, и он подходит не для каждой области, но для веб-разработки, особенно для управления контентом, электронной коммерции и фриланса, PHP остается практичным и широко используемым выбором.