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
# Dart — 生態系與工具指南
本指南涵蓋了 Dart 生態系統中的基本工具、框架和基礎設施。
---

## 工具鏈
|工具|目的|
|------|---------|
| **飛鏢** | Dart SDK（編譯器、格式化器、分析器）|
| **顫振** | Flutter SDK（包括 Dart）|
| **酒吧** |套件管理器（內建於 dart 中）|
| **飛鏢分析** |靜態分析|
| **飛鏢格式** |代碼格式化 |
| **dart 編譯** |編譯為原生/JS/WASM |
| **飛鏢跑** |執行 Dart 腳本 |
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

## 套件管理
|工具|目的|
|------|---------|
| **pub.dev** |官方套件儲存庫 |
| **飛鏢酒吧** |包管理器 CLI |
| **pubspec.yaml** |包裹清單 |
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
|技術 |目的|
|------------|---------|
| **顫動** |跨平台UI框架|
| **顫動網路** | Flutter 的 Web 應用程式 |
| **顫動桌面** | Windows、macOS、Linux |
| **顫動移動** | iOS 與 Android |
| **Flutter 嵌入式** |嵌入式裝置|
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

## Web 框架（伺服器端 Dart）
|框架|類型 |最適合 |
|------------|------|----------|
| **貨架** |基於中間件| HTTP 伺服器（最受歡迎）|
| **箭蛙** |全端|後端框架（如 Laravel）|
| **天使** |休息 API |簡單的 API |
| **阿爾弗雷德** |快車樣| Node.js 風格的伺服器 |
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

## 資料庫
|技術 |類型 |
|------------|------|
| **漂移** |型別安全 SQL（取代 Moor）|
| **物件框** | NoSQL 行動資料庫 |
| **伊薩爾** |快速移動資料庫|
| **蜂巢** |輕量級鍵值 |
| **postgres** | PostgreSQL 客戶端 |
| **mysql1** | MySQL 客戶端 |
| **沙發底** | Couchbase 用戶端 |
| **蘇帕巴斯** |後端即服務 |
| **Firebase** |GoogleBaaS |
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

## 測試
|框架|目的|
|------------|---------|
| **測試** |內建測試框架 |
| **模擬** |嘲笑|
| **無酒精雞尾酒** |空安全模擬 |
| **顫振測試** | Flutter 小部件測試 |
| **整合測試** |端對端測試|
| **黃金工具包** |黃金/快照測試 |
| **巡邏** | Flutter 整合測試 |
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

## 程式碼品質
|工具|目的|
|------|---------|
| **飛鏢分析** |內建靜態分析|
| **飛鏢格式** |內建格式化程式|
| **掉毛** |官方 lint 規則 |
| **flutter_lints** | Flutter 專用的 lints |
| **非常好的分析** |嚴格的 lint 規則 |
| **覆蓋範圍** |程式碼覆蓋率|
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

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **飛鏢：核心** |標準庫 |
| **dart：非同步** |期貨、流、非同步 |
| **飛鏢：io** |檔案、HTTP、TCP |
| **飛鏢：轉換** | JSON、UTF-8 |
| **http** | HTTP 用戶端 |
| **迪奧** | HTTP 用戶端 (Flutter) |
| **json_serialized** | JSON 程式碼產生 |
| **冷凍** |不可變資料類 |
| **河莢** |狀態管理|
| **塊/肘** |狀態管理|
| **得到它** |依賴注入 |
| **go_router** |聲明式路由 |
| **可等同** |價值平等|
| **uuid** | UUID 產生 |
| **加密** |密碼學 |
| **路徑** |檔案路徑操作|
| **收藏** |額外的集合類型 |
| **國際** |國際化|
---

## 狀態管理（Flutter）
|解決方案 |類型 |
|----------|------|
| **Riverpod** |編譯安全，可測試|
| **塊/肘** |事件驅動、可預測 |
| **提供者** |內置，簡單|
| **取得X** |多合一（有爭議）|
| **訊號** |反應式基元 |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS Code + Dart** |最佳 Dart/Flutter 支援 |
| **Android Studio + Flutter** |完整的 Flutter IDE |
| **IntelliJ + Dart** | JetBrains 支援 |
---

## 部署
|方法|筆記|
|--------|--------|
| **Dart 編譯** |本機執行檔 |
| **Dart 編譯 js** |編譯為 JavaScript |
| **Dart 編譯 wasm** |編譯為 WebAssembly |
| **顫振建構** |行動/桌面應用程式 |
| **碼頭工人** |容器化伺服器應用程式 |
| **Google雲端運行** |無伺服器容器 |
| **Firebase 託管** | Web 應用程式託管 |
---

＃＃ 概括
Dart 的生態系統以 **Flutter** 為主，用於跨平台 UI 開發。對於伺服器端 Dart，**Shelf** 是標準 HTTP 框架，**Dart Frog** 作為全端選項。標準堆疊是：**Dart 3.4+** 作為運行時，**pub.dev** 用於包，**Flutter** 用於移動/網絡/桌面 UI，**Riverpod** 或​​​​Dart 的優勢在於健全的 null 安全性、快速編譯、熱重載 (Flutter) 以及編譯為原生、JavaScript 或 WebAssembly 的能力。此生態系統非常適合跨平台行動、Web 和桌面應用程式。