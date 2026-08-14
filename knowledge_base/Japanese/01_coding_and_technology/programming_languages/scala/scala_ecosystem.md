<!--
---
# Metadata
title: "Scala — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Scala ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [scala, ecosystem, tooling, sbt, spark, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Scala — エコシステムとツールのガイド
このガイドでは、Scala エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## Scala のバージョンとランタイム
|バージョン |メモ |
|----------|----------|
| **スカラ 3** |現在のクリーンな構文、新機能 |
| **Scala 2.13** |広く使用され、成熟した |
| **Scala.js** | JavaScript にコンパイルする |
| **Scala ネイティブ** |ネイティブ コードにコンパイルする |
| **JVM** |プライマリ ランタイム (Java 相互運用) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## ビルドツール
|ツール |タイプ |最適な用途 |
|------|------|----------|
| **sbt** |標準 |ほとんどの Scala プロジェクト |
| **工場** |モダン |高速かつシンプルな構成 |
| **グラドル** | Java 相互運用性 | Java/Scala 混合 |
| **スカラクリ** |軽量 |スクリプト、小規模プロジェクト |
```scala
// build.sbt
lazy val root = (project in file("."))
  .settings(
    name := "myapp",
    version := "0.1.0",
    scalaVersion := "3.4.0",
    libraryDependencies ++= Seq(
      "org.http4s" %% "http4s-dsl" % "0.23.25",
      "org.http4s" %% "http4s-ember-server" % "0.23.25",
      "org.typelevel" %% "cats-effect" % "3.5.4",
      "org.scalameta" %% "munit" % "1.0.0" % Test
    )
  )
```

```bash
sbt compile               # compile
sbt test                  # run tests
sbt run                   # run application
sbt package               # create JAR
sbt assembly              # fat JAR (sbt-assembly)
```

---

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **http4s** |機能性 |タイプセーフな HTTP (cats 効果) |
| **ペッコ HTTP** |アクターベース | Apache Pekko (Akka フォーク) |
| **Play フレームワーク** |フルスタック |リアクティブ Web アプリ |
| **ZIO HTTP** | ZIOベース |機能的、高性能 |
| **フィナトラ** |ツイッター |マイクロサービス |
| **バク** |エンドポイント DSL |タイプセーフな API の説明 |
```scala
// http4s + cats-effect example
import cats.effect.*
import org.http4s.*
import org.http4s.dsl.io.*
import org.http4s.ember.server.*

object HelloWorld extends IOApp.Simple {
  val routes = HttpRoutes.of[IO] {
    case GET -> Root / "hello" => Ok("Hello, World!")
    case GET -> Root / "users" / IntVar(id) =>
      UserService.find(id).flatMap {
        case Some(user) => Ok(user.asJson)
        case None       => NotFound()
      }
  }.orNotFound

  def run = EmberServerBuilder
    .default[IO]
    .withHost(ipv4"0.0.0.0")
    .withPort(port"8080")
    .withHttpApp(routes)
    .build
    .useForever
}
```

---

## ビッグデータとデータエンジニアリング
|テクノロジー |目的 |
|-----------|-----------|
| **Apache Spark** |分散データ処理 (Scala ネイティブ) |
| **Apache Kafka** |イベントストリーミング (Scala クライアント) |
| **Apache フリンク** |ストリーム処理 |
| **Apache Pekko ストリーム** |リアクティブストリーム |
| **アッカ ストリーム** |リアクティブストリーム (レガシー) |
| **サイオ** | Google Cloud データフロー (Spotify) |
| **バルカン** | Avro スキーマの進化 |
---

## データベースと ORM
|テクノロジー |タイプ |
|-----------|------|
| **ドゥービー** |関数型 JDBC (猫効果) |
| **滑らか** |関数リレーショナル |
| **クイル** |コンパイル時の引用符付きクエリ |
| **アノーム** |シンプルな SQL アクセス (Play) |
| **スカンク** | PostgreSQL (猫効果、NIO) |
| **キャリバン** |グラフQL |
| **サングリア** |グラフQL |
```scala
// Doobie example
import doobie.*
import doobie.implicits.*

def findUser(id: Long): ConnectionIO[Option[User]] =
  sql"SELECT id, name, email FROM users WHERE id = $id"
    .query[User]
    .option
```

---

## テスト
|フレームワーク |目的 |
|----------|----------|
| **MUnit** |シンプル、モダン（おすすめ） |
| **ScalaTest** |豊富な機能、多くのスタイル |
| **ウィーバー** |機能的、不変 |
| **munit-cats 効果** |猫効果試験 |
| **mockito-scala** |嘲笑 |
| **スカラチェック** |プロパティベースのテスト |
| **testcontainers-scala** | Docker ベースの統合 |
```scala
// MUnit example
class UserServiceSuite extends munit.FunSuite {
  test("find user by id") {
    val repo = new InMemoryUserRepo
    repo.insert(User(1, "Alice"))
    val service = new UserService(repo)

    val result = service.find(1).unsafeRunSync()

    assertEquals(result.map(_.name), Some("Alice"))
  }
}
```

---

## コードの品質
|ツール |目的 |
|-----|----------|
| **スカラフムト** |コードのフォーマット |
| **スカラフィックス** |リンティングとリファクタリング |
| **いぼ除去剤** |コンパイル時リンター |
| **スケープゴート** |静的解析 |
| **sbt-tpolecat** |厳密なコンパイラ オプション |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## 関数型プログラミング ライブラリ
|図書館 |目的 |
|----------|----------|
| **猫** |関数の抽象化 (型クラス) |
| **キャッツ効果** | IO モナド、非同期ランタイム |
| **ジオ** |エフェクトシステム、完全なエコシステム |
| **形のない** |汎用プログラミング (Scala 2) |
| **子猫** |派生型クラスのインスタンス |
| **モノクル** |光学ライブラリ |
---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **キルケ** | JSON ライブラリ (猫) |
| **ユーピクル** | JSON シリアル化 |
| **ZIO JSON** |高速 JSON (ZIO) |
| **fs2** |機能ストリーム |
| **バク** |タイプセーフな API エンドポイント |
| **キャリバン** | GraphQLサーバー |
| **ログ4キャッツ** |機能ログ |
| **拒否** | CLI 引数の解析 |
| **スクォント** |タイプセーフな量 |
| **列挙** |強化された列挙型 |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **IntelliJ IDEA + Scala プラグイン** |最高の Scala IDE |
| **金属** |言語サーバー (マルチエディター) |
| **VS コード + メタル** | LSP による軽量化 |
| **ネオビム + 金属** |ターミナルベース |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **ファット JAR** | `sbt assembly`|
| **ドッカー** |マルチステージビルド |
| **GraalVM ネイティブ** |ネイティブ画像（限定） |
| **Kubernetes** |オーケストレーション |
| **AWS EMR** | AWS 上の Spark |
| **データブリック** |スパークプラットフォーム |
---

＃＃ まとめ
Scala のエコシステムは、エンタープライズ、関数型プログラミング、ビッグデータに及びます。標準スタックは次のとおりです。ビルドには **sbt**、言語には **Scala 3**、機能 Web サービスには **http4s +cats-effect** または **ZIO**、データベース アクセスには **Doobie** または **Slick**、テストには **MUnit**、フォーマットには **scalafmt**、IDE サポートには **IntelliJ + Metals** です。 Scala は、ビッグ データ (Apache Spark は Scala で書かれています)、ストリーミング (Pekko Streams)、および JVM パフォーマンスが関数型プログラミングと出会うあらゆる分野で優位に立っています。 Scala 3 のよりクリーンな構文、列挙型、交差型により、この言語はより親しみやすくなりました。