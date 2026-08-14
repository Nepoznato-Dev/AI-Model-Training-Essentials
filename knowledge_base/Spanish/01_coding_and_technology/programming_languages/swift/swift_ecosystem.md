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
# Swift: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema Swift.
---

## Cadena de herramientas
| Herramienta | Propósito |
|------|---------|
| **rápido** | Compilador y REPL |
| **rápido** | Compilador rápido |
| **Administrador de paquetes Swift (SPM)** | Administrador de paquetes incorporado |
| **Xcódigo** | IDE de Apple (solo macOS) |
| **xcodebuild** | Herramienta de compilación CLI |
| **xcrun** | Corredor de herramientas para desarrolladores |
| **Instrumentos** | Perfiles de desempeño |
| **SwiftLint** | Eliminación de código |
| **Formato rápido** | Formato de código |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## Gestión de paquetes
| Herramienta | Tipo | Notas |
|------|------|-------|
| **Administrador de paquetes Swift** | Incorporado | Oficial de Apple, multiplataforma |
| **Cápsulas de cacao** | A base de rubí | iOS/macOS, gran ecosistema |
| **Cartago** | Descentralizado | Marcos binarios |
| **Tuista** | Generación de proyectos | Gestión de proyectos Xcode |
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

## Marcos web (Swift del lado del servidor)
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Vapor** | Pila completa | Más popular, listo para producción |
| **Colibrí** | Ligero | Rápido, moderno, primero asíncrono |
| **Kitura** | IBM | Empresa (archivado) |
| **Perfecto** | Modulares | Swift del lado del servidor |
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

## Base de datos y ORM
| Tecnología | Tipo |
|------------|------|
| **Fluido** | ORM de Vapor (PostgreSQL, MySQL, SQLite) |
| **GRDB** | Kit de herramientas SQLite |
| **Reino** | Base de datos móvil |
| **Datos básicos** | Marco de gráficos de objetos de Apple |
| **Datos Swift** | Persistencia moderna de Apple (iOS 17+) |
| **PostgresNIO** | Controlador PostgreSQL (asíncrono) |
---

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **Prueba XCT** | Pruebas integradas de Apple |
| **Rápido** | Pruebas estilo BDD |
| **Ágil** | Marco Matcher (se empareja con Quick) |
| **Pruebas rápidas** | Moderno basado en macros (Swift 5.9+) |
| **Prueba de instantáneas** | Pruebas de UI/instantáneas |
| **OHHTTPStubs** | Trozo HTTP |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **SwiftLint** | Linting, aplicación del estilo |
| **Formato rápido** | Formato de código |
| **SwiftLint + reglas personalizadas** | Reglas específicas del proyecto |
| **Periferia** | Detección de códigos no utilizados |
| **SónarQube** | Plataforma de calidad de código |
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

## Marcos de trabajo de Apple (iOS/macOS)
| Marco | Propósito |
|-----------|------------------|
| **Interfaz de usuario rápida** | UI declarativa (todas las plataformas Apple) |
| **UIKit** | Interfaz de usuario tradicional de iOS |
| **Kit de aplicaciones** | Interfaz de usuario de macOS |
| **Combinar** | Programación reactiva |
| **async/await** | Concurrencia (concurrencia rápida) |
| **Actores** | Estado mutable seguro para subprocesos |
| **CoreML** | Aprendizaje automático |
| **ARKit** | Realidad aumentada |
| **Kit de salud** | Datos de salud |
| **NubeKit** | Integración de iCloud |
| **Kit de widgets** | Aparatos |
| **TiendaKit 2** | Compras dentro de la aplicación |
---

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **Alamofuego** | Redes HTTP |
| **Martín pescador / Bomba nuclear** | Carga/almacenamiento en caché de imágenes |
| **SnapKit** | Diseño automático DSL |
| **Lottie** | Animaciones de After Effects |
| **SwiftyJSON** | Análisis JSON |
| **Codificable** | Serialización incorporada |
| **Acceso al llavero** | Almacenamiento seguro de credenciales |
| **SwiftLint** | Eliminación de código |
| **RxSwift** | Extensiones reactivas |
| **La Arquitectura Componible** | Arquitectura unidireccional |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Xcódigo** | Requerido para el desarrollo de la plataforma Apple |
| **Código VS + Swift** | Desarrollo Swift multiplataforma |
| **Neovim + kit de fuente-lsp** | Basado en terminal |
| **Código de aplicación** | JetBrains (descontinuado, use Xcode) |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Tienda de aplicaciones** | Distribución iOS/macOS |
| **Vuelo de prueba** | Pruebas beta |
| **Carril rápido** | Construcción/implementación automatizada |
| **Nube Xcode** | CI/CD de Apple |
| **Acciones de GitHub** | CI multiplataforma |
| **Acoplador** | Implementación Swift del lado del servidor |
| **Vapor en ferrocarril/Fly.io** | Alojamiento del lado del servidor |
---

## Resumen
El ecosistema de Swift se divide entre el desarrollo de la plataforma Apple y Swift del lado del servidor. Para Apple: **Xcode** como IDE, **SwiftUI** para UI, **Swift Concurrency** (async/await, actores) para paralelismo, **SwiftData** o **Core Data** para persistencia y **XCTest** o **Swift Testing** para pruebas. Para el lado del servidor: **Vapor** o **Hummingbird** como marco, **SPM** para paquetes y **Docker** para implementación. SwiftLint exige la calidad del código. Los puntos fuertes de Swift son la seguridad (opcionales, tipos de valores), el rendimiento (compilado, LLVM) y la sintaxis moderna. El ecosistema es esencial para cualquiera que cree aplicaciones iOS, macOS, watchOS o tvOS.