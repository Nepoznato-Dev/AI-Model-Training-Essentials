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
# Dart - Mfumo wa Ikolojia na Mwongozo wa zana
Mwongozo huu unashughulikia zana muhimu, mifumo, na miundombinu katika mfumo ikolojia wa Dart.
---

##Mnyororo wa zana
| Zana | Kusudi |
|------|----------|
| **dart** | Dart SDK (compiler, formatter, analyzer) |
| **pepeta** | Flutter SDK (pamoja na Dart) |
| **baa** | Kidhibiti kifurushi (kimejengwa ndani ya dart) |
| **chambua dart** | Uchambuzi tuli |
| **umbizo la dati** | Uumbizaji wa msimbo |
| **kukusanya dart** | Unganisha kwa asili/JS/WASM |
| **kukimbia** | Endesha maandishi ya Dart |
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

## Usimamizi wa Kifurushi
| Zana | Kusudi |
|------|----------|
| **pub.dev** | Hazina rasmi ya kifurushi |
| **baa ya dart** | Meneja wa kifurushi CLI |
| **pubspec.yaml** | Faili ya maelezo ya kifurushi |
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

## Flutter (Mfumo wa UI wa Dart)
| Teknolojia | Kusudi |
|------------|---------|
| **Flutter** | Mfumo wa UI wa jukwaa-mbali |
| **Mtandao wa Flutter** | Programu za wavuti zilizo na Flutter |
| **Desktop ya Flutter** | Windows, macOS, Linux |
| **Flutter Mobile** | iOS na Android |
| **Flutter Iliyopachikwa** | Vifaa vilivyopachikwa |
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

## Mifumo ya Wavuti (Seva-Side Dart)
| Mfumo | Andika | Bora Kwa |
|-----------|------|-----------|
| **Rafu** | Kulingana na vifaa vya kati | Seva ya HTTP (maarufu zaidi) |
| **Chura wa Dart** | Rafu kamili | Mfumo wa nyuma (kama Laravel) |
| **Malaika** | REST API | API Rahisi |
| **Alfred** | Express-kama | Seva ya mtindo wa Node.js |
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

## Hifadhidata
| Teknolojia | Andika |
|------------|------|
| **Drift** | SQL ya aina salama (inachukua nafasi ya Moor) |
| **Sanduku la Kitu** | Hifadhidata ya rununu ya NoSQL |
| **Isar** | Hifadhidata ya haraka ya rununu |
| **Mzinga** | Thamani nyepesi ya ufunguo |
| **postgres** | Mteja wa PostgreSQL |
| **mysql1** | Mteja wa MySQL |
| **msingi wa kitanda** | Mteja wa Couchbase |
| **Supabase** | Nyuma-kama-huduma |
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

##Upimaji
| Mfumo | Kusudi |
|-----------|---------|
| **jaribio** | Mfumo wa majaribio uliojumuishwa |
| **mockito** | Mzaha |
| **kejeli** | Kejeli zisizo salama |
| **mtihani_wa_flutter** | Jaribio la wijeti ya Flutter |
| **jaribio_la_ujumuishaji** | Mtihani wa mwisho hadi mwisho |
| **zana_za_dhahabu** | Upimaji wa dhahabu/picha |
| **doria** | Jaribio la ujumuishaji wa Flutter |
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

## Ubora wa Kanuni
| Zana | Kusudi |
|------|----------|
| **chambua dart** | Uchambuzi tuli uliojengewa ndani |
| **umbizo la dati** | Umbizo lililojengewa ndani |
| **vingi** | Sheria rasmi za pamba |
| **vipande_vya_kupepea** | Vitambaa maalum vya Flutter |
| **uchambuzi_mzuri sana** | Sheria kali za pamba |
| ** chanjo** | Chanjo ya msimbo |
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

## Maktaba Muhimu
| Maktaba | Kusudi |
|---------|---------|
| **dart:msingi** | Maktaba ya kawaida |
| **dart:async** | Wakati Ujao, Mitiririko, Async |
| **dart:io** | Faili, HTTP, TCP |
| **dart:badilisha** | JSON, UTF-8 |
| **http** | mteja wa HTTP |
| **dio** | Kiteja cha HTTP (Flutter) |
| **json_serializable** | Uzalishaji wa msimbo wa JSON |
| **imeganda** | Madarasa ya data yasiyobadilika |
| **dungu la mto** | Usimamizi wa serikali |
| **bloki / dhiraa** | Usimamizi wa serikali |
| **pata_* | Sindano ya utegemezi |
| **go_router** | Uelekezaji wa kutangaza |
| **sawa** | Thamani usawa |
| **uuid** | kizazi cha UUID |
| **crypto** | Crystalgraphy |
| **njia** | Udanganyifu wa njia ya faili |
| **mkusanyiko** | Aina za mkusanyiko wa ziada |
| **intl** | Kimataifa |
---

## Usimamizi wa Jimbo (Flutter)
| Suluhisho | Andika |
|----------|------|
| **Mto** | Kukusanya-salama, inayoweza kujaribiwa |
| **Bloki / Cubit** | Inaendeshwa na tukio, inatabirika |
| **Mtoa huduma** | Imejengwa ndani, rahisi |
| **PataX** | Yote-kwa-moja (yenye utata) |
| **Ishara** | Asili tendaji |
---

## Vitambulisho na Vihariri
| ID | Nguvu |
|-----|------------|
| **Msimbo wa VS + Dart** | Usaidizi bora wa Dart/Flutter |
| **Studio ya Android + Flutter** | IDE Kamili ya Flutter |
| **IntelliJ + Dart** | JetBrains msaada |
---

## Usambazaji
| Mbinu | Vidokezo |
|--------|-------|
| **Mkusanyiko wa Dart** | Utekelezaji asilia |
| **Unda js** | Unganisha kwa JavaScript |
| **Undani wa Dart wasm** | Unganisha kwa WebAssembly |
| **Flutter kujenga** | Programu za rununu/desktop |
| **Docker** | Programu za seva zilizowekwa kwenye vyombo |
| **Google Cloud Run** | Vyombo visivyo na seva |
| **Kukaribisha Firebase** | Kupangisha programu za wavuti |
---

## Muhtasari
Mfumo ikolojia wa Dart unatawaliwa na **Flutter** kwa ajili ya ukuzaji wa kiolesura cha majukwaa mtambuka. Kwa Dart ya upande wa seva, **Rafu** ndiyo mfumo wa kawaida wa HTTP, na **Dart Frog** kama chaguo la mrundikano kamili. Rafu ya kawaida ni: **Dart 3.4+** kama wakati wa utekelezaji, **pub.dev** kwa vifurushi, **Flutter** kwa kiolesura cha rununu/mtandao/desktop, **Riverpod** au **Bloc** kwa usimamizi wa serikali, **Drift** kwa hifadhidata, **jaribio** kwa majaribio, na **kuchanganua dart.** Uimara wa Dart ni usalama usio na sauti, mkusanyiko wa haraka, upakiaji upya wa moto (Flutter), na uwezo wa kukusanya kwa asili, JavaScript, au WebAssembly. Mfumo ikolojia ni bora kwa matumizi ya simu za rununu, wavuti na eneo-kazi.