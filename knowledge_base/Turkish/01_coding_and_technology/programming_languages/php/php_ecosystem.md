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
# PHP — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz PHP ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## PHP Çalışma Zamanları
| Çalışma zamanı | Notlar |
|-----------|----------|
| **PHP-FPM** | FastCGI Süreç Yöneticisi (en yaygın) |
| **CLI** | Komut satırı arayüzü |
| **Swoole** | Zaman uyumsuz, eşyordam tabanlı |
| **RoadRunner** | Yüksek performanslı (Go tabanlı) |
| **FrankenPHP** | Modern PHP uygulama sunucusu (Go) |
| **PHP 8.3+** | Numaralandırmalar, fiberler, salt okunur ile mevcut kararlı |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **Besteci** | Bağımlılık yöneticisi (standart) |
| **Paketleme Uzmanı** | Varsayılan paket deposu |
| **Özel Paketleme Uzmanı** | Özel paket barındırma |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Laravel** | Tam yığın | En popüler, zarif API |
| **Symfony** | Tam yığın | Şirket, bileşenler |
| **İnce** | Mikro | API'ler, küçük uygulamalar |
| **Lümen** | Mikro (Laravel) | Hızlı mikro hizmetler |
| **KekPHP** | Tam yığın | Hızlı gelişme |
| **CodeIgniter** | Hafif | Basit uygulamalar |
| **Yii** | Tam yığın | Performans odaklı |
| **Sarmal** | Modern | Uzun süredir devam eden, Swoole |
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

## Veritabanı ve ORM
| Teknoloji | Tür |
|---------------|------|
| **Belagatli** | Laravel'in ORM'si (Aktif Kayıt) |
| **Doktrin** | Symfony'nin ORM'si (Veri Eşleyici) |
| **Sorgu Oluşturucu** | Akıcı SQL oluşturucu |
| **PDO** | Düşük seviyeli veritabanı erişimi |
| **Laravel Geçişi** | Şema yönetimi |
| **Phinx** | Bağımsız geçişler |
| **Geçiş yolu** | Veritabanı geçişleri |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **PHPUnit** | Standart test çerçevesi |
| **Haşere** | Zarif testler (PHPUnit üzerinde oluşturulmuştur) |
| **Laravel Alacakaranlık** | Tarayıcı testi |
| **alaycılık** | Alaycı çerçeve |
| **Enfeksiyon** | Mutasyon testi |
| **PHPStan** | Statik analiz (aynı zamanda hataları da yakalar) |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **PHPStan** | Statik analiz (0-9. düzeyler) |
| **Mezmur** | Statik analiz (alternatif) |
| **Laravel Bira bardağı** | Kod stili (Laravel) |
| **PHP-CS-Fixer** | Kod stili (genel) |
| **PHPMD** | Karışıklık tespiti |
| **PHP_CodeSniffer** | Koklama ve stil |
| **Rektör** | Otomatik yeniden düzenleme |
| **Deptrac** | Bağımlılık analizi |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Şablon Motorları
| Motor | Notlar |
|----------|----------|
| **Bıçak** | Laravel'in şablon motoru |
| **dal** | Symfony'nin şablon motoru |
| **Latte** | Nette'nin güvenli şablon motoru |
| **Tabaklar** | Yerel PHP şablonları |
---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **Gözleme** | HTTP istemcisi |
| **Symfony HttpClient** | HTTP istemcisi |
| **Karbon** | Tarih/saat kitaplığı |
| **Symfony Konsolu** | CLI çerçevesi |
| **Monolog** | Günlük |
| **Laravel Kuyruğu** | Arka plan işleri |
| **Laravel Kasiyer** | Şerit faturalandırma |
| **Laravel Sosyetesi** | OAuth kimlik doğrulaması |
| **Laravel Kutsal Alanı** | API kimlik doğrulaması |
| **Laravel Horizon** | Redis kuyruğu kontrol paneli |
| **Canlı kablolu** | JS'siz Dinamik Kullanıcı Arayüzü |
| **Atalet.js** | SPA bağdaştırıcısı (Vue/React + Laravel) |
| **Spatie paketleri** | Yüksek kaliteli yardımcı programlar |
| **Lig paketleri** | Topluluk kütüphaneleri |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **PhpStorm** | En İyi PHP IDE (JetBrains) |
| **VS Kodu + PHP Intelephense** | Hafif, LSP tabanlı |
| **Neovim + phpactor** | Terminal tabanlı |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **PHP-FPM + Nginx** | Klasik üretim kurulumu |
| **Apache + mod_php** | Geleneksel |
| **Docker** | Konteynerleştirilmiş (php:fpm-alpine) |
| **Laravel Forge** | Sunucu yönetimi |
| **Laravel Buharı** | AWS Lambda dağıtımı |
| **Elçi** | Sıfır kesinti süreli dağıtım |
| **Paylaşılan barındırma** | cPanel, Plesk |
| **RoadRunner / Swoole** | Uzun süredir çalışan PHP |
| **FrankenPHP** | Modern uygulama sunucusu |
---

## Özet
PHP'nin ekosistemine **Laravel** (zarif, geliştirici dostu) ve **Symfony** (kurumsal, bileşenler) hakimdir. Standart yığın şunlardır: Paketler için **Composer**, web için **Laravel** veya **Symfony**, test için **PHPUnit** veya **Pest**, statik analiz için **PHPStan**, biçimlendirme için **Laravel Pint** veya **PHP-CS-Fixer** ve sunum için **PHP-FPM** veya **RoadRunner**. Numaralandırmalar, fiberler, salt okunur sınıflar ve birleşim türleri içeren modern PHP 8.3+, itibarının gösterdiğinden çok daha yetenekli bir dildir. Ekosistem web geliştirme, içerik yönetimi (WordPress, Drupal) ve e-ticarette (Magento, WooCommerce) öne çıkıyor.