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
# PHP - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم PHP را پوشش می‌دهد.
---

## زمان اجرا PHP
| زمان اجرا | یادداشت ها |
|---------|-------|
| **PHP-FPM** | FastCGI Process Manager (متداول ترین) |
| **CLI** | رابط خط فرمان |
| **سوول** | Async، مبتنی بر کوروتین |
| **RoadRunner** | عملکرد بالا (بر اساس Go) |
| **FrankenPHP** | سرور برنامه مدرن PHP (Go) |
| **PHP 8.3+** | جریان پایدار با enums، فیبرها، فقط خواندنی |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **آهنگساز** | مدیر وابستگی (استاندارد) |
| **بسته فروش** | مخزن بسته پیش فرض |
| ** بسته بندی خصوصی ** | میزبانی پکیج خصوصی |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **لاراول** | تمام پشته | محبوب ترین و زیباترین API |
| **سیمفونی** | تمام پشته | شرکت، قطعات |
| **لاغر** | میکرو | API ها، برنامه های کوچک |
| **لومن** | میکرو (لاراول) | میکرو سرویس های سریع |
| **CakePHP** | تمام پشته | توسعه سریع |
| **CodeIgniter** | سبک | برنامه های ساده |
| **Yii** | تمام پشته | عملکرد محور |
| **مارپیچ** | مدرن | طولانی مدت، Swoole |
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

## پایگاه داده و ORM
| فناوری | نوع |
|------------|------|
| **فصیح** | ORM لاراول (Active Record) |
| **دکترین** | Symfony's ORM (Data Mapper) |
| **کوئری ساز** | سازنده SQL روان |
| **PDO** | دسترسی به پایگاه داده سطح پایین |
| ** مهاجرت لاراول** | مدیریت طرحواره |
| **فنکس** | مهاجرت های مستقل |
| **فلای وی** | مهاجرت های پایگاه داده |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **PHPUnit** | چارچوب آزمون استاندارد |
| **آفت ** | تست زیبا (ساخته شده بر روی PHPUnit) |
| **گرگ و میش لاراول** | تست مرورگر |
| **مسخره** | چارچوب تمسخر آمیز |
| **عفونت** | تست جهش |
| **PHPStan** | تجزیه و تحلیل استاتیک (همچنین اشکالات را می گیرد) |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **PHPStan** | تجزیه و تحلیل استاتیک (سطوح 0-9) |
| **مزمور** | تجزیه و تحلیل استاتیک (جایگزین) |
| **لاراول پینت** | سبک کد (لاراول) |
| **PHP-CS-Fixer** | سبک کد (عمومی) |
| **PHPMD** | تشخیص آشفتگی |
| **PHP_CodeSniffer** | خرناس و استایل |
| **رئیس** | بازسازی خودکار |
| **دپتراک** | تحلیل وابستگی |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## موتورهای قالب
| موتور | یادداشت ها |
|--------|-------|
| **تیغ** | موتور قالب لاراول |
| **شاخه** | موتور قالب سیمفونی |
| **لاته** | موتور قالب ایمن Nette |
| **بشقاب** | قالب های بومی PHP |
---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **گوزل** | سرویس گیرنده HTTP |
| **Symfony HttpClient** | سرویس گیرنده HTTP |
| **کربن** | کتابخانه تاریخ/زمان |
| **کنسول سیمفونی** | چارچوب CLI |
| **مونولوژیک** | ورود به سیستم |
| **صف لاراول** | مشاغل پیشینه |
| **صندوق لاراول** | صورتحساب راه راه |
| **Laravel Socialite** | احراز هویت OAuth |
| **Laravel Sanctum** | احراز هویت API |
| **Laravel Horizon** | داشبورد صف ردیس |
| **لایو وایر** | رابط کاربری پویا بدون JS |
| **Inertia.js** | آداپتور SPA (Vue/React + Laravel) |
| **بسته های اسپاتی** | آب و برق با کیفیت بالا |
| **بسته های لیگ** | کتابخانه های جامعه |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **PhpStorm** | بهترین PHP IDE (JetBrains) |
| **VS Code + PHP Intelephense** | سبک وزن مبتنی بر LSP |
| **Neovim + phpactor** | مبتنی بر ترمینال |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **PHP-FPM + Nginx** | راه اندازی تولید کلاسیک |
| **Apache + mod_php** | سنتی |
| **داکر** | Containerized (php:fpm-alpine) |
| **لاراول فورج** | مدیریت سرور |
| **بخار لاراول** | استقرار AWS Lambda |
| **فرستاده** | استقرار بدون توقف |
| ** هاست اشتراکی ** | سی پنل، پلسک |
| **RoadRunner / Swoole** | PHP طولانی مدت |
| **FrankenPHP** | سرور برنامه مدرن |
---

## خلاصه
اکوسیستم PHP تحت سلطه **Laravel** (ظریف، مناسب برای توسعه دهندگان) و **Symfony** (تشکیلات، مؤلفه ها) است. پشته استاندارد عبارتند از: **Composer** برای بسته‌ها، **Laravel** یا **Symfony** برای وب، **PHPUnit** یا **Pest** برای آزمایش، **PHPStan** برای تجزیه و تحلیل استاتیک، **Laravel Pint** یا **PHP-CS-Fixer** برای قالب‌بندی، و **PHP-FPMRving** یا Road. PHP 8.3+ مدرن با enums، فیبرها، کلاس‌های فقط خواندنی و انواع اتحادیه، زبانی بسیار تواناتر از آن چیزی است که شهرت آن نشان می‌دهد. این اکوسیستم در توسعه وب، مدیریت محتوا (وردپرس، دروپال) و تجارت الکترونیک (مجنتو، ووکامرس) برتری دارد.