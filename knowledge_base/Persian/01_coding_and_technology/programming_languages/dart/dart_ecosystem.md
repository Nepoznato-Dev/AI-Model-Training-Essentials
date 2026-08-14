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
# دارت - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم دارت را پوشش می‌دهد.
---

## زنجیره ابزار
| ابزار | هدف |
|------|---------|
| **دارت** | Dart SDK (کامپایلر، فرمت کننده، تحلیلگر) |
| **بال زدن** | فلوتر SDK (شامل دارت) |
| ** میخانه** | مدیر بسته (ساخته شده در دارت) |
| **تحلیل دارت** | تجزیه و تحلیل استاتیک |
| **فرمت دارت** | قالب بندی کد |
| **کامپایل دارت** | کامپایل به native/JS/WASM |
| **دوی دارت** | اجرای اسکریپت های دارت |
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

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **pub.dev** | مخزن رسمی بسته |
| **میخانه دارت** | مدیر بسته CLI |
| **pubspec.yaml** | مانیفست بسته |
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

## فلاتر (چارچوب رابط کاربری دارت)
| فناوری | هدف |
|------------|---------|
| **فلاتر** | چارچوب UI کراس پلتفرم |
| **فلاتر وب** | برنامه های وب با Flutter |
| **دسکتاپ فلاتر** | ویندوز، macOS، لینوکس |
| **فلاتر موبایل** | iOS و اندروید |
| **Flutter Embedded** | دستگاه های تعبیه شده |
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

## چارچوب های وب (دارت سمت سرور)
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **قفسه** | مبتنی بر میان افزار | سرور HTTP (محبوب ترین) |
| **قورباغه دارت** | تمام پشته | فریم ورک Backend (مانند لاراول) |
| **فرشته** | REST API | API های ساده |
| **آلفرد** | اکسپرس مانند | سرور به سبک Node.js |
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

## پایگاه داده
| فناوری | نوع |
|------------|------|
| **دریفت** | نوع ایمن SQL (جایگزین Moor) |
| **ObjectBox** | پایگاه داده موبایل NoSQL |
| **ایثار** | پایگاه داده سریع موبایل |
| **کندو** | کلید-مقدار سبک |
| **postgres** | مشتری PostgreSQL |
| **mysql1** | مشتری MySQL |
| **پایه کاناپه** | مشتری Couchbase |
| **Supbase** | Backend-as-a-service |
| **Firebase** | Google BaaS |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **تست** | چارچوب تست داخلی |
| **موکیتو** | تمسخر |
| **مکتل** | تمسخر بی خطر |
| **تست_فلاتر** | تست ویجت فلاتر |
| **تست_ادغام** | تست انتها به انتها |
| **ابزار_طلایی** | تست طلایی/عکس فوری |
| **گشت** | تست ادغام فلاتر |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **تحلیل دارت** | آنالیز استاتیک داخلی |
| **فرمت دارت** | فرمت داخلی |
| **پرز** | قوانین رسمی لینت |
| **فلتر_لینتس** | پرزهای مخصوص فلاتر |
| **تحلیل_خیلی_خوب** | قوانین سختگیرانه پرز |
| **پوشش** | پوشش کد |
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

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **دارت:هسته** | کتابخانه استاندارد |
| **dart:async** | آتی، جریان، همگام |
| **dart:io** | فایل، HTTP، TCP |
| **دارت:تبدیل** | JSON، UTF-8 |
| **http** | سرویس گیرنده HTTP |
| **دیو** | کلاینت HTTP (Flutter) |
| **json_serializable** | تولید کد JSON |
| **یخ زده** | کلاس های داده غیرقابل تغییر |
| **رودخانه** | مدیریت دولتی |
| **بلوک / کوبیت** | مدیریت دولتی |
| **دریافت_آن** | تزریق وابستگی |
| **go_router** | مسیریابی اعلامی |
| **مساوی** | برابری ارزش |
| **uuid** | نسل UUID |
| **کریپتو** | رمزنگاری |
| **مسیر** | دستکاری مسیر فایل |
| **مجموعه** | انواع مجموعه اضافی |
| **بین المللی** | بین المللی شدن |
---

## مدیریت دولتی (فلاتر)
| راه حل | نوع |
|----------|------|
| **Riverpod** | کامپایل-ایمن، قابل آزمایش |
| **بلوک / کوبیت** | رویداد محور، قابل پیش بینی |
| **ارائه دهنده** | توکار ساده |
| **GetX** | همه کاره (جنجالی) |
| **سیگنال** | اولیه های واکنشی |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + Dart** | بهترین پشتیبانی دارت/فلاتر |
| **اندروید استودیو + فلاتر** | Flutter IDE کامل |
| **IntelliJ + Dart** | پشتیبانی JetBrains |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **کامپایل دارت** | فایل های اجرایی بومی |
| **دارت کامپایل js** | کامپایل به جاوا اسکریپت |
| **دارت کامپایل wasm** | کامپایل به WebAssembly |
| **ساخت فلاتر** | برنامه های موبایل/رومیزی |
| **داکر** | برنامه های سرور کانتینری |
| **Google Cloud Run** | ظروف بدون سرور |
| **هاست فایربیس** | میزبانی وب اپلیکیشن |
---

## خلاصه
اکوسیستم Dart تحت سلطه **Flutter** برای توسعه رابط کاربری متقابل پلتفرم است. برای Dart سمت سرور، **Shelf** چارچوب استاندارد HTTP است، با **Dart Frog** به عنوان یک گزینه تمام پشته. پشته استاندارد عبارتند از: **Dart 3.4+** به عنوان زمان اجرا، **pub.dev** برای بسته ها، **Flutter** برای موبایل/وب/دسکتاپ UI، **Riverpod** یا **Block** برای مدیریت حالت، **Drift** برای پایگاه های داده، **تست** برای آزمایش، و **تحلیل دارت** برای پرز. نقاط قوت دارت ایمنی تهی صدا، کامپایل سریع، بارگذاری مجدد داغ (Flutter) و توانایی کامپایل به بومی، جاوا اسکریپت یا WebAssembly است. این اکوسیستم برای برنامه های کاربردی موبایل، وب و دسکتاپ بین پلتفرمی ایده آل است.