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
# Dart — エコシステムとツールのガイド
このガイドでは、Dart エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## ツールチェーン
|ツール |目的 |
|-----|----------|
| **ダーツ** | Dart SDK (コンパイラ、フォーマッタ、アナライザ) |
| **フラッター** | Flutter SDK (Dart を含む) |
| **パブ** |パッケージマネージャー (dart に組み込まれています) |
| **ダーツ分析** |静的解析 |
| **ダーツ形式** |コードのフォーマット |
| **ダーツコンパイル** |ネイティブ/JS/WASM にコンパイル |
| **ダーツラン** | Dart スクリプトを実行する |
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

## パッケージ管理
|ツール |目的 |
|-----|----------|
| **pub.dev** |公式パッケージリポジトリ |
| **ダーツパブ** |パッケージマネージャー CLI |
| **pubspec.yaml** |パッケージマニフェスト |
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

## Flutter (Dart UI フレームワーク)
|テクノロジー |目的 |
|-----------|-----------|
| **フラッター** |クロスプラットフォーム UI フレームワーク |
| **フラッターウェブ** | Flutter を使用した Web アプリ |
| **フラッター デスクトップ** | Windows、macOS、Linux |
| **フラッターモバイル** | iOS と Android |
| **フラッター埋め込み** |組み込みデバイス |
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

## Web フレームワーク (サーバーサイド Dart)
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **棚** |ミドルウェアベース | HTTP サーバー (最も一般的) |
| **ヤドクガエル** |フルスタック |バックエンド フレームワーク (Laravel など) |
| **天使** | REST API |シンプルな API |
| **アルフレッド** |特急っぽい | Node.js スタイルのサーバー |
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

## データベース
|テクノロジー |タイプ |
|-----------|------|
| **ドリフト** |タイプセーフ SQL (Moor を置き換え) |
| **オブジェクトボックス** | NoSQL モバイル データベース |
| **イザール** |高速モバイルデータベース |
| **ハイブ** |軽量のキーと値 |
| **ポストグレ** | PostgreSQL クライアント |
| **mysql1** | MySQL クライアント |
| **ソファベース** |カウチベースクライアント |
| **スーパーベース** |サービスとしてのバックエンド |
| **ファイアベース** | Google BaaS |
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

## テスト
|フレームワーク |目的 |
|----------|----------|
| **テスト** |組み込みのテスト フレームワーク |
| **モキト** |嘲笑 |
| **モクテル** | Null セーフ モック |
| **flutter_test** | Flutter ウィジェットのテスト |
| **統合テスト** |エンドツーエンドのテスト |
| **ゴールデン ツールキット** |ゴールデン/スナップショット テスト |
| **パトロール** | Flutter 統合テスト |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **ダーツ分析** |組み込みの静的分析 |
| **ダーツ形式** |内蔵フォーマッタ |
| **糸くず** |公式の lint ルール |
| **flutter_lints** | Flutter 固有のリント |
| **非常に良い分析** |厳密な lint ルール |
| **取材範囲** |コードカバレッジ |
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

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **ダーツ:コア** |標準ライブラリ |
| **ダーツ:非同期** |先物、ストリーム、非同期 |
| **ダーツ:io** |ファイル、HTTP、TCP |
| **ダーツ:変換** | JSON、UTF-8 |
| **http** | HTTPクライアント |
| **ディオ** | HTTP クライアント (Flutter) |
| **json_serializable** | JSONコード生成 |
| **凍結** |不変のデータ クラス |
| **リバーポッド** |状態管理 |
| **ブロック / キュビット** |状態管理 |
| **get_it** |依存関係の注入 |
| **go_router** |宣言型ルーティング |
| **同等** |値の等しい |
| **uuid** | UUIDの生成 |
| **暗号** |暗号化 |
| **パス** |ファイルパスの操作 |
| **コレクション** |追加のコレクション タイプ |
| **国際** |国際化 |
---

## 状態管理 (フラッター)
|ソリューション |タイプ |
|----------|------|
| **リバーポッド** |コンパイルセーフ、テスト可能 |
| **ブロック / キュービット** |イベント駆動型、予測可能 |
| **プロバイダー** |内蔵、シンプル |
| **GetX** |オールインワン (物議を醸す) |
| **信号** |リアクティブプリミティブ |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + ダーツ** |最高の Dart/Flutter サポート |
| **Android Studio + Flutter** |完全な Flutter IDE |
| **IntelliJ + Dart** | JetBrains サポート |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **Dart コンパイル** |ネイティブ実行可能ファイル |
| **Dart コンパイル js** | JavaScript にコンパイルする |
| **Dart コンパイル wasm** | WebAssembly にコンパイル |
| **フラッター ビルド** |モバイル/デスクトップ アプリ |
| **ドッカー** |コンテナ化されたサーバー アプリ |
| **Google Cloud Run** |サーバーレスコンテナ |
| **Firebase ホスティング** | Web アプリのホスティング |
---

＃＃ まとめ
Dart のエコシステムは、クロスプラットフォーム UI 開発用の **Flutter** によって支配されています。サーバーサイド Dart の場合、**Shelf** が標準の HTTP フレームワークであり、フルスタック オプションとして **Dart Frog** が使用されます。標準スタックは、ランタイムとして **Dart 3.4+**、パッケージに対して **pub.dev**、モバイル/ウェブ/デスクトップ UI に対して **Flutter**、状態管理に対して **Riverpod** または **Bloc**、データベースに対して **Drift**、テストに対して **test**、リンティングに対して **dart Analyzer** です。 Dart の強みは、健全な null 安全性、高速コンパイル、ホット リロード (Flutter)、およびネイティブ、JavaScript、または WebAssembly にコンパイルできる機能です。このエコシステムは、クロスプラットフォームのモバイル、Web、デスクトップ アプリケーションに最適です。