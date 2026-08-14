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
# PHP — 生態系與工具指南
本指南涵蓋了 PHP 生態系統中的基本工具、框架和基礎設施。
---

## PHP 運行時
|運行時 |筆記|
|--------|--------|
| **PHP-FPM** | FastCGI 進程管理器（最常見）|
| **命令列** |命令列介面 |
| **Swoole** |非同步、基於協程 |
| **走鵑** |高性能（基於 Go）|
| **FrankenPHP** |現代 PHP 應用伺服器 (Go) |
| **PHP 8.3+** |目前穩定的枚舉、纖維、唯讀 |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## 套件管理
|工具|目的|
|------|---------|
| **作曲家** |依賴管理器（標準）|
| **Packagist** |預設包存儲庫 |
| **私人包裝師** |私人包託管|
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **Laravel** |全端|最受歡迎、最優雅的API |
| **交響樂** |全端|企業、組件|
| **苗條** |微| API、小型應用程式 |
| **流明** |微（Laravel）|快速微服務|
| **CakePHP** |全端|快速發展 |
| **代碼點火器** |輕量化|簡單的應用程式 |
| **Yii** |全端|注重績效 |
| **螺旋** |現代|長期運行，Swoole |
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

## 資料庫和 ORM
|技術 |類型 |
|------------|------|
| **雄辯** | Laravel 的 ORM（活動記錄）|
| **學說** | Symfony 的 ORM（資料映射器）|
| **查詢產生器** |流暢的 SQL 建構器 |
| **PDO** |低階資料庫存取 |
| **Laravel 遷移** |模式管理|
| **芬克斯** |獨立遷移 |
| **飛行路線** |資料庫遷移 |
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

## 測試
|框架|目的|
|------------|---------|
| **PHPUnit** |標準測試框架 |
| **害蟲** |優雅的測試（基於 PHPUnit 建置）|
| **Laravel 黃昏** |瀏覽器測試 |
| **嘲諷** |模擬框架 |
| **感染** |突變測試|
| **PHPStan** |靜態分析（也捕獲錯誤）|
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

## 程式碼品質
|工具|目的|
|------|---------|
| **PHPStan** |靜態分析（0-9 級）|
| **詩篇** |靜態分析（替代）|
| **拉拉維爾品脫** |代碼風格 (Laravel) |
| **PHP-CS-修復程式** |程式碼樣式（通用）|
| **PHPMD** |髒亂偵測|
| **PHP_CodeSniffer** |嗅覺與風格 |
| **校長** |自動化重構 |
| **德普特拉克** |依賴性分析 |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## 模板引擎
|引擎|筆記|
|--------|--------|
| **刀片** | Laravel 的模板引擎 |
| **樹枝** | Symfony 的模板引擎 |
| **拿鐵** | Nette 的安全模板引擎 |
| **板材** |原生 PHP 模板 |
---

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **狂飲** | HTTP 用戶端 |
| **Symfony HttpClient** | HTTP 用戶端 |
| **碳** |日期/時間庫 |
| **Symfony 控制台** | CLI 框架 |
| **獨白** |記錄 |
| **Laravel 佇列** |後台工作 |
| **Laravel 收銀員** |條紋計費|
| **Laravel 社群名流** | OAuth 驗證 |
| **Laravel 聖所** | API認證|
| **Laravel 地平線** | Redis 佇列儀表板 |
| **Livewire** |無需JS的動態UI |
| **Inertia.js** | SPA 適配器（Vue/React + Laravel）|
| **Spatie 包** |高品質公用事業|
| **聯賽套餐** |社區圖書館|
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **PhpStorm** |最佳 PHP IDE (JetBrains) |
| **VS Code + PHP Intelephense** |輕量級、基於LSP |
| **Neovim + phpactor** |基於終端機 |
---

## 部署
|方法|筆記|
|--------|--------|
| **PHP-FPM + Nginx** |經典製作設定 |
| **Apache + mod_php** |傳統|
| **碼頭工人** |容器化 (php:fpm-alpine) |
| **Laravel Forge** |伺服器管理 |
| **Laravel Vapor** | AWS Lambda 部署 |
| **特使** |零停機部署|
| **共享主機** | cPanel、Plesk |
| **RoadRunner / Swoole** |長時間運行的 PHP |
| **FrankenPHP** |現代應用伺服器 |
---

＃＃ 概括
PHP 的生態系統由 **Laravel**（優雅、開發人員友好）和 **Symfony**（企業、組件）主導。標準堆疊是：用於套件的 **Composer**，用於 Web 的 **Laravel** 或 **Symfony**，用於測試的 **PHPUnit** 或 **Pest**，用於靜態分析的 **PHPStan**，用於格式化的 **Laravel Pint** 或 **PHP-CS-Fixer**，以及用於服務的 **PHPFPRM**。現代 PHP 8.3+ 具有枚舉、纖程、唯讀類和聯合類型，是一種比其聲譽所暗示的更強大的語言。此生態系統擅長 Web 開發、內容管理（WordPress、Drupal）和電子商務（Magento、WooCommerce）。