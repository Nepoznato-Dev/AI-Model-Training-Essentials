---
# मेटाडेटा
शीर्षक: "डार्ट"
विवरण: "डार्ट प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स बुनियादी बातें, पारिस्थितिकी तंत्र और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [डार्ट, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का_समय: "40 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
#डार्ट
डार्ट Google द्वारा विकसित एक क्लाइंट-अनुकूलित प्रोग्रामिंग भाषा है, जिसे पहली बार 2013 में जारी किया गया था। जबकि डार्ट को शुरू में वेब ब्राउज़र के लिए संभावित जावास्क्रिप्ट प्रतिस्थापन के रूप में तैनात किया गया था, इसे अपना प्राथमिक उद्देश्य **फ़्लटर** के पीछे की भाषा के रूप में मिला - एक ही कोडबेस से मोबाइल, वेब, डेस्कटॉप और एम्बेडेड एप्लिकेशन बनाने के लिए Google का क्रॉस-प्लेटफ़ॉर्म यूआई टूलकिट।
डार्ट आधुनिक भाषाओं की सर्वोत्तम विशेषताओं को जोड़ता है: यह ऑब्जेक्ट-ओरिएंटेड है, इसमें वैकल्पिक टाइपिंग है (डार्ट 3 के बाद से ध्वनि शून्य सुरक्षा),`async`/`await`के साथ अतुल्यकालिक प्रोग्रामिंग का समर्थन करता है, और मूल मशीन कोड (मोबाइल/डेस्कटॉप के लिए) और जावास्क्रिप्ट (वेब ​​के लिए) दोनों के लिए संकलित करता है।
---

## डार्ट क्यों मायने रखता है
- **फ़्लटर**: फ़्लटर के लिए प्राथमिक भाषा - सबसे तेज़ी से बढ़ते क्रॉस-प्लेटफ़ॉर्म फ़्रेमवर्क में से एक।
- **क्रॉस-प्लेटफ़ॉर्म**: iOS, Android, वेब, Windows, macOS, Linux और एम्बेडेड डिवाइस के लिए सिंगल कोडबेस।
- **उत्पादक**: हॉट रीलोड, समृद्ध विजेट लाइब्रेरी और अभिव्यंजक सिंटैक्स यूआई विकास को तेज़ बनाते हैं।
- **ध्वनि शून्य सुरक्षा**: संकलन-समय शून्य सुरक्षा शून्य संदर्भ त्रुटियों को समाप्त करती है।
- **प्रदर्शन**: मोबाइल के लिए मूल एआरएम कोड को संकलित करता है; किसी पुल की जरूरत नहीं.
- **बढ़ता पारिस्थितिकी तंत्र**: फ़्लटर का पैकेज पारिस्थितिकी तंत्र तेजी से विस्तार कर रहा है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **स्पंदन-केन्द्रित** | डार्ट का अधिकांश उपयोग फ़्लटर है; इसके बाहर सीमित | स्पंदन के लिए उपयोग करें; गैर-यूआई कार्य के लिए अन्य भाषाएँ |
| **छोटा पारिस्थितिकी तंत्र** | रिएक्ट नेटिव या नेटिव प्लेटफॉर्म की तुलना में कम पैकेज | तेजी से बढ़ रहा है; देशी एपीआई के लिए प्लेटफ़ॉर्म चैनल |
| **वेब प्रदर्शन** | WASM में संकलित डार्ट अभी भी परिपक्व हो रहा है | लगातार प्रदर्शन के लिए CanvasKit रेंडरर का उपयोग करें |
| **नौकरी बाज़ार** | स्पंदन भूमिकाएँ मौजूद हैं लेकिन देशी मोबाइल से कम | क्रॉस-प्लेटफ़ॉर्म डेवलपर्स की बढ़ती मांग |
| **बैकएंड के लिए नहीं** | संभव (सर्वर-साइड डार्ट) लेकिन उपयोग का मामला नहीं | बैकएंड के लिए Go, Node.js, Python का उपयोग करें |
---

## सिंटेक्स बुनियादी बातें
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

## उन्नत सिंटैक्स और पैटर्न
### अशक्त सुरक्षा - गहरा गोता
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

### मिश्रण
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

### एक्सटेंशन
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

### आइसोलेट्स (समवर्ती)
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
### एनोटेशन और कोड जनरेशन
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

## मुख्य विशेषताओं में गहराई से उतरें
### स्ट्रीम हैंडलिंग
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

### स्पंदन विजेट पैटर्न
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### पबस्पेक.yaml
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

### विश्लेषण_विकल्प.yaml
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

## परीक्षण
### परीक्षण पैकेज के साथ यूनिट परीक्षण
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

### स्पंदन_परीक्षण के साथ विजेट परीक्षण
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

### मॉकिटो के साथ मजाक करना
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

## अंतरसंचालनीयता
### एफएफआई (विदेशी फ़ंक्शन इंटरफ़ेस)
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

### प्लेटफार्म चैनल (स्पंदन)
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

### जावास्क्रिप्ट इंटरऑप (डार्ट वेब)
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

## डिज़ाइन पैटर्न
### पैटर्न 1: रिपॉजिटरी पैटर्न
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

### पैटर्न 2: प्रदाता राज्य प्रबंधन
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

### पैटर्न 3: बीएलओसी (बिजनेस लॉजिक कंपोनेंट)
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

## प्रदर्शन एवं अनुकूलन
### एओटी बनाम जेआईटी संकलन
| मोड | जब उपयोग किया जाता है | स्टार्टअप | रनटाइम | केस का प्रयोग करें |
|------|-----|--|---|---|
| **जीत** (जस्ट-इन-टाइम) | विकास, डिबग मोड | तेज | थोड़ा धीमा | विकास के दौरान गर्म पुनः लोड |
| **एओटी** (समय से पहले) | रिलीज़ बिल्ड | थोड़ा धीमा | तेज़ | मोबाइल/डेस्कटॉप ऐप्स का उत्पादन |
| **जेएस** | वेब लक्ष्य | निर्भर करता है | बदलता रहता है | स्पंदन वेब अनुप्रयोग |
| **WASM** | वेब (प्रयोगात्मक) | निर्भर करता है | तेज | भविष्य का वेब लक्ष्य |
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

## तैनाती
### स्पंदन परिनियोजन लक्ष्य
| प्लेटफार्म | बिल्ड कमांड | आउटपुट |
|---|----|--------|
| **एंड्रॉइड** |  __संरक्षित_0__ / __संरक्षित_1__ | प्ले स्टोर के लिए एपीके/एएबी |
| **आईओएस** |  __संरक्षित_2__ | ऐप स्टोर के लिए आईपीए |
| **वेब** |  __संरक्षित_3__ | स्टेटिक HTML/JS/CSS |
| **विंडोज़** |  __संरक्षित_4__ | MSIX या स्टैंडअलोन exe |
| **मैकओएस** |  __संरक्षित_5__ | .ऐप बंडल |
| **लिनक्स** |  __संरक्षित_6__ | बाइनरी + संपत्ति |
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

## डार्ट का उपयोग कब करें
| परिदृश्य | क्यों डार्ट (फड़फड़ाना) | बेहतर विकल्प |
|---|-------------------|-----|
| क्रॉस-प्लेटफ़ॉर्म मोबाइल ऐप्स | स्पंदन उत्कृष्ट है | रिएक्ट नेटिव, नेटिव स्विफ्ट/कोटलिन |
| क्रॉस-प्लेटफ़ॉर्म डेस्कटॉप | स्पंदन इसका समर्थन करता है | इलेक्ट्रॉन, सी#, एवलोनिया |
| वेब अनुप्रयोग | स्पंदन वेब मौजूद है | बेहतर वेब ऐप्स के लिए रिएक्ट, व्यू, एंगुलर |
| एंबेडेड यूआई | एंबेडेड के लिए स्पंदन | सी, एलवीजीएल |
| बैकएंड विकास | प्राथमिक उपयोग का मामला नहीं | जाओ, नोड.जेएस, पायथन |
| डेटा साइंस/एमएल | अनुकूल नहीं | पायथन, आर |
| सिस्टम प्रोग्रामिंग | अनुकूल नहीं | सी, सी++, जंग |
---

## सारांश
जीवन में डार्ट का उद्देश्य फ़्लटर है। एक स्टैंडअलोन भाषा के रूप में, यह सक्षम है लेकिन अचूक है। फ़्लटर के पीछे के इंजन के रूप में, यह डेवलपर्स को एक ही कोडबेस से हर प्रमुख प्लेटफ़ॉर्म के लिए सुंदर, उच्च-प्रदर्शन एप्लिकेशन बनाने में सक्षम बनाता है। यदि आप क्रॉस-प्लेटफ़ॉर्म मोबाइल या डेस्कटॉप एप्लिकेशन बना रहे हैं, तो डार्ट + फ़्लटर उपलब्ध सर्वोत्तम विकल्पों में से एक है। बाकी सभी चीज़ों के लिए, अन्य भाषाएँ अधिक उपयुक्त हैं।