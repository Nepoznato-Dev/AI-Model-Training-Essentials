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
# Java – Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema Java.
---

## Ferramentas de construção
| Ferramenta | Tipo | Melhor para |
|------|------|----------|
| **Maven** | Baseado em XML | Empresa, convenção sobre configuração |
| **Gradle** | DSL bacana/Kotlin | Flexível, Android, grandes projetos |
| **Formiga** | Baseado em XML | Projetos legados |
| **Bazel** | Multilíngue | Monorepos, escala Google |
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

## Estruturas
### Web/Empresa
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **Bota de primavera** | Pilha completa | Empresa, microsserviços |
| **Quarkus** | Nativo da nuvem | GraalVM, inicialização rápida |
| **Micronauta** | AOT compilado | Pouca memória, sem servidor |
| **Jacarta EE** | Padrão | Padrão Java corporativo |
| **Vert.x** | Reativo | Alta simultaneidade |
| **Javalino** | Leve | Aplicativos web simples |
### Ecossistema Key Spring
| Módulo | Finalidade |
|--------|---------|
| **Web de primavera** | API REST, MVC |
| **Dados da primavera** | Acesso a banco de dados (JPA, MongoDB, Redis) |
| **Segurança da Primavera** | Autenticação, autorização |
| **Nuvem de primavera** | Microsserviços (configuração, descoberta, gateway) |
| **Lote de primavera** | Processamento em lote |
| **AMQP Primavera** | Filas de mensagens |
---

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **JUnit 5** | Estrutura de teste padrão |
| **Mockito** | Zombando |
| **AfirmarJ** | Afirmações fluentes |
| **Contêineres de teste** | Testes de integração baseados em Docker |
| **WireMock** | Simulação da API HTTP |
| **ArchUnit** | Testes de arquitetura |
| **DESCANSO Garantido** | Teste de API REST |
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

## Banco de dados
| Tecnologia | Tipo |
|------------|------|
| **JDBC** | Acesso SQL de baixo nível |
| **JPA/Hibernação** | Padrão ORM |
| **jOOQ** | Construtor SQL com segurança de tipo |
| **Via aérea** | Migrações de banco de dados |
| **Liquibase** | Migrações de banco de dados |
| **HikariCP** | Conjunto de conexões |
---

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **Estilo de verificação** | Aplicação padrão de codificação |
| **SpotBugs** | Detecção de padrões de bugs |
| **PMD** | Análise estática |
| **Propenso a erros** | Plug-in do compilador do Google |
| **SonarQube** | Plataforma de qualidade de código |
| **JaCoCo** | Cobertura de código |
| **Impecável** | Formatação de código |
| **Formato Google Java** | O estilo do Google |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **IDEIA IntelliJ** | IDE Java dominante (Community + Ultimate) |
| **Eclipse** | Código aberto, ecossistema de plugins |
| **Código VS** | Leve com extensões Java |
| **NetBeans** | Mantido pelo Apache |
---

## Implantação
| Método | Ferramenta |
|--------|------|
| **JAR** | `java -jar app.jar`|
| **GUERRA** | Implantar no Tomcat, Jetty |
| **GraalVM** | Compilação de imagens nativas |
| **Docker** | Contêinerizado (Eclipse Temurin, Amazon Corretto) |
| **Kubernetes** | Orquestração |
| **Servidores de aplicativos** | WildFly, Tomcat, Molhe |
---

## Distribuições JDK
| Distribuição | Provedor |
|------------|----------|
| **Temurin** | Eclipse/Adoptium (recomendado) |
| **Correto** | Amazônia |
| **Zulu** | Azul |
| **GraalVM** | Oracle (imagem nativa, poliglota) |
| **Libéria** | BellSoft |
---

## Resumo
O ecossistema Java é o mais maduro em computação empresarial. A pilha padrão é: **Gradle** ou **Maven** para compilações, **Spring Boot** para web/microsserviços, **JUnit 5 + Mockito** para testes, **Hibernate** para ORM, **IntelliJ IDEA** como IDE e **Docker** para implantação. A força do Java é seu enorme ecossistema, suporte empresarial e compatibilidade com versões anteriores. Java moderno (17+) com registros, classes seladas, correspondência de padrões e threads virtuais está revitalizando a linguagem.