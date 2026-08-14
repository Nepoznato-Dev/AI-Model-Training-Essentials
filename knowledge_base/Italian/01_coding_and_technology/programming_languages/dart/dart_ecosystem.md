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
# Dart: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e le infrastrutture essenziali nell'ecosistema Dart.
---

## Catena di strumenti
| Strumento | Scopo |
|------|---------|
| **dardo** | Dart SDK (compilatore, formattatore, analizzatore) |
| **svolazzare** | SDK Flutter (include Dart) |
| **pub** | Gestore pacchetti (integrato in dart) |
| **analisi del dardo** | Analisi statica |
| **formato dardo** | Formattazione del codice |
| **compilazione freccette** | Compilare in nativo/JS/WASM |
| **corsa di freccette** | Esegui script Dart |
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

## Gestione dei pacchetti
| Strumento | Scopo |
|------|---------|
| **pub.dev** | Repository ufficiale dei pacchetti |
| **pub delle freccette** | CLI del gestore pacchetti |
| **pubspec.yaml** | Manifesto del pacchetto |
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

## Flutter (Framework dell'interfaccia utente di Dart)
| Tecnologia | Scopo |
|------------|---------|
| **Svolazzare** | Framework dell'interfaccia utente multipiattaforma |
| **Web svolazzante** | App Web con Flutter |
| **Desktop svolazzante** | Windows, macOS, Linux |
| **Cellulare svolazzante** | iOS e Android |
| **Flutter incorporato** | Dispositivi integrati |
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

## Framework Web (Dart lato server)
| Quadro | Digitare | Ideale per |
|-----------|------|----------|
| **Scaffale** | Basato su middleware | Server HTTP (il più popolare) |
| **Dardo Rana** | Stack completo | Framework backend (come Laravel) |
| **Angelo** | API REST | API semplici |
| **Alfred** | Tipo espresso | Server in stile Node.js |
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

##Banca dati
| Tecnologia | Digitare |
|------------|------|
| **Deriva** | SQL indipendente dai tipi (sostituisce Moor) |
| **ObjectBox** | Database mobile NoSQL |
| **Isar** | Database mobile veloce |
| **Alveare** | Valore-chiave leggero |
| **postgres** | Client PostgreSQL |
| **mysql1** | Client MySQL |
| **rete divano** | Cliente di Couchbase |
| **Supbase** | Backend come servizio |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **prova** | Quadro di test integrato |
| **mockito** | Beffardo |
| **cocktail** | Derisione a prova di null |
| **test_flutter** | Test del widget Flutter |
| **test_integrazione** | Test end-to-end |
| **golden_toolkit** | Test Golden/istantanea |
| **pattuglia** | Test di integrazione Flutter |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **analisi del dardo** | Analisi statica integrata |
| **formato dardo** | Formattatore integrato |
| **lanugine** | Regole ufficiali sui pelucchi |
| **flutter_lints** | Lanugine specifiche per Flutter |
| **analisi_molto_buona** | Regole rigorose per la lanugine |
| **copertura** | Copertura del codice |
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

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **dardo:nucleo** | Libreria standard |
| **dardo:asincrono** | Futures, Streams, asincroni |
| **dardo:io** | File, HTTP, TCP |
| **dart:converti** | JSON, UTF-8 |
| **http** | Client HTTP |
| **dio** | Client HTTP (Flutter) |
| **json_serializable** | Generazione del codice JSON |
| **congelato** | Classi di dati immutabili |
| **pod del fiume** | Gestione statale |
| **blocco / cubito** | Gestione statale |
| **prendilo** | Inserimento delle dipendenze |
| **go_router** | Routing dichiarativo |
| **equiparabile** | Uguaglianza di valore |
| **uuid** | Generazione UUID |
| **cripto** | Crittografia |
| **percorso** | Manipolazione del percorso del file |
| **collezione** | Tipi di raccolta extra |
| **intl** | Internazionalizzazione |
---

## Gestione dello stato (Flutter)
| Soluzione | Digitare |
|----------|------|
| **Riverpod** | Compilabile e testabile |
| **Blocco / Cubito** | Guidato dagli eventi, prevedibile |
| **Fornitore** | Integrato, semplice |
| **GetX** | Tutto in uno (controverso) |
| **Segnali** | Primitive reattive |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **Codice VS + Dardo** | Miglior supporto Dart/Flutter |
| **Android Studio + Flutter** | IDE Flutter completo |
| **IntelliJ+Dart** | Supporto JetBrains |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Compilazione di freccette** | Eseguibili nativi |
| **Dart compila js** | Compila in JavaScript |
| **Dart compile wasm** | Compila in WebAssembly |
| **Creazione svolazzante** | App mobili/desktop |
| **Docker** | App server in contenitori |
| **Google Cloud Run** | Contenitori senza server |
| **Hosting Firebase** | Hosting di app Web |
---

## Riepilogo
L'ecosistema di Dart è dominato da **Flutter** per lo sviluppo dell'interfaccia utente multipiattaforma. Per Dart lato server, **Shelf** è il framework HTTP standard, con **Dart Frog** come opzione full-stack. Lo stack standard è: **Dart 3.4+** come runtime, **pub.dev** per i pacchetti, **Flutter** per l'interfaccia utente mobile/web/desktop, **Riverpod** o **Bloc** per la gestione dello stato, **Drift** per i database, **test** per i test e **dart analyze** per l'linting. I punti di forza di Dart sono la sicurezza nulla, la compilazione rapida, il ricaricamento a caldo (Flutter) e la capacità di compilare in formato nativo, JavaScript o WebAssembly. L'ecosistema è ideale per applicazioni mobili, Web e desktop multipiattaforma.