---
# Metadata
title: "Dart — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic Dart code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [dart, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Dart — รูปแบบสำนวนและแนวทางปฏิบัติที่ดีที่สุด
คู่มือนี้ครอบคลุมถึงรูปแบบสำนวนและแนวปฏิบัติที่ดีที่สุดในการเขียนโค้ด Dart ที่มีสำนวนสะอาดตา
---

## ความปลอดภัยเป็นศูนย์
```dart
// ✅ Non-nullable by default
String name = 'Alice';  // cannot be null

// ✅ Nullable types
String? middleName;  // can be null

// ✅ Null-aware operators
final city = user?.address?.city ?? 'Unknown';
final length = name?.length ?? 0;

// ✅ Late initialization
late final Config config;  // initialized before first use

// ✅ Null assertion (only when certain)
final value = nullableValue!;
```

---

## ไวยากรณ์โผสมัยใหม่
```dart
// ✅ Records (Dart 3)
(String, int) getUser() => ('Alice', 30);
var (name, age) = getUser();

// ✅ Pattern matching (Dart 3)
switch (shape) {
  case Circle(radius: var r) when r > 0:
    print('Circle with radius $r');
  case Rectangle(width: var w, height: var h):
    print('Rectangle ${w}x$h');
}

// ✅ Sealed classes (Dart 3)
sealed class Result<T> {}
class Success<T> extends Result<T> {
  final T value;
  Success(this.value);
}
class Failure<T> extends Result<T> {
  final Object error;
  Failure(this.error);
}

// ✅ Collection if/for
Widget build(BuildContext context) {
  return Column(
    children: [
      if (isLoggedIn) const UserAvatar(),
      for (var item in items) ListTile(title: Text(item.name)),
    ],
  );
}
```

---

## Const & ความไม่เปลี่ยนรูป
```dart
// ✅ const constructors
class Point {
  final double x, y;
  const Point(this.x, this.y);
}

const origin = Point(0, 0);

// ✅ const collections
const colors = ['red', 'green', 'blue'];
const config = {'host': 'localhost', 'port': 8080};

// ✅ final for immutable references
final user = User(name: 'Alice');
```

---

## รูปแบบอะซิงก์
```dart
// ✅ async/await
Future<User> fetchUser(int id) async {
  final response = await http.get(Uri.parse('/api/users/$id'));
  return User.fromJson(jsonDecode(response.body));
}

// ✅ Stream for async sequences
Stream<int> countStream(int max) async* {
  for (int i = 0; i < max; i++) {
    yield i;
    await Future.delayed(Duration(seconds: 1));
  }
}

// ✅ Future.wait for parallel execution
final results = await Future.wait([
  fetchUsers(),
  fetchPosts(),
  fetchComments(),
]);
```

---

## วิธีการขยาย
```dart
extension StringExtensions on String {
  bool get isEmail => contains('@') && contains('.');
  String get capitalized => isEmpty ? this : '${this[0].toUpperCase()}${substring(1)}';
}

extension ListExtensions<T> on List<T> {
  T? get firstOrNull => isEmpty ? null : first;
  List<T> takeWhile(bool Function(T) test) => [...where(test)];
}
```

---

## สรุป
สำนวน Dart เน้น: ความปลอดภัยแบบ null, ตัวสร้าง const, บันทึกและการจับคู่รูปแบบ (Dart 3), async/await และวิธีการขยาย ปฏิบัติตามคำแนะนำ Effective Dart ใช้`dart format`สำหรับการจัดรูปแบบ และใช้`dart analyze`สำหรับ Linting Dart ให้ความสำคัญกับความปลอดภัยและประสิทธิภาพการทำงาน — "เขียนครั้งเดียว ทำงานได้ทุกที่" ด้วย Flutter