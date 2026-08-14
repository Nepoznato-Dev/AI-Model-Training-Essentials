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
# ডার্ট
ডার্ট হল একটি ক্লায়েন্ট-অপ্টিমাইজড প্রোগ্রামিং ল্যাঙ্গুয়েজ যা Google দ্বারা বিকশিত হয়েছে, যা 2013 সালে প্রথম প্রকাশিত হয়েছিল। যদিও ডার্টকে প্রাথমিকভাবে ওয়েব ব্রাউজারগুলির জন্য একটি সম্ভাব্য জাভাস্ক্রিপ্ট প্রতিস্থাপন হিসাবে স্থান দেওয়া হয়েছিল, এটি **ফ্লটার** এর পিছনে ভাষা হিসাবে এর প্রাথমিক উদ্দেশ্য খুঁজে পেয়েছিল — মোবাইল, ওয়েব, ডেস্কটপ, এবং একটি একক কোডবা অ্যাপ্লিকেশন তৈরির জন্য Google এর ক্রস-প্ল্যাটফর্ম UI টুলকিট।
ডার্ট আধুনিক ভাষার সেরা বৈশিষ্ট্যগুলিকে একত্রিত করে: এটি অবজেক্ট-ওরিয়েন্টেড, এতে ঐচ্ছিক টাইপিং রয়েছে (ডার্ট 3 থেকে শব্দ শূন্য নিরাপত্তা),`async`/`await`এর সাথে অ্যাসিঙ্ক্রোনাস প্রোগ্রামিং সমর্থন করে এবং স্থানীয় মেশিন কোড (মোবাইল/ডেস্কটপের জন্য) এবং জাভাস্ক্রিপ্ট (ওয়েব-এর জন্য) উভয়ের সাথে কম্পাইল করে।
---

## কেন ডার্ট ব্যাপার
- **ফ্লটার**: ফ্লটারের প্রাথমিক ভাষা — দ্রুত বর্ধনশীল ক্রস-প্ল্যাটফর্ম ফ্রেমওয়ার্কগুলির মধ্যে একটি।
- **ক্রস-প্ল্যাটফর্ম**: iOS, Android, ওয়েব, Windows, macOS, Linux, এবং এমবেডেড ডিভাইসগুলির জন্য একক কোডবেস।
- **উৎপাদনশীল**: হট রিলোড, সমৃদ্ধ উইজেট লাইব্রেরি এবং অভিব্যক্তিপূর্ণ সিনট্যাক্স UI বিকাশকে দ্রুত করে তোলে।
- **সাউন্ড নাল সেফটি**: কম্পাইল-টাইম নাল সেফটি নাল রেফারেন্স ত্রুটি দূর করে।
- **পারফরম্যান্স**: মোবাইলের জন্য নেটিভ এআরএম কোডে কম্পাইল করে; কোন সেতুর প্রয়োজন নেই।
- **বর্ধমান ইকোসিস্টেম**: ফ্লটার প্যাকেজ ইকোসিস্টেম দ্রুত প্রসারিত হচ্ছে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **ফ্লটার-কেন্দ্রিক** | সবচেয়ে বেশি ডার্ট ব্যবহার হচ্ছে ফ্লটার; এর বাইরে সীমাবদ্ধ | ফ্লটার জন্য ব্যবহার করুন; অ-ইউআই কাজের জন্য অন্যান্য ভাষা |
| **ছোট ইকোসিস্টেম** | প্রতিক্রিয়া নেটিভ বা নেটিভ প্ল্যাটফর্মের চেয়ে কম প্যাকেজ | দ্রুত বর্ধনশীল; নেটিভ API এর জন্য প্ল্যাটফর্ম চ্যানেল |
| **ওয়েব পারফরম্যান্স** | WASM-তে সংকলিত ডার্ট এখনও পরিপক্ক হচ্ছে | ধারাবাহিক পারফরম্যান্সের জন্য ক্যানভাসকিট রেন্ডারার ব্যবহার করুন |
| **চাকরীর বাজার** | ফ্লটার ভূমিকা বিদ্যমান কিন্তু নেটিভ মোবাইলের চেয়ে কম | ক্রস-প্ল্যাটফর্ম বিকাশকারীদের জন্য ক্রমবর্ধমান চাহিদা |
| **ব্যাকএন্ডের জন্য নয়** | সম্ভাব্য (সার্ভার-সাইড ডার্ট) কিন্তু ব্যবহারের ক্ষেত্রে নয় | ব্যাকএন্ডের জন্য Go, Node.js, Python ব্যবহার করুন |
---

## সিনট্যাক্স মৌলিক
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### শূন্য নিরাপত্তা — গভীর ডুব
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

### মিক্সিং
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

### এক্সটেনশন
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

### বিচ্ছিন্ন (সঙ্গতি)
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
### টীকা এবং কোড জেনারেশন
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

## মূল বৈশিষ্ট্যগুলিতে গভীরভাবে ডুব দিন
### স্ট্রিম হ্যান্ডলিং
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

### ফ্লটার উইজেট প্যাটার্ন
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
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

## পরীক্ষা
### পরীক্ষার প্যাকেজ সহ ইউনিট পরীক্ষা
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

### ফ্লাটার_টেস্ট সহ উইজেট টেস্ট
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

### মকিটোর সাথে ঠাট্টা
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

## ইন্টারঅপারেবিলিটি
### FFI (ফরেন ফাংশন ইন্টারফেস)
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

### প্ল্যাটফর্ম চ্যানেল (ফ্লটার)
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

### জাভাস্ক্রিপ্ট ইন্টারপ (ডার্ট ওয়েব)
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

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: রিপোজিটরি প্যাটার্ন
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

### প্যাটার্ন 2: প্রদানকারী রাষ্ট্র ব্যবস্থাপনা
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

### প্যাটার্ন 3: BLoC (ব্যবসায়িক যুক্তি উপাদান)
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### AOT বনাম JIT সংকলন
| মোড | কখন ব্যবহার করা হয় | স্টার্টআপ | রানটাইম | কেস ব্যবহার করুন |
|------|------------|---------|---------|----------|
| **JIT** (জাস্ট-ইন-টাইম) | উন্নয়ন, ডিবাগ মোড | দ্রুত | সামান্য ধীর | উন্নয়নের সময় হট রিলোড |
| **AOT** (সময়ের আগে) | রিলিজ বিল্ডস | সামান্য ধীর | দ্রুত | উৎপাদন মোবাইল/ডেস্কটপ অ্যাপস |
| **জেএস** | ওয়েব লক্ষ্য | নির্ভর করে | পরিবর্তিত হয় | ফ্লটার ওয়েব অ্যাপ্লিকেশন |
| **WASM** | ওয়েব (পরীক্ষামূলক) | নির্ভর করে | দ্রুত | ভবিষ্যতের ওয়েব লক্ষ্য |
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

## স্থাপনা
### ফ্লটার ডিপ্লয়মেন্ট টার্গেট
| প্ল্যাটফর্ম | বিল্ড কমান্ড | আউটপুট |
|------------|---------------|---------|
| **Android** | `flutter build apk`/`flutter build appbundle`| প্লে স্টোরের জন্য APK / AAB |
| **iOS** | `flutter build ipa`| অ্যাপ স্টোরের জন্য IPA |
| **ওয়েব** | `flutter build web`| স্ট্যাটিক HTML/JS/CSS |
| **উইন্ডোজ** | `flutter build windows`| MSIX বা স্বতন্ত্র exe |
| **macOS** | `flutter build macos`| অ্যাপ বান্ডেল |
| **লিনাক্স** | `flutter build linux`| বাইনারি + সম্পদ |
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

## কখন ডার্ট ব্যবহার করবেন
| দৃশ্যকল্প | কেন ডার্ট (ফ্লটার) | ভাল বিকল্প |
|------------|-------------------------------|
| ক্রস-প্ল্যাটফর্ম মোবাইল অ্যাপস | ফ্লটার চমৎকার | প্রতিক্রিয়া নেটিভ, নেটিভ সুইফট/কোটলিন |
| ক্রস-প্ল্যাটফর্ম ডেস্কটপ | ফ্লাটার এটা সমর্থন করে | ইলেক্ট্রন, সি#, অ্যাভালোনিয়া |
| ওয়েব অ্যাপ্লিকেশন | ফ্লটার ওয়েব বিদ্যমান | রিঅ্যাক্ট, ভিউ, আরও সমৃদ্ধ ওয়েব অ্যাপের জন্য কৌণিক |
| এমবেডেড UIs | এমবেডেড জন্য ফ্লটার | সি, এলভিজিএল |
| ব্যাকএন্ড উন্নয়ন | প্রাথমিক ব্যবহারের ক্ষেত্রে নয় | Go, Node.js, Python |
| ডেটা সায়েন্স / এমএল | উপযুক্ত নয় | পাইথন, আর |
| সিস্টেম প্রোগ্রামিং | উপযুক্ত নয় | C, C++, মরিচা |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: ডার্টের নাল নিরাপত্তা কীভাবে কাজ করে?
**A:** Dart 2.12+ এর সাউন্ড নাল নিরাপত্তা আছে। ভেরিয়েবল ডিফল্টরূপে অ-শূন্য হয়; শূন্য অনুমতি দিতে`?`ব্যবহার করুন:
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

### প্রশ্ন 2:`Future`এবং`Stream`এর মধ্যে পার্থক্য কী?
**A:**`Future`একটি একক অ্যাসিঙ্ক ফলাফল উপস্থাপন করে; `Stream`অ্যাসিঙ্ক ইভেন্টগুলির একটি ক্রম উপস্থাপন করে:
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

### প্রশ্ন 3: আমি কীভাবে একটি ফ্লাটার অ্যাপে রাজ্য পরিচালনা করব?
**A:** জটিলতার উপর নির্ভর করে একাধিক পন্থা:
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

### প্রশ্ন 4: ডার্টে এক্সটেনশন পদ্ধতিগুলি কীভাবে কাজ করে?
**A:** এক্সটেনশনগুলি উত্তরাধিকার ছাড়াই বিদ্যমান প্রকারগুলিতে কার্যকারিতা যোগ করে:
```dart
extension StringExtras on String {
  String get capitalized => '${this[0].toUpperCase()}${substring(1)}';
  bool get isEmail => contains(RegExp(r'@.+\..+'));
}

'hello'.capitalized  // 'Hello'
'user@example.com'.isEmail  // true
```

### প্রশ্ন 5: আমি কীভাবে পারফরম্যান্ট ডার্ট/ফ্লাটার কোড লিখব?
**A:** মূল অনুশীলন:
- যেখানেই সম্ভব`const`কনস্ট্রাক্টর ব্যবহার করুন
- উইজেট পুনর্নির্মাণ এড়িয়ে চলুন — `const`, `final`, এবং`shouldRebuild`ব্যবহার করুন 
- বড় তালিকার জন্য`ListView`এর পরিবর্তে`ListView.builder`ব্যবহার করুন
- Flutter DevTools সহ প্রোফাইল
- আইসোলেট থ্রেডে ব্যয়বহুল অপারেশনের জন্য`compute()`ব্যবহার করুন
-`setState`কলগুলিকে মিনিমাইজ করুন — কিসের পুনর্নির্মাণের প্রয়োজন সে সম্পর্কে নির্দিষ্ট থাকুন৷
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি টাইপ-সেফ API ক্লায়েন্ট তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি API ক্লায়েন্ট তৈরি করুন যা ডেটা নিয়ে আসে এবং সঠিকভাবে টাইপ করা বস্তু ফেরত দেয়।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
`fromJson` /`toJson`, async/await, এবং ফলাফলের জন্য সিল করা ক্লাস সহ Dart ক্লাস ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```dart
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

**পদক্ষেপ 4: যাচাই করুন**
মক HTTP ক্লায়েন্ট দিয়ে পরীক্ষা করুন। নেটওয়ার্ক ব্যর্থতা এবং খারাপ প্রতিক্রিয়াগুলির জন্য ত্রুটি হ্যান্ডলিং যাচাই করুন৷
### সমস্যা 2: ডিবাউন্স সহ একটি প্রতিক্রিয়াশীল অনুসন্ধান বাস্তবায়ন করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি অনুসন্ধান ক্ষেত্র তৈরি করুন যা একটি API জিজ্ঞাসা করে কিন্তু অতিরিক্ত অনুরোধ এড়াতে ইনপুট ডিবাউন্স করে।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
`debounceTime` এবং`distinct`এর সাথে ডার্ট স্ট্রিমগুলি ব্যবহার করুন৷
**ধাপ 3: প্রয়োগ করুন**```dart
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

**ধাপ 4: পরীক্ষা**
যাচাই করুন যে দ্রুত টাইপিং ডিবাউন্স সময়ের পরে শুধুমাত্র একটি API কল ট্রিগার করে।
---

## সারাংশ
ডার্টের জীবনের উদ্দেশ্য হল ফ্লাটার। একটি স্বতন্ত্র ভাষা হিসাবে, এটি যোগ্য কিন্তু অসাধারণ। ফ্লটারের পিছনে ইঞ্জিন হিসাবে, এটি বিকাশকারীদেরকে একটি একক কোডবেস থেকে প্রতিটি প্রধান প্ল্যাটফর্মের জন্য সুন্দর, উচ্চ-পারফরম্যান্স অ্যাপ্লিকেশন তৈরি করতে সক্ষম করে। আপনি যদি ক্রস-প্ল্যাটফর্ম মোবাইল বা ডেস্কটপ অ্যাপ্লিকেশন তৈরি করেন, তবে ডার্ট + ফ্লাটার উপলব্ধ সেরা বিকল্পগুলির মধ্যে একটি। অন্য সব কিছুর জন্য, অন্যান্য ভাষা আরও উপযুক্ত।