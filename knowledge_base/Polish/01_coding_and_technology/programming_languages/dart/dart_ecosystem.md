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
# Dart — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, struktury i infrastrukturę w ekosystemie Dart.
---

## Łańcuch narzędzi
| Narzędzie | Cel |
|------|-------------|
| **strzałka** | Dart SDK (kompilator, formater, analizator) |
| **trzepotanie** | Flutter SDK (zawiera Dart) |
| **pub** | Menedżer pakietów (wbudowany w dart) |
| **analiza strzałek** | Analiza statyczna |
| **format darta** | Formatowanie kodu |
| **kompilacja darta** | Kompiluj do natywnego/JS/WASM |
| **bieg dartowy** | Uruchom skrypty Dart |
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

## Zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **pub.dev** | Oficjalne repozytorium pakietów |
| **pub dartowy** | Menedżer pakietów CLI |
| **pubspec.yaml** | Manifest pakietu |
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

## Flutter (Framework interfejsu Dart)
| Technologia | Cel |
|------------|------------|
| **Trzepotanie** | Wieloplatformowy framework interfejsu użytkownika |
| **Trzepotająca sieć** | Aplikacje internetowe z Flutterem |
| **Trzepotający pulpit** | Windows, macOS, Linux |
| **Flutter Mobile** | iOS i Android |
| **Wbudowane trzepotanie** | Urządzenia wbudowane |
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

## Struktury internetowe (Dart po stronie serwera)
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **Półka** | Oparte na oprogramowaniu pośrednim | Serwer HTTP (najpopularniejszy) |
| **Żaba Dart** | Pełny stos | Framework backendowy (jak Laravel) |
| **Anioł** | API REST | Proste API |
| **Alfred** | Ekspresowo | Serwer w stylu Node.js |
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

## Baza danych
| Technologia | Wpisz |
|------------|------|
| **Drift** | Bezpieczny typ SQL (zastępuje Moora) |
| **ObjectBox** | Mobilna baza danych NoSQL |
| **Izar** | Szybka mobilna baza danych |
| **Ul** | Lekka para klucz-wartość |
| **postgres** | Klient PostgreSQL |
| **mysql1** | Klient MySQL |
| **podstawa** | Klient couchbase |
| **Supabaza** | Backend jako usługa |
| **Baza Firebase** | Google BaaS |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **test** | Wbudowane środowisko testowe |
| **mockito** | Kpiąco |
| **makieta** | Null-safe kpina |
| **test_trzepotania** | Testowanie widgetu Flutter |
| **test_integracji** | Testowanie typu end-to-end |
| **złoty_zestaw narzędzi** | Testowanie złotego/migawkowego |
| **patrol** | Testowanie integracji Fluttera |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **analiza strzałek** | Wbudowana analiza statyczna |
| **format darta** | Wbudowany formatyzator |
| **kłaczki** | Oficjalne zasady lintowania |
| **trzepotanie_lints** | Specyficzne dla trzepotania kłaczki |
| **bardzo_dobra_analiza** | Surowe zasady dotyczące lint |
| **zasięg** | Pokrycie kodu |
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

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **strzałka:rdzeń** | Biblioteka standardowa |
| **rzutka:asynchronizacja** | Kontrakty terminowe, strumienie, asynchroniczne |
| **rzutka:io** | Plik, HTTP, TCP |
| **rzutka:konwertuj** | JSON, UTF-8 |
| **http** | Klient HTTP |
| **dio** | Klient HTTP (Flutter) |
| **json_serializable** | Generowanie kodu JSON |
| **zamrożone** | Niezmienne klasy danych |
| **podwodne** | Zarządzanie państwem |
| **blok / łokieć** | Zarządzanie państwem |
| **get_it** | Zastrzyk zależności |
| **go_router** | Routing deklaratywny |
| **równe** | Równość wartości |
| **uid** | Generowanie UUID |
| **krypto** | Kryptografia |
| **ścieżka** | Manipulacja ścieżką pliku |
| **kolekcja** | Dodatkowe typy kolekcji |
| **int** | Internacjonalizacja |
---

## Zarządzanie stanem (trzepotanie)
| Rozwiązanie | Wpisz |
|-------------|------|
| **Pod rzeką** | Bezpieczne dla kompilacji, testowalne |
| **Blok / Łokieć** | Oparta na zdarzeniach, przewidywalna |
| **Dostawca** | Wbudowany, prosty |
| **GetX** | Wszystko w jednym (kontrowersyjne) |
| **Sygnały** | Reaktywne prymitywy |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS + Strzałka** | Najlepsza obsługa Dart/Flutter |
| **Android Studio + Flutter** | Pełne trzepotanie IDE |
| **IntelliJ + Dart** | Wsparcie JetBrains |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Dartowa kompilacja** | Natywne pliki wykonywalne |
| **Dart skompiluj js** | Kompiluj do JavaScript |
| **Dart skompilować wasm** | Kompiluj do zestawu WebAssembly |
| **Trzepotająca kompilacja** | Aplikacje mobilne/stacjonarne |
| **Doker** | Kontenerowe aplikacje serwerowe |
| **Google Cloud Run** | Kontenery bezserwerowe |
| **Hosting Firebase** | Hosting aplikacji internetowych |
---

## Streszczenie
Ekosystem Darta jest zdominowany przez **Flutter** do tworzenia wieloplatformowego interfejsu użytkownika. W przypadku Darta po stronie serwera **Shelf** to standardowy framework HTTP, z **Dart Frog** jako opcją pełnego stosu. Standardowy stos to: **Dart 3.4+** jako środowisko wykonawcze, **pub.dev** dla pakietów, **Flutter** dla mobilnego/internetowego/komputerowego interfejsu użytkownika, **Riverpod** lub **Bloc** do zarządzania stanem, **Drift** dla baz danych, **test** do testowania i **analiza dart** do lintingu. Mocnymi stronami Darta są zerowe bezpieczeństwo, szybka kompilacja, ponowne ładowanie na gorąco (Flutter) i możliwość kompilacji do kodu natywnego, JavaScript lub WebAssembly. Ekosystem jest idealny do wieloplatformowych aplikacji mobilnych, internetowych i stacjonarnych.