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

# PHP - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ پی ایچ پی ماحولیاتی نظام میں ضروری ٹولز، فریم ورک، اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## پی ایچ پی کے رن ٹائمز
| رن ٹائم | نوٹس |
|---------|---------|
| **PHP-FPM** | فاسٹ سی جی آئی پروسیس مینیجر (سب سے عام) |
| **CLI** | کمانڈ لائن انٹرفیس |
| **سوول** | Async، کوروٹین پر مبنی |
| **روڈ رنر** | اعلی کارکردگی (گو بیسڈ) |
| **FrankenPHP** | جدید پی ایچ پی ایپ سرور (گو) |
| **PHP 8.3+** | کرنٹ اسٹیبل جس میں اینم، ریشے، صرف پڑھنے کے ساتھ |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## پیکیج مینجمنٹ
| ٹول | مقصد |
|------|---------|
| **موسیقار** | انحصار مینیجر (معیاری) |
| **پیکیجسٹ** | پہلے سے طے شدہ پیکیج ذخیرہ |
| **نجی پیکجسٹ** | پرائیویٹ پیکج ہوسٹنگ |
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

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **لاراول** | مکمل اسٹیک | سب سے زیادہ مقبول، خوبصورت API |
| **سمفونی** | مکمل اسٹیک | انٹرپرائز، اجزاء |
| **پتلا** | مائیکرو | APIs، چھوٹی ایپس |
| **لومین** | مائیکرو (Laravel) | فاسٹ مائیکرو سروسز |
| **کیک پی ایچ پی** | مکمل اسٹیک | تیز رفتار ترقی |
| **CodeIgniter** | ہلکا پھلکا | سادہ ایپس |
| **Yii** | مکمل اسٹیک | کارکردگی پر مرکوز |
| **سرپل** | جدید | طویل عرصے سے چل رہا ہے، سوول |
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

## ڈیٹا بیس اور ORM
| ٹیکنالوجی | قسم |
|------------|------|
| **فصیح** | Laravel's ORM (ایکٹو ریکارڈ) |
| **نظریہ** | Symfony's ORM (ڈیٹا میپر) |
| **سوال بنانے والا** | روانی SQL بلڈر |
| **PDO** | نچلی سطح کے ڈیٹا بیس تک رسائی |
| **لاریول ہجرت** | سکیما مینجمنٹ |
| **فنکس** | اسٹینڈ اکیلے ہجرتیں |
| **فلائی وے** | ڈیٹا بیس کی منتقلی |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **PHPUnit** | معیاری ٹیسٹ فریم ورک |
| **کیڑے** | خوبصورت ٹیسٹنگ (PHPUnit پر بنایا گیا) |
| **لاریول ڈسک** | براؤزر ٹیسٹنگ |
| **مذاق** | طنزیہ فریم ورک |
| **انفیکشن** | میوٹیشن ٹیسٹنگ |
| **PHPStan** | جامد تجزیہ (کیڑے بھی پکڑتا ہے) |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **PHPStan** | جامد تجزیہ (سطح 0-9) |
| **زبور** | جامد تجزیہ (متبادل) |
| **لاراول پینٹ** | کوڈ سٹائل (Laravel) |
| **PHP-CS-Fixer** | کوڈ سٹائل (جنرل) |
| **PHPMD** | گندگی کا پتہ لگانا |
| **PHP_CodeSniffer** | سونگھنا اور انداز |
| **ریکٹر** | خودکار ری فیکٹرنگ |
| **Deptrac** | انحصار تجزیہ |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## ٹیمپلیٹ انجن
| انجن | نوٹس |
|---------|-------|
| **بلیڈ** | Laravel کا ٹیمپلیٹ انجن |
| **ٹہنی** | سیمفونی کا ٹیمپلیٹ انجن |
| **لیٹے** | نیٹ کا محفوظ ٹیمپلیٹ انجن |
| **پلیٹیں** | مقامی پی ایچ پی ٹیمپلیٹس |
---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **گزل** | HTTP کلائنٹ |
| **Symfony HttpClient** | HTTP کلائنٹ |
| **کاربن** | تاریخ/وقت لائبریری |
| **سیمفونی کنسول** | CLI فریم ورک |
| **مونولوگ** | لاگنگ |
| **لاریول قطار** | پس منظر کی نوکریاں |
| **لاریول کیشئیر** | پٹی بلنگ |
| **لاراول سوشلائٹ** | OAuth کی توثیق |
| **لاراول سینکٹم** | API کی توثیق |
| **لاراول ہورائزن** | ریڈیس قطار ڈیش بورڈ |
| **لائیو وائر** | JS کے بغیر متحرک UI |
| **Inertia.js** | SPA اڈاپٹر (Vue/React + Laravel) |
| **اسپیٹی پیکجز** | اعلی معیار کی افادیت |
| **لیگ پیکجز** | کمیونٹی لائبریریاں |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **PhpStorm** | بہترین PHP IDE (JetBrains) |
| **VS Code + PHP Intelephense** | ہلکا پھلکا، LSP پر مبنی |
| **نیوم + پی ایچ پییکٹر** | ٹرمینل پر مبنی |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **PHP-FPM + Nginx** | کلاسک پروڈکشن سیٹ اپ |
| **Apache + mod_php** | روایتی |
| **ڈوکر** | کنٹینرائزڈ (php:fpm-alpine) |
| **لاراول فورج** | سرور کا انتظام |
| **لاریول بخارات** | AWS Lambda کی تعیناتی |
| ** ایلچی** | زیرو ڈاؤن ٹائم تعیناتی |
| **مشترکہ ہوسٹنگ** | cPanel، Plesk |
| **روڈ رنر / سوول** | طویل عرصے سے چلنے والا پی ایچ پی |
| **FrankenPHP** | جدید ایپ سرور |
---

## خلاصہ
PHP کے ماحولیاتی نظام پر **Laravel** (خوبصورت، ڈویلپر کے موافق) اور **Symfony** (انٹرپرائز، اجزاء) کا غلبہ ہے۔ معیاری اسٹیک یہ ہے: پیکجز کے لیے **کمپوزر**، ویب کے لیے **Laravel** یا **Symfony**، **PHPUnit** یا **Pest** ٹیسٹنگ کے لیے، **PHPStan** جامد تجزیہ کے لیے، **Laravel Pint** یا **PHP-CS-Fixer** فارمیٹنگ کے لیے، اور **PHP-CS-Fixer** کے لیے اور **PHP-Unner** کے لیے سرور** جدید PHP 8.3+ enums، fibers، صرف پڑھنے والی کلاسز، اور یونین کی اقسام اس کی ساکھ سے کہیں زیادہ قابل زبان ہے۔ ماحولیاتی نظام ویب ڈویلپمنٹ، مواد کے انتظام (ورڈپریس، ڈروپل)، اور ای کامرس (میگینٹو، وو کامرس) میں سبقت لے جاتا ہے۔