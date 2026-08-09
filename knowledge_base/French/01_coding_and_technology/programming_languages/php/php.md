---
# Métadonnées
titre : "PHP"
description : "Référence complète sur le langage de programmation PHP couvrant la présentation, les compromis, les principes fondamentaux de la syntaxe, l'écosystème et quand l'utiliser."
catégorie : "Codage et technologie"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances en matière de codage et de technologie"
next_review : "2027-08-05"
#Classement
balises : [php, langage de programmation, syntaxe, écosystème, codage et technologie]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "34 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
#PHP
PHP (Hypertext Preprocessor) est un langage de script côté serveur créé par Rasmus Lerdorf en 1994 et lancé pour la première fois en 1995. Conçu à l'origine pour générer des pages Web dynamiques, PHP est devenu un langage polyvalent et complet. Il alimente environ 75 % de tous les sites Web dotés d’un langage côté serveur connu, notamment WordPress, Facebook (à l’origine), Wikipedia, Slack et des millions d’autres sites.
Le PHP moderne (8.x) est un langage très différent du PHP du début des années 2000. Il possède désormais des propriétés typées, des expressions de correspondance, des énumérations, des fibres, des classes en lecture seule et un système de types robuste. Malgré sa réputation auprès des développeurs (souvent critiquée pour ses incohérences), PHP est pratique, largement déployé et ne cesse de s'améliorer.
---

## Pourquoi PHP est important
- **Dominance du Web** : gère environ 75 % des sites Web. WordPress alimente à lui seul 43 % du Web.
- **Faible barrière à l'entrée** : déployez en téléchargeant des fichiers sur n'importe quel hébergement partagé. Pas de compilation, pas d'étape de build.
- **Écosystème mature** : Composer (gestionnaire de packages), Laravel, Symfony — outils matures et testés au combat.
- **Pratique** : Obtenez un site Web dynamique opérationnel en quelques minutes avec une configuration minimale.
- **Amélioration continue** : PHP 8.x a apporté des améliorations significatives en termes de qualité de vie.
- **Marché du freelance** : demande énorme pour les développeurs WordPress, Laravel et e-commerce (WooCommerce, Magento).
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Nom incohérent** | `strpos`contre`str_replace`,`array_key_exists`contre`in_array`— pas de convention cohérente | Apprenez les incohérences ; utiliser la saisie semi-automatique de l'IDE |
| **Bagages historiques** | Fonctionnalités et modèles hérités de PHP 5 et versions antérieures | Utiliser du PHP moderne (8.2+) ; suivre les normes PSR |
| **Performances** | Plus lent que Go, Rust ou Java pour les tâches non Web | Utilisez OPcache ; considérez Swoole pour l'asynchrone ; utiliser PHP-FPM |
| **Pas idéal pour le non-Web** | CLI, ordinateur de bureau, mobile, science des données : ce ne sont pas les points forts de PHP | Utiliser Python, Go ou d'autres langages pour le travail non Web |
| **Réputation en matière de sécurité** | Le code PHP existant présente de nombreux problèmes de sécurité | Utiliser des frameworks modernes ; suivre les meilleures pratiques de sécurité |
---

## Fondamentaux de la syntaxe
### Structure de base
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

### Fonctions et types
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

### Classes et POO
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

### Faire correspondre l'expression et le flux de contrôle
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

## L'écosystème
### Cadres
| Cadre | Style | Idéal pour |
|---------------|-------|--------------|
| **Laravel** | Syntaxe complète et élégante | La plupart des applications Web ; le plus grand framework PHP |
| **Symfony** | Entreprise, basée sur des composants | Applications pour grandes entreprises |
| **Mince** | Micro-framework | API et petites applications |
| **WordPress** | CMS | Blogs, sites de contenu, sites Web pour petites entreprises |
### Outils essentiels
| Outil | Objectif |
|------|--------------|
| **Compositeur** | Gestionnaire de dépendances (comme npm/pip) |
| **PHPUnit** | Cadre de test |
| **PHPStan / Psaume** | Analyse statique (trouve les bogues sans exécuter de code) |
| **Voile Laravel / Troupeau** | Environnements de développement local |
| **Normes PSR** | Style de codage et normes d'interface |
---

## Syntaxe et modèles avancés
### Génériques via PHPDoc et modèles
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

### Attributs (PHP 8.0+) — Annotations natives
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

### Fermetures et fonctions d'ordre supérieur
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

### Fibres (PHP 8.1+) — Multitâche coopératif
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

### Traits — Réutilisation du code horizontal
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

## Concurrence et parallélisme
### Fibres pour la concurrence coopérative
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

### Swoole — Concurrence basée sur Coroutine
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

### Extension parallèle
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

## Configuration du projet et système de construction
### Structure du projet (Laravel)
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

### composer.json — Gestion des dépendances
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

### Commandes de dépendance
```bash
composer install              # Install dependencies
composer update               # Update dependencies
composer require stripe/stripe-php  # Add package
composer remove stripe/stripe-php   # Remove package
composer dump-autoload        # Regenerate autoload
composer outdated             # List outdated packages
```

### Pipeline CI/CD (actions GitHub)
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

## Tests
### PHPUnit — Cadre de test
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

### Tests de fonctionnalités Laravel
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

### Se moquer de la moquerie
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

### Tester les commandes
```bash
vendor/bin/phpunit                     # Run all tests
vendor/bin/phpunit --filter testCreate # Run specific test
php artisan test                       # Laravel test runner
php artisan test --coverage            # With coverage report
```

---

## Interopérabilité
### Extensions C
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

### FFI — Interface de fonction étrangère (PHP 7.4+)
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

### Normes PSR
```php
// PSR-4: Autoloading — maps namespaces to directories
// PSR-7: HTTP Message Interface
// PSR-11: Container Interface
// PSR-15: HTTP Server Middleware

use Psr\Http\Message\ServerRequestInterface;
use Psr\Container\ContainerInterface;
```
---

## Modèles de conception
### Modèle de référentiel
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

### Modèle de middleware
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

### Conteneur de services / Injection de dépendances
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

## Performances et optimisation
### Outils de profilage
```bash
# Xdebug profiler: php.ini: xdebug.mode=profile
# OPcache (production): opcache.enable=1 opcache.memory_consumption=256
# Benchmarking: wrk -t12 -c400 -d30s http://localhost/api/users
```

### Techniques d'optimisation
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

## Déploiement
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

### Déploiement de Docker
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

## Quand utiliser PHP
| Scénario | Pourquoi PHP | Meilleure alternative |
|--------------|---------|-------------------|
| Développement WordPress | PHP est la seule option | — |
| Développement web indépendant | Immense marché ; facile à déployer | — |
| Commerce électronique (WooCommerce, Magento) | Plateformes PHP établies | — |
| Prototypage Web rapide | Faible configuration, rapide à déployer | Node.js, Python |
| Sites Web riches en contenu | L'écosystème CMS est mature | — |
| API et microservices | Possible avec Laravel/Slim | Allez, Node.js, Python |
| Outils CLI | Possible mais pas idéal | Allez, Python, Rouille |
| Applications en temps réel | Ce n'est pas la force de PHP | Node.js, allez |
| Science des données / ML | Pas l'écosystème | Python, R |
| Applications de bureau/mobiles | Ne convient pas | Utiliser des langues maternelles |
---

## Résumé
PHP est le cheval de bataille pragmatique du Web. Il alimente la majorité des sites Web, possède un écosystème massif et PHP moderne (8.x) est un langage bien conçu avec des types, des énumérations et une syntaxe propre. Ce n'est pas le langage le plus élégant et il ne convient pas à tous les domaines, mais pour le développement Web, en particulier la gestion de contenu, le commerce électronique et le travail indépendant, PHP reste un choix pratique et largement utilisé.