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
# Dart – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im Dart-Ökosystem.
---

## Werkzeugkette
| Werkzeug | Zweck |
|------|---------|
| **Dart** | Dart SDK (Compiler, Formatierer, Analysator) |
| **flattern** | Flutter SDK (einschließlich Dart) |
| **Kneipe** | Paketmanager (in Dart integriert) |
| **Dart-Analyse** | Statische Analyse |
| **Dartformat** | Codeformatierung |
| **Dart-Kompilierung** | Kompilieren nach native/JS/WASM |
| **Dartlauf** | Dart-Skripte ausführen |
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

## Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **pub.dev** | Offizielles Paket-Repository |
| **Dart-Pub** | Paketmanager-CLI |
| **pubspec.yaml** | Paketmanifest |
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
| Technologie | Zweck |
|------------|---------|
| **Flattern** | Plattformübergreifendes UI-Framework |
| **Flatternetz** | Web-Apps mit Flutter |
| **Flutter Desktop** | Windows, macOS, Linux |
| **Flutter Mobile** | iOS und Android |
| **Flutter eingebettet** | Eingebettete Geräte |
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

## Web Frameworks (serverseitiger Dart)
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **Regal** | Middleware-basiert | HTTP-Server (am beliebtesten) |
| **Pfeilfrosch** | Full-Stack | Backend-Framework (wie Laravel) |
| **Engel** | REST-API | Einfache APIs |
| **Alfred** | Express-artig | Server im Node.js-Stil |
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

## Datenbank
| Technologie | Geben Sie | ein
|------------|------|
| **Drift** | Typsicheres SQL (ersetzt Moor) |
| **ObjectBox** | NoSQL-Mobildatenbank |
| **Isar** | Schnelle mobile Datenbank |
| **Bienenstock** | Leichter Schlüsselwert |
| **postgres** | PostgreSQL-Client |
| **mysql1** | MySQL-Client |
| **Sofagestell** | Couchbase-Client |
| **Supabase** | Backend-as-a-Service |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **Test** | Integriertes Test-Framework |
| **Mockito** | Spott |
| **Mocktail** | Null-sicheres Spotten |
| **flutter_test** | Testen des Flutter-Widgets |
| **integrationstest** | End-to-End-Tests |
| **golden_toolkit** | Golden/Snapshot-Test |
| **Patrouille** | Flutter-Integrationstests |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **Dart-Analyse** | Integrierte statische Analyse |
| **Dartformat** | Integrierter Formatierer |
| **Fusseln** | Offizielle Flusenregeln |
| **flutter_lints** | Flatterspezifische Flusen |
| **sehr_gute_analyse** | Strenge Flusenregeln |
| **Abdeckung** | Codeabdeckung |
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

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **dart:core** | Standardbibliothek |
| **dart:async** | Futures, Streams, asynchron |
| **dart:io** | Datei, HTTP, TCP |
| **dart:convert** | JSON, UTF-8 |
| **http** | HTTP-Client |
| **dio** | HTTP-Client (Flutter) |
| **json_serializable** | JSON-Codegenerierung |
| **eingefroren** | Unveränderliche Datenklassen |
| **Riverpod** | Staatsverwaltung |
| **Block / Elle** | Staatsverwaltung |
| **get_it** | Abhängigkeitsinjektion |
| **go_router** | Deklaratives Routing |
| **gleichwertig** | Wertegleichheit |
| **uuid** | UUID-Generierung |
| **Krypto** | Kryptographie |
| **Pfad** | Dateipfadmanipulation |
| **Sammlung** | Zusätzliche Sammlungstypen |
| **intl** | Internationalisierung |
---

## Zustandsverwaltung (Flutter)
| Lösung | Geben Sie | ein
|----------|------|
| **Riverpod** | Kompiliersicher, testbar |
| **Block / Elle** | Ereignisgesteuert, vorhersehbar |
| **Anbieter** | Eingebaut, einfach |
| **GetX** | All-in-One (umstritten) |
| **Signale** | Reaktive Grundelemente |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **VS-Code + Dart** | Beste Dart/Flutter-Unterstützung |
| **Android Studio + Flutter** | Vollständige Flutter-IDE |
| **IntelliJ + Dart** | JetBrains-Unterstützung |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Dart-Kompilierung** | Native ausführbare Dateien |
| **Dart js kompilieren** | In JavaScript kompilieren |
| **Dart-Kompilierung wasm** | In WebAssembly kompilieren |
| **Flutter-Build** | Mobile/Desktop-Apps |
| **Docker** | Containerisierte Server-Apps |
| **Google Cloud Run** | Serverlose Container |
| **Firebase-Hosting** | Web-App-Hosting |
---

## Zusammenfassung
Das Dart-Ökosystem wird von **Flutter** für die plattformübergreifende UI-Entwicklung dominiert. Für serverseitiges Dart ist **Shelf** das Standard-HTTP-Framework, mit **Dart Frog** als Full-Stack-Option. Der Standard-Stack ist: **Dart 3.4+** als Laufzeit, **pub.dev** für Pakete, **Flutter** für Mobil-/Web-/Desktop-UI, **Riverpod** oder **Bloc** für die Zustandsverwaltung, **Drift** für Datenbanken, **test** für Tests und **dartanalysieren** für Linting. Die Stärken von Dart sind solide Nullsicherheit, schnelle Kompilierung, Hot-Reload (Flutter) und die Möglichkeit zur Kompilierung in natives JavaScript oder WebAssembly. Das Ökosystem ist ideal für plattformübergreifende Mobil-, Web- und Desktop-Anwendungen.