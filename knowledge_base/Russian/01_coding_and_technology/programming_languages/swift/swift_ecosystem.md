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
# Swift — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы Swift.
---

## Инструментальная цепочка
| Инструмент | Цель |
|------|---------|
| **быстро** | Компилятор и REPL |
| **быстрый** | Компилятор Swift |
| **Менеджер пакетов Swift (SPM)** | Встроенный менеджер пакетов |
| **Xcode** | Apple IDE (только для macOS) |
| **xcodebuild** | Инструмент сборки CLI |
| **xcrun** | Инструмент разработчика |
| **Инструменты** | Профилирование производительности |
| **СвифтЛинт** | Линтинг кода |
| **СвифтФормат** | Форматирование кода |
```bash
swift build               # build SPM project
swift test                # run tests
swift run                 # run executable
swift package init --type executable  # new project
swift package resolve     # resolve dependencies
```

---

## Управление пакетами
| Инструмент | Тип | Заметки |
|------|------|-------|
| **Менеджер пакетов Swift** | Встроенный | Официальный, кросс-платформенный от Apple |
| **Какао-подс** | На основе Ruby | iOS/macOS, большая экосистема |
| **Карфаген** | Децентрализованный | Бинарные фреймворки |
| **Туист** | Генерация проекта | Управление проектами Xcode |
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

## Веб-фреймворки (Серверный Swift)
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **Пар** | Полный стек | Самый популярный, готовый к производству |
| **Колибри** | Легкий | Быстрый, современный, асинхронный |
| **Китура** | IBM | Предприятие (в архиве) |
| **Идеально** | Модульный | Серверная часть Swift |
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

## База данных и ORM
| Технология | Тип |
|------------|------|
| **Свободное владение** | ORM Vapor (PostgreSQL, MySQL, SQLite) |
| **ГРДБ** | Инструментарий SQLite |
| **Царство** | Мобильная база данных |
| **Основные данные** | Структура объектного графа Apple |
| **СвифтДанные** | Современная настойчивость Apple (iOS 17+) |
| **ПостгресНИО** | Драйвер PostgreSQL (асинхронный) |
---

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **XCTest** | Встроенное тестирование Apple |
| **Быстро** | Тестирование в стиле BDD |
| **Проворный** | Платформа Matcher (в паре с Quick) |
| **Быстрое тестирование** | Современный макрос (Swift 5.9+) |
| **Снимочное тестирование** | Тестирование пользовательского интерфейса/снимков |
| **OHHTTPStubs** | HTTP-заглушка |
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

## Качество кода
| Инструмент | Цель |
|------|---------|
| **СвифтЛинт** | Линтинг, соблюдение стиля |
| **СвифтФормат** | Форматирование кода |
| **SwiftLint + пользовательские правила** | Правила, специфичные для проекта |
| **Периферия** | Обнаружение неиспользуемого кода |
| **SonarQube** | Платформа качества кода |
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

## Платформы Apple (iOS/macOS)
| Рамочная | Цель |
|-----------|---------|
| **СвифтUI** | Декларативный пользовательский интерфейс (все платформы Apple) |
| **UIKit** | Традиционный пользовательский интерфейс iOS |
| **AppKit** | Пользовательский интерфейс MacOS |
| **Объединить** | Реактивное программирование |
| **асинхронный/ожидание** | Параллелизм (Swift Concurrency) |
| **Актеры** | Потокобезопасное изменяемое состояние |
| **CoreML** | Машинное обучение |
| **АРКит** | Дополненная реальность |
| **Аптечка** | Данные о здоровье |
| **Облачный комплект** | интеграция с iCloud |
| **Набор виджетов** | Виджеты |
| **StoreKit 2** | Покупки в приложении |
---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **Аламофайр** | HTTP-сети |
| **Зимородок/Ядерная бомба** | Загрузка/кэширование изображений |
| **СнапКит** | Автоматическая компоновка DSL |
| **Лотти** | Анимации After Effects |
| **SwiftyJSON** | Разбор JSON |
| **Кодируемый** | Встроенная сериализация |
| **Доступ к цепочке ключей** | Безопасное хранение учетных данных |
| **СвифтЛинт** | Линтинг кода |
| **RxSwift** | Реактивные расширения |
| **Компонуемая архитектура** | Однонаправленная архитектура |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **Xcode** | Требуется для разработки платформы Apple |
| **VS Code + Swift** | Кроссплатформенная разработка на Swift |
| **Neovim + sourcekit-lsp** | На базе терминала |
| **Код приложения** | JetBrains (снято с производства, используйте Xcode) |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Магазин приложений** | Дистрибутив iOS/macOS |
| **Тестовый полет** | Бета-тестирование |
| **Скорая полоса** | Автоматизированная сборка/развертывание |
| **Облако Xcode** | CI/CD от Apple |
| **Действия GitHub** | Межплатформенная CI |
| **Докер** | Развертывание Swift на стороне сервера |
| **Пар на железной дороге/Fly.io** | Серверный хостинг |
---

## Краткое содержание
Экосистема Swift разделена между разработкой платформы Apple и серверной частью Swift. Для Apple: **Xcode** в качестве IDE, **SwiftUI** для пользовательского интерфейса, **Swift Concurrency** (async/await, субъекты) для параллелизма, **SwiftData** или **Core Data** для постоянства и **XCTest** или **Swift Testing** для тестов. На стороне сервера: **Vapor** или **Hummingbird** в качестве платформы, **SPM** для пакетов и **Docker** для развертывания. SwiftLint обеспечивает качество кода. Сильными сторонами Swift являются безопасность (опции, типы значений), производительность (компиляция, LLVM) и современный синтаксис. Экосистема важна для всех, кто создает приложения для iOS, macOS, watchOS или tvOS.