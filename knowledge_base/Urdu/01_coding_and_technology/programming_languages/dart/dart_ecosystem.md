---
# Metadata
title: "Dart — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Dart ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# ڈارٹ - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ ڈارٹ ایکو سسٹم میں ضروری ٹولز، فریم ورک اور انفراسٹرکچر کا احاطہ کرتی ہے۔
---

## ٹول چین
| ٹول | مقصد |
|------|---------|
| **ڈارٹ** | ڈارٹ SDK (مرتب، فارمیٹر، تجزیہ کار) |
| ** پھڑپھڑاہٹ** | فلٹر SDK (بشمول ڈارٹ) |
| **پب** | پیکیج مینیجر (ڈارٹ میں بنایا گیا) |
| **ڈارٹ تجزیہ** | جامد تجزیہ |
| **ڈارٹ فارمیٹ** | کوڈ فارمیٹنگ |
| **ڈارٹ کمپائل** | مقامی/JS/WASM میں مرتب کریں |
| **ڈارٹ رن** | ڈارٹ اسکرپٹ چلائیں |
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

## پیکیج مینجمنٹ
| ٹول | مقصد |
|------|---------|
| **pub.dev** | سرکاری پیکج ذخیرہ |
| **ڈارٹ پب** | پیکیج مینیجر CLI |
| **pubspec.yaml** | پیکیج مینی فیسٹ |
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

## پھڑپھڑانا (ڈارٹ UI فریم ورک)
| ٹیکنالوجی | مقصد |
|------------|---------|
| ** پھڑپھڑاہٹ** | کراس پلیٹ فارم UI فریم ورک |
| **فلٹر ویب** | فلٹر کے ساتھ ویب ایپس |
| **فلٹر ڈیسک ٹاپ** | ونڈوز، میک او ایس، لینکس |
| **فلٹر موبائل** | iOS اور Android |
| **فلٹر ایمبیڈڈ** | ایمبیڈڈ ڈیوائسز |
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

## ویب فریم ورکس (سرور سائیڈ ڈارٹ)
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **شیلف** | مڈل ویئر پر مبنی | HTTP سرور (سب سے زیادہ مقبول) |
| **ڈارٹ فراگ** | مکمل اسٹیک | بیک اینڈ فریم ورک (جیسے Laravel) |
| **فرشتہ** | REST API | سادہ APIs |
| **الفریڈ** | ایکسپریس کی طرح | Node.js طرز سرور |
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

## ڈیٹا بیس
| ٹیکنالوجی | قسم |
|------------|------|
| **آگہ** | ٹائپ سیف ایس کیو ایل (مور کی جگہ لے لیتا ہے) |
| **آبجیکٹ باکس** | NoSQL موبائل ڈیٹا بیس |
| **اسر** | تیز رفتار موبائل ڈیٹا بیس |
| **چھتہ** | ہلکا پھلکا کلیدی قدر |
| **پوسٹگریس** | PostgreSQL کلائنٹ |
| **mysql1** | MySQL کلائنٹ |
| **کاؤچ بیس** | Couchbase کلائنٹ |
| **Supabase** | بیک اینڈ بطور سروس |
| **فائر بیس** | Google BaaS |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **ٹیسٹ** | بلٹ ان ٹیسٹ فریم ورک |
| **مکیٹو** | طنز |
| **ماکٹیل** | null-safe مذاق |
| **فلٹر_ٹیسٹ** | لہرانا ویجیٹ ٹیسٹنگ |
| **انضمام_ٹیسٹ** | اینڈ ٹو اینڈ ٹیسٹنگ |
| **سنہری_ٹول کٹ** | گولڈن/اسنیپ شاٹ ٹیسٹنگ |
| **گشت** | فلٹر انٹیگریشن ٹیسٹنگ |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **ڈارٹ تجزیہ** | بلٹ ان جامد تجزیہ |
| **ڈارٹ فارمیٹ** | بلٹ ان فارمیٹر |
| **لنٹس** | سرکاری لنٹ قواعد |
| **فلٹر_لنٹ** ​​| پھڑپھڑانے کے لئے مخصوص لنٹ |
| **بہت_اچھا_تجزیہ** | سخت لنٹ قوانین |
| **کوریج** | کوڈ کوریج |
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

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **ڈارٹ: کور** | معیاری لائبریری |
| **dart:async** | فیوچرز، اسٹریمز، async |
| **dart:io** | فائل، HTTP، TCP |
| **ڈارٹ: کنورٹ** | JSON, UTF-8 |
| **http** | HTTP کلائنٹ |
| **dio** | HTTP کلائنٹ (فلٹر) |
| **json_serializable** | JSON کوڈ جنریشن |
| **منجمد** | ناقابل تغیر ڈیٹا کلاسز |
| **ریور پوڈ** | ریاستی انتظام |
| **بلاک / کیوبٹ** | ریاستی انتظام |
| **یہ حاصل کریں** | انحصار انجکشن |
| **go_router** | اعلانیہ روٹنگ |
| **مساوات** | قدر کی مساوات |
| **uuid** | UUID نسل |
| **کرپٹو** | خفیہ نگاری |
| **راستہ** | فائل پاتھ ہیرا پھیری |
| **مجموعہ** | جمع کرنے کی اضافی اقسام |
| **intl** | بین الاقوامی کاری |
---

## ریاستی انتظام (پھڑپھڑانا)
| حل | قسم |
|------------|------|
| **ریور پوڈ** | مرتب کرنے کے لیے محفوظ، قابل جانچ |
| **بلاک / کیوبٹ** | واقعہ پر مبنی، پیشین گوئی |
| **فراہم کنندہ** | بلٹ میں، سادہ |
| **GetX** | سب میں ایک (متنازعہ) |
| **سگنلز** | رد عمل سے متعلق قدیم |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **VS کوڈ + ڈارٹ** | بہترین ڈارٹ / فلٹر سپورٹ |
| **Android اسٹوڈیو + فلٹر** | فل فلٹر IDE |
| **انٹیلی جے + ڈارٹ** | JetBrains کی حمایت |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **ڈارٹ کمپائل** | مقامی ایگزیکیوٹیبلز |
| **ڈارٹ کمپائل جے ایس** | جاوا اسکرپٹ پر مرتب کریں |
| **ڈارٹ کمپائل wasm** | WebAssembly میں مرتب کریں |
| ** پھڑپھڑانا ** | موبائل/ڈیسک ٹاپ ایپس |
| **ڈوکر** | کنٹینرائزڈ سرور ایپس |
| **گوگل کلاؤڈ رن** | سرور کے بغیر کنٹینرز |
| **فائر بیس ہوسٹنگ** | ویب ایپ ہوسٹنگ |
---

## خلاصہ
کراس پلیٹ فارم UI ڈیولپمنٹ کے لیے Dart کے ماحولیاتی نظام پر **Flutter** کا غلبہ ہے۔ سرور سائیڈ ڈارٹ کے لیے، **Shelf** معیاری HTTP فریم ورک ہے، جس میں **Dart Frog** بطور فل اسٹیک آپشن ہے۔ معیاری اسٹیک یہ ہے: **Dart 3.4+** بطور رن ٹائم، **pub.dev** پیکجز کے لیے، **فلٹر** موبائل/ویب/ڈیسک ٹاپ UI کے لیے، **ریور پوڈ** یا **بلاک** اسٹیٹ مینجمنٹ کے لیے، **ڈرفٹ** ڈیٹا بیسز کے لیے، **ٹیسٹ** ٹیسٹنگ کے لیے، اور **ڈارٹ لینٹنگ کے لیے**۔ ڈارٹ کی طاقتیں آواز کی حفاظت، تیز تالیف، ہاٹ ری لوڈ (فلاٹر)، اور مقامی، جاوا اسکرپٹ، یا ویب اسمبلی میں مرتب کرنے کی صلاحیت ہیں۔ ماحولیاتی نظام کراس پلیٹ فارم موبائل، ویب اور ڈیسک ٹاپ ایپلی کیشنز کے لیے مثالی ہے۔