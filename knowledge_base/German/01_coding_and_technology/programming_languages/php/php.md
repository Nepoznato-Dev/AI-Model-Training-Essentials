<!--
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

-->
# PHP
PHP (Hypertext Preprocessor) ist eine serverseitige Skriptsprache, die 1994 von Rasmus Lerdorf entwickelt und erstmals 1995 veröffentlicht wurde. Ursprünglich für die Generierung dynamischer Webseiten konzipiert, hat sich PHP zu einer Allzwecksprache mit vollem Funktionsumfang entwickelt. Es betreibt etwa 75 % aller Websites mit einer bekannten serverseitigen Sprache, darunter WordPress, Facebook (ursprünglich), Wikipedia, Slack und Millionen anderer Websites.
Modernes PHP (8.x) ist eine ganz andere Sprache als das PHP der frühen 2000er Jahre. Es verfügt jetzt über typisierte Eigenschaften, Übereinstimmungsausdrücke, Aufzählungen, Fasern, schreibgeschützte Klassen und ein robustes Typsystem. Trotz seines Rufs unter Entwicklern (oft wegen Inkonsistenzen kritisiert), ist PHP praktisch, weit verbreitet und wird ständig verbessert.
---

## Warum PHP wichtig ist
- **Web-Dominanz**: Betreibt etwa 75 % der Websites. WordPress allein betreibt 43 % des Webs.
- **Geringe Eintrittsbarriere**: Bereitstellung durch Hochladen von Dateien auf ein beliebiges Shared Hosting. Keine Kompilierung, kein Build-Schritt.
- **Ausgereiftes Ökosystem**: Composer (Paketmanager), Laravel, Symfony – ausgereifte, kampferprobte Tools.
- **Praktisch**: Bringen Sie mit minimalem Setup in wenigen Minuten eine dynamische Website zum Laufen.
- **Kontinuierliche Verbesserung**: PHP 8.x hat erhebliche Verbesserungen der Lebensqualität gebracht.
- **Freiberuflicher Markt**: Riesige Nachfrage nach WordPress-, Laravel- und E-Commerce-Entwicklern (WooCommerce, Magento).
## Die Kompromisse
| Einschränkung | Einzelheiten | Typische Problemumgehung |
|-----------|---------|-----|
| **Inkonsistente Benennung** | `strpos`vs. `str_replace`,`array_key_exists`vs.`in_array`– keine einheitliche Konvention | Lernen Sie die Inkonsistenzen kennen; IDE-Autovervollständigung verwenden |
| **Historisches Gepäck** | Legacy-Funktionen und Muster von PHP 5 und früher | Verwenden Sie modernes PHP (8.2+); Befolgen Sie die PSR-Standards |
| **Leistung** | Langsamer als Go, Rust oder Java für Nicht-Web-Aufgaben | Verwenden Sie OPcache. Betrachten Sie Swoole für asynchron; PHP-FPM verwenden |
| **Nicht ideal für Nicht-Web** | CLI, Desktop, Mobile, Data Science – nicht die Stärken von PHP | Verwenden Sie Python, Go oder andere Sprachen für Arbeiten außerhalb des Webs |
| **Sicherheitsreputation** | Älterer PHP-Code weist viele Sicherheitsprobleme auf | Nutzen Sie moderne Frameworks; Befolgen Sie bewährte Sicherheitspraktiken |
---

## Syntax-Grundlagen
### Grundstruktur
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

### Funktionen und Typen
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

### Klassen und OOP
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

### Passen Sie Ausdruck und Kontrollfluss an
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

## Das Ökosystem
### Frameworks
| Rahmen | Stil | Am besten für |
|-----------|-------|----------|
| **Laravel** | Vollständige, elegante Syntax | Die meisten Webanwendungen; größtes PHP-Framework |
| **Symfony** | Enterprise, komponentenbasiert | Große Unternehmensanwendungen |
| **Schlank** | Mikro-Framework | APIs und kleine Anwendungen |
| **WordPress** | CMS | Blogs, Content-Sites, Websites für kleine Unternehmen |
### Wesentliche Werkzeuge
| Werkzeug | Zweck |
|------|---------|
| **Komponist** | Abhängigkeitsmanager (wie npm/pip) |
| **PHPUnit** | Testrahmen |
| **PHPStan / Psalm** | Statische Analyse (findet Fehler, ohne Code auszuführen) |
| **Laravel Segel / Herde** | Lokale Entwicklungsumgebungen |
| **PSR-Standards** | Codierungsstil und Schnittstellenstandards |
---

## Erweiterte Syntax und Muster
### Generics über PHPDoc und Templates
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

### Attribute (PHP 8.0+) – Native Anmerkungen
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

### Abschlüsse und Funktionen höherer Ordnung
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

### Fibers (PHP 8.1+) – Kooperatives Multitasking
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

### Merkmale – Horizontale Code-Wiederverwendung
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

## Parallelität und Parallelität
### Fasern für kooperative Parallelität
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

### Swoole – Coroutine-basierte Parallelität
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

### Parallele Erweiterung
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

## Projektkonfiguration und Build-System
### Projektstruktur (Laravel)
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

### Composer.json – Abhängigkeitsmanagement
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

### Abhängigkeitsbefehle
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### CI/CD-Pipeline (GitHub-Aktionen)
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

## Testen
### PHPUnit – Test-Framework
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

### Laravel-Funktionstests
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

### Spott mit Spott
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

### Testbefehle
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## Interoperabilität
### C-Erweiterungen
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

### FFI – Fremdfunktionsschnittstelle (PHP 7.4+)
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

### PSR-Standards
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## Designmuster
### Repository-Muster
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

### Middleware-Muster
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

### Service-Container/Abhängigkeitsinjektion
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

## Leistung und Optimierung
### Profilierungstools
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### Optimierungstechniken
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

## Bereitstellung
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

### Docker-Bereitstellung
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

## Wann man PHP verwenden sollte
| Szenario | Warum PHP | Bessere Alternative |
|----------|---------|-----|
| WordPress-Entwicklung | PHP ist die einzige Option | — |
| Freiberufliche Webentwicklung | Riesiger Markt; einfach bereitzustellen | — |
| E-Commerce (WooCommerce, Magento) | Etablierte PHP-Plattformen | — |
| Schnelles Web-Prototyping | Geringer Installationsaufwand, schnelle Bereitstellung | Node.js, Python |
| Inhaltsintensive Websites | Das CMS-Ökosystem ist ausgereift | — |
| APIs und Microservices | Möglich mit Laravel/Slim | Go, Node.js, Python |
| CLI-Tools | Möglich, aber nicht ideal | Go, Python, Rust |
| Echtzeitanwendungen | Nicht die Stärke von PHP | Node.js, Go |
| Datenwissenschaft / ML | Nicht das Ökosystem | Python, R |
| Desktop-/mobile Apps | Nicht geeignet | Verwenden Sie Muttersprachen |
---

## Synthetische Fragen und Antworten
### F1: Was ist der Unterschied zwischen`==`und`===`in PHP?
**A:**`==`ist ein loser Vergleich – es führt vor dem Vergleich eine Typumwandlung durch (`"0" == false`ist`true`). `===`ist ein strenger Vergleich – er prüft sowohl Wert als auch Typ (`"0" === false`ist`false`). Verwenden Sie immer `===`, es sei denn, Sie benötigen ausdrücklich eine Typerzwingung. Dies ist eine der häufigsten Fehlerquellen von PHP.
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

### F2: Wie funktionieren PHP-Namespaces und das automatische Laden?
**A:** Namespaces verhindern Klassennamenkollisionen. Das automatische Laden von PSR-4 ordnet die Namespace-Struktur der Verzeichnisstruktur zu –`App\Controllers\UserController`wird zu`src/Controllers/UserController.php`zugeordnet. Composer übernimmt das automatische Laden über`composer.json`. Verwenden Sie in modernem PHP immer Namespaces und PSR-4.
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

### F3: Was sind PHP 8-Attribute und in welcher Beziehung stehen sie zu Frameworks?
**A:** Attribute (PHP 8) sind strukturierte Metadatenanmerkungen für Klassen, Methoden, Eigenschaften und Parameter. Sie sind das PHP-Äquivalent von Java-Annotationen oder C#-Attributen. Frameworks wie Laravel und Symfony nutzen sie häufig für Routing, Validierung und Abhängigkeitsinjektion.
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

### F4: Wie gehe ich in modernem PHP richtig mit Fehlern um?
**A:** PHP hat sowohl Fehler (E_WARNING, E_NOTICE) als auch Ausnahmen. Modernes PHP verwendet ausschließlich Ausnahmen. Verwenden Sie try/catch für erwartete Fehler, benutzerdefinierte Ausnahmeklassen für Domänenfehler und `set_error_handler`, um Fehler in Ausnahmen umzuwandeln. PHP 7+`Throwable`ist die Basisschnittstelle für Fehler und Ausnahmen.
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

### F5: Was sind PHP-Fasern und in welcher Beziehung stehen sie zu Async?
**A:** Fibers (PHP 8.1) sind leichte kooperative Threads – sie können die Ausführung anhalten und wieder aufnehmen. Sie bilden die Grundlage für asynchrones PHP, sind jedoch auf niedrigem Niveau. Frameworks wie Amp und ReactPHP verwenden intern Fasern. Verwenden Sie für die meisten Anwendungen ein asynchrones Framework anstelle von Rohfasern.
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

## Problemlösung in der Gedankenkette
### Problem 1: Erstellen Sie eine Middleware-Pipeline
**Problemstellung:** Implementieren Sie eine Middleware-Pipeline für ein PHP-Webframework, bei dem jede Middleware die Anfrage vor und nach der nächsten Middleware in der Kette verarbeiten kann.
**Schritt 1 – Das Problem verstehen:**
Wir benötigen: (1) eine `Middleware`-Schnittstelle, (2) eine Pipeline, die Middleware verkettet, (3) jede Middleware empfängt eine Anfrage und einen `$next`-Rückruf, (4) Middleware kann sowohl die Anfrage (vorher) als auch die Antwort (nachher) ändern. Dies ist das Zwiebelmodell, das von Laravel, PSR-15 und ähnlichen Frameworks verwendet wird.
**Schritt 2 – Identifizieren Sie den Ansatz:**
- Definieren Sie`MiddlewareInterface`mit `process(Request, RequestHandler): Response`.
– Verwenden Sie die Array-Reduktion, um Middleware in einem einzigen Handler zusammenzufassen.
– Jede Middleware umschließt die nächste und erstellt verschachtelte Funktionsaufrufe.
**Schritt 3 – Implementieren Sie die Lösung:**
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

**Schritt 4 – Überprüfen und Optimieren:**
- Reihenfolge ist wichtig: zuerst weitergeleitet = äußerst (wird zuerst auf Anfrage ausgeführt, zuletzt auf Antwort).
– Jede Middleware kann einen Kurzschluss verursachen, indem sie eine Antwort zurückgibt, ohne`$next`aufzurufen.
- Produktion: Verwenden Sie PSR-15`MiddlewareInterface`für Interoperabilität mit jedem PSR-15-Framework.
### Problem 2: Implementieren Sie ein Repository mit Query Builder
**Problemstellung:** Erstellen Sie einen Fluent Query Builder, der SQL sicher mit parametrisierten Abfragen generiert, die Verkettung unterstützt und sich in ein Repository-Muster integrieren lässt.
**Schritt 1 – Das Problem verstehen:**
Wir benötigen: (1) eine `QueryBuilder`-Klasse mit verkettbaren Methoden (`select`,`where`,
**Schritt 2 – Identifizieren Sie den Ansatz:**
- Builder sammelt SQL-Fragmente und Parameter.
-`toSql()`generiert die endgültige Abfrage mit Platzhaltern.
-`getParameters()`gibt die gebundenen Werte zurück.
– Das Repository umschließt den Builder mit domänenspezifischen Methoden.
**Schritt 3 – Implementieren Sie die Lösung:**
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

**Schritt 4 – Überprüfen und Optimieren:**
- Verhinderung von SQL-Injection: Alle Werte durchlaufen parametrisierte Abfragen (`?`-Platzhalter).
- Verkettbare API: Jede Methode gibt`$this`für eine flüssige Komposition zurück.
- Produktion: Verwenden Sie`illuminate/database`(Laravels Abfrage-Builder) oder`doctrine/dbal`für eine umfassende, getestete Lösung.
---

## Zusammenfassung
PHP ist das pragmatische Arbeitstier des Webs. Es unterstützt die meisten Websites, verfügt über ein riesiges Ökosystem und modernes PHP (8.x) ist eine gut gestaltete Sprache mit richtigen Typen, Aufzählungen und sauberer Syntax. Es ist nicht die eleganteste Sprache und eignet sich nicht für jede Domäne – aber für die Webentwicklung, insbesondere Content Management, E-Commerce und Freiberufler, bleibt PHP eine praktische und weit verbreitete Wahl.