---
# Metadata
title: "Dart — Cheat Sheet"
description: "Quick-reference cheat sheet for Dart syntax, null safety, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [dart, flutter, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Dardo - Hoja de trucos
## Conceptos básicos
```dart
// Variables
var name = 'Alice';       // type inferred
String city = 'NYC';      // explicit type
final age = 30;           // immutable (runtime)
const pi = 3.14159;       // compile-time constant
late String lazy;         // initialized later

// Nullable
String? email;            // can be null
int? phone;

// Types
int x = 42;
double pi = 3.14;
bool active = true;
String s = 'hello';
List<int> nums = [1, 2, 3];
Map<String, int> scores = {'alice': 90};
Set<int> unique = {1, 2, 3};

// String interpolation
'Hello, $name!'
'Age: ${age + 1}'
'Pi: ${pi.toStringAsFixed(2)}'

// String methods
name.length
name.toUpperCase()
name.toLowerCase()
name.trim()
name.contains('lic')
name.replaceAll('Alice', 'Bob')
name.substring(0, 3)
name.split('')
'  hi  '.trim()
```

## Seguridad nula
```dart
// Null-aware operators
String? email;
email?.length;           // null if email is null
email ?? 'default';      // coalesce
email!.length;           // force unwrap (avoid)

// Cascade
var button = Button()
  ..text = 'Click'
  ..color = Colors.blue
  ..onPressed = () {};

// if-null
var value = email ?? 'N/A';
```

## Colecciones
```dart
// List
var list = [1, 2, 3];
list.add(4);
list.insert(0, 0);
list[0];
list.length;
list.remove(3);
list.map((x) => x * 2).toList();
list.where((x) => x > 2);
list.reduce((a, b) => a + b);
list.forEach((x) => print(x));
list.sort();
list.first;
list.last;

// Spread & collection-if
var combined = [...list, 5, 6];
var filtered = [if (active) 'active', ...items];

// Map
var map = {'alice': 90, 'bob': 85};
map['charlie'] = 78;
map['alice'];
map.containsKey('alice');
map.keys;
map.values;
map.map((k, v) => MapEntry(k.toUpperCase(), v * 2));

// Set
var set = {1, 2, 3};
set.add(4);
set.contains(2);
set.union({5, 6});
```

## Controlar el flujo
```dart
if (condition) {
  // ...
} else if (other) {
  // ...
} else {
  // ...
}

// Ternary
var result = condition ? 'yes' : 'no';

// Switch expression (Dart 3)
var label = switch (status) {
  'active'   => 'Active',
  'inactive' => 'Inactive',
  _          => 'Unknown',
};

// Pattern matching (Dart 3)
switch (shape) {
  case Circle(radius: var r):
    print('Circle r=$r');
  case Rectangle(width: var w, height: var h):
    print('${w}x$h');
}

// if-case (Dart 3)
if (obj is String s && s.isNotEmpty) {
  print(s);
}

// Loops
for (var item in collection) { ... }
for (var i = 0; i < 10; i++) { ... }
for (var (i, v) in list.indexed) { ... }  // Dart 3
while (condition) { ... }
collection.forEach((item) { ... });
```

## Clases y registros
```dart
// Class
class User {
  final String name;
  int age;

  User(this.name, this.age);

  User.fromJson(Map<String, dynamic> json)
      : name = json['name'],
        age = json['age'];

  Map<String, dynamic> toJson() => {'name': name, 'age': age};

  @override
  String toString() => 'User($name, $age)';
}

// Record (Dart 3)
var point = (1.0, 2.0);
var (x, y) = point;  // destructure
var (name: n, age: a) = (name: 'Alice', age: 30);

// Sealed class (Dart 3)
sealed class Shape {}
class Circle extends Shape {
  final double radius;
  Circle(this.radius);
}
class Rectangle extends Shape {
  final double width, height;
  Rectangle(this.width, this.height);
}
```

## Asíncrono
```dart
// Future
Future<String> fetchData() async {
  final response = await http.get(Uri.parse(url));
  return response.body;
}

// Stream
Stream<int> countStream(int max) async* {
  for (int i = 0; i < max; i++) {
    await Future.delayed(Duration(seconds: 1));
    yield i;
  }
}

// Listen
stream.listen((data) => print(data));

// StreamBuilder (Flutter)
StreamBuilder<int>(
  stream: countStream(10),
  builder: (context, snapshot) {
    return Text('${snapshot.data}');
  },
)
```

## Funciones y cierres
```dart
// Function
int add(int a, int b) => a + b;

// Arrow function
var square = (int x) => x * x;

// Optional & named params
void greet(String name, {String greeting = 'Hello'}) {
  print('$greeting, $name!');
}
greet('Alice', greeting: 'Hi');

// Positional optional
void log(String msg, [String? prefix]) {
  print('${prefix ?? ""} $msg');
}

// Extension
extension StringExt on String {
  bool get isEmail => contains('@');
  String capitalize() => '${this[0].toUpperCase()}${substring(1)}';
}
```

## Manejo de errores
```dart
try {
  var result = riskyOperation();
} on FormatException catch (e) {
  print('Format error: $e');
} catch (e) {
  print('Error: $e');
} finally {
  cleanup();
}

// Rethrow
catch (e) {
  log(e);
  rethrow;
}

// Custom exception
class NotFoundException implements Exception {
  final String id;
  NotFoundException(this.id);
  @override
  String toString() => 'Not found: $id';
}
```
