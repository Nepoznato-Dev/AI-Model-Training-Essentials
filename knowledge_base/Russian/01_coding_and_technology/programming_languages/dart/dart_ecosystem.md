---
# Metadata
title: "Dart — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Dart ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Dart — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы Dart.
---

## Инструментальная цепочка
| Инструмент | Цель |
|------|---------|
| **дротик** | Dart SDK (компилятор, форматтер, анализатор) |
| **трепетание** | Flutter SDK (включая Dart) |
| **паб** | Менеджер пакетов (встроен в dart) |
| **дарт-анализ** | Статический анализ |
| **формат дартса** | Форматирование кода |
| **компиляция дартс** | Скомпилировать в родной/JS/WASM |
| **дартс** | Запуск скриптов Dart |
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

## Управление пакетами
| Инструмент | Цель |
|------|---------|
| **pub.dev** | Официальный репозиторий пакетов |
| **дартс-паб** | Менеджер пакетов CLI |
| **pubspec.yaml** | Манифест пакета |
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
| Технология | Цель |
|------------|---------|
| **Трехат** | Межплатформенная среда пользовательского интерфейса |
| **Сеть Flutter** | Веб-приложения с Flutter |
| **Рабочий стол Flutter** | Windows, macOS, Linux |
| **Флаттер Мобайл** | iOS и Android |
| **Встроенный флаттер** | Встроенные устройства |
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

## Веб-фреймворки (серверный Dart)
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **Полка** | На основе промежуточного программного обеспечения | HTTP-сервер (самый популярный) |
| **Лягушка-дротик** | Полный стек | Бэкэнд-фреймворк (например, Laravel) |
| **Ангел** | ОТДЫХ API | Простые API |
| **Альфред** | Экспресс-подобный | Сервер в стиле Node.js |
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

## База данных
| Технология | Тип |
|------------|------|
| **Дрифт** | Типобезопасный SQL (заменяет Moor) |
| **Объектный ящик** | Мобильная база данных NoSQL |
| **Изар** | Быстрая мобильная база данных |
| **Улей** | Упрощенный ключ-значение |
| **постгрес** | Клиент PostgreSQL |
| **mysql1** | Клиент MySQL |
| **диван** | Клиент Couchbase |
| **Супабаза** | Серверная часть как услуга |
| **Огневая база** | Google BaaS |
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

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **тест** | Встроенная среда тестирования |
| **мокито** | Издевательство |
| **моктейль** | Null-безопасное издевательство |
| **flutter_test** | Тестирование виджетов Flutter |
| **интеграционный_тест** | Сквозное тестирование |
| **золотой_инструментарий** | Золотое/моментальное тестирование |
| **патруль** | Интеграционное тестирование Flutter |
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

## Качество кода
| Инструмент | Цель |
|------|---------|
| **дарт-анализ** | Встроенный статический анализ |
| **формат дартса** | Встроенный форматтер |
| **линты** | Официальные правила ворса |
| **flutter_lints** | Ворсы, специфичные для Flutter |
| **очень_хороший_анализ** | Строгие правила ворса |
| **охват** | Покрытие кода |
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

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **дротик:ядро** | Стандартная библиотека |
| **дротик:асинхронный** | Фьючерсы, потоки, асинхронность |
| **дарт:io** | Файл, HTTP, TCP |
| **дротик:конвертировать** | JSON, UTF-8 |
| **http** | HTTP-клиент |
| **дио** | HTTP-клиент (Flutter) |
| **json_serializable** | Генерация кода JSON |
| **замороженный** | Неизменяемые классы данных |
| **речная капсула** | Государственное управление |
| **блок/локоть** | Государственное управление |
| **get_it** | Внедрение зависимостей |
| **go_router** | Декларативная маршрутизация |
| **равный** | Равенство ценностей |
| **uuid** | Генерация UUID |
| **крипто** | Криптография |
| **путь** | Манипулирование путем к файлу |
| **коллекция** | Дополнительные типы коллекций |
| **между** | Интернационализация |
---

## Управление состоянием (Flutter)
| Решение | Тип |
|----------|------|
| **Риверпод** | Безопасный для компиляции, тестируемый |
| **Блок / Кубит** | Событийно-ориентированный, предсказуемый |
| **Поставщик** | Встроенный, простой |
| **GetX** | Все-в-одном (спорно) |
| **Сигналы** | Реактивные примитивы |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **VS Code + Дартс** | Лучшая поддержка Dart/Flutter |
| **Android Studio + Flutter** | Полная среда разработки Flutter |
| **IntelliJ + Дарт** | Поддержка JetBrains |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Компиляция Dart** | Собственные исполняемые файлы |
| **Dart-компиляция JS** | Компилировать в JavaScript |
| **Dart компиляция** | Компилировать в WebAssembly |
| **Сборка Flutter** | Мобильные/настольные приложения |
| **Докер** | Контейнерные серверные приложения |
| **Облачный забег Google** | Бессерверные контейнеры |
| **Хостинг Firebase** | Хостинг веб-приложений |
---

## Краткое содержание
В экосистеме Dart доминирует **Flutter** для кроссплатформенной разработки пользовательского интерфейса. Для серверной части Dart **Shelf** — это стандартная HTTP-платформа, а **Dart Frog** – полнофункциональная опция. Стандартный стек: **Dart 3.4+** в качестве среды выполнения, **pub.dev** для пакетов, **Flutter** для мобильного/веб-интерфейса/настольного пользовательского интерфейса, **Riverpod** или **Bloc** для управления состоянием, **Drift** для баз данных, **test** для тестирования и **dart Analysis** для анализа. Сильными сторонами Dart являются надежная нулевая безопасность, быстрая компиляция, горячая перезагрузка (Flutter) и возможность компиляции в нативный код, JavaScript или WebAssembly. Экосистема идеально подходит для кроссплатформенных мобильных, веб- и настольных приложений.