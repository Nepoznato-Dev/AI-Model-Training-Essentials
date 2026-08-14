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
# Delphi / Object Pascal — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz Delphi/Object Pascal ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Delphi Sürümleri ve Derleyicileri
| Derleyici | Platformu | Notlar |
|----------|----------|----------|
| **Delphi 12 Atina** | Çapraz platform | En son Embarcadero sürümü |
| **Ücretsiz Pascal (FPC)** | Çapraz platform | Açık kaynaklı Pascal derleyicisi |
| **Lazarus** | Çapraz platform | Ücretsiz Pascal IDE (Delphi gibi) |
| **Delphi Topluluğu** | Windows | Ücretsiz sürüm (sınırlı) |
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

## IDE'ler
| IDE | Güçlü Yönler |
|-----|-----------|
| **Delphi IDE** | Tam özellikli RAD aracı (Embarcadero) |
| **Lazarus** | Ücretsiz, açık kaynak (FPC) |
| **VS Kodu + Pascal** | Hafif düzenleme |
---

## GUI Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **VCL** | Windows yerel | Windows masaüstü uygulamaları |
| **FireMonkey (FMX)** | Çapraz platform | Windows, macOS, iOS, Android |
| **LCL** | Çapraz platform | Lazarus Bileşen Kütüphanesi |
| **DelphiMVC** | Web | MVC çerçevesi |
| **TMS Web Çekirdeği** | Web | Delphi'den web uygulamaları |
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

## Veritabanı
| Teknoloji | Tür |
|---------------|------|
| **FireDAC** | Evrensel veritabanı erişimi (Embarcadero) |
| **dbExpress** | Hafif veritabanı |
| **ADO** | ActiveX Veri Nesneleri |
| **ZeosLib** | Açık kaynaklı veritabanı bileşenleri |
| **SQLite3** | Yerleşik SQLite desteği |
| **İnterBase** | Embarcadero'nun gömülü veritabanı |
| **Sistemler Arası IRIS** | Nesne veritabanı |
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

## Web Geliştirme
| Teknoloji | Tür |
|---------------|------|
| **DelphiMVC** | MVC web çerçevesi |
| **TMS Web Çekirdeği** | Delphi'den web uygulamaları |
| **İntraWeb** | Web uygulamaları |
| **mORMot** | REST/SOA çerçevesi |
| **Delphi-WebRTC** | Gerçek zamanlı iletişim |
| **Indy** | İnternet bileşenleri (HTTP, SMTP, vb.) |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **DUnit** | Birim testi (yerleşik) |
| **DUnitX** | Modern test çerçevesi |
| **Sahte Fabrika** | Alaycı |
| **DelphiMock** | Alaycı kütüphane |
| **FinalBuilder** | Yapı otomasyonu |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **Delphi Kodu Kapsamı** | Kod kapsamı |
| **Pascal Analizörü** | Statik analiz |
| **GEuzmanları** | IDE uzman araçları |
| **DelphiLint** | Linting |
---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **System.SysUtils** | Dize, tarih yardımcı programları |
| **Sistem.Sınıfları** | Akışlar, koleksiyonlar |
| **System.Generics** | Genel türler |
| **System.Threading** | Paralel programlama |
| **Indy** | İnternet protokolleri |
| **Sinaps** | Ağ kitaplığı |
| **Bahar4D** | Yardımcı program kütüphanesi (Boost gibi) |
| **DWScript** | Komut dosyası motoru |
| **JCL/JVCL** | Jedi kütüphanesi |
| **Grafikler32** | Grafik kütüphanesi |
| **Alcinoe** | Bileşen kütüphanesi |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Yerel Windows** | .exe dosyaları |
| **macOS** | FireMonkey uygulamaları |
| **iOS / Android** | FireMonkey mobil |
| **Linux** | Sunucu Tarafı Delphi |
| **Docker** | Konteynerde |
| **Inno Kurulumu** | Windows yükleyici |
| **NSIS** | Windows yükleyici |
---

## Özet
Delphi'nin ekosistemi masaüstü, mobil ve web için hızlı uygulama geliştirmeye (RAD) odaklanmıştır. Standart yığın şu şekildedir: IDE/derleyici olarak **Delphi 12**, Windows masaüstü için **VCL**, çapraz platform için **FireMonkey**, veritabanı erişimi için **FireDAC**, test için **DUnitX** ve yardımcı programlar için **Spring4D**. Ücretsiz alternatif **Ücretsiz Pascal** + **Lazarus**'tur. Delphi, Windows masaüstü uygulamalarında, veritabanı uygulamalarında ve hızlı prototip oluşturmada uzmandır. Ekosistem, kurumsal, sağlık ve kamu sektörlerindeki Delphi uygulamalarının geniş kurulu tabanını korumak için gereklidir.