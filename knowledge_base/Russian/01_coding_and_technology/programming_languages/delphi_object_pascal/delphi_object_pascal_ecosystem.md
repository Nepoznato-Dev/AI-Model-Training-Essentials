<!--
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

-->
# Delphi/Object Pascal — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы Delphi/Object Pascal.
---

## Версии и компиляторы Delphi
| Компилятор | Платформа | Заметки |
|----------|----------|-------|
| **Делфи 12 Афины** | Кроссплатформенный | Последний выпуск Embarcadero |
| **Фри Паскаль (FPC)** | Кроссплатформенный | Компилятор Pascal с открытым исходным кодом |
| **Лазарь** | Кроссплатформенный | Бесплатная IDE для Паскаля (например, Delphi) |
| **Сообщество Delphi** | Окна | Бесплатная версия (ограниченная) |
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
| IDE | Сильные стороны |
|-----|-----------|
| **IDE для Delphi** | Полнофункциональный инструмент RAD (Embarcadero) |
| **Лазарь** | Бесплатно, с открытым исходным кодом (FPC) |
| **VS Code + Паскаль** | Легкое редактирование |
---

## Фреймворки графического интерфейса
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **ВКЛ** | Родной для Windows | Настольные приложения для Windows |
| **FireMonkey (FMX)** | Кроссплатформенный | Windows, macOS, iOS, Android |
| **ЛКЛ** | Кроссплатформенный | Библиотека компонентов Lazarus |
| **DelphiMVC** | Интернет | MVC-фреймворк |
| **Веб-ядро TMS** | Интернет | Веб-приложения от Delphi |
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

## База данных
| Технология | Тип |
|------------|------|
| **FireDAC** | Универсальный доступ к базе данных (Embarcadero) |
| **дбЭкспресс** | Легкая база данных |
| **АДО** | Объекты данных ActiveX |
| **Зеослиб** | Компоненты базы данных с открытым исходным кодом |
| **SQLite3** | Встроенная поддержка SQLite |
| **ИнтерБаза** | Встроенная база данных Embarcadero |
| **ИнтерСистемс ИРИС** | База данных объектов |
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

## Веб-разработка
| Технология | Тип |
|------------|------|
| **DelphiMVC** | Веб-фреймворк MVC |
| **Веб-ядро TMS** | Веб-приложения от Delphi |
| **ИнтраВеб** | Веб-приложения |
| **мОРМот** | Структура REST/SOA |
| **Delphi-WebRTC** | Общение в режиме реального времени |
| **Инди** | Интернет-компоненты (HTTP, SMTP и т. д.) |
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

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **ДУнит** | Модульное тестирование (встроенное) |
| **DUnitX** | Современная среда тестирования |
| **МокФабрика** | Издевательство |
| **DelphiMock** | Издевательская библиотека |
| **FinalBuilder** | Автоматизация сборки |
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

## Качество кода
| Инструмент | Цель |
|------|---------|
| **Покрытие кода Delphi** | Покрытие кода |
| **Анализатор Паскаля** | Статический анализ |
| **GExperts** | Экспертные инструменты IDE |
| **ДелфиЛинт** | Линтинг |
---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **System.SysUtils** | Утилиты для работы со строками и датами |
| **Система.Классы** | Потоки, коллекции |
| **System.Generics** | Общие типы |
| **Система.Поточность** | Параллельное программирование |
| **Инди** | Интернет-протоколы |
| **Синапс** | Сетевая библиотека |
| **Весна4Д** | Библиотека утилит (например, Boost) |
| **DWScript** | Скриптовый движок |
| **JCL/JVCL** | Библиотека джедаев |
| **Графика32** | Графическая библиотека |
| **Алкиноя** | Библиотека компонентов |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Родная версия Windows** | .exe-файлы |
| **macOS** | Приложения FireMonkey |
| **iOS/Android** | FireMonkey для мобильных устройств |
| **Линукс** | Серверная часть Delphi |
| **Докер** | Контейнерный |
| **Настройка Inno** | Установщик Windows |
| **НСИС** | Установщик Windows |
---

## Краткое содержание
Экосистема Delphi сосредоточена на быстрой разработке приложений (RAD) для настольных компьютеров, мобильных устройств и Интернета. Стандартный стек: **Delphi 12** в качестве IDE/компилятора, **VCL** для рабочего стола Windows, **FireMonkey** для кроссплатформенности, **FireDAC** для доступа к базе данных, **DUnitX** для тестирования и **Spring4D** для утилит. Бесплатная альтернатива — **Free Pascal** + **Lazarus**. Delphi преуспевает в настольных приложениях Windows, приложениях баз данных и быстром прототипировании. Экосистема необходима для поддержки обширной установленной базы приложений Delphi на предприятиях, в здравоохранении и государственном секторе.