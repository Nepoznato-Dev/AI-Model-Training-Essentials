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
# ডার্ট — ইডিওম্যাটিক প্যাটার্নস এবং সেরা অনুশীলন
এই নির্দেশিকাটি পরিচ্ছন্ন, ইডিওম্যাটিক ডার্ট কোড লেখার জন্য বাহাদুরি প্যাটার্ন এবং সর্বোত্তম অনুশীলনগুলি কভার করে।
---

## শূন্য নিরাপত্তা
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

## আধুনিক ডার্ট সিনট্যাক্স
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

## কনস্ট এবং অপরিবর্তনীয়তা
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

## অ্যাসিঙ্ক প্যাটার্ন
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

## এক্সটেনশন পদ্ধতি
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

## সারাংশ
ডার্ট ইডিয়মগুলি জোর দেয়: নাল সেফটি, কনস্ট্রাক্টর, রেকর্ড এবং প্যাটার্ন ম্যাচিং (ডার্ট 3), অ্যাসিঙ্ক/ওয়েট এবং এক্সটেনশন পদ্ধতি। কার্যকরী ডার্ট গাইড অনুসরণ করুন, বিন্যাসের জন্য`dart format`এবং লিন্টিংয়ের জন্য`dart analyze`ব্যবহার করুন। ডার্ট নিরাপত্তা এবং উৎপাদনশীলতাকে মূল্য দেয় — "একবার লিখুন, কোথাও দৌড়ান" ফ্লটারের সাথে।