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

# Delphi / Object Pascal — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Delphi/Object Pascal.
---

## Versi & Kompiler Delphi
| Kompiler | Peron | Catatan |
|----------|----------|-------|
| **Delphi 12 Athena** | Lintas platform | Rilis Embarcadero terbaru |
| **Pascal Gratis (FPC)** | Lintas platform | Kompiler Pascal sumber terbuka |
| **Lazarus** | Lintas platform | IDE Pascal Gratis (seperti Delphi) |
| **Komunitas Delphi** | jendela | Edisi gratis (terbatas) |
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
| IDE | Kekuatan |
|-----|-----------|
| **IDE Delphi** | Alat RAD berfitur lengkap (Embarcadero) |
| **Lazarus** | Gratis, sumber terbuka (FPC) |
| **Kode VS + Pascal** | Pengeditan ringan |
---

## Kerangka GUI
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **VCL** | Windows asli | Aplikasi desktop Windows |
| **Monyet Api (FMX)** | Lintas platform | Windows, macOS, iOS, Android |
| **LCL** | Lintas platform | Perpustakaan Komponen Lazarus |
| **DelphiMVC** | jaringan | Kerangka kerja MVC |
| **Inti WebTMS** | jaringan | Aplikasi web dari Delphi |
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

## Basis Data
| Teknologi | Ketik |
|------------|------|
| **FireDAC** | Akses basis data universal (Embarcadero) |
| **dbEkspres** | Basis data ringan |
| **LAKUKAN** | Objek Data ActiveX |
| **ZeosLib** | Komponen database sumber terbuka |
| **SQLite3** | Dukungan SQLite bawaan |
| **AntarBase** | DB tertanam Embarcadero |
| **IRIS AntarSistem** | Basis data objek |
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

## Pengembangan Web
| Teknologi | Ketik |
|------------|------|
| **DelphiMVC** | Kerangka web MVC |
| **Inti WebTMS** | Aplikasi web dari Delphi |
| **IntraWeb** | Aplikasi web |
| **mORMot** | Kerangka kerja REST/SOA |
| **Delphi-WebRTC** | Komunikasi waktu nyata |
| **India** | Komponen Internet (HTTP, SMTP, dll) |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Satuan** | Pengujian unit (bawaan) |
| **DUnitX** | Kerangka pengujian modern |
| **Pabrik Tiruan** | Mengejek |
| **DelphiMock** | Perpustakaan mengejek |
| **Pembangun Akhir** | Bangun otomatisasi |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **Cakupan Kode Delphi** | Cakupan kode |
| **Penganalisis Pascal** | Analisis statis |
| **GPakar** | Alat ahli IDE |
| **DelphiLint** | Linting |
---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Sistem.SysUtils** | String, utilitas tanggal |
| **Sistem.Kelas** | Aliran, koleksi |
| **Sistem.Generik** | Tipe generik |
| **Sistem.Threading** | Pemrograman paralel |
| **India** | Protokol Internet |
| **Sinapsis** | Perpustakaan jaringan |
| **Musim Semi4D** | Pustaka utilitas (seperti Boost) |
| **Skrip DW** | Mesin skrip |
| **JCL/JVCL** | Perpustakaan Jedi |
| **Grafik32** | Perpustakaan grafis |
| **Alcinoe** | Perpustakaan komponen |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Jendela Asli** | file .exe |
| **macOS** | Aplikasi FireMonkey |
| **iOS/Android** | Ponsel FireMonkey |
| **Linux** | Delphi sisi server |
| **Buruh pelabuhan** | dalam kontainer |
| **Pengaturan Inno** | Pemasang Windows |
| **NSIS** | Pemasang Windows |
---

## Ringkasan
Ekosistem Delphi berpusat pada pengembangan aplikasi cepat (RAD) untuk desktop, seluler, dan web. Tumpukan standarnya adalah: **Delphi 12** sebagai IDE/kompiler, **VCL** untuk desktop Windows, **FireMonkey** untuk lintas platform, **FireDAC** untuk akses database, **DUnitX** untuk pengujian, dan **Spring4D** untuk utilitas. Alternatif gratisnya adalah **Pascal Gratis** + **Lazarus**. Delphi unggul dalam aplikasi desktop Windows, aplikasi database, dan pembuatan prototipe cepat. Ekosistem ini penting untuk mempertahankan basis aplikasi Delphi yang terinstal secara luas di sektor perusahaan, layanan kesehatan, dan pemerintahan.