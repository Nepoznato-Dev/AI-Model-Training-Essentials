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
PHP (Hypertext Preprocessor), 1994 yılında Rasmus Lerdorf tarafından oluşturulan ve ilk olarak 1995'te piyasaya sürülen, sunucu taraflı bir kodlama dilidir. Başlangıçta dinamik web sayfaları oluşturmak için tasarlanan PHP, tam özellikli genel amaçlı bir dile dönüştü. WordPress, Facebook (orijinal olarak), Wikipedia, Slack ve diğer milyonlarca site dahil olmak üzere bilinen bir sunucu tarafı dili kullanan tüm web sitelerinin yaklaşık %75'ine güç sağlar.
Modern PHP (8.x), 2000'li yılların başındaki PHP'den çok farklı bir dildir. Artık yazılan özelliklere, eşleşme ifadelerine, numaralandırmalara, liflere, salt okunur sınıflara ve sağlam bir tür sistemine sahiptir. Geliştiriciler arasındaki itibarına rağmen (genellikle tutarsızlıklar nedeniyle eleştirilir), PHP pratiktir, yaygın olarak kullanılmaktadır ve gelişmeye devam etmektedir.
---

## PHP Neden Önemlidir
- **Web hakimiyeti**: Web sitelerinin ~%75'ini çalıştırır. WordPress tek başına internetin %43’üne güç sağlıyor.
- **Giriş engeli düşük**: Dosyaları herhangi bir paylaşılan barındırma sunucusuna yükleyerek dağıtın. Derleme yok, oluşturma adımı yok.
- **Olgun ekosistem**: Composer (paket yöneticisi), Laravel, Symfony — olgun, savaşta test edilmiş araçlar.
- **Pratik**: Minimum kurulumla dakikalar içinde çalışan dinamik bir web sitesine sahip olun.
- **Sürekli iyileştirme**: PHP 8.x, yaşam kalitesinde önemli iyileştirmeler sağladı.
- **Serbest çalışma pazarı**: WordPress, Laravel ve e-ticaret (WooCommerce, Magento) geliştiricilerine yönelik büyük talep.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Tutarsız adlandırma** | `strpos`ve `str_replace`,`array_key_exists`ve`in_array`— tutarlı bir kural yok | Tutarsızlıkları öğrenin; IDE otomatik tamamlamayı kullan |
| **Tarihsel bagaj** | PHP 5 ve önceki sürümlerden eski özellikler ve modeller | Modern PHP (8.2+) kullanın; PSR standartlarına uyun |
| **Performans** | Web dışı görevler için Go, Rust veya Java'dan daha yavaş | OPcache'i kullanın; async için Swoole'u düşünün; PHP-FPM kullanın |
| **Web dışı ortamlar için ideal değildir** | CLI, masaüstü, mobil, veri bilimi — PHP'nin güçlü yönleri değil | Web dışı çalışmalar için Python, Go veya diğer dilleri kullanın |
| **Güvenlik itibarı** | Eski PHP kodunda birçok güvenlik sorunu var | Modern çerçeveleri kullanın; güvenlikle ilgili en iyi uygulamaları takip edin |
---

## Söz Diziminin Temelleri
### Temel Yapı
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

### İşlevler ve Türler
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

### Sınıflar ve OOP
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

### İfadeyi ve Kontrol Akışını Eşleştir
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

## Ekosistem
### Çerçeveler
| Çerçeve | Stil | En İyisi |
|-----------|----------|----------|
| **Laravel** | Tam yığın, zarif sözdizimi | Çoğu web uygulaması; en büyük PHP çerçevesi |
| **Symfony** | Kurumsal, bileşen tabanlı | Büyük kurumsal uygulamalar |
| **İnce** | Mikro çerçeve | API'ler ve küçük uygulamalar |
| **WordPress** | CMS | Bloglar, içerik siteleri, küçük işletme web siteleri |
### Temel Araçlar
| Araç | Amaç |
|------|------------|
| **Besteci** | Bağımlılık yöneticisi (npm/pip gibi) |
| **PHPUnit** | Test çerçevesi |
| **PHPStan / Mezmur** | Statik analiz (kod çalıştırmadan hataları bulur) |
| **Laravel Yelkeni / Sürü** | Yerel kalkınma ortamları |
| **PSR standartları** | Kodlama stili ve arayüz standartları |
---

## Gelişmiş Sözdizimi ve Desenler
### PHPDoc ve Şablonlar aracılığıyla Jenerikler
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

### Nitelikler (PHP 8.0+) — Yerel Ek Açıklamalar
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

### Kapanışlar ve Üst Düzey İşlevler
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

### Fiberler (PHP 8.1+) — İşbirliğine Dayalı Çoklu Görev
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

### Özellikler — Yatay Kodun Yeniden Kullanımı
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

## Eşzamanlılık ve Paralellik
### İşbirlikçi Eşzamanlılık için Fiberler
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

### Swoole — Eşyordam Tabanlı Eşzamanlılık
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

### Paralel Uzatma
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı (Laravel)
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

### besteci.json — Bağımlılık Yönetimi
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

### Bağımlılık Komutları
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### PHPUnit — Çerçeveyi Test Etme
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

### Laravel Özellik Testleri
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

### Alay ile Alay Etmek
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

### Test Komutları
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## Birlikte Çalışabilirlik
### C Uzantıları
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

### FFI — Yabancı İşlev Arayüzü (PHP 7.4+)
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

### PSR Standartları
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## Tasarım Desenleri
### Depo Modeli
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

### Ara Yazılım Kalıbı
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

### Hizmet Kapsayıcı / Bağımlılık Ekleme
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

## Performans ve Optimizasyon
### Profil Oluşturma Araçları
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### Optimizasyon Teknikleri
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

## Dağıtım
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

### Docker Dağıtımı
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

## PHP Ne Zaman Kullanılmalı
| Senaryo | Neden PHP | Daha İyi Alternatif |
|----------|------------|-----------|
| WordPress geliştirme | PHP tek seçenektir | — |
| Serbest web geliştirme | Büyük pazar; dağıtımı kolay | — |
| E-ticaret (WooCommerce, Magento) | PHP platformları kuruldu | — |
| Hızlı web prototipleme | Düşük kurulum, hızlı dağıtım | Node.js, Python |
| İçerik ağırlıklı web siteleri | CMS ekosistemi olgunlaştı | — |
| API'ler ve mikro hizmetler | Laravel/Slim ile mümkün | Git, Node.js, Python |
| CLI araçları | Mümkün ama ideal değil | Git, Python, Pas |
| Gerçek zamanlı uygulamalar | PHP'nin gücü değil | Node.js, Git |
| Veri bilimi / ML | Ekosistem değil | Python, R |
| Masaüstü/mobil uygulamalar | Uygun değil | Yerel dilleri kullanın |
---

## Sentetik Soru-Cevap
### S1: PHP'de`==`ve`===`arasındaki fark nedir?
**A:**`==`gevşek bir karşılaştırmadır — karşılaştırmadan önce tür zorlaması gerçekleştirir ( `"0" == false`, `true`'dur). `===`sıkı bir karşılaştırmadır; hem değeri hem de türü kontrol eder (`"0" === false`, `false`'dir). Özellikle tür zorlamaya ihtiyaç duymadığınız sürece her zaman`===`kullanın. Bu, PHP'nin en yaygın hata kaynaklarından biridir.
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

### S2: PHP ad alanları ve otomatik yükleme nasıl çalışır?
**C:** Ad alanları sınıf adı çakışmalarını önler. PSR-4 otomatik yükleme, ad alanı yapısını dizin yapısına eşler — `App\Controllers\UserController`,`src/Controllers/UserController.php`ile eşleşir. Besteci otomatik yüklemeyi`composer.json`aracılığıyla gerçekleştirir. Modern PHP'de her zaman ad alanlarını ve PSR-4'ü kullanın.
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

### S3: PHP 8 özellikleri nelerdir ve bunların çerçevelerle ilişkisi nedir?
**C:** Nitelikler (PHP 8) sınıflar, yöntemler, özellikler ve parametreler için yapılandırılmış meta veri açıklamalarıdır. Bunlar Java ek açıklamalarının veya C# niteliklerinin PHP eşdeğeridir. Laravel ve Symfony gibi çerçeveler bunları yönlendirme, doğrulama ve bağımlılık enjeksiyonu için yaygın olarak kullanır.
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

### S4: Modern PHP'de hataları doğru şekilde nasıl ele alabilirim?
**C:** PHP'de hem hatalar (E_WARNING, E_NOTICE) hem de istisnalar vardır. Modern PHP yalnızca istisnaları kullanır. Beklenen hatalar için try/catch'i, etki alanı hataları için özel istisna sınıflarını ve hataları istisnalara dönüştürmek için `set_error_handler`'yi kullanın. PHP 7+`Throwable`hem hatalar hem de istisnalar için temel arayüzdür.
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

### S5: PHP fiberleri nedir ve bunların zaman uyumsuzlukla ilişkisi nedir?
**C:** Fiberler (PHP 8.1) hafif, işbirlikçi iş parçacıklarıdır; yürütmeyi askıya alabilir ve devam ettirebilirler. Bunlar async PHP'nin temelidir ancak düşük seviyelidir. Amp ve ReactPHP gibi çerçeveler fiberleri dahili olarak kullanır. Çoğu uygulama için ham fiberler yerine eşzamansız bir çerçeve kullanın.
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

## Düşünce Zinciri Problem Çözme
### Sorun 1: Bir Ara Yazılım Ardışık Düzeni Oluşturun
**Sorun Açıklaması:** PHP web çerçevesi için her bir ara yazılımın, zincirdeki bir sonraki ara yazılımdan önce ve sonra isteği işleyebileceği bir ara katman yazılımı ardışık düzeni uygulayın.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) bir`Middleware`arayüzü, (2) ara yazılımı zincirleyen bir işlem hattı, (3) her ara yazılım bir istek ve bir`$next`geri çağrısı alır, (4) ara katman yazılımı hem isteği (öncesi) hem de yanıtı (sonra) değiştirebilir. Bu, Laravel, PSR-15 ve benzer çerçeveler tarafından kullanılan soğan modelidir.
**2. Adım — Yaklaşımı Belirleyin:**
- `MiddlewareInterface`'yi`process(Request, RequestHandler): Response`ile tanımlayın.
- Ara yazılımı tek bir işleyicide oluşturmak için dizi azaltmayı kullanın.
- Her ara katman yazılımı bir sonrakini sararak iç içe işlev çağrıları oluşturur.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Sıra önemlidir: ilk borulanan = en dıştaki (istek üzerine ilk olarak gerçekleştirilir, yanıt üzerine son olarak gerçekleştirilir).
- Her ara yazılım,`$next`çağrılmadan bir Yanıt döndürerek kısa devre yapabilir.
- Üretim: Herhangi bir PSR-15 çerçevesiyle birlikte çalışabilirlik için PSR-15 `MiddlewareInterface`'yi kullanın.
### Sorun 2: Sorgu Oluşturucu ile Depo Uygulama
**Sorun Açıklaması:** Parametreli sorgularla güvenli bir şekilde SQL oluşturan, zincirlemeyi destekleyen ve bir veri havuzu modeliyle entegre olan akıcı bir sorgu oluşturucu oluşturun.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) zincirlenebilir yöntemlere sahip bir`QueryBuilder`sınıfı (`select`,`where`,`orderBy`,`limit`), (2) SQL enjeksiyonunu önlemek için parametreli sorgular, (3) veri erişimi için sorgu oluşturucuyu kullanan bir `Repository`.
**2. Adım — Yaklaşımı Belirleyin:**
- Oluşturucu SQL parçalarını ve parametrelerini biriktirir.
- `toSql()`, yer tutucularla son sorguyu oluşturur.
-`getParameters()`sınırlanan değerleri döndürür.
- Depo, oluşturucuyu alana özgü yöntemlerle sarar.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- SQL enjeksiyon önleme: tüm değerler parametreli sorgulardan (`?` yer tutucular) geçer.
- Zincirlenebilir API: her yöntem akıcı kompozisyon için`$this`değerini döndürür.
- Üretim: Kapsamlı, test edilmiş bir çözüm için`illuminate/database`(Laravel'in sorgu oluşturucusu) veya `doctrine/dbal`'yi kullanın.
---

## Özet
PHP webin pragmatik beygiridir. Web sitelerinin çoğuna güç verir, devasa bir ekosisteme sahiptir ve modern PHP (8.x), uygun türler, numaralandırmalar ve temiz sözdizimiyle iyi tasarlanmış bir dildir. En zarif dil değildir ve her alan için uygun değildir; ancak web geliştirme, özellikle içerik yönetimi, e-ticaret ve serbest çalışma için PHP pratik ve yaygın olarak kullanılan bir seçim olmaya devam etmektedir.