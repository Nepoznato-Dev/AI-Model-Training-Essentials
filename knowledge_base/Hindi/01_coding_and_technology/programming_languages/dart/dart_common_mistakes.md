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

# डार्ट - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ डार्ट में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है।
---

## 1. अशक्त सुरक्षा दुरुपयोग
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

## 2. एरर हैंडलिंग के बिना Async/प्रतीक्षा करें
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

## 3.`const`कंस्ट्रक्टर का उपयोग नहीं करना
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

## 4.`==`बिना`hashCode`के
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

## 5. स्प्रेड और कलेक्शन का उपयोग न करना-यदि
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

## 6. एंटी-पैटर्न: विशाल स्टेटफुलविजेट
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

## सारांश
डार्ट की शून्य सुरक्षा शक्तिशाली है - इसे`!`से पराजित न करें। विहित उदाहरणों के लिए`const`कंस्ट्रक्टर का उपयोग करें, हमेशा`==`के साथ`hashCode`को ओवरराइड करें, संक्षिप्त सूची निर्माण के लिए संग्रह-यदि और स्प्रेड ऑपरेटरों का उपयोग करें, और विजेट्स से व्यावसायिक तर्क निकालें। डार्ट स्वच्छ, अशक्त-सुरक्षित, कॉन्स्ट-सही कोड को पुरस्कृत करता है।