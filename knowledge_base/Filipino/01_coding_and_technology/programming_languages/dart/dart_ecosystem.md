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
# Dart — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, framework, at imprastraktura sa Dart ecosystem.
---

## Toolchain
| Tool | Layunin |
|------|---------|
| **dart** | Dart SDK (compiler, formatter, analyzer) |
| **flutter** | Flutter SDK (kasama ang Dart) |
| **pub** | Package manager (built into dart) |
| **dart analysis** | Static na pagsusuri |
| **format ng dart** | Pag-format ng code |
| **dart compile** | Mag-compile sa native/JS/WASM |
| **dart run** | Patakbuhin ang mga Dart script |
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

## Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **pub.dev** | Opisyal na imbakan ng package |
| **dart pub** | Package manager CLI |
| **pubspec.yaml** | Package manifest |
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

## Flutter (Dart UI Framework)
| Teknolohiya | Layunin |
|------------|---------|
| **Pag-flutter** | Cross-platform UI framework |
| **Flutter Web** | Mga web app na may Flutter |
| **Flutter Desktop** | Windows, macOS, Linux |
| **Flutter Mobile** | iOS at Android |
| **Flutter Embedded** | Mga naka-embed na device |
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

## Web Frameworks (Server-Side Dart)
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **Shelf** | Nakabatay sa Middleware | HTTP server (pinakatanyag) |
| **Dart Frog** | Full-stack | Backend framework (tulad ng Laravel) |
| **Anghel** | REST API | Mga Simpleng API |
| **Alfred** | Express-like | Node.js-style na server |
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

## Database
| Teknolohiya | Uri |
|------------|------|
| **Pag-anod** | Ligtas sa uri ng SQL (pinapalitan ang Moor) |
| **ObjectBox** | NoSQL mobile database |
| **Isar** | Mabilis na mobile database |
| **Hive** | Magaan na key-value |
| **postgres** | PostgreSQL client |
| **mysql1** | MySQL client |
| **couchbase** | Couchbase client |
| **Supabase** | Backend-bilang-isang-serbisyo |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **pagsubok** | Built-in na balangkas ng pagsubok |
| **mockito** | Nanunuya |
| **mocktail** | Null-safe na pangungutya |
| **flutter_test** | Pagsubok ng flutter widget |
| **integration_test** | End-to-end na pagsubok |
| **golden_toolkit** | Golden/snapshot na pagsubok |
| **patrol** | Flutter integration testing |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **dart analysis** | Built-in na static na pagsusuri |
| **format ng dart** | Built-in na formatter |
| **lints** | Mga opisyal na panuntunan sa lint |
| **flutter_lints** | Flutter-specific na lints |
| **very_good_analysis** | Mahigpit na mga panuntunan sa lint |
| **saklaw** | Saklaw ng code |
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

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **dart:core** | Karaniwang aklatan |
| **dart:async** | Futures, Streams, async |
| **dart:io** | File, HTTP, TCP |
| **dart:convert** | JSON, UTF-8 |
| **http** | HTTP client |
| **dio** | HTTP client (Flutter) |
| **json_serializable** | Pagbuo ng JSON code |
| **na-freeze** | Mga hindi nababagong klase ng data |
| **riverpod** | Pamamahala ng estado |
| **bloc / cubit** | Pamamahala ng estado |
| **get_it** | Dependency injection |
| **go_router** | Pahayag na pagruruta |
| **mapapantay** | Pagkakapantay-pantay ng halaga |
| **uuuid** | henerasyon ng UUID |
| **crypto** | Cryptography |
| **landas** | Pagmamanipula ng landas ng file |
| **koleksyon** | Mga karagdagang uri ng koleksyon |
| **intl** | Internasyonalisasyon |
---

## Pamamahala ng Estado (Flutter)
| Solusyon | Uri |
|----------|------|
| **Riverpod** | Compile-safe, masusubok |
| **Bloc / Cubit** | Dahil sa kaganapan, predictable |
| **Provider** | Built-in, simple |
| **GetX** | All-in-one (kontrobersyal) |
| **Mga Senyales** | Mga reaktibong primitibo |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code + Dart** | Pinakamahusay na suporta sa Dart/Flutter |
| **Android Studio + Flutter** | Buong Flutter IDE |
| **IntelliJ + Dart** | Suporta sa JetBrains |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Dart compile** | Mga katutubong executable |
| **Dart compile js** | Mag-compile sa JavaScript |
| **Dart compile wasm** | Mag-compile sa WebAssembly |
| **Flutter build** | Mga mobile/desktop na app |
| **Docker** | Containerized server app |
| **Google Cloud Run** | Mga container na walang server |
| **Firebase Hosting** | Pagho-host ng web app |
---

## Buod
Ang ecosystem ng Dart ay pinangungunahan ng **Flutter** para sa cross-platform UI development. Para sa server-side na Dart, **Shelf** ay ang karaniwang HTTP framework, na may **Dart Frog** bilang isang full-stack na opsyon. Ang karaniwang stack ay: **Dart 3.4+** bilang runtime, **pub.dev** para sa mga package, **Flutter** para sa mobile/web/desktop UI, **Riverpod** o **Bloc** para sa pamamahala ng estado, **Drift** para sa mga database, **test** para sa pagsubok, at **dart analysis** para sa linting. Ang mga kalakasan ni Dart ay ligtas na walang bisa, mabilis na compilation, mainit na pag-reload (Flutter), at ang kakayahang mag-compile sa native, JavaScript, o WebAssembly. Ang ecosystem ay perpekto para sa cross-platform na mobile, web, at desktop application.