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

# PHP - पारिस्थितिकी तंत्र और टूलींग गाइड
यह मार्गदर्शिका PHP पारिस्थितिकी तंत्र में आवश्यक उपकरण, ढांचे और बुनियादी ढांचे को शामिल करती है।
---

## PHP रनटाइम्स
| रनटाइम | नोट्स |
|------|-------|
| **पीएचपी-एफपीएम** | फास्टसीजीआई प्रक्रिया प्रबंधक (सबसे सामान्य) |
| **सीएलआई** | कमांड-लाइन इंटरफ़ेस |
| **स्वूले** | Async, कोरआउटिन-आधारित |
| **रोडरनर** | उच्च-प्रदर्शन (गो-आधारित) |
| **फ्रैंकनपीएचपी** | आधुनिक PHP ऐप सर्वर (जाओ) |
| **PHP 8.3+** | एनम, फाइबर के साथ वर्तमान स्थिर, केवल पढ़ने के लिए |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## पैकेज प्रबंधन
| उपकरण | उद्देश्य |
|------|---------|
| **संगीतकार** | निर्भरता प्रबंधक (मानक) |
| **पैकेजिस्ट** | डिफ़ॉल्ट पैकेज भंडार |
| **निजी पैकेजिस्ट** | निजी पैकेज होस्टिंग |
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

## वेब फ्रेमवर्क
| ढाँचा | प्रकार | के लिए सर्वश्रेष्ठ |
|--------|------|-------|
| **लारवेल** | फुल-स्टैक | सबसे लोकप्रिय, सुंदर एपीआई |
| **सिम्फनी** | फुल-स्टैक | उद्यम, घटक |
| **स्लिम** | सूक्ष्म | एपीआई, छोटे ऐप्स |
| **लुमेन** | माइक्रो (लारवेल) | तेज़ सूक्ष्म सेवाएँ |
| **केकपीएचपी** | फुल-स्टैक | तेजी से विकास |
| **कोडइग्निटर** | हल्का वजन | सरल ऐप्स |
| **यी** | फुल-स्टैक | प्रदर्शन-केंद्रित |
| **सर्पिल** | आधुनिक | लंबे समय तक चलने वाला, स्वोले |
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

## डेटाबेस और ओआरएम
| प्रौद्योगिकी | प्रकार |
|------|------|
| **वाक्पटु** | लारवेल का ORM (सक्रिय रिकॉर्ड) |
| **सिद्धांत** | सिम्फनी का ORM (डेटा मैपर) |
| **क्वेरी बिल्डर** | धाराप्रवाह SQL बिल्डर |
| **पीडीओ** | निम्न-स्तरीय डेटाबेस पहुंच |
| **लारवेल माइग्रेशन** | स्कीमा प्रबंधन |
| **फिंक्स** | स्टैंडअलोन माइग्रेशन |
| **फ्लाईवे** | डेटाबेस माइग्रेशन |
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

## परीक्षण
| ढाँचा | उद्देश्य |
|----|----|
| **पीएचपीयूनिट** | मानक परीक्षण रूपरेखा |
| **कीट** | शानदार परीक्षण (PHPUnit पर निर्मित) |
| **लारवेल डस्क** | ब्राउज़र परीक्षण |
| **उपहास** | मॉकिंग फ्रेमवर्क |
| **संक्रमण** | उत्परिवर्तन परीक्षण |
| **PHPStan** | स्थैतिक विश्लेषण (बग्स भी पकड़ता है) |
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

## कोड गुणवत्ता
| उपकरण | उद्देश्य |
|------|---------|
| **PHPStan** | स्थैतिक विश्लेषण (स्तर 0-9) |
| **स्तोत्र** | स्थैतिक विश्लेषण (वैकल्पिक) |
| **लारवेल पिंट** | कोड शैली (लारवेल) |
| **पीएचपी-सीएस-फिक्सर** | कोड शैली (सामान्य) |
| **पीएचपीएमडी** | गड़बड़ी का पता लगाना |
| **PHP_CodeSniffer** | सूँघना और स्टाइल |
| **रेक्टर** | स्वचालित रिफैक्टरिंग |
| **डिप्ट्रैक** | निर्भरता विश्लेषण |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## टेम्पलेट इंजन
| इंजन | नोट्स |
|-------|-------|
| **ब्लेड** | लारवेल का टेम्पलेट इंजन |
| **टहनी** | सिम्फनी का टेम्पलेट इंजन |
| **लट्टे** | नेट्टे का सुरक्षित टेम्पलेट इंजन |
| **प्लेट्स** | मूल PHP टेम्प्लेट |
---

## प्रमुख पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **घूमना** | HTTP क्लाइंट |
| **सिम्फनी एचटीपीक्लाइंट** | HTTP क्लाइंट |
| **कार्बन** | दिनांक/समय पुस्तकालय |
| **सिम्फनी कंसोल** | सीएलआई ढांचा |
| **मोनोलॉग** | लॉगिंग |
| **लारवेल कतार** | पृष्ठभूमि नौकरियाँ |
| **लारवेल कैशियर** | स्ट्राइप बिलिंग |
| **लारवेल सोशलाइट** | OAuth प्रमाणीकरण |
| **लारवेल सैंक्टम** | एपीआई प्रमाणीकरण |
| **लारवेल होराइजन** | रेडिस कतार डैशबोर्ड |
| **लाइववायर** | जेएस के बिना गतिशील यूआई |
| **जड़ता.जेएस** | एसपीए एडाप्टर (Vue/React + Laravel) |
| **स्पैटी पैकेज** | उच्च गुणवत्ता वाली उपयोगिताएँ |
| **लीग पैकेज** | सामुदायिक पुस्तकालय |
---

## आईडीई और संपादक
| आईडीई | ताकतें |
|----|-----|
| **पीएचपीस्टॉर्म** | सर्वश्रेष्ठ PHP IDE (जेटब्रेन) |
| **वीएस कोड + पीएचपी इंटेलीफेंस** | हल्का, एलएसपी-आधारित |
| **नियोविम + फ़ैक्टर** | टर्मिनल-आधारित |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **PHP-FPM + Nginx** | क्लासिक प्रोडक्शन सेटअप |
| **अपाचे + mod_php** | पारंपरिक |
| **डॉकर** | कंटेनरीकृत (php:fpm-अल्पाइन) |
| **लारवेल फोर्ज** | सर्वर प्रबंधन |
| **लारवेल वाष्प** | AWS लैम्ब्डा परिनियोजन |
| **दूत** | शून्य-डाउनटाइम परिनियोजन |
| **साझा होस्टिंग** | सीपीनल, प्लेस्क |
| **रोडरनर / स्वूले** | लंबे समय से चल रहा PHP |
| **फ्रैंकनपीएचपी** | आधुनिक ऐप सर्वर |
---

## सारांश
PHP के पारिस्थितिकी तंत्र में **लारवेल** (सुरुचिपूर्ण, डेवलपर-अनुकूल) और **सिम्फनी** (उद्यम, घटक) का प्रभुत्व है। मानक स्टैक है: पैकेज के लिए **कंपोजर**, वेब के लिए **लारवेल** या **सिम्फनी**, परीक्षण के लिए **पीएचपीयूनिट** या **पेस्ट**, स्थैतिक विश्लेषण के लिए **पीएचपीस्टेन**, फ़ॉर्मेटिंग के लिए **लारवेल पिंट** या **पीएचपी-सीएस-फिक्सर**, और सर्विंग के लिए **पीएचपी-एफपीएम** या **रोडरनर**। आधुनिक PHP 8.3+ एनम, फ़ाइबर, रीडओनली क्लास और यूनियन प्रकारों के साथ अपनी प्रतिष्ठा से कहीं अधिक सक्षम भाषा है। पारिस्थितिकी तंत्र वेब विकास, सामग्री प्रबंधन (वर्डप्रेस, ड्रूपल), और ई-कॉमर्स (मैजेंटो, वूकॉमर्स) में उत्कृष्टता प्राप्त करता है।