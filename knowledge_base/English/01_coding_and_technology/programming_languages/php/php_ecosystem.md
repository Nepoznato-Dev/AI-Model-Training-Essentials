<!--
---
# Metadata
title: "PHP — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the PHP ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [php, ecosystem, tooling, composer, laravel, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "16 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# PHP — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the PHP ecosystem.

---

## PHP Runtimes

| Runtime | Notes |
|---------|-------|
| **PHP-FPM** | FastCGI Process Manager (most common) |
| **CLI** | Command-line interface |
| **Swoole** | Async, coroutine-based |
| **RoadRunner** | High-performance (Go-based) |
| **FrankenPHP** | Modern PHP app server (Go) |
| **PHP 8.3+** | Current stable with enums, fibers, readonly |

```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Package Management

| Tool | Purpose |
|------|---------|
| **Composer** | Dependency manager (the standard) |
| **Packagist** | Default package repository |
| **Private Packagist** | Private package hosting |

```json
// composer.json
{
    "name": "myapp/web",
    "require": {
        "php": "^8.2",
        "laravel/framework": "^11.0",
        "guzzlehttp/guzzle": "^7.8"
    },
    "require-dev": {
        "phpunit/phpunit": "^11.0",
        "laravel/pint": "^1.13",
        "phpstan/phpstan": "^1.10"
    },
    "autoload": {
        "psr-4": {"App\\": "app/"}
    }
}
```

```bash
composer install            # install dependencies
composer update             # update packages
composer require guzzlehttp/guzzle  # add package
composer dump-autoload      # regenerate autoloader
```

---

## Web Frameworks

| Framework | Type | Best For |
|-----------|------|----------|
| **Laravel** | Full-stack | Most popular, elegant API |
| **Symfony** | Full-stack | Enterprise, components |
| **Slim** | Micro | APIs, small apps |
| **Lumen** | Micro (Laravel) | Fast micro-services |
| **CakePHP** | Full-stack | Rapid development |
| **CodeIgniter** | Lightweight | Simple apps |
| **Yii** | Full-stack | Performance-focused |
| **Spiral** | Modern | Long-running, Swoole |

```php
// Laravel route example
Route::get('/users/{id}', function (int $id) {
    $user = User::findOrFail($id);
    return response()->json($user);
});

Route::post('/users', function (Request $request) {
    $validated = $request->validate([
        'name'  => 'required|string|max:255',
        'email' => 'required|email|unique:users',
    ]);
    $user = User::create($validated);
    return response()->json($user, 201);
});
```

```php
// Symfony controller
#[Route('/api/users/{id}', methods: ['GET'])]
public function show(int $id, UserRepository $repo): JsonResponse
{
    $user = $repo->find($id) ?? throw new NotFoundHttpException();
    return $this->json($user);
}
```

---

## Database & ORM

| Technology | Type |
|------------|------|
| **Eloquent** | Laravel's ORM (Active Record) |
| **Doctrine** | Symfony's ORM (Data Mapper) |
| **Query Builder** | Fluent SQL builder |
| **PDO** | Low-level database access |
| **Laravel Migration** | Schema management |
| **Phinx** | Standalone migrations |
| **Flyway** | Database migrations |

```php
// Eloquent example
class User extends Model {
    protected $fillable = ['name', 'email'];
    
    public function posts(): HasMany {
        return $this->hasMany(Post::class);
    }
}

$users = User::where('active', true)
    ->with('posts')
    ->orderBy('name')
    ->paginate(20);
```

---

## Testing

| Framework | Purpose |
|-----------|---------|
| **PHPUnit** | Standard test framework |
| **Pest** | Elegant testing (built on PHPUnit) |
| **Laravel Dusk** | Browser testing |
| **Mockery** | Mocking framework |
| **Infection** | Mutation testing |
| **PHPStan** | Static analysis (also catches bugs) |

```php
// Pest example
test('creates user successfully', function () {
    $response = $this->postJson('/api/users', [
        'name'  => 'Alice',
        'email' => 'alice@example.com',
    ]);

    $response->assertStatus(201)
        ->assertJsonStructure(['id', 'name', 'email']);
});

// PHPUnit example
class UserServiceTest extends TestCase
{
    public function test_finds_user_by_id(): void
    {
        $repo = Mockery::mock(UserRepository::class);
        $repo->shouldReceive('find')->with(1)->andReturn(new User('Alice'));
        $service = new UserService($repo);

        $user = $service->find(1);

        $this->assertEquals('Alice', $user->name);
    }
}
```

---

## Code Quality

| Tool | Purpose |
|------|---------|
| **PHPStan** | Static analysis (levels 0-9) |
| **Psalm** | Static analysis (alternative) |
| **Laravel Pint** | Code style (Laravel) |
| **PHP-CS-Fixer** | Code style (general) |
| **PHPMD** | Mess detection |
| **PHP_CodeSniffer** | Sniffing and style |
| **Rector** | Automated refactoring |
| **Deptrac** | Dependency analysis |

```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Template Engines

| Engine | Notes |
|--------|-------|
| **Blade** | Laravel's template engine |
| **Twig** | Symfony's template engine |
| **Latte** | Nette's safe template engine |
| **Plates** | Native PHP templates |

---

## Key Libraries

| Library | Purpose |
|---------|---------|
| **Guzzle** | HTTP client |
| **Symfony HttpClient** | HTTP client |
| **Carbon** | Date/time library |
| **Symfony Console** | CLI framework |
| **Monolog** | Logging |
| **Laravel Queue** | Background jobs |
| **Laravel Cashier** | Stripe billing |
| **Laravel Socialite** | OAuth authentication |
| **Laravel Sanctum** | API authentication |
| **Laravel Horizon** | Redis queue dashboard |
| **Livewire** | Dynamic UI without JS |
| **Inertia.js** | SPA adapter (Vue/React + Laravel) |
| **Spatie packages** | High-quality utilities |
| **League packages** | Community libraries |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **PhpStorm** | Best PHP IDE (JetBrains) |
| **VS Code + PHP Intelephense** | Lightweight, LSP-based |
| **Neovim + phpactor** | Terminal-based |

---

## Deployment

| Method | Notes |
|--------|-------|
| **PHP-FPM + Nginx** | Classic production setup |
| **Apache + mod_php** | Traditional |
| **Docker** | Containerized (php:fpm-alpine) |
| **Laravel Forge** | Server management |
| **Laravel Vapor** | AWS Lambda deployment |
| **Envoyer** | Zero-downtime deployment |
| **Shared hosting** | cPanel, Plesk |
| **RoadRunner / Swoole** | Long-running PHP |
| **FrankenPHP** | Modern app server |

---

## Summary

PHP's ecosystem is dominated by **Laravel** (elegant, developer-friendly) and **Symfony** (enterprise, components). The standard stack is: **Composer** for packages, **Laravel** or **Symfony** for web, **PHPUnit** or **Pest** for testing, **PHPStan** for static analysis, **Laravel Pint** or **PHP-CS-Fixer** for formatting, and **PHP-FPM** or **RoadRunner** for serving. Modern PHP 8.3+ with enums, fibers, readonly classes, and union types is a much more capable language than its reputation suggests. The ecosystem excels at web development, content management (WordPress, Drupal), and e-commerce (Magento, WooCommerce).
