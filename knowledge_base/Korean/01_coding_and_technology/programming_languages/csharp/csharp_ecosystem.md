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
# C# — 생태계 및 도구 가이드
이 가이드에서는 C#/.NET 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## .NET SDK 및 툴체인
| 도구 | 목적 |
|------|---------|
| **닷넷 CLI** | 빌드, 실행, 테스트, 게시 |
| **MS빌드** | 기본 빌드 엔진 |
| **누겟 CLI** | 패키지 관리 |
| **닷넷 형식** | 코드 서식 |
| **dotnet-ef** | 엔터티 프레임워크 도구 |
| **dotnet-구식** | 오래된 패키지 찾기 |
| **dotnet-스크립트** | C# 스크립트(.csx) 실행 |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## 런타임 및 구현
| 런타임 | 메모 |
|---------|---------|
| **.NET 8/9** | 현재 LTS/STS, 크로스 플랫폼 |
| **.NET 프레임워크** | Windows 전용, 레거시(4.8.x) |
| **모노** | 오픈 소스 .NET Framework(Xamarin) |
| **유니티(IL2CPP/모노)** | 게임 엔진 런타임 |
| **고도(.NET)** | C#을 지원하는 게임 엔진 |
---

## 패키지 관리
| 소스 | 목적 |
|---------|---------|
| **NuGet.org** | 공식 패키지 레지스트리 |
| **dotnet 패키지 추가** | CLI 패키지 설치 |
| **패키지 참조** | 최신 .csproj 형식 |
| **비공개 피드** | Azure 아티팩트, GitHub 패키지, MyGet |
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

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **ASP.NET 코어** | 풀스택 웹 | API, MVC, Blazor |
| **최소 API** | 경량 | 간단한 API |
| **Blazor 서버** | 인터랙티브 UI | 서버 렌더링 SPA |
| **Blazor 웹어셈블리** | 클라이언트 측 | 브라우저 기반 SPA |
| **gRPC** | RPC | 고성능 서비스 |
| **시그널R** | 실시간 | WebSocket, 푸시 |
| **O데이터** | REST 확장 | 쿼리 가능한 API |
| **FastEndpoint** | API 프레임워크 | 빠르고 최소한의 상용구 |
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

## 데이터베이스 및 ORM
| 기술 | 유형 |
|------------|------|
| **엔티티 프레임워크 코어** | 전체 ORM, 마이그레이션 |
| **멋쟁이** | 마이크로 ORM, 원시 SQL |
| **N최대 절전 모드** | 성숙한 ORM |
| **FreeSql** | 경량 ORM |
| **담비** | PostgreSQL 문서 DB |
| **StackExchange.Redis** | Redis 클라이언트 |
| **MongoDB.드라이버** | 몽고DB 클라이언트 |
| **NPGSQL** | PostgreSQL 드라이버 |
| **MySql커넥터** | MySQL 드라이버 |
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

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **x유닛** | 가장 인기 있는 테스트 프레임워크 |
| **NUnit** | 클래식 테스트 프레임워크 |
| **MS테스트** | Microsoft의 테스트 프레임워크 |
| **모크** | 모의도서관 |
| **N대체** | 친절한 조롱 |
| **FluentAssertions** | 유창한 주장 |
| **반드시** | 읽을 수 있는 주장 |
| **가짜** | 가짜 데이터 생성 |
| **자동 고정장치** | 테스트 데이터 자동화 |
| **테스트 컨테이너** | Docker 기반 통합 테스트 |
| **BenchmarkDotNet** | 마이크로벤치마킹 |
| **이불** | 코드 적용 범위 |
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

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **Roslyn 분석기** | 내장 코드 분석 |
| **SonarAnalyzer.CSharp** | SonarQube 규칙 |
| **스타일캅** | 코딩 스타일 시행 |
| **닷넷 형식** | 코드 서식 |
| **편집기 구성** | 편집기 간 일관성 |
| **SonarQube / SonarCloud** | 코드 품질 플랫폼 |
| **ReSharper** | JetBrains 분석 + 리팩토링 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **비주얼 스튜디오** | 모든 기능을 갖춘 Windows IDE(Community/Pro/Enterprise) |
| **라이더** | 크로스 플랫폼 JetBrains C# IDE |
| **VS 코드 + C# 개발 키트** | 경량의 Microsoft 확장 |
| **Mac용 Visual Studio** | 은퇴 예정(Rider 또는 VS Code 사용) |
---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **시스템.텍스트.Json** | 내장 JSON 직렬화 |
| **뉴턴소프트.Json** | 레거시 JSON(여전히 널리 사용됨) |
| **세리로그** | 구조화된 로깅 |
| **NLog** | 로깅 프레임워크 |
| **폴리** | 복원력 및 재시도 정책 |
| **미디어R** | 중재자 패턴(CQRS) |
| **AutoMapper** | 개체 간 매핑 |
| **Fluent검증** | 검증 라이브러리 |
| **대중교통** | 메시지 버스(RabbitMQ, Azure SB) |
| **행파이어** | 백그라운드 작업 처리 |
| **Quartz.NET** | 채용 일정 |
| **Spectre.콘솔** | 아름다운 콘솔 앱 |
| **CommandLineParser** | CLI 인수 구문 분석 |
---

## 클라우드 및 Azure 통합
| 서비스 | 목적 |
|---------|---------|
| **Azure 기능** | 서버리스 |
| **.NET용 Azure SDK** | 모든 Azure 서비스 |
| **.NET용 AWS SDK** | AWS 서비스 |
| **구글 클라우드 .NET** | GCP 서비스 |
| **Azure Cosmos DB** | NoSQL 데이터베이스 |
| **Azure 서비스 버스** | 메시징 |
| **Azure Key Vault** | 비밀 관리 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **자체 포함** | .NET 런타임 번들 |
| **프레임워크에 따라 다름** | .NET 설치 필요 |
| **단일 파일 게시** | `dotnet publish /p:PublishSingleFile=true`|
| **네이티브 AOT** |  `PublishAot=true`(JIT 필요 없음) |
| **도커** | `mcr.microsoft.com/dotnet/aspnet`|
| **Azure 앱 서비스** | PaaS 배포 |
| **AWS 람다** | 서버리스 |
| **IIS** | Windows 호스팅 |
| **케스트렐** | 내장된 크로스 플랫폼 웹 서버 |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## 요약
C#과 .NET은 가장 생산적인 생태계 중 하나를 제공합니다. 표준 스택은 런타임으로 **.NET 8+**, 웹용 **ASP.NET Core**, 데이터 액세스용 **Entity Framework Core** 또는 **Dapper**, 테스트용 **xUnit + Moq**, IDE용 **Visual Studio** 또는 **Rider**, 패키지용 **NuGet**입니다. 레코드, 패턴 일치, null 허용 참조 유형 및 최소 API를 갖춘 최신 C#은 간결하고 표현력이 뛰어납니다. **네이티브 AOT** 컴파일을 통해 매우 빠른 시작과 작은 바이너리가 가능합니다. 생태계는 엔터프라이즈, 클라우드(Azure), 게임 개발(Unity, Godot) 및 크로스 플랫폼 애플리케이션에서 탁월합니다.