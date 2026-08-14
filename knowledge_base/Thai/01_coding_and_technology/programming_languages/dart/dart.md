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
#ดาร์ท
Dart เป็นภาษาโปรแกรมที่ปรับให้เหมาะกับไคลเอนต์ซึ่งพัฒนาโดย Google ซึ่งเปิดตัวครั้งแรกในปี 2013 แม้ว่า Dart จะถูกวางตำแหน่งให้เป็นสิ่งทดแทน JavaScript ที่เป็นไปได้สำหรับเว็บเบราว์เซอร์ แต่ก็พบว่าจุดประสงค์หลักคือภาษาที่อยู่เบื้องหลัง **Flutter** ซึ่งเป็นชุดเครื่องมือ UI ข้ามแพลตฟอร์มของ Google สำหรับการสร้างแอปพลิเคชันบนมือถือ เว็บ เดสก์ท็อป และแอปพลิเคชันแบบฝังจากโค้ดเบสเดียว
Dart ผสมผสานคุณสมบัติที่ดีที่สุดของภาษาสมัยใหม่: เป็นแบบเชิงวัตถุ มีตัวเลือกการพิมพ์ (ความปลอดภัยแบบ null ของเสียงตั้งแต่ Dart 3) รองรับการเขียนโปรแกรมแบบอะซิงโครนัสด้วย`async`/`await`และคอมไพล์ทั้งรหัสเครื่องเนทีฟ (สำหรับมือถือ/เดสก์ท็อป) และ JavaScript (สำหรับเว็บ)
---

## ทำไมเรื่องโผ
- **Flutter**: ภาษาหลักสำหรับ Flutter — หนึ่งในเฟรมเวิร์กข้ามแพลตฟอร์มที่เติบโตเร็วที่สุด
- **ข้ามแพลตฟอร์ม**: โค้ดเบสเดี่ยวสำหรับ iOS, Android, เว็บ, Windows, macOS, Linux และอุปกรณ์ฝังตัว
- **ประสิทธิผล**: การรีโหลดแบบด่วน ไลบรารีวิดเจ็ตที่หลากหลาย และไวยากรณ์ที่แสดงออกทำให้การพัฒนา UI รวดเร็ว
- **ความปลอดภัยที่เป็นโมฆะ**: ความปลอดภัยของโมฆะในเวลาคอมไพล์ช่วยลดข้อผิดพลาดในการอ้างอิงที่เป็นโมฆะ
- **ประสิทธิภาพ**: คอมไพล์เป็นโค้ด ARM ดั้งเดิมสำหรับมือถือ ไม่จำเป็นต้องมีสะพาน
- **ระบบนิเวศที่กำลังเติบโต**: ระบบนิเวศแพ็คเกจของ Flutter กำลังขยายตัวอย่างรวดเร็ว
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **กระพือเป็นศูนย์กลาง** | การใช้งาน Dart ส่วนใหญ่เป็น Flutter; นอกนั้นจำกัด | ใช้สำหรับกระพือ; ภาษาอื่นสำหรับงานที่ไม่ใช่ UI |
| **ระบบนิเวศเล็กลง** | แพ็คเกจน้อยกว่า React Native หรือ Native Platforms เติบโตอย่างรวดเร็ว ช่องทางแพลตฟอร์มสำหรับ API ดั้งเดิม |
| **ประสิทธิภาพของเว็บ** | Dart ที่คอมไพล์เป็น WASM ยังคงสุก | ใช้ตัวเรนเดอร์ CanvasKit เพื่อประสิทธิภาพที่สม่ำเสมอ |
| **ตลาดงาน** | มีบทบาท Flutter แต่น้อยกว่ามือถือดั้งเดิม | ความต้องการที่เพิ่มขึ้นสำหรับนักพัฒนาข้ามแพลตฟอร์ม |
| **ไม่ใช่สำหรับแบ็กเอนด์** | เป็นไปได้ (Dart ฝั่งเซิร์ฟเวอร์) แต่ไม่ใช่กรณีการใช้งาน | ใช้ Go, Node.js, Python สำหรับแบ็กเอนด์ |
---

## พื้นฐานไวยากรณ์
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

## ไวยากรณ์และรูปแบบขั้นสูง
### ความปลอดภัยแบบไร้ศูนย์ — เจาะลึก
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

### มิกซ์อิน
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

### ส่วนขยาย
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

### แยก (พร้อมกัน)
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
### คำอธิบายประกอบและการสร้างโค้ด
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

## เจาะลึกคุณสมบัติหลัก
### การจัดการสตรีม
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

### รูปแบบวิดเจ็ตกระพือ
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
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

### analysis_options.yaml
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

## การทดสอบ
### การทดสอบหน่วยพร้อมแพ็คเกจการทดสอบ
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

### การทดสอบวิดเจ็ตด้วย flutter_test
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

### ล้อเลียนกับม็อกคิโต
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

## การทำงานร่วมกัน
### FFI (อินเทอร์เฟซฟังก์ชันต่างประเทศ)
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

### ช่องทางแพลตฟอร์ม (Flutter)
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

### การทำงานร่วมกันของ JavaScript (เว็บโผ)
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

## รูปแบบการออกแบบ
### รูปแบบ 1: รูปแบบพื้นที่เก็บข้อมูล
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

### รูปแบบ 2: การจัดการสถานะของผู้ให้บริการ
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

### รูปแบบ 3: BLoC (ส่วนประกอบตรรกะทางธุรกิจ)
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### AOT กับการรวบรวม JIT
| โหมด | เมื่อใช้ | เริ่มต้น | รันไทม์ | ใช้กรณี |
|------|-----------|---------|---------|----------|
| **JIT** (ทันเวลาพอดี) | การพัฒนา โหมดแก้ไขข้อบกพร่อง | รวดเร็ว | ช้าลงเล็กน้อย | โหลดซ้ำร้อนระหว่างการพัฒนา |
| **ทอท.** (ล่วงหน้า) | ปล่อยบิลด์ | ช้าลงเล็กน้อย | เร็วขึ้น | แอปมือถือ/เดสก์ท็อปที่ใช้งานจริง |
| **จส** | เป้าหมายเว็บ | ขึ้นอยู่กับ | ต่างกันไป | เว็บแอปพลิเคชั่นกระพือ |
| **WASM** | เว็บ (ทดลอง) | ขึ้นอยู่กับ | รวดเร็ว | เป้าหมายเว็บในอนาคต |
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

## การปรับใช้
### เป้าหมายการปรับใช้ Flutter
| แพลตฟอร์ม | สร้างคำสั่ง | เอาท์พุท |
|----------|--------------|--------|
| **แอนดรอยด์** | `flutter build apk`/`flutter build appbundle`| APK / AAB สำหรับ Play Store |
| **iOS** | `flutter build ipa`| IPA สำหรับ App Store |
| **เว็บ** | `flutter build web`| HTML/JS/CSS แบบคงที่ |
| **หน้าต่าง** | `flutter build windows`| MSIX หรือ exe แบบสแตนด์อโลน |
| **macOS** | `flutter build macos`| .app บันเดิล |
| **ลินุกซ์** | `flutter build linux`| ไบนารี + สินทรัพย์ |
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

## เมื่อใดจึงควรใช้โผ
| สถานการณ์ | ทำไมต้อง Dart (Flutter) | ทางเลือกที่ดีกว่า |
|----------|-------------------|-------------------|
| แอพมือถือข้ามแพลตฟอร์ม | กระพือเป็นเลิศ | โต้ตอบ Native, Native Swift/Kotlin |
| เดสก์ท็อปข้ามแพลตฟอร์ม | Flutter รองรับมัน | อิเล็กตรอน, C#, อวาโลเนีย |
| เว็บแอปพลิเคชั่น | มีเว็บ Flutter อยู่ | React, Vue, Angular สำหรับเว็บแอปที่สมบูรณ์ยิ่งขึ้น |
| UI แบบฝัง | กระพือเพื่อฝัง | C, LVGL |
| การพัฒนาแบ็กเอนด์ | ไม่ใช่กรณีการใช้งานหลัก | ไป, Node.js, Python |
| วิทยาศาสตร์ข้อมูล / ML | ไม่เหมาะ | หลาม, อาร์ |
| การเขียนโปรแกรมระบบ | ไม่เหมาะ | C, C++, สนิม |
---

## คำถามและคำตอบสังเคราะห์
### คำถามที่ 1: ความปลอดภัยแบบ null ของ Dart ทำงานอย่างไร
**A:** Dart 2.12+ มีความปลอดภัยแบบ null ตัวแปรไม่เป็นค่าว่างตามค่าเริ่มต้น ใช้`?`เพื่ออนุญาตให้เป็นโมฆะ:
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

### Q2: อะไรคือความแตกต่างระหว่าง`Future`และ`Stream`?
**A:**`Future`แสดงถึงผลลัพธ์อะซิงก์เดียว `Stream`แสดงถึงลำดับของเหตุการณ์อะซิงก์:
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

### Q3: ฉันจะจัดการสถานะในแอป Flutter ได้อย่างไร
**ตอบ:** มีหลายวิธีขึ้นอยู่กับความซับซ้อน:
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

### Q4: วิธีการขยายทำงานใน Dart อย่างไร
**ตอบ:** ส่วนขยายเพิ่มฟังก์ชันการทำงานให้กับประเภทที่มีอยู่โดยไม่มีการสืบทอด:
```dart
extension StringExtras on String {
  String get capitalized => '${this[0].toUpperCase()}${substring(1)}';
  bool get isEmail => contains(RegExp(r'@.+\..+'));
}

'hello'.capitalized  // 'Hello'
'user@example.com'.isEmail  // true
```

### Q5: ฉันจะเขียนโค้ด Dart/Flutter ที่มีประสิทธิภาพได้อย่างไร
**ก:** แนวทางปฏิบัติหลัก:
- ใช้ตัวสร้าง`const`ทุกที่ที่เป็นไปได้
- หลีกเลี่ยงการสร้างวิดเจ็ตใหม่ — ใช้`const`,`final`และ`shouldRebuild`
- ใช้`ListView.builder`แทน`ListView`สำหรับรายการขนาดใหญ่
- โปรไฟล์ด้วย Flutter DevTools
- ใช้`compute()`สำหรับการดำเนินการที่มีราคาแพงบนการแยกเธรด
- ลดการเรียก`setState`ให้เหลือน้อยที่สุด — ให้เจาะจงเกี่ยวกับสิ่งที่จำเป็นต้องสร้างใหม่
---

## การแก้ปัญหาลูกโซ่แห่งความคิด
### ปัญหาที่ 1: การสร้างไคลเอนต์ API แบบปลอดภัย
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
สร้างไคลเอ็นต์ API ที่ดึงข้อมูลและส่งคืนออบเจ็กต์ที่พิมพ์อย่างถูกต้อง
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้คลาส Dart กับ`fromJson`/`toJson`, async/await และคลาสที่ปิดผนึกเพื่อดูผลลัพธ์
**ขั้นตอนที่ 3: นำไปใช้**```dart
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

**ขั้นตอนที่ 4: ยืนยัน**
ทดสอบกับไคลเอ็นต์ HTTP จำลอง ตรวจสอบการจัดการข้อผิดพลาดสำหรับความล้มเหลวของเครือข่ายและการตอบกลับที่ไม่ถูกต้อง
### ปัญหาที่ 2: การใช้การค้นหาเชิงโต้ตอบด้วย Debounce
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
สร้างช่องค้นหาที่สอบถาม API แต่หักล้างอินพุตเพื่อหลีกเลี่ยงคำขอที่มากเกินไป
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้ Dart Streams กับ`debounceTime`และ `distinct`
**ขั้นตอนที่ 3: นำไปใช้**```dart
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

**ขั้นตอนที่ 4: ทดสอบ**
ตรวจสอบว่าการพิมพ์อย่างรวดเร็วทำให้เกิดการเรียก API เพียงครั้งเดียวหลังจากช่วง debounce
---

## สรุป
จุดประสงค์ในชีวิตของ Dart คือ Flutter เนื่องจากเป็นภาษาสแตนด์อโลน จึงมีความสามารถแต่ไม่โดดเด่น ในฐานะกลไกที่อยู่เบื้องหลัง Flutter ช่วยให้นักพัฒนาสามารถสร้างแอปพลิเคชันที่สวยงามและมีประสิทธิภาพสูงสำหรับแพลตฟอร์มหลักทุกแพลตฟอร์มจากโค้ดเบสเดียว หากคุณกำลังสร้างแอปพลิเคชันมือถือหรือเดสก์ท็อปข้ามแพลตฟอร์ม Dart + Flutter เป็นหนึ่งในตัวเลือกที่ดีที่สุด สำหรับอย่างอื่น ภาษาอื่นจะเหมาะสมกว่า