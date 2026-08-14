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
# Dart: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema de Dart.
---

## Cadena de herramientas
| Herramienta | Propósito |
|------|---------|
| **dardo** | Dart SDK (compilador, formateador, analizador) |
| **aleteo** | SDK de Flutter (incluye Dart) |
| **pub** | Administrador de paquetes (integrado en dart) |
| **análisis de dardos** | Análisis estático |
| **formato de dardo** | Formato de código |
| **compilación de dardos** | Compilar en nativo/JS/WASM |
| **carrera de dardos** | Ejecutar scripts de Dart |
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

## Gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **pub.dev** | Repositorio oficial de paquetes |
| **pub de dardos** | CLI del administrador de paquetes |
| **pubspec.yaml** | Manifiesto del paquete |
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

## Flutter (marco de interfaz de usuario de Dart)
| Tecnología | Propósito |
|------------|---------|
| **Aleteo** | Marco de interfaz de usuario multiplataforma |
| **Telaraña agitada** | Aplicaciones web con Flutter |
| **Escritorio Flutter** | Windows, macOS, Linux |
| **Móvil Flutter** | iOS y Android |
| **Aleteo integrado** | Dispositivos integrados |
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

## Marcos web (Dart del lado del servidor)
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Estante** | Basado en middleware | Servidor HTTP (el más popular) |
| **Rana dardo** | Pila completa | Marco de backend (como Laravel) |
| **Ángel** | API REST | API simples |
| **Alfred** | Como expreso | Servidor estilo Node.js |
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

## Base de datos
| Tecnología | Tipo |
|------------|------|
| **Deriva** | SQL con seguridad de tipos (reemplaza a Moor) |
| **Cuadro de objetos** | Base de datos móvil NoSQL |
| **Isar** | Base de datos móvil rápida |
| **Colmena** | Valor-clave ligero |
| **postgres** | Cliente PostgreSQL |
| **mysql1** | Cliente MySQL |
| **base del sofá** | Cliente Couchbase |
| **Supabase** | Backend como servicio |
| **Base de fuego** | BaaS de Google |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **prueba** | Marco de prueba incorporado |
| **burla** | Burlarse |
| **cóctel sin alcohol** | Burla nula segura |
| **prueba_flutter** | Prueba de widgets de aleteo |
| **prueba_integración** | Pruebas de un extremo a otro |
| **kit_de_herramientas_dorado** | Prueba dorada/instantánea |
| **patrulla** | Pruebas de integración de Flutter |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **análisis de dardos** | Análisis estático incorporado |
| **formato de dardo** | Formateador incorporado |
| **pelusas** | Reglas oficiales de pelusa |
| **flutter_lints** | Pelusas específicas de aleteo |
| **muy_buen_análisis** | Normas estrictas sobre pelusa |
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

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **dardo:núcleo** | Biblioteca estándar |
| **dardo:async** | Futuros, Streams, asíncronos |
| **dardo:io** | Archivo, HTTP, TCP |
| **dardo:convertir** | JSON, UTF-8 |
| **http** | Cliente HTTP |
| **dio** | Cliente HTTP (Flutter) |
| **json_serializable** | Generación de código JSON |
| **congelado** | Clases de datos inmutables |
| **vaina de río** | Gestión estatal |
| **bloque / codo** | Gestión estatal |
| **consíguelo** | Inyección de dependencia |
| **go_router** | Enrutamiento declarativo |
| **igualar** | Igualdad de valores |
| **uuido** | Generación de UUID |
| **cripto** | Criptografía |
| **ruta** | Manipulación de ruta de archivo |
| **colección** | Tipos de colección extra |
| **intl** | Internacionalización |
---

## Gestión del Estado (Flutter)
| Solución | Tipo |
|----------|------|
| **Río** | Compilable y comprobable |
| **Bloque / Codo** | Impulsado por eventos, predecible |
| **Proveedor** | Integrado, sencillo |
| **ObtenerX** | Todo en uno (polémico) |
| **Señales** | Primitivas reactivas |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Código VS + Dardo** | Mejor soporte para Dart/Flutter |
| **Android Estudio + Flutter** | IDE de aleteo completo |
| **IntelliJ + Dardo** | Soporte de JetBrains |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Compilación de dardos** | Ejecutables nativos |
| **Dardo compila js** | Compilar en JavaScript |
| **La compilación de dardos fue increíble** | Compilar en WebAssembly |
| **Construcción de aleteo** | Aplicaciones móviles/de escritorio |
| **Acoplador** | Aplicaciones de servidor en contenedores |
| **Ejecución de Google Cloud** | Contenedores sin servidor |
| **Hospedaje Firebase** | Alojamiento de aplicaciones web |
---

## Resumen
El ecosistema de Dart está dominado por **Flutter** para el desarrollo de UI multiplataforma. Para Dart del lado del servidor, **Shelf** es el marco HTTP estándar, con **Dart Frog** como opción de pila completa. La pila estándar es: **Dart 3.4+** como tiempo de ejecución, **pub.dev** para paquetes, **Flutter** para interfaz de usuario móvil/web/escritorio, **Riverpod** o **Bloc** para administración de estado, **Drift** para bases de datos, **test** para pruebas y **dart analyse** para linting. Los puntos fuertes de Dart son la sólida seguridad nula, la compilación rápida, la recarga en caliente (Flutter) y la capacidad de compilar en JavaScript nativo o WebAssembly. El ecosistema es ideal para aplicaciones móviles, web y de escritorio multiplataforma.