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
# PHP: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e l'infrastruttura essenziali nell'ecosistema PHP.
---

## Runtime PHP
| Durata | Note |
|---------|-------|
| **PHP-FPM** | Gestore processi FastCGI (più comune) |
| **CLI** | Interfaccia della riga di comando |
| **Lana** | Asincrono, basato su coroutine |
| **RoadRunner** | Ad alte prestazioni (basato su Go) |
| **FrankenPHP** | Server di app PHP moderno (Go) |
| **PHP 8.3+** | Corrente stabile con enumerazioni, fibre, sola lettura |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Gestione dei pacchetti
| Strumento | Scopo |
|------|---------|
| **Compositore** | Gestore delle dipendenze (lo standard) |
| **Packagista** | Repository dei pacchetti predefinito |
| **Packagista privato** | Hosting di pacchetti privati ​​|
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

## Framework Web
| Quadro | Digitare | Ideale per |
|-----------|------|----------|
| **Laravel** | Stack completo | API più popolare ed elegante |
| **Sinfonia** | Stack completo | Impresa, componenti |
| **Sottile** | Micro | API, piccole app |
| **Lumen** | Micro (Laravel) | Microservizi veloci |
| **TortaPHP** | Stack completo | Sviluppo rapido |
| **CodiceIgniter** | Leggero | App semplici |
| **Ehi** | Stack completo | Incentrato sulle prestazioni |
| **Spirale** | Moderno | Di lunga durata, Swoole |
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

## Database e ORM
| Tecnologia | Digitare |
|------------|------|
| **Eloquente** | ORM (record attivo) di Laravel |
| **Dottrina** | ORM (Data Mapper) di Symfony |
| **Generatore di query** | Generatore SQL fluente |
| **DOP** | Accesso al database di basso livello |
| **Migrazione Laravel** | Gestione dello schema |
| **Finge** | Migrazioni autonome |
| **Volo** | Migrazioni del database |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **PHPUnit** | Quadro di prova standard |
| **Peste** | Test eleganti (basati su PHPUnit) |
| **Laravel Crepuscolo** | Test del browser |
| **Scherza** | Quadro beffardo |
| **Infezione** | Test di mutazione |
| **PHPStan** | Analisi statica (rileva anche bug) |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **PHPStan** | Analisi statica (livelli 0-9) |
| **Salmo** | Analisi statica (alternativa) |
| **Pinta Laravel** | Stile codice (Laravel) |
| **Fissatore PHP-CS** | Stile del codice (generale) |
| **PHPMD** | Rilevamento disordine |
| **PHP_CodeSniffer** | Annusare e stile |
| **Rettore** | Refactoring automatizzato |
| **Deptrac** | Analisi delle dipendenze |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Motori modello
| Motore | Note |
|--------|-------|
| **Lama** | Motore di modelli di Laravel |
| **Ramoscello** | Il motore dei template di Symfony |
| **Latte** | Motore di modelli sicuro di Nette |
| **Piatti** | Modelli PHP nativi |
---

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **Guzzle** | Client HTTP |
| **Symfony HttpClient** | Client HTTP |
| **Carbonio** | Libreria data/ora |
| **Console Symfony** | Quadro CLI |
| **Monologo** | Registrazione |
| **Coda Laravel** | Lavori in background |
| **Cassa Laravel** | Fatturazione a strisce |
| **Laravel Socialista** | Autenticazione OAuth |
| **Laravel Sanctum** | Autenticazione API |
| **Laravel Orizzonte** | Dashboard della coda Redis |
| **Livewire** | Interfaccia utente dinamica senza JS |
| **Inertia.js** | Adattatore SPA (Vue/React + Laravel) |
| **Pacchetti Spazio** | Utilità di alta qualità |
| **Pacchetti campionato** | Biblioteche comunitarie |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **PhpStorm** | Miglior IDE PHP (JetBrains) |
| **Codice VS + Intelephense PHP** | Leggero, basato su LSP |
| **Neovim + phpactor** | Basato su terminale |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **PHP-FPM + Nginx** | Impostazione di produzione classica |
| **Apache + mod_php** | Tradizionale |
| **Docker** | Containerizzato (php:fpm-alpine) |
| **Laravel Forge** | Gestione server |
| **Laravel Vapor** | Distribuzione di AWS Lambda |
| **Inviato** | Distribuzione senza tempi di inattività |
| **Hosting condiviso** | cPanel, Plesk |
| **RoadRunner / Swoole** | PHP di lunga durata |
| **FrankenPHP** | Server di app moderno |
---

## Riepilogo
L'ecosistema PHP è dominato da **Laravel** (elegante, adatto agli sviluppatori) e **Symfony** (enterprise, componenti). Lo stack standard è: **Composer** per i pacchetti, **Laravel** o **Symfony** per il web, **PHPUnit** o **Pest** per i test, **PHPStan** per l'analisi statica, **Laravel Pint** o **PHP-CS-Fixer** per la formattazione e **PHP-FPM** o **RoadRunner** per la pubblicazione. Il moderno PHP 8.3+ con enumerazioni, fibre, classi di sola lettura e tipi di unione è un linguaggio molto più capace di quanto suggerisca la sua reputazione. L'ecosistema eccelle nello sviluppo web, nella gestione dei contenuti (WordPress, Drupal) e nell'e-commerce (Magento, WooCommerce).