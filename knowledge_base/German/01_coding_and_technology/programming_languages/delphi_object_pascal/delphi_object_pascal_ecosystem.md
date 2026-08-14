---
# Metadata
title: "Delphi / Object Pascal — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Delphi ecosystem including IDEs, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Delphi / Object Pascal – Leitfaden für Ökosysteme und Tools
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im Delphi/Object Pascal-Ökosystem.
---

## Delphi-Versionen und Compiler
| Compiler | Plattform | Notizen |
|----------|----------|-------|
| **Delphi 12 Athen** | Plattformübergreifend | Neueste Embarcadero-Veröffentlichung |
| **Free Pascal (FPC)** | Plattformübergreifend | Open-Source-Pascal-Compiler |
| **Lazarus** | Plattformübergreifend | Kostenlose Pascal-IDE (wie Delphi) |
| **Delphi-Community** | Windows | Kostenlose Edition (limitiert) |
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

## IDEs
| IDE | Stärken |
|-----|-----------|
| **Delphi-IDE** | Voll ausgestattetes RAD-Tool (Embarcadero) |
| **Lazarus** | Kostenlos, Open-Source (FPC) |
| **VS-Code + Pascal** | Leichte Bearbeitung |
---

## GUI-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **VCL** | Windows nativ | Windows-Desktop-Apps |
| **FireMonkey (FMX)** | Plattformübergreifend | Windows, macOS, iOS, Android |
| **LCL** | Plattformübergreifend | Lazarus-Komponentenbibliothek |
| **DelphiMVC** | Web | MVC-Framework |
| **TMS Web Core** | Web | Web-Apps von Delphi |
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

## Datenbank
| Technologie | Geben Sie | ein
|------------|------|
| **FireDAC** | Universeller Datenbankzugriff (Embarcadero) |
| **dbExpress** | Leichte Datenbank |
| **ADO** | ActiveX-Datenobjekte |
| **ZeosLib** | Open-Source-Datenbankkomponenten |
| **SQLite3** | Integrierte SQLite-Unterstützung |
| **InterBase** | Embarcaderos eingebettete DB |
| **InterSystems IRIS** | Objektdatenbank |
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

## Webentwicklung
| Technologie | Geben Sie | ein
|------------|------|
| **DelphiMVC** | MVC-Webframework |
| **TMS Web Core** | Web-Apps von Delphi |
| **IntraWeb** | Webanwendungen |
| **mORMot** | REST/SOA-Framework |
| **Delphi-WebRTC** | Echtzeitkommunikation |
| **Indy** | Internetkomponenten (HTTP, SMTP usw.) |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **DUnit** | Unit-Tests (integriert) |
| **DUnitX** | Modernes Test-Framework |
| **MockFactory** | Spott |
| **DelphiMock** | Verspottungsbibliothek |
| **FinalBuilder** | Build-Automatisierung |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **Delphi-Code-Abdeckung** | Codeabdeckung |
| **Pascal-Analysator** | Statische Analyse |
| **GExperts** | IDE-Expertentools |
| **DelphiLint** | Fusseln |
---

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **System.SysUtils** | String-, Datums-Dienstprogramme |
| **System.Classes** | Streams, Sammlungen |
| **System.Generics** | Generische Typen |
| **System.Threading** | Parallele Programmierung |
| **Indy** | Internetprotokolle |
| **Synapse** | Netzwerkbibliothek |
| **Spring4D** | Utility-Bibliothek (wie Boost) |
| **DWScript** | Skript-Engine |
| **JCL/JVCL** | Jedi-Bibliothek |
| **Grafik32** | Grafikbibliothek |
| **Alcinoe** | Komponentenbibliothek |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Natives Windows** | .exe-Dateien |
| **macOS** | FireMonkey-Apps |
| **iOS / Android** | FireMonkey mobil |
| **Linux** | Serverseitiges Delphi |
| **Docker** | Containerisiert |
| **Inno-Setup** | Windows-Installer |
| **NSIS** | Windows-Installer |
---

## Zusammenfassung
Das Ökosystem von Delphi konzentriert sich auf die schnelle Anwendungsentwicklung (RAD) für Desktop, Mobilgeräte und Web. Der Standard-Stack ist: **Delphi 12** als IDE/Compiler, **VCL** für Windows-Desktop, **FireMonkey** für plattformübergreifende, **FireDAC** für Datenbankzugriff, **DUnitX** für Tests und **Spring4D** für Dienstprogramme. Die kostenlose Alternative ist **Free Pascal** + **Lazarus**. Delphi zeichnet sich durch Windows-Desktopanwendungen, Datenbankanwendungen und Rapid Prototyping aus. Das Ökosystem ist für die Aufrechterhaltung der umfangreichen installierten Basis von Delphi-Anwendungen in Unternehmen, im Gesundheitswesen und im öffentlichen Sektor von entscheidender Bedeutung.