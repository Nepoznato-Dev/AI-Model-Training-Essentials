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

# Dart — よくある間違いとアンチパターン
このドキュメントでは、Dart で最も一般的な間違い、罠、アンチパターンを修正とともにカタログ化します。
---

## 1. ヌルセーフティの誤用
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

## 2. エラー処理を行わない非同期/待機
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

## 3.`const`コンストラクターを使用しない
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

## 4.`==``hashCode` なし
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

## 5. Spread と Collection-if を使用しない
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

## 6. アンチパターン: 大規模な StatefulWidget
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

＃＃ まとめ
Dart のヌル セーフティは強力です。`!`で無効にしないでください。正規インスタンスには`const`コンストラクターを使用し、常に`hashCode`を`==`でオーバーライドし、コレクション if 演算子とスプレッド演算子を使用して簡潔なリストを構築し、ウィジェットからビジネス ロジックを抽出します。 Dart は、クリーンで null セーフで const が正しいコードを評価します。