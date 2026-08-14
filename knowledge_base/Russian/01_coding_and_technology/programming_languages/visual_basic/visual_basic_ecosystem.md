---
# Metadata
title: "Visual Basic — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Visual Basic ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [visual-basic, vbnet, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Visual Basic — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы Visual Basic (.NET).
---

## Версии Visual Basic
| Версия | Заметки |
|---------|-------|
| **VB.NET (Visual Basic 2022)** | Текущая версия, .NET 8+ |
| **ВБ6** | Классический Visual Basic (устаревший вариант) |
| **ВБА** | Visual Basic для приложений (Office) |
| **VBScript** | Язык сценариев (устаревший) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Инструменты сборки
| Инструмент | Цель |
|------|---------|
| **интерфейс командной строки dotnet** | .NET сборка, тестирование, публикация |
| **MSBuild** | Построить двигатель |
| **Визуальная студия** | Полная IDE |
| **НюГет** | Управление пакетами |
```xml
<!-- .vbproj (SDK-style) -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <RootNamespace>MyApp</RootNamespace>
    <TargetFramework>net8.0</TargetFramework>
    <OptionStrict>On</OptionStrict>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
  </ItemGroup>
</Project>
```

---

## Веб-фреймворки
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **ASP.NET Core** | Полный стек | API, MVC, страницы Razor |
| **Минимальные API** | Легкий | Простые API |
| **Блазор** | Веб-интерфейс | Компонентный пользовательский интерфейс |
| **СигналR** | В режиме реального времени | Вебсокеты |
```vb
' ASP.NET Core Minimal API
Imports Microsoft.AspNetCore.Builder
Imports Microsoft.Extensions.DependencyInjection

Dim builder = WebApplication.CreateBuilder(args)
Dim app = builder.Build()

app.MapGet("/hello", Function() "Hello, World!")

app.MapGet("/users/{id}", Async Function(id As Integer)
    Dim user = Await UserService.FindById(id)
    If user Is Nothing Then
        Return Results.NotFound()
    End If
    Return Results.Ok(user)
End Function)

app.Run()
```

---

## База данных
| Технология | Тип |
|------------|------|
| **Ядро Entity Framework** | Полный ОРМ |
| **Красивый** | Микро-ОРМ |
| **АДО.NET** | Низкоуровневый доступ к данным |
| **ОлеДб** | Доступ к устаревшим данным |
| **MySql.Данные** | Коннектор MySQL |
| **Нпгsql** | Коннектор PostgreSQL |
```vb
' Dapper example
Imports Dapper
Imports System.Data.SqlClient

Using conn As New SqlConnection("connection-string")
    Dim users = Await conn.QueryAsync(Of User)(
        "SELECT Id, Name, Email FROM Users WHERE Age > @Age",
        New With {.Age = 18}
    )
    For Each user In users
        Console.WriteLine($"{user.Name} ({user.Email})")
    Next
End Using
```

---

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **xUnit** | Тестовая среда |
| **NUnit** | Тестовая среда |
| **МСТест** | Платформа тестирования Microsoft |
| **Минимальный заказ** | Издевательство |
| **NSubstitute** | Издевательство |
| **FluentAssertions** | Беглые утверждения |
| **BenchmarkDotNet** | Бенчмаркинг |
```vb
' xUnit test
Imports Xunit
Imports NSubstitute

Public Class UserServiceTests
    <Fact>
    Public Async Function FindUser_ReturnsUser() As Task
        ' Arrange
        Dim repo = Substitute.For(Of IUserRepository)()
        repo.GetByIdAsync(1).Returns(New User("Alice"))
        Dim service = New UserService(repo)

        ' Act
        Dim user = Await service.FindByIdAsync(1)

        ' Assert
        Assert.Equal("Alice", user.Name)
    End Function
End Class
```

---

## Качество кода
| Инструмент | Цель |
|------|---------|
| **Анализаторы Roslyn** | Встроенный анализ |
| **Сонарный анализатор** | Правила SonarQube |
| **формат dotnet** | Форматирование кода |
| **Конфигурация редактора** | Последовательный стиль |
| **SonarQube** | Платформа качества кода |
---

## Рабочий стол (WinForms/WPF)
| Рамочная | Цель |
|-----------|---------|
| **ВинФормс** | Классические формы Windows |
| **WPF** | Современный пользовательский интерфейс Windows (XAML) |
| **МАУИ** | Кроссплатформенность (преемник Xamarin) |
| **Авалония** | Кроссплатформенный WPF-подобный |
```vb
' WinForms example
Public Class MainForm
    Inherits Form

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim name = TextBox1.Text
        MessageBox.Show($"Hello, {name}!", "Greeting")
    End Sub
End Class
```

---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **System.Text.Json** | Сериализация JSON |
| **Ньютонсофт.Json** | JSON (устаревший) |
| **Серилог** | Ведение журнала |
| **Полли** | Политика устойчивости |
| **Автомапер** | Отображение объектов |
| **FluentValidation** | Проверка |
| **Массовый транспорт** | Шина сообщений |
| **Зависание** | Фоновые вакансии |
| **Спектр.Консоль** | Пользовательский интерфейс консоли |
---

## Автоматизация офиса (VBA)
| Технология | Цель |
|------------|---------|
| **Excel VBA** | Автоматизация Excel |
| **Слово VBA** | Автоматизация слов |
| **Доступ к VBA** | Автоматизация доступа |
| **Outlook VBA** | Автоматизация Outlook |
```vb
' Excel VBA example
Sub FormatReport()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Data")
    
    ws.Range("A1:D1").Font.Bold = True
    ws.Range("A1:D1").Interior.Color = RGB(0, 112, 192)
    
    ws.Columns("A:D").AutoFit
    
    MsgBox "Report formatted successfully!"
End Sub
```

---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **Визуальная студия** | Полная версия VB.NET IDE (Community/Pro/Enterprise) |
| **Код VS** | Легкость с расширениями .NET |
| **Редактор VBA** | Встроено в приложения Office |
| **Райдер** | JetBrains (ограниченная поддержка VB) |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Автономный** | Пакеты среды выполнения .NET |
| **Зависит от платформы** | Требуется установленный .NET |
| **Один файл** | `PublishSingleFile`|
| **Докер** | Контейнерный |
| **MSI/ClickOnce** | Установщик Windows |
| **Служба приложений Azure** | Облачный хостинг |
| **ИИС** | Windows-хостинг |
---

## Краткое содержание
Экосистема Visual Basic разделяет обширную инфраструктуру .NET. Стандартный стек: **.NET 8+** в качестве среды выполнения, **Visual Studio** в качестве IDE, **ASP.NET Core** для Интернета, **Entity Framework Core** или **Dapper** для доступа к данным, **xUnit** для тестирования и **NuGet** для пакетов. VB.NET идеально подходит для разработчиков, знакомых с синтаксисом BASIC и которым необходим доступ к экосистеме .NET. **VBA** по-прежнему необходим для автоматизации Office — миллионы бизнес-пользователей полагаются на макросы Excel и Access. Экосистема лучше всего подходит для настольных приложений Windows, автоматизации Office и корпоративных бизнес-приложений.