---
# Metadata
title: "Delphi / Object Pascal"
description: "Comprehensive reference for the Delphi/Object Pascal programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [delphi-object-pascal, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "44 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Delphi / オブジェクト パスカル
Delphi は、Pascal をベースにしたオブジェクト指向プログラミング言語で、元々は Borland (後の Embarcadero、現在は Idera) によって開発されました。 1995 年に「Delphi 1」として初めてリリースされ、Windows デスクトップ アプリケーションの高速アプリケーション開発 (RAD) のために設計されました。この言語は正式には Object Pascal として知られており、Delphi IDE はビジュアル フォーム デザイナー、統合データベース ツール、および強力なコンパイラを提供します。
Delphi は、1990 年代後半から 2000 年代前半に最も人気のある Windows 開発ツールの 1 つでした。その人気は大幅に低下しましたが、特にエンタープライズ デスクトップ アプリケーション、データベース フロントエンド、レガシー システムのメンテナンスにおいて、専用のユーザー ベースを維持しています。 Modern Delphi (11/12) は、FireMonkey (FMX) フレームワークを通じて、Windows、macOS、iOS、Android のクロスプラットフォーム開発をサポートします。
---

## Delphi が重要な理由
- **迅速なアプリケーション開発**: ビジュアル フォーム デザイナー + ネイティブ コンパイルにより、Windows GUI の構築が非常に高速になりました。
- **ネイティブ パフォーマンス**: マシン コードに直接コンパイルします。ランタイムや VM は必要ありません。
- **データベース接続**: 歴史的に優れたデータベース コンポーネント (dbExpress、FireDAC、ADO)。
- **レガシー コードベース**: 多くのエンタープライズ アプリケーションは依然として Delphi 上で実行されます。メンテナンスはニッチなスキルです。
- **クロスプラットフォーム (最新)**: FireMonkey フレームワークは、単一のコードベースから Windows、macOS、iOS、Android をターゲットとしています。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **衰退するコミュニティ** | C#、Java、または JavaScript コミュニティよりもはるかに小さい |活発だが小規模なフォーラム。 Idera からの商用サポート |
| **限られたエコシステム** |最新の言語よりもサードパーティのライブラリが少ない | VCL/FMX コンポーネント ライブラリを使用します。カスタムコンポーネントを書く |
| **主に Windows に重点を置いています** |クロスプラットフォーム サポート (FMX) はまだ成熟していません。 C#、Flutter、または Web テクノロジを使用して真のクロスプラットフォームを実現 |
| **ライセンス費用** |商用 IDE には有料ライセンスが必要です |オープンソースの代替案: Free Pascal / Lazarus |
| **採用の難しさ** |市場に参入する Delphi 開発者の減少 |既存のシステムを維持します。新しい機能を最新のスタックに移行する |
---

## 構文の基礎
```pascal
program HelloWorld;

{$APPTYPE CONSOLE}

uses
  SysUtils;

var
  Name: string;
  Age: Integer;
  Score: Double;

// Procedure (no return value)
procedure Greet(const AName: string);
begin
  WriteLn('Hello, ' + AName + '!');
end;

// Function (returns a value)
function Add(A, B: Integer): Integer;
begin
  Result := A + B;
end;

// Object-oriented programming
type
  TAnimal = class
  private
    FName: string;
  public
    constructor Create(const AName: string);
    function Speak: string; virtual; abstract;
    property Name: string read FName;
  end;

  TDog = class(TAnimal)
  public
    function Speak: string; override;
  end;

constructor TAnimal.Create(const AName: string);
begin
  inherited Create;
  FName := AName;
end;

function TDog.Speak: string;
begin
  Result := Name + ' says woof';
end;

// Main program
begin
  Name := 'Alice';
  Age := 30;
  Score := 9.5;
  
  Greet(Name);
  WriteLn('Sum: ', Add(3, 5));
  
  ReadLn;  // Wait for Enter
end.
```

---

## 高度な構文とパターン
### ジェネリックとコレクション
Delphi はジェネリックスをサポートしており (Delphi 2009 以降)、タイプセーフなコンテナ クラスを有効にします。
```pascal
unit GenericsDemo;

interface

uses
  System.Generics.Collections,
  System.Generics.Defaults,
  SysUtils;

type
  // Generic pair class
  TPair<TKey, TValue> = class
  private
    FKey: TKey;
    FValue: TValue;
  public
    constructor Create(const AKey: TKey; const AValue: TValue);
    property Key: TKey read FKey;
    property Value: TValue read FValue;
  end;

  // Generic stack implementation
  TStack<T> = class
  private
    FItems: TList<T>;
  public
    constructor Create;
    destructor Destroy; override;
    procedure Push(const AItem: T);
    function Pop: T;
    function Peek: T;
    function Count: Integer;
  end;

  // Custom comparer for sorting
  TEmployeeComparer = class(TComparer<TObject>)
  public
    function Compare(const Left, Right: TObject): Integer; override;
  end;

implementation

{ TStack<T> }

constructor TStack<T>.Create;
begin
  inherited Create;
  FItems := TList<T>.Create;
end;

destructor TStack<T>.Destroy;
begin
  FItems.Free;
  inherited;
end;

procedure TStack<T>.Push(const AItem: T);
begin
  FItems.Add(AItem);
end;

function TStack<T>.Pop: T;
begin
  if FItems.Count = 0 then
    raise Exception.Create('Stack is empty');
  Result := FItems[FItems.Count - 1];
  FItems.Delete(FItems.Count - 1);
end;

function TStack<T>.Peek: T;
begin
  if FItems.Count = 0 then
    raise Exception.Create('Stack is empty');
  Result := FItems[FItems.Count - 1];
end;

function TStack<T>.Count: Integer;
begin
  Result := FItems.Count;
end;

end.
```

### 匿名メソッドとクロージャ
```pascal
program AnonymousMethods;

{$APPTYPE CONSOLE}

uses
  SysUtils, System.Generics.Collections;

type
  TIntFunction = reference to function(X: Integer): Integer;
  TVoidProc = reference to procedure(const AMsg: string);

var
  Square: TIntFunction;
  Logger: TVoidProc;
  Counter: TProc;

begin
  // Anonymous method — inline function
  Square := function(X: Integer): Integer
  begin
    Result := X * X;
  end;
  WriteLn('5 squared = ', Square(5));

  // Closure — captures outer variable
  // The Count variable persists between calls
  var Count: Integer := 0;
  Counter := procedure
  begin
    Inc(Count);
    WriteLn('Call count: ', Count);
  end;
  Counter;  // Call count: 1
  Counter;  // Call count: 2
  Counter;  // Call count: 3

  // Using anonymous methods with collections
  var Numbers := TList<Integer>.Create;
  try
    Numbers.AddRange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

    // Filter: keep only even numbers
    var Evens := TList<Integer>.Create;
    try
      Numbers.ForEach(
        procedure(const N: Integer)
        begin
          if N mod 2 = 0 then
            Evens.Add(N);
        end
      );
      Write('Even numbers: ');
      for var N in Evens do
        Write(N, ' ');
      WriteLn;
    finally
      Evens.Free;
    end;
  finally
    Numbers.Free;
  end;

  ReadLn;
end.
```

### インターフェースと依存関係の注入
```pascal
unit DIExample;

interface

uses
  SysUtils;

type
  // Interface definitions
  ILogger = interface
    ['{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}']
    procedure Log(const AMessage: string);
  end;

  IRepository = interface
    ['{B2C3D4E5-F6A7-8901-BCDE-F12345678901}']
    function FindById(const AId: Integer): string;
    procedure Save(const AData: string);
  end;

  // Concrete implementations
  TFileLogger = class(TInterfacedObject, ILogger)
  public
    procedure Log(const AMessage: string);
  end;

  TConsoleLogger = class(TInterfacedObject, ILogger)
  public
    procedure Log(const AMessage: string);
  end;

  TDatabaseRepository = class(TInterfacedObject, IRepository)
  private
    FLogger: ILogger;
  public
    constructor Create(const ALogger: ILogger);
    function FindById(const AId: Integer): string;
    procedure Save(const AData: string);
  end;

  // Service class using dependency injection
  TUserService = class
  private
    FRepository: IRepository;
    FLogger: ILogger;
  public
    constructor Create(const ARepo: IRepository; const ALogger: ILogger);
    procedure CreateUser(const AName: string);
  end;

implementation

{ TFileLogger }
procedure TFileLogger.Log(const AMessage: string);
begin
  // Write to log file
  WriteLn('[FILE LOG] ', AMessage);
end;

{ TConsoleLogger }
procedure TConsoleLogger.Log(const AMessage: string);
begin
  WriteLn('[CONSOLE] ', AMessage);
end;

{ TDatabaseRepository }
constructor TDatabaseRepository.Create(const ALogger: ILogger);
begin
  inherited Create;
  FLogger := ALogger;
end;

function TDatabaseRepository.FindById(const AId: Integer): string;
begin
  FLogger.Log('Finding record ' + IntToStr(AId));
  Result := 'Record_' + IntToStr(AId);
end;

procedure TDatabaseRepository.Save(const AData: string);
begin
  FLogger.Log('Saving: ' + AData);
end;

{ TUserService }
constructor TUserService.Create(const ARepo: IRepository; const ALogger: ILogger);
begin
  FRepository := ARepo;
  FLogger := ALogger;
end;

procedure TUserService.CreateUser(const AName: string);
begin
  FLogger.Log('Creating user: ' + AName);
  FRepository.Save(AName);
end;

end.
```

### VCL コンポーネント パターン
```pascal
unit MainForm;

interface

uses
  Winapi.Windows, Winapi.Messages,
  System.SysUtils, System.Classes,
  Vcl.Graphics, Vcl.Controls, Vcl.Forms,
  Vcl.Dialogs, Vcl.StdCtrls, Vcl.ExtCtrls,
  Vcl.Grids, Vcl.DBGrids, Data.DB;

type
  TfrmMain = class(TForm)
    pnlTop: TPanel;
    btnSearch: TButton;
    btnExport: TButton;
    edtSearch: TEdit;
    dbgResults: TDBGrid;
    StatusBar: TStatusBar;
    procedure FormCreate(Sender: TObject);
    procedure btnSearchClick(Sender: TObject);
    procedure btnExportClick(Sender: TObject);
    procedure dbgResultsDblClick(Sender: TObject);
  private
    procedure SetupDataSet;
    procedure FilterData(const ASearchText: string);
    procedure ExportToCSV(const AFileName: string);
    procedure UpdateStatusBar(const AMessage: string);
  public
    { Public declarations }
  end;

var
  frmMain: TfrmMain;

implementation

{$R *.dfm}

procedure TfrmMain.FormCreate(Sender: TObject);
begin
  SetupDataSet;
  UpdateStatusBar('Ready');
end;

procedure TfrmMain.btnSearchClick(Sender: TObject);
begin
  if Trim(edtSearch.Text) = '' then
  begin
    ShowMessage('Please enter a search term');
    edtSearch.SetFocus;
    Exit;
  end;
  FilterData(edtSearch.Text);
  UpdateStatusBar('Search complete');
end;

procedure TfrmMain.btnExportClick(Sender: TObject);
begin
  ExportToCSV('export_' + FormatDateTime('yyyymmdd', Now) + '.csv');
  UpdateStatusBar('Export complete');
end;

procedure TfrmMain.dbgResultsDblClick(Sender: TObject);
begin
  ShowMessage('Selected: ' + dbgResults.Fields[1].AsString);
end;

procedure TfrmMain.SetupDataSet;
begin
  // Configure dataset and connect to DBGrid
  StatusBar.SimpleText := 'Initializing...';
end;

procedure TfrmMain.FilterData(const ASearchText: string);
begin
  // Apply filter to dataset
end;

procedure TfrmMain.ExportToCSV(const AFileName: string);
begin
  // Export DBGrid data to CSV file
end;

procedure TfrmMain.UpdateStatusBar(const AMessage: string);
begin
  StatusBar.SimpleText := AMessage;
end;

end.
```

---

## アーキテクチャとシステム設計
### コンポーネントのアーキテクチャ
Delphi の VCL (Visual Component Library) と FMX (FireMonkey) はコンポーネント階層に基づいて構築されています。すべての視覚要素は`TComponent`から継承します。
```
TObject
└── TPersistent
    └── TComponent
        ├── TControl
        │   ├── TWinControl
        │   │   ├── TForm          (window/form)
        │   │   ├── TButton        (push button)
        │   │   ├── TEdit          (text input)
        │   │   ├── TPanel         (container panel)
        │   │   ├── TDBGrid        (database grid)
        │   │   └── TListBox       (list box)
        │   └── TGraphicControl
        │       ├── TLabel         (text label)
        │       ├── TImage         (image display)
        │       └── TShape         (geometric shapes)
        ├── TDataSet               (database dataset base)
        │   ├── TFDQuery           (FireDAC query)
        │   ├── TClientDataSet     (in-memory dataset)
        │   └── TADODataSet        (ADO database)
        └── TDataModule            (non-visual container)
```

### 一般的なプロジェクトのディレクトリ構造
```
delphi-project/
├── src/
│   ├── Project.dpr              * Main project file
│   ├── MainForm.pas             * Main form unit
│   ├── MainForm.dfm             * Main form definition (binary)
│   ├── MainForm.fmx             * FMX form definition (text XML)
│   ├── DataModule.pas           * Data access module
│   ├── BusinessLogic.pas        * Business logic unit
│   └── Utils.pas                * Utility functions
├── packages/
│   ├── CustomComponents.bpl     * Component package
│   └── CustomComponents.dpk     * Package source
├── lib/                         * Compiled units
├── dcu/                         * Delphi compiled units
├── resources/
│   ├── images/                  * Application images
│   └── icons/                   * Application icons
├── Project.dproj                * Project configuration (XML)
└── README.md
```

### .dproj プロジェクト ファイル
```xml
<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
    <PropertyGroup>
        <ProjectGuid>{12345678-ABCD-EF01-2345-6789ABCDEF01}</ProjectGuid>
        <MainSource>Project.dpr</MainSource>
        <Base>True</Base>
        <Config Condition="'$(Config)'==''">Debug</Config>
        <Platform>Win32</Platform>
        <AppType>Application</AppType>
        <FrameworkType>VCL</FrameworkType>
        <DCC_DCCCompiler>DCC32</DCC_DCCCompiler>
    </PropertyGroup>
    <PropertyGroup Condition="'$(Config)'=='Base'">
        <Base>true</Base>
    </PropertyGroup>
    <PropertyGroup Condition="'$(Config)'=='Debug'">
        <DCC_Optimize>false</DCC_Optimize>
        <DCC_GenerateStackFrames>true</DCC_GenerateStackFrames>
        <DCC_DebugDCUs>true</DCC_DebugDCUs>
    </PropertyGroup>
    <PropertyGroup Condition="'$(Config)'=='Release'">
        <DCC_Optimize>true</DCC_Optimize>
        <DCC_DebugInformation>0</DCC_DebugInformation>
        <DCC_LocalDebugSymbols>false</DCC_LocalDebugSymbols>
        <DCC_SymbolReferenceInfo>0</DCC_SymbolReferenceInfo>
    </PropertyGroup>
</Project>
```

---

## プロジェクトの構成とシステムの構築
### コンパイラ ディレクティブのリファレンス
|ディレクティブ |目的 |例 |
|----------|-----------|----------|
| `{$APPTYPE CONSOLE}`|コンソールアプリケーション | `{$APPTYPE CONSOLE}`|
| `{$APPTYPE GUI}`| GUI アプリケーション (デフォルト) | `{$APPTYPE GUI}`|
| `{$DEFINE DEBUG}`|条件付き記号を定義する | `{$DEFINE DEBUG}`|
| `{$IFDEF symbol}`|条件付きコンパイル | `{$IFDEF DEBUG}`|
| `{$R *.dfm}`|フォームリソースを含める | `{$R *.dfm}`|
| `{$WARNINGS OFF}`|警告を抑制する | `{$WARNINGS OFF}`|
| `{$HINTS OFF}`|ヒントを抑制 | `{$HINTS OFF}`|
| `{$OPTIMIZATION ON}`|オプティマイザを有効にする | `{$OPTIMIZATION ON}`|
| `{$STRINGCHECKS ON}`|文字列範囲チェックを有効にする | `{$STRINGCHECKS ON}`|
### コマンドラインからのビルド
```batch
REM 32-bit Windows build (DCC32)
dcc32 Project.dpr -NSVcl;System;Winapi -R resources -E bin\win32

REM 64-bit Windows build (DCC64)
dcc64 Project.dpr -NSVcl;System;Winapi -R resources -E bin\win64

REM Using MSBuild (modern approach)
msbuild Project.dproj /p:Config=Release /p:Platform=Win32

REM Free Pascal / Lazarus (cross-platform, open source)
fpc -Mdelphi -dLCL -Fu"lib/units" src/Project.lpr
```

### パッケージ構成 (.dpk)
```pascal
package CustomComponents;

{$R *.res}
{$IFDEF RELEASE}
  {$OPTIMIZATION ON}
  {$DEBUG OFF}
{$ENDIF}

requires
  rtl,
  vcl;

contains
  CustomButton in 'src\CustomButton.pas',
  CustomGrid in 'src\CustomGrid.pas',
  CustomChart in 'src\CustomChart.pas';

end.
```

---

## テストとデバッグ
### IDE デバッガーの機能
Delphi の IDE には、フル機能の統合デバッガが含まれています。
|特集 |説明 |
|----------|---------------|
| **ブレークポイント** |任意の実行可能行に設定します。条件付きブレークポイントのサポート |
| **監視ウィンドウ** |変数値をリアルタイムで監視 |
| **呼び出しスタック** |ローカル変数を使用して完全な呼び出しチェーンを表示する |
| **CPU ウィンドウ** |生成されたアセンブリをソース コードと一緒に表示 |
| **メモリビュー** |任意のアドレスの生メモリを検査する |
| **イベント ブレークポイント** |例外、DLL ロード、スレッド イベントで中断 |
| **リモート デバッグ** |リモート マシン上で実行されているアプリケーションをデバッグする |
| **データの視覚化** |データセット、文字列、コレクションのカスタム ビジュアライザー |
### DUnit テスト フレームワーク
```pascal
unit TestBusinessLogic;

interface

uses
  TestFramework, SysUtils, BusinessLogic;

type
  TestTPriceCalculator = class(TTestCase)
  private
    FCalc: TPriceCalculator;
  public
    procedure SetUp; override;
    procedure TearDown; override;
  published
    procedure TestBasePrice;
    procedure TestDiscountCalculation;
    procedure TestTaxCalculation;
    procedure TestFinalPrice;
    procedure TestNegativePriceRaisesException;
    procedure TestZeroQuantity;
  end;

implementation

procedure TestTPriceCalculator.SetUp;
begin
  FCalc := TPriceCalculator.Create;
end;

procedure TestTPriceCalculator.TearDown;
begin
  FCalc.Free;
end;

procedure TestTPriceCalculator.TestBasePrice;
begin
  CheckEquals(100.00, FCalc.CalculateBasePrice(10, 10.00),
    'Base price should be quantity * unit price');
end;

procedure TestTPriceCalculator.TestDiscountCalculation;
begin
  CheckEquals(90.00, FCalc.ApplyDiscount(100.00, 10),
    '10% discount on 100 should be 90');
  CheckEquals(100.00, FCalc.ApplyDiscount(100.00, 0),
    '0% discount should not change price');
end;

procedure TestTPriceCalculator.TestTaxCalculation;
begin
  CheckEquals(122.00, FCalc.AddTax(100.00, 22),
    '22% tax on 100 should be 122');
end;

procedure TestTPriceCalculator.TestFinalPrice;
begin
  CheckEquals(109.80,
    FCalc.CalculateFinalPrice(10, 10.00, 10, 22),
    'Final price: 100 base, 10% discount, 22% tax');
end;

procedure TestTPriceCalculator.TestNegativePriceRaisesException;
begin
  ExpectedException := EInvalidArgument;
  FCalc.CalculateBasePrice(-1, 10.00);
end;

procedure TestTPriceCalculator.TestZeroQuantity;
begin
  CheckEquals(0.00, FCalc.CalculateBasePrice(0, 10.00),
    'Zero quantity should give zero price');
end;

initialization
  RegisterTest(TestTPriceCalculator.Suite);

end.
```

### デバッグワークフロー
```
1. Set breakpoints at suspicious code locations
2. Run the application (F9)
3. When breakpoint hits:
   a. Inspect variables in the Watch window
   b. Step through code (F7 = into, F8 = over)
   c. Check the Call Stack window for execution path
   d. Use Evaluate/Modify (Ctrl+F7) to test expressions
4. For memory issues:
   a. Enable ReportMemoryLeaksOnShutdown
   b. Use FastMM full debug mode
   c. Check for dangling pointers after Free
```

---

## 相互運用性
### COM/ActiveX 統合
```pascal
unit COMExample;

interface

uses
  Winapi.Windows, System.Win.ComObj, ActiveX;

// Create and use a COM object
procedure UseExcelCOM;

// Implement a COM server
type
  TMyCOMObject = class(TAutoObject, IMyCOMInterface)
  protected
    function Get_Version: string; safecall;
    procedure ProcessData(const AInput: string); safecall;
  end;

implementation

uses
  ComServ;

procedure UseExcelCOM;
var
  ExcelApp: OleVariant;
  Workbook: OleVariant;
begin
  ExcelApp := CreateOleObject('Excel.Application');
  try
    ExcelApp.Visible := True;
    Workbook := ExcelApp.Workbooks.Add;
    Workbook.Sheets[1].Cells[1, 1] := 'Hello from Delphi';
    Workbook.Sheets[1].Cells[1, 2] := 42;
    Workbook.SaveAs('C:\temp\delphi_output.xlsx');
  finally
    ExcelApp.Quit;
  end;
end;

end.
```

### C/C++ DLL の呼び出し
```pascal
unit DLLInterop;

interface

uses
  Winapi.Windows, SysUtils;

// Import functions from a C DLL
function AddNumbers(A, B: Integer): Integer; cdecl;
  external 'mathlib.dll' name 'add_numbers';

function ProcessString(Input: PAnsiChar; Output: PAnsiChar;
  MaxLen: Integer): Integer; cdecl;
  external 'stringlib.dll' name 'process_string';

// Import with dynamic loading
type
  TEncryptFunc = function(const AData: PAnsiChar;
    AKey: Integer): PAnsiChar; cdecl;

var
  EncryptData: TEncryptFunc;

procedure LoadCryptoLibrary;
procedure UnloadCryptoLibrary;

implementation

var
  CryptoLib: HMODULE;

procedure LoadCryptoLibrary;
begin
  CryptoLib := LoadLibrary('crypto.dll');
  if CryptoLib = 0 then
    raise Exception.Create('Failed to load crypto.dll');
  
  @EncryptData := GetProcAddress(CryptoLib, 'encrypt_data');
  if not Assigned(EncryptData) then
    raise Exception.Create('encrypt_data not found');
end;

procedure UnloadCryptoLibrary;
begin
  if CryptoLib <> 0 then
  begin
    FreeLibrary(CryptoLib);
    CryptoLib := 0;
  end;
end;

end.
```

### .NET の相互運用性
```pascal
// Delphi Prism / Oxygene can interop with .NET assemblies
// Modern approach: use Java2OP for Android, or WinRT for Windows

// WinRT / Windows Runtime interop
uses
  Winapi.WinRT, Winapi.UI.Notifications;

procedure ShowToastNotification(const AMessage: string);
var
  ToastXML: string;
  ToastDoc: IXmlDocument;
  Toast: IToastNotification;
  Notifier: IToastNotifier;
begin
  ToastXML := '<toast><visual><binding template="ToastText01">' +
    '<text id="1">' + AMessage + '</text>' +
    '</binding></visual></toast>';
  
  ToastDoc := TXmlDocument.Create as IXmlDocument;
  ToastDoc.LoadXml(ToastXML);
  
  Toast := TToastNotification.Create(ToastDoc) as IToastNotification;
  Notifier := TToastNotificationManager.CreateToastNotifier('MyApp');
  Notifier.Show(Toast);
end;
```

---

## デザインパターン
### パターン 1: シングルトン (スレッドセーフ)
```pascal
type
  TAppConfig = class
  private
    class var FInstance: TAppConfig;
    class var FLock: TObject;
    FSettings: TStringList;
    constructor CreatePrivate;
  public
    class function GetInstance: TAppConfig; static;
    class procedure Release; static;
    function GetSetting(const AKey: string): string;
    procedure SetSetting(const AKey, AValue: string);
  end;

class constructor TAppConfig.Create;
begin
  FLock := TObject.Create;
end;

constructor TAppConfig.CreatePrivate;
begin
  inherited Create;
  FSettings := TStringList.Create;
  FSettings.LoadFromFile('config.ini');
end;

class function TAppConfig.GetInstance: TAppConfig;
begin
  TMonitor.Enter(FLock);
  try
    if FInstance = nil then
      FInstance := TAppConfig.CreatePrivate;
    Result := FInstance;
  finally
    TMonitor.Exit(FLock);
  end;
end;
```

### パターン 2: オブザーバー (イベント駆動型)
```pascal
type
  TDataChangeEvent = procedure(Sender: TObject; const AFieldName: string;
    const AOldValue, ANewValue: string) of object;

  TDataStore = class
  private
    FData: TDictionary<string, string>;
    FOnChange: TDataChangeEvent;
  public
    constructor Create;
    destructor Destroy; override;
    procedure SetValue(const AKey, AValue: string);
    function GetValue(const AKey: string): string;
    property OnChange: TDataChangeEvent read FOnChange write FOnChange;
  end;

procedure TDataStore.SetValue(const AKey, AValue: string);
var
  OldValue: string;
begin
  if FData.TryGetValue(AKey, OldValue) then
  begin
    if OldValue <> AValue then
    begin
      FData[AKey] := AValue;
      if Assigned(FOnChange) then
        FOnChange(Self, AKey, OldValue, AValue);
    end;
  end
  else
  begin
    FData.Add(AKey, AValue);
    if Assigned(FOnChange) then
      FOnChange(Self, AKey, '', AValue);
  end;
end;
```

### パターン 3: 工場出荷時の方法
```pascal
type
  // Base report class
  TReport = class
  public
    procedure Generate; virtual; abstract;
    class function GetReportType: string; virtual; abstract;
  end;

  TReportClass = class of TReport;

  // Concrete reports
  TPDFReport = class(TReport)
  public
    procedure Generate; override;
    class function GetReportType: string; override;
  end;

  TCSVReport = class(TReport)
  public
    procedure Generate; override;
    class function GetReportType: string; override;
  end;

  // Factory
  TReportFactory = class
  private
    class var FRegistry: TDictionary<string, TReportClass>;
  public
    class constructor Create;
    class function CreateReport(const AType: string): TReport;
    class procedure RegisterReport(const AType: string;
      AClass: TReportClass);
  end;

class constructor TReportFactory.Create;
begin
  FRegistry := TDictionary<string, TReportClass>.Create;
  RegisterReport('PDF', TPDFReport);
  RegisterReport('CSV', TCSVReport);
end;

class function TReportFactory.CreateReport(const AType: string): TReport;
var
  ReportClass: TReportClass;
begin
  if not FRegistry.TryGetValue(AType, ReportClass) then
    raise Exception.CreateFmt('Unknown report type: %s', [AType]);
  Result := ReportClass.Create;
end;
```

---

## パフォーマンスと最適化
### メモリ管理
```pascal
// Proper memory management pattern
procedure ProcessLargeData;
var
  Buffer: TBytes;
  Stream: TMemoryStream;
begin
  // Use TBytes (managed array) — automatically freed
  SetLength(Buffer, 1024 * 1024);  // 1MB
  try
    // Process buffer...
    FillChar(Buffer[0], Length(Buffer), 0);
  finally
    // Buffer is automatically freed when it goes out of scope
  end;

  // Use try-finally for unmanaged objects
  Stream := TMemoryStream.Create;
  try
    Stream.WriteBuffer(Buffer[0], Length(Buffer));
    Stream.SaveToFile('output.bin');
  finally
    Stream.Free;  // Always free in finally block
  end;
end;

// Use interfaces for automatic reference counting
procedure ProcessWithInterfaces;
var
  Processor: IDataProcessor;
begin
  Processor := TDataProcessor.Create;
  // No Free needed — reference counting handles cleanup
  Processor.Execute;
end;
```

### VCL/FMX 最適化のヒント
|テクニック |影響 |説明 |
|----------|----------|---------------|
| **更新の開始/更新の終了** |高 |再描画を防ぐためにリスト/グリッドの更新をラップする |
| **ダブルバッファリング** |中 |`DoubleBuffered := True`を設定してちらつきを軽減 |
| **仮想リスト** |高 |大規模なデータセットには`TVirtualStringTree`を使用します。
| **ストリングインターン** |中 |文字列定数を再利用します。繰り返しの連結を避ける |
| **オブジェクト プーリング** |中 |頻繁に作成/破棄されるオブジェクトを再利用する |
| **遅延読み込み** |高 |必要な場合にのみデータ/フォームをロードする |
| **コンパイラの最適化** |中 |リリース ビルドに対して`{$O+}`を有効にする |
---

## 導入と実際の使用法
### 導入オプション
```
Delphi Deployment Targets:
├── Windows (VCL/FMX)
│   ├── Standalone .exe (no dependencies)
│   ├── Installer (Inno Setup, InstallShield)
│   └── MSIX / Windows Store package
├── macOS (FMX)
│   └── .app bundle
├── iOS (FMX)
│   └── IPA via Xcode toolchain
├── Android (FMX)
│   └── APK/AAB via Android SDK
└── Linux (FPC/Lazarus only)
    └── ELF binary
```

### 実際の使用例
|業界 |アプリケーション |デルフィを選ぶ理由 |
|----------|---------------|----------|
| **財務** |取引プラットフォーム、銀行ダッシュボード |高速ネイティブ GUI、データベース接続 |
| **ヘルスケア** |医用画像処理、患者管理 | VCL コンポーネント、ネイティブ パフォーマンス |
| **製造** | SCADA システム、産業用制御 |ハードウェアへの直接アクセス、リアルタイム応答 |
| **政府** |内部管理ツール |レガシー システムの継続性 |
| **テレコム** |ネットワーク監視ダッシュボード |高速データ視覚化 |
| **教育** |教育用ソフトウェア、eラーニングツール |迅速な開発、マルチメディアのサポート |
---

## Delphi を使用する場合
|シナリオ |デルフィを選ぶ理由 |より良い代替案 |
|----------|-----------|--------|
|レガシー Delphi メンテナンス |既存のコードベース | — |
| Windows デスクトップ アプリ (高速) | VCL は成熟していて高速です | C# (WPF/WinForms) |
|データベース フロントエンド |優れたデータコンポーネント | C#、Java |
|クロスプラットフォーム デスクトップ (ニッチ) | FireMonkey は存在します | C#、フラッター、電子 |
|新しい Windows GUI の開発 |可能だがコミュニティは縮小している | C# (WPF/WinUI 3) |
|ウェブ開発 |適さない | JavaScript、Python、C# |
|モバイルアプリ | FMX 経由で可能ですが制限があります | Swift、Kotlin、Flutter |
---

## 総合的な Q&A
### Q1: Delphi の VCL フレームワークはどのように機能しますか?
**A:** VCL は、Windows API コントロールをオブジェクト指向の階層でラップします。フォーム、ボタン、グリッドはすべてクラスです。
```pascal
type
  TMainForm = class(TForm)
    Button1: TButton;
    Memo1: TMemo;
    procedure Button1Click(Sender: TObject);
  end;

procedure TMainForm.Button1Click(Sender: TObject);
begin
  Memo1.Lines.Add('Button clicked!');
end;
```

### Q2: Delphi でコンポーネントを作成するにはどうすればよいですか?
**A:** TComponent または TControl から継承:
```pascal
type
  TMyComponent = class(TComponent)
  private
    FValue: Integer;
  protected
    procedure Notification(AComponent: TComponent; Operation: TOperation); override;
  published
    property Value: Integer read FValue write FValue default 0;
  end;
```

### Q3: Delphi と Free Pascal の違いは何ですか?
**A:** Delphi は、Embarcadero による商用 IDE/コンパイラです。 Free Pascal はオープンソースのコンパイラで、Lazarus は無料の IDE です。どちらも Object Pascal 構文を使用します。
### Q4: Delphi でデータベースを操作するにはどうすればよいですか?
**A:** FireDAC または dbExpress コンポーネントを使用します。
```pascal
FDConnection1.ConnectionString := 'DriverID=SQLite;Database=mydb.db';
FDConnection1.Open;
FDQuery1.SQL.Text := 'SELECT * FROM users';
FDQuery1.Open;
while not FDQuery1.Eof do
begin
  Memo1.Lines.Add(FDQuery1.FieldByName('name').AsString);
  FDQuery1.Next;
end;
```

### Q5: Delphi は現在でも関連性がありますか?
**A:** レガシー Windows アプリケーションの保守については、はい。新しいプロジェクトの場合、ほとんどの開発者は C# または Web テクノロジーを好みます。 Free Pascal/Lazarus は、無料のクロスプラットフォームの代替手段を提供します。
---

## 思考連鎖による問題解決
### 問題 1: データ対応フォームの構築
**ステップ 1: 問題を理解する**
データベース レコードを表示および編集するフォームを作成します。
**ステップ 2: アプローチを特定する**
データセットにバインドされたデータ対応コンポーネントを使用します。
**ステップ 3: 実装**```pascal
procedure TMainForm.FormCreate(Sender: TObject);
begin
  FDConnection1.Open;
  FDQuery1.Open;
  DataSource1.DataSet := FDQuery1;
  DBGrid1.DataSource := DataSource1;
  DBNavigator1.DataSource := DataSource1;
end;

procedure TMainForm.btnSaveClick(Sender: TObject);
begin
  FDQuery1.Post;
  ShowMessage('Record saved');
end;
```

**ステップ 4: 延長**
検証、エラー処理、検索/フィルター機能を追加します。
---

＃＃ まとめ
Delphi は、Windows 向けの迅速なアプリケーション開発の先駆けとなった歴史的に重要な言語です。最新の Delphi はネイティブ Windows アプリケーションとデータベース フロントエンドの機能を維持していますが、そのコミュニティとエコシステムは大幅に縮小しています。既存の Delphi コードベースを維持するために、これは引き続き不可欠です。新しいプロジェクトの場合、ほとんどの開発者は C#、Web テクノロジ、またはクロスプラットフォーム フレームワークに移行しました。オープンソースの Free Pascal / Lazarus プロジェクトは、Object Pascal 言語に興味がある人に無料の代替手段を提供します。