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
# C# — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais no ecossistema C#/.NET.
---

## SDK e conjunto de ferramentas do .NET
| Ferramenta | Finalidade |
|------|---------|
| **CLI dotnet** | Construa, execute, teste, publique |
| **MSBuild** | Mecanismo de construção subjacente |
| **CLI do NuGet** | Gestão de pacotes |
| **formato dotnet** | Formatação de código |
| **dotnet-ef** | Ferramentas do Entity Framework |
| **dotnet desatualizado** | Encontre pacotes desatualizados |
| **dotnet-script** | Execute scripts C# (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Tempos de execução e implementações
| Tempo de execução | Notas |
|--------|-------|
| **.NET 8/9** | LTS/STS atual, plataforma cruzada |
| **.NET Framework** | Somente Windows, legado (4.8.x) |
| **Mono** | .NET Framework de código aberto (Xamarin) |
| **Unidade (IL2CPP/Mono)** | Tempo de execução do motor de jogo |
| **Godot (.NET)** | Motor de jogo com suporte a C# |
---

## Gerenciamento de pacotes
| Fonte | Finalidade |
|--------|---------|
| **NuGet.org** | Registro oficial de pacotes |
| **dotnet adicionar pacote** | Instalação do pacote CLI |
| **Referência do pacote** | Formato .csproj moderno |
| **Feeds privados** | Artefatos do Azure, pacotes GitHub, MyGet |
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

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **ASP.NET Core** | Web full-stack | APIs, MVC, Blazor |
| **APIs mínimas** | Leve | APIs simples |
| **Servidor Blazor** | UI interativa | SPA renderizado por servidor |
| **Blazor WebAssembly** | Lado do cliente | SPA baseado em navegador |
| **gRPC** | RPC | Serviços de alto desempenho |
| **SinalR** | Em tempo real | WebSockets, empurre |
| **Dados** | Extensões REST | APIs consultáveis ​​|
| **FastEndpoints** | Estrutura de API | Padrão rápido e mínimo |
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

## Banco de dados e ORM
| Tecnologia | Tipo |
|------------|------|
| **Núcleo do Entity Framework** | ORM completo, migrações |
| **Elegante** | Micro-ORM, SQL bruto |
| **NHibernar** | ORM maduro |
| **FreeSql** | ORM leve |
| **Marta** | Banco de dados de documentos PostgreSQL |
| **StackExchange.Redis** | Cliente Redis |
| **MongoDB.Driver** | Cliente MongoDB |
| **Npgsql** | Driver PostgreSQL |
| **MySqlConnector** | Driver MySQL |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **xUnidade** | Estrutura de teste mais popular |
| **NUunidade** | Estrutura de teste clássica |
| **MSTest** | Estrutura de teste da Microsoft |
| **Quantidade mínima** | Biblioteca zombando |
| **NSubstituto** | Zombaria amigável |
| **Asserções Fluentes** | Afirmações fluentes |
| **Deveria** | Asserções legíveis |
| **Falso** | Geração de dados falsos |
| **AutoFixtura** | Automação de dados de teste |
| **Contêineres de teste** | Testes de integração baseados em Docker |
| **BenchmarkDotNet** | Microbenchmarking |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **Analisadores Roslyn** | Análise de código integrada |
| **SonarAnalyzer.CSharp** | Regras do SonarQube |
| **EstiloCop** | Aplicação do estilo de codificação |
| **formato dotnet** | Formatação de código |
| **EditorConfig** | Consistência entre editores |
| **SonarQube/SonarCloud** | Plataforma de qualidade de código |
| **ReSharper** | Análise JetBrains + refatoração |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Estúdio Visual** | IDE do Windows completo (Community/Pro/Enterprise) |
| **Cavaleiro** | IDE JetBrains C# multiplataforma |
| **Código VS + Kit de desenvolvimento C#** | Extensão leve da Microsoft |
| **Visual Studio para Mac** | Estar aposentado (use Rider ou VS Code) |
---

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **System.Text.Json** | Serialização JSON integrada |
| **Newtonsoft.Json** | JSON legado (ainda amplamente utilizado) |
| **Serilog** | Registro estruturado |
| **NLog** | Estrutura de registro |
| **Polly** | Políticas de resiliência e novas tentativas |
| **MediatR** | Padrão mediador (CQRS) |
| **AutoMapper** | Mapeamento objeto a objeto |
| **Validação Fluente** | Biblioteca de validação |
| **Trânsito de massa** | Barramento de mensagens (RabbitMQ, Azure SB) |
| **Hangfire** | Processamento de trabalho em segundo plano |
| **Quartzo.NET** | Agendamento de trabalho |
| **Spectre.Console** | Lindos aplicativos de console |
| **CommandLineParser** | Análise de argumento CLI |
---

## Integração em nuvem e Azure
| Serviço | Finalidade |
|--------|---------|
| **Funções do Azure** | Sem servidor |
| **SDK do Azure para .NET** | Todos os serviços do Azure |
| **AWS SDK para .NET** | Serviços AWS |
| **Google Cloud .NET** | Serviços GCP |
| **Azure Cosmos DB** | Banco de dados NoSQL |
| **Barramento de serviço do Azure** | Mensagens |
| **Cofre de Chaves do Azure** | Gestão de segredos |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Autônomo** | Pacotes de tempo de execução .NET |
| **Dependente da estrutura** | Requer .NET instalado |
| **Publicação de arquivo único** | `dotnet publish /p:PublishSingleFile=true`|
| **AOT nativo** | `PublishAot=true`(sem necessidade de JIT) |
| **Docker** | `mcr.microsoft.com/dotnet/aspnet`|
| **Serviço de Aplicativo do Azure** | Implantação de PaaS |
| **AWS Lambda** | Sem servidor |
| **IIS** | Hospedagem Windows |
| **Francelho** | Servidor web multiplataforma integrado |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Resumo
C# e .NET oferecem um dos ecossistemas mais produtivos. A pilha padrão é: **.NET 8+** como tempo de execução, **ASP.NET Core** para web, **Entity Framework Core** ou **Dapper** para acesso a dados, **xUnit + Moq** para testes, **Visual Studio** ou **Rider** como IDE e **NuGet** para pacotes. C# moderno com registros, correspondência de padrões, tipos de referência anuláveis ​​e APIs mínimas é conciso e expressivo. A compilação **AOT nativa** permite uma inicialização extremamente rápida e pequenos binários. O ecossistema é excelente em aplicativos corporativos, em nuvem (Azure), de jogos (Unity, Godot) e de plataforma cruzada.