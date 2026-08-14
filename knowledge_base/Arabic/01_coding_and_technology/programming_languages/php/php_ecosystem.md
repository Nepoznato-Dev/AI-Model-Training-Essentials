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
# PHP - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية التحتية الأساسية في نظام PHP البيئي.
---

## أوقات تشغيل PHP
| وقت التشغيل | ملاحظات |
|---------|------|
| ** PHP-FPM ** | مدير عمليات FastCGI (الأكثر شيوعًا) |
| ** سطر ** | واجهة سطر الأوامر |
| **سوول** | غير متزامن، قائم على الكوروتين |
| **رود رانر** | أداء عالي (معتمد على الذهاب) |
| ** فرانكن PHP ** | خادم تطبيقات PHP الحديث (Go) |
| ** PHP 8.3+** | التيار المستقر مع التعدادات والألياف للقراءة فقط |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## إدارة الحزم
| أداة | الغرض |
|------|---------|
| ** الملحن ** | مدير التبعية (المعيار) |
| **باكاجيست** | مستودع الحزمة الافتراضي |
| **معبئ خاص** | استضافة الباقة الخاصة |
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

## أطر الويب
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| **لارافيل** | مكدس كامل | واجهة برمجة التطبيقات (API) الأكثر شعبية وأنيقة |
| **سيمفوني** | مكدس كامل | المؤسسة والمكونات |
| ** سليم ** | مايكرو | واجهات برمجة التطبيقات والتطبيقات الصغيرة |
| **التجويف** | مايكرو (لارافيل) | خدمات متناهية الصغر سريعة |
| **كيكPHP** | مكدس كامل | التطور السريع |
| **كود ايجنيتر** | خفيف الوزن | تطبيقات بسيطة |
| **يي** | مكدس كامل | تركز على الأداء |
| **دوامة** | حديث | طويلة المدى، سوول |
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

## قاعدة البيانات وORM
| تكنولوجيا | اكتب |
|------------|------|
| **بليغ** | Laravel's ORM (السجل النشط) |
| **العقيدة** | Symfony's ORM (مخطط البيانات) |
| **منشئ الاستعلام** | منشئ SQL بطلاقة |
| ** شركة تنمية نفط عمان ** | الوصول إلى قاعدة البيانات ذات المستوى المنخفض |
| **الهجرة لارافيل** | إدارة المخطط |
| **فينكس** | الهجرات المستقلة |
| **مسار الهجرة** | ترحيل قاعدة البيانات |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| ** PHPUnit ** | إطار الاختبار القياسي |
| **الآفة** | اختبار أنيق (مبني على PHPUnit) |
| ** لارافيل داسك ** | اختبار المتصفح |
| **استهزاء** | إطار السخرية |
| **العدوى** | اختبار الطفرة |
| **PHPStan** | التحليل الثابت (يكتشف الأخطاء أيضًا) |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **PHPStan** | التحليل الثابت (المستويات 0-9) |
| **مزمور** | التحليل الثابت (البديل) |
| **لارافيل باينت** | نمط الكود (لارافيل) |
| **مثبت PHP-CS** | نمط الكود (عام) |
| ** PHPMD ** | كشف الفوضى |
| **PHP_CodeSniffer** | الشمة والأسلوب |
| **رئيس الجامعة** | إعادة البناء الآلي |
| **ديبتراك** | تحليل التبعية |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## محركات القالب
| المحرك | ملاحظات |
|--------|------|
| **شفرة** | محرك قوالب لارافيل |
| **غصين** | محرك قالب Symfony |
| **لاتيه** | محرك القالب الآمن الخاص بـ Nette |
| **لوحات** | قوالب PHP الأصلية |
---

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| ** غزالة ** | عميل HTTP |
| **Symfony HttpClient** | عميل HTTP |
| **كربون** | مكتبة التاريخ/الوقت |
| ** وحدة تحكم Symfony ** | إطار عمل واجهة سطر الأوامر |
| ** مونولوج ** | تسجيل |
| ** قائمة انتظار لارافيل ** | وظائف الخلفية |
| ** لارافيل كاشير ** | الفواتير الشريطية |
| ** لارافيل الإجتماعي ** | مصادقة OAuth |
| ** حرم لارافيل ** | مصادقة API |
| **لارافيل هورايزن** | لوحة معلومات قائمة انتظار Redis |
| **لايف واير** | واجهة مستخدم ديناميكية بدون JS |
| **القصور الذاتي.js** | محول SPA (Vue/React + Laravel) |
| **باقات سباتي** | مرافق عالية الجودة |
| **حزم الدوري** | مكتبات المجتمع |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| ** PHPStorm ** | أفضل PHP IDE (JetBrains) |
| ** كود VS + PHP Intelephense ** | خفيف الوزن، يعتمد على LSP |
| ** نيوفيم + phpactor ** | القائم على المحطة الطرفية |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **PHP-FPM + Nginx** | إعداد الإنتاج الكلاسيكي |
| **اباتشي + mod_php** | تقليدي |
| ** عامل الميناء ** | حاويات (php:fpm-alpine) |
| ** لارافيل فورج ** | إدارة الخادم |
| **بخار لارافيل** | نشر AWS Lambda |
| **المبعوث** | النشر بدون توقف |
| **استضافة مشتركة** | لوحة التحكم، بليسك |
| ** رود رانر / سوول ** | PHP طويل المدى |
| ** فرانكن PHP ** | خادم التطبيقات الحديث |
---

## ملخص
يهيمن **Laravel** (أنيق وسهل الاستخدام للمطورين) و **Symfony** (للمؤسسات والمكونات) على النظام البيئي لـ PHP. المكدس القياسي هو: **Composer** للحزم، **Laravel** أو **Symfony** للويب، **PHPUnit** أو **Pest** للاختبار، **PHPStan** للتحليل الثابت، **Laravel Pint** أو **PHP-CS-Fixer** للتنسيق، و **PHP-FPM** أو **RoadRunner** للعرض. تعد PHP 8.3+ الحديثة مع التعدادات والألياف وفئات القراءة فقط وأنواع الاتحاد لغة أكثر قدرة بكثير مما توحي به سمعتها. يتفوق النظام البيئي في تطوير الويب وإدارة المحتوى (WordPress وDrupal) والتجارة الإلكترونية (Magento وWooCommerce).