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
# Dart — Guide de l'écosystème et des outils
Ce guide couvre les outils, frameworks et infrastructures essentiels de l'écosystème Dart.
---

## Chaîne d'outils
| Outil | Objectif |
|------|--------------|
| **fléchette** | Dart SDK (compilateur, formateur, analyseur) |
| **battement** | SDK Flutter (inclut Dart) |
| **pub** | Gestionnaire de packages (intégré à Dart) |
| **analyse de fléchettes** | Analyse statique |
| **format fléchette** | Formatage des codes |
| **compilation de fléchettes** | Compiler en natif/JS/WASM |
| **course de fléchettes** | Exécuter des scripts Dart |
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

## Gestion des paquets
| Outil | Objectif |
|------|--------------|
| **pub.dev** | Dépôt officiel de packages |
| **pub de fléchettes** | CLI du gestionnaire de packages |
| **pubspec.yaml** | Manifeste du package |
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

## Flutter (cadre d'interface utilisateur Dart)
| Technologie | Objectif |
|------------|---------|
| **Flutter** | Cadre d'interface utilisateur multiplateforme |
| **Flutter Web** | Applications Web avec Flutter |
| **Bureau Flutter** | Windows, macOS, Linux |
| **Flutter Mobile** | iOS et Android |
| **Flutter intégré** | Appareils embarqués |
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

## Frameworks Web (Dart côté serveur)
| Cadre | Tapez | Idéal pour |
|---------------|------|--------------|
| **Étagère** | Basé sur un middleware | Serveur HTTP (le plus populaire) |
| **Grenouille de fléchettes** | Pile complète | Framework backend (comme Laravel) |
| **Ange** | API REST | API simples |
| **Alfred** | De type express | Serveur de style Node.js |
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

## Base de données
| Technologie | Tapez |
|------------|------|
| **Dérive** | SQL de type sécurisé (remplace Moor) |
| **BoîteObjet** | Base de données mobile NoSQL |
| **Isar** | Base de données mobile rapide |
| **Ruche** | Valeur-clé légère |
| **postgres** | Client PostgreSQL |
| **mysql1** | Client MySQL |
| **base de canapé** | Client Couchbase |
| **Subase** | Backend en tant que service |
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

## Tests
| Cadre | Objectif |
|-----------|---------|
| **tester** | Cadre de test intégré |
| **simulacre** | Moqueur |
| **cocktail sans alcool** | Moquerie sans danger |
| **flutter_test** | Test du widget Flutter |
| **integration_test** | Tests de bout en bout |
| **golden_toolkit** | Tests Golden/instantanés |
| **patrouille** | Tests d'intégration Flutter |
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

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **analyse de fléchettes** | Analyse statique intégrée |
| **format fléchette** | Formateur intégré |
| **peluches** | Règles officielles des peluches |
| **flutter_lints** | Peluches spécifiques au flottement |
| **very_good_analysis** | Règles strictes en matière de peluches |
| **couverture** | Couverture du code |
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

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **fléchette:core** | Bibliothèque standard |
| **fléchette:asynchrone** | Futures, Streams, asynchrone |
| **fléchette:io** | Fichier, HTTP, TCP |
| **fléchette:convertir** | JSON, UTF-8 |
| **http** | Client HTTP |
| **dio** | Client HTTP (Flutter) |
| **json_serialalisable** | Génération de code JSON |
| **congelé** | Classes de données immuables |
| **rivière** | Gestion de l'État |
| **bloc / coudée** | Gestion de l'État |
| **get_it** | Injection de dépendances |
| **go_router** | Routage déclaratif |
| **équitable** | Égalité des valeurs |
| **uuid** | Génération d'UUID |
| **crypto** | Cryptographie |
| **chemin** | Manipulation du chemin de fichier |
| **collection** | Types de collecte supplémentaires |
| **intl** | Internationalisation |
---

## Gestion de l'état (Flutter)
| Solutions | Tapez |
|--------------|------|
| **Riverpod** | Compilable, testable |
| **Bloc / Coudée** | Orienté événementiel, prévisible |
| **Fournisseur** | Intégré, simple |
| **ObtenirX** | Tout-en-un (controversé) |
| **Signaux** | Primitives réactives |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **Code VS + Fléchette** | Meilleur support Dart/Flutter |
| **Android Studio + Flutter** | IDE Flutter complet |
| **IntelliJ + Dart** | Prise en charge de JetBrains |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Compilation Dart** | Exécutables natifs |
| **Dart compile js** | Compiler en JavaScript |
| **Dart compile wasm** | Compiler vers WebAssembly |
| **Construction Flutter** | Applications mobiles/de bureau |
| **Docker** | Applications serveur conteneurisées |
| **Google Cloud Run** | Conteneurs sans serveur |
| **Hébergement Firebase** | Hébergement d'applications Web |
---

## Résumé
L'écosystème de Dart est dominé par **Flutter** pour le développement d'interface utilisateur multiplateforme. Pour Dart côté serveur, **Shelf** est le framework HTTP standard, avec **Dart Frog** comme option full-stack. La pile standard est : **Dart 3.4+** pour l'exécution, **pub.dev** pour les packages, **Flutter** pour l'interface utilisateur mobile/web/de bureau, **Riverpod** ou **Bloc** pour la gestion de l'état, **Drift** pour les bases de données, **test** pour les tests et **dart analyser** pour le peluchage. Les points forts de Dart sont une sécurité nulle, une compilation rapide, un rechargement à chaud (Flutter) et la possibilité de compiler en natif, JavaScript ou WebAssembly. L'écosystème est idéal pour les applications mobiles, Web et de bureau multiplateformes.