<!--
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

-->
# Dart — Informacje o składni
Ten dokument zawiera kompleksowe, uporządkowane omówienie składni Darta (3.x). Uzupełnia główne odniesienia do Darta, koncentrując się na wyczerpujących wzorcach składni, bezpieczeństwie zerowym, programowaniu asynchronicznym i wzorcach projektowych zorientowanych na Flutter.
---

## Operatory i wyrażenia
### Główni operatorzy
| Operator | Imię | Przykład | Notatki |
|---------|------|---------|-------|
| `+``-``*``/``%``~/` | Arytmetyka | `7 ~/ 3`| `~/`to dzielenie liczb całkowitych |
| `==``!=` | Równość | `a == b`| |
| `<``>``<=``>=` | Porównanie | `a >= b`| |
| `&&``\|\|``!`| Logiczne | `a && b`| Zwarcie |
| `??`| Połączenie zerowe | `a ?? b`|  `b`, jeśli`a`ma wartość null |
| `?.`| Dostęp z uwzględnieniem wartości null | `a?.b`| null, jeśli`a`ma wartość null |
| `!`| Twierdzenie zerowe | `a!`| Zgłasza, jeśli null |
| `..``?..` | Kaskada | `obj..a..b`| Operacje łańcuchowe na tym samym obiekcie |
| `??=`| Przypisanie z uwzględnieniem wartości null | `a ??= b`| Przypisz, jeśli null |
| `as`| Wpisz obsada | `obj as String`| Rzuca na niepowodzenie |
| `is``is!` | Test typu | `obj is String`| |
| `=>`| Funkcja strzałki | `() => expr`| |
### Notacja kaskadowa
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

## Kontroluj przepływ
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

## Zerowe bezpieczeństwo
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

## Zajęcia i OOP
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

## Programowanie asynchroniczne
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

## Ogólne i kolekcje
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

## Metody i wzorce rozszerzeń
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

## Streszczenie
Składnia Darta jest czysta, spójna i zaprojektowana z myślą o produktywności. Solidne bezpieczeństwo zerowe eliminuje błędy referencyjne zerowe w czasie kompilacji. Async/await i strumienie zapewniają naturalne wzorce programowania asynchronicznego. Klasy, miksy i klasy zapieczętowane umożliwiają elastyczną kompozycję obiektów. Dopasowywanie wzorców, rekordy i modyfikatory klas Dart 3 dodają wyrazistości. Chociaż głównym celem Darta jest Flutter, jego składnia jest dobrze dostosowana do dowolnej domeny aplikacji — po stronie serwera (z Dart Frog lub Shelf), narzędzi CLI i aplikacji internetowych (skompilowanych do JavaScript).