<!--
---
# Metadata
title: "Swift — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Swift ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [swift, ecosystem, tooling, apple, ios, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Swift – Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema Swift.
---

## Conjunto de ferramentas
| Ferramenta | Finalidade |
|------|---------|
| **rápido** | Compilador e REPL |
| **rápido** | Compilador rápido |
| **Gerenciador de Pacotes Swift (SPM)** | Gerenciador de pacotes integrado |
| **Xcódigo** | IDE da Apple (somente macOS) |
| **xcodebuild** | Ferramenta de construção CLI |
| **xcrun** | Corredor de ferramentas do desenvolvedor |
| **Instrumentos** | Perfil de desempenho |
| **SwiftLint** | Linting de código |
| **SwiftFormat** | Formatação de código |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## Gerenciamento de pacotes
| Ferramenta | Tipo | Notas |
|------|------|-------|
| **Gerenciador de Pacotes Swift** | Integrado | Plataforma cruzada oficial da Apple |
| **CocoaPods** | Baseado em Ruby | iOS/macOS, grande ecossistema |
| **Cartago** | Descentralizado | Estruturas binárias |
| **Tuist** | Geração de projetos | Gerenciamento de projetos Xcode |
```swift
// Package.swift
// swift-tools-version: 5.10
import PackageDescription

let package = Package(
    name: "MyApp",
    platforms: [.macOS(.v14), .iOS(.v17)],
    dependencies: [
        .package(url: "https://github.com/Alamofire/Alamofire", from: "5.9.0"),
        .package(url: "https://github.com/SwiftyJSON/SwiftyJSON", from: "5.0.0"),
    ],
    targets: [
        .executableTarget(
            name: "MyApp",
            dependencies: ["Alamofire", "SwiftyJSON"]),
        .testTarget(name: "MyAppTests", dependencies: ["MyApp"]),
    ]
)
```

---

## Frameworks Web (Swift do lado do servidor)
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **Vapor** | Pilha completa | Mais popular, pronto para produção |
| **Beija-flor** | Leve | Rápido, moderno, assíncrono primeiro |
| **Kitura** | IBM | Empresa (arquivada) |
| **Perfeito** | Modular | Swift do lado do servidor |
```swift
// Vapor example
import Vapor

func routes(_ app: Application) throws {
    app.get("hello") { req in
        "Hello, World!"
    }

    app.get("users", ":id") { req async throws -> User in
        let id = req.parameters.get("id")!
        return try await User.find(id, on: req.db) ?? abort(.notFound)
    }
}
```

---

## Banco de dados e ORM
| Tecnologia | Tipo |
|------------|------|
| **Fluente** | ORM do Vapor (PostgreSQL, MySQL, SQLite) |
| **GRDB** | Kit de ferramentas SQLite |
| **Reino** | Banco de dados móvel |
| **Dados principais** | Estrutura de gráfico de objetos da Apple |
| **SwiftData** | Persistência moderna da Apple (iOS 17+) |
| **PostgresNIO** | Driver PostgreSQL (assíncrono) |
---

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **XCTest** | Testes integrados da Apple |
| **Rápido** | Teste estilo BDD |
| **Ágil** | Estrutura Matcher (pares com Quick) |
| **Teste rápido** | Moderno baseado em macro (Swift 5.9+) |
| **Teste de instantâneo** | Teste de UI/instantâneo |
| **OHHTTPStubs** | stub HTTP |
```swift
// Swift Testing (modern)
import Testing

@Test("user creation")
func createUser() async throws {
    let service = UserService()
    let user = try await service.create(name: "Alice", email: "alice@example.com")
    #expect(user.name == "Alice")
    #expect(user.email == "alice@example.com")
}

// XCTest
class UserServiceTests: XCTestCase {
    func testCreateUser() async throws {
        let service = UserService()
        let user = try await service.create(name: "Alice", email: "alice@example.com")
        XCTAssertEqual(user.name, "Alice")
    }
}
```

---

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **SwiftLint** | Linting, aplicação de estilo |
| **SwiftFormat** | Formatação de código |
| **SwiftLint + regras personalizadas** | Regras específicas do projeto |
| **Periferia** | Detecção de código não utilizado |
| **SonarQube** | Plataforma de qualidade de código |
```yaml
# .swiftlint.yml
included:
  - Sources
excluded:
  - Tests/.build

line_length:
  warning: 120
  error: 200

type_body_length:
  warning: 300
  error: 500
```

---

## Estruturas Apple (iOS/macOS)
| Estrutura | Finalidade |
|-----------|---------|
| **SwiftUI** | UI declarativa (todas as plataformas Apple) |
| **UIKit** | UI iOS tradicional |
| **AppKit** | IU do macOS |
| **Combinar** | Programação reativa |
| **assíncrono/aguarda** | Simultaneidade (Simultaneidade Swift) |
| **Atores** | Estado mutável thread-safe |
| **CoreML** | Aprendizado de máquina |
| **ARKit** | Realidade aumentada |
| **Kit de Saúde** | Dados de saúde |
| **CloudKit** | Integração iCloud |
| **WidgetKit** | Widgets |
| **LojaKit 2** | Compras no aplicativo |
---

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **Alamofire** | Rede HTTP |
| **Martim-pescador/Nuke** | Carregamento/cache de imagem |
| **SnapKit** | Layout automático DSL |
| **Lottie** | Animações After Effects |
| **SwiftyJSON** | Análise JSON |
| **Codificável** | Serialização integrada |
| **Acesso às Chaves** | Armazenamento seguro de credenciais |
| **SwiftLint** | Linting de código |
| **RxSwift** | Extensões reativas |
| **A Arquitetura Combinável** | Arquitetura unidirecional |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Xcódigo** | Necessário para desenvolvimento da plataforma Apple |
| **Código VS + Swift** | Desenvolvimento Swift multiplataforma |
| **Neovim + sourcekit-lsp** | Baseado em terminal |
| **AppCode** | JetBrains (descontinuado, use Xcode) |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Loja de aplicativos** | Distribuição iOS/macOS |
| **TestFlight** | Teste beta |
| **Lista rápida** | Construção/implantação automatizada |
| **Nuvem Xcode** | CI/CD da Apple |
| **Ações do GitHub** | CI multiplataforma |
| **Docker** | Implantação Swift no lado do servidor |
| **Vapor na Ferrovia/Fly.io** | Hospedagem do lado do servidor |
---

## Resumo
O ecossistema do Swift está dividido entre o desenvolvimento da plataforma Apple e o Swift do lado do servidor. Para Apple: **Xcode** como IDE, **SwiftUI** para UI, **Swift Concurrency** (async/await, atores) para paralelismo, **SwiftData** ou **Core Data** para persistência e **XCTest** ou **Swift Testing** para testes. Para lado do servidor: **Vapor** ou **Hummingbird** como estrutura, **SPM** para pacotes e **Docker** para implantação. SwiftLint reforça a qualidade do código. Os pontos fortes do Swift são segurança (opcionais, tipos de valor), desempenho (compilado, LLVM) e sintaxe moderna. O ecossistema é essencial para qualquer pessoa que crie aplicativos iOS, macOS, watchOS ou tvOS.