---
# Metadata
title: "Dart — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Dart ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [dart, ecosystem, tooling, flutter, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Dart — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Dart.
---

## Chuỗi công cụ
| Công cụ | Mục đích |
|------|----------|
| **phi tiêu** | Dart SDK (trình biên dịch, định dạng, phân tích) |
| **rung rinh** | SDK Flutter (bao gồm Dart) |
| **quán rượu** | Trình quản lý gói (được tích hợp trong phi tiêu) |
| **phân tích phi tiêu** | Phân tích tĩnh |
| **định dạng phi tiêu** | Định dạng mã |
| **biên dịch phi tiêu** | Biên dịch sang bản địa/JS/WASM |
| **chạy phi tiêu** | Chạy tập lệnh Dart |
```bash
dart --version              # check version
dart create myapp           # create project
dart run                    # run project
dart pub get                # install dependencies
dart analyze                # static analysis
dart format .               # format code
dart compile exe bin/app.dart -o app  # compile to native
```

---

## Quản lý gói
| Công cụ | Mục đích |
|------|----------|
| **pub.dev** | Kho gói chính thức |
| **quán rượu phi tiêu** | Quản lý gói CLI |
| **pubspec.yaml** | Bản kê khai gói |
```yaml
# pubspec.yaml
name: myapp
description: A sample Dart application
version: 0.1.0
environment:
  sdk: ^3.4.0

dependencies:
  http: ^1.2.0
  json_annotation: ^4.9.0
  riverpod: ^2.5.0

dev_dependencies:
  test: ^1.25.0
  build_runner: ^2.4.0
  json_serializable: ^6.7.0
  lints: ^4.0.0
```

```bash
dart pub get                # install dependencies
dart pub upgrade            # upgrade packages
dart pub add http           # add dependency
dart pub outdated           # check outdated packages
```

---

## Flutter (Khung giao diện người dùng phi tiêu)
| Công nghệ | Mục đích |
|----------||---------|
| **Rung rinh** | Khung giao diện người dùng đa nền tảng |
| **Web rung** | Ứng dụng web với Flutter |
| **Màn hình rung** | Windows, macOS, Linux |
| **Flutter Mobile** | iOS và Android |
| **Nhúng rung** | Thiết bị nhúng |
```dart
// Flutter widget example
class UserCard extends StatelessWidget {
  final User user;
  const UserCard({super.key, required this.user});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        title: Text(user.name),
        subtitle: Text(user.email),
        trailing: Icon(Icons.arrow_forward),
        onTap: () => Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => UserDetail(user: user)),
        ),
      ),
    );
  }
}
```

---

## Khung web (Phi tiêu phía máy chủ)
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **Kệ** | Dựa trên phần mềm trung gian | Máy chủ HTTP (phổ biến nhất) |
| **Ếch phi tiêu** | Toàn ngăn xếp | Khung phụ trợ (như Laravel) |
| **Thiên thần** | API REST | API đơn giản |
| **Alfred** | Thích thể hiện | Máy chủ kiểu Node.js |
```dart
// Shelf example
import 'package:shelf/shelf.dart';
import 'package:shelf_router/shelf_router.dart';
import 'package:shelf/shelf_io.dart' as io;

void main() async {
  final router = Router();
  
  router.get('/hello', (Request req) => Response.ok('Hello, World!'));
  
  router.get('/users/<id>', (Request req) async {
    final id = req.params['id']!;
    final user = await UserService.findById(int.parse(id));
    return Response.ok(jsonEncode(user));
  });

  var server = await io.serve(router, 'localhost', 8080);
  print('Serving at http://${server.address.host}:${server.port}');
}
```

---

## Cơ sở dữ liệu
| Công nghệ | Loại |
|----------||------|
| **Trôi trôi** | SQL an toàn kiểu (thay thế Moor) |
| **Hộp đối tượng** | Cơ sở dữ liệu di động NoSQL |
| **Isar** | Cơ sở dữ liệu di động nhanh |
| **Tổ ong** | Khóa-giá trị nhẹ |
| **postgres** | Máy khách PostgreSQL |
| **mysql1** | Máy khách MySQL |
| **đế đi văng** | Khách hàng Couchbase |
| **Supabase** | Phần cuối dưới dạng dịch vụ |
| **Căn cứ hỏa lực** | Google BaaS |
```dart
// Drift (type-safe SQL)
class UsersDao extends DatabaseAccessor<AppDatabase> with _$UsersDaoMixin {
  UsersDao(AppDatabase db) : super(db);

  Future<List<User>> findAll() => select(users).get();
  
  Future<User> findById(int id) =>
    (select(users)..where((t) => t.id.equals(id)))
      .getSingle();
  
  Stream<List<User>> watchAll() => select(users).watch();
}
```

---

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **kiểm tra** | Khung kiểm tra tích hợp |
| **giả vờ** | Chế giễu |
| **mocktail** | Chế nhạo không an toàn |
| **flutter_test** | Kiểm tra widget Flutter |
| **kiểm tra tích hợp** | Thử nghiệm từ đầu đến cuối |
| **bộ công cụ vàng** | Kiểm tra vàng/chụp nhanh |
| **tuần tra** | Thử nghiệm tích hợp Flutter |
```dart
import 'package:test/test.dart';

void main() {
  group('UserService', () {
    late UserService service;
    late MockUserRepository mockRepo;

    setUp(() {
      mockRepo = MockUserRepository();
      service = UserService(mockRepo);
    });

    test('finds user by id', () async {
      when(mockRepo.findById(1)).thenAnswer((_) async => User(1, 'Alice'));

      final user = await service.findById(1);

      expect(user.name, equals('Alice'));
      verify(mockRepo.findById(1)).called(1);
    });

    test('throws when user not found', () async {
      when(mockRepo.findById(any)).thenThrow(NotFoundException());

      expect(() => service.findById(999), throwsA(isA<NotFoundException>()));
    });
  });
}
```

---

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **phân tích phi tiêu** | Phân tích tĩnh tích hợp |
| **định dạng phi tiêu** | Trình định dạng tích hợp |
| **lint** | Quy tắc lint chính thức |
| **flutter_lint** | Lint dành riêng cho rung động |
| **phân tích rất tốt** | Quy tắc lint nghiêm ngặt |
| **phạm vi bảo hiểm** | Bảo hiểm mã |
```yaml
# analysis_options.yaml
include: package:lints/recommended.yaml

linter:
  rules:
    - prefer_final_locals
    - prefer_const_constructors
    - avoid_dynamic_calls
    - always_declare_return_types

analyzer:
  errors:
    missing_return: error
    dead_code: warning
```

---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **phi tiêu:lõi** | Thư viện chuẩn |
| **phi tiêu:không đồng bộ** | Tương lai, Luồng, không đồng bộ |
| **phi tiêu:io** | Tệp, HTTP, TCP |
| **phi tiêu:chuyển đổi** | JSON, UTF-8 |
| **http** | Máy khách HTTP |
| **dio** | Máy khách HTTP (Flutter) |
| **json_serializable** | Tạo mã JSON |
| **đóng băng** | Lớp dữ liệu bất biến |
| **riverpod** | Quản lý nhà nước |
| **khối / cubit** | Quản lý nhà nước |
| **lấy_nó** | Tiêm phụ thuộc |
| **go_router** | Định tuyến khai báo |
| **tương đương** | Giá trị bình đẳng |
| **uuid** | Tạo UUID |
| **tiền điện tử** | Mật mã |
| **đường dẫn** | Thao tác đường dẫn tệp |
| **bộ sưu tập** | Các loại bộ sưu tập bổ sung |
| **quốc tế** | Quốc tế hóa |
---

## Quản lý nhà nước (Flutter)
| Giải pháp | Loại |
|----------|------|
| **Riverpod** | Biên dịch an toàn, có thể kiểm tra |
| **Khối / Cubit** | Theo hướng sự kiện, có thể dự đoán được |
| **Nhà cung cấp** | Tích hợp, đơn giản |
| **GetX** | Tất cả trong một (gây tranh cãi) |
| **Tín hiệu** | Nguyên thủy phản ứng |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Mã VS + Phi tiêu** | Hỗ trợ Dart/Flutter tốt nhất |
| **Studio Android + Flutter** | IDE rung đầy đủ |
| **IntelliJ + Phi tiêu** | Hỗ trợ JetBrains |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Biên dịch phi tiêu** | Tệp thực thi gốc |
| **Dart biên dịch js** | Biên dịch sang JavaScript |
| **Biên dịch phi tiêu wasm** | Biên dịch sang WebAssembly |
| **Xây dựng rung** | Ứng dụng dành cho thiết bị di động/máy tính để bàn |
| **Docker** | Ứng dụng máy chủ được đóng gói |
| **Chạy trên nền tảng đám mây của Google** | Thùng chứa không có máy chủ |
| **Dịch vụ lưu trữ Firebase** | Lưu trữ ứng dụng web |
---

## Bản tóm tắt
Hệ sinh thái của Dart bị thống trị bởi **Flutter** để phát triển giao diện người dùng đa nền tảng. Đối với Dart phía máy chủ, **Shelf** là khung HTTP tiêu chuẩn, với **Dart Frog** là tùy chọn toàn bộ ngăn xếp. Ngăn xếp tiêu chuẩn là: **Dart 3.4+** làm thời gian chạy, **pub.dev** cho các gói, **Flutter** cho giao diện người dùng trên thiết bị di động/web/máy tính để bàn, **Riverpod** hoặc **Bloc** để quản lý trạng thái, **Drift** cho cơ sở dữ liệu, **test** cho thử nghiệm và **phân tích phi tiêu** cho linting. Điểm mạnh của Dart là âm thanh an toàn, biên dịch nhanh, tải lại nóng (Flutter) và khả năng biên dịch sang ngôn ngữ gốc, JavaScript hoặc WebAssembly. Hệ sinh thái này lý tưởng cho các ứng dụng di động, web và máy tính để bàn đa nền tảng.