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

# Dart - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่สำคัญในระบบนิเวศของ Dart
---

## ห่วงโซ่เครื่องมือ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **โผ** | Dart SDK (คอมไพเลอร์, ฟอร์แมตเตอร์, ตัววิเคราะห์) |
| **กระพือ** | Flutter SDK (รวม Dart) |
| **ผับ** | ตัวจัดการแพ็คเกจ (มีอยู่ในโผ) |
| **วิเคราะห์โผ** | การวิเคราะห์แบบคงที่ |
| **รูปแบบโผ** | การจัดรูปแบบโค้ด |
| **รวบรวมโผ** | คอมไพล์เป็น Native/JS/WASM |
| **โผวิ่ง** | เรียกใช้สคริปต์ Dart |
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

## การจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **pub.dev** | ที่เก็บแพ็คเกจอย่างเป็นทางการ |
| **ดาร์ทผับ** | ตัวจัดการแพ็คเกจ CLI |
| **pubspec.yaml** | รายการแพ็คเกจ |
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

## กระพือ (กรอบงาน Dart UI)
| เทคโนโลยี | วัตถุประสงค์ |
|------------|---------|
| **กระพือ** | กรอบงาน UI ข้ามแพลตฟอร์ม |
| **เว็บกระพือ** | เว็บแอปพร้อม Flutter |
| **Flutter Desktop** | วินโดวส์, macOS, ลินุกซ์ |
| **กระพือมือถือ** | iOS และ Android |
| **กระพือฝังตัว** | อุปกรณ์ฝังตัว |
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

## กรอบงานเว็บ (โผฝั่งเซิร์ฟเวอร์)
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **ชั้นวางของ** | ที่ใช้มิดเดิลแวร์ | เซิร์ฟเวอร์ HTTP (ยอดนิยมที่สุด) |
| **กบโผ** | เต็มกอง | กรอบงานแบ็กเอนด์ (เช่น Laravel) |
| **นางฟ้า** | ส่วนที่เหลือ API | API แบบง่าย |
| **อัลเฟรด** | ด่วนเหมือน | เซิร์ฟเวอร์สไตล์ Node.js |
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

## ฐานข้อมูล
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **ดริฟท์** | พิมพ์ SQL ที่ปลอดภัย (แทนที่ Moor) |
| **ObjectBox** | ฐานข้อมูลมือถือ NoSQL |
| **อิศรา** | ฐานข้อมูลมือถือที่รวดเร็ว |
| **ไฮฟ์** | คีย์-ค่าแบบน้ำหนักเบา |
| **โพสต์เกรส** | ไคลเอนต์ PostgreSQL |
| **mysql1** | ไคลเอนต์ MySQL |
| **ฐานโซฟา** | ลูกค้า Couchbase |
| **ซูปาเบส** | แบ็กเอนด์ตามบริการ |
| **ไฟร์เบส** | Google BaaS |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **ทดสอบ** | กรอบการทดสอบในตัว |
| **ม็อคโตโต** | ล้อเลียน |
| **ม็อกเทล** | การเยาะเย้ยที่ไม่ปลอดภัย |
| **flutter_test** | การทดสอบวิดเจ็ต Flutter |
| **integration_test** | การทดสอบแบบครบวงจร |
| **golden_toolkit** | การทดสอบสีทอง/สแนปชอต |
| **ตระเวน** | การทดสอบการรวม Flutter |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **วิเคราะห์โผ** | การวิเคราะห์แบบคงที่ในตัว |
| **รูปแบบโผ** | ฟอร์แมตเตอร์ในตัว |
| **ผ้าสำลี** | กฎผ้าสำลีอย่างเป็นทางการ |
| **กระพือ_lints** | ผ้าสำลีเฉพาะกระพือ |
| **วิเคราะห์ดีมาก** | กฎผ้าสำลีที่เข้มงวด |
| **ความคุ้มครอง** | ความครอบคลุมของโค้ด |
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

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **โผ:แกน** | ไลบรารีมาตรฐาน |
| **โผ:async** | ฟิวเจอร์ส, สตรีม, อะซิงก์ |
| **โผ:io** | ไฟล์, HTTP, TCP |
| **โผ: แปลง** | JSON, UTF-8 |
| **http** | ไคลเอ็นต์ HTTP |
| **ดิโอ** | ไคลเอนต์ HTTP (กระพือ) |
| **json_serializable** | การสร้างโค้ด JSON |
| **แช่แข็ง** | คลาสข้อมูลที่ไม่เปลี่ยนรูป |
| **สายน้ำ** | การจัดการของรัฐ |
| **บล็อก / ศอก** | การจัดการของรัฐ |
| **get_it** | การฉีดพึ่งพา |
| **go_router** | การกำหนดเส้นทางที่ประกาศ |
| **เท่าเทียมกัน** | ความเท่าเทียมกันของมูลค่า |
| **อุ๊ย** | การสร้าง UUID |
| **คริปโต** | การเข้ารหัส |
| **เส้นทาง** | การจัดการเส้นทางไฟล์ |
| **คอลเลกชัน** | ประเภทคอลเลกชันพิเศษ |
| **นานาชาติ** | ความเป็นสากล |
---

## การจัดการของรัฐ (กระพือ)
| โซลูชั่น | พิมพ์ |
|----------|-|
| **แม่น้ำพ็อด** | คอมไพล์ปลอดภัย ทดสอบได้ |
| **บล็อก / คิวบิต** | ขับเคลื่อนด้วยเหตุการณ์ คาดเดาได้ |
| **ผู้ให้บริการ** | ในตัว | เรียบง่าย
| **GetX** | All-in-one (แย้ง) |
| **สัญญาณ** | ปฏิกิริยาดั้งเดิม |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **VS Code + Dart** | สุดยอดการสนับสนุน Dart/Flutter
| **Android Studio + Flutter** | IDE กระพือเต็ม |
| **IntelliJ + โผ** | การสนับสนุน JetBrains |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **รวบรวมโผ** | ไฟล์ปฏิบัติการเนทิฟ |
| **Dart คอมไพล์ js** | คอมไพล์เป็น JavaScript |
| **คอมไพล์ Dart wasm** | คอมไพล์เป็น WebAssembly |
| **กระพือสร้าง** | แอพมือถือ/เดสก์ท็อป |
| **นักเทียบท่า** | แอปเซิร์ฟเวอร์คอนเทนเนอร์ |
| **Google Cloud Run** | คอนเทนเนอร์แบบไร้เซิร์ฟเวอร์ |
| **โฮสติ้ง Firebase** | เว็บแอปโฮสติ้ง |
---

## สรุป
ระบบนิเวศของ Dart ถูกครอบงำโดย **Flutter** สำหรับการพัฒนา UI ข้ามแพลตฟอร์ม สำหรับ Dart ฝั่งเซิร์ฟเวอร์ **Shelf** คือเฟรมเวิร์ก HTTP มาตรฐาน โดยมี **Dart Frog** เป็นตัวเลือกแบบเต็มสแต็ก สแต็กมาตรฐานคือ: **Dart 3.4+** สำหรับรันไทม์, **pub.dev** สำหรับแพ็คเกจ, **Flutter** สำหรับ UI บนมือถือ/เว็บ/เดสก์ท็อป, **Riverpod** หรือ **Bloc** สำหรับการจัดการสถานะ, **Drift** สำหรับฐานข้อมูล, **ทดสอบ** สำหรับการทดสอบ และ **dart วิเคราะห์** สำหรับ Linting จุดแข็งของ Dart คือความปลอดภัยแบบ null ที่ดี การคอมไพล์ที่รวดเร็ว การรีโหลดแบบร้อน (Flutter) และความสามารถในการคอมไพล์เป็นภาษาเนทีฟ, JavaScript หรือ WebAssembly ระบบนิเวศนี้เหมาะอย่างยิ่งสำหรับแอปพลิเคชันมือถือ เว็บ และเดสก์ท็อปข้ามแพลตฟอร์ม