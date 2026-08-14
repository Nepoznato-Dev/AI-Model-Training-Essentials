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
# Kotlin - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่สำคัญในระบบนิเวศ Kotlin
---

## ห่วงโซ่เครื่องมือ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **kotlinc** | คอมไพเลอร์ Kotlin |
| **Gradle + Kotlin DSL** | สร้างระบบ (แนะนำ) |
| **มาเวน** | บิลด์ทางเลือก |
| **kotlinx** | ห้องสมุด Kotlin อย่างเป็นทางการ |
| **Kotlin/พื้นเมือง** | คอมไพล์เป็นไบนารีดั้งเดิม |
| **Kotlin/JS** | คอมไพล์เป็น JavaScript |
| **Kotlin หลากหลายแพลตฟอร์ม** | รหัสที่ใช้ร่วมกันข้ามแพลตฟอร์ม |
| **kscript** | การเขียนสคริปต์ Kotlin |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## สร้างเครื่องมือ
| เครื่องมือ | พิมพ์ | ดีที่สุดสำหรับ |
|------|-|---------|
| **Gradle (Kotlin DSL)** | หลัก | Android หลายโมดูล |
| **Gradle (Groovy DSL)** | มรดก | โครงการเก่า |
| **มาเวน** | อิง XML | องค์กร |
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

## กรอบงานเว็บ
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **กทอร์** | Kotlin-พื้นเมือง | น้ำหนักเบา แบบอะซิงโครนัส |
| **สปริงบูท** | การทำงานร่วมกันของ Java | องค์กร ฟูลสแตก |
| **http4k** | ฟังก์ชั่น | ไร้เซิร์ฟเวอร์ HTTP |
| **จาวาลิน** | น้ำหนักเบา | เว็บแอปง่ายๆ |
| **Spring WebFlux** | ปฏิกิริยา | พร้อมกันสูง |
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

## การพัฒนา Android
| เทคโนโลยี | วัตถุประสงค์ |
|------------|---------|
| **เขียน Jetpack** | UI ที่ประกาศสมัยใหม่ |
| **Android SDK** | API ของแพลตฟอร์ม |
| **ห้อง** | SQLite ORM |
| **ชุดติดตั้งเพิ่ม** | ไคลเอ็นต์ HTTP |
| **ตกลงHttp** | เครื่องมือ HTTP |
| **โครูทีน + โฟลว์** | การเขียนโปรแกรมแบบอะซิงก์ |
| **ด้าม/โคอิน** | การฉีดพึ่งพา |
| **ส่วนประกอบการนำทาง** | การนำทางหน้าจอ |
| **ผู้จัดการงาน** | งานพื้นหลัง |
| **คลังข้อมูล** | การแทนที่ค่ากำหนด |
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

## ฐานข้อมูลและ ORM
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **เปิดเผย** | ไลบรารี Kotlin SQL ของ JetBrains |
| **ห้อง** | Android SQLite ORM |
| **ไฮเบอร์เนต / JPA** | Java ORM (การทำงานร่วมกันของ Kotlin) |
| **jOOQ** | ตัวสร้าง SQL ที่ปลอดภัยต่อประเภท |
| **SQLDelight** | SQL หลายแพลตฟอร์ม |
| **อาณาจักร** | ฐานข้อมูลมือถือ |
| **โคทิสา** | Kotlin ชนิดปลอดภัย SQL |
---

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **kotlin.test** | ยูทิลิตี้ทดสอบในตัว |
| **มิถุนายน 5** | กรอบการทดสอบมาตรฐาน |
| **ม็อคเค** | การเยาะเย้ยแบบพื้นเมืองของ Kotlin |
| **ม็อกคิโต (คอตลิน)** | Java Mockito พร้อม Kotlin รองรับ |
| **โคเตสท์** | กรอบการทดสอบ Kotlin (BDD, คุณสมบัติ) |
| **กังหัน** | การทดสอบการไหล |
| **kotlinx-coroutines-test** | การทดสอบ Coroutine |
| **kotlin-faker** | การสร้างข้อมูลปลอม |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ตรวจจับ** | การวิเคราะห์แบบคงที่ Kotlin |
| **ktlint** | Kotlin linter และฟอร์แมตเตอร์ |
| **โคเวอร์** | การครอบคลุมโค้ด (JetBrains) |
| **โซนาร์คิวบ์** | แพลตฟอร์มคุณภาพรหัส |
| **สะอาดสะอ้าน + ktlint** | การจัดรูปแบบใน Gradle |
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

## การทำให้เป็นอนุกรม
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **kotlinx.serialization** | เป็นทางการ หลากหลายแพลตฟอร์ม |
| **แจ็คสัน (โมดูล kotlin)** | Java JSON พร้อมรองรับ Kotlin |
| **โมชิ (โคตลิน)** | ไลบรารี JSON ของ Square |
| **kotlinx.serialization.json** | รองรับ JSON |
| **kotlinx.serialization.protobuf** | รองรับ Protobuf |
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

## โครูทีนและอะซิงค์
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **kotlinx-coroutines-core** | Coroutine ดั้งเดิม |
| **kotlinx-coroutines-android** | ผู้มอบหมายงาน Android |
| **ไหล** | กระแสปฏิกิริยา |
| **ช่อง** | การสื่อสาร Coroutine |
| **StateFlow / SharedFlow** | การจัดการของรัฐ |
---

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **kotlinx.coroutines** | Coroutines และ async |
| **kotlinx.serialization** | การทำให้เป็นอนุกรมหลายแพลตฟอร์ม |
| **kotlinx.datetime** | ไลบรารีวันที่/เวลา |
| **ลูกศร** | การเขียนโปรแกรมเชิงฟังก์ชัน |
| **คอยน์** | DI | น้ำหนักเบา
| **ด้าม** | Android DI (กระดาษห่อกริช) |
| **ชุดติดตั้งเพิ่ม** | ไคลเอ็นต์ HTTP |
| **ตกลงHttp** | เครื่องมือ HTTP |
| **SQLDelight** | SQL หลายแพลตฟอร์ม |
| **เขียนได้หลากหลายแพลตฟอร์ม** | UI ที่ใช้ร่วมกันข้ามแพลตฟอร์ม |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **IntelliJ IDEA** | การสนับสนุน Kotlin ที่ดีที่สุด (สร้างโดย JetBrains) |
| **Android Studio** | Android IDE อย่างเป็นทางการ (ใช้ IntelliJ) |
| **กองเรือ** | โปรแกรมแก้ไขน้ำหนักเบา JetBrains |
| **VS Code + Kotlin** | รองรับน้ำหนักเบา |
---

## Kotlin มัลติแพลตฟอร์ม
| เป้าหมาย | หมายเหตุ |
|--------|--------|
| **แอนดรอยด์** | รองรับแพลตฟอร์มเต็มรูปแบบ |
| **iOS** | ผ่าน Kotlin/Native |
| **เจวีเอ็ม** | เดสก์ท็อป เซิร์ฟเวอร์ |
| **จส** | เบราว์เซอร์, Node.js |
| **พื้นเมือง** | macOS, Windows, ลินุกซ์ |
| **เว็บแอสเซมบลี** | ทดลอง |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **จาร์** | `java -jar app.jar`|
| **จาร์อ้วน** | ปลั๊กอินเงาสำหรับ uber-jar |
| **ภาพพื้นเมือง** | GraalVM (รองรับ Kotlin แบบจำกัด) |
| **นักเทียบท่า** | การปรับใช้แบบคอนเทนเนอร์ |
| **Kotlin/พื้นเมือง** | ไบนารี่แบบสแตนด์อโลน (ไม่มี JVM) |
| **กูเกิลเพลย์** | การกระจาย Android |
---

## สรุป
ระบบนิเวศของ Kotlin ครอบคลุมการพัฒนา JVM, Android, มัลติแพลตฟอร์ม และฝั่งเซิร์ฟเวอร์ สแต็กมาตรฐานคือ: **Gradle (Kotlin DSL)** สำหรับบิลด์, **IntelliJ IDEA** หรือ **Android Studio** เป็น IDE, **Ktor** สำหรับฝั่งเซิร์ฟเวอร์ (หรือ **Spring Boot** สำหรับองค์กร), **Jetpack Compose** สำหรับ Android UI, **kotlinx.coroutines** สำหรับ async, **MockK** หรือ **Kotest** สำหรับการทดสอบ, **detekt** สำหรับ Linting และ **kotlinx.serialization** สำหรับ JSON Kotlin Multiplatform ช่วยให้สามารถแชร์ตรรกะทางธุรกิจได้ทั้งบน Android, iOS และแบ็กเอนด์ จุดแข็งของ Kotlin คือความปลอดภัยแบบ null ความกระชับ async ที่ใช้ coroutine และการทำงานร่วมกันของ Java ที่ราบรื่น