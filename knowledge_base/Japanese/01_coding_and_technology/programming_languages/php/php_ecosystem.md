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
# PHP — エコシステムとツールのガイド
このガイドでは、PHP エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## PHP ランタイム
|ランタイム |メモ |
|----------|----------|
| **PHP-FPM** | FastCGI プロセス マネージャー (最も一般的) |
| **CLI** |コマンドラインインターフェース |
| **スウール** |非同期、コルーチンベース |
| **ロードランナー** |高性能 (Go ベース) |
| **フランケンPHP** |最新の PHP アプリ サーバー (Go) |
| **PHP 8.3+** |現在は列挙型、ファイバー、読み取り専用で安定しています。
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## パッケージ管理
|ツール |目的 |
|-----|----------|
| **作曲家** |依存関係マネージャー (標準) |
| **パッケージニスト** |デフォルトのパッケージリポジトリ |
| **プライベートパッケージニスト** |プライベートパッケージホスティング |
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

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **Laravel** |フルスタック |最も人気のあるエレガントな API |
| **シンフォニー** |フルスタック |エンタープライズ、コンポーネント |
| **スリム** |マイクロ | API、小規模アプリ |
| **ルーメン** |マイクロ (Laravel) |高速マイクロサービス |
| **CakePHP** |フルスタック |急速な開発 |
| **CodeIgniter** |軽量 |シンプルなアプリ |
| **Yii** |フルスタック |パフォーマンス重視 |
| **スパイラル** |モダン |ロングラン、Swoole |
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

## データベースと ORM
|テクノロジー |タイプ |
|-----------|------|
| **雄弁** | LaravelのORM（アクティブレコード） |
| **教義** | Symfony の ORM (データ マッパー) |
| **クエリ ビルダー** |流暢な SQL ビルダー |
| **PDO** |低レベルのデータベース アクセス |
| **Laravel の移行** |スキーマ管理 |
| **フィンクス** |スタンドアロンの移行 |
| **フライウェイ** |データベースの移行 |
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

## テスト
|フレームワーク |目的 |
|----------|----------|
| **PHPUnit** |標準テストフレームワーク |
| **害虫** |エレガントなテスト (PHPUnit 上に構築) |
| **Laravel Dusk** |ブラウザのテスト |
| **嘲笑** |モックフレームワーク |
| **感染** |突然変異テスト |
| **PHPStan** |静的解析 (バグもキャッチ) |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **PHPStan** |静的解析 (レベル 0 ～ 9) |
| **詩篇** |静的解析 (代替) |
| **Laravel パイント** |コードスタイル（Laravel） |
| **PHP-CS-Fixer** |コードスタイル (一般) |
| **PHPMD** |混乱の検出 |
| **PHP_CodeSniffer** |スニッフィングとスタイル |
| **学長** |自動化されたリファクタリング |
| **デプトラック** |依存関係の分析 |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## テンプレート エンジン
|エンジン |メモ |
|------|------|
| **ブレード** | Laravelのテンプレートエンジン |
| **小枝** | Symfony のテンプレート エンジン |
| **ラテ** | Nette の安全なテンプレート エンジン |
| **プレート** |ネイティブ PHP テンプレート |
---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **ガズル** | HTTPクライアント |
| **Symfony HttpClient** | HTTPクライアント |
| **カーボン** |日付/時刻ライブラリ |
| **Symfony コンソール** | CLI フレームワーク |
| **モノローグ** |ロギング |
| **Laravel キュー** |バックグラウンドジョブ |
| **Laravel レジ係** |ストライプ請求 |
| **Laravel 社交家** | OAuth認証 |
| **Laravel サンクタム** | API認証 |
| **Laravel Horizo​​n** | Redis キュー ダッシュボード |
| **ライブワイヤー** | JS を使用しない動的 UI |
| **Inertia.js** | SPA アダプター (Vue/React + Laravel) |
| **スパティー パッケージ** |高品質のユーティリティ |
| **リーグパッケージ** |コミュニティ図書館 |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **PhpStorm** |ベスト PHP IDE (JetBrains) |
| **VS コード + PHP Intelephense** |軽量、LSP ベース |
| **Neovim + phpactor** |ターミナルベース |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **PHP-FPM + Nginx** |クラシックなプロダクションセットアップ |
| **Apache + mod_php** |伝統的な |
| **ドッカー** |コンテナ化 (php:fpm-alpine) |
| **Laravel Forge** |サーバー管理 |
| **Laravel Vapor** | AWS Lambda のデプロイメント |
| **使者** |ダウンタイムゼロの展開 |
| **共有ホスティング** | cPanel、Plesk |
| **ロードランナー / スウール** |長期にわたって実行される PHP |
| **フランケンPHP** |最新のアプリサーバー |
---

＃＃ まとめ
PHP のエコシステムは、**Laravel** (エレガントで開発者に優しい) と **Symfony** (エンタープライズ、コンポーネント) によって支配されています。標準スタックは次のとおりです。パッケージの場合は **Composer**、Web の場合は **Laravel** または **Symfony**、テストの場合は **PHPUnit** または **Pest**、静的分析の場合は **PHPStan**、フォーマットの場合は **Laravel Pint** または **PHP-CS-Fixer**、サービスの場合は **PHP-FPM** または **RoadRunner** です。列挙型、ファイバー、読み取り専用クラス、共用体型を備えた最新の PHP 8.3 以降は、その評判が示すよりもはるかに高性能な言語です。このエコシステムは、Web 開発、コンテンツ管理 (WordPress、Drupal)、および電子商取引 (Magento、WooCommerce) に優れています。