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
# PHP — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem PHP.
---

## Waktu Proses PHP
| Waktu proses | Catatan |
|---------|-------|
| **PHP-FPM** | Manajer Proses FastCGI (paling umum) |
| **KLI** | Antarmuka baris perintah |
| **Swoole** | Async, berbasis coroutine |
| **Pelari Jalan** | Kinerja tinggi (berbasis Go) |
| **FrankenPHP** | Server aplikasi PHP modern (Go) |
| **PHP 8.3+** | Stabil saat ini dengan enum, fiber, readonly |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **Komposer** | Manajer ketergantungan (standar) |
| **Pengemasan** | Repositori paket default |
| **Paket Pribadi** | Hosting paket pribadi |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Laravel** | Tumpukan penuh | API paling populer dan elegan |
| **Simfoni** | Tumpukan penuh | Perusahaan, komponen |
| **Ramping** | Mikro | API, aplikasi kecil |
| **Lumen** | Mikro (Laravel) | Layanan mikro cepat |
| **KuePHP** | Tumpukan penuh | Perkembangan pesat |
| **CodeIgniter** | Ringan | Aplikasi sederhana |
| **Yii** | Tumpukan penuh | Berfokus pada kinerja |
| **Spiral** | Modern | Berjalan lama, Swoole |
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

## Basis Data & ORM
| Teknologi | Ketik |
|------------|------|
| **Fasih** | ORM Laravel (Catatan Aktif) |
| **Doktrin** | ORM (Pemeta Data) Symfony |
| **Pembuat Kueri** | Pembuat SQL yang lancar |
| **PDO** | Akses database tingkat rendah |
| **Migrasi Laravel** | Manajemen skema |
| **Phinx** | Migrasi mandiri |
| **Jalur Terbang** | Migrasi basis data |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Satuan PHP** | Kerangka uji standar |
| **Hama** | Pengujian elegan (dibangun di PHPUnit) |
| **Laravel Senja** | Pengujian peramban |
| **Ejekan** | Kerangka mengejek |
| **Infeksi** | Pengujian mutasi |
| **PHPStan** | Analisis statis (juga menangkap bug) |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **PHPStan** | Analisis statis (level 0-9) |
| **Mazmur** | Analisis statis (alternatif) |
| **Laravel Pint** | Gaya kode (Laravel) |
| **Pemecah PHP-CS** | Gaya kode (umum) |
| **PHPMD** | Deteksi kekacauan |
| **PHP_CodeSniffer** | Mengendus dan bergaya |
| **Rektor** | Pemfaktoran ulang otomatis |
| **Deptrak** | Analisis ketergantungan |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Mesin Templat
| Mesin | Catatan |
|--------|-------|
| **Pisau** | Mesin templat Laravel |
| **ranting** | Mesin templat Symfony |
| **Latte** | Mesin templat aman Nette |
| **Piring** | Templat PHP asli |
---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Membuang waktu** | Klien HTTP |
| **Symfony HttpClient** | Klien HTTP |
| **Karbon** | Perpustakaan tanggal/waktu |
| **Konsol Symfony** | Kerangka CLI |
| **Monolog** | Pencatatan |
| **Antrian Laravel** | Pekerjaan latar belakang |
| **Kasir Laravel** | Penagihan garis |
| **Sosialita Laravel** | Otentikasi OAuth |
| **Tempat Suci Laravel** | Otentikasi API |
| **Laravel Cakrawala** | Dasbor antrian Redis |
| **kabel langsung** | UI Dinamis tanpa JS |
| **Inersia.js** | Adaptor SPA (Vue/React + Laravel) |
| **Paket Spatie** | Utilitas berkualitas tinggi |
| **Paket Liga** | Perpustakaan komunitas |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **PhpStorm** | IDE PHP Terbaik (JetBrains) |
| **Kode VS + Intelefense PHP** | Ringan, berbasis LSP |
| **Neovim + phpactor** | Berbasis terminal |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **PHP-FPM + Nginx** | Pengaturan produksi klasik |
| **Apache+mod_php** | Tradisional |
| **Buruh pelabuhan** | dalam kontainer (php:fpm-alpine) |
| **Laravel Penempaan** | Manajemen server |
| **Uap Laravel** | Penerapan AWS Lambda |
| **Utusan** | Penerapan tanpa waktu henti |
| **Hosting bersama** | cPanel, Plesk |
| **Pelari Jalan / Swoole** | PHP yang sudah berjalan lama |
| **FrankenPHP** | Server aplikasi modern |
---

## Ringkasan
Ekosistem PHP didominasi oleh **Laravel** (elegan, ramah pengembang) dan **Symfony** (perusahaan, komponen). Tumpukan standarnya adalah: **Composer** untuk paket, **Laravel** atau **Symfony** untuk web, **PHPUnit** atau **Pest** untuk pengujian, **PHPStan** untuk analisis statis, **Laravel Pint** atau **PHP-CS-Fixer** untuk pemformatan, dan **PHP-FPM** atau **RoadRunner** untuk penyajian. PHP 8.3+ modern dengan enum, fiber, kelas readonly, dan tipe gabungan adalah bahasa yang jauh lebih mumpuni daripada yang ditunjukkan oleh reputasinya. Ekosistemnya unggul dalam pengembangan web, manajemen konten (WordPress, Drupal), dan e-commerce (Magento, WooCommerce).