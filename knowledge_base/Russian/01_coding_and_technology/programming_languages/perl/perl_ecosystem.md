<!--
---
# Metadata
title: "Perl — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Perl ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [perl, ecosystem, tooling, cpan, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "13 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Perl — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы Perl.
---

## Версии Perl
| Версия | Заметки |
|---------|-------|
| **Перл 5.38+** | Текущая стабильная |
| **Перл 5.40** | Последняя с новыми функциями |
| **Раку (Perl 6)** | Современный редизайн (отдельный язык) |
| **Лось** | Современная ОО-система |
| **Му** | Легкий лось |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Управление пакетами
| Инструмент | Цель |
|------|---------|
| **CPAN** | Комплексная сеть архивов Perl (более 200 000 модулей) |
| **cpanm** | Легкий установщик CPAN |
| **cpanfile** | Декларация зависимости |
| **Коробка** | Сборщик зависимостей (например, Bundler) |
| **Расстояние::Зилла** | Строитель дистрибутива |
| **Приложение::cpanminus** | Минимальный клиент CPAN |
```bash
cpanm Module::Name          # install module
cpanm --installdeps .       # install from cpanfile
cpanm --self-upgrade        # upgrade cpanm
carton install              # install from cpanfile (Carton)
carton exec perl script.pl  # run with bundled deps
```

```perl
# cpanfile
requires 'perl', '5.038';
requires 'Mojolicious', '>= 9.0';
requires 'DBI', '>= 1.643';
requires 'JSON::XS';

on 'test' => sub {
    requires 'Test::More', '>= 1.302';
    requires 'Test::Fatal';
    requires 'Test::MockModule';
};
```

---

## Веб-фреймворки
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **Веселый** | Полный стек | Современный, чистый, с батарейками |
| **Танцовщица2** | Микро | Легкий, похожий на Синатру |
| **Катализатор** | Полный стек | Предприятие, MVC |
| **Плак** | Инструментарий PSGI | Низкоуровневый веб-интерфейс |
| **Звездный человек** | HTTP-сервер | PSGI-сервер |
```perl
# Mojolicious::Lite example
use Mojolicious::Lite -signatures;

get '/hello' => sub ($c) {
    $c->render(text => 'Hello, World!');
};

get '/users/:id' => sub ($c) {
    my $id = $c->param('id');
    my $user = $c->users->find($id);
    $c->render(json => $user);
};

post '/users' => sub ($c) {
    my $data = $c->req->json;
    my $user = $c->users->create($data);
    $c->render(json => $user, status => 201);
};

app->start;
```

```perl
# Dancer2 example
use Dancer2;

get '/hello' => sub {
    return "Hello, World!";
};

get '/users/:id' => sub {
    my $id = route_parameters->get('id');
    my $user = schema->resultset('User')->find($id);
    return to_json($user);
};

dance;
```

---

## База данных
| Технология | Тип |
|------------|------|
| **ДБИ** | Стандарт интерфейса базы данных |
| **DBD::SQLite** | Драйвер SQLite |
| **DBD::Pg** | Драйвер PostgreSQL |
| **DBD::mysql** | Драйвер MySQL |
| **DBix::Класс** | Полный ОРМ |
| **Мохо::Pg** | PostgreSQL (Mojolicious) |
| **Редис** | Клиент Redis |
```perl
# DBI example
use DBI;

my $dbh = DBI->connect("dbi:SQLite:dbname=mydb.sqlite", "", "", {
    RaiseError => 1,
    PrintError => 0,
});

my $sth = $dbh->prepare("SELECT * FROM users WHERE age > ?");
$sth->execute(18);

while (my $row = $sth->fetchrow_hashref) {
    print "$row->{name} ($row->{email})\n";
}
```

```perl
# DBIx::Class example
package MyApp::Schema::Result::User;
use base 'DBIx::Class::Core';
__PACKAGE__->table('users');
__PACKAGE__->add_columns(qw/id name email age/);
__PACKAGE__->set_primary_key('id');

# Usage
my @adults = $schema->resultset('User')->search(
    { age => { '>' => 18 } },
    { order_by => 'name' }
);
```

---

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **Тест::Подробнее** | Стандартная среда тестирования |
| **Test2::Suite** | Современное тестирование (рекомендуется) |
| **Тест::Фатальный** | Тестирование исключений |
| **Тест::MockModule** | Издевательство |
| **Тест::Глубокий** | Комплексное сравнение данных |
| **Тест::Вывод** | Захват STDOUT/STDERR |
| **доказать** | Тестовый бегун |
```perl
# Test2::V0 example
use Test2::V0;
use MyApp::UserService;

my $service = MyApp::UserService->new();

subtest 'find user' => sub {
    my $user = $service->find(1);
    is($user->name, 'Alice', 'found user by id');
    ok(defined $user, 'user is defined');
};

subtest 'not found' => sub {
    my $user = $service->find(999);
    is($user, undef, 'returns undef for missing user');
};

done_testing();
```

```bash
prove -lrv t/             # run tests (verbose)
prove -j4 t/              # parallel testing
```

---

## Качество кода
| Инструмент | Цель |
|------|---------|
| **перлкритик** | Линтинг и стиль кода |
| **перлтиди** | Форматирование кода |
| **Девел::Обложка** | Покрытие кода |
| **Perl::Критик** | Применение политики |
| **Тест::Perl::Критик** | Критик в тестах |
```perl
# .perlcriticrc
severity = 3
[Variables::ProhibitPunctuationVars]
severity = 4
```

```bash
perlcritic --brutal lib/  # lint
perltidy -b lib/          # format
```

---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **Лось / Му** | Современная объектная система |
| **Веселый** | Веб-фреймворк |
| **ДБИ** | Интерфейс базы данных |
| **DBix::Класс** | ОРМ |
| **JSON::XS / Cpanel::JSON::XS** | Разбор JSON |
| **ЯМЛ::XS** | Парсинг YAML |
| **LWP::UserAgent** | HTTP-клиент |
| **HTTP::Tiny** | Минимальный HTTP-клиент |
| **IO::Socket::SSL** | SSL/TLS |
| **Параллельно::ForkManager** | Параллельная обработка |
| **MCE** | Многоядерный двигатель |
| **Попробуйте::Tiny** | Обработка исключений |
| **Путь::Крошечный** | Пути к файлам |
| **Список::Util** | Список утилит |
| **Скаляр::Util** | Скалярные утилиты |
| **ДатаВремя** | Обработка даты/времени |
| **Журнал::Любой** | Бревенчатый фасад |
| **Конфигурация::Любая** | Конфигурация |
---

## Обработка текста
| Инструмент | Цель |
|---------|---------|
| **Регулярные выражения** | Встроенный, мощный |
| **Шаблон::Инструментарий** | Шаблонизатор |
| **Текст::CSV** | Анализ CSV |
| **XML::LibXML** | обработка XML |
| **Моджо::DOM** | Парсинг HTML/XML |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **VS-код + Perl** | Поддержка языка Perl |
| **вим-перл** | Поддержка Vim Perl |
| **Emacs + режим cperl** | Классическая среда Perl |
| **Комодо** | ActiveState Perl IDE |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Звездный человек** | Веб-сервер PSGI |
| **Гипножаба** | Модный сервер |
| **Докер** | Контейнерный |
| **PAR::Пакер** | Автономные исполняемые файлы |
| **Коробка** | Зависимости пакета |
| **cpanfile + коробка** | Воспроизводимые развертывания |
---

## Краткое содержание
Экосистема Perl обширна и развита: на CPAN размещено более 200 000 модулей. Стандартный стек: **Perl 5.38+** в качестве среды выполнения, **cpanm** для пакетов, **Mojolicious** для Интернета, **DBI** + **DBIx::Class** для баз данных, **Test2::Suite** для тестирования, **perlcritic** для проверки и **perltidy** для форматирования. Perl превосходно справляется с обработкой текста, системным администрированием, биоинформатикой и устаревшими веб-приложениями. Современный Perl (5.38+) с сигнатурами, разыменованием постфикса и try/catch значительно чище, чем предполагает его репутация. Экосистема идеально подходит для написания сценариев системного администратора, обработки данных и быстрого прототипирования.