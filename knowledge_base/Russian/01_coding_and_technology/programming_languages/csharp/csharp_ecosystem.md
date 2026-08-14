---
# Metadata
title: "C# — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the C# ecosystem including toolchains, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [csharp, ecosystem, tooling, dotnet, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C# — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы C#/.NET.
---

## .NET SDK и набор инструментов
| Инструмент | Цель |
|------|---------|
| **интерфейс командной строки dotnet** | Сборка, запуск, тестирование, публикация |
| **MSBuild** | Базовый движок сборки |
| **CLI NuGet** | Управление пакетами |
| **формат dotnet** | Форматирование кода |
| **дотнет-эф** | Инструменты Entity Framework |
| **dotnet-устарело** | Найти устаревшие пакеты |
| **dotnet-скрипт** | Запуск сценариев C# (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Среды выполнения и реализации
| Время выполнения | Заметки |
|---------|-------|
| **.NET 8/9** | Текущая LTS/STS, кроссплатформенная |
| **.NET Framework** | Только для Windows, устаревшая версия (4.8.x) |
| **Моно** | .NET Framework с открытым исходным кодом (Xamarin) |
| **Единство (IL2CPP/Моно)** | Среда выполнения игрового движка |
| **Годо (.NET)** | Игровой движок с поддержкой C# |
---

## Управление пакетами
| Источник | Цель |
|--------|---------|
| **NuGet.org** | Официальный реестр пакетов |
| **добавить пакет dotnet** | Установка пакета CLI |
| **Ссылка на пакет** | Современный формат .csproj |
| **Частные каналы** | Артефакты Azure, пакеты GitHub, MyGet |
```xml
<!-- .csproj (SDK-style) -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Dapper" Version="2.1.0" />
  </ItemGroup>
</Project>
```

---

## Веб-фреймворки
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **ASP.NET Core** | Полнофункциональный веб-интерфейс | API, MVC, Blazor |
| **Минимальные API** | Легкий | Простые API |
| **Сервер Blazor** | Интерактивный интерфейс | Серверный SPA |
| **Blazor WebAssembly** | Клиентская часть | Браузерное SPA |
| **gRPC** | РПК | Высокопроизводительные услуги |
| **СигналR** | В режиме реального времени | WebSockets, push |
| **ОДата** | Расширения REST | Запрашиваемые API |
| **Быстрые конечные точки** | API-фреймворк | Быстрый, минимальный шаблон |
```csharp
// Minimal API example
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/hello", () => "Hello, World!");
app.MapGet("/users/{id}", async (int id, UserDb db) =>
    await db.Users.FindAsync(id) is User u ? Results.Ok(u) : Results.NotFound());

app.Run();
```

---

## База данных и ORM
| Технология | Тип |
|------------|------|
| **Ядро Entity Framework** | Полная ORM, миграции |
| **Красивый** | Микро-ORM, необработанный SQL |
| **NСпящий режим** | Зрелый ОРМ |
| **FreeSql** | Легкий ОРМ |
| **Мартен** | База данных документов PostgreSQL |
| **StackExchange.Redis** | Клиент Redis |
| **MongoDB.Драйвер** | Клиент MongoDB |
| **Нпгsql** | Драйвер PostgreSQL |
| **MySqlConnector** | Драйвер MySQL |
```csharp
// EF Core example
public class AppDbContext : DbContext
{
    public DbSet<User> Users => Set<User>();
    protected override void OnConfiguring(DbContextOptionsBuilder o)
        => o.UseSqlServer("connection-string");
}

var users = await db.Users
    .Where(u => u.Age > 18)
    .OrderBy(u => u.Name)
    .ToListAsync();
```

---

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **xUnit** | Самая популярная среда тестирования |
| **NUnit** | Классический тестовый фреймворк |
| **МСТест** | Платформа тестирования Microsoft |
| **Минимальный заказ** | Издевательская библиотека |
| **NSubstitute** | Дружеское издевательство |
| **FluentAssertions** | Беглые утверждения |
| **Обязательно** | Читабельные утверждения |
| **Подделка** | Генерация фейковых данных |
| **Автофиксация** | Автоматизация тестовых данных |
| **Тестовые контейнеры** | Интеграционные тесты на основе Docker |
| **BenchmarkDotNet** | Микробенчмаркинг |
| **покрывало** | Покрытие кода |
```csharp
// xUnit + FluentAssertions
public class UserServiceTests
{
    [Fact]
    public async Task Should_Find_User_By_Id()
    {
        var mockRepo = Substitute.For<IUserRepository>();
        mockRepo.GetByIdAsync(1).Returns(new User("Alice"));
        var service = new UserService(mockRepo);

        var user = await service.GetByIdAsync(1);

        user.Name.Should().Be("Alice");
    }
}
```

---

## Качество кода
| Инструмент | Цель |
|------|---------|
| **Анализаторы Roslyn** | Встроенный анализ кода |
| **SonarAnalyzer.CSharp** | Правила SonarQube |
| **Стильный полицейский** | Обеспечение соблюдения стиля кодирования |
| **формат dotnet** | Форматирование кода |
| **Конфигурация редактора** | Межредакторская согласованность |
| **SonarQube/SonarCloud** | Платформа качества кода |
| **ReSharper** | JetBrains анализ + рефакторинг |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **Визуальная студия** | Полнофункциональная среда разработки Windows (Community/Pro/Enterprise) |
| **Райдер** | Кроссплатформенная среда разработки JetBrains C# |
| **VS Code + C# Dev Kit** | Легкое расширение Microsoft |
| **Visual Studio для Mac** | Выход на пенсию (используйте Rider или VS Code) |
---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **System.Text.Json** | Встроенная сериализация JSON |
| **Ньютонсофт.Json** | Устаревший JSON (все еще широко используется) |
| **Серилог** | Структурированное журналирование |
| **Нлог** | Система ведения журнала |
| **Полли** | Политики устойчивости и повторных попыток |
| **МедиатР** | Шаблон посредника (CQRS) |
| **Автомапер** | Сопоставление объектов с объектами |
| **FluentValidation** | Библиотека проверки |
| **Массовый транспорт** | Шина сообщений (RabbitMQ, Azure SB) |
| **Зависание** | Обработка фоновых заданий |
| **Кварц.NET** | Планирование работы |
| **Спектр.Консоль** | Красивые консольные приложения |
| **Парсер командной строки** | Анализ аргументов CLI |
---

## Интеграция облака и Azure
| Сервис | Цель |
|---------|---------|
| **Функции Azure** | Бессерверное |
| **Azure SDK для .NET** | Все службы Azure |
| **AWS SDK для .NET** | Сервисы AWS |
| **Облако Google .NET** | Услуги GCP |
| **База данных Azure Cosmos** | База данных NoSQL |
| **Служебный автобус Azure** | Обмен сообщениями |
| **Хранилище ключей Azure** | Секреты управления |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Автономный** | Пакеты среды выполнения .NET |
| **Зависит от платформы** | Требуется установленный .NET |
| **Публикация одним файлом** | `dotnet publish /p:PublishSingleFile=true`|
| **Родной AOT** | `PublishAot=true`(JIT не требуется) |
| **Докер** | `mcr.microsoft.com/dotnet/aspnet`|
| **Служба приложений Azure** | Развертывание PaaS |
| **AWS Лямбда** | Бессерверное |
| **ИИС** | Windows-хостинг |
| **Пустельга** | Встроенный кроссплатформенный веб-сервер |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Краткое содержание
C# и .NET предлагают одну из самых продуктивных экосистем. Стандартный стек: **.NET 8+** в качестве среды выполнения, **ASP.NET Core** для Интернета, **Entity Framework Core** или **Dapper** для доступа к данным, **xUnit + Moq** для тестирования, **Visual Studio** или **Rider** в качестве IDE и **NuGet** для пакетов. Современный C# с записями, сопоставлением с образцом, ссылочными типами, допускающими значение NULL, и минимальными API-интерфейсами лаконичен и выразителен. **Встроенная компиляция AOT** обеспечивает молниеносный запуск и небольшие двоичные файлы. Экосистема превосходно работает в корпоративных, облачных (Azure), разработке игр (Unity, Godot) и кроссплатформенных приложениях.