---
# मेटाडेटा
शीर्षक: "डेल्फ़ी/ऑब्जेक्ट पास्कल"
विवरण: "डेल्फ़ी/ऑब्जेक्ट पास्कल प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स बुनियादी बातें, पारिस्थितिकी तंत्र और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [डेल्फ़ी-ऑब्जेक्ट-पास्कल, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "44 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# डेल्फ़ी/ऑब्जेक्ट पास्कल
डेल्फ़ी पास्कल पर आधारित एक ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग भाषा है, जिसे मूल रूप से बोरलैंड (बाद में एम्बरकेडेरो, अब इडेरा) द्वारा विकसित किया गया था। पहली बार 1995 में "डेल्फ़ी 1" के रूप में रिलीज़ किया गया था, इसे विंडोज़ डेस्कटॉप अनुप्रयोगों के तीव्र अनुप्रयोग विकास (आरएडी) के लिए डिज़ाइन किया गया था। भाषा को औपचारिक रूप से ऑब्जेक्ट पास्कल के रूप में जाना जाता है, और डेल्फ़ी आईडीई एक विज़ुअल फॉर्म डिज़ाइनर, एकीकृत डेटाबेस टूल और एक शक्तिशाली कंपाइलर प्रदान करता है।
1990 के दशक के अंत और 2000 के दशक की शुरुआत में डेल्फ़ी सबसे लोकप्रिय विंडोज़ डेवलपमेंट टूल्स में से एक था। हालाँकि इसकी लोकप्रियता में काफी गिरावट आई है, यह एक समर्पित उपयोगकर्ता आधार बनाए रखता है, विशेष रूप से एंटरप्राइज़ डेस्कटॉप एप्लिकेशन, डेटाबेस फ्रंट-एंड और लीगेसी सिस्टम रखरखाव में। मॉडर्न डेल्फ़ी (11/12) फायरमॉन्की (एफएमएक्स) फ्रेमवर्क के माध्यम से विंडोज, मैकओएस, आईओएस और एंड्रॉइड के लिए क्रॉस-प्लेटफ़ॉर्म विकास का समर्थन करता है।
---

## डेल्फ़ी क्यों मायने रखती है
- **तीव्र अनुप्रयोग विकास**: विज़ुअल फॉर्म डिज़ाइनर + देशी संकलन ने विंडोज़ जीयूआई को बेहद तेज़ बना दिया।
- **मूल प्रदर्शन**: सीधे मशीन कोड पर संकलित होता है - किसी रनटाइम या वीएम की आवश्यकता नहीं होती है।
- **डेटाबेस कनेक्टिविटी**: ऐतिहासिक रूप से उत्कृष्ट डेटाबेस घटक (dbExpress, FireDAC, ADO)।
- **लीगेसी कोडबेस**: कई एंटरप्राइज़ एप्लिकेशन अभी भी डेल्फ़ी पर चलते हैं; रखरखाव एक विशिष्ट कौशल है।
- **क्रॉस-प्लेटफॉर्म (आधुनिक)**: फायरमंकी फ्रेमवर्क एक ही कोडबेस से विंडोज, मैकओएस, आईओएस और एंड्रॉइड को लक्षित करता है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **घटता हुआ समुदाय** | C#, Java, या JavaScript समुदायों से बहुत छोटा | सक्रिय लेकिन छोटे मंच; इडेरा से व्यावसायिक समर्थन |
| **सीमित पारिस्थितिकी तंत्र** | आधुनिक भाषाओं की तुलना में कम तृतीय-पक्ष लाइब्रेरी | वीसीएल/एफएमएक्स घटक लाइब्रेरी का उपयोग करें; कस्टम घटक लिखें |
| **मुख्यतः विंडोज़-केंद्रित** | क्रॉस-प्लेटफ़ॉर्म समर्थन (एफएमएक्स) कम परिपक्व है | सच्चे क्रॉस-प्लेटफ़ॉर्म के लिए C#, फ़्लटर, या वेब तकनीकों का उपयोग करें |
| **लाइसेंसिंग लागत** | वाणिज्यिक आईडीई के लिए सशुल्क लाइसेंस की आवश्यकता होती है | ओपन-सोर्स विकल्प: फ्री पास्कल / लाजर |
| **किराए पर लेने में कठिनाई** | कम डेल्फ़ी डेवलपर्स बाज़ार में प्रवेश कर रहे हैं | मौजूदा प्रणालियों को बनाए रखें; नई सुविधाओं को आधुनिक स्टैक में स्थानांतरित करें |
---

## सिंटेक्स बुनियादी बातें
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

## उन्नत सिंटैक्स और पैटर्न
### जेनरिक और संग्रह
डेल्फ़ी जेनेरिक का समर्थन करता है (डेल्फ़ी 2009 से), प्रकार-सुरक्षित कंटेनर कक्षाओं को सक्षम करता है।
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

### अज्ञात तरीके और समापन
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

### इंटरफेस और निर्भरता इंजेक्शन
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

### वीसीएल घटक पैटर्न
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

## वास्तुकला एवं सिस्टम डिज़ाइन
### घटक वास्तुकला
डेल्फ़ी की वीसीएल (विज़ुअल कंपोनेंट लाइब्रेरी) और एफएमएक्स (फ़ायरमंकी) एक घटक पदानुक्रम पर बनाए गए हैं। प्रत्येक दृश्य तत्व`TComponent`से प्राप्त होता है।
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

### विशिष्ट परियोजना निर्देशिका संरचना
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

### .dproj प्रोजेक्ट फ़ाइल
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### कंपाइलर निर्देश संदर्भ
| निर्देश | उद्देश्य | उदाहरण |
|----|---|----|
|  __संरक्षित_0__ | कंसोल एप्लिकेशन |  __संरक्षित_1__ |
|  __संरक्षित_2__ | जीयूआई एप्लिकेशन (डिफ़ॉल्ट) |  __संरक्षित_3__ |
|  __संरक्षित_4__ | सशर्त प्रतीक को परिभाषित करें |  __संरक्षित_5__ |
|  __संरक्षित_6__ | सशर्त संकलन |  __संरक्षित_7__ |
|  __संरक्षित_8__ | प्रपत्र संसाधन शामिल करें |  __संरक्षित_9__ |
|  __संरक्षित_10__ | चेतावनियाँ दबाएँ |  __संरक्षित_11__ |
|  __संरक्षित_12__ | संकेत दबाएँ |  __संरक्षित_13__ |
|  __संरक्षित_14__ | अनुकूलक सक्षम करें |  __संरक्षित_15__ |
|  __संरक्षित_16__ | स्ट्रिंग रेंज जांच सक्षम करें |  __संरक्षित_17__ |
### कमांड लाइन से बिल्डिंग
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

### पैकेज कॉन्फ़िगरेशन (.dpk)
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

## परीक्षण एवं डिबगिंग
### आईडीई डिबगर सुविधाएँ
डेल्फ़ी की IDE में एक पूर्ण विशेषताओं वाला एकीकृत डिबगर शामिल है।
| फ़ीचर | विवरण |
|---------|-----------------|
| **ब्रेकप्वाइंट** | किसी भी निष्पादन योग्य लाइन पर सेट करें; सशर्त ब्रेकप्वाइंट समर्थित |
| **खिड़की देखें** | वास्तविक समय में परिवर्तनीय मानों की निगरानी करें |
| **कॉल स्टैक** | स्थानीय चरों के साथ पूरी कॉल श्रृंखला देखें |
| **सीपीयू विंडो** | स्रोत कोड के साथ जेनरेटेड असेंबली देखें |
| **मेमोरी दृश्य** | किसी भी पते पर कच्ची मेमोरी का निरीक्षण करें |
| **इवेंट ब्रेकप्वाइंट** | अपवादों, डीएलएल लोड, थ्रेड इवेंट पर ब्रेक |
| **दूरस्थ डिबगिंग** | दूरस्थ मशीनों पर चल रहे अनुप्रयोगों को डीबग करें |
| **डेटा विज़ुअलाइज़ेशन** | डेटासेट, स्ट्रिंग्स, संग्रह के लिए कस्टम विज़ुअलाइज़र |
### DUnit परीक्षण ढाँचा
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

### डिबगिंग वर्कफ़्लो
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

## अंतरसंचालनीयता
### COM/ActiveX एकीकरण
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

### सी/सी++ डीएलएल को कॉल करना
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

### .NET इंटरऑपरेबिलिटी
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

## डिज़ाइन पैटर्न
### पैटर्न 1: सिंगलटन (थ्रेड-सुरक्षित)
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

### पैटर्न 2: पर्यवेक्षक (घटना-संचालित)
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

### पैटर्न 3: फ़ैक्टरी विधि
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

## प्रदर्शन एवं अनुकूलन
### मेमोरी प्रबंधन
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

### वीसीएल/एफएमएक्स अनुकूलन युक्तियाँ
| तकनीक | प्रभाव | विवरण |
|----|-------|----|
| **आरंभ अद्यतन/अंत अद्यतन** | उच्च | दोबारा रंग-रोगन रोकने के लिए सूची/ग्रिड अपडेट लपेटें |
| **डबल बफ़रिंग** | मध्यम | झिलमिलाहट कम करने के लिए`DoubleBuffered := True`सेट करें |
| **आभासी सूचियाँ** | उच्च | बड़े डेटासेट के लिए`TVirtualStringTree`का उपयोग करें |
| **स्ट्रिंग इंटर्निंग** | मध्यम | स्ट्रिंग स्थिरांक का पुन: उपयोग करें; बार-बार सम्मिलन से बचें |
| **ऑब्जेक्ट पूलिंग** | मध्यम | बार-बार निर्मित/नष्ट वस्तुओं का पुन: उपयोग करें |
| **आलसी लोडिंग** | उच्च | जरूरत पड़ने पर ही डेटा/फॉर्म लोड करें |
| **संकलक अनुकूलन** | मध्यम | रिलीज़ बिल्ड के लिए`{$O+}`सक्षम करें |
---

## परिनियोजन और वास्तविक दुनिया में उपयोग
### परिनियोजन विकल्प
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

### वास्तविक दुनिया में उपयोग के मामले
| उद्योग | आवेदन | डेल्फ़ी क्यों |
|---|---|----|
| **वित्त** | ट्रेडिंग प्लेटफॉर्म, बैंकिंग डैशबोर्ड | तेज़ देशी जीयूआई, डेटाबेस कनेक्टिविटी |
| **स्वास्थ्य सेवा** | मेडिकल इमेजिंग, रोगी प्रबंधन | वीसीएल घटक, मूल प्रदर्शन |
| **विनिर्माण** | SCADA सिस्टम, औद्योगिक नियंत्रण | प्रत्यक्ष हार्डवेयर पहुंच, वास्तविक समय प्रतिक्रिया |
| **सरकार** | आंतरिक प्रशासनिक उपकरण | विरासत प्रणाली निरंतरता |
| **टेलीकॉम** | नेटवर्क मॉनिटरिंग डैशबोर्ड | तेज़ डेटा विज़ुअलाइज़ेशन |
| **शिक्षा** | शैक्षिक सॉफ्टवेयर, ई-लर्निंग उपकरण | तीव्र विकास, मल्टीमीडिया समर्थन |
---

## डेल्फ़ी का उपयोग कब करें
| परिदृश्य | डेल्फ़ी क्यों | बेहतर विकल्प |
|---|----|-----|
| लीगेसी डेल्फ़ी रखरखाव | मौजूदा कोडबेस | — |
| विंडोज़ डेस्कटॉप ऐप्स (रैपिड) | वीसीएल परिपक्व और तेज़ है | सी# (डब्ल्यूपीएफ/विनफॉर्म) |
| डेटाबेस फ्रंट-एंड | उत्कृष्ट डेटा घटक | सी#, जावा |
| क्रॉस-प्लेटफ़ॉर्म डेस्कटॉप (आला) | फायरमंकी मौजूद है | सी#, स्पंदन, इलेक्ट्रॉन |
| नया विंडोज़ जीयूआई विकास | संभव है लेकिन समुदाय सिकुड़ रहा है | सी# (डब्ल्यूपीएफ/विनयूआई 3) |
| वेब विकास | अनुकूल नहीं | जावास्क्रिप्ट, पायथन, सी# |
| मोबाइल ऐप्स | एफएमएक्स के माध्यम से संभव लेकिन सीमित | स्विफ्ट, कोटलिन, स्पंदन |
---

## सारांश
डेल्फ़ी एक ऐतिहासिक रूप से महत्वपूर्ण भाषा है जिसने विंडोज़ के लिए तीव्र अनुप्रयोग विकास का बीड़ा उठाया है। आधुनिक डेल्फ़ी देशी विंडोज़ अनुप्रयोगों और डेटाबेस फ्रंट-एंड के लिए सक्षम है, लेकिन इसका समुदाय और पारिस्थितिकी तंत्र काफी कम हो गया है। मौजूदा डेल्फ़ी कोडबेस को बनाए रखने के लिए, यह आवश्यक है। नई परियोजनाओं के लिए, अधिकांश डेवलपर्स C#, वेब प्रौद्योगिकियों, या क्रॉस-प्लेटफ़ॉर्म फ़्रेमवर्क में स्थानांतरित हो गए हैं। ओपन-सोर्स फ्री पास्कल/लाजर प्रोजेक्ट ऑब्जेक्ट पास्कल भाषा में रुचि रखने वालों के लिए एक मुफ्त विकल्प प्रदान करता है।