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
# Java — 생태계 및 도구 가이드
이 가이드에서는 Java 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 빌드 도구
| 도구 | 유형 | 최고의 대상 |
|------|------|----------|
| **메이븐** | XML 기반 | 엔터프라이즈, 구성보다 규칙 |
| **그라들** | 그루비/코틀린 DSL | 유연한 Android, 대규모 프로젝트 |
| **개미** | XML 기반 | 레거시 프로젝트 |
| **바젤** | 다국어 | Google 규모의 Monorepos |
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

## 프레임워크
### 웹/엔터프라이즈
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **스프링 부트** | 풀스택 | 엔터프라이즈, 마이크로서비스 |
| **쿼커스** | 클라우드 네이티브 | GraalVM, 빠른 시작 |
| **마이크로노트** | AOT 컴파일 | 낮은 메모리, 서버리스 |
| **자카르타 EE** | 표준 | 엔터프라이즈 Java 표준 |
| **Vert.x** | 반응성 | 높은 동시성 |
| **자발린** | 경량 | 간단한 웹 앱 |
### 키 스프링 생태계
| 모듈 | 목적 |
|---------|---------|
| **스프링 웹** | REST API, MVC |
| **봄 데이터** | 데이터베이스 액세스(JPA, MongoDB, Redis) |
| **스프링 시큐리티** | 인증, 승인 |
| **봄구름** | 마이크로서비스(구성, 검색, 게이트웨이) |
| **봄 배치** | 일괄 처리 |
| **봄 AMQP** | 메시지 대기열 |
---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **JUnit 5** | 표준 테스트 프레임워크 |
| **모키토** | 조롱 |
| **주장J** ​​| 유창한 주장 |
| **테스트 컨테이너** | Docker 기반 통합 테스트 |
| **와이어모크** | HTTP API 조롱 |
| **아치유닛** | 아키텍처 테스트 |
| **REST 보장** | REST API 테스트 |
| **JMH** | 마이크로벤치마킹 |
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

## 데이터베이스
| 기술 | 유형 |
|------------|------|
| **JDBC** | 낮은 수준의 SQL 액세스 |
| **JPA/최대 절전 모드** | ORM 표준 |
| **jOOQ** | 유형이 안전한 SQL 빌더 |
| **이동 경로** | 데이터베이스 마이그레이션 |
| **리퀴베이스** | 데이터베이스 마이그레이션 |
| **히카리CP** | 연결 풀 |
---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **체크스타일** | 코딩표준 시행 |
| **스팟버그** | 버그 패턴 감지 |
| **PMD** | 정적 분석 |
| **오류 발생 가능성** | Google의 컴파일러 플러그인 |
| **소나큐브** | 코드 품질 플랫폼 |
| **자코코** | 코드 적용 범위 |
| **무결함** | 코드 서식 |
| **Google Java 형식** | 구글의 스타일 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **IntelliJ 아이디어** | 주요 Java IDE(커뮤니티 + Ultimate) |
| **일식** | 오픈 소스, 플러그인 생태계 |
| **VS 코드** | Java 확장 기능으로 경량화 |
| **넷빈즈** | Apache가 유지 관리 |
---

## 배포
| 방법 | 도구 |
|---------|------|
| **항아리** | `java -jar app.jar`|
| **전쟁** | Tomcat, Jetty에 배포 |
| **GraalVM** | 네이티브 이미지 편집 |
| **도커** | 컨테이너화(Eclipse Temurin, Amazon Corretto) |
| **쿠버네티스** | 오케스트레이션 |
| **앱 서버** | WildFly, Tomcat, 부두 |
---

## JDK 배포판
| 유통 | 공급자 |
|-------------|----------|
| **테무린** | Eclipse/Adoptium(권장) |
| **코레토** | 아마존 |
| **줄루어** | 아줄 |
| **GraalVM** | Oracle(네이티브 이미지, 다중 언어) |
| **리베리카** | 벨소프트 |
---

## 요약
Java의 생태계는 엔터프라이즈 컴퓨팅 분야에서 가장 성숙합니다. 표준 스택은 빌드용 **Gradle** 또는 **Maven**, 웹/마이크로서비스용 **Spring Boot**, 테스트용 **JUnit 5 + Mockito**, ORM용 **Hibernate**, IDE용 **IntelliJ IDEA**, 배포용 **Docker**입니다. Java의 강점은 대규모 생태계, 기업 지원 및 이전 버전과의 호환성입니다. 레코드, 봉인된 클래스, 패턴 일치 및 가상 스레드를 갖춘 최신 Java(17+)가 언어에 활력을 불어넣고 있습니다.