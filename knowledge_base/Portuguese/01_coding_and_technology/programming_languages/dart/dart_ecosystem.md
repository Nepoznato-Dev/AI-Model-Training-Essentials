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
# Dart — Guia de ecossistema e ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema Dart.
---

## Conjunto de ferramentas
| Ferramenta | Finalidade |
|------|---------|
| **dardo** | Dart SDK (compilador, formatador, analisador) |
| **vibração** | Flutter SDK (inclui Dart) |
| **pub** | Gerenciador de pacotes (integrado ao dart) |
| **análise de dardo** | Análise estática |
| **formato dardo** | Formatação de código |
| **compilação do dardo** | Compilar para nativo/JS/WASM |
| **corrida de dardo** | Execute scripts Dart |
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

## Gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **pub.dev** | Repositório oficial de pacotes |
| **pub dardo** | CLI do gerenciador de pacotes |
| **pubspec.yaml** | Manifesto do pacote |
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

## Flutter (estrutura de interface do usuário Dart)
| Tecnologia | Finalidade |
|------------|---------|
| **Vibração** | Estrutura de UI multiplataforma |
| **Web flutuante** | Aplicativos da Web com Flutter |
| **Área de trabalho vibrante** | Windows, macOS, Linux |
| **Flutter Móvel** | iOS e Android |
| **Flutter incorporado** | Dispositivos incorporados |
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

## Web Frameworks (Dart do lado do servidor)
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **Prateleira** | Baseado em middleware | Servidor HTTP (mais popular) |
| **Sapo Dardo** | Pilha completa | Estrutura de back-end (como Laravel) |
| **Anjo** | API REST | APIs simples |
| **Alfredo** | Expresso | Servidor estilo Node.js |
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

## Banco de dados
| Tecnologia | Tipo |
|------------|------|
| **Deriva** | SQL com segurança de tipo (substitui Moor) |
| **Caixa de Objetos** | Banco de dados móvel NoSQL |
| **Isar** | Banco de dados móvel rápido |
| **Colmeia** | Valor-chave leve |
| **postgres** | Cliente PostgreSQL |
| **mysql1** | Cliente MySQL |
| **base do sofá** | Cliente Couchbase |
| **Supabase** | Back-end como serviço |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **teste** | Estrutura de teste integrada |
| **mockito** | Zombando |
| **mocktail** | Zombaria com segurança nula |
| **flutter_test** | Teste de widget Flutter |
| **teste_integração** | Testes ponta a ponta |
| **golden_toolkit** | Teste de ouro/instantâneo |
| **patrulha** | Teste de integração Flutter |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **análise de dardo** | Análise estática integrada |
| **formato dardo** | Formatador integrado |
| **fiapos** | Regras oficiais de fiapos |
| **flutter_lints** | Lints específicos para vibração |
| **análise_muito_boa** | Regras rígidas de fiapos |
| **cobertura** | Cobertura de código |
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

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **dardo:núcleo** | Biblioteca padrão |
| **dardo:assíncrono** | Futuros, Streams, assíncronos |
| **dardo:io** | Arquivo, HTTP, TCP |
| **dardo:converter** | JSON, UTF-8 |
| **http** | Cliente HTTP |
| **dio** | Cliente HTTP (Flutter) |
| **json_serializável** | Geração de código JSON |
| **congelado** | Classes de dados imutáveis ​​|
| **riverpod** | Gestão do Estado |
| **bloco / côvado** | Gestão do Estado |
| **pegue_isso** | Injeção de dependência |
| **go_router** | Roteamento declarativo |
| **igualável** | Igualdade de valores |
| **uuid** | Geração de UUID |
| **criptografado** | Criptografia |
| **caminho** | Manipulação de caminho de arquivo |
| **coleção** | Tipos de coleção extras |
| **intl** | Internacionalização |
---

## Gerenciamento de estado (flutter)
| Solução | Tipo |
|----------|------|
| **Riverpod** | Compilado com segurança, testável |
| **Bloco / Cúbito** | Orientado por eventos, previsível |
| **Provedor** | Integrado, simples |
| **ObterX** | Tudo-em-um (controverso) |
| **Sinais** | Primitivas reativas |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Código VS + Dardo** | Melhor suporte Dart/Flutter |
| **Android Studio + Flutter** | IDE Flutter completo |
| **IntelliJ + Dardo** | Suporte JetBrains |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Compilação do Dart** | Executáveis ​​nativos |
| **Dart compila js** | Compilar para JavaScript |
| **A compilação do Dart foi** | Compilar para WebAssembly |
| **Construção de vibração** | Aplicativos móveis/desktop |
| **Docker** | Aplicativos de servidor em contêineres |
| **Google Cloud Run** | Contêineres sem servidor |
| **Hospedagem Firebase** | Hospedagem de aplicativos web |
---

## Resumo
O ecossistema do Dart é dominado pelo **Flutter** para desenvolvimento de UI multiplataforma. Para o Dart do lado do servidor, **Shelf** é a estrutura HTTP padrão, com **Dart Frog** como uma opção full-stack. A pilha padrão é: **Dart 3.4+** como tempo de execução, **pub.dev** para pacotes, **Flutter** para UI móvel/web/desktop, **Riverpod** ou **Bloc** para gerenciamento de estado, **Drift** para bancos de dados, **test** para testes e **dart analyze** para linting. Os pontos fortes do Dart são segurança nula sólida, compilação rápida, recarga a quente (Flutter) e a capacidade de compilar para nativo, JavaScript ou WebAssembly. O ecossistema é ideal para aplicativos multiplataforma móveis, web e desktop.