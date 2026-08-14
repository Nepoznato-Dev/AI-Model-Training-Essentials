---
# Metadata
title: "Delphi / Object Pascal — Version History & Evolution"
description: "Comprehensive version history and evolution of Delphi/Object Pascal from Turbo Pascal to modern Delphi."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [delphi, object-pascal, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Delphi / Object Pascal — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| Paskal | 1970 | **Niklaus Wirth** Pascal'ı (ETH Zürih) yaratıyor |
| Turbo Paskal 1 | 1983 | **Borland** — hızlı, ucuz, IDE tabanlı (Anders Hejlsberg) |
| Turbo Pascal 3 | 1986 | Birimler, kaplama desteği |
| Turbo Pascal 5 | 1988 | **Entegre hata ayıklayıcı**, IDE iyileştirmeleri |
| Turbo Pascal 5.5 | 1989 | **Nesneye yönelik Pascal** — nesneler, kalıtım |
| Turbo Pascal 6 | 1989 | OOP iyileştirmeleri, birimler |
| Turbo Pascal 7 | 1992 | Son DOS tabanlı Turbo Pascal |
| Delfi 1 | 1995 | **Görsel programlama** — VCL, bileşenler, Windows GUI |
| Delfi 2 | 1996 | 32-bit Windows |
| Delfi 3 | 1997 | COM/ActiveX desteği |
| Delfi 4 | 1998 | Dinamik diziler, fonksiyon aşırı yüklemesi |
| Delfi 5 | 1999 | **ADO**, WebSnap |
| Delfi 6 | 2001 | **Web Hizmetleri**, CLX (platformlar arası) |
| Delfi 7 | 2002 | **En popüler sürüm** — kararlı, hızlı |
| Delfi 8 | 2003 | .NET desteği |
| Delfi 2005 | 2005 | Unicode (kısmi), jenerikler |
| Delfi 2006 | 2006 | **Jenerikler**, anonim yöntemler |
| Delfi 2007 | 2007 | Unicode (tam), Vista desteği |
| Delfi 2009 | 2008 | **Tam Unicode** (UTF-16), RTTI iyileştirmeleri |
| Delfi 2010 | 2009 | RTTI, gelişmiş kayıtlar |
| Delphi XE | 2010 | Platformlar arası hazırlık |
| Delphi XE2 | 2011 | **FireMonkey** — platformlar arası (Windows, macOS) |
| Delphi XE3 | 2012 | **iOS desteği** |
| Delphi XE4 | 2013 | **Android desteği** |
| Delphi XE7 | 2014 | Çoklu cihaz iyileştirmeleri |
| Delphi 10 Seattle | 2015 | Windows 10 desteği |
| Delphi 10.4 Sidney | 2020 | **Yüksek DPI**, geliştirilmiş RTL |
| Delphi 11 İskenderiye | 2021 | **64 bit macOS**, Android 64 bit |
| Delfi 12 Atina | 2023 | **Modern IDE**, geliştirilmiş derleyici |
| Delphı 12.2 | 2024 | Daha fazla iyileştirme |
## Önemli Kilometre Taşları
### Pascal (1970–1982)
- **1970**: Niklaus Wirth, ETH Zürih'te Pascal'ı yarattı
- **Hedef**: Yapılandırılmış programlamayı öğretmek — temiz, tür uyumlu
- Temel özellikler: `record`, `procedure`, `function`,`begin`/ `end`, güçlü yazma
- UCSD Pascal (1978) — taşınabilir, p-kodu makinesi
### Turbo Pascal (1983–1992)
- **1983**: Anders Hejlsberg Borland için Turbo Pascal'ı yarattı
- **Devrim niteliğinde**: Hızlı derleyici, entegre IDE, ucuz (49,95$)
- **5.5 (1989)**: Nesneler — Pascal'da OOP (`object`, kalıtım)
- **7 (1992)**: Son DOS sürümü — efsanevi hız ve güvenilirlik
### Delphi 1–7: Altın Çağ (1995–2002)
- **1995**: Delphi 1 — görsel programlama, VCL (Görsel Bileşen Kütüphanesi)
- **2 (1996)**: 32 bit Windows
- **7 (2002)**: En popüler sürüm — hızlı, kararlı, yaygın olarak kullanılan
- Hızlı Uygulama Geliştirme (RAD) — sürükle ve bırak GUI'si
### Delphi 2005–XE: Modern Özellikler (2005–2010)
- **2006**: Jenerikler, anonim yöntemler
- **2009**: Tam Unicode (UTF-16 dizeleri)
- **2010**: Geliştirilmiş RTTI (yansıma)
### Delphi XE2+: Platformlar Arası (2011 – günümüz)
- **XE2 (2011)**: FireMonkey — platformlar arası çerçeve (Windows, macOS)
- **XE3 (2012)**: iOS desteği
- **XE4 (2013)**: Android desteği
- **11 (2021)**: 64 bit macOS, Android 64 bit
- **12 (2023)**: Modern IDE, geliştirilmiş derleyici
## Söz Dizimi Gelişimi
```pascal
{ Pascal (1970): Structured programming }
program Hello;
var
  Name: string;
begin
  Write('Enter name: ');
  ReadLn(Name);
  WriteLn('Hello, ', Name, '!');
end.

{ Turbo Pascal 5.5 (1989): Objects }
type
  PAnimal = ^TAnimal;
  TAnimal = object
    Name: string;
    procedure Speak; virtual;
  end;

  PDog = ^TDog;
  TDog = object(TAnimal)
    procedure Speak; virtual;
  end;

procedure TDog.Speak;
begin
  WriteLn('Woof!');
end;

{ Delphi 1 (1995): Visual programming, VCL }
type
  TForm1 = class(TForm)
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
  end;

procedure TForm1.Button1Click(Sender: TObject);
begin
  ShowMessage('Hello, Delphi!');
end;

{ Delphi 2006: Generics }
type
  TPair<TKey, TValue> = class
    Key: TKey;
    Value: TValue;
    constructor Create(const AKey: TKey; const AValue: TValue);
  end;

{ Delphi 2009: Unicode strings }
var
  S: string;  { UTF-16 UnicodeString }
begin
  S := 'Hello, 世界!';  { Unicode works natively }
end;

{ Delphi 12 (2023): Modern Delphi }
type
  TMyClass = class
    class function Create: TMyClass; static;
    procedure DoSomething; virtual; abstract;
  end;

  TRecord = record
    Value: Integer;
    class operator Implicit(V: Integer): TRecord;
  end;
```

## Özellik Gelişimi
```
Pascal (1970):     Records, procedures, strong typing, begin/end
Turbo Pascal (1983): Integrated IDE, fast compiler, units
TP 5.5 (1989):     Objects, inheritance, virtual methods
Delphi 1 (1995):   VCL, visual programming, components
Delphi 4 (1998):   Dynamic arrays, overloading
Delphi 2006:       Generics, anonymous methods
Delphi 2009:       Full Unicode (UTF-16)
Delphi XE2 (2011): FireMonkey (cross-platform)
Delphi XE3 (2012): iOS support
Delphi XE4 (2013): Android support
Delphi 11 (2021):  64-bit macOS, Android 64-bit
Delphi 12 (2023):  Modern IDE, improved compiler
```

## Temel Tasarım İlkeleri
```
1. "Type safety" — strong static typing (Wirth's philosophy)
2. "Readability" — begin/end, clear syntax
3. "Visual development" — drag-and-drop GUI (Delphi)
4. "Component-based" — VCL/FMX components
5. "Native compilation" — fast executables (not interpreted)
6. "Cross-platform" — FireMonkey (Windows, macOS, iOS, Android)
7. "Backward compatible" — Turbo Pascal code still compiles
```

## Ekosistem Büyümesi
```
1970: Pascal created by Niklaus Wirth (ETH Zurich)
1983: Turbo Pascal — Borland, Anders Hejlsberg
1989: Turbo Pascal 5.5 — OOP in Pascal
1995: Delphi 1 — visual programming, VCL
2002: Delphi 7 — golden age, most popular version
2006: Generics, anonymous methods
2009: Full Unicode
2011: FireMonkey — cross-platform
2013: Android support
2023: Delphi 12 — modern IDE
2025: Delphi used in:
       - Windows desktop applications (enterprise)
       - Database applications (FireDAC)
       - Cross-platform mobile apps (iOS, Android)
       - Legacy systems (Turbo Pascal, Delphi 7)
       Embarcadero maintains Delphi; Free Pascal (Lazarus) is open source
```
