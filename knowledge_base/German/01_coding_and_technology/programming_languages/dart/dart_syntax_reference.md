---
# Metadata
title: "Dart — Syntax Reference"
description: "Detailed syntax reference for Dart covering null safety, async/await, classes, mixins, isolates, and Flutter-oriented patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "AI Model Training Team"
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

# Dart – Syntaxreferenz
Dieses Dokument bietet eine umfassende, strukturierte Syntaxreferenz für Dart (3.x). Es ergänzt die Hauptreferenz von Dart, indem es sich auf umfassende Syntaxmuster, Nullsicherheit, asynchrone Programmierung und Flutter-orientierte Entwurfsmuster konzentriert.
---

## Operatoren und Ausdrücke
### Kernbetreiber
| Betreiber | Name | Beispiel | Notizen |
|----------|------|---------|-------|
| `+``-``*``/``%``~/` | Arithmetik | `7 ~/ 3`| `~/`ist eine ganzzahlige Division |
| `==``!=` | Gleichheit | `a == b`| |
| `<``>``<=``>=` | Vergleich | `a >= b`| |
| `&&``\|\|``!`| Logisch | `a && b`| Kurzschluss |
| `??`| Null-Koaleszenz | `a ?? b`|  `b`, wenn`a`null ist |
| `?.`| Null-bewusster Zugriff | `a?.b`| null, wenn`a`null ist |
| `!`| Null-Behauptung | `a!`| Wird ausgelöst, wenn null |
| `..``?..` | Kaskade | `obj..a..b`| Kettenoperationen für dasselbe Objekt |
| `??=`| Nullbewusste Zuweisung | `a ??= b`| Zuweisen, wenn null |
| `as`| Geben Sie Besetzung | ein `obj as String`| Wirft bei Misserfolg |
| `is``is!` | Typprüfung | `obj is String`| |
| `=>`| Pfeilfunktion | `() => expr`| |
### Kaskadennotation
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

## Kontrollfluss
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

## Null Sicherheit
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

## Klassen & OOP
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

## Asynchrone Programmierung
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

## Generika und Sammlungen
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

## Erweiterungsmethoden und -muster
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

## Zusammenfassung
Die Syntax von Dart ist sauber, konsistent und auf Produktivität ausgelegt. Solide Nullsicherheit eliminiert Nullreferenzfehler zur Kompilierungszeit. Async/await und Streams bieten natürliche Muster für die asynchrone Programmierung. Klassen, Mixins und versiegelte Klassen ermöglichen eine flexible Objektzusammensetzung. Der Mustervergleich, die Datensätze und die Klassenmodifikatoren von Dart 3 sorgen für mehr Ausdruckskraft. Obwohl der Hauptzweck von Dart Flutter ist, eignet sich seine Syntax gut für jede Anwendungsdomäne – serverseitig (mit Dart Frog oder Shelf), CLI-Tools und Webanwendungen (kompiliert zu JavaScript).