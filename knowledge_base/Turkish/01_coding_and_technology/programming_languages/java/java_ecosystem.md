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
# Java — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz, Java ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Oluşturma Araçları
| Araç | Tür | En İyisi |
|------|----------|----------|
| **Maven** | XML tabanlı | Kurumsal, yapılandırma yerine kongre |
| **Kepçe** | Harika/Kotlin DSL | Esnek, Android, büyük projeler |
| **Karınca** | XML tabanlı | Eski projeler |
| **Bazel** | Çoklu dil | Monorepos, Google ölçeğinde |
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

## Çerçeveler
### Web / Kurumsal
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Bahar Çizme** | Tam yığın | Kurumsal, mikro hizmetler |
| **Kuarkus** | Bulutta yerel | GraalVM, hızlı başlatma |
| **Mikronot** | AOT derlendi | Düşük bellek, sunucusuz |
| **Jakarta EE** | Standart | Kurumsal Java standardı |
| **Vert.x** | Reaktif | Yüksek eşzamanlılık |
| **Javalin** | Hafif | Basit web uygulamaları |
### Key Spring Ekosistemi
| Modül | Amaç |
|----------|------------|
| **Bahar Ağı** | REST API'leri, MVC |
| **Bahar Verileri** | Veritabanı erişimi (JPA, MongoDB, Redis) |
| **Bahar Güvenliği** | Kimlik doğrulama, yetkilendirme |
| **Bahar Bulutu** | Mikro hizmetler (yapılandırma, keşif, ağ geçidi) |
| **Bahar Grubu** | Toplu işleme |
| **Bahar AMQP** | Mesaj kuyrukları |
---

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **JÜnite 5** | Standart test çerçevesi |
| **Mockito** | Alaycı |
| **İddiaJ** | Akıcı iddialar |
| **Test kapsayıcıları** | Docker tabanlı entegrasyon testleri |
| **WireMock** | HTTP API alayı |
| **ArchUnit** | Mimari testler |
| **REST Güvencesi** | REST API testi |
| **JMH** | Mikro kıyaslama |
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

## Veritabanı
| Teknoloji | Tür |
|---------------|------|
| **JDBC** | Düşük seviyeli SQL erişimi |
| **JPA / Hazırda Bekletme** | ORM standardı |
| **jOOQ** | Tip güvenli SQL oluşturucu |
| **Geçiş yolu** | Veritabanı geçişleri |
| **Sıvıbaz** | Veritabanı geçişleri |
| **HikariCP** | Bağlantı havuzu |
---

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **Kontrol stili** | Kodlama standardının uygulanması |
| **SpotBugs** | Hata modeli tespiti |
| **PMD** | Statik analiz |
| **Hataya Açık** | Google'ın derleyici eklentisi |
| **SonarQube** | Kod kalitesi platformu |
| **JaCoCo** | Kod kapsamı |
| **Lekesiz** | Kod biçimlendirme |
| **Google Java Formatı** | Google'ın tarzı |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **IntelliJ FİKİRİ** | Baskın Java IDE (Topluluk + Ultimate) |
| **Tutulma** | Açık kaynak, eklenti ekosistemi |
| **VS Kodu** | Java uzantılarıyla hafif |
| **NetBeans** | Apache tarafından korunan |
---

## Dağıtım
| Yöntem | Araç |
|----------|------|
| **JAR** | `java -jar app.jar`|
| **SAVAŞ** | Tomcat, İskele'ye Dağıtın |
| **GraalVM** | Yerel görsel derlemesi |
| **Docker** | Konteynerli (Eclipse Temurin, Amazon Corretto) |
| **Kubernetes** | Orkestrasyon |
| **Uygulama Sunucuları** | WildFly, Tomcat, İskele |
---

## JDK Dağıtımları
| Dağıtım | Sağlayıcı |
|---------------|----------|
| **Temurin** | Eclipse/Adoptium (önerilen) |
| **Düzelt** | Amazon |
| **Zulu** | Azul |
| **GraalVM** | Oracle (yerel resim, çok dilli) |
| **Liberika** | BellSoft |
---

## Özet
Java'nın ekosistemi kurumsal bilgi işlem alanında en olgun olanıdır. Standart yığın şunlardır: Derlemeler için **Gradle** veya **Maven**, web/mikro hizmetler için **Spring Boot**, test için **JUnit 5 + Mockito**, ORM için **Hibernate**, IDE olarak **IntelliJ IDEA** ve dağıtım için **Docker**. Java'nın gücü devasa ekosistemi, kurumsal desteği ve geriye dönük uyumluluğudur. Kayıtlar, mühürlü sınıflar, kalıp eşleştirme ve sanal iş parçacıklarıyla modern Java (17+) dili yeniden canlandırıyor.