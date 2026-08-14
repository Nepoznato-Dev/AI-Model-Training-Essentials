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
# Delphi / Object Pascal — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, frameworks, at imprastraktura sa Delphi / Object Pascal ecosystem.
---

## Mga Bersyon at Compiler ng Delphi
| Compiler | Platform | Mga Tala |
|----------|----------|-------|
| **Delphi 12 Athens** | Cross-platform | Pinakabagong paglabas ng Embarcadero |
| **Libreng Pascal (FPC)** | Cross-platform | Open-source Pascal compiler |
| **Lazarus** | Cross-platform | Libreng Pascal IDE (tulad ng Delphi) |
| **Komunidad ng Delphi** | Windows | Libreng edisyon (limitado) |
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

## mga IDE
| IDE | Mga Lakas |
|-----|-----------|
| **Delphi IDE** | Full-feature na RAD tool (Embarcadero) |
| **Lazarus** | Libre, open-source (FPC) |
| **VS Code + Pascal** | Magaan na pag-edit |
---

## GUI Frameworks
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **VCL** | Windows native | Windows desktop apps |
| **FireMonkey (FMX)** | Cross-platform | Windows, macOS, iOS, Android |
| **LCL** | Cross-platform | Lazarus Component Library |
| **DelphiMVC** | Web | MVC framework |
| **TMS Web Core** | Web | Mga web app mula sa Delphi |
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

## Database
| Teknolohiya | Uri |
|------------|------|
| **FireDAC** | Universal database access (Embarcadero) |
| **dbExpress** | Magaang database |
| **ADO** | ActiveX Data Objects |
| **ZeosLib** | Open-source na mga bahagi ng database |
| **SQLite3** | Built-in na suporta sa SQLite |
| **InterBase** | Ang naka-embed na DB ni Embarcadero |
| **InterSystems IRIS** | Bagay database |
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

## Web Development
| Teknolohiya | Uri |
|------------|------|
| **DelphiMVC** | MVC web framework |
| **TMS Web Core** | Mga web app mula sa Delphi |
| **IntraWeb** | Mga web application |
| **mORMot** | REST/SOA framework |
| **Delphi-WebRTC** | Real-time na komunikasyon |
| **Indy** | Mga bahagi ng Internet (HTTP, SMTP, atbp.) |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **DUnit** | Pagsubok ng unit (built-in) |
| **DUnitX** | Makabagong balangkas ng pagsubok |
| **MockFactory** | Nanunuya |
| **DelphiMock** | Mapanuksong library |
| **FinalBuilder** | Bumuo ng automation |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **Sakop ng Delphi Code** | Saklaw ng code |
| **Pascal Analyzer** | Static na pagsusuri |
| **GExperts** | Mga tool ng dalubhasa sa IDE |
| **DelphiLint** | Linting |
---

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **System.SysUtils** | String, date utilities |
| **System.Classes** | Mga stream, mga koleksyon |
| **System.Generics** | Mga generic na uri |
| **System.Threading** | Parallel programming |
| **Indy** | Mga protocol sa Internet |
| **Synapse** | Network library |
| **Spring4D** | Utility library (tulad ng Boost) |
| **DWScript** | Engine ng scripting |
| **JCL/JVCL** | Jedi library |
| **Graphics32** | Graphics library |
| **Alcinoe** | Component library |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Native Windows** | .exe file |
| **macOS** | Mga app ng FireMonkey |
| **iOS / Android** | FireMonkey mobile |
| **Linux** | Delphi sa gilid ng server |
| **Docker** | Naka-container |
| **Inno Setup** | Windows installer |
| **NSIS** | Windows installer |
---

## Buod
Ang ecosystem ng Delphi ay nakasentro sa mabilis na pag-unlad ng aplikasyon (RAD) para sa desktop, mobile, at web. Ang karaniwang stack ay: **Delphi 12** bilang IDE/compiler, **VCL** para sa Windows desktop, **FireMonkey** para sa cross-platform, **FireDAC** para sa access sa database, **DUnitX** para sa pagsubok, at **Spring4D** para sa mga utility. Ang libreng alternatibo ay **Libreng Pascal** + **Lazarus**. Ang Delphi ay mahusay sa Windows desktop application, database application, at mabilis na prototyping. Ang ecosystem ay mahalaga para sa pagpapanatili ng malawak na naka-install na base ng mga application ng Delphi sa enterprise, healthcare, at mga sektor ng gobyerno.