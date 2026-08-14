---
# Metadata
title: "Dart"
description: "Comprehensive reference for the Dart programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [dart, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "40 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 飞镖
Dart 是 Google 开发的客户端优化编程语言，于 2013 年首次发布。虽然 Dart 最初被定位为 Web 浏览器的潜在 JavaScript 替代品，但它发现其主要目的是作为 **Flutter** 背后的语言 - Google 的跨平台 UI 工具包，用于从单个代码库构建移动、Web、桌面和嵌入式应用程序。
Dart 结合了现代语言的最佳功能：它是面向对象的，具有可选类型（自 Dart 3 以来健全的 null 安全性），支持使用`async`/`await`进行异步编程，并编译为本机机器代码（用于移动/桌面）和 JavaScript（用于 Web）。
---

## 为什么 Dart 很重要
- **Flutter**：Flutter 的主要语言 - 增长最快的跨平台框架之一。
- **跨平台**：适用于 iOS、Android、Web、Windows、macOS、Linux 和嵌入式设备的单一代码库。
- **高效**：热重载、丰富的小部件库和富有表现力的语法使 UI 开发变得快速。
- **健全的空安全性**：编译时空安全性消除了空引用错误。
- **性能**：编译为移动设备的本机 ARM 代码；不需要桥梁。
- **不断增长的生态系统**：Flutter 的包生态系统正在迅速扩张。
## 权衡
|限制|详情 |典型解决方法|
|------------|---------|--------------------|
| **以颤振为中心** | Dart 使用最多的是 Flutter；限制在它之外|用于颤振；用于非 UI 工作的其他语言 |
| **较小的生态系统** |比 React Native 或本机平台更少的包 |成长迅速；原生 API 的平台渠道 |
| **网络性能** | Dart 编译为 WASM 仍在成熟 |使用 CanvasKit 渲染器获得一致的性能 |
| **就业市场** | Flutter 角色存在，但少于原生移动 |跨平台开发人员的需求不断增长|
| **不适用于后端** |可能（服务器端 Dart）但不是用例 |使用 Go、Node.js、Python 作为后端 |
---

## 语法基础知识
```dart
// Variables
var name = 'Alice';          // Type inferred
String city = 'London';      // Explicit type
final age = 30;              // Immutable
const pi = 3.14159;          // Compile-time constant

// Null safety
String? nickname;            // Nullable type
nickname = null;             // OK
// String forced = null;     // Compile error!

// Null-aware operators
String display = nickname ?? 'Anonymous';  // Default if null
int? length = nickname?.length;             // Safe navigation

// Functions
String greet(String name, [String greeting = 'Hello']) {
  return '$greeting, $name!';
}

// Arrow functions
int add(int a, int b) => a + b;

// Classes
class Animal {
  final String name;
  Animal(this.name);
  
  String speak() => '$name makes a sound';
}

class Dog extends Animal {
  Dog(super.name);
  
  @override
  String speak() => '$name says woof';
}

// Async/await
Future<String> fetchData() async {
  await Future.delayed(Duration(seconds: 1));
  return 'Data loaded';
}

// Collections
var numbers = [1, 2, 3, 4, 5];
var doubled = numbers.map((n) => n * 2).toList();
var evens = numbers.where((n) => n % 2 == 0).toList();

// Flutter widget (simplified)
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Hello Dart')),
        body: Center(child: Text('Welcome!')),
      ),
    );
  }
}
```
---

## 高级语法和模式
### 零安全 — 深入探讨
```dart
// Sound null safety: all types are non-nullable by default
String name = 'Alice';     // Cannot be null
String? nickname;           // Explicitly nullable

// Null assertion operator (!) — tells compiler "I know this is not null"
String getNickname() {
  String? cached = _cache;
  return cached!;  // Throws if cached is null
}

// Late initialization
class Config {
  late final String apiUrl;  // Initialized after construction, but before use
  
  void initialize() {
    apiUrl = 'https://api.example.com';
  }
}

// Null-aware cascade
class User {
  String? email;
  String? phone;
}

void updateContact(User user) {
  user..email = 'alice@mail.com'
      ..phone = '+1234567890';
}

// Required named parameters with null safety
class ApiResponse<T> {
  final T? data;
  final String? error;
  final int statusCode;

  ApiResponse.success(this.data, this.statusCode) : error = null;
  ApiResponse.failure(this.error, this.statusCode) : data = null;

  bool get isSuccess => error == null;
}
```

### 混合
```dart
// Mixins: share code between classes without inheritance
mixin Loggable on Object {
  void log(String message) {
    print('[${runtimeType}] $message');
  }
}

mixin Serializable {
  Map<String, dynamic> toJson();
  
  String toJsonString() => jsonEncode(toJson());
}

// Use mixins with 'with' keyword
class UserModel with Loggable, Serializable {
  final String name;
  final String email;

  UserModel(this.name, this.email);

  void updateEmail(String newEmail) {
    log('Updating email from $email to $newEmail');
    // update logic...
  }

  @override
  Map<String, dynamic> toJson() => {'name': name, 'email': email};
}

final user = UserModel('Alice', 'alice@mail.com');
user.log('User created');  // [UserModel] User created
print(user.toJsonString()); // {"name":"Alice","email":"alice@mail.com"}
```

### 扩展
```dart
// Extend existing types with new functionality
extension StringExtensions on String {
  String get capitalize =>
      isEmpty ? this : '${this[0].toUpperCase()}${substring(1)}';

  String get initials =>
      split(' ').map((w) => w.isNotEmpty ? w[0] : '').join();

  bool get isValidEmail =>
      RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,}$').hasMatch(this);

  String truncate(int maxLength) =>
      length <= maxLength ? this : '${substring(0, maxLength)}...';
}

print('hello world'.capitalize);  // Hello world
print('John Doe'.initials);       // JD
print('test@mail.com'.isValidEmail); // true
print('A very long string'.truncate(10)); // A very lo...

// Extension on DateTime
extension DateTimeExtensions on DateTime {
  bool get isToday => DateUtils.isSameDay(this, DateTime.now());
  
  String get relative {
    final diff = DateTime.now().difference(this);
    if (diff.inSeconds < 60) return 'just now';
    if (diff.inMinutes < 60) return '${diff.inMinutes}m ago';
    if (diff.inHours < 24) return '${diff.inHours}h ago';
    return '${diff.inDays}d ago';
  }
}
```

### 隔离（并发）
```dart
import 'dart:isolate';

// Isolates are separate threads with their own memory heap
// Use for CPU-intensive work to avoid blocking the UI

// Top-level or static function required for isolate entry point
int fibonacci(int n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

// Using compute() for simple isolate tasks (Flutter)
Future<void> heavyComputation() async {
  // Runs fibonacci(45) in a separate isolate
  final result = await compute(fibonacci, 45);
  print('Result: $result');
}

// Manual isolate communication with SendPort/ReceivePort
Future<int> runInIsolate(int value) async {
  final receivePort = ReceivePort();
  
  await Isolate.spawn((SendPort sendPort) {
    final result = fibonacci(value);
    sendPort.send(result);
  }, receivePort.sendPort);

  return await receivePort.first as int;
}
```
### 注释和代码生成
```dart
// Built-in annotations
@deprecated
void oldMethod() {}

@override
String toString() => 'Custom';

// Custom annotations (metadata)
class Deprecated {
  final String message;
  const Deprecated(this.message);
}

@Deprecated('Use newMethod() instead')
void oldMethod() {}

// Code generation with build_runner
// pubspec.yaml dependencies:
// dev_dependencies:
//   build_runner: ^2.4.0
//   json_serializable: ^6.0.0
//   freezed: ^2.0.0

// Using freezed for immutable data classes
// Run: dart run build_runner build
import 'package:freezed_annotation/freezed_annotation.dart';
part 'user.freezed.dart';

@freezed
class User with _$User {
  const factory User({
    required String id,
    required String name,
    required String email,
    @Default(false) bool isActive,
  }) = _User;

  factory User.fromJson(Map<String, dynamic> json) =>
      _$UserFromJson(json);
}

// Usage
final user = User(id: '1', name: 'Alice', email: 'alice@mail.com');
final json = user.toJson();
final copy = user.copyWith(isActive: true);
```

---

## 深入探讨核心功能
### 流处理
```dart
// Streams: sequences of asynchronous events
// SingleEvent: Future  |  MultipleEvents: Stream

// Creating streams
Stream<int> countStream(int max) async* {
  for (int i = 0; i < max; i++) {
    await Future.delayed(Duration(seconds: 1));
    yield i;
  }
}

// Consuming streams
void main() async {
  // await for
  await for (final value in countStream(5)) {
    print('Count: $value');
  }

  // Stream transformers
  final subscription = countStream(100)
      .where((n) => n % 2 == 0)
      .map((n) => n * n)
      .take(5)
      .listen(
        (value) => print('Received: $value'),
        onError: (error) => print('Error: $error'),
        onDone: () => print('Done!'),
      );
}

// StreamController for manual stream management
class SearchService {
  final _controller = StreamController<String>.broadcast();
  
  Stream<String> get searchTerms => _controller.stream;
  
  void onSearch(String term) {
    _controller.add(term);
  }
  
  void dispose() {
    _controller.close();
  }
}

// StreamBuilder in Flutter
class SearchWidget extends StatelessWidget {
  final SearchService service;
  
  const SearchWidget(this.service);

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<String>(
      stream: service.searchTerms,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Text('Searching: ${snapshot.data}');
        }
        return Text('Type to search...');
      },
    );
  }
}
```

### Flutter Widget 模式
```dart
// Stateful widget with lifecycle
class CounterWidget extends StatefulWidget {
  final int initialValue;
  const CounterWidget({super.key, this.initialValue = 0});

  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget>
    with SingleTickerProviderStateMixin {
  late int _count;
  late AnimationController _animController;

  @override
  void initState() {
    super.initState();
    _count = widget.initialValue;
    _animController = AnimationController(
      duration: const Duration(milliseconds: 300),
      vsync: this,
    );
  }

  @override
  void didUpdateWidget(CounterWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.initialValue != widget.initialValue) {
      _count = widget.initialValue;
    }
  }

  @override
  void dispose() {
    _animController.dispose();
    super.dispose();
  }

  void _increment() {
    setState(() => _count++);
    _animController.forward(from: 0.0);
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        AnimatedBuilder(
          animation: _animController,
          builder: (context, child) {
            final scale = 1.0 + (_animController.value * 0.1);
            return Transform.scale(scale: scale, child: child);
          },
          child: Text('Count: $_count', style: Theme.of(context).textTheme.headlineMedium),
        ),
        ElevatedButton(onPressed: _increment, child: const Text('Increment')),
      ],
    );
  }
}

// InheritedWidget for dependency injection
class AppTheme extends InheritedWidget {
  final Color primaryColor;
  final Color backgroundColor;

  const AppTheme({
    required this.primaryColor,
    required this.backgroundColor,
    required super.child,
    super.key,
  });

  static AppTheme of(BuildContext context) {
    final widget = context.dependOnInheritedWidgetOfExactType<AppTheme>();
    assert(widget != null, 'No AppTheme found in context');
    return widget!;
  }

  @override
  bool updateShouldNotify(AppTheme oldWidget) =>
      primaryColor != oldWidget.primaryColor ||
      backgroundColor != oldWidget.backgroundColor;
}
```
---

## 项目配置和构建系统
### pubspec.yaml
```yaml
# pubspec.yaml - Dart/Flutter project configuration
name: my_app
description: A cross-platform Flutter application.
version: 1.0.0+1
publish_to: none

environment:
  sdk: '>=3.0.0 <4.0.0'
  flutter: ">=3.10.0"

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.6
  http: ^1.1.0
  provider: ^6.1.1
  shared_preferences: ^2.2.2
  json_annotation: ^4.8.1

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0
  build_runner: ^2.4.7
  json_serializable: ^6.7.1
  freezed: ^2.4.5
  mockito: ^5.4.3

flutter:
  uses-material-design: true
  
  assets:
    - assets/images/
    - assets/icons/
    - assets/fonts/
    
  fonts:
    - family: CustomFont
      fonts:
        - asset: assets/fonts/CustomFont-Regular.ttf
        - asset: assets/fonts/CustomFont-Bold.ttf
          weight: 700
```

###analysis_options.yaml
```yaml
# analysis_options.yaml - Linting and analysis configuration
include: package:flutter_lints/flutter.yaml

analyzer:
  exclude:
    - "**/*.g.dart"
    - "**/*.freezed.dart"
  errors:
    invalid_annotation_target: ignore

linter:
  rules:
    - always_declare_return_types
    - annotate_overrides
    - avoid_empty_else
    - avoid_print
    - avoid_relative_lib_imports
    - avoid_returning_null_for_void
    - avoid_unused_constructor_parameters
    - cancel_subscriptions
    - prefer_const_constructors
    - prefer_final_fields
    - prefer_single_quotes
    - sort_child_properties_last
    - unawaited_futures
    - unnecessary_brace_in_string_interps
```
---

## 测试
### 使用测试包进行单元测试
```dart
// test/calculator_test.dart
import 'package:test/test.dart';
import 'package:my_app/calculator.dart';

void main() {
  group('Calculator', () {
    late Calculator calc;

    setUp(() {
      calc = Calculator();
    });

    test('adds two numbers correctly', () {
      expect(calc.add(2, 3), equals(5));
      expect(calc.add(-1, 1), equals(0));
      expect(calc.add(0, 0), equals(0));
    });

    test('throws on division by zero', () {
      expect(() => calc.divide(10, 0), throwsA(isA<ArgumentError>()));
    });

    test('handles large numbers', () {
      expect(calc.add(999999, 1), equals(1000000));
    }, tags: 'slow');
  });
}
```

### 使用 flutter_test 进行小部件测试
```dart
// test/widget/counter_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:my_app/widgets/counter_widget.dart';

void main() {
  testWidgets('Counter increments when button is pressed', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: CounterWidget(initialValue: 0),
    ));

    // Verify initial state
    expect(find.text('Count: 0'), findsOneWidget);

    // Tap the increment button
    await tester.tap(find.text('Increment'));
    await tester.pump();

    // Verify updated state
    expect(find.text('Count: 1'), findsOneWidget);
  });

  testWidgets('Displays initial value', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: CounterWidget(initialValue: 42),
    ));

    expect(find.text('Count: 42'), findsOneWidget);
  });
}
```

### 用 Mockito 进行嘲笑
```dart
// test/services/user_service_test.dart
import 'package:mockito/mockito.dart';
import 'package:test/test.dart';

// Generate mocks with: dart run build_runner build
class MockApiService extends Mock implements ApiService {}

void main() {
  late MockApiService mockApi;
  late UserService userService;

  setUp(() {
    mockApi = MockApiService();
    userService = UserService(api: mockApi);
  });

  test('getUser returns user from API', () async {
    when(mockApi.fetchUser('1')).thenAnswer(
      (_) async => {'id': '1', 'name': 'Alice', 'email': 'alice@mail.com'},
    );

    final user = await userService.getUser('1');
    
    expect(user.name, equals('Alice'));
    verify(mockApi.fetchUser('1')).called(1);
    verifyNever(mockApi.fetchUser(any));
  });

  test('handles API failure gracefully', () async {
    when(mockApi.fetchUser('1')).thenThrow(Exception('Network error'));

    expect(
      () => userService.getUser('1'),
      throwsA(isA<UserServiceException>()),
    );
  });
}
```
---

## 互操作性
### FFI（外部函数接口）
```dart
// Dart FFI: call native C/C++ libraries directly
import 'dart:ffi';
import 'package:ffi/ffi.dart';

// Define the native function signature
typedef NativeAdd = Int32 Function(Int32 a, Int32 b);
typedef DartAdd = int Function(int a, int b);

// Load the native library
final DynamicLibrary lib = Platform.isAndroid
    ? DynamicLibrary.open('libnative.so')
    : DynamicLibrary.process();

// Look up the function
final DartAdd nativeAdd = lib
    .lookup<NativeFunction<NativeAdd>>('native_add')
    .asFunction();

void main() {
  print(nativeAdd(5, 3));  // 8
}
```

### 平台频道（Flutter）
```dart
// Dart side: call native platform code
class BatteryService {
  static const platform = MethodChannel('com.example/battery');

  Future<int> getBatteryLevel() async {
    try {
      final int result = await platform.invokeMethod('getBatteryLevel');
      return result;
    } on PlatformException catch (e) {
      print('Failed to get battery level: ${e.message}');
      return -1;
    }
  }
}

// Android side (Kotlin) - in MainActivity.kt:
// class MainActivity : FlutterActivity() {
//     private val CHANNEL = "com.example/battery"
//     override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
//         super.configureFlutterEngine(flutterEngine)
//         MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL)
//             .setMethodCallHandler { call, result ->
//                 if (call.method == "getBatteryLevel") {
//                     val level = getBatteryLevel()
//                     result.success(level)
//                 } else {
//                     result.notImplemented()
//                 }
//             }
//     }
// }
```

### JavaScript 互操作 (Dart Web)
```dart
// dart:js_interop for web targets
import 'dart:js_interop';

@JS('console.log')
external void jsConsoleLog(String message);

@JS('JSON.stringify')
external String jsonStringify(Object? value);

@JS()
extension type Window._(JSObject it) implements JSObject {
  external int get innerWidth;
  external int get innerHeight;
}
```

---

## 设计模式
### 模式 1：存储库模式
```dart
// Abstract repository interface
abstract class UserRepository {
  Future<User> getUser(String id);
  Future<List<User>> getAllUsers();
  Future<void> saveUser(User user);
}

// Implementation with API
class ApiUserRepository implements UserRepository {
  final ApiService _api;
  ApiUserRepository(this._api);

  @override
  Future<User> getUser(String id) async {
    final json = await _api.fetchUser(id);
    return User.fromJson(json);
  }

  @override
  Future<List<User>> getAllUsers() async {
    final list = await _api.fetchUsers();
    return list.map((json) => User.fromJson(json)).toList();
  }

  @override
  Future<void> saveUser(User user) async {
    await _api.updateUser(user.id, user.toJson());
  }
}

// In-memory cache decorator
class CachedUserRepository implements UserRepository {
  final UserRepository _inner;
  final Map<String, User> _cache = {};

  CachedUserRepository(this._inner);

  @override
  Future<User> getUser(String id) async {
    if (_cache.containsKey(id)) return _cache[id]!;
    final user = await _inner.getUser(id);
    _cache[id] = user;
    return user;
  }

  @override
  Future<List<User>> getAllUsers() => _inner.getAllUsers();

  @override
  Future<void> saveUser(User user) async {
    await _inner.saveUser(user);
    _cache[user.id] = user;
  }
}
```

### 模式 2：提供者状态管理
```dart
// Using Provider for state management in Flutter
class CounterModel extends ChangeNotifier {
  int _count = 0;
  int get count => _count;

  void increment() {
    _count++;
    notifyListeners();
  }
}

// Provide at the top of the widget tree
void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => CounterModel(),
      child: const MyApp(),
    ),
  );
}

// Consume in widgets
class CounterDisplay extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final count = context.watch<CounterModel>().count;
    return Text('Count: $count');
  }
}

class IncrementButton extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () => context.read<CounterModel>().increment(),
      child: const Text('Increment'),
    );
  }
}
```

### 模式 3：BLoC（业务逻辑组件）
```dart
// BLoC pattern: separate business logic from UI
class LoginBloc {
  final _emailController = StreamController<String>.broadcast();
  final _passwordController = StreamController<String>.broadcast();
  final _loginResultController = StreamController<LoginState>.broadcast();

  Stream<String> get emailChanges => _emailController.stream;
  Stream<String> get passwordChanges => _passwordController.stream;
  Stream<LoginState> get loginResults => _loginResultController.stream;

  void onEmailChanged(String email) => _emailController.add(email);
  void onPasswordChanged(String password) => _passwordController.add(password);

  Future<void> login() async {
    _loginResultController.add(LoginState.loading);
    try {
      final user = await _authService.login(email, password);
      _loginResultController.add(LoginState.success(user));
    } catch (e) {
      _loginResultController.add(LoginState.error(e.toString()));
    }
  }

  void dispose() {
    _emailController.close();
    _passwordController.close();
    _loginResultController.close();
  }
}
```
---

## 性能与优化
### AOT 与 JIT 编译
|模式|使用时 |启动|运行时|使用案例|
|------|---------|---------|---------|----------|
| **JIT**（准时制）|开发、调试模式|快|稍微慢一点|开发期间热重载 |
| **AOT**（提前）|发布版本 |稍微慢一点|更快 |生产移动/桌面应用程序 |
| **JS** |网络目标 |取决于 |变化 | Flutter Web 应用程序 |
| **WASM** |网络（实验性）|取决于 |快|未来网络目标|
```dart
// Performance tips for Flutter/Dart:

// 1. Use const constructors where possible
const SizedBox(height: 16);  // Reused, not recreated
const Text('Hello');          // Compiled into the binary

// 2. Avoid unnecessary rebuilds with const widgets
class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return const Padding(
      padding: EdgeInsets.all(8.0),
      child: Text('Optimized'),
    );
  }
}

// 3. Use RepaintBoundary for expensive widgets
RepaintBoundary(
  child: ExpensiveChartWidget(data: data),
)

// 4. Lazy loading with FutureBuilder
FutureBuilder<List<Item>>(
  future: fetchItems(),
  builder: (context, snapshot) {
    if (snapshot.connectionState == ConnectionState.waiting) {
      return const CircularProgressIndicator();
    }
    if (snapshot.hasError) {
      return Text('Error: ${snapshot.error}');
    }
    return ListView.builder(
      itemCount: snapshot.data!.length,
      itemBuilder: (context, index) => ItemTile(snapshot.data![index]),
    );
  },
)
```

---

## 部署
### Flutter 部署目标
|平台|构建命令|输出|
|----------|--------------|--------|
| **安卓** | `flutter build apk`/`flutter build appbundle`| Play 商店的 APK / AAB |
| **iOS** | `flutter build ipa`| App Store 的 IPA |
| **网络** | `flutter build web`|静态 HTML/JS/CSS |
| **Windows** | `flutter build windows`| MSIX 或独立 exe |
| **macOS** | `flutter build macos`| .app 捆绑包 |
| **Linux** | `flutter build linux`|二元+资产 |
```bash
# Build commands
flutter build apk --release                    # Android APK
flutter build appbundle --release              # Android App Bundle (Play Store)
flutter build ipa --release                    # iOS IPA (App Store)
flutter build web --release --web-renderer canvaskit  # Web with CanvasKit

# Environment-specific builds
flutter build apk --release --dart-define=ENV=production
flutter build apk --release --dart-define=ENV=staging

# Code signing (Android)
# In android/app/build.gradle:
# signingConfigs {
#     release {
#         storeFile file('keystore.jks')
#         storePassword System.getenv('STORE_PASSWORD')
#         keyAlias 'release-key'
#         keyPassword System.getenv('KEY_PASSWORD')
#     }
# }
```

---

## 何时使用 Dart
|场景|为什么使用 Dart（Flutter）|更好的选择|
|----------|--------------------|--------------------|
|跨平台移动应用程序 |颤振很优秀 | React Native、原生 Swift/Kotlin |
|跨平台桌面 | Flutter 支持 |电子、C#、Avalonia |
|网络应用程序| Flutter 网络存在 | React、Vue、Angular 打造更丰富的 Web 应用程序 |
|嵌入式用户界面 | Flutter 嵌入式 | C、LVGL |
|后端开发|不是主要用例 | Go、Node.js、Python |
|数据科学/机器学习 |不适合| Python、R |
|系统编程|不适合| C、C++、Rust |
---

## 综合问答
### Q1：Dart 的空安全是如何工作的？
**答：** Dart 2.12+ 具有健全的 null 安全性。默认情况下变量不可为空；使用`?`允许 null：
```dart
String name = 'Alice';    // Cannot be null
String? nickname;          // Can be null
// name = null;            // Compile error!

// Null-aware operators
int? age;
int displayAge = age ?? 0;        // Elvis: default if null
int len = age?.toString().length ?? 0;  // Safe chaining

// Null assertion (use sparingly)
String! forced = nullableString!;  // Throws if null

// Late initialization
late final Config config;  // Assigned before first use
```

### Q2：`Future` 和`Stream`有什么区别？
**A:**`Future`表示单个异步结果； `Stream`表示一系列异步事件：
```dart
// Future — one value, later
Future<String> fetchName() async => 'Alice';

// Stream — multiple values over time
Stream<int> counter() async* {
  for (int i = 0; i < 10; i++) {
    await Future.delayed(Duration(seconds: 1));
    yield i;
  }
}

// Consuming
counter().listen(print);
// or
await for (final n in counter()) {
  print(n);
}
```

### Q3：如何管理 Flutter 应用中的状态？
**答：** 根据复杂程度采用多种方法：
```dart
// Simple: StatefulWidget
class CounterWidget extends StatefulWidget {
  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}
class _CounterWidgetState extends State<CounterWidget> {
  int _count = 0;
  void increment() => setState(() => _count++);
}

// Medium: Provider (dependency injection)
// Complex: Riverpod, BLoC, or Redux
```

### Q4：扩展方法在 Dart 中如何工作？
**A:** 扩展向现有类型添加功能而无需继承：
```dart
extension StringExtras on String {
  String get capitalized => '${this[0].toUpperCase()}${substring(1)}';
  bool get isEmail => contains(RegExp(r'@.+\..+'));
}

'hello'.capitalized  // 'Hello'
'user@example.com'.isEmail  // true
```

### Q5：如何编写高性能的 Dart/Flutter 代码？
**答：** 关键做法：
- 尽可能使用`const`构造函数
- 避免重建小部件 - 使用`const`、`final`和`shouldRebuild`
- 对于大型列表，使用`ListView.builder`而不是 `ListView`
- 使用 Flutter DevTools 进行配置
- 使用`compute()`在隔离线程上执行昂贵的操作
- 最小化`setState`调用 - 具体说明需要重建的内容
---

## 解决问题的思路
### 问题 1：构建类型安全的 API 客户端
**第 1 步：了解问题**
创建一个 API 客户端来获取数据并返回类型正确的对象。
**第 2 步：确定方法**
将 Dart 类与`fromJson`/`toJson`、 async/await 和密封类一起使用以获取结果。
**步骤 3：实施**```dart
sealed class ApiResult<T> {
  const ApiResult();
}
class ApiSuccess<T> extends ApiResult<T> {
  final T data;
  const ApiSuccess(this.data);
}
class ApiError<T> extends ApiResult<T> {
  final String message;
  final int? statusCode;
  const ApiError(this.message, {this.statusCode});
}

class User {
  final String name;
  final String email;
  User({required this.name, required this.email});
  factory User.fromJson(Map<String, dynamic> json) =>
    User(name: json['name'], email: json['email']);
}

class ApiClient {
  final http.Client _client;
  ApiClient(this._client);

  Future<ApiResult<User>> getUser(String id) async {
    try {
      final response = await _client.get(
        Uri.parse('https://api.example.com/users/$id'),
      );
      if (response.statusCode == 200) {
        final json = jsonDecode(response.body);
        return ApiSuccess(User.fromJson(json));
      }
      return ApiError('Failed', statusCode: response.statusCode);
    } catch (e) {
      return ApiError(e.toString());
    }
  }
}
```

**第 4 步：验证**
使用模拟 HTTP 客户端进行测试。验证网络故障和不良响应的错误处理。
### 问题 2：通过去抖动实现响应式搜索
**第 1 步：了解问题**
构建一个查询 API 的搜索字段，但会对输入进行反跳以避免过多的请求。
**第 2 步：确定方法**
将 Dart Streams 与`debounceTime`和`distinct`结合使用。
**步骤 3：实施**```dart
import 'dart:async';

class SearchController {
  final _controller = StreamController<String>();
  final _results = <String>[];

  Stream<List<String>> get results => _controller.stream
    .debounceTime(Duration(milliseconds: 300))
    .distinct()
    .asyncMap(_fetchResults);

  void onQuery(String query) => _controller.add(query);

  Future<List<String>> _fetchResults(String query) async {
    // Simulate API call
    await Future.delayed(Duration(milliseconds: 200));
    return ['Result 1 for $query', 'Result 2 for $query'];
  }

  void dispose() => _controller.close();
}
```

**第 4 步：测试**
验证快速输入是否仅在去抖期后触发一次 API 调用。
---

＃＃ 概括
Dart 的人生目标是 Flutter。作为一门独立的语言，它是有能力的，但并不起眼。作为 Flutter 背后的引擎，它使开发人员能够从单个代码库为每个主要平台构建美观、高性能的应用程序。如果您正在构建跨平台移动或桌面应用程序，Dart + Flutter 是最好的选择之一。对于其他一切，其他语言更合适。