---
# Metadata
title: "Delphi / Object Pascal — Syntax Reference"
description: "Detailed syntax reference for Delphi/Object Pascal covering operators, control flow, classes, interfaces, generics, records, properties, and advanced OOP patterns."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [delphi, object-pascal, syntax-reference, oop, generics, vcl, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Delphi / Object Pascal — Sözdizimi Referansı
Bu belge Delphi/Object Pascal için kapsamlı, yapılandırılmış bir sözdizimi referansı sağlar. Kapsamlı sözdizimi kalıplarına, OOP özelliklerine, jeneriklere, kayıtlara ve dil deyimlerine odaklanarak ana Delphi referansını tamamlar.
---

## Operatörler ve İfadeler
| Kategori | Operatör | Açıklama | Örnek |
|----------|----------|------------|-----------|
| **Aritmetik** | `+`| İlave | `A + B`|
| | `-`| Çıkarma | `A - B`|
| | `*`| Çarpma | `A * B`|
| | `/`| Gerçek bölüm | `A / B`(her zaman Real değerini döndürür) |
| | `div`| Tamsayı bölümü | `A div B`(Tamsayıyı döndürür) |
| | `mod`| Modül | `A mod B`|
| **Karşılaştırma** | `=`| Eşit | `A = B`|
| | `<>`| Eşit değil | `A <> B`|
| | `<`| |'dan az | `A < B`|
| | `>`| Şundan büyük: | `A > B`|
| | `<=`| Daha az veya eşit | `A <= B`|
| | `>=`| Büyük veya eşit | `A >= B`|
| **Mantıksal** | `and`| Mantıksal VE | `A and B`|
| | `or`| Mantıksal VEYA | `A or B`|
| | `not`| Mantıksal DEĞİL | `not A`|
| | `xor`| Özel VEYA | `A xor B`|
| **Dize** | `+`| birleştirme | `'Hello' + ' ' + 'World'`|
| **Ayarla** | `in`| Üyelik | `X in [1, 2, 3]`|
| | `+`| Birliği | `SetA + SetB`|
| | `-`| Fark | `SetA - SetB`|
| | `*`| Kavşak | `SetA * SetB`|
| **Ödev** | `:=`| Değer ata | `X := 42`|
| **Adres** | `@`| Adresi | `P := @X`|
| | `^`| Referans | `P^`|
---

## Akışı Kontrol Et
```pascal
// If-then-else
if X > 0 then
  WriteLn('Positive')
else if X = 0 then
  WriteLn('Zero')
else
  WriteLn('Negative');

// Case statement
case DayOfWeek of
  1: WriteLn('Monday');
  2: WriteLn('Tuesday');
  3, 4, 5: WriteLn('Midweek');
  6..7: WriteLn('Weekend');
else
  WriteLn('Invalid day');
end;

// For loop (known count)
for I := 1 to 10 do
  WriteLn(I);

for I := 10 downto 1 do
  WriteLn(I);

// While loop (condition first)
while X > 0 do
begin
  WriteLn(X);
  Dec(X);
end;

// Repeat-until loop (condition last, executes at least once)
repeat
  WriteLn(X);
  Dec(X);
until X = 0;

// For-in loop (enumerable collections)
for Item in Collection do
  Process(Item);

// Inline variable declaration (Delphi 10.3+)
for var I := 0 to List.Count - 1 do
  WriteLn(List[I]);
```

---

## Veri Türleri ve Değişkenler
```pascal
// Scalar types
var
  B: Boolean;          // True or False
  C: Char;             // Single character
  I: Integer;          // 32-bit signed integer
  L: Int64;            // 64-bit signed integer
  D: Double;           // 64-bit floating point
  E: Extended;         // 80-bit floating point (x86)
  S: string;           // Unicode string (reference-counted)
  SA: AnsiString;      // ANSI string

// Enumerated types
type
  TColor = (Red, Green, Blue, Yellow);
  TDay = (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday);

var
  MyColor: TColor;
  Today: TDay;

begin
  MyColor := Green;
  Today := Monday;
  if Ord(MyColor) = 1 then WriteLn('Green is index 1');
end;

// Subrange types
type
  TPercent = 0..100;
  TLetter = 'A'..'Z';

// Set types
type
  TColors = set of TColor;
  TDigits = set of 0..9;

var
  Palette: TColors;
begin
  Palette := [Red, Blue];
  Include(Palette, Green);
  if Green in Palette then WriteLn('Has green');
end;

// Records (value types)
type
  TPoint = record
    X: Double;
    Y: Double;
    function DistanceTo(const Other: TPoint): Double;
  end;

  TPoint3D = record
    X, Y, Z: Double;
    class function Origin: TPoint3D; static;
    class operator Add(const A, B: TPoint3D): TPoint3D;
  end;

class operator TPoint3D.Add(const A, B: TPoint3D): TPoint3D;
begin
  Result.X := A.X + B.X;
  Result.Y := A.Y + B.Y;
  Result.Z := A.Z + B.Z;
end;
```

---

## Sınıflar ve OOP
```pascal
type
  // Base class
  TShape = class
  private
    FColor: TColor;
    FVisible: Boolean;
  protected
    procedure SetColor(const Value: TColor); virtual;
    function GetArea: Double; virtual; abstract;
  public
    constructor Create; virtual;
    destructor Destroy; override;
    procedure Draw; virtual;
    property Color: TColor read FColor write SetColor;
    property Visible: Boolean read FVisible write FVisible default True;
  end;

  // Derived class
  TCircle = class(TShape)
  private
    FRadius: Double;
  protected
    function GetArea: Double; override;
  public
    constructor Create; override;
    constructor CreateWithRadius(ARadius: Double);
    property Radius: Double read FRadius write FRadius;
  end;

  // Abstract class
  TAnimal = class abstract
  public
    function Speak: string; virtual; abstract;
    procedure Feed; virtual;
  end;

  // Sealed class (cannot be inherited)
  TFinalClass = class sealed
  end;

  // Class with class methods and class vars
  TCounter = class
  private
    class var FCount: Integer;
  public
    class procedure Increment; static;
    class function GetCount: Integer; static;
    class constructor Create;  // Class constructor (runs once)
  end;

constructor TShape.Create;
begin
  inherited Create;
  FColor := Red;
  FVisible := True;
end;

destructor TShape.Destroy;
begin
  // Cleanup
  inherited;
end;

constructor TCircle.CreateWithRadius(ARadius: Double);
begin
  inherited Create;
  FRadius := ARadius;
end;

function TCircle.GetArea: Double;
begin
  Result := Pi * FRadius * FRadius;
end;
```

---

## Arayüzler
```pascal
type
  // Interface definition (GUID required for COM interop)
  ISerializable = interface
    ['{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}']
    function Serialize: string;
    procedure Deserialize(const AData: string);
  end;

  IPrintable = interface
    ['{B2C3D4E5-F6A7-8901-BCDE-F12345678901}']
    function ToString: string;
    procedure Print;
  end;

  // Class implementing multiple interfaces
  TDocument = class(TInterfacedObject, ISerializable, IPrintable)
  private
    FContent: string;
  public
    function Serialize: string;
    procedure Deserialize(const AData: string);
    function ToString: string; override;
    procedure Print;
  end;

// Usage with automatic reference counting
var
  Doc: ISerializable;
begin
  Doc := TDocument.Create;  // No Free needed — interface ref counting
  Doc.Serialize;
end;
```

---

## Jenerikler
```pascal
type
  // Generic class
  TRepository<T: class, constructor> = class
  private
    FItems: TObjectList<T>;
  public
    constructor Create;
    destructor Destroy; override;
    procedure Add(const AItem: T);
    function FindById(AId: Integer): T;
    function GetAll: TArray<T>;
    property Count: Integer read GetCount;
  end;

  // Generic record with constraints
  TOptional<T> = record
  private
    FValue: T;
    FHasValue: Boolean;
  public
    class function Empty: TOptional<T>; static;
    class function Of(const AValue: T): TOptional<T>; static;
    function HasValue: Boolean;
    function GetValue: T;
    function GetValueOrDefault(const ADefault: T): T;
  end;

  // Generic method
  TUtils = class
  public
    class function Max<T>(const A, B: T): T; static;
    class procedure Swap<T>(var A, B: T); static;
  end;

  // Generic interface
  IComparer<T> = interface
    function Compare(const A, B: T): Integer;
  end;
```

---

## İstisna İşleme
```pascal
// Try-except-finally
try
  Stream := TFileStream.Create('data.bin', fmOpenRead);
  try
    Stream.ReadBuffer(Buffer, SizeOf(Buffer));
    ProcessData(Buffer);
  except
    on E: EReadError do
      WriteLn('Read error: ', E.Message);
    on E: EStreamError do
      WriteLn('Stream error: ', E.Message);
    on E: Exception do
      WriteLn('Unexpected: ', E.ClassName, ' - ', E.Message);
  end;
finally
  Stream.Free;  // Always executed
end;

// Custom exceptions
type
  EValidationError = class(Exception)
  private
    FField: string;
  public
    constructor Create(const AField, AMessage: string);
    property Field: string read FField;
  end;

raise EValidationError.Create('Email', 'Invalid email format');
```

---

## Özet
Delphi/Object Pascal, temiz, okunabilir sözdizimini güçlü OOP özellikleriyle birleştirir. Sınıflar, arayüzler, jenerikler ve kayıtlar, uygulama geliştirme için eksiksiz bir araç seti sağlar. Dilin açık başlangıç/bitiş blokları, yazılan değişkenler ve büyük/küçük harfe duyarlı olmayan tanımlayıcılar onu ulaşılabilir kılar. VCL/FMX çerçeveleri, hızlı uygulama geliştirme için dili görsel bileşen kitaplıklarıyla genişletir. Kurumsal Windows uygulamaları ve veritabanı ön uçları için Delphi üretken bir seçim olmaya devam ediyor.