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
# جاوا - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم جاوا را پوشش می‌دهد.
---

## ابزارهای ساخت
| ابزار | نوع | بهترین برای |
|------|------|----------|
| **ماون** | مبتنی بر XML | Enterprise، Convention over config |
| **گرادل** | Groovy/Kotlin DSL | انعطاف پذیر، اندروید، پروژه های بزرگ |
| **مورچه** | مبتنی بر XML | پروژه های قدیمی |
| **بازل** | چند زبانه | Monorepos، Google-scale |
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

## چارچوب
### وب / سازمانی
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **چکمه بهاره** | تمام پشته | شرکت، میکروسرویس |
| **کوارکوس** | Cloud-Native | GraalVM، راه اندازی سریع |
| **Micronaut** | AOT گردآوری شده | حافظه کم، بدون سرور |
| **جاکارتا EE** | استاندارد | استاندارد جاوا سازمانی |
| **Vert.x** | واکنشی | همزمانی بالا |
| **جاوالین** | سبک | برنامه های وب ساده |
### اکوسیستم کلید بهار
| ماژول | هدف |
|--------|---------|
| **بهار وب** | REST APIs، MVC |
| **سپرینگ دیتا** | دسترسی به پایگاه داده (JPA، MongoDB، Redis) |
| **سپرینگ امنیت** | احراز هویت، مجوز |
| **ابر بهار** | میکروسرویس ها (پیکربندی، کشف، دروازه) |
| **دسته فنری** | پردازش دسته ای |
| **بهار AMQP** | صف های پیام |
---

## تست
| چارچوب | هدف |
|-----------|---------|
| **واحد 5** | چارچوب آزمون استاندارد |
| **موکیتو** | تمسخر |
| **AssertJ** | ادعاهای روان |
| **تست ظروف** | تست های یکپارچه سازی مبتنی بر داکر |
| **WireMock** | تمسخر API HTTP |
| **ArchUnit** | تست های معماری |
| **مطمئن باشید** | تست REST API |
| **JMH** | Microbenchmarking |
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

## پایگاه داده
| فناوری | نوع |
|------------|------|
| **JDBC** | دسترسی SQL سطح پایین |
| **JPA / Hibernate ** | استاندارد ORM |
| **jOOQ** | سازنده SQL ایمن |
| **فلای وی** | مهاجرت های پایگاه داده |
| **Liquibase** | مهاجرت های پایگاه داده |
| **HikariCP** | استخر اتصال |
---

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **چک استایل** | اجرای استاندارد کدنویسی |
| **SpotBugs** | تشخیص الگوی اشکال |
| **PMD** | تجزیه و تحلیل استاتیک |
| **خطا مستعد ** | افزونه کامپایلر گوگل |
| **SonarQube** | پلت فرم کیفیت کد |
| **جاکوکو** | پوشش کد |
| **بدون لک** | قالب بندی کد |
| **فرمت گوگل جاوا** | سبک گوگل |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **IntelliJ IDEA** | IDE غالب جاوا (Community + Ultimate) |
| **کسوف** | منبع باز، اکوسیستم پلاگین |
| ** کد VS ** | سبک با پسوند جاوا |
| **NetBeans** | Apache-maintained |
---

## استقرار
| روش | ابزار |
|--------|------|
| **جار** | `java -jar app.jar`|
| **جنگ** | مستقر در تامکت، جتی |
| **GraalVM** | گردآوری تصویر بومی |
| **داکر** | ظروف (Eclipse Temurin، Amazon Corretto) |
| **Kubernetes** | ارکستراسیون |
| **سرورهای برنامه** | WildFly، Tomcat، Jetty |
---

## توزیع های JDK
| توزیع | ارائه دهنده |
|-------------|----------|
| **تمورین** | Eclipse/Adoptium (توصیه می شود) |
| **کورتو** | آمازون |
| **زولو** | آزول |
| **GraalVM** | اوراکل (تصویر بومی، چند زبانه) |
| **لیبریکا** | BellSoft |
---

## خلاصه
اکوسیستم جاوا بالغ ترین اکوسیستم در محاسبات سازمانی است. پشته استاندارد عبارتند از: **Gradle** یا **Maven** برای بیلدها، **Spring Boot** برای وب/میکروسرویسها، **JUnit 5 + Mockito** برای آزمایش، **Hibernate** برای ORM، **IntelliJ IDEA** به عنوان IDE، و **Docker** برای استقرار. نقطه قوت جاوا اکوسیستم عظیم، پشتیبانی سازمانی و سازگاری با عقب است. جاوای مدرن (17+) با رکوردها، کلاس های مهر و موم شده، تطبیق الگو، و رشته های مجازی زبان را احیا می کند.