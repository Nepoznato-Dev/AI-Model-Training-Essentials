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
# Delphi / Object Pascal — エコシステムとツールのガイド
このガイドでは、Delphi / Object Pascal エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## Delphi のバージョンとコンパイラ
|コンパイラ |プラットフォーム |メモ |
|----------|----------|----------|
| **デルフィ 12 アテネ** |クロスプラットフォーム | Embarcadero の最新リリース |
| **フリー パスカル (FPC)** |クロスプラットフォーム |オープンソースの Pascal コンパイラ |
| **ラザロ** |クロスプラットフォーム | Free Pascal IDE (Delphi など) |
| **Delphi コミュニティ** |ウィンドウズ |無料版（限定版） |
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
| IDE |強み |
|-----|----------|
| **Delphi IDE** |フル機能の RAD ツール (Embarcadero) |
| **ラザロ** |無料、オープンソース (FPC) |
| **VS コード + パスカル** |軽量編集 |
---

## GUI フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **VCL** | Windows ネイティブ | Windows デスクトップ アプリ |
| **FireMonkey (FMX)** |クロスプラットフォーム | Windows、macOS、iOS、Android |
| **LCL** |クロスプラットフォーム | Lazarus コンポーネント ライブラリ |
| **DelphiMVC** |ウェブ | MVC フレームワーク |
| **TMS Web コア** |ウェブ | Delphi の Web アプリ |
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

## データベース
|テクノロジー |タイプ |
|-----------|------|
| **FireDAC** |ユニバーサル データベース アクセス (Embarcadero) |
| **dbExpress** |軽量データベース |
| **ADO** | ActiveX データ オブジェクト |
| **ゼオスリブ** |オープンソース データベース コンポーネント |
| **SQLite3** |組み込みの SQLite サポート |
| **インターベース** | Embarcadero の組み込み DB |
| **インターシステムズ IRIS** |オブジェクトデータベース |
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

## ウェブ開発
|テクノロジー |タイプ |
|-----------|------|
| **DelphiMVC** | MVC Web フレームワーク |
| **TMS Web コア** | Delphi の Web アプリ |
| **イントラウェブ** |ウェブアプリケーション |
| **mORMot** | REST/SOAフレームワーク |
| **Delphi-WebRTC** |リアルタイムコミュニケーション |
| **インディ** |インターネット コンポーネント (HTTP、SMTP など) |
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

## テスト
|フレームワーク |目的 |
|----------|----------|
| **DUnit** |単体テスト (組み込み) |
| **DUnitX** |最新のテスト フレームワーク |
| **モックファクトリー** |嘲笑 |
| **デルフィモック** |モッキングライブラリ |
| **ファイナルビルダー** |ビルドの自動化 |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **Delphi コード カバレッジ** |コードカバレッジ |
| **パスカル アナライザー** |静的解析 |
| **Gエキスパート** | IDE エキスパート ツール |
| **DelphiLint** |リンティング |
---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **System.SysUtils** |文字列、日付ユーティリティ |
| **System.Classes** |ストリーム、コレクション |
| **System.Generics** |ジェネリックタイプ |
| **システム.スレッディング** |並列プログラミング |
| **インディ** |インターネットプロトコル |
| **シナプス** |ネットワークライブラリ |
| **Spring4D** |ユーティリティ ライブラリ (Boost など) |
| **DWScript** |スクリプト エンジン |
| **JCL/JVCL** |ジェダイ図書館 |
| **グラフィック32** |グラフィックライブラリ |
| **アルシノ** |コンポーネントライブラリ |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **ネイティブ Windows** | .exe ファイル |
| **macOS** | FireMonkey アプリ |
| **iOS / Android** | FireMonkey モバイル |
| **Linux** |サーバーサイドの Delphi |
| **ドッカー** |コンテナ化 |
| **Inno セットアップ** | Windows インストーラー |
| **NSIS** | Windows インストーラー |
---

＃＃ まとめ
Delphi のエコシステムは、デスクトップ、モバイル、Web 向けの高速アプリケーション開発 (RAD) を中心としています。標準スタックは、IDE/コンパイラとして **Delphi 12**、Windows デスクトップ用に **VCL**、クロスプラットフォーム用に **FireMonkey**、データベース アクセス用に **FireDAC**、テスト用に **DUnitX**、ユーティリティ用に **Spring4D** です。無料の代替案は **Free Pascal** + **Lazarus** です。 Delphi は、Windows デスクトップ アプリケーション、データベース アプリケーション、ラピッド プロトタイピングに優れています。エコシステムは、企業、医療、政府部門における Delphi アプリケーションの広大なインストール ベースを維持するために不可欠です。