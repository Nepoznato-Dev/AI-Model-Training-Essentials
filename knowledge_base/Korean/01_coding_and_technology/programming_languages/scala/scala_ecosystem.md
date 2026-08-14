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

# Scala — 생태계 및 툴링 가이드
이 가이드에서는 Scala 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 스칼라 버전 및 런타임
| 버전 | 메모 |
|---------|---------|
| **스칼라 3** | 현재의 깔끔한 구문, 새로운 기능 |
| **스칼라 2.13** | 널리 사용되며 성숙함 |
| **스칼라.js** | JavaScript로 컴파일 |
| **스칼라 네이티브** | 네이티브 코드로 컴파일 |
| **JVM** | 기본 런타임(Java 상호 운용성) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## 빌드 도구
| 도구 | 유형 | 최고의 대상 |
|------|------|----------|
| **sbt** | 표준 | 대부분의 Scala 프로젝트 |
| **밀** | 현대 | 빠르고 간단한 구성 |
| **그라들** | 자바 상호운용성 | 혼합 Java/Scala |
| **스칼라-cli** | 경량 | 스크립트, 소규모 프로젝트 |
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

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **http4s** | 기능성 | 유형이 안전한 HTTP(cats-효과) |
| **페코 HTTP** | 배우 기반 | Apache Pekko(Akka 포크) |
| **플레이 프레임워크** | 풀스택 | 반응형 웹 앱 |
| **지오 HTTP** | ZIO 기반 | 기능성, 고성능 |
| **피나트라** | 트위터 | 마이크로서비스 |
| **테이퍼** | 엔드포인트 DSL | 유형이 안전한 API 설명 |
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

## 빅데이터 및 데이터 엔지니어링
| 기술 | 목적 |
|------------|---------|
| **아파치 스파크** | 분산 데이터 처리(Scala 기반) |
| **아파치 카프카** | 이벤트 스트리밍(Scala 클라이언트) |
| **아파치 플링크** | 스트림 처리 |
| **Apache Pekko 스트림** | 반응형 스트림 |
| **아카 스트림** | 반응형 스트림(레거시) |
| **사이오** | Google Cloud Dataflow(Spotify) |
| **발칸** | Avro 스키마 진화 |
---

## 데이터베이스 및 ORM
| 기술 | 유형 |
|------------|------|
| **두비** | 기능적 JDBC(고양이 효과) |
| **매끄러운** | 기능적 관계 |
| **퀼** | 컴파일 시간 인용 쿼리 |
| **비정상** | 단순 SQL 액세스(Play) |
| **스컹크** | PostgreSQL(고양이 효과, NIO) |
| **칼리반** | GraphQL |
| **상그리아** | GraphQL |
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

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **M단위** | 심플하고 모던함(권장) |
| **스칼라테스트** | 기능이 풍부하고 다양한 스타일 |
| **위버** | 기능적, 불변 |
| **munit-cats-효과** | 고양이 효과 테스트 |
| **mockito-scala** | 조롱 |
| **스칼라체크** | 속성 기반 테스트 |
| **테스트컨테이너스-스칼라** | Docker 기반 통합 |
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

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **scalafmt** | 코드 서식 |
| **스칼라픽스** | 린팅 및 리팩토링 |
| **사마귀 제거제** | 컴파일 타임 린터 |
| **희생양** | 정적 분석 |
| **sbt-tpolecat** | 엄격한 컴파일러 옵션 |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## 함수형 프로그래밍 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **고양이** | 기능적 추상화(유형 클래스) |
| **고양이 효과** | IO 모나드, 비동기 런타임 |
| **지오** | 효과 시스템, 전체 생태계 |
| **무형** | 일반 프로그래밍(Scala 2) |
| **새끼 고양이** | 파생 유형 클래스 인스턴스 |
| **단안경** | 광학 도서관 |
---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **키르케** | JSON 라이브러리(고양이) |
| **피클** | JSON 직렬화 |
| **지오 JSON** | 빠른 JSON(ZIO) |
| **fs2** | 기능적 스트림 |
| **테이퍼** | 유형이 안전한 API 엔드포인트 |
| **칼리반** | GraphQL 서버 |
| **Log4cats** | 기능적 로깅 |
| **거절** | CLI 인수 구문 분석 |
| **스퀀트** | 유형이 안전한 수량 |
| **열거함** | 향상된 열거형 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **IntelliJ IDEA + Scala 플러그인** | 최고의 스칼라 IDE |
| **금속** | 언어 서버(다중 편집기) |
| **VS 코드 + 금속** | LSP로 경량화 |
| **네오빔 + 금속** | 터미널 기반 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **뚱뚱한 항아리** | `sbt assembly`|
| **도커** | 다단계 빌드 |
| **GraalVM 네이티브** | 네이티브 이미지(제한적) |
| **쿠버네티스** | 오케스트레이션 |
| **AWS EMR** | AWS에서의 스파크 |
| **데이터브릭스** | 스파크 플랫폼 |
---

## 요약
Scala의 생태계는 엔터프라이즈, 함수형 프로그래밍, 빅 데이터를 포괄합니다. 표준 스택은 빌드용 **sbt**, 언어용 **Scala 3**, 기능적 웹 서비스용 **http4s + cats- effect** 또는 **ZIO**, 데이터베이스 액세스용 **Doobie** 또는 **Slick**, 테스트용 **MUnit**, 형식 지정용 **scalafmt**, IDE 지원용 **IntelliJ + Metals**입니다. Scala는 빅 데이터(Apache Spark는 Scala로 작성됨), 스트리밍(Pekko Streams) 및 JVM 성능이 기능적 프로그래밍과 만나는 모든 분야에서 우위를 점하고 있습니다. Scala 3의 깔끔한 구문, 열거형 및 교차 유형은 언어에 대한 접근성을 더욱 높여줍니다.