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
# PHP — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы PHP.
---

## Среды выполнения PHP
| Время выполнения | Заметки |
|---------|-------|
| **PHP-FPM** | Менеджер процессов FastCGI (наиболее распространенный) |
| **CLI** | Интерфейс командной строки |
| **Сулл** | Асинхронный, на основе сопрограмм |
| **РоудРаннер** | Высокая производительность (на основе Go) |
| **ФранкенPHP** | Современный сервер приложений PHP (Go) |
| **PHP 8.3+** | Текущая стабильная версия с перечислениями, волокнами, только для чтения |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Управление пакетами
| Инструмент | Цель |
|------|---------|
| **Композитор** | Менеджер зависимостей (стандарт) |
| **Упаковщик** | Репозиторий пакетов по умолчанию |
| **Частный упаковщик** | Хостинг частных пакетов |
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

## Веб-фреймворки
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **Ларавель** | Полный стек | Самый популярный и элегантный API |
| **Симфония** | Полный стек | Предприятие, комплектующие |
| **Тонкий** | Микро | API, небольшие приложения |
| **Люмен** | Микро (Laravel) | Быстрые микросервисы |
| **CakePHP** | Полный стек | Быстрое развитие |
| **КодИгнитер** | Легкий | Простые приложения |
| **Юии** | Полный стек | Ориентированность на производительность |
| **Спираль** | Современный | Долгосрочный, Свул |
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

## База данных и ORM
| Технология | Тип |
|------------|------|
| **Красноречивое** | ORM Laravel (активная запись) |
| **Доктрина** | ORM Symfony (сопоставитель данных) |
| **Конструктор запросов** | Свободный конструктор SQL |
| **ПДО** | Низкоуровневый доступ к базе данных |
| **Миграция Laravel** | Управление схемой |
| **Финкс** | Автономные миграции |
| **Пролетный путь** | Миграция базы данных |
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

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **PHPUUnit** | Стандартная среда тестирования |
| **Пешт** | Элегантное тестирование (построенное на PHPUnit) |
| **Ларавель Даск** | Тестирование браузера |
| **Издевательство** | Издевательская структура |
| **Инфекция** | Мутационное тестирование |
| **PHPStan** | Статический анализ (также выявляет ошибки) |
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

## Качество кода
| Инструмент | Цель |
|------|---------|
| **PHPStan** | Статический анализ (уровни 0–9) |
| **Псалом** | Статический анализ (альтернативный вариант) |
| **Пинта Laravel** | Стиль кода (Laravel) |
| **PHP-CS-Fixer** | Стиль кода (общий) |
| **ПХПМД** | Обнаружение беспорядка |
| **PHP_CodeSniffer** | Нюхание и стиль |
| **Ректор** | Автоматический рефакторинг |
| **Дептрак** | Анализ зависимостей |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Шаблонизаторы
| Двигатель | Заметки |
|--------|-------|
| **Лезвие** | Шаблонизатор Laravel |
| **Ветка** | Шаблонизатор Symfony |
| **Латте** | Безопасный шаблонизатор Nette |
| **Тарелки** | Собственные шаблоны PHP |
---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **Жрать** | HTTP-клиент |
| **Symfony HttpClient** | HTTP-клиент |
| **Углерод** | Библиотека даты/времени |
| **Консоль Symfony** | CLI-фреймворк |
| **Монолог** | Ведение журнала |
| **Очередь Laravel** | Фоновые вакансии |
| **Кассир в Laravel** | Полоса биллинга |
| **Laravel Socialite** | Аутентификация OAuth |
| **Святилище Laravel** | Аутентификация API |
| **Горизонт Laravel** | Панель управления очередью Redis |
| **Живой провод** | Динамический интерфейс без JS |
| **Инерция.js** | SPA-адаптер (Vue/React + Laravel) |
| **Пакеты спа** | Качественные коммунальные услуги |
| **Пакеты лиги** | Общественные библиотеки |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **PhpStorm** | Лучшая PHP IDE (JetBrains) |
| **VS Code + PHP Intelephense** | Легкий, на основе LSP |
| **Неовим + phpactor** | На базе терминала |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **PHP-FPM + Nginx** | Классическая производственная установка |
| **Apache + mod_php** | Традиционный |
| **Докер** | Контейнерный (php:fpm-alpine) |
| **Ларавель Фордж** | Управление сервером |
| **Laravel Vapor** | Развертывание AWS Lambda |
| **Посланник** | Развертывание с нулевым временем простоя |
| **Общий хостинг** | cPanel, Плеск |
| **RoadRunner / Свул** | Долго работающий PHP |
| **ФранкенPHP** | Современный сервер приложений |
---

## Краткое содержание
В экосистеме PHP доминируют **Laravel** (элегантный, удобный для разработчиков) и **Symfony** (корпоративный, компоненты). Стандартный стек: **Composer** для пакетов, **Laravel** или **Symfony** для Интернета, **PHPUnit** или **Pest** для тестирования, **PHPStan** для статического анализа, **Laravel Pint** или **PHP-CS-Fixer** для форматирования и **PHP-FPM** или **RoadRunner** для обслуживания. Современный PHP 8.3+ с перечислениями, волокнами, классами только для чтения и типами объединения — гораздо более функциональный язык, чем предполагает его репутация. Экосистема превосходна в веб-разработке, управлении контентом (WordPress, Drupal) и электронной коммерции (Magento, WooCommerce).