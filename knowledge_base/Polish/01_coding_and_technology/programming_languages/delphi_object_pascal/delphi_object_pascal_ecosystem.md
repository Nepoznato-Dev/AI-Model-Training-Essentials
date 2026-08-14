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
# Delphi / Object Pascal — Przewodnik po ekosystemie i narzędziach
Ten przewodnik omawia podstawowe narzędzia, frameworki i infrastrukturę w ekosystemie Delphi/Object Pascal.
---

## Wersje i kompilatory Delphi
| Kompilator | Platforma | Notatki |
|---------|-----|-------|
| **Delphi 12 Ateny** | Wieloplatformowe | Najnowsza wersja Embarcadero |
| **Darmowy Pascal (FPC)** | Wieloplatformowe | Kompilator Pascala typu open source |
| **Łazarz** | Wieloplatformowe | Darmowe Pascal IDE (jak Delphi) |
| **Społeczność Delphi** | Okna | Edycja bezpłatna (ograniczona) |
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
| IDE | Mocne strony |
|-----|-----------|
| **Środowisko Delphi** | W pełni funkcjonalne narzędzie RAD (Embarcadero) |
| **Łazarz** | Bezpłatny, open source (FPC) |
| **Kod VS + Pascal** | Lekka edycja |
---

## Ramy GUI
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **VCL** | Natywny dla systemu Windows | Aplikacje komputerowe dla systemu Windows |
| **FireMonkey (FMX)** | Wieloplatformowe | Windows, macOS, iOS, Android |
| **LCL** | Wieloplatformowe | Biblioteka komponentów Lazarusa |
| **DelphiMVC** | Sieć | framework MVC |
| **Rdzeń sieciowy TMS** | Sieć | Aplikacje internetowe firmy Delphi |
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

## Baza danych
| Technologia | Wpisz |
|------------|------|
| **FireDAC** | Uniwersalny dostęp do baz danych (Embarcadero) |
| **dbExpress** | Lekka baza danych |
| **ADO** | Obiekty danych ActiveX |
| **ZeosLib** | Składniki bazy danych typu open source |
| **SQLite3** | Wbudowana obsługa SQLite |
| **InterBase** | Wbudowany DB Embarcadero |
| **InterSystemy IRIS** | Baza obiektów |
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

## Tworzenie stron internetowych
| Technologia | Wpisz |
|------------|------|
| **DelphiMVC** | Framework sieciowy MVC |
| **Rdzeń sieciowy TMS** | Aplikacje internetowe firmy Delphi |
| **Wewnątrz sieci** | Aplikacje internetowe |
| **mORMot** | Framework REST/SOA |
| **Delphi-WebRTC** | Komunikacja w czasie rzeczywistym |
| **Indy** | Komponenty internetowe (HTTP, SMTP itp.) |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **jednostka** | Testowanie jednostkowe (wbudowane) |
| **DUnitX** | Nowoczesne ramy testowania |
| **MockFactory** | Kpiąco |
| **DelphiMock** | Kpiąca biblioteka |
| **FinalBuilder** | Buduj automatyzację |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **Zasięg kodu Delphi** | Pokrycie kodu |
| **Analizator Pascal** | Analiza statyczna |
| **GEeksperci** | Narzędzia eksperckie IDE |
| **DelphiLint** | Linting |
---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **System.SysUtils** | Ciąg znaków, narzędzia daty |
| **System.Klasy** | Strumienie, kolekcje |
| **System.Generics** | Typy ogólne |
| **System.Threading** | Programowanie równoległe |
| **Indy** | Protokoły internetowe |
| **Synapsa** | Biblioteka sieciowa |
| **Wiosna4D** | Biblioteka narzędziowa (np. Boost) |
| **Skrypt DW** | Silnik skryptowy |
| **JCL/JVCL** | Biblioteka Jedi |
| **Grafika32** | Biblioteka graficzna |
| **Alcyno** | Biblioteka komponentów |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Natywny system Windows** | pliki .exe |
| **macOS** | aplikacje FireMonkey |
| **iOS / Android** | Komórka FireMonkey |
| **Linux** | Delphi po stronie serwera |
| **Doker** | Kontenerowy |
| **Konfiguracja Inno** | Instalator Windows |
| **NSIS** | Instalator Windows |
---

## Streszczenie
Ekosystem Delphi koncentruje się na szybkim tworzeniu aplikacji (RAD) dla komputerów stacjonarnych, urządzeń mobilnych i Internetu. Standardowy stos to: **Delphi 12** jako IDE/kompilator, **VCL** dla komputerów stacjonarnych Windows, **FireMonkey** dla wielu platform, **FireDAC** dla dostępu do baz danych, **DUnitX** dla testowania i **Spring4D** dla narzędzi. Bezpłatną alternatywą jest **Free Pascal** + **Lazarus**. Delphi specjalizuje się w aplikacjach komputerowych Windows, aplikacjach bazodanowych i szybkim prototypowaniu. Ekosystem jest niezbędny do utrzymania ogromnej bazy zainstalowanych aplikacji Delphi w przedsiębiorstwach, służbie zdrowia i sektorach rządowych.