---
# Metadata
title: "Dart — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Dart with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [dart, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# ڈارٹ - عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز تصحیح کے ساتھ ڈارٹ میں سب سے عام غلطیوں، ٹریپس اور اینٹی پیٹرن کی فہرست بناتی ہے۔
---

## 1. کالعدم حفاظتی غلط استعمال
```dart
// ❌ WRONG — force unwrap
String name = user!.name;  // throws if user is null

// ✅ CORRECT — null-aware operators
String? name = user?.name;
String name = user?.name ?? 'Unknown';

// ✅ CORRECT — late with initialization guarantee
late final String name;
void init(String n) { name = n; }
```

---

## 2. غلطی سے نمٹنے کے بغیر Async/انتظار کریں۔
```dart
// ❌ WRONG — unhandled Future errors
Future<void> loadData() async {
  final data = await api.fetchData();  // throws on network error
  process(data);
}

// ✅ CORRECT — try/catch
Future<void> loadData() async {
  try {
    final data = await api.fetchData();
    process(data);
  } on SocketException catch (e) {
    print('Network error: $e');
  } catch (e) {
    print('Error: $e');
  }
}
```

---

## 3.`const`کنسٹرکٹرز استعمال نہیں کرنا
```dart
// ❌ WRONG — creating new instances unnecessarily
class Point {
  final double x, y;
  Point(this.x, this.y);  // always allocates
}

// ✅ CORRECT — const constructor
class Point {
  final double x, y;
  const Point(this.x, this.y);
}
final a = const Point(1, 2);
final b = const Point(1, 2);
identical(a, b);  // true — same instance
```

---

## 4.`==`بغیر`hashCode`کے
```dart
// ❌ WRONG — breaks Set/Map
class User {
  final String name;
  User(this.name);
  @override
  bool operator ==(Object other) =>
      other is User && other.name == name;
  // Missing hashCode!
}

// ✅ CORRECT — override both
class User {
  final String name;
  User(this.name);
  @override
  bool operator ==(Object other) =>
      other is User && other.name == name;
  @override
  int get hashCode => name.hashCode;
}
```

---

## 5. اسپریڈ اور کلیکشن کا استعمال نہیں کرنا-اگر
```dart
// ❌ WRONG — verbose list building
List<Widget> buildList(bool showExtra) {
  var items = [Text('A'), Text('B')];
  if (showExtra) {
    items.add(Text('C'));
  }
  items.addAll([Text('D'), Text('E')]);
  return items;
}

// ✅ CORRECT — collection operators
List<Widget> buildList(bool showExtra) => [
  const Text('A'),
  const Text('B'),
  if (showExtra) const Text('C'),
  ...[const Text('D'), const Text('E')],
];
```

---

## 6. اینٹی پیٹرن: بڑے پیمانے پر اسٹیٹفول ویجیٹ
```dart
// ❌ WRONG — everything in one widget
class MyPage extends StatefulWidget { ... }
// 500+ lines of state management, API calls, UI

// ✅ CORRECT — extract logic to BLoC/Provider
class MyPage extends StatelessWidget {
  @override
  Widget build(context) {
    return BlocBuilder<MyBloc, MyState>(
      builder: (context, state) => MyPageContent(state: state),
    );
  }
}
```

---

## خلاصہ
ڈارٹ کی نال سیفٹی طاقتور ہے — اسے`!`کے ساتھ شکست نہ دیں۔ کینونیکل مثالوں کے لیے`const`کنسٹرکٹرز کا استعمال کریں، ہمیشہ`hashCode`کو`==`کے ساتھ اوور رائیڈ کریں، جامع فہرست بنانے کے لیے کلیکشن-اگر اور اسپریڈ آپریٹرز کا استعمال کریں، اور ویجیٹس سے کاروباری منطق نکالیں۔ ڈارٹ انعامات صاف، null-safe، const- درست کوڈ دیتا ہے۔