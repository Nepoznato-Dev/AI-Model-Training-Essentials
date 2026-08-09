---
# البيانات الوصفية
العنوان: "PHP"
الوصف: "مرجع شامل للغة برمجة PHP يغطي نظرة عامة، والمقايضات، وأساسيات بناء الجملة، والنظام البيئي، ومتى يتم استخدامها."
الفئة: "البرمجة والتكنولوجيا"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
تمت المراجعة بواسطة: "فريق قاعدة معارف البرمجة والتكنولوجيا"
next_review: "2027-08-05"
# التصنيف
العلامات: [php، لغة البرمجة، بناء الجملة، النظام البيئي، الترميز والتكنولوجيا]
مستوى الصعوبة: "متوسط"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "34 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
# PHP
PHP (المعالج المسبق للنص التشعبي) هي لغة برمجة نصية من جانب الخادم أنشأها راسموس ليردورف في عام 1994 وتم إصدارها لأول مرة في عام 1995. تم تصميم PHP في الأصل لإنشاء صفحات ويب ديناميكية، وقد تطورت إلى لغة كاملة الميزات للأغراض العامة. إنه يشغل ما يقرب من 75% من جميع مواقع الويب ذات لغة الخادم المعروفة، بما في ذلك WordPress وFacebook (في الأصل) وWikipedia وSlack وملايين المواقع الأخرى.
تعد PHP الحديثة (8.x) لغة مختلفة تمامًا عن PHP في أوائل العقد الأول من القرن الحادي والعشرين. أصبح لديه الآن خصائص مكتوبة، وتعبيرات مطابقة، وتعدادات، وألياف، وفئات للقراءة فقط، ونظام كتابة قوي. على الرغم من سمعتها بين المطورين (غالبًا ما يتم انتقادها بسبب التناقضات)، إلا أن لغة PHP عملية ومنتشرة على نطاق واسع وتستمر في التحسن.
---

## لماذا PHP مهم
- **الهيمنة على الويب**: تدير ما يقرب من 75% من مواقع الويب. يعمل WordPress وحده على تشغيل 43% من الويب.
- **عائق الدخول منخفض**: يتم النشر عن طريق تحميل الملفات إلى أي استضافة مشتركة. لا يوجد تجميع ولا خطوة بناء.
- **النظام البيئي الناضج**: Composer (مدير الحزم)، Laravel، Symfony — أدوات ناضجة تم اختبارها في المعركة.
- **عملي**: احصل على موقع ويب ديناميكي يعمل في دقائق مع الحد الأدنى من الإعداد.
- **التحسين المستمر**: جلب PHP 8.x تحسينات كبيرة في جودة الحياة.
- **سوق العمل الحر**: طلب كبير على مطوري WordPress وLaravel والتجارة الإلكترونية (WooCommerce وMagento).
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **تسمية غير متناسقة** | `strpos`مقابل `str_replace`،`array_key_exists`مقابل`in_array`- لا توجد اتفاقية متسقة | تعلم التناقضات. استخدام الإكمال التلقائي IDE |
| ** الأمتعة التاريخية ** | الميزات والأنماط القديمة من PHP 5 والإصدارات الأقدم | استخدم لغة PHP الحديثة (8.2+)؛ اتبع معايير PSR |
| **الأداء** | أبطأ من Go أو Rust أو Java للمهام غير المتعلقة بالويب | استخدم OPcache؛ خذ بعين الاعتبار استخدام Swoole كخيار غير متزامن؛ استخدم PHP-FPM |
| ** ليست مثالية لغير الويب ** | واجهة سطر الأوامر (CLI)، وسطح المكتب، والجوال، وعلوم البيانات - ليست نقاط قوة PHP | استخدم Python أو Go أو لغات أخرى للعمل خارج الويب |
| **السمعة الأمنية** | يحتوي كود PHP القديم على العديد من المشكلات الأمنية | استخدام الأطر الحديثة؛ اتبع أفضل الممارسات الأمنية |
---

## أساسيات بناء الجملة
### البنية الأساسية
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

### الوظائف والأنواع
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

### الفصول و OOP
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

### مطابقة تدفق التعبير والتحكم
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

## النظام البيئي
### الأطر
| الإطار | النمط | الأفضل لـ |
|-----------|------|----------|
| **لارافيل** | بناء جملة متكامل وأنيق | معظم تطبيقات الويب؛ أكبر إطار عمل PHP |
| **سيمفوني** | المؤسسة، القائمة على المكونات | تطبيقات المؤسسات الكبيرة |
| ** سليم ** | الإطار الجزئي | واجهات برمجة التطبيقات والتطبيقات الصغيرة |
| **ووردبريس** | نظام إدارة المحتوى | المدونات، مواقع المحتوى، مواقع الأعمال الصغيرة |
### الأدوات الأساسية
| أداة | الغرض |
|------|---------|
| ** الملحن ** | مدير التبعية (مثل npm/pip) |
| ** PHPUnit ** | إطار الاختبار |
| **PHPStan / مزمور** | التحليل الثابت (يبحث عن الأخطاء دون تشغيل التعليمات البرمجية) |
| **شراع لارافيل / قطيع** | بيئات التنمية المحلية |
| **معايير PSR** | أسلوب الترميز ومعايير الواجهة |
---

## بناء الجملة والأنماط المتقدمة
### الأدوية العامة عبر PHPDoc والقوالب
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

### السمات (PHP 8.0+) — التعليقات التوضيحية الأصلية
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

### عمليات الإغلاق والوظائف ذات الترتيب الأعلى
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

### الألياف (PHP 8.1+) — تعدد المهام التعاوني
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

### السمات — إعادة استخدام الكود الأفقي
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

## التزامن والتوازي
### ألياف للتزامن التعاوني
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

### Swoole — التزامن القائم على Coroutine
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

### الامتداد الموازي
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

## تكوين المشروع ونظام البناء
### هيكل المشروع (لارافيل)
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

### الملحن.json — إدارة التبعيات
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

### أوامر التبعية
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### خط أنابيب CI/CD (إجراءات GitHub)
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

## الاختبار
### PHPUnit — إطار الاختبار
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

### اختبارات ميزات Laravel
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

### السخرية بالسخرية
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

### أوامر الاختبار
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## إمكانية التشغيل البيني
### ملحقات C
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

### FFI — واجهة الوظائف الخارجية (PHP 7.4+)
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

### معايير PSR
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## أنماط التصميم
### نمط المستودع
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

### نمط الوسيطة
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

### حاوية الخدمة / حقن التبعية
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

## الأداء والتحسين
### أدوات التنميط
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### تقنيات التحسين
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

## النشر
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

### نشر عامل الميناء
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

## متى تستخدم PHP
| السيناريو | لماذا PHP | البديل الأفضل |
|----------|--------|------------------|
| تطوير ووردبريس | PHP هو الخيار الوحيد | — |
| تطوير الويب لحسابهم الخاص | سوق ضخمة؛ من السهل نشر | — |
| التجارة الإلكترونية (WooCommerce، Magento) | تأسيس منصات PHP | — |
| النماذج الأولية السريعة للويب | إعداد منخفض وسريع النشر | Node.js، بايثون |
| مواقع الويب ذات المحتوى الثقيل | النظام البيئي CMS ناضج | — |
| واجهات برمجة التطبيقات والخدمات الصغيرة | ممكن مع Laravel/Slim | اذهب، Node.js، بايثون |
| أدوات سطر الأوامر | ممكن ولكن ليس مثاليا | اذهب، بايثون، روست |
| تطبيقات في الوقت الحقيقي | ليست قوة PHP | Node.js، اذهب |
| علم البيانات / تعلم الآلة | ليس النظام البيئي | بايثون، ر |
| تطبيقات سطح المكتب/الجوال | غير مناسب | استخدم اللغات الأصلية |
---

## ملخص
PHP هو العمود الفقري العملي للويب. إنها تشغل غالبية مواقع الويب، ولديها نظام بيئي ضخم، وPHP (8.x) الحديثة هي لغة مصممة جيدًا بأنواع مناسبة، وتعدادات، وبناء جملة نظيف. إنها ليست اللغة الأكثر أناقة، وليست مناسبة لكل مجال - ولكن لتطوير الويب، وخاصة إدارة المحتوى، والتجارة الإلكترونية، والعمل الحر، تظل لغة PHP خيارًا عمليًا ومستخدمًا على نطاق واسع.