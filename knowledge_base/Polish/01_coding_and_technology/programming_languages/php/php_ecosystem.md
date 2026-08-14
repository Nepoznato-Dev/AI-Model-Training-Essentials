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
# PHP — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, frameworki i infrastrukturę w ekosystemie PHP.
---

## Środowiska wykonawcze PHP
| Czas wykonania | Notatki |
|--------|-------|
| **PHP-FPM** | Menedżer procesów FastCGI (najczęściej) |
| **CLI** | Interfejs wiersza poleceń |
| **Słowo** | Asynchroniczny, oparty na współprogramie |
| **Biegacz drogowy** | Wysoka wydajność (oparta na Go) |
| **FrankenPHP** | Nowoczesny serwer aplikacji PHP (Go) |
| **PHP 8.3+** | Obecna stabilna z wyliczeniami, włóknami, tylko do odczytu |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **Kompozytor** | Menedżer zależności (w standardzie) |
| **Pakowacz** | Domyślne repozytorium pakietów |
| **Prywatny pakowacz** | Prywatny hosting pakietów |
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

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **Laravel** | Pełny stos | Najpopularniejsze, eleganckie API |
| **Symfony** | Pełny stos | Przedsiębiorstwo, komponenty |
| **Szczupły** | Mikro | API, małe aplikacje |
| **Światło** | Mikro (Laravel) | Szybkie mikrousługi |
| **CiastoPHP** | Pełny stos | Szybki rozwój |
| **Zapalnik kodu** | Lekki | Proste aplikacje |
| **Yii** | Pełny stos | Skoncentrowany na wydajności |
| **Spirala** | Nowoczesne | Długotrwałe, Swoole |
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

## Baza danych i ORM
| Technologia | Wpisz |
|------------|------|
| **Wymowny** | ORM Laravela (aktywny rekord) |
| **Doktryna** | Symfony ORM (mapowanie danych) |
| **Kreator zapytań** | Biegły konstruktor SQL |
| **ChNP** | Dostęp do bazy danych niskiego poziomu |
| **Migracja Laravel** | Zarządzanie schematami |
| **Finks** | Samodzielne migracje |
| **Trasa przelotowa** | Migracje baz danych |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **PHPUnit** | Standardowe ramy testów |
| **Szkodnik** | Eleganckie testowanie (zbudowane na PHPUnit) |
| **Laravel Zmierzch** | Testowanie przeglądarki |
| **Kpina** | Framework kpiący |
| **Infekcja** | Testowanie mutacji |
| **PHPStan** | Analiza statyczna (wyłapuje także błędy) |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **PHPStan** | Analiza statyczna (poziomy 0-9) |
| **Psalm** | Analiza statyczna (alternatywa) |
| **Laravel Pinta** | Styl kodu (Laravel) |
| **Naprawa PHP-CS** | Styl kodu (ogólnie) |
| **PHPMD** | Wykrywanie bałaganu |
| **PHP_CodeSniffer** | Wąchanie i styl |
| **Rektor** | Zautomatyzowana refaktoryzacja |
| **Deptrac** | Analiza zależności |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Silniki szablonów
| Silnik | Notatki |
|------------|-------|
| **Ostrze** | Silnik szablonów Laravela |
| **Gałązka** | Silnik szablonów Symfony |
| **Latte** | Bezpieczny silnik szablonów Nette |
| **Talerze** | Natywne szablony PHP |
---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **Przełknięcie** | Klient HTTP |
| **Symfony HttpClient** | Klient HTTP |
| **Węgiel** | Biblioteka daty/godziny |
| **Konsola Symfony** | Struktura CLI |
| **Monolog** | Rejestrowanie |
| **Kolejka Laravel** | Zadania w tle |
| **Kasjer Laravel** | Rozliczenia w paski |
| **Laravel Social** | Uwierzytelnianie OAuth |
| **Laravel Sanctum** | Uwierzytelnianie API |
| **Horyzont Laravel** | Panel kolejki Redis |
| **Przewód na żywo** | Dynamiczny interfejs użytkownika bez JS |
| **Inertia.js** | Adapter SPA (Vue/React + Laravel) |
| **Pakiety przestrzenne** | Wysokiej jakości media |
| **Pakiety ligowe** | Biblioteki społeczne |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **PhpStorm** | Najlepszy PHP IDE (JetBrains) |
| **Kod VS + PHP Intelefense** | Lekki, oparty na LSP |
| **Neovim + phpactor** | Oparte na terminalu |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **PHP-FPM + Nginx** | Klasyczna konfiguracja produkcyjna |
| **Apache + mod_php** | Tradycyjny |
| **Doker** | Konteneryzowany (php:fpm-alpine) |
| **Kuźnia Laravel** | Zarządzanie serwerem |
| **Laravel Vapor** | Wdrożenie AWS Lambda |
| **Wysłannik** | Wdrożenie bez przestojów |
| **Hosting współdzielony** | cPanel, Plesk |
| **RoadRunner / Swoole** | Długotrwałe PHP |
| **FrankenPHP** | Nowoczesny serwer aplikacji |
---

## Streszczenie
Ekosystem PHP jest zdominowany przez **Laravel** (elegancki, przyjazny programistom) i **Symfony** (korporacja, komponenty). Standardowy stos to: **Composer** dla pakietów, **Laravel** lub **Symfony** dla Internetu, **PHPUnit** lub **Pest** do testowania, **PHPStan** do analizy statycznej, **Laravel Pint** lub **PHP-CS-Fixer** do formatowania oraz **PHP-FPM** lub **RoadRunner** do serwowania. Nowoczesny PHP 8.3+ z wyliczeniami, włóknami, klasami tylko do odczytu i typami unii jest językiem o wiele bardziej wydajnym, niż sugeruje jego reputacja. Ekosystem wyróżnia się tworzeniem stron internetowych, zarządzaniem treścią (WordPress, Drupal) i e-commerce (Magento, WooCommerce).