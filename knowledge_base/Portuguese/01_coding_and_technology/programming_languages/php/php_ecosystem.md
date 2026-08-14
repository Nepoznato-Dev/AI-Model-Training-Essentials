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
# PHP – Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema PHP.
---

## Tempos de execução PHP
| Tempo de execução | Notas |
|--------|-------|
| **PHP-FPM** | FastCGI Process Manager (mais comum) |
| **CLI** | Interface de linha de comando |
| **Swoole** | Assíncrono, baseado em corrotina |
| **RoadRunner** | Alto desempenho (baseado em Go) |
| **FrankenPHP** | Servidor de aplicativos PHP moderno (Go) |
| **PHP 8.3+** | Atual estável com enums, fibras, somente leitura |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **Compositor** | Gerenciador de dependências (o padrão) |
| **Embalador** | Repositório de pacotes padrão |
| **Embalador Privado** | Hospedagem de pacotes privados |
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

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **Laravel** | Pilha completa | API elegante e mais popular |
| **Symfony** | Pilha completa | Empresa, componentes |
| **Fino** | Micro | APIs, pequenos aplicativos |
| **Lúmen** | Micro (Laravel) | Microsserviços rápidos |
| **BoloPHP** | Pilha completa | Desenvolvimento rápido |
| **CodeIgniter** | Leve | Aplicativos simples |
| **Sim** | Pilha completa | Focado no desempenho |
| **Espiral** | Moderno | Longa duração, Swoole |
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

## Banco de dados e ORM
| Tecnologia | Tipo |
|------------|------|
| **Eloquente** | ORM (registro ativo) do Laravel |
| **Doutrina** | ORM (Mapeador de Dados) do Symfony |
| **Construtor de consultas** | Construtor SQL fluente |
| **DOP** | Acesso ao banco de dados de baixo nível |
| **Migração para Laravel** | Gerenciamento de esquema |
| **Finge** | Migrações autônomas |
| **Via aérea** | Migrações de banco de dados |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **PHPUnit** | Estrutura de teste padrão |
| **Praga** | Teste elegante (construído em PHPUnit) |
| **Crepúsculo do Laravel** | Teste de navegador |
| **Zombaria** | Estrutura de simulação |
| **Infecção** | Teste de mutação |
| **PHPStan** | Análise estática (também detecta bugs) |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **PHPStan** | Análise estática (níveis 0-9) |
| **Salmo** | Análise estática (alternativa) |
| **Laravel Pinta** | Estilo de código (Laravel) |
| **PHP-CS-Fixer** | Estilo de código (geral) |
| **PHPMD** | Detecção de bagunça |
| **PHP_CodeSniffer** | Cheirando e estilo |
| **Reitor** | Refatoração automatizada |
| **Deptrac** | Análise de dependência |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Mecanismos de modelo
| Motor | Notas |
|-------|-------|
| **Lâmina** | Motor de template do Laravel |
| **Galho** | Mecanismo de template do Symfony |
| ** Café com leite ** | Motor de modelo seguro de Nette |
| **Placas** | Modelos PHP nativos |
---

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **Guzzle** | Cliente HTTP |
| **Symfony HttpClient** | Cliente HTTP |
| **Carbono** | Biblioteca de data/hora |
| **Console Symfony** | Estrutura CLI |
| **Monólogo** | Registro |
| **Fila do Laravel** | Trabalhos em segundo plano |
| **Caixa Laravel** | Faturamento de faixa |
| **Socialite Laravel** | Autenticação OAuth |
| **Laravel Santuário** | Autenticação de API |
| **Horizonte Laravel** | Painel de fila do Redis |
| **Livewire** | UI dinâmica sem JS |
| **Inércia.js** | Adaptador SPA (Vue/React + Laravel) |
| **Pacotes espaciais** | Utilitários de alta qualidade |
| **Pacotes da Liga** | Bibliotecas comunitárias |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **PhpStorm** | Melhor IDE PHP (JetBrains) |
| **Código VS + PHP Intelephense** | Leve, baseado em LSP |
| **Neovim + phpactor** | Baseado em terminal |
---

## Implantação
| Método | Notas |
|-------|-------|
| **PHP-FPM + Nginx** | Configuração de produção clássica |
| **Apache + mod_php** | Tradicional |
| **Docker** | Contentorizado (php:fpm-alpine) |
| **LaravelForja** | Gerenciamento de servidores |
| **Vapor Laravel** | Implantação do AWS Lambda |
| **Enviado** | Implantação com tempo de inatividade zero |
| **Hospedagem compartilhada** | cPanel, Plesk |
| **RoadRunner/Swoole** | PHP de longa duração |
| **FrankenPHP** | Servidor de aplicativos moderno |
---

## Resumo
O ecossistema do PHP é dominado pelo **Laravel** (elegante e amigável ao desenvolvedor) e pelo **Symfony** (corporativo, componentes). A pilha padrão é: **Composer** para pacotes, **Laravel** ou **Symfony** para web, **PHPUnit** ou **Pest** para testes, **PHPStan** para análise estática, **Laravel Pint** ou **PHP-CS-Fixer** para formatação e **PHP-FPM** ou **RoadRunner** para servir. O PHP 8.3+ moderno com enums, fibras, classes somente leitura e tipos de união é uma linguagem muito mais capaz do que sua reputação sugere. O ecossistema é excelente em desenvolvimento web, gerenciamento de conteúdo (WordPress, Drupal) e comércio eletrônico (Magento, WooCommerce).