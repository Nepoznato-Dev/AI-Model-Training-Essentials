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
# कोटलिन - पारिस्थितिकी तंत्र और टूलींग गाइड
यह मार्गदर्शिका कोटलिन पारिस्थितिकी तंत्र में आवश्यक उपकरण, ढांचे और बुनियादी ढांचे को शामिल करती है।
---

## टूलचेन
| उपकरण | उद्देश्य |
|------|---------|
| **कोटलिन्क** | कोटलिन कंपाइलर |
| **ग्रैडल + कोटलिन डीएसएल** | सिस्टम बनाएं (अनुशंसित) |
| **मेवेन** | वैकल्पिक निर्माण |
| **कोटलिनक्स** | आधिकारिक कोटलिन पुस्तकालय |
| **कोटलिन/नेटिव** | देशी बायनेरिज़ में संकलित करें |
| **कोटलिन/जेएस** | जावास्क्रिप्ट में संकलित करें |
| **कोटलिन मल्टीप्लेटफ़ॉर्म** | सभी प्लेटफार्मों पर कोड साझा किया गया |
| **केस्क्रिप्ट** | कोटलिन स्क्रिप्टिंग |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## उपकरण बनाएं
| उपकरण | प्रकार | के लिए सर्वश्रेष्ठ |
|------|------|----------|
| **ग्रैडल (कोटलिन डीएसएल)** | प्राथमिक | एंड्रॉइड, मल्टी-मॉड्यूल |
| **ग्रैडल (ग्रूवी डीएसएल)** | विरासत | पुराने प्रोजेक्ट |
| **मेवेन** | XML-आधारित | उद्यम |
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

## वेब फ्रेमवर्क
| ढाँचा | प्रकार | के लिए सर्वश्रेष्ठ |
|--------|------|-------|
| **केटोर** | कोटलिन-मूल | हल्का, एसिंक |
| **स्प्रिंग बूट** | जावा इंटरऑप | उद्यम, पूर्ण-स्टैक |
| **http4k** | कार्यात्मक | सर्वर रहित, HTTP |
| **जैवलिन** | हल्का वजन | सरल वेब ऐप्स |
| **स्प्रिंग वेबफ्लक्स** | प्रतिक्रियाशील | उच्च-संगामिति |
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

## एंड्रॉइड डेवलपमेंट
| प्रौद्योगिकी | उद्देश्य |
|---|---|
| **जेटपैक कंपोज़** | आधुनिक घोषणात्मक यूआई |
| **एंड्रॉइड एसडीके** | प्लेटफ़ॉर्म एपीआई |
| **कक्ष** | SQLite ORM |
| **रेट्रोफिट** | HTTP क्लाइंट |
| **OkHttp** | HTTP इंजन |
| **कोरटाइन्स + फ्लो** | एसिंक प्रोग्रामिंग |
| **हिल्ट / कोइन** | निर्भरता इंजेक्शन |
| **नेविगेशन घटक** | स्क्रीन नेविगेशन |
| **कार्यप्रबंधक** | पृष्ठभूमि कार्य |
| **डेटास्टोर** | प्राथमिकताएँ प्रतिस्थापन |
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

## डेटाबेस और ओआरएम
| प्रौद्योगिकी | प्रकार |
|------|------|
| **उजागर** | जेटब्रेन की कोटलिन एसक्यूएल लाइब्रेरी |
| **कक्ष** | एंड्रॉइड SQLite ORM |
| **हाइबरनेट/जेपीए** | जावा ओआरएम (कोटलिन इंटरऑप) |
| **जूक** | टाइप-सुरक्षित SQL बिल्डर |
| **SQLDelight** | मल्टीप्लेटफार्म एसक्यूएल |
| **क्षेत्र** | मोबाइल डेटाबेस |
| **कोट्य्सा** | कोटलिन प्रकार-सुरक्षित एसक्यूएल |
---

## परीक्षण
| ढाँचा | उद्देश्य |
|----|----|
| **कोटलिन.टेस्ट** | अंतर्निर्मित परीक्षण उपयोगिताएँ |
| **जूनिट 5** | मानक परीक्षण रूपरेखा |
| **मॉकके** | कोटलिन-मूल उपहास |
| **मॉकिटो (कोटलिन)** | कोटलिन समर्थन के साथ जावा मॉकिटो |
| **कोटेस्ट** | कोटलिन परीक्षण ढांचा (बीडीडी, संपत्ति) |
| **टरबाइन** | प्रवाह परीक्षण |
| **kotlinx-coroutines-परीक्षण** | कोरटाइन परीक्षण |
| **कोटलिन-फेकर** | नकली डेटा जनरेशन |
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

## कोड गुणवत्ता
| उपकरण | उद्देश्य |
|------|---------|
| **पता लगाएं** | कोटलिन स्थैतिक विश्लेषण |
| **ktlint** | कोटलिन लिंटर और फ़ॉर्मेटर |
| **कवर** | कोड कवरेज (जेटब्रेन) |
| **सोनारक्यूब** | कोड गुणवत्ता मंच |
| **बेदाग + ktlint** | ग्रैडल में फ़ॉर्मेटिंग |
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

## क्रमांकन
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **kotlinx.serialization** | आधिकारिक, मल्टीप्लेटफ़ॉर्म |
| **जैक्सन (कोटलिन-मॉड्यूल)** | कोटलिन समर्थन के साथ जावा JSON |
| **मोशी (कोटलिन)** | स्क्वायर की JSON लाइब्रेरी |
| **kotlinx.serialization.json** | JSON समर्थन |
| **kotlinx.serialization.protobuf** | प्रोटोबफ समर्थन |
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

## कोरटाइन्स और एसिंक्स
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **kotlinx-coroutines-core** | कोरटाइन आदिम |
| **kotlinx-coroutines-android** | एंड्रॉइड डिस्पैचर्स |
| **प्रवाह** | प्रतिक्रियाशील धाराएँ |
| **चैनल** | कोरटाइन संचार |
| **स्टेटफ्लो/शेयर्डफ्लो** | राज्य प्रबंधन |
---

## प्रमुख पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **kotlinx.coroutines** | कॉरआउटिंस और एसिंक्स |
| **kotlinx.serialization** | बहुमंचीय क्रमबद्धता |
| **kotlinx.datetime** | दिनांक/समय पुस्तकालय |
| **तीर** | कार्यात्मक प्रोग्रामिंग |
| **कोइन** | लाइटवेट डीआई |
| **हिल्ट** | एंड्रॉइड डीआई (डैगर रैपर) |
| **रेट्रोफिट** | HTTP क्लाइंट |
| **OkHttp** | HTTP इंजन |
| **SQLDelight** | मल्टीप्लेटफार्म एसक्यूएल |
| **मल्टीप्लेटफ़ॉर्म लिखें** | सभी प्लेटफार्मों पर साझा यूआई |
---

## आईडीई और संपादक
| आईडीई | ताकतें |
|----|-----|
| **इंटेलिजे आइडिया** | सर्वश्रेष्ठ कोटलिन समर्थन (जेटब्रेन द्वारा निर्मित) |
| **एंड्रॉइड स्टूडियो** | आधिकारिक एंड्रॉइड आईडीई (इंटेलिजे-आधारित) |
| **बेड़ा** | JetBrains हल्के संपादक |
| **वीएस कोड + कोटलिन** | हल्का समर्थन |
---

## कोटलिन मल्टीप्लेटफ़ॉर्म
| लक्ष्य | नोट्स |
|-------|-------|
| **एंड्रॉइड** | पूर्ण मंच समर्थन |
| **आईओएस** | कोटलिन/नेटिव के माध्यम से |
| **जेवीएम** | डेस्कटॉप, सर्वर |
| **जेएस** | ब्राउज़र, नोड.जेएस |
| **मूलनिवासी** | मैकओएस, विंडोज, लिनक्स |
| **वेबअसेंबली** | प्रायोगिक |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **जार** | `java -jar app.jar`|
| **मोटा जार** | उबर-जार के लिए छाया प्लगइन |
| **मूल छवि** | GraalVM (सीमित कोटलिन समर्थन) |
| **डॉकर** | कंटेनरीकृत परिनियोजन |
| **कोटलिन/नेटिव** | स्टैंडअलोन बाइनरी (कोई जेवीएम नहीं) |
| **गूगल प्ले** | एंड्रॉइड वितरण |
---

## सारांश
कोटलिन का पारिस्थितिकी तंत्र जेवीएम, एंड्रॉइड, मल्टीप्लेटफॉर्म और सर्वर-साइड विकास तक फैला हुआ है। मानक स्टैक है: बिल्ड के लिए **ग्रैडल (कोटलिन डीएसएल)**, आईडीई के रूप में **इंटेलिजे आइडिया** या **एंड्रॉइड स्टूडियो**, सर्वर-साइड के लिए **केटोर** (या एंटरप्राइज़ के लिए **स्प्रिंग बूट**), एंड्रॉइड यूआई के लिए **जेटपैक कंपोज़**, एसिंक्स के लिए **kotlinx.coroutines**, परीक्षण के लिए **मॉकके** या **कोटेस्ट**, लिंटिंग के लिए **detekt**, और JSON के लिए **kotlinx.serialization**। कोटलिन मल्टीप्लेटफ़ॉर्म एंड्रॉइड, आईओएस और बैकएंड पर व्यावसायिक तर्क साझा करने में सक्षम बनाता है। कोटलिन की ताकतें शून्य सुरक्षा, संक्षिप्तता, कोरआउटिन-आधारित एसिंक और निर्बाध जावा इंटरऑप हैं।