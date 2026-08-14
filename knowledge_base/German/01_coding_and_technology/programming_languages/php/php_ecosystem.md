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
# PHP – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im PHP-Ökosystem.
---

## PHP-Laufzeiten
| Laufzeit | Notizen |
|---------|-------|
| **PHP-FPM** | FastCGI Process Manager (am häufigsten) |
| **CLI** | Befehlszeilenschnittstelle |
| **Swoole** | Asynchron, Coroutine-basiert |
| **RoadRunner** | Hochleistung (Go-basiert) |
| **FrankenPHP** | Moderner PHP-App-Server (Go) |
| **PHP 8.3+** | Derzeit stabil mit Enumerationen, Fasern, schreibgeschützt |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **Komponist** | Abhängigkeitsmanager (der Standard) |
| **Verpacker** | Standardpaket-Repository |
| **Privater Paketdienst** | Privates Paket-Hosting |
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

## Web-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **Laravel** | Full-Stack | Beliebteste und eleganteste API |
| **Symfony** | Full-Stack | Unternehmen, Komponenten |
| **Schlank** | Mikro | APIs, kleine Apps |
| **Lumen** | Mikro (Laravel) | Schnelle Mikrodienste |
| **CakePHP** | Full-Stack | Schnelle Entwicklung |
| **CodeIgniter** | Leicht | Einfache Apps |
| **Yii** | Full-Stack | Leistungsorientiert |
| **Spirale** | Modern | Langfristig, Swoole |
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

## Datenbank und ORM
| Technologie | Geben Sie | ein
|------------|------|
| **Eloquent** | Laravel's ORM (Active Record) |
| **Lehre** | Symfonys ORM (Data Mapper) |
| **Abfrage-Generator** | Fluent SQL-Builder |
| **PDO** | Low-Level-Datenbankzugriff |
| **Laravel-Migration** | Schemaverwaltung |
| **Phinx** | Standalone-Migrationen |
| **Flugbahn** | Datenbankmigrationen |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **PHPUnit** | Standardtest-Framework |
| **Schädling** | Elegantes Testen (aufgebaut auf PHPUnit) |
| **Laravel Dämmerung** | Browsertests |
| **Spott** | Spott-Framework |
| **Infektion** | Mutationstests |
| **phpStan** | Statische Analyse (fängt auch Fehler ab) |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **phpStan** | Statische Analyse (Stufen 0-9) |
| **Psalm** | Statische Analyse (alternativ) |
| **Laravel Pint** | Codestil (Laravel) |
| **PHP-CS-Fixer** | Codestil (allgemein) |
| **PHPMD** | Messerkennung |
| **PHP_CodeSniffer** | Schnüffeln und Stylen |
| **Rektor** | Automatisiertes Refactoring |
| **Deptrac** | Abhängigkeitsanalyse |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Template-Engines
| Motor | Notizen |
|--------|-------|
| **Klinge** | Laravels Template-Engine |
| **Zweig** | Symfonys Template-Engine |
| **Latte** | Nettes sichere Template-Engine |
| **Teller** | Native PHP-Vorlagen |
---

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Fressen** | HTTP-Client |
| **Symfony HttpClient** | HTTP-Client |
| **Kohlenstoff** | Datums-/Uhrzeitbibliothek |
| **Symfony-Konsole** | CLI-Framework |
| **Monolog** | Protokollierung |
| **Laravel-Warteschlange** | Hintergrundjobs |
| **Laravel-Kassiererin** | Stripe-Abrechnung |
| **Laravel-Socialite** | OAuth-Authentifizierung |
| **Laravel Sanctum** | API-Authentifizierung |
| **Laravel Horizon** | Redis-Warteschlangen-Dashboard |
| **Livewire** | Dynamische Benutzeroberfläche ohne JS |
| **Inertia.js** | SPA-Adapter (Vue/React + Laravel) |
| **Spatie-Pakete** | Hochwertige Versorgungsunternehmen |
| **Liga-Pakete** | Gemeinschaftsbibliotheken |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **PhpStorm** | Beste PHP-IDE (JetBrains) |
| **VS-Code + PHP Intelepense** | Leicht, LSP-basiert |
| **Neovim + PHPactor** | Terminalbasiert |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **PHP-FPM + Nginx** | Klassischer Produktionsaufbau |
| **Apache + mod_php** | Traditionell |
| **Docker** | Containerisiert (php:fpm-alpine) |
| **Laravel-Schmiede** | Serververwaltung |
| **Laravel-Dampf** | AWS Lambda-Bereitstellung |
| **Gesandter** | Bereitstellung ohne Ausfallzeiten |
| **Shared-Hosting** | cPanel, Plesk |
| **RoadRunner / Swoole** | Lang laufendes PHP |
| **FrankenPHP** | Moderner App-Server |
---

## Zusammenfassung
Das PHP-Ökosystem wird von **Laravel** (elegant, entwicklerfreundlich) und **Symfony** (Unternehmen, Komponenten) dominiert. Der Standard-Stack ist: **Composer** für Pakete, **Laravel** oder **Symfony** für das Web, **PHPUnit** oder **Pest** zum Testen, **PHPStan** für statische Analyse, **Laravel Pint** oder **PHP-CS-Fixer** für die Formatierung und **PHP-FPM** oder **RoadRunner** für die Bereitstellung. Modernes PHP 8.3+ mit Aufzählungen, Fasern, schreibgeschützten Klassen und Union-Typen ist eine viel leistungsfähigere Sprache, als ihr Ruf vermuten lässt. Das Ökosystem zeichnet sich durch Webentwicklung, Content-Management (WordPress, Drupal) und E-Commerce (Magento, WooCommerce) aus.