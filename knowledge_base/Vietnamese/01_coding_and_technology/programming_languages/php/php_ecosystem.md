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
# PHP — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái PHP.
---

## Thời gian chạy PHP
| Thời gian chạy | Ghi chú |
|----------|-------|
| **PHP-FPM** | Trình quản lý quy trình FastCGI (phổ biến nhất) |
| **CLI** | Giao diện dòng lệnh |
| **Đổ mồ hôi** | Không đồng bộ, dựa trên coroutine |
| **RoadRunner** | Hiệu suất cao (dựa trên Go) |
| **FrankenPHP** | Máy chủ ứng dụng PHP hiện đại (Go) |
| **PHP 8.3+** | Hiện tại ổn định với enum, sợi, chỉ đọc |
```bash
php -v                    # check version
php -S localhost:8000     # built-in dev server
php artisan serve         # Laravel dev server
php -r 'echo "Hello\n";'  # inline execution
```

---

## Quản lý gói
| Công cụ | Mục đích |
|------|----------|
| **Nhà soạn nhạc** | Người quản lý phụ thuộc (tiêu chuẩn) |
| **Người đóng gói** | Kho lưu trữ gói mặc định |
| **Nhà đóng gói riêng** | Lưu trữ gói riêng |
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

## Khung web
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **Laravel** | Toàn ngăn xếp | API thanh lịch, phổ biến nhất |
| **Symfony** | Toàn ngăn xếp | Doanh nghiệp, linh kiện |
| **Mỏng** | Vi mô | API, ứng dụng nhỏ |
| **Lumen** | Micro (Laravel) | Dịch vụ vi mô nhanh |
| **BánhPHP** | Toàn ngăn xếp | Phát triển nhanh chóng |
| **CodeIgniter** | Nhẹ | Ứng dụng đơn giản |
| **Yi** | Toàn ngăn xếp | Tập trung vào hiệu suất |
| **xoắn ốc** | Hiện đại | Chạy dài, Swoole |
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

## Cơ sở dữ liệu & ORM
| Công nghệ | Loại |
|----------||------|
| **Hùng hồn** | ORM của Laravel (Bản ghi hoạt động) |
| **Học thuyết** | ORM của Symfony (Trình ánh xạ dữ liệu) |
| **Trình tạo truy vấn** | Trình tạo SQL thông thạo |
| **PDO** | Truy cập cơ sở dữ liệu cấp thấp |
| **Di chuyển Laravel** | Quản lý lược đồ |
| **Phinx** | Di chuyển độc lập |
| **Đường bay** | Di chuyển cơ sở dữ liệu |
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

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **PHPUnit** | Khung kiểm tra tiêu chuẩn |
| **Sâu bệnh** | Thử nghiệm tao nhã (được xây dựng trên PHPUnit) |
| **Chạng vạng Laravel** | Kiểm tra trình duyệt |
| **Chế nhạo** | Khung mô phỏng |
| **Nhiễm trùng** | Thử nghiệm đột biến |
| **PHPStan** | Phân tích tĩnh (cũng phát hiện lỗi) |
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

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **PHPStan** | Phân tích tĩnh (cấp 0-9) |
| **Thánh vịnh** | Phân tích tĩnh (thay thế) |
| **Pint Laravel** | Kiểu mã (Laravel) |
| **Trình sửa lỗi PHP-CS** | Kiểu mã (chung) |
| **PHPMD** | Phát hiện lộn xộn |
| **PHP_CodeSniffer** | Đánh hơi và phong cách |
| **Hiệu trưởng** | Tái cấu trúc tự động |
| **Deptrac** | Phân tích phụ thuộc |
```bash
vendor/bin/phpstan analyse app --level=6
vendor/bin/pint                    # fix code style
vendor/bin/phpunit                 # run tests
vendor/bin/rector process src      # auto-refactor
```

---

## Công cụ tạo mẫu
| Động cơ | Ghi chú |
|--------|-------|
| **Lưỡi** | Công cụ tạo mẫu của Laravel |
| **Cành cây** | Công cụ tạo mẫu của Symfony |
| **Latte** | Công cụ tạo mẫu an toàn của Nette |
| **Đĩa** | Mẫu PHP gốc |
---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **Ngốc** | Máy khách HTTP |
| **Symfony HttpClient** | Máy khách HTTP |
| **Cacbon** | Thư viện ngày/giờ |
| **Bảng điều khiển Symfony** | Khung CLI |
| **Độc thoại** | Ghi nhật ký |
| **Hàng đợi Laravel** | Công việc nền tảng |
| **Nhân viên thu ngân Laravel** | Thanh toán sọc |
| **Laravel Socialite** | Xác thực OAuth |
| **Thánh đường Laravel** | Xác thực API |
| **Chân trời Laravel** | Bảng điều khiển hàng đợi Redis |
| **Dây trực tiếp** | Giao diện người dùng động không có JS |
| ** Quán tính.js ** | Bộ chuyển đổi SPA (Vue/React + Laravel) |
| **Gói không gian** | Tiện ích chất lượng cao |
| **Gói giải đấu** | Thư viện cộng đồng |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **PhpStorm** | IDE PHP tốt nhất (JetBrains) |
| **Mã VS + PHP Intelephense** | Nhẹ, dựa trên LSP |
| **Nevim + phpactor** | Dựa trên thiết bị đầu cuối |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **PHP-FPM + Nginx** | Thiết lập sản xuất cổ điển |
| **Apache + mod_php** | Truyền thống |
| **Docker** | Được đóng gói (php:fpm-alpine) |
| **Lò rèn Laravel** | Quản lý máy chủ |
| **Hơi Laravel** | Triển khai AWS Lambda |
| **Sứ giả** | Triển khai không có thời gian ngừng hoạt động |
| **Lưu trữ chia sẻ** | cPanel, Plesk |
| **RoadRunner / Swoole** | PHP chạy dài |
| **FrankenPHP** | Máy chủ ứng dụng hiện đại |
---

## Bản tóm tắt
Hệ sinh thái của PHP bị chi phối bởi **Laravel** (thanh lịch, thân thiện với nhà phát triển) và **Symfony** (doanh nghiệp, thành phần). Ngăn xếp tiêu chuẩn là: **Composer** cho các gói, **Laravel** hoặc **Symfony** cho web, **PHPUnit** hoặc **Pest** để thử nghiệm, **PHPStan** để phân tích tĩnh, **Laravel Pint** hoặc **PHP-CS-Fixer** để định dạng và **PHP-FPM** hoặc **RoadRunner** để phân phối. PHP 8.3+ hiện đại với các enum, các sợi, các lớp chỉ đọc và các kiểu kết hợp là một ngôn ngữ có nhiều khả năng hơn so với danh tiếng của nó. Hệ sinh thái vượt trội về phát triển web, quản lý nội dung (WordPress, Drupal) và thương mại điện tử (Magento, WooC Commerce).