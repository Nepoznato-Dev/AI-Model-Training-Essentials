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

# PHP — 생태계 및 도구 가이드
이 가이드에서는 PHP 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## PHP 런타임
| 런타임 | 메모 |
|---------|---------|
| **PHP-FPM** | FastCGI 프로세스 관리자(가장 일반적) |
| **CLI** | 명령줄 인터페이스 |
| **스울** | 비동기, 코루틴 기반 |
| **로드러너** | 고성능(Go 기반) |
| **프랑켄PHP** | 최신 PHP 앱 서버(Go) |
| **PHP 8.3+** | 열거형, 파이버, 읽기 전용이 있는 현재 안정 |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## 패키지 관리
| 도구 | 목적 |
|------|---------|
| **작곡가** | 종속성 관리자(표준) |
| **패키지스트** | 기본 패키지 저장소 |
| **개인 포장 전문가** | 개인 패키지 호스팅 |
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

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **라라벨** | 풀스택 | 가장 인기 있고 우아한 API |
| **심포니** | 풀스택 | 엔터프라이즈, 구성 요소 |
| **슬림** | 마이크로 | API, 소형 앱 |
| **루멘** | 마이크로(라라벨) | 빠른 마이크로서비스 |
| **케이크PHP** | 풀스택 | 신속한 개발 |
| **코드이그나이터** | 경량 | 간단한 앱 |
| **이이이** | 풀스택 | 성과 중심 |
| **나선형** | 현대 | 장기 런닝, 스울 |
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

## 데이터베이스 및 ORM
| 기술 | 유형 |
|------------|------|
| **웅변** | Laravel의 ORM(활성 레코드) |
| **교리** | Symfony의 ORM(데이터 매퍼) |
| **쿼리 빌더** | 유창한 SQL 빌더 |
| **PDO** | 낮은 수준의 데이터베이스 액세스 |
| **라라벨 마이그레이션** | 스키마 관리 |
| **핑크스** | 독립 실행형 마이그레이션 |
| **이동 경로** | 데이터베이스 마이그레이션 |
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

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **PHP유닛** | 표준 테스트 프레임워크 |
| **해충** | 우아한 테스트(PHPUnit 기반) |
| **라라벨 더스크** | 브라우저 테스트 |
| **조롱** | 모의 프레임워크 |
| **감염** | 돌연변이 테스트 |
| **PHP스탄** | 정적 분석(버그도 포착) |
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

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **PHP스탄** | 정적 분석(레벨 0-9) |
| **시편** | 정적 분석(대체) |
| **라라벨 파인트** | 코드 스타일(Laravel) |
| **PHP-CS-Fixer** | 코드 스타일(일반) |
| **PHPMD** | 혼란 감지 |
| **PHP_CodeSniffer** | 스니핑과 스타일 |
| **총장** | 자동화된 리팩토링 |
| **디프트랙** | 종속성 분석 |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## 템플릿 엔진
| 엔진 | 메모 |
|---------|-------|
| **블레이드** | Laravel의 템플릿 엔진 |
| **나뭇가지** | Symfony의 템플릿 엔진 |
| **라떼** | Nette의 안전한 템플릿 엔진 |
| **접시** | 기본 PHP 템플릿 |
---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **꿀꺽꿀꺽** | HTTP 클라이언트 |
| **심포니 HttpClient** | HTTP 클라이언트 |
| **탄소** | 날짜/시간 라이브러리 |
| **심포니 콘솔** | CLI 프레임워크 |
| **모놀로그** | 로깅 |
| **라라벨 대기열** | 백그라운드 작업 |
| **라라벨 캐셔** | 스트라이프 청구 |
| **라라벨 사교계** | OAuth 인증 |
| **라라벨 성소** | API 인증 |
| **라라벨 호라이즌** | Redis 대기열 대시보드 |
| **라이브와이어** | JS가 없는 동적 UI |
| **Inertia.js** | SPA 어댑터(Vue/React + Laravel) |
| **Spatie 패키지** | 고품질 유틸리티 |
| **리그 패키지** | 커뮤니티 도서관 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **PhpStorm** | 최고의 PHP IDE(JetBrains) |
| **VS 코드 + PHP Intelephense** | 경량, LSP 기반 |
| **Neovim + phpactor** | 터미널 기반 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **PHP-FPM + Nginx** | 클래식 프로덕션 설정 |
| **아파치 + mod_php** | 전통 |
| **도커** | 컨테이너화(php:fpm-alpine) |
| **라라벨 포지** | 서버 관리 |
| **라라벨 증기** | AWS Lambda 배포 |
| **특사** | 다운타임 없는 배포 |
| **공유 호스팅** | c패널, Plesk |
| **로드러너 / 스울** | 장기 실행 PHP |
| **프랑켄PHP** | 최신 앱 서버 |
---

## 요약
PHP의 생태계는 **Laravel**(우아함, 개발자 친화적) 및 **Symfony**(엔터프라이즈, 구성 요소)가 지배합니다. 표준 스택은 패키지용 **Composer**, 웹용 **Laravel** 또는 **Symfony**, 테스트용 **PHPUnit** 또는 **Pest**, 정적 분석용 **PHPStan**, 형식 지정용 **Laravel Pint** 또는 **PHP-CS-Fixer**, 제공용 **PHP-FPM** 또는 **RoadRunner**입니다. 열거형, 파이버, 읽기 전용 클래스 및 공용체 유형을 갖춘 최신 PHP 8.3+는 명성에서 알 수 있는 것보다 훨씬 더 유능한 언어입니다. 생태계는 웹 개발, 콘텐츠 관리(WordPress, Drupal) 및 전자 상거래(Magento, WooCommerce)에 탁월합니다.