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

# 다트 — 생태계 및 툴링 가이드
이 가이드는 Dart 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 툴체인
| 도구 | 목적 |
|------|---------|
| **다트** | Dart SDK(컴파일러, 포맷터, 분석기) |
| **설레임** | Flutter SDK(Dart 포함) |
| **펍** | 패키지 관리자(dart에 내장) |
| **다트 분석** | 정적 분석 |
| **다트 형식** | 코드 서식 |
| **다트 컴파일** | 기본/JS/WASM으로 컴파일 |
| **다트 런** | Dart 스크립트 실행 |
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

## 패키지 관리
| 도구 | 목적 |
|------|---------|
| **pub.dev** | 공식 패키지 저장소 |
| **다트 펍** | 패키지 관리자 CLI |
| **pubspec.yaml** | 패키지 매니페스트 |
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

## Flutter(Dart UI 프레임워크)
| 기술 | 목적 |
|------------|---------|
| **플러터** | 크로스 플랫폼 UI 프레임워크 |
| **플러터 웹** | Flutter를 사용한 웹 앱 |
| **Flutter 데스크톱** | 윈도우, macOS, 리눅스 |
| **Flutter 모바일** | iOS와 안드로이드 |
| **Flutter 임베디드** | 임베디드 장치 |
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

## 웹 프레임워크(서버측 Dart)
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **선반** | 미들웨어 기반 | HTTP 서버(가장 인기 있음) |
| **다트 개구리** | 풀스택 | 백엔드 프레임워크(예: Laravel) |
| **천사** | REST API | 간단한 API |
| **알프레드** | 익스프레스형 | Node.js 스타일 서버 |
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

## 데이터베이스
| 기술 | 유형 |
|------------|------|
| **드리프트** | 유형이 안전한 SQL(Moor 대체) |
| **오브젝트박스** | NoSQL 모바일 데이터베이스 |
| **이자르** | 빠른 모바일 데이터베이스 |
| **하이브** | 경량 키-값 |
| **포스트그레스** | PostgreSQL 클라이언트 |
| **mysql1** | MySQL 클라이언트 |
| **카우치베이스** | Couchbase 클라이언트 |
| **수파베이스** | 서비스형 백엔드 |
| **Firebase** | 구글 BaaS |
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

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **테스트** | 내장된 테스트 프레임워크 |
| **모키토** | 조롱 |
| **목테일** | Null 안전 조롱 |
| **flutter_test** | Flutter 위젯 테스트 |
| **통합_테스트** | 엔드 투 엔드 테스트 |
| **golden_toolkit** | 골든/스냅샷 테스트 |
| **순찰** | Flutter 통합 테스트 |
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

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **다트 분석** | 내장된 정적 분석 |
| **다트 형식** | 내장 포맷터 |
| **린트** | 공식 린트 규칙 |
| **flutter_lints** | Flutter 관련 린트 |
| **아주_좋은_분석** | 엄격한 린트 규칙 |
| **취재** | 코드 적용 범위 |
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

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **다트:코어** | 표준 라이브러리 |
| **다트:비동기** | 선물, 스트림, 비동기 |
| **다트:io** | 파일, HTTP, TCP |
| **다트:변환** | JSON, UTF-8 |
| **http** | HTTP 클라이언트 |
| **디오** | HTTP 클라이언트(Flutter) |
| **json_직렬화 가능** | JSON 코드 생성 |
| **동결** | 불변 데이터 클래스 |
| **강 포드** | 상태 관리 |
| **블록/큐빗** | 상태 관리 |
| **get_it** | 의존성 주입 |
| **go_router** | 선언적 라우팅 |
| **균등** | 가치평등 |
| **유UID** | UUID 생성 |
| **암호화폐** | 암호화 |
| **경로** | 파일 경로 조작 |
| **컬렉션** | 추가 컬렉션 유형 |
| **국제** | 국제화 |
---

## 상태 관리(Flutter)
| 솔루션 | 유형 |
|------------|------|
| **리버포드** | 컴파일 안전, 테스트 가능 |
| **블록/큐빗** | 이벤트 중심, 예측 가능 |
| **공급자** | 내장형, 단순 |
| **GetX** | 올인원(논란의 여지) |
| **신호** | 반응성 프리미티브 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + 다트** | 최고의 Dart/Flutter 지원 |
| **안드로이드 스튜디오 + Flutter** | 전체 Flutter IDE |
| **IntelliJ + Dart** | JetBrains 지원 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **다트 컴파일** | 네이티브 실행 파일 |
| **Dart 컴파일 js** | JavaScript로 컴파일 |
| **다트 컴파일 wasm** | WebAssembly로 컴파일 |
| **Flutter 빌드** | 모바일/데스크톱 앱 |
| **도커** | 컨테이너화된 서버 앱 |
| **구글 클라우드 런** | 서버리스 컨테이너 |
| **Firebase 호스팅** | 웹 앱 호스팅 |
---

## 요약
Dart의 생태계는 크로스 플랫폼 UI 개발을 위한 **Flutter**가 지배합니다. 서버 측 Dart의 경우 **Shelf**는 표준 HTTP 프레임워크이며 **Dart Frog**는 전체 스택 옵션입니다. 표준 스택은 런타임용 **Dart 3.4+**, 패키지용 **pub.dev**, 모바일/웹/데스크톱 UI용 **Flutter**, 상태 관리용 **Riverpod** 또는 **Bloc**, 데이터베이스용 **Drift**, 테스트용 **test**, Linting용 **dart analyze**입니다. Dart의 강점은 확실한 Null 안전성, 빠른 컴파일, 핫 리로드(Flutter) 및 네이티브, JavaScript 또는 WebAssembly로 컴파일하는 기능입니다. 생태계는 크로스 플랫폼 모바일, 웹 및 데스크톱 애플리케이션에 이상적입니다.