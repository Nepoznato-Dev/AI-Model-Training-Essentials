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

# ডার্ট — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই দস্তাবেজটি সংশোধন সহ ডার্টের সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে।
---

## 1. শূন্য নিরাপত্তা অপব্যবহার
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

## 2. ত্রুটি হ্যান্ডলিং ছাড়াই অ্যাসিঙ্ক/অপেক্ষা করুন
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

## 3.`const`কনস্ট্রাক্টর ব্যবহার করছেন না
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

## 4.`hashCode`ছাড়া `==`
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

## 5. স্প্রেড এবং সংগ্রহ ব্যবহার করছেন না-যদি
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

## 6. অ্যান্টি-প্যাটার্ন: ম্যাসিভ স্টেটফুল উইজেট
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

## সারাংশ
ডার্টের নাল নিরাপত্তা শক্তিশালী — এটিকে`!`দিয়ে পরাজিত করবেন না। ক্যানোনিকাল দৃষ্টান্তের জন্য`const`কনস্ট্রাক্টর ব্যবহার করুন, সর্বদা`==`দিয়ে`hashCode`ওভাররাইড করুন, সংক্ষিপ্ত তালিকা তৈরির জন্য সংগ্রহ-ইফ এবং স্প্রেড অপারেটর ব্যবহার করুন এবং উইজেটগুলি থেকে ব্যবসায়িক যুক্তি বের করুন৷ ডার্ট পুরষ্কার পরিষ্কার, নাল-নিরাপদ, কনস্ট-সঠিক কোড।