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
# Java — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Java.
---

## Alat Bangun
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| **Maven** | Berbasis XML | Perusahaan, konvensi atas config |
| **Kelas** | DSL Groovy/Kotlin | Fleksibel, Android, proyek besar |
| **Semut** | Berbasis XML | Proyek warisan |
| **Bazel** | Multi-bahasa | Monorepos, skala Google |
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

## Kerangka kerja
### Web / Perusahaan
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Sepatu Musim Semi** | Tumpukan penuh | Perusahaan, layanan mikro |
| **Kuarkus** | Cloud-asli | GraalVM, startup cepat |
| **Mikronaut** | AOT dikompilasi | Memori rendah, tanpa server |
| **Jakarta EE** | Standar | Standar Java Perusahaan |
| **Vertikal.x** | Reaktif | Konkurensi tinggi |
| **Javalin** | Ringan | Aplikasi web sederhana |
### Ekosistem Mata Air Kunci
| Modul | Tujuan |
|--------|---------|
| **Web Musim Semi** | REST API, MVC |
| **Data Musim Semi** | Akses basis data (JPA, MongoDB, Redis) |
| **Keamanan Musim Semi** | Otentikasi, otorisasi |
| **Awan Musim Semi** | Layanan mikro (konfigurasi, penemuan, gateway) |
| **Gelombang Musim Semi** | Pemrosesan batch |
| **AMQP Musim Semi** | Antrian pesan |
---

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **5 JUNI** | Kerangka uji standar |
| **Mockito** | Mengejek |
| **TegaskanJ** | Pernyataan lancar |
| **Wadah uji** | Tes integrasi berbasis Docker |
| **KawatMock** | HTTP API mengejek |
| **Unit Agung** | Tes arsitektur |
| **Yakinlah** | Pengujian REST API |
| **JMH** | Benchmarking Mikro |
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

## Basis Data
| Teknologi | Ketik |
|------------|------|
| **JDBC** | Akses SQL tingkat rendah |
| **JPA / Hibernasi** | Standar ORM |
| **jOOQ** | Pembuat SQL yang aman untuk tipe |
| **Jalur Terbang** | Migrasi basis data |
| **Liquibase** | Migrasi basis data |
| **HikariCP** | Kumpulan koneksi |
---

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **Gaya centang** | Penegakan standar pengkodean |
| **Bug Spot** | Deteksi pola bug |
| **PMD** | Analisis statis |
| **Rawan Kesalahan** | Plugin kompiler Google |
| **SonarQube** | Platform kualitas kode |
| **JaCoCo** | Cakupan kode |
| **Tanpa Noda** | Pemformatan kode |
| **Format Google Java** | Gaya Google |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **IDE IntelliJ** | IDE Java Dominan (Komunitas + Ultimate) |
| **Gerhana** | Sumber terbuka, ekosistem plugin |
| **Kode VS** | Ringan dengan ekstensi Java |
| **NetBeans** | Dikelola Apache |
---

## Penerapan
| Metode | Alat |
|--------|------|
| **JAR** | `java -jar app.jar`|
| **PERANG** | Dikerahkan ke Tomcat, Jetty |
| **GraalVM** | Kompilasi gambar asli |
| **Buruh pelabuhan** | Dalam Kontainer (Eclipse Temurin, Amazon Corretto) |
| **Kubernetes** | Orkestrasi |
| **Server Aplikasi** | WildFly, Tomcat, Dermaga |
---

## Distribusi JDK
| Distribusi | Penyedia |
|-------------|----------|
| **Temurin** | Eclipse/Adoptium (disarankan) |
| **Korret** | Amazon |
| **Zulu** | Azul |
| **GraalVM** | Oracle (gambar asli, poliglot) |
| **Liberika** | BellSoft |
---

## Ringkasan
Ekosistem Java adalah yang paling matang dalam komputasi perusahaan. Tumpukan standarnya adalah: **Gradle** atau **Maven** untuk build, **Spring Boot** untuk web/layanan mikro, **JUnit 5 + Mockito** untuk pengujian, **Hibernate** untuk ORM, **IntelliJ IDEA** sebagai IDE, dan **Docker** untuk penerapan. Kekuatan Java terletak pada ekosistemnya yang besar, dukungan perusahaan, dan kompatibilitas ke belakang. Java modern (17+) dengan catatan, kelas tersegel, pencocokan pola, dan rangkaian virtual merevitalisasi bahasa ini.