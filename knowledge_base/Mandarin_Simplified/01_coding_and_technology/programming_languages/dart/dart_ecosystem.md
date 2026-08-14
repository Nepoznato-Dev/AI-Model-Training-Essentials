<!--
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

-->
# Dart — 生态系统和工具指南
本指南涵盖了 Dart 生态系统中的基本工具、框架和基础设施。
---

## 工具链
|工具|目的|
|------|---------|
| **飞镖** | Dart SDK（编译器、格式化器、分析器）|
| **颤振** | Flutter SDK（包括 Dart）|
| **酒吧** |包管理器（内置于 dart 中）|
| **飞镖分析** |静态分析|
| **飞镖格式** |代码格式化 |
| **dart 编译** |编译为原生/JS/WASM |
| **飞镖跑** |运行 Dart 脚本 |
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

## 包管理
|工具|目的|
|------|---------|
| **pub.dev** |官方包存储库 |
| **飞镖酒吧** |包管理器 CLI |
| **pubspec.yaml** |包裹清单 |
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

## Flutter（Dart UI 框架）
|技术 |目的|
|------------|---------|
| **颤动** |跨平台UI框架|
| **颤动网络** | Flutter 的 Web 应用程序 |
| **颤动桌面** | Windows、macOS、Linux |
| **颤动移动** | iOS 和 Android |
| **Flutter 嵌入式** |嵌入式设备|
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

## Web 框架（服务器端 Dart）
|框架|类型 |最适合 |
|------------|------|----------|
| **货架** |基于中间件| HTTP 服务器（最流行）|
| **箭蛙** |全栈|后端框架（如 Laravel）|
| **天使** |休息 API |简单的 API |
| **阿尔弗雷德** |快车样| Node.js 风格的服务器 |
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

＃＃ 数据库
|技术 |类型 |
|------------|------|
| **漂移** |类型安全 SQL（取代 Moor）|
| **对象框** | NoSQL 移动数据库 |
| **伊萨尔** |快速移动数据库|
| **蜂巢** |轻量级键值 |
| **postgres** | PostgreSQL 客户端 |
| **mysql1** | MySQL 客户端 |
| **沙发底** | Couchbase 客户端 |
| **苏帕巴斯** |后端即服务 |
| **Firebase** |谷歌BaaS |
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

## 测试
|框架|目的|
|------------|---------|
| **测试** |内置测试框架 |
| **模拟** |嘲笑|
| **无酒精鸡尾酒** |空安全模拟 |
| **颤振测试** | Flutter 小部件测试 |
| **集成测试** |端到端测试|
| **黄金工具包** |黄金/快照测试 |
| **巡逻** | Flutter 集成测试 |
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

## 代码质量
|工具|目的|
|------|---------|
| **飞镖分析** |内置静态分析|
| **飞镖格式** |内置格式化程序|
| **掉毛** |官方 lint 规则 |
| **flutter_lints** | Flutter 专用的 lints |
| **非常好的分析** |严格的 lint 规则 |
| **覆盖范围** |代码覆盖率|
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

## 关键库
|图书馆 |目的|
|---------|---------|
| **飞镖：核心** |标准库 |
| **dart：异步** |期货、流、异步 |
| **飞镖：io** |文件、HTTP、TCP |
| **飞镖：转换** | JSON、UTF-8 |
| **http** | HTTP 客户端 |
| **迪奥** | HTTP 客户端 (Flutter) |
| **json_serialized** | JSON 代码生成 |
| **冷冻** |不可变数据类 |
| **河荚** |状态管理|
| **块/肘** |状态管理|
| **得到它** |依赖注入 |
| **go_router** |声明式路由 |
| **可等同** |价值平等|
| **uuid** | UUID 生成 |
| **加密** |密码学 |
| **路径** |文件路径操作|
| **收藏** |额外的集合类型 |
| **国际** |国际化|
---

## 状态管理（Flutter）
|解决方案 |类型 |
|----------|------|
| **Riverpod** |编译安全，可测试|
| **块/肘** |事件驱动、可预测 |
| **提供商** |内置，简单|
| **获取X** |多合一（有争议）|
| **信号** |反应式基元 |
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **VS Code + Dart** |最佳 Dart/Flutter 支持 |
| **Android Studio + Flutter** |完整的 Flutter IDE |
| **IntelliJ + Dart** | JetBrains 支持 |
---

## 部署
|方法|笔记|
|--------|--------|
| **Dart 编译** |本机可执行文件 |
| **Dart 编译 js** |编译为 JavaScript |
| **Dart 编译 wasm** |编译为 WebAssembly |
| **颤振构建** |移动/桌面应用程序 |
| **码头工人** |容器化服务器应用程序 |
| **谷歌云运行** |无服务器容器 |
| **Firebase 托管** | Web 应用程序托管 |
---

＃＃ 概括
Dart 的生态系统以 **Flutter** 为主，用于跨平台 UI 开发。对于服务器端 Dart，**Shelf** 是标准 HTTP 框架，**Dart Frog** 作为全栈选项。标准堆栈是：**Dart 3.4+** 作为运行时，**pub.dev** 用于包，**Flutter** 用于移动/网络/桌面 UI，**Riverpod** 或​​ **Bloc** 用于状态管理，**Drift** 用于数据库，**test** 用于测试，以及 **dartanalyze** 用于 linting。 Dart 的优势在于健全的 null 安全性、快速编译、热重载 (Flutter) 以及编译为原生、JavaScript 或 WebAssembly 的能力。该生态系统非常适合跨平台移动、Web 和桌面应用程序。