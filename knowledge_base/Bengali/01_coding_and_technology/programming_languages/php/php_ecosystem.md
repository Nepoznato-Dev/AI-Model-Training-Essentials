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

# PHP — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি পিএইচপি ইকোসিস্টেমের প্রয়োজনীয় টুল, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## পিএইচপি রানটাইম
| রানটাইম | নোট |
|---------|---------|
| **PHP-FPM** | ফাস্টসিজিআই প্রসেস ম্যানেজার (সবচেয়ে সাধারণ) |
| **CLI** | কমান্ড লাইন ইন্টারফেস |
| **স্বুল** | Async, coroutine-ভিত্তিক |
| **রোডরানার** | উচ্চ-কর্মক্ষমতা (গো-ভিত্তিক) |
| **ফ্রাঙ্কেনপিএইচপি** | আধুনিক পিএইচপি অ্যাপ সার্ভার (গো) |
| **PHP 8.3+** | enums, fibers সহ বর্তমান স্থিতিশীল, শুধুমাত্র পঠন |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য |
|------|---------|
| **সুরকার** | নির্ভরতা ব্যবস্থাপক (মান) |
| **প্যাকেজিস্ট** | ডিফল্ট প্যাকেজ সংগ্রহস্থল |
| **ব্যক্তিগত প্যাকেজিস্ট** | ব্যক্তিগত প্যাকেজ হোস্টিং |
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

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **লারাভেল** | ফুল-স্ট্যাক | সবচেয়ে জনপ্রিয়, মার্জিত API |
| **সিমফনি** | ফুল-স্ট্যাক | এন্টারপ্রাইজ, উপাদান |
| **স্লিম** | মাইক্রো | APIs, ছোট অ্যাপস |
| **লুমেন** | মাইক্রো (লারাভেল) | দ্রুত মাইক্রো সার্ভিস |
| **কেকপিএইচপি** | ফুল-স্ট্যাক | দ্রুত উন্নয়ন |
| **কোডইগনিটার** | লাইটওয়েট | সহজ অ্যাপস |
| **ইই** | ফুল-স্ট্যাক | কর্মক্ষমতা-কেন্দ্রিক |
| **সর্পিল** | আধুনিক | দীর্ঘমেয়াদী, Swoole |
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

## ডাটাবেস এবং ওআরএম
| প্রযুক্তি | প্রকার |
|------------|------|
| **বক্তা** | লারাভেলের ওআরএম (সক্রিয় রেকর্ড) |
| ** মতবাদ** | Symfony's ORM (ডেটা ম্যাপার) |
| **কোয়েরি নির্মাতা** | সাবলীল এসকিউএল নির্মাতা |
| **PDO** | নিম্ন-স্তরের ডাটাবেস অ্যাক্সেস |
| **লারাভেল মাইগ্রেশন** | স্কিমা ব্যবস্থাপনা |
| **ফিনক্স** | স্বতন্ত্র মাইগ্রেশন |
| **ফ্লাইওয়ে** | ডাটাবেস মাইগ্রেশন |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **PHPUnit** | স্ট্যান্ডার্ড টেস্ট ফ্রেমওয়ার্ক |
| **কীট** | মার্জিত পরীক্ষা (PHPUnit এ নির্মিত) |
| **লারাভেল সন্ধ্যা** | ব্রাউজার টেস্টিং |
| **বিদ্রুপ** | উপহাস কাঠামো |
| **সংক্রমণ** | মিউটেশন পরীক্ষা |
| **PHPStan** | স্ট্যাটিক বিশ্লেষণ (এছাড়াও বাগ ধরা) |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **PHPStan** | স্ট্যাটিক বিশ্লেষণ (স্তর 0-9) |
| **গীত** | স্ট্যাটিক বিশ্লেষণ (বিকল্প) |
| **লারাভেল পিন্ট** | কোড শৈলী (লারাভেল) |
| **পিএইচপি-সিএস-ফিক্সার** | কোড শৈলী (সাধারণ) |
| **PHPMD** | মেস সনাক্তকরণ |
| **PHP_CodeSniffer** | স্নিফিং এবং স্টাইল |
| **রেক্টর** | স্বয়ংক্রিয় রিফ্যাক্টরিং |
| **Deptrac** | নির্ভরতা বিশ্লেষণ |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## টেমপ্লেট ইঞ্জিন
| ইঞ্জিন | নোট |
|---------|-------|
| **ব্লেড** | লারাভেলের টেমপ্লেট ইঞ্জিন |
| **টুইগ** | Symfony এর টেমপ্লেট ইঞ্জিন |
| **ল্যাটে** | Nette এর নিরাপদ টেমপ্লেট ইঞ্জিন |
| **প্লেট** | নেটিভ পিএইচপি টেমপ্লেট |
---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **গজল** | HTTP ক্লায়েন্ট |
| **Symfony HttpClient** | HTTP ক্লায়েন্ট |
| **কার্বন** | তারিখ/সময় লাইব্রেরি |
| **সিমফনি কনসোল** | CLI ফ্রেমওয়ার্ক |
| **মনোলগ** | লগিং |
| **লারাভেল সারি** | পটভূমি চাকরি |
| **লারাভেল ক্যাশিয়ার** | স্ট্রাইপ বিলিং |
| **লারাভেল সোশ্যালাইট** | OAuth প্রমাণীকরণ |
| **লারাভেল অভয়ারণ্য** | API প্রমাণীকরণ |
| **লারাভেল দিগন্ত** | রেডিস কিউ ড্যাশবোর্ড |
| **লাইভওয়্যার** | JS ছাড়া ডায়নামিক UI |
| **Inertia.js** | SPA অ্যাডাপ্টার (Vue/React + Laravel) |
| **স্পেটি প্যাকেজ** | উচ্চ মানের ইউটিলিটি |
| **লীগ প্যাকেজ** | কমিউনিটি লাইব্রেরি |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **পিএইচপিস্টর্ম** | সেরা PHP IDE (JetBrains) |
| **ভিএস কোড + পিএইচপি ইন্টেলিফেনস** | লাইটওয়েট, LSP-ভিত্তিক |
| **নিওভিম + পিএইচপ্যাক্টর** | টার্মিনাল ভিত্তিক |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **PHP-FPM + Nginx** | ক্লাসিক উত্পাদন সেটআপ |
| **Apache + mod_php** | ঐতিহ্যগত |
| **ডকার** | কন্টেইনারাইজড (php:fpm-আল্পাইন) |
| **লারাভেল ফোর্জ** | সার্ভার ব্যবস্থাপনা |
| **লারাভেল বাষ্প** | AWS Lambda স্থাপনা |
| **দূত** | জিরো-ডাউনটাইম স্থাপনা |
| **শেয়ারড হোস্টিং** | cPanel, Plesk |
| **রোডরানার / সোউল** | দীর্ঘদিন ধরে চলমান পিএইচপি |
| **ফ্রাঙ্কেনপিএইচপি** | আধুনিক অ্যাপ সার্ভার |
---

## সারাংশ
PHP-এর ইকোসিস্টেম **Laravel** (মার্জিত, বিকাশকারী-বান্ধব) এবং **Symfony** (এন্টারপ্রাইজ, উপাদান) দ্বারা প্রভাবিত। স্ট্যান্ডার্ড স্ট্যাক হল: প্যাকেজের জন্য **কম্পোজার**, ওয়েবের জন্য **Laravel** বা **Symfony**, **PHPUnit** বা **পেস্ট** পরীক্ষার জন্য, **PHPStan** স্ট্যাটিক বিশ্লেষণের জন্য, **Laravel পিন্ট** বা **PHP-CS-Fixer** বিন্যাসের জন্য, এবং **PHP-S-Fixer** এর জন্য **PHP-Ro** সার্ভ করার জন্য। আধুনিক PHP 8.3+ enums, fibers, শুধুমাত্র পঠনযোগ্য শ্রেণী এবং ইউনিয়নের ধরন এর খ্যাতির চেয়ে অনেক বেশি সক্ষম ভাষা। ইকোসিস্টেমটি ওয়েব ডেভেলপমেন্ট, কন্টেন্ট ম্যানেজমেন্ট (ওয়ার্ডপ্রেস, ড্রুপাল), এবং ই-কমার্সে (ম্যাজেন্টো, WooCommerce) পারদর্শী।