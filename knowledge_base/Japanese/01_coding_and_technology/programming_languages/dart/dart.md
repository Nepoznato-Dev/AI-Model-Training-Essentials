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
#ダーツ
Dart は、Google によって開発され、2013 年に初めてリリースされた、クライアントに最適化されたプログラミング言語です。Dart は当初、Web ブラウザの JavaScript の代替候補として位置付けられていましたが、その主な目的は、単一のコードベースからモバイル、Web、デスクトップ、および組み込みアプリケーションを構築するための Google のクロスプラットフォーム UI ツールキットである **Flutter** の背後にある言語であることがわかりました。
Dart は現代言語の最高の機能を組み合わせています。オブジェクト指向であり、オプションの型付け (Dart 3 以降ではサウンド null 安全性) があり、`async`/`await`による非同期プログラミングをサポートし、ネイティブ マシン コード (モバイル/デスクトップ用) と JavaScript (Web 用) の両方にコンパイルされます。
---

## なぜダーツが重要なのか
- **Flutter**: Flutter の主要言語であり、最も急速に成長しているクロスプラットフォーム フレームワークの 1 つです。
- **クロスプラットフォーム**: iOS、Android、Web、Windows、macOS、Linux、および組み込みデバイス用の単一コードベース。
- **生産性**: ホット リロード、豊富なウィジェット ライブラリ、表現力豊かな構文により、UI 開発が高速化されます。
- **健全な null 安全性**: コンパイル時の null 安全性により、null 参照エラーが排除されます。
- **パフォーマンス**: モバイル用のネイティブ ARM コードにコンパイルします。橋は必要ありません。
- **成長するエコシステム**: Flutter のパッケージ エコシステムは急速に拡大しています。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **Flutter 中心** | Dart のほとんどの使用法は Flutter です。それ以外では限定される |フラッターに使用します。非 UI 作業用の他の言語 |
| **小規模なエコシステム** | React Native またはネイティブ プラットフォームよりもパッケージが少ない |急速に成長しています。ネイティブ API のプラットフォーム チャネル |
| **ウェブ パフォーマンス** | WASM にコンパイルされた Dart はまだ成熟しています。一貫したパフォーマンスを得るには CanvasKit レンダラーを使用してください。
| **雇用市場** | Flutter ロールは存在しますが、ネイティブ モバイルよりも少ない |クロスプラットフォーム開発者の需要の高まり |
| **バックエンド用ではありません** |可能 (サーバー側 Dart) ですが、ユースケースではありません |バックエンドに Go、Node.js、Python を使用する |
---

## 構文の基礎
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

## 高度な構文とパターン
### ヌル安全性 — 詳細
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

### ミックスイン
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

### 拡張機能
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

### 分離 (同時実行)
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
### 注釈とコード生成
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

## コア機能の詳細
### ストリーム処理
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

### フラッターウィジェットパターン
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

## プロジェクトの構成とシステムの構築
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

### 分析オプション.yaml
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

## テスト
### テストパッケージを使用した単体テスト
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

### flutter_test を使用したウィジェットのテスト
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

### Mockito を使ったモック
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

## 相互運用性
### FFI (外部関数インターフェース)
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

### プラットフォーム チャネル (Flutter)
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

### JavaScript 相互運用性 (Dart Web)
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

## デザインパターン
### パターン 1: リポジトリ パターン
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

### パターン 2: プロバイダーの状態管理
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

### パターン 3: BLoC (ビジネス ロジック コンポーネント)
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

## パフォーマンスと最適化
### AOT と JIT のコンパイル
|モード |使用時 |スタートアップ |ランタイム |使用例 |
|------|-----------|----------|-----------|----------|
| **JIT** (ジャストインタイム) |開発、デバッグモード |速い |わずかに遅い |開発中のホットリロード |
| **AOT** (事前) |リリースビルド |わずかに遅い |より速く |実稼働モバイル/デスクトップ アプリ |
| **JS** |ウェブターゲット |場合による |さまざま | Flutter Web アプリケーション |
| **ワズム** |ウェブ (実験的) |場合による |速い |将来の Web ターゲット |
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

## デプロイメント
### Flutter デプロイメントターゲット
|プラットフォーム |ビルドコマンド |出力 |
|----------|--------------|----------|
| **アンドロイド** | `flutter build apk`/`flutter build appbundle`| Play ストア用 APK / AAB |
| **iOS** | `flutter build ipa`| App Store 向け IPA |
| **ウェブ** | `flutter build web`|静的HTML/JS/CSS |
| **Windows** | `flutter build windows`| MSIX またはスタンドアロン exe |
| **macOS** | `flutter build macos`| .appバンドル |
| **Linux** | `flutter build linux`|バイナリ + アセット |
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

## ダーツを使用する場合
|シナリオ |なぜダーツ (フラッター) |より良い代替案 |
|----------|-------------------|--------|
|クロスプラットフォームのモバイル アプリ |フラッターは素晴らしいです | React Native、ネイティブ Swift/Kotlin |
|クロスプラットフォームデスクトップ | Flutter はそれをサポートします |電子、C#、アバロニア |
|ウェブアプリケーション |フラッターウェブが存在します |よりリッチな Web アプリのための React、Vue、Angular |
|埋め込み型 UI |組み込み用のフラッター | C、LVGL |
|バックエンド開発 |主な使用例ではありません | Go、Node.js、Python |
|データ サイエンス / ML |適さない |パイソン、R |
|システムプログラミング |適さない | C、C++、Rust |
---

## 総合的な Q&A
### Q1: Dart のヌル セーフティはどのように機能しますか?
**A:** Dart 2.12+ には健全なヌル安全性があります。変数はデフォルトでは null 値を許容できません。 null を許可するには`?`を使用します。
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

### Q2:`Future`と`Stream`の違いは何ですか?
**A:**`Future`は単一の非同期結果を表します。 `Stream`は、一連の非同期イベントを表します。
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

### Q3: Flutter アプリで状態を管理するにはどうすればよいですか?
**A:** 複雑さに応じて複数のアプローチ:
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

### Q4: Dart では拡張メソッドはどのように機能しますか?
**A:** 拡張機能は、継承せずに既存の型に機能を追加します。
```dart
extension StringExtras on String {
  String get capitalized => '${this[0].toUpperCase()}${substring(1)}';
  bool get isEmail => contains(RegExp(r'@.+\..+'));
}

'hello'.capitalized  // 'Hello'
'user@example.com'.isEmail  // true
```

### Q5: パフォーマンスの高い Dart/Flutter コードを作成するにはどうすればよいですか?
**A:** 主な実践方法:
- 可能な限り`const`コンストラクターを使用します
- ウィジェットの再構築を避ける -`const`、`final`、および`shouldRebuild`を使用します 
- 大きなリストには`ListView`の代わりに`ListView.builder`を使用します
- Flutter DevTools を使用したプロファイル
- 分離スレッドでの負荷の高い操作には`compute()`を使用します
-`setState`呼び出しを最小限に抑える — 再構築が必要なものを具体的にする
---

## 思考連鎖による問題解決
### 問題 1: タイプセーフな API クライアントの構築
**ステップ 1: 問題を理解する**
データをフェッチし、適切に型指定されたオブジェクトを返す API クライアントを作成します。
**ステップ 2: アプローチを特定する**
結果には`fromJson`/`toJson`、 async/await 、および sealed クラスを持つ Dart クラスを使用します。
**ステップ 3: 実装**```dart
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

**ステップ 4: 確認**
模擬 HTTP クライアントを使用してテストします。ネットワーク障害と不正な応答に対するエラー処理を確認します。
### 問題 2: デバウンスを使用したリアクティブ検索の実装
**ステップ 1: 問題を理解する**
API をクエリする検索フィールドを構築しますが、過剰なリクエストを避けるために入力をデバウンスします。
**ステップ 2: アプローチを特定する**
`debounceTime` および`distinct`でダーツ ストリームを使用します。
**ステップ 3: 実装**```dart
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

**ステップ 4: テスト**
デバウンス期間後に、高速入力によって API 呼び出しが 1 回だけトリガーされることを確認します。
---

＃＃ まとめ
ダーツの人生の目的はフラッターです。スタンドアロン言語としては有能ですが、目立たないものです。 Flutter の背後にあるエンジンとして、開発者は単一のコードベースからあらゆる主要プラットフォーム向けの美しく高性能なアプリケーションを構築できます。クロスプラットフォームのモバイルまたはデスクトップ アプリケーションを構築している場合、Dart + Flutter は利用可能な最良のオプションの 1 つです。それ以外の場合は、他の言語の方が適切です。