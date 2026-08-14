<!--
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

-->
# Phi tiêu — Các mẫu thành ngữ & các phương pháp hay nhất
Hướng dẫn này bao gồm các mẫu thành ngữ và các phương pháp hay nhất để viết mã Dart rõ ràng, thành ngữ.
---

## Không an toàn
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

## Cú pháp phi tiêu hiện đại
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

## Hằng số & Tính bất biến
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

## Mẫu không đồng bộ
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

## Phương pháp mở rộng
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

## Bản tóm tắt
Thành ngữ Dart nhấn mạnh: an toàn null, hàm tạo const, bản ghi và khớp mẫu (Dart 3), async/await và các phương thức mở rộng. Làm theo hướng dẫn Phi tiêu hiệu quả, sử dụng`dart format`để định dạng và`dart analyze`để tạo linting. Dart coi trọng sự an toàn và năng suất — "viết một lần, chạy mọi nơi" với Flutter.