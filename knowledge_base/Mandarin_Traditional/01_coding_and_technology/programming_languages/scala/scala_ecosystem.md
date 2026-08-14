---
# Metadata
title: "Scala — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Scala ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Scala — 生態系統與工具指南
本指南涵蓋了 Scala 生態系統中的基本工具、框架和基礎設施。
---

## Scala 版本和運行時
|版本 |筆記|
|--------|--------|
| **Scala 3** |當前、簡潔的語法、新功能 |
| **Scala 2.13** |應用廣泛，成熟|
| **Scala.js** |編譯為 JavaScript |
| **Scala Native** |編譯為本機程式碼 |
| **JVM** |主執行階段（Java 互通）|
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## 建置工具
|工具|類型 |最適合 |
|------|------|----------|
| **sbt** |標準|大多數 Scala 項目 |
| **工廠** |現代|快速、簡單的配置 |
| **搖籃** | Java 互通 |混合 Java/Scala |
| **scala-cli** |輕量化|腳本、小專案 |
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **http4s** |功能性|型別安全 HTTP（貓效應）|
| **Pekko HTTP** |基於演員 | Apache Pekko（Akka 叉）|
| **播放框架** |全端|反應式網路應用程式 |
| **ZIO HTTP** |基於ZIO |功能齊全、高效能|
| **菲納特拉** |推特 |微服務|
| **貘** |端點 DSL |型別安全 API 說明 |
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

## 大數據與數據工程
|技術 |目的|
|------------|---------|
| **阿帕契火花** |分散式資料處理（Scala 原生）|
| **阿帕契卡夫卡** |事件流（Scala 用戶端）|
| **Apache Flink** |流程處理|
| **Apache Pekko 流** |反應流 |
| **Akka 流** |反應式串流（舊版）|
| **科學國際組織** |Google雲端資料流（Spotify）|
| **瓦肯** | Avro 架構演進 |
---

## 資料庫和 ORM
|技術 |類型 |
|------------|------|
| **杜比** |函數式 JDBC（貓效應）|
| **光滑** |函數關係 |
| **鵝毛筆** |編譯時引用查詢 |
| **異常** |簡單的 SQL 存取（播放）|
| **臭鼬** | PostgreSQL（貓效應，NIO）|
| **卡利班** | GraphQL |
| **桑格利亞汽酒** | GraphQL |
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

## 測試
|框架|目的|
|------------|---------|
| **MUnit** |簡約、現代（推薦）|
| **Scala測試** |功能豐富、款式眾多 |
| **織工** |功能性、不可變 |
| **munit 貓效應** |貓效應測驗|
| **mockito-scala** |嘲笑|
| **scalacheck** |基於屬性的測試 |
| **測試容器-scala** |基於 Docker 的整合 |
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

## 程式碼品質
|工具|目的|
|------|---------|
| **scalafmt** |程式碼格式化 |
| **scalafix** |程式碼檢查與重構 |
| **去疣劑** |編譯時 linter |
| **替罪羔羊** |靜態分析|
| **sbt-tpolecat** |嚴格的編譯器選項 |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## 函數式程式設計庫
|圖書館 |目的|
|---------|---------|
| **貓** |功能抽象（類型類別） |
| **貓效應** | IO monad，非同步運行時 |
| **ZIO** |效果系統，全生態系|
| **無形** |通用編程 (Scala 2) |
| **小貓** |衍生型別類別實例 |
| **單片眼鏡** |光學圖書館 |
---

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **瑟茜** | JSON 庫（貓）|
| **泡菜** | JSON 序列化 |
| **ZIO JSON** |快速 JSON (ZIO) |
| **fs2** |功能流 |
| **貘** |型別安全的 API 端點 |
| **卡利班** | GraphQL 伺服器 |
| **Log4cats** |功能日誌|
| **拒絕** | CLI 參數解析 |
| **深蹲** |類型安全數量 |
| **枚舉** |增強的枚舉 |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **IntelliJ IDEA + Scala 插件** |最佳 Scala IDE |
| **金屬** |語言伺服器（多重編輯器）|
| **VS 代碼 + 金屬** |輕量級 LSP |
| **Neovim + 金屬** |基於終端 |
---

## 部署
|方法|筆記|
|--------|--------|
| **胖罐** |`sbt assembly`|
| **碼頭工人** |多階段建造 |
| **GraalVM Native** |原生鏡像（限量）|
| **Kubernetes** |編排|
| **AWS EMR** | AWS 上的 Spark |
| **資料塊** | Spark平台|
---

＃＃ 概括
Scala 的生態系統涵蓋企業、函數式程式設計和大數據。標準堆疊是：用於構建的 **sbt**、用於語言的 **Scala 3**、用於功能性 Web 服務的 **http4s + cats-effect** 或 **ZIO**、用於資料庫訪問的 **Doobie** 或 **Slick**、用於測試的 **MUnit**、用於格式化的 **scalafmt** 以及用於 IDE 支援的 **IntelliJ Metals**。 Scala 在大數據（Apache Spark 是用 Scala 編寫）、串流媒體（Pekko Streams）以及任何 JVM 效能滿足函數式程式設計的領域中佔據主導地位。 Scala 3 更簡潔的語法、枚舉和交集類型使語言更加平易近人。