<!--
---
# Metadata
title: "Dart — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Dart ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [dart, ecosystem, tooling, flutter, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# ডার্ট — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি ডার্ট ইকোসিস্টেমের প্রয়োজনীয় টুল, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## টুলচেইন
| টুল | উদ্দেশ্য |
|------|---------|
| **ডার্ট** | ডার্ট SDK (কম্পাইলার, ফরম্যাটার, বিশ্লেষক) |
| **ফ্লাটার** | ফ্লটার SDK (ডার্ট সহ) |
| **পাব** | প্যাকেজ ম্যানেজার (বিল্ট ইন ডার্ট) |
| **ডার্ট বিশ্লেষণ** | স্ট্যাটিক বিশ্লেষণ |
| **ডার্ট ফরম্যাট** | কোড ফরম্যাটিং |
| **ডার্ট কম্পাইল** | নেটিভ/জেএস/WASM এ কম্পাইল |
| **ডার্ট রান** | ডার্ট স্ক্রিপ্ট চালান |
```bash
dart --version              # check version
dart create myapp           # create project
dart run                    # run project
dart pub get                # install dependencies
dart analyze                # static analysis
dart format .               # format code
dart compile exe bin/app.dart -o app  # compile to native
```

---

## প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য |
|------|---------|
| **pub.dev** | অফিসিয়াল প্যাকেজ ভান্ডার |
| **ডার্ট পাব** | প্যাকেজ ম্যানেজার CLI |
| **pubspec.yaml** | প্যাকেজ ম্যানিফেস্ট |
```yaml
# pubspec.yaml
name: myapp
description: A sample Dart application
version: 0.1.0
environment:
  sdk: ^3.4.0

dependencies:
  http: ^1.2.0
  json_annotation: ^4.9.0
  riverpod: ^2.5.0

dev_dependencies:
  test: ^1.25.0
  build_runner: ^2.4.0
  json_serializable: ^6.7.0
  lints: ^4.0.0
```

```bash
dart pub get                # install dependencies
dart pub upgrade            # upgrade packages
dart pub add http           # add dependency
dart pub outdated           # check outdated packages
```

---

## ফ্লটার (ডার্ট ইউআই ফ্রেমওয়ার্ক)
| প্রযুক্তি | উদ্দেশ্য |
|------------|---------|
| **ফ্লটার** | ক্রস-প্ল্যাটফর্ম UI ফ্রেমওয়ার্ক |
| **ফ্লটার ওয়েব** | ফ্লটার সহ ওয়েব অ্যাপস |
| **ফ্লটার ডেস্কটপ** | Windows, macOS, Linux |
| **ফ্লটার মোবাইল** | iOS এবং Android |
| **ফ্লটার এমবেডেড** | এমবেডেড ডিভাইস |
```dart
// Flutter widget example
class UserCard extends StatelessWidget {
  final User user;
  const UserCard({super.key, required this.user});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        title: Text(user.name),
        subtitle: Text(user.email),
        trailing: Icon(Icons.arrow_forward),
        onTap: () => Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => UserDetail(user: user)),
        ),
      ),
    );
  }
}
```

---

## ওয়েব ফ্রেমওয়ার্ক (সার্ভার-সাইড ডার্ট)
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **শেল্ফ** | মিডলওয়্যার ভিত্তিক | HTTP সার্ভার (সবচেয়ে জনপ্রিয়) |
| **ডার্ট ফ্রগ** | ফুল-স্ট্যাক | ব্যাকএন্ড ফ্রেমওয়ার্ক (লারাভেলের মতো) |
| **এঞ্জেল** | REST API | সরল APIs |
| **আলফ্রেড** | এক্সপ্রেস মত | Node.js-স্টাইল সার্ভার |
```dart
// Shelf example
import 'package:shelf/shelf.dart';
import 'package:shelf_router/shelf_router.dart';
import 'package:shelf/shelf_io.dart' as io;

void main() async {
  final router = Router();
  
  router.get('/hello', (Request req) => Response.ok('Hello, World!'));
  
  router.get('/users/<id>', (Request req) async {
    final id = req.params['id']!;
    final user = await UserService.findById(int.parse(id));
    return Response.ok(jsonEncode(user));
  });

  var server = await io.serve(router, 'localhost', 8080);
  print('Serving at http://${server.address.host}:${server.port}');
}
```

---

## ডাটাবেস
| প্রযুক্তি | প্রকার |
|------------|------|
| **প্রবাহ** | টাইপ-সেফ SQL (মুর প্রতিস্থাপন করে) |
| **অবজেক্ট বক্স** | NoSQL মোবাইল ডাটাবেস |
| **ইসার** | দ্রুত মোবাইল ডাটাবেস |
| **মৌচা** | লাইটওয়েট কী-মান |
| **পোস্টগ্রেস** | PostgreSQL ক্লায়েন্ট |
| **mysql1** | MySQL ক্লায়েন্ট |
| **কাউচবেস** | কাউচবেস ক্লায়েন্ট |
| **সুপাবেস** | ব্যাকএন্ড-এ-একটি-পরিষেবা |
| **ফায়ারবেস** | Google BaaS |
```dart
// Drift (type-safe SQL)
class UsersDao extends DatabaseAccessor<AppDatabase> with _$UsersDaoMixin {
  UsersDao(AppDatabase db) : super(db);

  Future<List<User>> findAll() => select(users).get();
  
  Future<User> findById(int id) =>
    (select(users)..where((t) => t.id.equals(id)))
      .getSingle();
  
  Stream<List<User>> watchAll() => select(users).watch();
}
```

---

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **পরীক্ষা** | বিল্ট-ইন টেস্ট ফ্রেমওয়ার্ক |
| **মকিটো** | উপহাস |
| **মকটেল** | নাল-নিরাপদ উপহাস |
| **ফ্লটার_টেস্ট** | ফ্লটার উইজেট টেস্টিং |
| **একীকরণ_পরীক্ষা** | এন্ড-টু-এন্ড টেস্টিং |
| **গোল্ডেন_টুলকিট** | গোল্ডেন/স্ন্যাপশট টেস্টিং |
| **টহল** | ফ্লটার ইন্টিগ্রেশন টেস্টিং |
```dart
import 'package:test/test.dart';

void main() {
  group('UserService', () {
    late UserService service;
    late MockUserRepository mockRepo;

    setUp(() {
      mockRepo = MockUserRepository();
      service = UserService(mockRepo);
    });

    test('finds user by id', () async {
      when(mockRepo.findById(1)).thenAnswer((_) async => User(1, 'Alice'));

      final user = await service.findById(1);

      expect(user.name, equals('Alice'));
      verify(mockRepo.findById(1)).called(1);
    });

    test('throws when user not found', () async {
      when(mockRepo.findById(any)).thenThrow(NotFoundException());

      expect(() => service.findById(999), throwsA(isA<NotFoundException>()));
    });
  });
}
```

---

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **ডার্ট বিশ্লেষণ** | অন্তর্নির্মিত স্ট্যাটিক বিশ্লেষণ |
| **ডার্ট ফরম্যাট** | অন্তর্নির্মিত বিন্যাস |
| **লিন্ট** | অফিসিয়াল লিন্ট নিয়ম |
| **ফ্লটার_লিন্ট** | ফ্লটার-নির্দিষ্ট লিন্ট |
| **খুব_ভালো_বিশ্লেষণ** | কড়া লিন্ট নিয়ম |
| **কভারেজ** | কোড কভারেজ |
```yaml
# analysis_options.yaml
include: package:lints/recommended.yaml

linter:
  rules:
    - prefer_final_locals
    - prefer_const_constructors
    - avoid_dynamic_calls
    - always_declare_return_types

analyzer:
  errors:
    missing_return: error
    dead_code: warning
```

---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **ডার্ট:কোর** | স্ট্যান্ডার্ড লাইব্রেরি |
| **dart:async** | ফিউচার, স্ট্রীম, অ্যাসিঙ্ক |
| **dart:io** | ফাইল, HTTP, TCP |
| **ডার্ট:রূপান্তর** | JSON, UTF-8 |
| **http** | HTTP ক্লায়েন্ট |
| **ডিও** | HTTP ক্লায়েন্ট (ফ্লটার) |
| **json_serializable** | JSON কোড প্রজন্ম |
| **হিমায়িত** | অপরিবর্তনীয় ডেটা ক্লাস |
| **রিভারপড** | রাষ্ট্র পরিচালনা |
| **ব্লক / হাত** | রাষ্ট্র পরিচালনা |
| **গেট_এটি** | নির্ভরতা ইনজেকশন |
| **গো_রাউটার** | ঘোষণামূলক রাউটিং |
| **সমান্য** | মূল্য সমতা |
| **uuid** | UUID প্রজন্ম |
| **ক্রিপ্টো** | ক্রিপ্টোগ্রাফি |
| **পথ** | ফাইল পাথ ম্যানিপুলেশন |
| **সংগ্রহ** | অতিরিক্ত সংগ্রহের ধরন |
| **intl** | আন্তর্জাতিকীকরণ |
---

## রাজ্য ব্যবস্থাপনা (ফ্লটার)
| সমাধান | প্রকার |
|----------|------|
| **রিভারপড** | কম্পাইল-নিরাপদ, পরীক্ষাযোগ্য |
| **ব্লক / কিউবিট** | ঘটনা-চালিত, অনুমানযোগ্য |
| **প্রদানকারী** | অন্তর্নির্মিত, সহজ |
| **GetX** | অল-ইন-ওয়ান (বিতর্কিত) |
| **সংকেত** | প্রতিক্রিয়াশীল আদিম |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **ভিএস কোড + ডার্ট** | সেরা ডার্ট/ফ্লটার সমর্থন |
| **অ্যান্ড্রয়েড স্টুডিও + ফ্লটার** | সম্পূর্ণ ফ্লটার IDE |
| **IntelliJ + Dart** | JetBrains সমর্থন |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **ডার্ট কম্পাইল** | নেটিভ এক্সিকিউটেবল |
| **ডার্ট কম্পাইল js** | জাভাস্ক্রিপ্টে কম্পাইল |
| **ডার্ট কম্পাইল wasm** | WebAssembly এ কম্পাইল |
| **ফ্লটার বিল্ড** | মোবাইল/ডেস্কটপ অ্যাপস |
| **ডকার** | কনটেইনারাইজড সার্ভার অ্যাপস |
| **গুগল ক্লাউড রান** | সার্ভারহীন পাত্রে |
| **ফায়ারবেস হোস্টিং** | ওয়েব অ্যাপ হোস্টিং |
---

## সারাংশ
ক্রস-প্ল্যাটফর্ম UI ডেভেলপমেন্টের জন্য ডার্টের ইকোসিস্টেমে **ফ্লটার** দ্বারা প্রাধান্য রয়েছে। সার্ভার-সাইড ডার্টের জন্য, **শেল্ফ** হল স্ট্যান্ডার্ড HTTP ফ্রেমওয়ার্ক, **ডার্ট ফ্রগ** একটি ফুল-স্ট্যাক বিকল্প হিসেবে। স্ট্যান্ডার্ড স্ট্যাক হল: রানটাইম হিসাবে **Dart 3.4+**, প্যাকেজের জন্য **pub.dev**, মোবাইল/ওয়েব/ডেস্কটপ UI এর জন্য **ফ্লটার**, স্টেট ম্যানেজমেন্টের জন্য **রিভারপড** বা **ব্লক**, ডাটাবেসের জন্য **ড্রিফট**, পরীক্ষার জন্য **পরীক্ষা** এবং **ডার্ট লিনটিং ** বিশ্লেষণের জন্য। ডার্টের শক্তি হল সাউন্ড নাল নিরাপত্তা, দ্রুত সংকলন, হট রিলোড (ফ্লাটার), এবং নেটিভ, জাভাস্ক্রিপ্ট বা ওয়েব অ্যাসেম্বলিতে কম্পাইল করার ক্ষমতা। ইকোসিস্টেমটি ক্রস-প্ল্যাটফর্ম মোবাইল, ওয়েব এবং ডেস্কটপ অ্যাপ্লিকেশনের জন্য আদর্শ।