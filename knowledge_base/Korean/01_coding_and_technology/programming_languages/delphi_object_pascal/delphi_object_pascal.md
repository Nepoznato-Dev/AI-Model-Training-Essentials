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
# 델파이/오브젝트 파스칼
Delphi는 원래 Borland(이후 Embarcadero, 현재 Idera)에서 개발한 Pascal을 기반으로 한 객체 지향 프로그래밍 언어입니다. 1995년 "Delphi 1"로 처음 ​​출시된 이 제품은 Windows 데스크톱 애플리케이션의 RAD(신속한 애플리케이션 개발)를 위해 설계되었습니다. 이 언어는 공식적으로 Object Pascal로 알려져 있으며 Delphi IDE는 시각적 양식 디자이너, 통합 데이터베이스 도구 및 강력한 컴파일러를 제공합니다.
델파이는 1990년대 후반과 2000년대 초반에 가장 인기 있는 Windows 개발 도구 중 하나였습니다. 인기가 크게 감소했지만 특히 엔터프라이즈 데스크톱 애플리케이션, 데이터베이스 프런트엔드 및 레거시 시스템 유지 관리 분야에서 전용 사용자 기반을 유지하고 있습니다. Modern Delphi(11/12)는 FireMonkey(FMX) 프레임워크를 통해 Windows, macOS, iOS 및 Android용 크로스 플랫폼 개발을 지원합니다.
---

## 델파이가 중요한 이유
- **신속한 애플리케이션 개발**: 시각적 양식 디자이너 + 기본 컴파일을 통해 Windows GUI 구축이 매우 빨라졌습니다.
- **기본 성능**: 런타임이나 VM이 필요하지 않고 기계어 코드로 직접 컴파일됩니다.
- **데이터베이스 연결**: 역사적으로 뛰어난 데이터베이스 구성 요소(dbExpress, FireDAC, ADO).
- **레거시 코드베이스**: 많은 엔터프라이즈 애플리케이션이 여전히 Delphi에서 실행됩니다. 유지 관리는 틈새 기술입니다.
- **크로스 플랫폼(현대)**: FireMonkey 프레임워크는 단일 코드베이스에서 Windows, macOS, iOS 및 Android를 대상으로 합니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **쇠퇴하는 커뮤니티** | C#, Java 또는 JavaScript 커뮤니티보다 훨씬 작습니다 | 활발하지만 규모가 작은 포럼 Idera의 상업적 지원 |
| **제한된 생태계** | 현대 언어보다 적은 수의 타사 라이브러리 | VCL/FMX 컴포넌트 라이브러리를 사용하십시오. 사용자 정의 구성요소 작성 |
| **주로 Windows 중심** | 크로스 플랫폼 지원(FMX)이 덜 성숙함 | 진정한 크로스 플랫폼을 위해 C#, Flutter 또는 웹 기술 사용 |
| **라이센스 비용** | 상업용 IDE에는 유료 라이센스가 필요합니다 | 오픈 소스 대안: Free Pascal/Lazarus |
| **채용난이도** | 시장에 진입하는 델파이 개발자 감소 | 기존 시스템을 유지합니다. 새로운 기능을 최신 스택으로 마이그레이션 |
---

## 구문 기본 사항
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

## 고급 구문 및 패턴
### 제네릭 및 컬렉션
Delphi는 Delphi 2009부터 제네릭을 지원하여 유형이 안전한 컨테이너 클래스를 활성화합니다.
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

### 익명 메소드 및 클로저
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

### 인터페이스 및 종속성 주입
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

### VCL 구성 요소 패턴
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

## 아키텍처 및 시스템 설계
### 구성요소 아키텍처
Delphi의 VCL(Visual Component Library)과 FMX(FireMonkey)는 구성 요소 계층 구조를 기반으로 구축되었습니다. 모든 시각적 요소는`TComponent`에서 상속됩니다.
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

### 일반적인 프로젝트 디렉터리 구조
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

### .dproj 프로젝트 파일
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

## 프로젝트 구성 및 빌드 시스템
### 컴파일러 지시문 참조
| 지시어 | 목적 | 예 |
|------------|---------|---------|
|  __보호됨_0__ | 콘솔 애플리케이션 |  __보호됨_1__ |
|  __보호됨_2__ | GUI 애플리케이션(기본값) |  __보호됨_3__ |
|  __보호됨_4__ | 조건부 기호 정의 |  __보호됨_5__ |
|  __보호_6__ | 조건부 컴파일 |  __보호_7__ |
|  __보호됨_8__ | 양식 리소스 포함 |  __보호_9__ |
|  __보호됨_10__ | 경고 억제 |  __보호됨_11__ |
|  __보호됨_12__ | 힌트 억제 |  __보호_13__ |
|  __보호됨_14__ | 최적화 프로그램 활성화 |  __보호_15__ |
|  __보호됨_16__ | 문자열 범위 확인 활성화 |  __보호됨_17__ |
### 명령줄에서 빌드
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

### 패키지 구성(.dpk)
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

## 테스트 및 디버깅
### IDE 디버거 기능
Delphi의 IDE에는 모든 기능을 갖춘 통합 디버거가 포함되어 있습니다.
| 기능 | 설명 |
|---------|-------------|
| **중단점** | 실행 가능한 라인에 설정하십시오. 조건부 중단점 지원 |
| **감시 창** | 변수 값을 실시간으로 모니터링 |
| **호출 스택** | 지역 변수가 포함된 전체 호출 체인 보기 |
| **CPU 창** | 소스 코드와 함께 생성된 어셈블리 보기 |
| **메모리 보기** | 모든 주소에서 원시 메모리 검사 |
| **이벤트 중단점** | 예외, DLL 로드, 스레드 이벤트 중단 |
| **원격 디버깅** | 원격 시스템에서 실행 중인 애플리케이션 디버그 |
| **데이터 시각화** | 데이터세트, 문자열, 컬렉션을 위한 사용자 정의 시각화 도우미 |
### DUnit 테스트 프레임워크
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

### 디버깅 작업흐름
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

## 상호 운용성
### COM/ActiveX 통합
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

### C/C++ DLL 호출
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

### .NET 상호 운용성
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

## 디자인 패턴
### 패턴 1: 싱글톤(스레드로부터 안전함)
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

### 패턴 2: 관찰자(이벤트 기반)
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

### 패턴 3: 팩토리 메소드
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

## 성능 및 최적화
### 메모리 관리
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

### VCL/FMX 최적화 팁
| 기술 | 영향 | 설명 |
|------------|---------|-------------|
| **업데이트 시작/업데이트 종료** | 높음 | 다시 그리기를 방지하기 위해 목록/그리드 업데이트 래핑 |
| **이중 버퍼링** | 중간 | 깜박임을 줄이기 위해`DoubleBuffered := True`설정 |
| **가상 목록** | 높음 | 대규모 데이터 세트에는`TVirtualStringTree`사용 |
| **스트링인턴** | 중간 | 문자열 상수를 재사용합니다. 반복되는 연결을 피하세요 |
| **객체 풀링** | 중간 | 자주 생성/파기되는 객체 재사용 |
| **지연 로딩** | 높음 | 필요할 때만 데이터/양식 로드 |
| **컴파일러 최적화** | 중간 | 릴리스 빌드에`{$O+}`활성화 |
---

## 배포 및 실제 사용
### 배포 옵션
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

### 실제 사용 사례
| 산업 | 신청 | 왜 델파이인가 |
|----------|-------------|----------|
| **금융** | 거래 플랫폼, 은행 대시보드 | 빠른 기본 GUI, 데이터베이스 연결 |
| **헬스케어** | 의료영상, 환자관리 | VCL 구성 요소, 기본 성능 |
| **제조** | SCADA 시스템, 산업 제어 | 직접 하드웨어 액세스, 실시간 응답 |
| **정부** | 내부 관리 도구 | 레거시 시스템 연속성 |
| **통신** | 네트워크 모니터링 대시보드 | 빠른 데이터 시각화 |
| **교육** | 교육용 소프트웨어, e-러닝 도구 | 신속한 개발, 멀티미디어 지원 |
---

## 델파이를 사용해야 하는 경우
| 시나리오 | 왜 델파이인가 | 더 나은 대안 |
|----------|------------|------|
| 레거시 델파이 유지 관리 | 기존 코드베이스 | — |
| Windows 데스크톱 앱(빠름) | VCL은 성숙하고 빠릅니다 | C#(WPF/WinForms) |
| 데이터베이스 프런트엔드 | 뛰어난 데이터 구성요소 | C#, 자바 |
| 크로스 플랫폼 데스크탑(틈새) | 파이어몽키가 존재합니다 | C#, 플러터, 전자 |
| 새로운 Windows GUI 개발 | 가능하지만 커뮤니티가 축소되고 있음 | C#(WPF/WinUI 3) |
| 웹 개발 | 적합하지 않음 | 자바스크립트, 파이썬, C# |
| 모바일 앱 | FMX를 통해 가능하지만 제한됨 | 스위프트, 코틀린, 플러터 |
---

## 요약
Delphi는 Windows용 신속한 애플리케이션 개발을 개척한 역사적으로 중요한 언어입니다. 최신 Delphi는 여전히 기본 Windows 애플리케이션과 데이터베이스 프런트엔드를 지원하지만 커뮤니티와 생태계는 상당히 축소되었습니다. 기존 Delphi 코드베이스를 유지하려면 여전히 필수적입니다. 새 프로젝트의 경우 대부분의 개발자는 C#, 웹 기술 또는 크로스 플랫폼 프레임워크로 마이그레이션했습니다. 오픈 소스 Free Pascal/Lazarus 프로젝트는 오브젝트 파스칼 언어에 관심이 있는 사람들을 위한 무료 대안을 제공합니다.