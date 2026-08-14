---
# Metadata
title: "PHP — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the PHP ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# PHP: Guía de ecosistemas y herramientas
Esta guía cubre las herramientas, marcos e infraestructura esenciales en el ecosistema PHP.
---

## Tiempos de ejecución de PHP
| Tiempo de ejecución | Notas |
|---------|-------|
| **PHP-FPM** | FastCGI Process Manager (más común) |
| **CLI** | Interfaz de línea de comandos |
| **Lana** | Asíncrono, basado en corrutinas |
| **Correcaminos** | Alto rendimiento (basado en Go) |
| **FrankenPHP** | Servidor de aplicaciones PHP moderno (Go) |
| **PHP 8.3+** | Estable actual con enumeraciones, fibras, solo lectura |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **Compositor** | Gestor de dependencias (el estándar) |
| **Empaquetador** | Repositorio de paquetes predeterminado |
| **Empaquetador privado** | Alojamiento de paquetes privados |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Laravel** | Pila completa | API más popular y elegante |
| **Symfony** | Pila completa | Empresa, componentes |
| **Delgado** | micro | API, pequeñas aplicaciones |
| **Lúmenes** | Micro (Laravel) | Microservicios rápidos |
| **PastelPHP** | Pila completa | Desarrollo rápido |
| **CodeIgniter** | Ligero | Aplicaciones sencillas |
| **Sí** | Pila completa | Centrado en el rendimiento |
| **Espiral** | Moderno | De larga duración, Swoole |
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

## Base de datos y ORM
| Tecnología | Tipo |
|------------|------|
| **Elocuente** | ORM (Registro activo) de Laravel |
| **Doctrina** | ORM (Mapeador de datos) de Symfony |
| **Creador de consultas** | Constructor de SQL fluido |
| **DOP** | Acceso a bases de datos de bajo nivel |
| **Migración de Laravel** | Gestión de esquemas |
| **Finge** | Migraciones independientes |
| **Ruta migratoria** | Migraciones de bases de datos |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **Unidad PHP** | Marco de prueba estándar |
| **Plagas** | Pruebas elegantes (basadas en PHPUnit) |
| **Anochecer de Laravel** | Pruebas del navegador |
| **Burla** | Marco burlón |
| **Infección** | Pruebas de mutación |
| **PHPStan** | Análisis estático (también detecta errores) |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **PHPStan** | Análisis estático (niveles 0-9) |
| **Salmo** | Análisis estático (alternativo) |
| **Pinta Laravel** | Estilo de código (Laravel) |
| **Reparador de PHP-CS** | Estilo de código (general) |
| **PHPMD** | Detección de desorden |
| **PHP_CodeSniffer** | Olfateo y estilo |
| **Rector** | Refactorización automatizada |
| **Deptrac** | Análisis de dependencia |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Motores de plantillas
| Motor | Notas |
|--------|-------|
| **Hoja** | Motor de plantillas de Laravel |
| **Ramita** | Motor de plantillas de Symfony |
| **Café con leche** | El motor de plantillas seguro de Nette |
| **Platos** | Plantillas PHP nativas |
---

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **Beber** | Cliente HTTP |
| **Cliente HTTP de Symfony** | Cliente HTTP |
| **Carbono** | Biblioteca de fecha/hora |
| **Consola Symfony** | Marco CLI |
| **Monólogo** | Registro |
| **Cola de Laravel** | Trabajos en segundo plano |
| **Cajero Laravel** | Facturación por franjas |
| **Laravel socialité** | Autenticación OAuth |
| **Santuario de Laravel** | Autenticación API |
| **Horizonte Laravel** | Panel de cola de Redis |
| **Cableado vivo** | UI dinámica sin JS |
| **Inercia.js** | Adaptador SPA (Vue/React + Laravel) |
| **Paquetes espaciales** | Servicios públicos de alta calidad |
| **Paquetes de liga** | Bibliotecas comunitarias |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **PhpStorm** | Mejor IDE de PHP (JetBrains) |
| **Código VS + PHP Intelephense** | Ligero, basado en LSP |
| **Neovim + phpactor** | Basado en terminal |
---

## Implementación
| Método | Notas |
|--------|-------|
| **PHP-FPM + Nginx** | Configuración de producción clásica |
| **Apache + mod_php** | Tradicional |
| **Acoplador** | En contenedores (php:fpm-alpine) |
| **Forja Laravel** | Gestión de servidores |
| **Vapor Laravel** | Implementación de AWS Lambda |
| **Enviador** | Implementación sin tiempo de inactividad |
| **Hospedaje compartido** | cPanel, Plesk |
| **Correcaminos / Swoole** | PHP de larga duración |
| **FrankenPHP** | Servidor de aplicaciones moderno |
---

## Resumen
El ecosistema de PHP está dominado por **Laravel** (elegante, fácil de desarrollar) y **Symfony** (empresa, componentes). La pila estándar es: **Composer** para paquetes, **Laravel** o **Symfony** para web, **PHPUnit** o **Pest** para pruebas, **PHPStan** para análisis estático, **Laravel Pint** o **PHP-CS-Fixer** para formatear y **PHP-FPM** o **RoadRunner** para servir. El PHP 8.3+ moderno con enumeraciones, fibras, clases de solo lectura y tipos de unión es un lenguaje mucho más capaz de lo que sugiere su reputación. El ecosistema destaca en desarrollo web, gestión de contenidos (WordPress, Drupal) y comercio electrónico (Magento, WooCommerce).