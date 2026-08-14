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
# Dart — Ekosistem ve Takım Kılavuzu
Bu kılavuz Dart ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Alet Zinciri
| Araç | Amaç |
|------|------------|
| **dart** | Dart SDK (derleyici, biçimlendirici, analizör) |
| **çarpıntı** | Flutter SDK'sı (Dart'ı içerir) |
| **bar** | Paket yöneticisi (dart'ta yerleşik) |
| **dart analizi** | Statik analiz |
| **dart formatı** | Kod biçimlendirme |
| **dart derlemesi** | Yerel/JS/WASM'ye derleme |
| **dart koşusu** | Dart komut dosyalarını çalıştırın |
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

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **pub.dev** | Resmi paket deposu |
| **dart barı** | Paket yöneticisi CLI |
| **pubspec.yaml** | Paket bildirimi |
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

## Flutter (Dart UI Çerçevesi)
| Teknoloji | Amaç |
|---------------|-----------|
| **Çarpıntı** | Platformlar arası kullanıcı arayüzü çerçevesi |
| **Çırpınan Web** | Flutter'lı web uygulamaları |
| **Flutter Masaüstü** | Windows, macOS, Linux |
| **Flutter Mobil** | iOS ve Android |
| **Flutter Gömülü** | Gömülü cihazlar |
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

## Web Çerçeveleri (Sunucu Tarafı Dart)
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Raf** | Ara yazılım tabanlı | HTTP sunucusu (en popüler) |
| **Dart Kurbağası** | Tam yığın | Arka uç çerçevesi (Laravel gibi) |
| **Melek** | REST API'si | Basit API'ler |
| **Alfred** | Ekspres benzeri | Node.js tarzı sunucu |
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

## Veritabanı
| Teknoloji | Tür |
|---------------|------|
| **Sürüklenme** | Tür açısından güvenli SQL (Moor'un yerine geçer) |
| **ObjectBox** | NoSQL mobil veritabanı |
| **İsar** | Hızlı mobil veritabanı |
| **Kovan** | Hafif anahtar/değer çifti |
| **postgres** | PostgreSQL istemcisi |
| **mysql1** | MySQL istemcisi |
| **kanepe tabanı** | Couchbase istemcisi |
| **Supaba** | Hizmet olarak arka uç |
| **Firebase** | Google BaaS'ı |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **test** | Yerleşik test çerçevesi |
| **sahte** | Alaycı |
| **taklit** | Sıfır güvenli alay |
| **flutter_test** | Flutter widget testi |
| **entegrasyon_testi** | Uçtan uca test |
| **golden_toolkit** | Altın/anlık görüntü testi |
| **devriye** | Flutter entegrasyon testi |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **dart analizi** | Dahili statik analiz |
| **dart formatı** | Dahili formatlayıcı |
| **tüy tüyleri** | Resmi tüy bırakmama kuralları |
| **flutter_lints** | Flutter'a özgü tüyler |
| **çok_iyi_analiz** | Sıkı tüy bırakmayan kurallar |
| **kapsam** | Kod kapsamı |
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

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **dart:çekirdek** | Standart kütüphane |
| **dart:eşzamansız** | Vadeli İşlemler, Akışlar, Eşzamansız |
| **dart:io** | Dosya, HTTP, TCP |
| **dart:dönüştürme** | JSON, UTF-8 |
| **http** | HTTP istemcisi |
| **dio** | HTTP istemcisi (Flutter) |
| **json_serializable** | JSON kodu oluşturma |
| **dondurulmuş** | Değişmez veri sınıfları |
| **nehir kapsülü** | Devlet yönetimi |
| **blok / arşın** | Devlet yönetimi |
| **get_it** | Bağımlılık enjeksiyonu |
| **go_router** | Bildirimsel yönlendirme |
| **eşitlenebilir** | Değer eşitliği |
| **uuid** | UUID oluşturma |
| **kripto** | Kriptografi |
| **yol** | Dosya yolu manipülasyonu |
| **koleksiyon** | Ekstra koleksiyon türleri |
| **uluslararası** | Uluslararasılaşma |
---

## Devlet Yönetimi (Flutter)
| Çözüm | Tür |
|----------|------|
| **Nehirpod** | Derleme açısından güvenli, test edilebilir |
| **Blok / Arşın** | Olay odaklı, öngörülebilir |
| **Sağlayıcı** | Yerleşik, basit |
| **X'i edinin** | Hepsi bir arada (tartışmalı) |
| **Sinyaller** | Reaktif ilkeller |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + Dart** | En İyi Dart/Flutter desteği |
| **Android Studio + Flutter** | Tam Flutter IDE |
| **IntelliJ + Dart** | JetBrains desteği |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Dart derlemesi** | Yerel yürütülebilir dosyalar |
| **Dart js'yi derleme** | JavaScript'e Derle |
| **Dart derlemesi wasm** | WebAssembly'de Derle |
| **Flutter yapısı** | Mobil/masaüstü uygulamalar |
| **Docker** | Container mimarisine alınmış sunucu uygulamaları |
| **Google Cloud Run** | Sunucusuz konteynerler |
| **Firebase Barındırma** | Web uygulaması barındırma |
---

## Özet
Dart'ın ekosistemi, platformlar arası kullanıcı arayüzü geliştirme açısından **Flutter**'ın hakimiyetindedir. Sunucu tarafı Dart için **Shelf** standart HTTP çerçevesidir ve **Dart Frog** tam yığın seçeneğidir. Standart yığın şöyledir: Çalışma zamanı olarak **Dart 3.4+**, paketler için **pub.dev**, mobil/web/masaüstü kullanıcı arayüzü için **Flutter**, durum yönetimi için **Riverpod** veya **Bloc**, veritabanları için **Drift**, test için **test** ve linting için **dart analizi**. Dart'ın güçlü yönleri sağlam sıfır güvenliği, hızlı derleme, çalışırken yeniden yükleme (Flutter) ve yerel, JavaScript veya WebAssembly'ye derleme yeteneğidir. Ekosistem, platformlar arası mobil, web ve masaüstü uygulamaları için idealdir.