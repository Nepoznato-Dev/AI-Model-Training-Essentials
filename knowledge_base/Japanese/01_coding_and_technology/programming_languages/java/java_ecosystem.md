<!--
---
# Metadata
title: "Java — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Java ecosystem including build tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [java, ecosystem, tooling, maven, gradle, spring, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Java — エコシステムとツールのガイド
このガイドでは、Java エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## ビルドツール
|ツール |タイプ |最適な用途 |
|------|------|----------|
| **メイブン** | XML ベース |エンタープライズ、設定よりも規約 |
| **グラドル** | Groovy/Kotlin DSL |柔軟、Android、大規模プロジェクト |
| **アリ** | XML ベース |レガシープロジェクト |
| **バゼル** |多言語 |モノリポジトリ、Google スケール |
```bash
# Maven
mvn clean install               # build
mvn test                        # run tests
mvn package                     # create JAR/WAR

# Gradle
./gradlew build                 # build
./gradlew test                  # run tests
./gradlew bootRun               # run Spring Boot app
```

---

## フレームワーク
### Web / エンタープライズ
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **スプリングブーツ** |フルスタック |エンタープライズ、マイクロサービス |
| **クォーカス** |クラウドネイティブ | GraalVM、高速起動 |
| **マイクロノート** | AOT コンパイル済み |低メモリ、サーバーレス |
| **ジャカルタEE** |標準 |エンタープライズ Java 標準 |
| **Vert.x** |リアクティブ |高い同時実行性 |
| **ジャバリン** |軽量 |シンプルなウェブアプリ |
### 主要な春のエコシステム
|モジュール |目的 |
|--------|--------|
| **春のウェブ** | REST API、MVC |
| **春のデータ** |データベースアクセス (JPA、MongoDB、Redis) |
| **Spring セキュリティ** |認証・認可 |
| **春の雲** |マイクロサービス (構成、検出、ゲートウェイ) |
| **春のバッチ** |バッチ処理 |
| **春の AMQP** |メッセージキュー |
---

## テスト
|フレームワーク |目的 |
|----------|----------|
| **JUnit 5** |標準テストフレームワーク |
| **モキト** |嘲笑 |
| **アサートJ** |流暢な主張 |
| **テストコンテナ** | Docker ベースの統合テスト |
| **ワイヤーモック** | HTTP API モック |
| **ArchUnit** |アーキテクチャテスト |
| **休息保証** | REST API テスト |
| **JMH** |マイクロベンチマーク |
```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    @Mock UserRepository repo;
    @InjectMocks UserService service;

    @Test
    void shouldFindUserById() {
        when(repo.findById(1L)).thenReturn(Optional.of(new User("Alice")));
        var user = service.findById(1L);
        assertThat(user.name()).isEqualTo("Alice");
    }
}
```

---

## データベース
|テクノロジー |タイプ |
|-----------|------|
| **JDBC** |低レベル SQL アクセス |
| **JPA / 休止状態** | ORM標準 |
| **jOOQ** |タイプセーフな SQL ビルダー |
| **フライウェイ** |データベースの移行 |
| **リキベース** |データベースの移行 |
| **ヒカリCP** |接続プール |
---

## コードの品質
|ツール |目的 |
|-----|----------|
| **チェックスタイル** |コーディング標準の施行 |
| **スポットバグ** |バグパターンの検出 |
| **PMD** |静的解析 |
| **エラーが発生しやすい** | Google のコンパイラ プラグイン |
| **ソナークベ** |コード品質プラットフォーム |
| **ジャココ** |コードカバレッジ |
| **きれいな** |コードのフォーマット |
| **Google Java 形式** | Google のスタイル |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **IntelliJ IDEA** |主要な Java IDE (コミュニティ + 究極) |
| **日食** |オープンソース、プラグインエコシステム |
| **VS コード** | Java 拡張機能を使用した軽量 |
| **NetBeans** | Apache で保守される |
---

## デプロイメント
|方法 |ツール |
|------|------|
| **JAR** | `java -jar app.jar`|
| **戦争** | Tomcat、桟橋に展開 |
| **GraalVM** |ネイティブイメージのコンパイル |
| **ドッカー** |コンテナ化 (Eclipse Temurin、Amazon Corretto) |
| **Kubernetes** |オーケストレーション |
| **アプリサーバー** |ワイルドフライ、トムキャット、桟橋 |
---

## JDK ディストリビューション
|配布 |プロバイダー |
|---------------|----------|
| **テムリン** | Eclipse/Adoptium (推奨) |
| **コレット** |アマゾン |
| **ズールー語** |アズール |
| **GraalVM** | Oracle (ネイティブ イメージ、多言語) |
| **リベリカ** |ベルソフト |
---

＃＃ まとめ
Java のエコシステムは、エンタープライズ コンピューティングの分野で最も成熟しています。標準スタックは、ビルドには **Gradle** または **Maven**、Web/マイクロサービスには **Spring Boot**、テストには **JUnit 5 + Mockito**、ORM には **Hibernate**、IDE として **IntelliJ IDEA**、デプロイメントには **Docker** です。 Java の強みは、大規模なエコシステム、エンタープライズ サポート、および下位互換性です。レコード、シールされたクラス、パターン マッチング、仮想スレッドを備えた最新の Java (17 以降) が言語を活性化しています。