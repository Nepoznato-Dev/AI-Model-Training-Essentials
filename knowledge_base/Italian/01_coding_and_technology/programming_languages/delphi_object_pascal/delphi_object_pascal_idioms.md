---
# Metadata
title: "Delphi / Object Pascal — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean Delphi and Object Pascal code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [delphi, object-pascal, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Delphi / Object Pascal: modelli idiomatici e migliori pratiche
Questa guida copre i modelli idiomatici per scrivere codice Delphi e Object Pascal pulito.
---

## Gestione delle risorse con try/finally
```delphi
// ✅ Always use try/finally for resource cleanup
var
  Stream: TFileStream;
begin
  Stream := TFileStream.Create('data.bin', fmOpenRead);
  try
    // use Stream — guaranteed cleanup even on exception
    ProcessData(Stream);
  finally
    Stream.Free;
  end;
end;

// ✅ Nested resources — each gets its own try/finally
var
  Reader: TStreamReader;
  Writer: TStreamWriter;
begin
  Reader := TStreamReader.Create('input.txt');
  try
    Writer := TStreamWriter.Create('output.txt');
    try
      Writer.Write(Reader.ReadToEnd);
    finally
      Writer.Free;
    end;
  finally
    Reader.Free;
  end;
end;
```

---

## Gestione delle stringhe
```delphi
// ✅ Use Format for complex string building
var
  Msg: string;
begin
  Msg := Format('User %s (%d) logged in at %s',
    [UserName, UserID, FormatDateTime('hh:nn:ss', Now)]);
end;

// ✅ Use TStringBuilder for loops
var
  SB: TStringBuilder;
  I: Integer;
begin
  SB := TStringBuilder.Create;
  try
    for I := 0 to Items.Count - 1 do
    begin
      if I > 0 then SB.Append(', ');
      SB.Append(Items[I]);
    end;
    Result := SB.ToString;
  finally
    SB.Free;
  end;
end;

// ✅ Prefer string helper methods
var
  S: string;
begin
  S := 'Hello World';
  if S.StartsWith('Hello') then ...
  if S.Contains('World') then ...
  S := S.ToUpper;
end;
```

---

## Design e interfacce delle classi
```delphi
// ✅ Use interfaces for loose coupling
type
  ILogger = interface
    ['{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}']
    procedure Log(const Msg: string);
    function GetLevel: TLogLevel;
  end;

  TConsoleLogger = class(TInterfacedObject, ILogger)
  public
    procedure Log(const Msg: string); override;
    function GetLevel: TLogLevel; override;
  end;

// ✅ Use class helpers / class operators for extensions
type
  TMyEnumHelper = record helper for TMyEnum
    function ToString: string;
    class function FromString(const S: string): TMyEnum; static;
  end;

// ✅ Prefer records for simple data carriers
type
  TPoint = record
    X, Y: Double;
    function DistanceTo(const Other: TPoint): Double;
  end;
```

---

## Gestione delle eccezioni
```delphi
// ✅ Catch specific exceptions
try
  Value := StrToInt(UserInput);
except
  on E: EConvertError do
    ShowMessage('Invalid number: ' + UserInput);
  on E: EOverflow do
    ShowMessage('Number too large');
end;

// ✅ Use custom exception classes
type
  EBusinessRuleViolation = class(Exception)
  public
    constructor Create(const FieldName, Reason: string);
  end;

// ✅ Raise with context
raise EBusinessRuleViolation.Create('Age', 'Must be >= 18');
```

---

## Modelli Delphi moderni
```delphi
// ✅ Anonymous methods & closures
var
  OnComplete: TProc<string>;
begin
  OnComplete := procedure(const Result: string)
    begin
      Log(Result);
      UpdateUI(Result);
    end;
  AsyncProcess(OnComplete);
end;

// ✅ Generics for type-safe collections
type
  TRepository<T: class> = class
  private
    FItems: TObjectList<T>;
  public
    function Find(const Predicate: TPredicate<T>): T;
    procedure Save(const Item: T);
  end;

// ✅ Inline variables (Delphi 10.3+)
begin
  var Count := Items.Count;
  for var Item in Items do
    Process(Item);
end;
```

---

## Riepilogo
Gli idiomi Delphi enfatizzano:`try/finally`per la pulizia deterministica delle risorse,`Format`per la creazione di stringhe, interfacce per accoppiamento lento, record per supporti dati, gestione specifica delle eccezioni e funzionalità moderne come metodi generici e anonimi. Delphi valorizza la gestione esplicita delle risorse: "creala, usala, liberala finalmente".