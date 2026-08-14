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
# Delphi / Object Pascal: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema Delphi/Object Pascal.
---

## Versiones y compiladores de Delphi
| Compilador | Plataforma | Notas |
|----------|----------|-------|
| **Delfos 12 Atenas** | Multiplataforma | Último lanzamiento de Embarcadero |
| **Pascal libre (FPC)** | Multiplataforma | Compilador Pascal de código abierto |
| **Lázaro** | Multiplataforma | Pascal IDE gratuito (como Delphi) |
| **Comunidad Delphi** | Ventanas | Edición gratuita (limitada) |
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
| IDE | Fortalezas |
|-----|-----------|
| **IDE de Delphi** | Herramienta RAD con todas las funciones (Embarcadero) |
| **Lázaro** | Gratis, de código abierto (FPC) |
| **Código VS + Pascal** | Edición ligera |
---

## Marcos GUI
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **VCL** | Nativo de Windows | Aplicaciones de escritorio de Windows |
| **Mono de Fuego (FMX)** | Multiplataforma | Windows, macOS, iOS, Android |
| **LCL** | Multiplataforma | Biblioteca de componentes de Lazarus |
| **DelphiMVC** | Web | Marco MVC |
| **Núcleo web TMS** | Web | Aplicaciones web de Delphi |
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

## Base de datos
| Tecnología | Tipo |
|------------|------|
| **FuegoDAC** | Acceso universal a bases de datos (Embarcadero) |
| **dbExpress** | Base de datos ligera |
| **ADO** | Objetos de datos ActiveX |
| **ZeosLib** | Componentes de bases de datos de código abierto |
| **SQLite3** | Soporte SQLite incorporado |
| **Interbase** | Base de datos integrada de Embarcadero |
| **InterSystems IRIS** | Base de datos de objetos |
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

## Desarrollo web
| Tecnología | Tipo |
|------------|------|
| **DelphiMVC** | Marco web MVC |
| **Núcleo web TMS** | Aplicaciones web de Delphi |
| **Intraweb** | Aplicaciones web |
| **mORMot** | Marco REST/SOA |
| **Delphi-WebRTC** | Comunicación en tiempo real |
| **Indiana** | Componentes de Internet (HTTP, SMTP, etc.) |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **Unidad D** | Pruebas unitarias (integradas) |
| **DUnidadX** | Marco de prueba moderno |
| **Fábrica simulada** | Burlarse |
| **DelphiMock** | Biblioteca burlona |
| **Constructor final** | Automatización de construcciones |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **Cobertura del código Delphi** | Cobertura de código |
| **Analizador Pascal** | Análisis estático |
| **GExpertos** | Herramientas expertas IDE |
| **DelphiLint** | pelusa |
---

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **System.SysUtils** | Utilidades de cadena y fecha |
| **Clases.de.sistema** | Corrientes, colecciones |
| **Sistema.Genéricos** | Tipos genéricos |
| **Sistema.Subprocesamiento** | Programación paralela |
| **Indiana** | Protocolos de Internet |
| **Sinapsis** | Biblioteca de red |
| **Primavera4D** | Biblioteca de utilidades (como Boost) |
| **DWScript** | Motor de secuencias de comandos |
| **JCL/JVCL** | Biblioteca Jedi |
| **Gráficos32** | Biblioteca de gráficos |
| **Alcínoe** | Biblioteca de componentes |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Windows nativo** | archivos .exe |
| **macOS** | Aplicaciones de FireMonkey |
| **iOS/Android** | Móvil FireMonkey |
| **Linux** | Delphi del lado del servidor |
| **Acoplador** | En contenedores |
| **Configuración Inno** | Instalador de Windows |
| **NSIS** | Instalador de Windows |
---

## Resumen
El ecosistema de Delphi se centra en el desarrollo rápido de aplicaciones (RAD) para escritorio, dispositivos móviles y web. La pila estándar es: **Delphi 12** como IDE/compilador, **VCL** para escritorio de Windows, **FireMonkey** para multiplataforma, **FireDAC** para acceso a bases de datos, **DUnitX** para pruebas y **Spring4D** para utilidades. La alternativa gratuita es **Free Pascal** + **Lazarus**. Delphi se destaca en aplicaciones de escritorio de Windows, aplicaciones de bases de datos y creación rápida de prototipos. El ecosistema es esencial para mantener la amplia base instalada de aplicaciones Delphi en los sectores empresarial, sanitario y gubernamental.