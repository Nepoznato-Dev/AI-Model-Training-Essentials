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
# Dart — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Dart.
---

## Rantai Alat
| Alat | Tujuan |
|------|---------|
| **panah** | Dart SDK (kompiler, pemformat, penganalisis) |
| **berdebar** | Flutter SDK (termasuk Dart) |
| **pub** | Manajer paket (dibangun di dart) |
| **analisis panah** | Analisis statis |
| **format panah** | Pemformatan kode |
| **kompilasi panah** | Kompilasi ke native/JS/WASM |
| **lari cepat** | Jalankan skrip Dart |
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

## Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **pub.dev** | Repositori paket resmi |
| **pub panah** | CLI manajer paket |
| **pubspec.yaml** | Manifes paket |
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

## Flutter (Kerangka Dart UI)
| Teknologi | Tujuan |
|------------|---------|
| **Berkibar** | Kerangka UI lintas platform |
| **Web Berkibar** | Aplikasi web dengan Flutter |
| **Desktop Berkibar** | Windows, macOS, Linux |
| **Flutter Ponsel** | iOS dan Android |
| **Flutter Tertanam** | Perangkat tertanam |
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

## Kerangka Web (Dart Sisi Server)
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Rak** | Berbasis middleware | Server HTTP (paling populer) |
| **Katak Panah** | Tumpukan penuh | Kerangka kerja backend (seperti Laravel) |
| **Malaikat** | API REST | API Sederhana |
| **Alfred** | Seperti ekspres | Server bergaya Node.js |
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

## Basis Data
| Teknologi | Ketik |
|------------|------|
| **Melayang** | SQL yang aman untuk tipe (menggantikan Moor) |
| **Kotak Objek** | Basis data seluler NoSQL |
| **Isar** | Basis data seluler cepat |
| **Sarang** | Nilai kunci yang ringan |
| **postgres** | Klien PostgreSQL |
| **mysql1** | Klien MySQL |
| **basis sofa** | Klien sofa |
| **Supabase** | Backend-sebagai-layanan |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **tes** | Kerangka pengujian bawaan |
| **mockito** | Mengejek |
| **moktail** | Ejekan yang tidak aman |
| **uji_flutter** | Pengujian widget Flutter |
| **uji_integrasi** | Pengujian ujung ke ujung |
| **perangkat_emas** | Pengujian emas/snapshot |
| **patroli** | Pengujian integrasi Flutter |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **analisis panah** | Analisis statis bawaan |
| **format panah** | Pemformat bawaan |
| **lint** | Aturan serat resmi |
| **flutter_lints** | Lint khusus Flutter |
| **analisis_sangat_bagus** | Aturan serat yang ketat |
| **cakupan** | Cakupan kode |
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

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **panah:inti** | Perpustakaan standar |
| **panah:async** | Berjangka, Aliran, async |
| **panah:io** | Berkas, HTTP, TCP |
| **panah:konversi** | JSON, UTF-8 |
| **http** | Klien HTTP |
| **dio** | Klien HTTP (Flutter) |
| **json_serializable** | Pembuatan kode JSON |
| **dibekukan** | Kelas data yang tidak dapat diubah |
| **sungai** | Pengelolaan negara |
| **blok / hasta** | Pengelolaan negara |
| **dapatkan_itu** | Injeksi ketergantungan |
| **pergi_router** | Perutean deklaratif |
| **dapat disamakan** | Nilai kesetaraan |
| **uuid** | generasi UUID |
| **kripto** | Kriptografi |
| **jalur** | Manipulasi jalur file |
| **koleksi** | Jenis koleksi tambahan |
| **intl** | Internasionalisasi |
---

## Manajemen Negara (Flutter)
| Solusi | Ketik |
|----------|------|
| **Pod Sungai** | Aman untuk kompilasi, dapat diuji |
| **Blok / Hasta** | Didorong oleh peristiwa, dapat diprediksi |
| **Penyedia** | Terintegrasi, sederhana |
| **DapatkanX** | All-in-one (kontroversial) |
| **Sinyal** | Primitif reaktif |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + Panah** | Dukungan Dart/Flutter terbaik |
| **Android Studio + Flutter** | IDE Flutter Penuh |
| **IntelliJ + Dart** | Dukungan JetBrain |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Kompilasi panah** | Eksekusi asli |
| **Kompilasi panah js** | Kompilasi ke JavaScript |
| **Dart kompilasi wasm** | Kompilasi ke WebAssembly |
| **Bangunan bergetar** | Aplikasi seluler/desktop |
| **Buruh pelabuhan** | Aplikasi server dalam container |
| **Google Cloud Run** | Kontainer tanpa server |
| **Firebase Hosting** | Hosting aplikasi web |
---

## Ringkasan
Ekosistem Dart didominasi oleh **Flutter** untuk pengembangan UI lintas platform. Untuk Dart sisi server, **Shelf** adalah kerangka kerja HTTP standar, dengan **Dart Frog** sebagai opsi tumpukan penuh. Tumpukan standarnya adalah: **Dart 3.4+** sebagai runtime, **pub.dev** untuk paket, **Flutter** untuk UI seluler/web/desktop, **Riverpod** atau **Bloc** untuk pengelolaan status, **Drift** untuk database, **test** untuk pengujian, dan **dart analysis** untuk linting. Kekuatan Dart adalah keamanan null yang baik, kompilasi cepat, hot reload (Flutter), dan kemampuan untuk mengkompilasi ke native, JavaScript, atau WebAssembly. Ekosistem ini ideal untuk aplikasi seluler, web, dan desktop lintas platform.