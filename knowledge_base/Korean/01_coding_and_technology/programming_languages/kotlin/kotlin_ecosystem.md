<!--
---
# Metadata
title: "Kotlin — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Kotlin ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [kotlin, ecosystem, tooling, android, jvm, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "16 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Kotlin — 생태계 및 도구 가이드
이 가이드에서는 Kotlin 생태계의 필수 도구, 프레임워크, 인프라를 다룹니다.
---

## 툴체인
| 도구 | 목적 |
|------|---------|
| **코틀린** | Kotlin 컴파일러 |
| **Gradle + Kotlin DSL** | 빌드 시스템(권장) |
| **메이븐** | 대체 빌드 |
| **코틀링스** | 공식 Kotlin 라이브러리 |
| **Kotlin/네이티브** | 네이티브 바이너리로 컴파일 |
| **코틀린/JS** | JavaScript로 컴파일 |
| **Kotlin 멀티플랫폼** | 플랫폼 간 공유 코드 |
| **k스크립트** | Kotlin 스크립팅 |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## 빌드 도구
| 도구 | 유형 | 최고의 대상 |
|------|------|----------|
| **Gradle(Kotlin DSL)** | 기본 | 안드로이드, 다중 모듈 |
| **Gradle(그루비 DSL)** | 레거시 | 이전 프로젝트 |
| **메이븐** | XML 기반 | 기업 |
```kotlin
// build.gradle.kts
plugins {
    kotlin("jvm") version "2.0.0"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.ktor:ktor-server-core:2.3.0")
    implementation("io.ktor:ktor-server-netty:2.3.0")
    implementation("org.jetbrains.exposed:exposed-core:0.50.0")
    testImplementation(kotlin("test"))
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
}

application {
    mainClass.set("com.example.MainKt")
}
```

---

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **크토르** | Kotlin 기반 | 경량, 비동기 |
| **스프링 부트** | 자바 상호운용성 | 엔터프라이즈, 풀스택 |
| **http4k** | 기능성 | 서버리스, HTTP |
| **자발린** | 경량 | 간단한 웹 앱 |
| **스프링 WebFlux** | 반응성 | 높은 동시성 |
```kotlin
// Ktor example
fun main() {
    embeddedServer(Netty, port = 8080) {
        routing {
            get("/hello") {
                call.respondText("Hello, World!")
            }
            get("/users/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                    ?: return@get call.respond(HttpStatusCode.BadRequest)
                val user = userService.findById(id)
                call.respond(user ?: HttpStatusCode.NotFound)
            }
        }
    }.start(wait = true)
}
```

---

## 안드로이드 개발
| 기술 | 목적 |
|------------|---------|
| **Jetpack Compose** | 현대적인 선언적 UI |
| **안드로이드 SDK** | 플랫폼 API |
| **방** | SQLite ORM |
| **개조** | HTTP 클라이언트 |
| **확인Http** | HTTP 엔진 |
| **코루틴 + 흐름** | 비동기 프로그래밍 |
| **힐트 / 코인** | 의존성 주입 |
| **탐색 구성요소** | 화면 탐색 |
| **워크매니저** | 백그라운드 작업 |
| **데이터 저장소** | 환경설정 교체 |
```kotlin
// Jetpack Compose example
@Composable
fun UserCard(user: User) {
    Card(modifier = Modifier.padding(8.dp)) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(text = user.name, style = MaterialTheme.typography.headlineSmall)
            Text(text = user.email, style = MaterialTheme.typography.bodyMedium)
        }
    }
}
```

---

## 데이터베이스 및 ORM
| 기술 | 유형 |
|------------|------|
| **노출** | JetBrains의 Kotlin SQL 라이브러리 |
| **방** | 안드로이드 SQLite ORM |
| **최대 절전 모드/JPA** | Java ORM(Kotlin 상호 운용성) |
| **jOOQ** | 유형이 안전한 SQL 빌더 |
| **SQLDelight** | 다중 플랫폼 SQL |
| **영역** | 모바일 데이터베이스 |
| **코티사** | Kotlin 유형 안전 SQL |
---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **kotlin.test** | 내장 테스트 유틸리티 |
| **JUnit 5** | 표준 테스트 프레임워크 |
| **MockK** | Kotlin 네이티브 조롱 |
| **Mockito(코틀린)** | Kotlin을 지원하는 Java Mockito |
| **코테스트** | Kotlin 테스트 프레임워크(BDD, 속성) |
| **터빈** | 흐름 테스트 |
| **kotlinx-코루틴-테스트** | 코루틴 테스트 |
| **코틀린 페이커** | 가짜 데이터 생성 |
```kotlin
// Kotest example
class UserServiceTest : StringSpec({
    "should find user by id" {
        val repo = mockk<UserRepository>()
        coEvery { repo.findById(1) } returns User("Alice")
        val service = UserService(repo)

        val user = service.findById(1)

        user.name shouldBe "Alice"
    }

    "should throw when user not found" {
        val repo = mockk<UserRepository>()
        coEvery { repo.findById(any()) } throws NotFoundException()
        val service = UserService(repo)

        shouldThrow<NotFoundException> {
            service.findById(999)
        }
    }
})
```

---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **감지** | Kotlin 정적 분석 |
| **크틀린트** | Kotlin 린터 및 포맷터 |
| **코버** | 코드 적용 범위(JetBrains) |
| **소나큐브** | 코드 품질 플랫폼 |
| **스팟리스 + ktlint** | Gradle에서 서식 지정 |
```kotlin
// detekt configuration (detekt.yml)
build:
  maxIssues: 0

complexity:
  LongMethod:
    threshold: 60
  TooManyFunctions:
    thresholdInClasses: 15

style:
  MaxLineLength:
    maxLineLength: 120
```

---

## 직렬화
| 도서관 | 목적 |
|---------|---------|
| **kotlinx.serialization** | 공식, 멀티플랫폼 |
| **Jackson(kotlin 모듈)** | Kotlin을 지원하는 Java JSON |
| **모시(코틀린)** | Square의 JSON 라이브러리 |
| **kotlinx.serialization.json** | JSON 지원 |
| **kotlinx.serialization.protobuf** | 프로토부프 지원 |
```kotlin
@Serializable
data class User(
    val id: Long,
    val name: String,
    val email: String,
    val role: Role = Role.USER
)

enum class Role { USER, ADMIN }

// Usage
val json = Json.encodeToString(user)
val user = Json.decodeFromString<User>(jsonString)
```

---

## 코루틴 및 비동기
| 도서관 | 목적 |
|---------|---------|
| **kotlinx-코루틴-코어** | 코루틴 프리미티브 |
| **kotlinx-코루틴-안드로이드** | 안드로이드 디스패처 |
| **흐름** | 반응형 스트림 |
| **채널** | 코루틴 통신 |
| **StateFlow / SharedFlow** | 상태 관리 |
---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **kotlinx.coroutines** | 코루틴과 비동기 |
| **kotlinx.serialization** | 다중 플랫폼 직렬화 |
| **kotlinx.datetime** | 날짜/시간 라이브러리 |
| **화살표** | 함수형 프로그래밍 |
| **코인** | 경량 DI |
| **힐트** | Android DI(Dagger 래퍼) |
| **개조** | HTTP 클라이언트 |
| **확인Http** | HTTP 엔진 |
| **SQLDelight** | 다중 플랫폼 SQL |
| **Compose 멀티플랫폼** | 플랫폼 간 공유 UI |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **IntelliJ 아이디어** | 최고의 Kotlin 지원(JetBrains에서 구축) |
| **안드로이드 스튜디오** | 공식 Android IDE(IntelliJ 기반) |
| **함대** | JetBrains 경량 편집기 |
| **VS 코드 + Kotlin** | 경량 지원 |
---

## Kotlin 멀티플랫폼
| 대상 | 메모 |
|---------|-------|
| **안드로이드** | 전체 플랫폼 지원 |
| **iOS** | Kotlin/네이티브를 통해 |
| **JVM** | 데스크탑, 서버 |
| **JS** | 브라우저, Node.js |
| **네이티브** | 맥OS, 윈도우, 리눅스 |
| **웹어셈블리** | 실험적 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **항아리** | `java -jar app.jar`|
| **뚱뚱한 항아리** | uber-jar용 섀도우 플러그인 |
| **네이티브 이미지** | GraalVM(제한된 Kotlin 지원) |
| **도커** | 컨테이너화된 배포 |
| **Kotlin/네이티브** | 독립 실행형 바이너리(JVM 없음) |
| **구글 플레이** | 안드로이드 배포 |
---

## 요약
Kotlin의 생태계는 JVM, Android, 다중 플랫폼, 서버 측 개발을 포괄합니다. 표준 스택은 빌드용 **Gradle(Kotlin DSL)**, IDE용 **IntelliJ IDEA** 또는 **Android Studio**, 서버측(또는 엔터프라이즈용 **Spring Boot**)용 **Ktor**, Android UI용 **Jetpack Compose**, 비동기용 **kotlinx.coroutines**, 테스트용 **MockK** 또는 **Kotest**, Linting용 **detekt** 및 JSON용 **kotlinx.serialization**. Kotlin Multiplatform을 사용하면 Android, iOS, 백엔드 전반에서 비즈니스 로직을 공유할 수 있습니다. Kotlin의 강점은 널 안전성, 간결성, 코루틴 기반 비동기, 원활한 Java 상호 운용성입니다.