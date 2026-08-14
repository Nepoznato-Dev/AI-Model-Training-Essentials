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

# Делфи/Объект Паскаль
Delphi — объектно-ориентированный язык программирования, основанный на Pascal, первоначально разработанный Borland (позже Embarcadero, теперь Idera). Впервые выпущенный в 1995 году как «Delphi 1», он был разработан для быстрой разработки приложений (RAD) для настольных приложений Windows. Язык формально известен как Object Pascal, а среда разработки Delphi предоставляет визуальный дизайнер форм, интегрированные инструменты баз данных и мощный компилятор.
Delphi был одним из самых популярных инструментов разработки для Windows в конце 1990-х — начале 2000-х годов. Хотя его популярность значительно снизилась, он поддерживает выделенную базу пользователей, особенно в корпоративных настольных приложениях, интерфейсах баз данных и обслуживании устаревших систем. Modern Delphi (11/12) поддерживает кроссплатформенную разработку для Windows, macOS, iOS и Android с помощью платформы FireMonkey (FMX).
---

## Почему Delphi имеет значение
- **Быстрая разработка приложений**: визуальный дизайнер форм и встроенная компиляция позволили чрезвычайно быстро создавать графические интерфейсы Windows.
- **Встроенная производительность**: компилируется непосредственно в машинный код — среда выполнения или виртуальная машина не требуются.
- **Подключение к базе данных**: исторически превосходные компоненты базы данных (dbExpress, FireDAC, ADO).
- **Устаревшие кодовые базы**: многие корпоративные приложения по-прежнему работают на Delphi; техническое обслуживание — это нишевый навык.
- **Кроссплатформенность (современная)**: платформа FireMonkey ориентирована на Windows, macOS, iOS и Android и использует единую базу кода.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Угасание сообщества** | Гораздо меньше, чем сообщества C#, Java или JavaScript | Активные, но небольшие форумы; коммерческая поддержка от Idera |
| **Ограниченная экосистема** | Меньше сторонних библиотек, чем в современных языках | Используйте библиотеку компонентов VCL/FMX; писать пользовательские компоненты |
| **В основном ориентирован на Windows** | Кроссплатформенная поддержка (FMX) менее развита | Используйте C#, Flutter или веб-технологии для настоящей кроссплатформенности |
| **Стоимость лицензии** | Коммерческая IDE требует платной лицензии | Альтернатива с открытым исходным кодом: Free Pascal/Lazarus |
| **Сложность с наймом** | Меньше разработчиков Delphi выходит на рынок | Поддерживать существующие системы; перенести новые функции в современные стеки |
---

## Основы синтаксиса
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

## Расширенный синтаксис и шаблоны
### Обобщения и коллекции
Delphi поддерживает дженерики (начиная с Delphi 2009), что позволяет использовать типобезопасные контейнерные классы.
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

### Анонимные методы и замыкания
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

### Интерфейсы и внедрение зависимостей
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

### Шаблоны компонентов VCL
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

## Архитектура и системный дизайн
### Архитектура компонентов
VCL (библиотека визуальных компонентов) и FMX (FireMonkey) Delphi построены на иерархии компонентов. Каждый визуальный элемент наследуется от `TComponent`.
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

### Типичная структура каталога проекта
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

### Файл проекта .dproj
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

## Конфигурация проекта и система сборки
### Справочник по директивам компилятора
| Директива | Цель | Пример |
|-----------|---------|---------|
| `{$APPTYPE CONSOLE}`| Консольное приложение | `{$APPTYPE CONSOLE}`|
| `{$APPTYPE GUI}`| Приложение с графическим интерфейсом (по умолчанию) | `{$APPTYPE GUI}`|
| `{$DEFINE DEBUG}`| Определить условный символ | `{$DEFINE DEBUG}`|
| `{$IFDEF symbol}`| Условная компиляция | `{$IFDEF DEBUG}`|
| `{$R *.dfm}`| Включить ресурс формы | `{$R *.dfm}`|
| `{$WARNINGS OFF}`| Подавить предупреждения | `{$WARNINGS OFF}`|
| `{$HINTS OFF}`| Подавить подсказки | `{$HINTS OFF}`|
| `{$OPTIMIZATION ON}`| Включить оптимизатор | `{$OPTIMIZATION ON}`|
| `{$STRINGCHECKS ON}`| Включить проверку диапазона строк | `{$STRINGCHECKS ON}`|
### Сборка из командной строки
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

### Конфигурация пакета (.dpk)
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

## Тестирование и отладка
### Возможности IDE-отладчика
IDE Delphi включает в себя полнофункциональный интегрированный отладчик.
| Особенность | Описание |
|---------|-------------|
| **Точки останова** | Устанавливается в любой исполняемой строке; поддерживаются условные точки останова |
| **Окно просмотра** | Мониторинг значений переменных в режиме реального времени |
| **Стек вызовов** | Просмотр полной цепочки вызовов с локальными переменными |
| **Окно ЦП** | Просмотр созданной сборки вместе с исходным кодом |
| **Вид из памяти** | Проверить необработанную память по любому адресу |
| **Точки останова событий** | Прерывание исключений, загрузок DLL, событий потоков |
| **Удаленная отладка** | Отладка приложений, работающих на удаленных машинах |
| **Визуализация данных** | Пользовательские визуализаторы для наборов данных, строк и коллекций |
### Платформа тестирования DUnit
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

### Рабочий процесс отладки
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

## Совместимость
### Интеграция COM/ActiveX
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

### Вызов DLL C/C++
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

### Совместимость .NET
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

## Шаблоны проектирования
### Шаблон 1: синглтон (потокобезопасный)
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

### Шаблон 2: наблюдатель (управляемый событиями)
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

### Шаблон 3: Фабричный метод
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

## Производительность и оптимизация
### Управление памятью
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

### Советы по оптимизации VCL/FMX
| Техника | Воздействие | Описание |
|-----------|--------|-------------|
| **BeginUpdate/EndUpdate** | Высокий | Обернуть обновления списка/сетки, чтобы предотвратить перерисовку |
| **Двойная буферизация** | Средний | Установите `DoubleBuffered := True`, чтобы уменьшить мерцание |
| **Виртуальные списки** | Высокий | Используйте`TVirtualStringTree`для больших наборов данных |
| **Стройная стажировка** | Средний | Повторное использование строковых констант; избежать повторной конкатенации |
| **Объединение объектов** | Средний | Повторное использование часто создаваемых/уничтожаемых объектов |
| **Отложенная загрузка** | Высокий | Загружайте данные/формы только при необходимости |
| **Оптимизация компилятора** | Средний | Включите`{$O+}`для выпускных сборок |
---

## Развертывание и использование в реальных условиях
### Варианты развертывания
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

### Реальные примеры использования
| Промышленность | Приложение | Почему Дельфи |
|----------|-------------|-----------|
| **Финансы** | Торговые платформы, банковские панели | Быстрый встроенный графический интерфейс, подключение к базе данных |
| **Здравоохранение** | Медицинская визуализация, ведение пациентов | Компоненты VCL, собственная производительность |
| **Производство** | Системы SCADA промышленного контроля | Прямой доступ к оборудованию, реагирование в режиме реального времени |
| **Правительство** | Внутренние административные инструменты | Непрерывность устаревшей системы |
| **Телеком** | Панели мониторинга сетевого мониторинга | Быстрая визуализация данных |
| **Образование** | Образовательное программное обеспечение, инструменты электронного обучения | Быстрая разработка, поддержка мультимедиа |
---

## Когда использовать Delphi
| Сценарий | Почему Дельфи | Лучшая альтернатива |
|----------|-----------|-------------------|
| Обслуживание устаревших версий Delphi | Существующая кодовая база | — |
| Настольные приложения для Windows (быстрая версия) | VCL — зрелая и быстрая | С# (WPF/WinForms) |
| Интерфейсы базы данных | Отличные компоненты данных | С#, Java |
| Кроссплатформенный десктоп (ниша) | FireMonkey существует | C#, Флаттер, Электрон |
| Разработка нового графического интерфейса Windows | Возможно, но сообщество сокращается | С# (WPF/WinUI 3) |
| Веб-разработка | Не подходит | JavaScript, Python, C# |
| Мобильные приложения | Возможно через FMX, но ограничено | Свифт, Котлин, Флаттер |
---

## Синтетические вопросы и ответы
### Вопрос 1. Как работает среда Delphi VCL?
**A:** VCL объединяет элементы управления Windows API в объектно-ориентированную иерархию. Формы, кнопки и сетки — все это классы:
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

### Вопрос 2. Как создавать компоненты в Delphi?
**A:** Наследовать от TComponent или TControl:
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

### Q3: В чем разница между Delphi и Free Pascal?
**О:** Delphi — это коммерческая среда разработки/компилятор от Embarcadero. Free Pascal — это компилятор с открытым исходным кодом, а Lazarus — бесплатная IDE. Оба используют синтаксис Object Pascal.
### Q4: Как работать с базами данных в Delphi?
**A:** Используйте компоненты FireDAC или dbExpress:
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

### Вопрос 5: Актуален ли Delphi сегодня?
**О:** Да, для поддержки устаревших приложений Windows. Для новых проектов большинство разработчиков предпочитают C# или веб-технологии. Free Pascal/Lazarus предоставляет бесплатную кроссплатформенную альтернативу.
---

## Решение проблем с цепочкой мыслей
### Проблема 1. Создание формы, учитывающей данные
**Шаг 1. Поймите проблему**
Создайте форму, которая отображает и редактирует записи базы данных.
**Шаг 2. Определите подход**
Используйте компоненты, поддерживающие данные, привязанные к набору данных.
**Шаг 3. Реализация**```pascal
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

**Шаг 4. Продлить**
Добавьте функции проверки, обработки ошибок и поиска/фильтрации.
---

## Краткое содержание
Delphi — исторически важный язык, который стал пионером в быстрой разработке приложений для Windows. Современный Delphi по-прежнему поддерживает собственные приложения Windows и интерфейсы баз данных, но его сообщество и экосистема значительно сократились. Для поддержки существующих кодовых баз Delphi это по-прежнему важно. Для новых проектов большинство разработчиков перешли на C#, веб-технологии или кроссплатформенные платформы. Проект Free Pascal/Lazarus с открытым исходным кодом предоставляет бесплатную альтернативу для тех, кто интересуется языком Object Pascal.