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
# Kotlin — エコシステムとツールのガイド
このガイドでは、Kotlin エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## ツールチェーン
|ツール |目的 |
|-----|----------|
| **kotlinc** | Kotlin コンパイラ |
| **Gradle + Kotlin DSL** |ビルドシステム (推奨) |
| **メイブン** |代替ビルド |
| **kotlinx** |公式 Kotlin ライブラリ |
| **Kotlin/ネイティブ** |ネイティブ バイナリにコンパイルする |
| **Kotlin/JS** | JavaScript にコンパイルする |
| **Kotlin マルチプラットフォーム** |プラットフォーム間での共有コード |
| **kscript** | Kotlin スクリプト |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## ビルドツール
|ツール |タイプ |最適な用途 |
|------|------|----------|
| **Gradle (Kotlin DSL)** |プライマリー | Android、マルチモジュール |
| **Gradle (Groovy DSL)** |レガシー |古いプロジェクト |
| **メイブン** | XML ベース |エンタープライズ |
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

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **Ktor** | Kotlin ネイティブ |軽量、非同期 |
| **スプリングブーツ** | Java 相互運用性 |エンタープライズ、フルスタック |
| **http4k** |機能性 |サーバーレス、HTTP |
| **ジャバリン** |軽量 |シンプルなウェブアプリ |
| **Spring WebFlux** |リアクティブ |高い同時実行性 |
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

## Android 開発
|テクノロジー |目的 |
|-----------|-----------|
| **Jetpack Compose** |最新の宣言型 UI |
| **Android SDK** |プラットフォーム API |
| **部屋** | SQLite ORM |
| **レトロフィット** | HTTPクライアント |
| **わかりました** | HTTPエンジン |
| **コルーチン + フロー** |非同期プログラミング |
| **ヒルト/コイン** |依存関係の注入 |
| **ナビゲーション コンポーネント** |画面ナビゲーション |
| **ワークマネージャー** |バックグラウンドタスク |
| **データストア** |プリファレンスの置換 |
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

## データベースと ORM
|テクノロジー |タイプ |
|-----------|------|
| **露出** | JetBrains の Kotlin SQL ライブラリ |
| **部屋** | Android SQLite ORM |
| **休止状態 / JPA** | Java ORM (Kotlin 相互運用性) |
| **jOOQ** |タイプセーフな SQL ビルダー |
| **SQLDelight** |マルチプラットフォーム SQL |
| **レルム** |モバイルデータベース |
| **コティサ** | Kotlin のタイプセーフな SQL |
---

## テスト
|フレームワーク |目的 |
|----------|----------|
| **kotlin.test** |組み込みのテスト ユーティリティ |
| **JUnit 5** |標準テストフレームワーク |
| **モック** | Kotlin ネイティブのモック |
| **Mockito (kotlin)** | Kotlin サポートを備えた Java Mockito |
| **コテスト** | Kotlin テスト フレームワーク (BDD、プロパティ) |
| **タービン** |フローテスト |
| **kotlinx-coroutines-test** |コルーチンのテスト |
| **kotlin-faker** |偽のデータの生成 |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **検出** | Kotlin 静的分析 |
| **ktlint** | Kotlin リンターとフォーマッタ |
| **コーバー** |コードカバレッジ (JetBrains) |
| **ソナークベ** |コード品質プラットフォーム |
| **スポットレス + ktlint** | Gradle での書式設定 |
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

## シリアル化
|図書館 |目的 |
|----------|----------|
| **kotlinx.serialization** |公式、マルチプラットフォーム |
| **ジャクソン (kotlin モジュール)** | Kotlin をサポートする Java JSON |
| **モシ (kotlin)** | Square の JSON ライブラリ |
| **kotlinx.serialization.json** | JSON のサポート |
| **kotlinx.serialization.protobuf** | Protobuf のサポート |
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

## コルーチンと非同期
|図書館 |目的 |
|----------|----------|
| **kotlinx-coroutines-core** |コルーチン プリミティブ |
| **kotlinx-coroutines-android** | Android ディスパッチャ |
| **流れ** |リアクティブストリーム |
| **チャンネル** |コルーチン通信 |
| **StateFlow / SharedFlow** |状態管理 |
---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **kotlinx.coroutines** |コルーチンと非同期 |
| **kotlinx.serialization** |マルチプラットフォームのシリアル化 |
| **kotlinx.datetime** |日付/時刻ライブラリ |
| **矢印** |関数型プログラミング |
| **コイン** |軽量DI |
| **柄** | Android DI (ダガーラッパー) |
| **レトロフィット** | HTTPクライアント |
| **わかりました** | HTTPエンジン |
| **SQLDelight** |マルチプラットフォーム SQL |
| **マルチプラットフォームの構成** |プラットフォーム間での共有 UI |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **IntelliJ IDEA** |最高の Kotlin サポート (JetBrains によって構築) |
| **Android Studio** |公式 Android IDE (IntelliJ ベース) |
| **艦隊** | JetBrains 軽量エディタ |
| **VS コード + Kotlin** |軽量サポート |
---

## Kotlin マルチプラットフォーム
|ターゲット |メモ |
|------|------|
| **アンドロイド** |完全なプラットフォームのサポート |
| **iOS** | Kotlin/ネイティブ経由 |
| **JVM** |デスクトップ、サーバー |
| **JS** |ブラウザ、Node.js |
| **ネイティブ** | macOS、Windows、Linux |
| **WebAssembly** |実験的 |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **JAR** | `java -jar app.jar`|
| **ファット JAR** | uber-jar 用のシャドウ プラグイン |
| **ネイティブ画像** | GraalVM (限定的な Kotlin サポート) |
| **ドッカー** |コンテナ化された展開 |
| **Kotlin/ネイティブ** |スタンドアロン バイナリ (JVM なし) |
| **Google Play** | Android ディストリビューション |
---

＃＃ まとめ
Kotlin のエコシステムは、JVM、Android、マルチプラットフォーム、サーバーサイド開発に及びます。標準スタックは次のとおりです: ビルド用 **Gradle (Kotlin DSL)**、IDE として **IntelliJ IDEA** または **Android Studio**、サーバー側用 **Ktor** (またはエンタープライズ用 **Spring Boot**)、Android UI 用 **Jetpack Compose**、非同期用 **kotlinx.coroutines**、テスト用 **MockK** または **Kotest**、リンティング用 **detekt** JSON の **kotlinx.serialization**。 Kotlin マルチプラットフォームを使用すると、Android、iOS、バックエンド間でビジネス ロジックを共有できます。 Kotlin の強みは、null 安全性、簡潔さ、コルーチンベースの非同期、シームレスな Java 相互運用です。