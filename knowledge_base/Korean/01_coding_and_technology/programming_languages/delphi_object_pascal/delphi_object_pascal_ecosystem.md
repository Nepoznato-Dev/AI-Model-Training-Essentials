<!--
---
# Metadata
title: "Delphi / Object Pascal — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Delphi ecosystem including IDEs, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [delphi, pascal, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Delphi/오브젝트 파스칼 — 생태계 및 툴링 가이드
이 가이드는 Delphi/오브젝트 파스칼 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 델파이 버전 및 컴파일러
| 컴파일러 | 플랫폼 | 메모 |
|----------|----------|-------|
| **델파이 12 아테네** | 크로스 플랫폼 | 최신 Embarcadero 릴리스 |
| **프리 파스칼(FPC)** | 크로스 플랫폼 | 오픈 소스 파스칼 컴파일러 |
| **나사로** | 크로스 플랫폼 | 무료 Pascal IDE(Delphi와 유사) |
| **델파이 커뮤니티** | 윈도우 | 무료 버전(한정) |
```bash
# Free Pascal
fpc -version              # check version
fpc program.pas           # compile
fpc -Mobjfpc program.pas  # Object Pascal mode

# DCC32/DCC64 (Delphi command-line)
dcc32 project.dpr         # 32-bit compile
dcc64 project.dpr         # 64-bit compile
```

---

## IDE
| IDE | 강점 |
|------|------------|
| **델파이 IDE** | 모든 기능을 갖춘 RAD 도구(Embarcadero) |
| **나사로** | 무료 오픈 소스(FPC) |
| **VS 코드 + 파스칼** | 간단한 편집 |
---

## GUI 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **VCL** | Windows 기본 | Windows 데스크톱 앱 |
| **파이어몽키(FMX)** | 크로스 플랫폼 | 윈도우, 맥OS, iOS, 안드로이드 |
| **LCL** | 크로스 플랫폼 | 라자루스 구성 요소 라이브러리 |
| **델파이MVC** | 웹 | MVC 프레임워크 |
| **TMS 웹 코어** | 웹 | Delphi의 웹 앱 |
```pascal
// VCL example
procedure TForm1.Button1Click(Sender: TObject);
var
  UserName: string;
begin
  UserName := Edit1.Text;
  ShowMessage('Hello, ' + UserName + '!');
end;

// FireMonkey (cross-platform)
procedure TForm1.Button1Click(Sender: TObject);
begin
  ShowMessage('Hello from ' + TOSVersion.Platform.ToString);
end;
```

---

## 데이터베이스
| 기술 | 유형 |
|------------|------|
| **FireDAC** | 범용 데이터베이스 액세스(Embarcadero) |
| **dbExpress** | 경량 데이터베이스 |
| **아도** | ActiveX 데이터 개체 |
| **제오스립** | 오픈 소스 데이터베이스 구성 요소 |
| **SQLite3** | 내장된 SQLite 지원 |
| **인터베이스** | Embarcadero의 임베디드 DB |
| **인터시스템즈 IRIS** | 객체 데이터베이스 |
```pascal
// FireDAC example
var
  FDConn: TFDConnection;
  FDQuery: TFDQuery;
begin
  FDConn := TFDConnection.Create(nil);
  FDConn.DriverName := 'SQLite';
  FDConn.Params.Database := 'mydb.sqlite';
  FDConn.Connected := True;

  FDQuery := TFDQuery.Create(nil);
  FDQuery.Connection := FDConn;
  FDQuery.SQL.Text := 'SELECT * FROM users WHERE age > :age';
  FDQuery.ParamByName('age').AsInteger := 18;
  FDQuery.Open;

  while not FDQuery.Eof do
  begin
    WriteLn(FDQuery.FieldByName('name').AsString);
    FDQuery.Next;
  end;
end;
```

---

## 웹 개발
| 기술 | 유형 |
|------------|------|
| **델파이MVC** | MVC 웹 프레임워크 |
| **TMS 웹 코어** | Delphi의 웹 앱 |
| **인트라웹** | 웹 애플리케이션 |
| **모못** | REST/SOA 프레임워크 |
| **델파이-WebRTC** | 실시간 소통 |
| **인디** | 인터넷 구성요소(HTTP, SMTP 등) |
```pascal
// DelphiMVC controller
type
  [MVCPath('/api')]
  TUserController = class(TController)
  public
    [MVCPath('/users')]
    [MVCHTTPMethods([httpGET])]
    procedure GetUsers(Ctx: THttpContextBase);

    [MVCPath('/users/($id)')]
    [MVCHTTPMethods([httpGET])]
    procedure GetUser(Ctx: THttpContextBase);
  end;

procedure TUserController.GetUsers(Ctx: THttpContextBase);
var
  Users: TObjectList<TUser>;
begin
  Users := UserService.GetAll;
  Ctx.RenderObject(Users);
end;
```

---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **DUnit** | 단위 테스트(내장) |
| **DUnitX** | 최신 테스트 프레임워크 |
| **모의공장** | 조롱 |
| **DelphiMock** | 모의도서관 |
| **최종 빌더** | 자동화 구축 |
```pascal
// DUnitX example
uses DUnitX.TestFramework;

type
  [TestFixture]
  TUserServiceTest = class
  public
    [Test]
    procedure TestFindUser;
    [Test]
    procedure TestUserNotFound;
  end;

procedure TUserServiceTest.TestFindUser;
var
  Service: TUserService;
  User: TUser;
begin
  Service := TUserService.Create;
  try
    User := Service.Find(1);
    Assert.AreEqual('Alice', User.Name);
  finally
    Service.Free;
  end;
end;
```

---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **델파이 코드 적용 범위** | 코드 적용 범위 |
| **파스칼 분석기** | 정적 분석 |
| **G전문가** | IDE 전문가 도구 |
| **델파이린트** | 린팅 |
---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **시스템.SysUtils** | 문자열, 날짜 유틸리티 |
| **시스템.클래스** | 스트림, 컬렉션 |
| **시스템.제네릭** | 일반 유형 |
| **시스템.스레딩** | 병렬 프로그래밍 |
| **인디** | 인터넷 프로토콜 |
| **시냅스** | 네트워크 라이브러리 |
| **스프링4D** | 유틸리티 라이브러리(예: Boost) |
| **DW스크립트** | 스크립팅 엔진 |
| **JCL/JVCL** | 제다이 도서관 |
| **그래픽32** | 그래픽 라이브러리 |
| **알시노** | 구성요소 라이브러리 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **기본 Windows** | .exe 파일 |
| **맥OS** | 파이어몽키 앱 |
| **iOS/안드로이드** | 파이어몽키 모바일 |
| **리눅스** | 서버측 델파이 |
| **도커** | 컨테이너화 |
| **이노 설정** | Windows 설치 프로그램 |
| **NSIS** | Windows 설치 프로그램 |
---

## 요약
Delphi의 에코시스템은 데스크탑, 모바일 및 웹을 위한 신속한 애플리케이션 개발(RAD)에 중점을 두고 있습니다. 표준 스택은 IDE/컴파일러인 **Delphi 12**, Windows 데스크톱용 **VCL**, 크로스 플랫폼용 **FireMonkey**, 데이터베이스 액세스용 **FireDAC**, 테스트용 **DUnitX**, 유틸리티용 **Spring4D**입니다. 무료 대안은 **Free Pascal** + **Lazarus**입니다. Delphi는 Windows 데스크톱 애플리케이션, 데이터베이스 애플리케이션 및 신속한 프로토타이핑에 탁월합니다. 생태계는 기업, 의료, 정부 부문에서 Delphi 애플리케이션의 방대한 설치 기반을 유지하는 데 필수적입니다.