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

# Delphi / 物件 Pascal
Delphi 是一種基於 Pascal 的物件導向程式語言，最初由 Borland（後來的 Embarcadero，現在的 Idera）開發。它於 1995 年首次發布，名為“Delphi 1”，專為 Windows 桌面應用程式的快速應用程式開發 (RAD) 而設計。該語言的正式名稱為 Object Pascal，Delphi IDE 提供了視覺化表單設計器、整合式資料庫工具和強大的編譯器。
Delphi 是 20 世紀 90 年代末和 2000 年代初期最受歡迎的 Windows 開發工具之一。儘管其受歡迎程度已大幅下降，但它仍保持著專門的用戶群，特別是在企業桌面應用程式、資料庫前端和遺留系統維護方面。現代 Delphi (11/12) 透過 FireMonkey (FMX) 框架支援 Windows、macOS、iOS 和 Android 的跨平台開發。
---

## 為什麼德爾福很重要
- **快速應用程式開發**：視覺化表單設計器+本機編譯使得建立 Windows GUI 變得非常快。
- **本機效能**：直接編譯為機器碼 - 無需執行時間或虛擬機器。
- **資料庫連線**：歷史上優秀的資料庫元件（dbExpress、FireDAC、ADO）。
- **遺留程式碼庫**：許多企業應用程式仍然在 Delphi 上運行；維護是一項小眾技能。
- **跨平台（現代）**：FireMonkey 框架透過單一程式碼庫針對 Windows、macOS、iOS 和 Android。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **社群日漸衰退** |比 C#、Java 或 JavaScript 社群小得多 |活躍但規模較小的論壇；井寺的商業支援|
| **有限的生態系統** |比現代語言更少的第三方函式庫 |使用VCL/FMX元件庫；編寫自訂元件|
| **主要針對 Windows** |跨平台支援（FMX）不太成熟 |使用 C#、Flutter 或 Web 技術實現真正的跨平台 |
| **許可證費用** |商業 IDE 需要付費許可證 |開源替代方案：Free Pascal / Lazarus |
| **招募困難** |進入市場的德爾福開發商越來越少維護現有系統；將新功能遷移到現代堆疊 |
---

## 文法基礎知識
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

## 進階語法和模式
### 泛型和集合
Delphi 支援泛型（自 Delphi 2009 年起），支援類型安全的容器類別。
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

### 匿名方法與閉包
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

### 介面和依賴注入
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

### VCL 元件模式
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

## 架構與系統設計
### 元件架構
Delphi 的 VCL（視覺化元件庫）和 FMX（FireMonkey）建構在元件層次結構上。每個視覺元素都繼承自`TComponent`。
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

### 典型的專案目錄結構
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

### .dproj 專案文件
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

## 專案配置與建置系統
### 編譯器指令參考
|指令|目的|範例|
|------------|---------|---------|
|`{$APPTYPE CONSOLE}`|控制台應用程式|`{$APPTYPE CONSOLE}`|
|`{$APPTYPE GUI}`| GUI 應用程式（預設）|`{$APPTYPE GUI}`|
|`{$DEFINE DEBUG}`|定義條件符號 |`{$DEFINE DEBUG}`|
|`{$IFDEF symbol}`|條件編譯 |`{$IFDEF DEBUG}`|
|`{$R *.dfm}`|包含表單資源 |`{$R *.dfm}`|
|`{$WARNINGS OFF}`|抑制警告 |`{$WARNINGS OFF}`|
|`{$HINTS OFF}`|抑制提示 |`{$HINTS OFF}`|
|`{$OPTIMIZATION ON}`|啟用優化器 |`{$OPTIMIZATION ON}`|
|`{$STRINGCHECKS ON}`|啟用字串範圍檢查 |`{$STRINGCHECKS ON}`|
### 從命令列構建
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

### 套件配置（.dpk）
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

## 測試和調試
### IDE 偵錯器功能
Delphi 的 IDE 包括一個全功能的整合式偵錯器。
|特色 |描述 |
|---------|-------------|
| **斷點** |在任何可執行行上設定；支援條件斷點|
| **觀察視窗** |即時監控變數值 |
| **呼叫堆疊** |查看帶有局部變數的完整呼叫鏈 |
| **CPU 視窗** |查看產生的組件和原始碼 |
| **記憶體視圖** |檢查任意位址的原始記憶體 |
| **事件斷點** |異常中斷、DLL 載入、執行緒事件 |
| **遠端偵錯** |調試在遠端機器上運行的應用程式|
| **資料視覺化** |資料集、字串、集合的自訂視覺化工具 |
### DUnit 測試框架
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

### 偵錯工作流程
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

## 互通性
### COM/ActiveX 集成
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

### 呼叫 C/C++ DLL
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

### .NET 互通性
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

## 設計模式
### 模式 1：單例（線程安全）
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

### 模式 2：觀察者（事件驅動）
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

### 模式 3：工廠方法
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

## 效能與最佳化
### 記憶體管理
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

### VCL/FMX 最佳化技巧
|技術|影響 |描述 |
|------------|--------|-------------|
| **開始更新/結束更新** |高|包裝清單/網格更新以防止重新繪製 |
| **雙緩衝** |中|設定`DoubleBuffered := True`以減少閃爍 |
| **虛擬清單** |高|使用`TVirtualStringTree`處理大型資料集 |
| **字串實習** |中|重複使用字串常數；避免重複串聯 |
| **物件池** |中|重複使用經常建立/銷毀的物件 |
| **延遲載入** |高|僅在需要時載入資料/表單 |
| **編譯器最佳化** |中|為發布版本啟用`{$O+}`|
---

## 部署和實際使用
### 部署選項
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

### 現實世界用例
|工業|應用 |為什麼選擇德爾福 |
|----------|-------------|------------|
| **金融** |交易平台、銀行儀表板 |快速本機 GUI、資料庫連線 |
| **醫療保健** |醫學影像、病患管理| VCL組件，原生性能|
| **製造** | SCADA系統，工業控制|硬體直接接入，即時回應 |
| **政府** |內部管理工具|遺留系統連續性|
| **電信** |網路監控儀表板|快速資料視覺化 |
| **教育** |教育軟體、電子學習工具|快速開發，多媒體支援|
---

## 何時使用 Delphi
|場景 |為什麼選擇德爾福 |更好的選擇|
|----------|----------|--------------------|
|舊版德爾福維護|現有程式碼庫 | — |
| Windows 桌面應用程式（快速）| VCL成熟、速度快| C#（WPF/WinForms）|
|資料庫前端 |優秀的資料組件| C#、Java |
|跨平台桌面（利基）| FireMonkey 存在 | C#、顫振、電子 |
|新的Windows GUI開發|有可能，但社群正在縮小 | C# (WPF/WinUI 3) |
|網頁開發|不適合| JavaScript、Python、C# |
|行動應用程式 |可以通過 FMX 但有限 |斯威夫特、科特林、顫振 |
---

＃＃ 概括
Delphi 是一種歷史上很重要的語言，它開創了 Windows 快速應用程式開發的先河。現代 Delphi 仍然能夠支援本機 Windows 應用程式和資料庫前端，但其社群和生態系統已大幅萎縮。對於維護現有的 Delphi 程式碼庫，它仍然至關重要。對於新項目，大多數開發人員已遷移到 C#、Web 技術或跨平台框架。開源 Free Pascal / Lazarus 專案為對 Object Pascal 語言感興趣的人提供了免費的替代方案。