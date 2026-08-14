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
# PHP - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่จำเป็นในระบบนิเวศ PHP
---

## รันไทม์ PHP
| รันไทม์ | หมายเหตุ |
|---------|-------|
| **PHP-FPM** | FastCGI Process Manager (ทั่วไปที่สุด) |
| **คลี** | อินเทอร์เฟซบรรทัดคำสั่ง |
| **สวูล** | Async ที่ใช้ coroutine |
| **โรดรันเนอร์** | ประสิทธิภาพสูง (Go-based) |
| **แฟรงเกน PHP** | เซิร์ฟเวอร์แอป PHP สมัยใหม่ (Go) |
| **PHP 8.3+** | กระแสเสถียรด้วย enums, ไฟเบอร์, อ่านอย่างเดียว |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## การจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ผู้แต่ง** | ผู้จัดการการพึ่งพา (มาตรฐาน) |
| **ผู้บรรจุหีบห่อ** | พื้นที่เก็บข้อมูลแพ็กเกจเริ่มต้น |
| **ผู้บรรจุหีบห่อส่วนตัว** | แพ็คเกจโฮสติ้งส่วนตัว |
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

## กรอบงานเว็บ
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **ลาร์ราเวล** | เต็มกอง | API ที่หรูหราและได้รับความนิยมสูงสุด |
| **ซิมโฟนี่** | เต็มกอง | องค์กรส่วนประกอบ |
| **ผอม** | ไมโคร | APIs แอพขนาดเล็ก |
| **ลูเมน** | ไมโคร (Laravel) | ไมโครเซอร์วิสที่รวดเร็ว |
| **CakePHP** | เต็มกอง | การพัฒนาอย่างรวดเร็ว |
| **โค้ดอิกนิเตอร์** | น้ำหนักเบา | แอพง่ายๆ |
| **ยี้** | เต็มกอง | เน้นประสิทธิภาพ |
| **เกลียว** | ทันสมัย ​​| วิ่งระยะยาว Swoole |
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

## ฐานข้อมูลและ ORM
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **ฝีปาก** | ORM ของ Laravel (บันทึกที่ใช้งานอยู่) |
| **หลักคำสอน** | ORM (Data Mapper) ของ Symfony |
| **ตัวสร้างแบบสอบถาม** | ตัวสร้าง SQL ได้อย่างคล่องแคล่ว |
| **PDO** | การเข้าถึงฐานข้อมูลระดับต่ำ |
| **การโยกย้าย Laravel** | การจัดการสคีมา |
| **ฟิงค์** | การโยกย้ายแบบสแตนด์อโลน |
| **ทางบิน** | การย้ายฐานข้อมูล |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **PHPUnit** | กรอบการทดสอบมาตรฐาน |
| **สัตว์รบกวน** | การทดสอบที่หรูหรา (สร้างบน PHPUnit) |
| **Laravel Dusk** | การทดสอบเบราว์เซอร์ |
| **การเยาะเย้ย** | กรอบการเยาะเย้ย |
| **การติดเชื้อ** | การทดสอบการกลายพันธุ์ |
| **PHPStan** | การวิเคราะห์แบบคงที่ (จับจุดบกพร่องด้วย) |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **PHPStan** | การวิเคราะห์แบบคงที่ (ระดับ 0-9) |
| **สดุดี** | การวิเคราะห์แบบคงที่ (ทางเลือก) |
| **ลาราเวล ไพน์** | รูปแบบโค้ด (Laravel) |
| **PHP-CS-Fixer** | รูปแบบโค้ด (ทั่วไป) |
| **PHPMD** | การตรวจจับความยุ่งเหยิง |
| **PHP_CodeSniffer** | ดมและสไตล์ |
| **อธิการบดี** | การรีแฟคเตอร์อัตโนมัติ |
| **เดปแทรค** | การวิเคราะห์การพึ่งพา |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## เอ็นจิ้นเทมเพลต
| เครื่องยนต์ | หมายเหตุ |
|--------|--------|
| **ใบมีด** | เอ็นจิ้นเทมเพลตของ Laravel |
| **กิ่ง** | เอ็นจิ้นเทมเพลตของ Symfony |
| **ลาเต้** | เอ็นจิ้นเทมเพลตที่ปลอดภัยของ Nette |
| **จาน** | เทมเพลต PHP ดั้งเดิม |
---

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **ตะลึง** | ไคลเอ็นต์ HTTP |
| **Symfony HttpClient** | ไคลเอ็นต์ HTTP |
| **คาร์บอน** | ไลบรารีวันที่/เวลา |
| **คอนโซล Symfony** | กรอบงาน CLI |
| **พูดคนเดียว** | การบันทึก |
| **คิว Laravel** | งานพื้นหลัง |
| **แคชเชียร์ Laravel** | ลายการเรียกเก็บเงิน |
| **Laravel สังคม** | การรับรองความถูกต้อง OAuth |
| **สถานที่ศักดิ์สิทธิ์ Laravel** | การรับรองความถูกต้อง API |
| **ลาราเวล ฮอไรซัน** | แดชบอร์ดคิว Redis |
| **ถ่ายทอดสด** | UI แบบไดนามิกที่ไม่มี JS |
| **ความเฉื่อย.js** | อะแดปเตอร์ SPA (Vue / React + Laravel) |
| **แพ็คเกจ Spatie** | สาธารณูปโภคคุณภาพสูง |
| **แพ็คเกจลีก** | ห้องสมุดชุมชน |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **PhpStorm** | สุดยอด PHP IDE (JetBrains) |
| **รหัส VS + PHP Intelephense** | น้ำหนักเบา ใช้ LSP |
| **นีโอวิม + phpactor** | บนเทอร์มินัล |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **PHP-FPM + Nginx** | การตั้งค่าการผลิตแบบคลาสสิก |
| **Apache + mod_php** | แบบดั้งเดิม |
| **นักเทียบท่า** | บรรจุในคอนเทนเนอร์ (php:fpm-alpine) |
| **Laravel Forge** | การจัดการเซิร์ฟเวอร์ |
| **ไอระเหย Laravel** | การปรับใช้ AWS Lambda |
| **ทูต** | การปรับใช้โดยไม่ต้องหยุดทำงานเป็นศูนย์ |
| **โฮสติ้งที่ใช้ร่วมกัน** | cPanel, Plesk |
| **โรดรันเนอร์ / สวูล** | PHP ระยะยาว |
| **แฟรงเกน PHP** | เซิร์ฟเวอร์แอปสมัยใหม่ |
---

## สรุป
ระบบนิเวศของ PHP ถูกครอบงำโดย **Laravel** (หรูหรา เป็นมิตรกับนักพัฒนา) และ **Symfony** (องค์กร ส่วนประกอบ) สแต็กมาตรฐานคือ **Composer** สำหรับแพ็คเกจ **Laravel** หรือ **Symfony** สำหรับเว็บ **PHPUnit** หรือ **Pest** สำหรับการทดสอบ **PHPStan** สำหรับการวิเคราะห์แบบคงที่ **Laravel Pint** หรือ **PHP-CS-Fixer** สำหรับการจัดรูปแบบ และ **PHP-FPM** หรือ **RoadRunner** สำหรับการให้บริการ PHP 8.3+ สมัยใหม่พร้อม enums, ไฟเบอร์, คลาสแบบอ่านอย่างเดียว และประเภทยูเนียนเป็นภาษาที่มีความสามารถมากกว่าที่ชื่อเสียงแนะนำไว้มาก ระบบนิเวศเป็นเลิศในด้านการพัฒนาเว็บไซต์ การจัดการเนื้อหา (WordPress, Drupal) และอีคอมเมิร์ซ (Magento, WooCommerce)