---
# Metadata
title: "C# — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the C# ecosystem including toolchains, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C# — Guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema C#/.NET.
---

## SDK de .NET y cadena de herramientas
| Herramienta | Propósito |
|------|---------|
| ** CLI puntonet ** | Construir, ejecutar, probar, publicar |
| **MSBuild** | Motor de construcción subyacente |
| ** CLI de NuGet ** | Gestión de paquetes |
| **formato dotnet** | Formato de código |
| **puntonet-ef** | Herramientas de Entity Framework |
| **dotnet-obsoleto** | Encuentra paquetes obsoletos |
| **script dotnet** | Ejecutar scripts de C# (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Tiempos de ejecución e implementaciones
| Tiempo de ejecución | Notas |
|---------|-------|
| **.NET 8/9** | LTS/STS actuales, multiplataforma |
| **.NET Framework** | Solo Windows, heredado (4.8.x) |
| **Mono** | Framework .NET de código abierto (Xamarin) |
| **Unidad (IL2CPP/Mono)** | Tiempo de ejecución del motor de juego |
| **Godot (.NET)** | Motor de juego con soporte C# |
---

## Gestión de paquetes
| Fuente | Propósito |
|--------|---------|
| **NuGet.org** | Registro oficial de paquetes |
| **añadir paquete dotnet** | Instalación del paquete CLI |
| **Referencia del paquete** | Formato .csproj moderno |
| **Feeds privadas** | Artefactos de Azure, paquetes de GitHub, MyGet |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Núcleo ASP.NET** | Web de pila completa | API, MVC, Blazor |
| **API mínimas** | Ligero | API simples |
| **Servidor Blazor** | Interfaz de usuario interactiva | SPA renderizado por servidor |
| **Asamblea web de Blazor** | Lado del cliente | SPA basado en navegador |
| **gRPC** | RPC | Servicios de alto rendimiento |
| **SeñalR** | En tiempo real | WebSockets, empujar |
| **ODatos** | Extensiones REST | API consultables |
| **Puntos finales rápidos** | Marco API | Texto repetitivo rápido y mínimo |
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

## Base de datos y ORM
| Tecnología | Tipo |
|------------|------|
| **Núcleo de Entity Framework** | ORM completo, migraciones |
| **Apuesto** | Micro-ORM, SQL sin formato |
| **NHibernar** | ORM maduro |
| **FreeSql** | ORM ligero |
| **Marta** | Base de datos de documentos PostgreSQL |
| **StackExchange.Redis** | Cliente Redis |
| **MongoDB.Controlador** | Cliente MongoDB |
| **Npgsql** | Controlador PostgreSQL |
| **ConectorMySql** | Controlador MySQL |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **xUnidad** | Marco de prueba más popular |
| **NUnidad** | Marco de prueba clásico |
| **Prueba MST** | Marco de prueba de Microsoft |
| **Pedido mínimo** | Biblioteca burlona |
| **NSustituto** | Burla amistosa |
| **Afirmaciones fluidas** | Afirmaciones fluidas |
| **Debería** | Afirmaciones legibles |
| **Falso** | Generación de datos falsos |
| **AutoFixture** | Automatización de datos de prueba |
| **Contenedores de prueba** | Pruebas de integración basadas en Docker |
| **Parámetro de referenciaDotNet** | Microbenchmarking |
| **colcha** | Cobertura de código |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **Analizadores Roslyn** | Análisis de código incorporado |
| **SonarAnalyzer.CSharp** | Reglas de SonarQube |
| **EstiloCop** | Aplicación del estilo de codificación |
| **formato dotnet** | Formato de código |
| **EditorConfiguración** | Coherencia entre editores |
| **SonarQube / SonarCloud** | Plataforma de calidad de código |
| **ReSharper** | Análisis JetBrains + refactorización |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Estudio visual** | IDE de Windows con todas las funciones (Comunidad/Pro/Empresa) |
| **Jinete** | IDE multiplataforma JetBrains C# |
| **Código VS + kit de desarrollo C#** | Ligero, extensión de Microsoft |
| **Visual Studio para Mac** | Estar jubilado (use la cláusula adicional o el código VS) |
---

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **Sistema.Texto.Json** | Serialización JSON incorporada |
| **Newtonsoft.Json** | JSON heredado (todavía se usa ampliamente) |
| **Serilog** | Registro estructurado |
| **NLog** | Marco de registro |
| **Polly** | Políticas de resiliencia y reintento |
| **MediatR** | Patrón mediador (CQRS) |
| **AutoMapeador** | Mapeo de objeto a objeto |
| **Validación de fluidez** | Biblioteca de validación |
| **Tránsito masivo** | Bus de mensajes (RabbitMQ, Azure SB) |
| **Hangfire** | Procesamiento de trabajos en segundo plano |
| **Cuarzo.NET** | Programación de trabajos |
| **Spectre.Consola** | Hermosas aplicaciones de consola |
| **CommandLineParser** | Análisis de argumentos CLI |
---

## Integración en la nube y Azure
| Servicio | Propósito |
|---------|---------|
| **Funciones de Azure** | Sin servidor |
| **SDK de Azure para .NET** | Todos los servicios de Azure |
| **SDK de AWS para .NET** | Servicios de AWS |
| **Google Cloud .NET** | Servicios de PCG |
| **Azure Cosmos DB** | Base de datos NoSQL |
| **Autobús de servicio Azure** | Mensajería |
| **Bóveda de claves de Azure** | Gestión de secretos |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Autónomo** | Paquetes de tiempo de ejecución .NET |
| **Depende del marco** | Requiere .NET instalado |
| **Publicación de un solo archivo** | `dotnet publish /p:PublishSingleFile=true`|
| **AOT nativo** | `PublishAot=true`(no se necesita JIT) |
| **Acoplador** | `mcr.microsoft.com/dotnet/aspnet`|
| **Servicio de aplicaciones Azure** | Implementación de PaaS |
| **AWS Lambda** | Sin servidor |
| **IIS** | Alojamiento de Windows |
| **Cernícalo** | Servidor web multiplataforma incorporado |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Resumen
C# y .NET ofrecen uno de los ecosistemas más productivos. La pila estándar es: **.NET 8+** como tiempo de ejecución, **ASP.NET Core** para web, **Entity Framework Core** o **Dapper** para acceso a datos, **xUnit + Moq** para pruebas, **Visual Studio** o **Rider** como IDE y **NuGet** para paquetes. El C# moderno con registros, coincidencia de patrones, tipos de referencia que aceptan valores NULL y API mínimas es conciso y expresivo. La compilación **AOT nativa** permite un inicio ultrarrápido y binarios pequeños. El ecosistema se destaca en aplicaciones empresariales, en la nube (Azure), desarrollo de juegos (Unity, Godot) y multiplataforma.