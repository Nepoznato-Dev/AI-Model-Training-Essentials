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
# Delphi / Object Pascal: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e l'infrastruttura essenziali nell'ecosistema Delphi/Object Pascal.
---

## Versioni e compilatori Delphi
| Compilatore | Piattaforma | Note |
|----------|----------|-------|
| **Delfi 12 Atene** | Multipiattaforma | Ultima versione di Embarcadero |
| **Pascal libero (FPC)** | Multipiattaforma | Compilatore Pascal open source |
| **Lazzaro** | Multipiattaforma | IDE Pascal gratuito (come Delphi) |
| **Comunità Delfi** | Finestre | Edizione gratuita (limitata) |
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
| IDE | Punti di forza |
|-----|-----------|
| **IDE Delphi** | Strumento RAD completo (Embarcadero) |
| **Lazzaro** | Gratuito, open source (FPC) |
| **Codice VS + Pascal** | Modifica leggera |
---

## Strutture GUI
| Quadro | Digitare | Ideale per |
|-----------|------|----------|
| **VCL** | Nativo di Windows | App desktop Windows |
| **FireMonkey (FMX)** | Multipiattaforma | Windows, macOS, iOS, Android |
| **LCL** | Multipiattaforma | Libreria dei componenti Lazarus |
| **DelphiMVC** | Rete | Quadro MVC |
| **TMS Web Core** | Rete | App Web da Delphi |
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

##Banca dati
| Tecnologia | Digitare |
|------------|------|
| **FireDAC** | Accesso universale al database (Embarcadero) |
| **dbExpress** | Banca dati leggera |
| **ADO** | Oggetti dati ActiveX |
| **ZeosLib** | Componenti del database open source |
| **SQLite3** | Supporto SQLite integrato |
| **InterBase** | DB incorporato di Embarcadero |
| **InterSystems IRIS** | Database oggetti |
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

##Sviluppo Web
| Tecnologia | Digitare |
|------------|------|
| **DelphiMVC** | Framework Web MVC |
| **TMS Web Core** | App Web da Delphi |
| **IntraWeb** | Applicazioni Web |
| **mORMot** | Struttura REST/SOA |
| **Delphi-WebRTC** | Comunicazione in tempo reale |
| **Indy** | Componenti Internet (HTTP, SMTP, ecc.) |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **DUnità** | Test unitario (integrato) |
| **DUnitX** | Quadro di test moderno |
| **MockFactory** | Beffardo |
| **DelphiMock** | Biblioteca beffarda |
| **FinalBuilder** | Costruisci automazione |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **Copertura del codice Delphi** | Copertura del codice |
| **Analizzatore Pascal** | Analisi statica |
| **Gesperti** | Strumenti esperti IDE |
| **DelphiLint** | Lining |
---

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **System.SysUtils** | Stringa, utilità data |
| **System.Classes** | Stream, raccolte |
| **System.Generics** | Tipi generici |
| **Threading.di sistema** | Programmazione parallela |
| **Indy** | Protocolli Internet |
| **Sinapsi** | Biblioteca di rete |
| **Primavera4D** | Libreria di utilità (come Boost) |
| **DWScript** | Motore di scripting |
| **JCL/JVCL** | Biblioteca Jedi |
| **Grafica32** | Libreria grafica |
| **Alcinoe** | Libreria dei componenti |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Windows nativo** | File .exe |
| **macOS** | App FireMonkey |
| **iOS/Android** | FireMonkey cellulare |
| **Linux** | Delphi lato server |
| **Docker** | Containerizzato |
| **Inno Setup** | Programma di installazione di Windows |
| **NSIS** | Programma di installazione di Windows |
---

## Riepilogo
L'ecosistema di Delphi è incentrato sullo sviluppo rapido di applicazioni (RAD) per desktop, dispositivi mobili e web. Lo stack standard è: **Delphi 12** come IDE/compilatore, **VCL** per desktop Windows, **FireMonkey** per multipiattaforma, **FireDAC** per l'accesso al database, **DUnitX** per i test e **Spring4D** per le utilità. L'alternativa gratuita è **Free Pascal** + **Lazarus**. Delphi eccelle nelle applicazioni desktop Windows, nelle applicazioni database e nella prototipazione rapida. L'ecosistema è essenziale per mantenere la vasta base installata di applicazioni Delphi nei settori aziendale, sanitario e governativo.