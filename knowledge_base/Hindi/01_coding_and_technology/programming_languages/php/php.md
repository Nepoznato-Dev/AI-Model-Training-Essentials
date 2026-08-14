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
#पीएचपी
PHP (हाइपरटेक्स्ट प्रीप्रोसेसर) एक सर्वर-साइड स्क्रिप्टिंग भाषा है जो 1994 में रासमस लेरडॉर्फ द्वारा बनाई गई थी और पहली बार 1995 में जारी की गई थी। मूल रूप से गतिशील वेब पेज बनाने के लिए डिज़ाइन किया गया, PHP एक पूर्ण-विशेषताओं वाली सामान्य प्रयोजन भाषा में विकसित हुई है। यह वर्डप्रेस, फेसबुक (मूल रूप से), विकिपीडिया, स्लैक और लाखों अन्य साइटों सहित ज्ञात सर्वर-साइड भाषा वाली सभी वेबसाइटों में से लगभग 75% को संचालित करता है।
आधुनिक PHP (8.x) 2000 के दशक की शुरुआत की PHP से बहुत अलग भाषा है। इसमें अब टाइप किए गए गुण, मिलान अभिव्यक्ति, एनम, फाइबर, केवल पढ़ने योग्य कक्षाएं और एक मजबूत प्रकार की प्रणाली है। डेवलपर्स के बीच इसकी प्रतिष्ठा (अक्सर विसंगतियों के लिए आलोचना) के बावजूद, PHP व्यावहारिक है, व्यापक रूप से तैनात है, और इसमें सुधार जारी है।
---

## PHP क्यों मायने रखती है
- **वेब प्रभुत्व**: ~75% वेबसाइट चलाता है। अकेले वर्डप्रेस 43% वेब पर अधिकार रखता है।
- **प्रवेश में कम बाधा**: किसी भी साझा होस्टिंग पर फ़ाइलें अपलोड करके तैनात करें। कोई संकलन नहीं, कोई निर्माण चरण नहीं।
- **परिपक्व पारिस्थितिकी तंत्र**: संगीतकार (पैकेज प्रबंधक), लारवेल, सिम्फनी - परिपक्व, युद्ध-परीक्षित उपकरण।
- **व्यावहारिक**: न्यूनतम सेटअप के साथ मिनटों में चलने वाली एक गतिशील वेबसाइट प्राप्त करें।
- **निरंतर सुधार**: PHP 8.x ने जीवन की गुणवत्ता में महत्वपूर्ण सुधार लाए हैं।
- **फ्रीलांसिंग बाजार**: वर्डप्रेस, लारवेल और ई-कॉमर्स (वूकॉमर्स, मैगेंटो) डेवलपर्स की भारी मांग।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **असंगत नामकरण** | `strpos`बनाम `str_replace`,`array_key_exists`बनाम`in_array`- कोई सुसंगत परंपरा नहीं | विसंगतियों को जानें; आईडीई स्वत: पूर्ण का उपयोग करें |
| **ऐतिहासिक सामान** | PHP 5 और उससे पहले की विरासत सुविधाएँ और पैटर्न | आधुनिक PHP (8.2+) का उपयोग करें; पीएसआर मानकों का पालन करें |
| **प्रदर्शन** | गैर-वेब कार्यों के लिए गो, रस्ट या जावा से धीमा | ओपीकैश का प्रयोग करें; एसिंक्स के लिए स्वूले पर विचार करें; PHP-FPM का उपयोग करें |
| **गैर-वेब के लिए आदर्श नहीं** | सीएलआई, डेस्कटॉप, मोबाइल, डेटा विज्ञान - PHP की ताकत नहीं | गैर-वेब कार्य के लिए पायथन, गो या अन्य भाषाओं का उपयोग करें |
| **सुरक्षा प्रतिष्ठा** | लीगेसी PHP कोड में कई सुरक्षा समस्याएं हैं | आधुनिक ढांचे का प्रयोग करें; सुरक्षा संबंधी सर्वोत्तम प्रक्रियाओं का पालन करें |
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संरचना
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

### कार्य एवं प्रकार
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

### कक्षाएं और ओओपी
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

### अभिव्यक्ति और नियंत्रण प्रवाह का मिलान करें
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

## पारिस्थितिकी तंत्र
### ढाँचे
| ढाँचा | शैली | के लिए सर्वश्रेष्ठ |
|----|-------|-------|
| **लारवेल** | पूर्ण-स्टैक, सुंदर वाक्यविन्यास | अधिकांश वेब एप्लिकेशन; सबसे बड़ा PHP ढांचा |
| **सिम्फनी** | उद्यम, घटक-आधारित | बड़े उद्यम अनुप्रयोग |
| **स्लिम** | माइक्रो-फ्रेमवर्क | एपीआई और छोटे अनुप्रयोग |
| **वर्डप्रेस** | सीएमएस | ब्लॉग, सामग्री साइटें, लघु व्यवसाय वेबसाइटें |
### आवश्यक उपकरण
| उपकरण | उद्देश्य |
|------|---------|
| **संगीतकार** | निर्भरता प्रबंधक (जैसे एनपीएम/पिप) |
| **पीएचपीयूनिट** | परीक्षण रूपरेखा |
| **PHPStan/स्तोत्र** | स्थैतिक विश्लेषण (बिना कोड चलाए बग ढूंढता है) |
| **लारवेल सेल/झुंड** | स्थानीय विकास वातावरण |
| **पीएसआर मानक** | कोडिंग शैली और इंटरफ़ेस मानक |
---

## उन्नत सिंटैक्स और पैटर्न
### PHPDoc और टेम्प्लेट के माध्यम से जेनेरिक
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

### विशेषताएँ (PHP 8.0+) - मूल एनोटेशन
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

### क्लोजर और उच्च-क्रम के कार्य
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

### फ़ाइबर (PHP 8.1+) - सहकारी मल्टीटास्किंग
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

### लक्षण - क्षैतिज कोड का पुन: उपयोग
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

## समवर्ती एवं समांतरता
### सहकारी समवर्ती के लिए फाइबर
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

### स्वूले - कॉरआउटिन-आधारित कॉनकरेंसी
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

### समानांतर विस्तार
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना (लारवेल)
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

### कंपोज़र.जेसन - निर्भरता प्रबंधन
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

### निर्भरता आदेश
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### PHPUnit - परीक्षण ढाँचा
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

### लारवेल फ़ीचर टेस्ट
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

### उपहास के साथ उपहास
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

### टेस्ट कमांड
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## अंतरसंचालनीयता
### सी एक्सटेंशन
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

### एफएफआई - विदेशी फ़ंक्शन इंटरफ़ेस (पीएचपी 7.4+)
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

### पीएसआर मानक
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## डिज़ाइन पैटर्न
### रिपॉजिटरी पैटर्न
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

### मिडलवेयर पैटर्न
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

### सर्विस कंटेनर/निर्भरता इंजेक्शन
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

## प्रदर्शन और अनुकूलन
### प्रोफाइलिंग उपकरण
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### अनुकूलन तकनीकें
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

## तैनाती
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

### डॉकर परिनियोजन
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

## PHP का उपयोग कब करें
| परिदृश्य | PHP क्यों | बेहतर विकल्प |
|---|---|-----|
| वर्डप्रेस विकास | PHP ही एकमात्र विकल्प है | — |
| फ्रीलांस वेब डेवलपमेंट | विशाल बाज़ार; तैनात करना आसान | — |
| ई-कॉमर्स (वूकॉमर्स, मैगेंटो) | स्थापित PHP प्लेटफ़ॉर्म | — |
| रैपिड वेब प्रोटोटाइपिंग | कम सेटअप, तैनात करने में तेज़ | नोड.जेएस, पायथन |
| सामग्री-भारी वेबसाइटें | सीएमएस पारिस्थितिकी तंत्र परिपक्व है | — |
| एपीआई और माइक्रोसर्विसेज | लारवेल/स्लिम के साथ संभव | जाओ, नोड.जेएस, पायथन |
| सीएलआई उपकरण | संभव है लेकिन आदर्श नहीं | जाओ, अजगर, जंग |
| वास्तविक समय अनुप्रयोग | PHP की ताकत नहीं | नोड.जेएस, जाओ |
| डेटा साइंस/एमएल | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
| डेस्कटॉप/मोबाइल ऐप्स | अनुकूल नहीं | देशी भाषाओं का प्रयोग करें |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: PHP में`==`और`===`के बीच क्या अंतर है?
**ए:**`==`ढीली तुलना है - यह तुलना करने से पहले प्रकार का ज़बरदस्ती करता है (`"0" == false``true`है)। `===`सख्त तुलना है - यह मूल्य और प्रकार दोनों की जांच करता है (`"0" === false``false`है)। हमेशा`===`का उपयोग करें जब तक कि आपको विशेष रूप से किसी प्रकार की जबरदस्ती की आवश्यकता न हो। यह PHP में बग के सबसे आम स्रोतों में से एक है।
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

### Q2: PHP नेमस्पेस और ऑटोलोडिंग कैसे काम करते हैं?
**ए:** नेमस्पेस वर्ग नाम टकराव को रोकते हैं। PSR-4 ऑटोलोडिंग नेमस्पेस संरचना को निर्देशिका संरचना में मैप करता है -`App\Controllers\UserController`मैप`src/Controllers/UserController.php`पर। संगीतकार`composer.json`के माध्यम से ऑटोलोडिंग को संभालता है। आधुनिक PHP में हमेशा नेमस्पेस और PSR-4 का उपयोग करें।
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

### Q3: PHP 8 विशेषताएँ क्या हैं, और वे फ़्रेमवर्क से कैसे संबंधित हैं?
**ए:** विशेषताएँ (PHP 8) कक्षाओं, विधियों, गुणों और मापदंडों के लिए संरचित मेटाडेटा एनोटेशन हैं। वे जावा एनोटेशन या C# विशेषताओं के PHP समकक्ष हैं। लारवेल और सिम्फनी जैसे फ्रेमवर्क रूटिंग, सत्यापन और निर्भरता इंजेक्शन के लिए बड़े पैमाने पर उनका उपयोग करते हैं।
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

### Q4: मैं आधुनिक PHP में त्रुटियों को ठीक से कैसे संभालूं?
**ए:** PHP में त्रुटियाँ (E_WARNING, E_NOTICE) और अपवाद दोनों हैं। आधुनिक PHP विशेष रूप से अपवादों का उपयोग करता है। अपेक्षित विफलताओं के लिए प्रयास/पकड़, डोमेन त्रुटियों के लिए कस्टम अपवाद वर्ग और त्रुटियों को अपवादों में बदलने के लिए`set_error_handler`का उपयोग करें। PHP 7+`Throwable`त्रुटियों और अपवादों दोनों के लिए आधार इंटरफ़ेस है।
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

### Q5: PHP फाइबर क्या हैं, और वे async से कैसे संबंधित हैं?
**ए:** फाइबर (पीएचपी 8.1) हल्के सहकारी धागे हैं - वे निष्पादन को निलंबित और फिर से शुरू कर सकते हैं। वे एसिंक PHP की नींव हैं लेकिन निम्न स्तर के हैं। Amp और ReactPHP जैसे फ्रेमवर्क आंतरिक रूप से फाइबर का उपयोग करते हैं। अधिकांश अनुप्रयोगों के लिए, कच्चे फाइबर के बजाय एसिंक फ्रेमवर्क का उपयोग करें।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक मिडलवेयर पाइपलाइन बनाएँ
**समस्या कथन:** एक PHP वेब फ्रेमवर्क के लिए एक मिडलवेयर पाइपलाइन लागू करें जहां प्रत्येक मिडलवेयर श्रृंखला में अगले मिडलवेयर से पहले और बाद में अनुरोध को संसाधित कर सकता है।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) एक`Middleware`इंटरफ़ेस, (2) एक पाइपलाइन जो मिडलवेयर को चेन करती है, (3) प्रत्येक मिडलवेयर को एक अनुरोध और एक`$next`कॉलबैक प्राप्त होता है, (4) मिडलवेयर अनुरोध (पहले) और प्रतिक्रिया (बाद) दोनों को संशोधित कर सकता है। यह लारवेल, पीएसआर-15 और इसी तरह के ढांचे द्वारा उपयोग किया जाने वाला प्याज मॉडल है।
**चरण 2 - दृष्टिकोण को पहचानें:**
-`process(Request, RequestHandler): Response`के साथ`MiddlewareInterface`को परिभाषित करें।
- मिडलवेयर को एकल हैंडलर में संकलित करने के लिए ऐरे रिडक्शन का उपयोग करें।
- प्रत्येक मिडलवेयर अगले को लपेटता है, नेस्टेड फ़ंक्शन कॉल बनाता है।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- आदेश मायने रखता है: पहला पाइप = सबसे बाहरी (अनुरोध पर पहले निष्पादित, प्रतिक्रिया पर अंतिम)।
- प्रत्येक मिडलवेयर`$next`को कॉल किए बिना प्रतिक्रिया लौटाकर शॉर्ट-सर्किट कर सकता है।
- उत्पादन: किसी भी PSR-15 ढांचे के साथ अंतरसंचालनीयता के लिए PSR-15`MiddlewareInterface`का उपयोग करें।
### समस्या 2: क्वेरी बिल्डर के साथ एक रिपोजिटरी लागू करें
**समस्या कथन:** एक धाराप्रवाह क्वेरी बिल्डर बनाएं जो पैरामीटरयुक्त प्रश्नों के साथ सुरक्षित रूप से एसक्यूएल उत्पन्न करता है, चेनिंग का समर्थन करता है, और रिपॉजिटरी पैटर्न के साथ एकीकृत होता है।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) श्रृंखलाबद्ध तरीकों के साथ एक`QueryBuilder`वर्ग (
**चरण 2 - दृष्टिकोण को पहचानें:**
- बिल्डर SQL टुकड़े और पैरामीटर जमा करता है।
-`toSql()`प्लेसहोल्डर्स के साथ अंतिम क्वेरी उत्पन्न करता है।
-`getParameters()`बाउंड मान लौटाता है।
- रिपोजिटरी बिल्डर को डोमेन-विशिष्ट तरीकों से लपेटता है।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- एसक्यूएल इंजेक्शन रोकथाम: सभी मान पैरामीटरयुक्त प्रश्नों (`?` प्लेसहोल्डर्स) से गुजरते हैं।
- चेनएबल एपीआई: प्रत्येक विधि धाराप्रवाह रचना के लिए`$this`लौटाती है।
- उत्पादन: व्यापक, परीक्षणित समाधान के लिए`illuminate/database`(लारवेल का क्वेरी बिल्डर) या`doctrine/dbal`का उपयोग करें।
---

## सारांश
PHP वेब का व्यावहारिक वर्कहॉर्स है। यह अधिकांश वेबसाइटों को शक्ति प्रदान करता है, इसमें एक विशाल पारिस्थितिकी तंत्र है, और आधुनिक PHP (8.x) उचित प्रकार, एनम और स्वच्छ वाक्यविन्यास के साथ एक अच्छी तरह से डिज़ाइन की गई भाषा है। यह सबसे सुंदर भाषा नहीं है, और यह हर डोमेन के लिए उपयुक्त नहीं है - लेकिन वेब विकास, विशेष रूप से सामग्री प्रबंधन, ई-कॉमर्स और फ्रीलांसिंग के लिए, PHP एक व्यावहारिक और व्यापक रूप से नियोजित विकल्प बनी हुई है।