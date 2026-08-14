---
# Metadata
title: "Dart — Syntax Reference"
description: "Detailed syntax reference for Dart covering null safety, async/await, classes, mixins, isolates, and Flutter-oriented patterns."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [dart, syntax-reference, null-safety, async, oop, flutter, isolates, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# डार्ट - सिंटेक्स संदर्भ
यह दस्तावेज़ डार्ट (3.x) के लिए एक व्यापक, संरचित वाक्यविन्यास संदर्भ प्रदान करता है। यह संपूर्ण सिंटैक्स पैटर्न, अशक्त सुरक्षा, एसिंक प्रोग्रामिंग और फ़्लटर-उन्मुख डिज़ाइन पैटर्न पर ध्यान केंद्रित करके मुख्य डार्ट संदर्भ को पूरक करता है।
---

## ऑपरेटर्स और अभिव्यक्तियाँ
### कोर ऑपरेटर्स
| ऑपरेटर | नाम | उदाहरण | नोट्स |
|-------|------|------|-------|
| `+``-``*``/``%``~/` | अंकगणित | `7 ~/ 3`| `~/`पूर्णांक विभाजन है |
| `==``!=` | समानता | `a == b`| |
| `<``>``<=``>=` | तुलना | `a >= b`| |
| `&&``\|\|``!`| तार्किक | `a && b`| शॉर्ट-सर्किट |
| `??`| अशक्त संलयन | `a ?? b`| `b`यदि`a`शून्य है |
| `?.`| शून्य-जागरूक पहुँच | `a?.b`| यदि`a`शून्य है तो शून्य |
| `!`| शून्य दावा | `a!`| शून्य होने पर फेंकता है |
| `..``?..` | कैस्केड | `obj..a..b`| एक ही वस्तु पर श्रृंखला संचालन |
| `??=`| अशक्त-जागरूक असाइन करें | `a ??= b`| यदि शून्य हो तो असाइन करें |
| `as`| कास्ट टाइप करें | `obj as String`| असफलता पर वार करता है |
| `is``is!` | टाइप टेस्ट | `obj is String`| |
| `=>`| एरो फ़ंक्शन | `() => expr`| |
### कैस्केड नोटेशन
```dart
// Cascade — chain operations on same object
var button = Button()
  ..text = 'Click me'
  ..style = 'primary'
  ..onClick.listen((_) => print('Clicked!'));

// Null-aware cascade
account?.address
  ..street = '123 Main St'
  ..city = 'Springfield';
```

---

## प्रवाह को नियंत्रित करें
```dart
// if / else if / else
if (score >= 90) {
  grade = 'A';
} else if (score >= 80) {
  grade = 'B';
} else {
  grade = 'F';
}

// Switch with pattern matching (Dart 3)
switch (shape) {
  case Circle(radius: var r) when r > 0:
    print('Valid circle with radius $r');
  case Rectangle(width: var w, height: var h):
    print('Rectangle ${w}x$h');
  case _:
    print('Unknown shape');
}

// Switch expression (Dart 3)
final label = switch (status) {
  Status.active => 'Active',
  Status.pending => 'Pending',
  Status.inactive => 'Inactive',
};

// For loops
for (var item in items) {
  print(item);
}

for (var i = 0; i < 10; i++) {
  print(i);
}

// While
while (condition) {
  doSomething();
}

// Break and continue
for (var item in items) {
  if (item == 'skip') continue;
  if (item == 'stop') break;
  process(item);
}
```

---

## अशक्त सुरक्षा
```dart
// Non-nullable by default
String name = 'Alice';     // Cannot be null
// name = null;             // Compile error!

// Nullable types
String? nickname;           // Can be null
int? age = null;            // OK

// Null-aware operators
int len = name?.length ?? 0;          // Safe access + default
String display = nickname ?? 'N/A';   // Elvis operator
nickname ??= 'Default';               // Assign if null

// Null assertion (use sparingly)
String forced = nullableString!;      // Throws if null

// Late initialization
late final Config config;             // Must be set before first read
config = loadConfig();

// Flow analysis
void check(String? value) {
  if (value == null) return;
  // value is promoted to String here
  print(value.length);
}
```

---

## कक्षाएं और ओओपी
```dart
// Class with constructor
class User {
  final String name;
  final String email;
  int age;

  User(this.name, this.email, {this.age = 0});

  // Named constructor
  User.fromJson(Map<String, dynamic> json)
      : name = json['name'],
        email = json['email'],
        age = json['age'] ?? 0;

  // Method
  String greet() => 'Hello, I\'m $name';

  // Getter/setter
  String get displayName => name.toUpperCase();
  set age(int value) {
    if (value < 0) throw ArgumentError('Age cannot be negative');
    age = value;
  }

  @override
  String toString() => 'User($name, $email)';
}

// Abstract class
abstract class Animal {
  String get name;
  void speak();
}

// Mixin
mixin Flyable {
  void fly() => print('$this is flying');
}

mixin Swimmable {
  void swim() => print('$this is swimming');
}

// Multiple inheritance via mixins
class Duck extends Animal with Flyable, Swimmable {
  @override
  String get name => 'Duck';

  @override
  void speak() => print('Quack!');
}

// Enum with methods (Dart 3)
enum Status {
  active('Currently active'),
  pending('Awaiting activation'),
  inactive('Disabled');

  final String description;
  const Status(this.description);
}

// Sealed classes (Dart 3)
sealed class Result<T> {}
class Success<T> extends Result<T> {
  final T value;
  Success(this.value);
}
class Failure<T> extends Result<T> {
  final String error;
  Failure(this.error);
}
```

---

## एसिंक प्रोग्रामिंग
```dart
// Future — single async value
Future<String> fetchName() async {
  await Future.delayed(Duration(seconds: 1));
  return 'Alice';
}

// async/await
Future<void> main() async {
  final name = await fetchName();
  print('Hello, $name!');
}

// Stream — multiple async values
Stream<int> counter() async* {
  for (int i = 0; i < 10; i++) {
    await Future.delayed(Duration(seconds: 1));
    yield i;
  }
}

// Consuming streams
await for (final value in counter()) {
  print(value);
}

// Stream transformations
counter()
  .where((n) => n.isEven)
  .map((n) => n * n)
  .listen(print);

// Future.wait — parallel execution
final results = await Future.wait([
  fetchUser(1),
  fetchPosts(1),
  fetchNotifications(),
]);

// Completer — manual future control
final completer = Completer<String>();
// Later: completer.complete('done');
// Or: completer.completeError(error);
```

---

## जेनेरिक और संग्रह
```dart
// Generic class
class Stack<T> {
  final List<T> _items = [];
  void push(T item) => _items.add(item);
  T pop() => _items.removeLast();
  T get peek => _items.last;
  bool get isEmpty => _items.isEmpty;
}

// Generic method
T first<T>(List<T> items) => items.first;

// List
var list = [1, 2, 3, 4, 5];
list.map((x) => x * 2).toList();
list.where((x) => x > 3).toList();
list.fold(0, (sum, x) => sum + x);
list.reduce((a, b) => a + b);

// Map
var map = {'a': 1, 'b': 2};
map['c'] = 3;
map.putIfAbsent('d', () => 4);
map.forEach((key, value) => print('$key: $value'));

// Set
var set = {1, 2, 3};
set.add(4);
set.contains(3);
set.union({4, 5, 6});
set.intersection({2, 3, 4});

// Spread operator
var combined = [...list1, ...list2, 99];
var merged = {...map1, ...map2};
```

---

## विस्तार के तरीके और पैटर्न
```dart
// Extension methods
extension StringExtras on String {
  String get capitalized => '${this[0].toUpperCase()}${substring(1)}';
  bool get isEmail => contains(RegExp(r'@.+\..+'));
  String truncate(int max) => length > max ? '${substring(0, max)}...' : this;
}

'hello'.capitalized  // 'Hello'

// Extension on nullable
extension IntX on int? {
  bool get isPositive => this != null && this! > 0;
}

// Records / patterns (Dart 3)
var (name, age) = ('Alice', 30);  // destructuring

// Pattern matching with switch
switch (obj) {
  case int n when n > 0:
    print('Positive: $n');
  case String s:
    print('String: ${s.length}');
  case [var first, ...var rest]:
    print('List: first=$first, rest=$rest');
}

// Isolates (background threads)
Future<int> heavyComputation() async {
  return await compute((_) {
    // Runs in a separate isolate
    int sum = 0;
    for (int i = 0; i < 1000000; i++) sum += i;
    return sum;
  }, null);
}
```

---

## सारांश
डार्ट का सिंटैक्स साफ़, सुसंगत और उत्पादकता के लिए डिज़ाइन किया गया है। ध्वनि शून्य सुरक्षा संकलन समय पर शून्य संदर्भ त्रुटियों को समाप्त करती है। Async/प्रतीक्षा और स्ट्रीम अतुल्यकालिक प्रोग्रामिंग के लिए प्राकृतिक पैटर्न प्रदान करते हैं। कक्षाएं, मिक्सिन और सीलबंद कक्षाएं लचीली वस्तु संरचना को सक्षम बनाती हैं। डार्ट 3 का पैटर्न मिलान, रिकॉर्ड और वर्ग संशोधक अभिव्यंजकता जोड़ते हैं। जबकि डार्ट का प्राथमिक उद्देश्य फ़्लटर है, इसका सिंटैक्स किसी भी एप्लिकेशन डोमेन - सर्वर-साइड (डार्ट फ्रॉग या शेल्फ़ के साथ), सीएलआई टूल और वेब एप्लिकेशन (जावास्क्रिप्ट पर संकलित) के लिए उपयुक्त है।