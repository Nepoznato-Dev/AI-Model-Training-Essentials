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

# PHP — 生态系统和工具指南
本指南涵盖了 PHP 生态系统中的基本工具、框架和基础设施。
---

## PHP 运行时
|运行时 |笔记|
|--------|--------|
| **PHP-FPM** | FastCGI 进程管理器（最常见）|
| **命令行** |命令行界面 |
| **Swoole** |异步、基于协程 |
| **走鹃** |高性能（基于 Go）|
| **FrankenPHP** |现代 PHP 应用服务器 (Go) |
| **PHP 8.3+** |当前稳定的枚举、纤维、只读 |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## 包管理
|工具|目的|
|------|---------|
| **作曲家** |依赖管理器（标准）|
| **Packagist** |默认包存储库 |
| **私人包装师** |私人包托管|
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

## 网络框架
|框架|类型 |最适合 |
|------------|------|----------|
| **Laravel** |全栈|最流行、最优雅的API |
| **交响乐** |全栈|企业、组件|
| **苗条** |微| API、小型应用程序 |
| **流明** |微（Laravel）|快速微服务|
| **CakePHP** |全栈|快速发展 |
| **代码点火器** |轻量化|简单的应用程序 |
| **Yii** |全栈|注重绩效 |
| **螺旋** |现代|长期运行，Swoole |
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

## 数据库和 ORM
|技术 |类型 |
|------------|------|
| **雄辩** | Laravel 的 ORM（活动记录）|
| **学说** | Symfony 的 ORM（数据映射器）|
| **查询生成器** |流畅的 SQL 构建器 |
| **PDO** |低级数据库访问 |
| **Laravel 迁移** |模式管理|
| **芬克斯** |独立迁移 |
| **飞行路线** |数据库迁移 |
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

## 测试
|框架|目的|
|------------|---------|
| **PHPUnit** |标准测试框架 |
| **害虫** |优雅的测试（基于 PHPUnit 构建）|
| **Laravel 黄昏** |浏览器测试 |
| **嘲讽** |模拟框架 |
| **感染** |突变测试|
| **PHPStan** |静态分析（也捕获错误）|
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

## 代码质量
|工具|目的|
|------|---------|
| **PHPStan** |静态分析（0-9 级）|
| **诗篇** |静态分析（替代）|
| **拉拉维尔品脱** |代码风格 (Laravel) |
| **PHP-CS-修复程序** |代码风格（通用）|
| **PHPMD** |脏乱检测|
| **PHP_CodeSniffer** |嗅觉与风格 |
| **校长** |自动化重构 |
| **德普特拉克** |依赖性分析 |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## 模板引擎
|发动机|笔记|
|--------|--------|
| **刀片** | Laravel 的模板引擎 |
| **树枝** | Symfony 的模板引擎 |
| **拿铁** | Nette 的安全模板引擎 |
| **板材** |原生 PHP 模板 |
---

## 关键库
|图书馆 |目的|
|---------|---------|
| **狂饮** | HTTP 客户端 |
| **Symfony HttpClient** | HTTP 客户端 |
| **碳** |日期/时间库 |
| **Symfony 控制台** | CLI 框架 |
| **独白** |记录 |
| **Laravel 队列** |后台工作 |
| **Laravel 收银员** |条纹计费|
| **Laravel 社交名流** | OAuth 身份验证 |
| **Laravel 圣所** | API认证|
| **Laravel 地平线** | Redis 队列仪表板 |
| **Livewire** |无需JS的动态UI |
| **Inertia.js** | SPA 适配器（Vue/React + Laravel）|
| **Spatie 包** |高品质公用事业|
| **联赛套餐** |社区图书馆|
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **PhpStorm** |最佳 PHP IDE (JetBrains) |
| **VS Code + PHP Intelephense** |轻量级、基于LSP |
| **Neovim + phpactor** |基于终端 |
---

## 部署
|方法|笔记|
|--------|--------|
| **PHP-FPM + Nginx** |经典制作设置 |
| **Apache + mod_php** |传统|
| **码头工人** |容器化 (php:fpm-alpine) |
| **Laravel Forge** |服务器管理 |
| **Laravel Vapor** | AWS Lambda 部署 |
| **特使** |零停机部署|
| **共享主机** | cPanel、Plesk |
| **RoadRunner / Swoole** |长时间运行的 PHP |
| **FrankenPHP** |现代应用服务器 |
---

＃＃ 概括
PHP 的生态系统由 **Laravel**（优雅、开发人员友好）和 **Symfony**（企业、组件）主导。标准堆栈是：用于包的 **Composer**，用于 Web 的 **Laravel** 或 **Symfony**，用于测试的 **PHPUnit** 或 **Pest**，用于静态分析的 **PHPStan**，用于格式化的 **Laravel Pint** 或 **PHP-CS-Fixer**，以及用于服务的 **PHP-FPM** 或 **RoadRunner**。现代 PHP 8.3+ 具有枚举、纤程、只读类和联合类型，是一种比其声誉所暗示的更强大的语言。该生态系统擅长 Web 开发、内容管理（WordPress、Drupal）和电子商务（Magento、WooCommerce）。