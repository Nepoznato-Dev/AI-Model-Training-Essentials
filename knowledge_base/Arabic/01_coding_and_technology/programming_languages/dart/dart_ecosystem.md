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
# دارت - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية التحتية الأساسية في نظام Dart البيئي.
---

## سلسلة الأدوات
| أداة | الغرض |
|------|---------|
| **السهام** | Dart SDK (مترجم، منسق، محلل) |
| **رفرفة** | Flutter SDK (يتضمن Dart) |
| **حانة** | مدير الحزم (مدمج في دارت) |
| **تحليل السهام** | التحليل الساكن |
| **تنسيق دارت** | تنسيق الكود |
| ** تجميع السهام ** | ترجمة إلى الأصلي/JS/WASM |
| ** تشغيل السهام ** | تشغيل البرامج النصية دارت |
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

## إدارة الحزم
| أداة | الغرض |
|------|---------|
| **pub.dev** | مستودع الحزم الرسمي |
| **حانة السهام** | مدير الحزم CLI |
| **pubspec.yaml** | بيان الحزمة |
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

## الرفرفة (إطار عمل Dart UI)
| تكنولوجيا | الغرض |
|------------|---------|
| **رفرفة** | إطار عمل واجهة المستخدم عبر الأنظمة الأساسية |
| **رفرفة الويب** | تطبيقات الويب مع Flutter |
| **رفرفة سطح المكتب** | ويندوز، ماك، لينكس |
| **رفرفة موبايل** | iOS وأندرويد |
| **رفرفة مضمنة** | الأجهزة المدمجة |
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

## أطر عمل الويب (Dart من جانب الخادم)
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| **الجرف** | القائم على الوسيطة | خادم HTTP (الأكثر شهرة) |
| ** دارت الضفدع ** | مكدس كامل | إطار عمل الواجهة الخلفية (مثل Laravel) |
| **ملاك** | ريست API | واجهات برمجة التطبيقات البسيطة |
| **الفريد** | أعرب مثل | خادم بنمط Node.js |
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

##قاعدة البيانات
| تكنولوجيا | اكتب |
|------------|------|
| **الانجراف** | SQL من النوع الآمن (يحل محل Moor) |
| **ObjectBox** | قاعدة بيانات NoSQL المتنقلة |
| **إيزار** | قاعدة بيانات متنقلة سريعة |
| **خلية** | قيمة مفتاح خفيفة الوزن |
| **بوستجرس** | عميل PostgreSQL |
| **mysql1** | عميل MySQL |
| **قاعدة الأريكة** | عميل Couchbase |
| **سوبابيس** | الواجهة الخلفية كخدمة |
| **فايرباسي** | جوجل كخدمة |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **اختبار** | إطار اختبار مدمج |
| ** موكيتو ** | استهزاء |
| ** موكتيل ** | السخرية الآمنة الخالية |
| **flutter_test** | اختبار القطعة رفرفة |
| **اختبار_التكامل** | اختبار شامل |
| **golden_toolkit** | اختبار الذهبي/اللقطة |
| ** دورية ** | اختبار تكامل الرفرفة |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **تحليل السهام** | تحليل ثابت مدمج |
| **تنسيق دارت** | المنسق المدمج |
| **الوبر** | قواعد الوبر الرسمية |
| **flutter_lints** | الوبر الخاص بالرفرفة |
| **تحليل_جيد جدًا** | قواعد الوبر الصارمة |
| **التغطية** | تغطية الكود |
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

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **السهام:الأساسية** | المكتبة القياسية |
| ** دارت: غير متزامن ** | العقود الآجلة، تيارات، غير متزامن |
| **دارت:io** | ملف، HTTP، TCP |
| ** دارت: تحويل ** | JSON، UTF-8 |
| **تتب** | عميل HTTP |
| **ديو** | عميل HTTP (رفرفة) |
| **json_serializable** | توليد كود JSON |
| **متجمد** | فئات البيانات غير القابلة للتغيير |
| ** Riverpod ** | إدارة الدولة |
| ** الكتلة / الذراع ** | إدارة الدولة |
| **get_it** | حقن التبعية |
| **go_router** | التوجيه التعريفي |
| **متساوي** | المساواة في القيمة |
| **uid** | جيل UUID |
| **التشفير** | التشفير |
| **المسار** | معالجة مسار الملف |
| **مجموعة** | أنواع التجميع الإضافية |
| **دولي** | التدويل |
---

## إدارة الحالة (الرفرفة)
| الحل | اكتب |
|----------|------|
| **ريفيربود** | ترجمة آمنة وقابلة للاختبار |
| ** الكتلة / الذراع ** | مدفوعة بالأحداث، ويمكن التنبؤ بها |
| **المزود** | مدمج وبسيط |
| **جيتكس** | الكل في واحد (مثير للجدل) |
| **الإشارات** | البدائيات التفاعلية |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **رمز VS + دارت** | أفضل دعم للسهم/الرفرفة |
| **أندرويد ستوديو + رفرفة** | رفرفة كاملة IDE |
| **IntelliJ + دارت** | دعم JetBrains |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| ** تجميع دارت ** | الملفات التنفيذية الأصلية |
| ** ترجمة دارت JS ** | ترجمة إلى جافا سكريبت |
| **دارت تجميع وسم** | ترجمة إلى WebAssembly |
| ** بناء الرفرفة ** | تطبيقات الجوال/سطح المكتب |
| ** عامل الميناء ** | تطبيقات الخادم المعبأة في حاويات |
| **جوجل كلاود رن** | حاويات بدون خادم |
| **استضافة Firebase** | استضافة تطبيقات الويب |
---

## ملخص
يهيمن **Flutter** على نظام Dart البيئي لتطوير واجهة المستخدم عبر الأنظمة الأساسية. بالنسبة إلى Dart من جانب الخادم، **Shelf** هو إطار عمل HTTP القياسي، مع **Dart Frog** كخيار متكامل. المكدس القياسي هو: **Dart 3.4+** كوقت تشغيل، **pub.dev** للحزم، **Flutter** لواجهة المستخدم للجوال/الويب/سطح المكتب، **Riverpod** أو **Bloc** لإدارة الحالة، **Drift** لقواعد البيانات، **test** للاختبار، و **dart Analysis** للفحص. تتمثل نقاط قوة Dart في الأمان التام، والتجميع السريع، والتحديث السريع (Flutter)، والقدرة على التحويل البرمجي إلى JavaScript أو WebAssembly الأصلي. يعد النظام البيئي مثاليًا لتطبيقات الهاتف المحمول والويب وسطح المكتب عبر الأنظمة الأساسية.