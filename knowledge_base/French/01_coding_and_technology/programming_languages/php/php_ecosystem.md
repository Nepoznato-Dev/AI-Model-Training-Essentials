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
# PHP — Guide de l'écosystème et des outils
Ce guide couvre les outils, frameworks et infrastructures essentiels de l'écosystème PHP.
---

## Exécutions PHP
| Durée d'exécution | Remarques |
|---------|-------|
| **PHP-FPM** | Gestionnaire de processus FastCGI (le plus courant) |
| **CLI** | Interface de ligne de commande |
| **Swoole** | Asynchrone, basé sur une coroutine |
| **RoadRunner** | Haute performance (basé sur Go) |
| **FrankenPHP** | Serveur d'application PHP moderne (Go) |
| **PHP8.3+** | Actuel stable avec énumérations, fibres, lecture seule |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Gestion des paquets
| Outil | Objectif |
|------|--------------|
| **Compositeur** | Gestionnaire de dépendances (le standard) |
| **Packagiste** | Dépôt de packages par défaut |
| **Emballeur privé** | Hébergement de forfaits privés |
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

## Cadres Web
| Cadre | Tapez | Idéal pour |
|---------------|------|--------------|
| **Laravel** | Pile complète | API la plus populaire et la plus élégante |
| **Symfony** | Pile complète | Entreprise, composants |
| **Mince** | Micro | API, petites applications |
| **Lumène** | Micro (Laravel) | Micro-services rapides |
| **GâteauPHP** | Pile complète | Développement rapide |
| **CodeIgniter** | Léger | Applications simples |
| **Oui** | Pile complète | Axé sur la performance |
| **Spirale** | Moderne | De longue durée, Swoole |
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

## Base de données et ORM
| Technologie | Tapez |
|------------|------|
| **Éloquent** | ORM de Laravel (enregistrement actif) |
| **Doctrine** | ORM (Data Mapper) de Symfony |
| **Générateur de requêtes** | Générateur SQL courant |
| **AOP** | Accès à la base de données de bas niveau |
| **Migration Laravel** | Gestion de schéma |
| **Phinx** | Migrations autonomes |
| **Voie de migration** | Migrations de bases de données |
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

## Tests
| Cadre | Objectif |
|-----------|---------|
| **PHPUnit** | Cadre de test standard |
| **Ravageur** | Tests élégants (construits sur PHPUnit) |
| **Laravel Crépuscule** | Test du navigateur |
| **Moquerie** | Cadre moqueur |
| **Infection** | Tests de mutations |
| **PHPStan** | Analyse statique (détecte également les bugs) |
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

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **PHPStan** | Analyse statique (niveaux 0 à 9) |
| **Psaume** | Analyse statique (alternative) |
| **Pinte Laravel** | Style de code (Laravel) |
| **PHP-CS-Fixeur** | Style de code (général) |
| **PHPMD** | Détection des dégâts |
| **PHP_CodeSniffer** | Renifler et style |
| **Recteur** | Refactorisation automatisée |
| **Deptrac** | Analyse des dépendances |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Moteurs de modèles
| Moteur | Remarques |
|--------|-------|
| **Lame** | Le moteur de modèles de Laravel |
| **Brindille** | Le moteur de templates de Symfony |
| **Café** | Le moteur de modèles sécurisé de Nette |
| **Plaques** | Modèles PHP natifs |
---

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **Engloutir** | Client HTTP |
| **Client HTTPS Symfony** | Client HTTP |
| **Carbone** | Bibliothèque date/heure |
| **Console Symfony** | Cadre CLI |
| **Monologue** | Journalisation |
| **File d'attente Laravel** | Emplois en arrière-plan |
| **Caissier Laravel** | Facturation Stripe |
| **Laravel Socialite** | Authentification OAuth |
| **Sanctuaire de Laravel** | Authentification API |
| **Laravel Horizon** | Tableau de bord de la file d'attente Redis |
| **Livewire** | Interface utilisateur dynamique sans JS |
| **Inertie.js** | Adaptateur SPA (Vue/React + Laravel) |
| **Forfaits Spatie** | Utilitaires de haute qualité |
| **Forfaits Ligue** | Bibliothèques communautaires |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **PhpStorm** | Meilleur EDI PHP (JetBrains) |
| **VS Code + PHP Intelephense** | Léger, basé sur LSP |
| **Neovim + phpacteur** | Basé sur un terminal |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **PHP-FPM + Nginx** | Configuration de production classique |
| **Apache + mod_php** | Traditionnel |
| **Docker** | Conteneurisé (php:fpm-alpine) |
| **Forge Laravel** | Gestion de serveur |
| **Laravel Vapeur** | Déploiement AWS Lambda |
| **Envoyé** | Déploiement sans temps d'arrêt |
| **Hébergement partagé** | cPanel, Plesk |
| **RoadRunner / Swoole** | PHP de longue durée |
| **FrankenPHP** | Serveur d'applications moderne |
---

## Résumé
L'écosystème PHP est dominé par **Laravel** (élégant, convivial pour les développeurs) et **Symfony** (entreprise, composants). La pile standard est : **Composer** pour les packages, **Laravel** ou **Symfony** pour le Web, **PHPUnit** ou **Pest** pour les tests, **PHPStan** pour l'analyse statique, **Laravel Pint** ou **PHP-CS-Fixer** pour le formatage et **PHP-FPM** ou **RoadRunner** pour le service. Le PHP 8.3+ moderne avec des énumérations, des fibres, des classes en lecture seule et des types d'union est un langage beaucoup plus performant que sa réputation ne le suggère. L'écosystème excelle dans le développement Web, la gestion de contenu (WordPress, Drupal) et le commerce électronique (Magento, WooCommerce).