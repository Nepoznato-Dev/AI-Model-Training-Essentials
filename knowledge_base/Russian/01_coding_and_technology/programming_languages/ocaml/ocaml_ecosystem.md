---
# Metadata
title: "OCaml — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the OCaml ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ocaml, ecosystem, tooling, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "13 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# OCaml — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы OCaml.
---

## Реализации OCaml
| Реализация | Заметки |
|---------------|-------|
| **OCaml 5** | Текущий, с эффектами и параллелизмом |
| **OCaml 4.14** | Последняя версия 4.x (широко используемая) |
| **Причина** | Альтернативный синтаксис (Facebook) |
| **Рескрипт** | Преемник Modern Reason (BuckleScript) |
| **Встроенный OCaml** | Скомпилировано в собственный код |
| **js_of_ocaml** | Компилировать в JavaScript |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## Инструменты сборки и управление пакетами
| Инструмент | Цель |
|------|---------|
| **Дюна** | Система сборки (стандартная) |
| **опам** | Менеджер пакетов |
| **ocamlfind** | Поиск библиотеки |
| **проект дюны** | Конфигурация проекта |
| **эси** | Альтернативный менеджер пакетов |
```bash
# opam
opam init                 # initialize
opam install dune         # install package
opam list                 # list installed
opam update               # update index
opam upgrade              # upgrade packages

# Create project
dune init proj myapp      # new project
dune build                # build
dune runtest              # run tests
```

```lisp
;; dune-project
(lang dune 3.12)
(name myapp)
(generate_opam_files true)

;; dune (executable)
(executable
 (public_name myapp)
 (name main)
 (libraries core async cohttp-lwt-unix))

;; dune (library)
(library
 (name mylib)
 (public_name mylib)
 (libraries core))
```

```opam
# myapp.opam
opam-version: "2.0"
synopsis: "My OCaml application"
depends: [
  "ocaml" {>= "5.0"}
  "dune" {>= "3.0"}
  "core" {>= "v0.16"}
  "async" {>= "v0.16"}
]
```

---

## Веб-фреймворки
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **Мечта** | Полный стек | Современный Интернет (по мотивам Express) |
| **Коhttp** | HTTP | HTTP-клиент/сервер |
| **Опиум** | Легкий | в духе Синатры |
| **Оксиген** | Полный стек | Элиом (клиент-сервер) |
| **Морф** | Легкий | Веб-фреймворк |
| **Lwt** | Асинхронный | Совместная резьба |
| **Асинхронный** | Асинхронный | Асинхронность Джейн Стрит |
```ocaml
(* Dream example *)
let () =
  Dream.run
  @@ Dream.logger
  @@ Dream.router [
       Dream.get "/" (fun _ -> Dream.html "Hello, World!");
       Dream.get "/users/:id" (fun req ->
         let id = Dream.param "id" req in
         Dream.json {|{"id": "|} ^ id ^ {|"}|});
     ]
```

---

## База данных
| Технология | Тип |
|------------|------|
| **Какти** | Типобезопасная база данных |
| **PG'OCaml** | PostgreSQL (типобезопасный) |
| **sqlite3-ocaml** | Привязки SQLite |
| **mysql-ocaml** | Привязки MySQL |
| **postgresql-ocaml** | Привязки PostgreSQL |
| **Ирмин** | Git-подобная база данных |
```ocaml
(* Caqti example *)
module Db = Caqti_connect_sig(S)

let find_user (module Db : Db) id =
  Db.find_opt
    (Caqti_type.(int ->! t2 int string)
       "SELECT id, name FROM users WHERE id = ?")
    id
```

---

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **Алкотест** | Быстрое и красочное тестирование |
| **Юнит** | Модульное тестирование (в стиле xUnit) |
| **QCheck** | Тестирование на основе свойств |
| **Лом** | Фазз-тестирование |
| **ppx_expect** | Ожидайте тестирования (Джейн Стрит) |
```ocaml
(* Alcotest example *)
let test_find () =
  let service = UserService.create () in
  let user = UserService.find service 1 in
  Alcotest.(check (option string)) "found user" (Some "Alice") (Option.map User.name user)

let test_not_found () =
  let service = UserService.create () in
  let user = UserService.find service 999 in
  Alcotest.(check (option string)) "not found" None (Option.map User.name user)

let () =
  Alcotest.run "UserService" [
    "find", [
      Alcotest.test_case "finds user" `Quick test_find;
      Alcotest.test_case "not found" `Quick test_not_found;
    ];
  ]
```

---

## Качество кода
| Инструмент | Цель |
|------|---------|
| **окамлформат** | Форматирование кода |
| **ocp-отступ** | Отступ |
| **ocaml-lsp** | Языковой сервер |
| **ппкс** | Расширения синтаксиса |
| **мерлин** | Поддержка IDE (дополнения, типы) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **Ядро/База** | Стандартная библиотека Джейн Стрит |
| **Stdlib** | Стандартная библиотека OCaml |
| **Результат** | Обработка ошибок |
| **Контейнеры** | Структуры данных |
| **Батареи** | Расширенная стандартная библиотека |
| **Lwt** | Легкие нитки |
| **Асинхронный** | Асинхронное программирование |
| **Эйо** | Ввод-вывод на основе эффектов (OCaml 5) |
| **Домен** | Параллелизм (OCaml 5) |
| **ppx_deriving** | Вывод функций |
| **ppx_yojson_conv** | Получение JSON |
| **йойсон** | Разбор JSON |
| **ангстрем** | Парсер-комбинаторы |
| **менгир** | Генератор парсера |
| **окамлграф** | Библиотека графов |
| **Зарит** | Произвольная точность |
| **Юнит** | Тестирование |
---

## Формальные методы
| Инструмент | Цель |
|------|---------|
| **Кок** | Помощник по доказательству (написан на OCaml) |
| **Почему3** | Проверка программы |
| **Альтернативная эргономика** | SMT-решатель |
| **OCaml + доказательства** | Проверенные программы |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **VS Code + платформа ocaml** | Лучший OCaml LSP |
| **Emacs + туарег + мерлин** | Классическая среда OCaml |
| **Вим + Мерлин** | Интеграция с Vim |
| **Neovim + ocaml-lsp** | На базе терминала |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Собственный двоичный файл** | `dune build`создает собственные двоичные файлы |
| **Статическая ссылка** | Полностью статические двоичные файлы |
| **Докер** | Контейнерный |
| **переключатель опама** | Несколько версий OCaml |
| **Кросс-компиляция** | Кросс-компиляция |
---

## Краткое содержание
Экосистема OCaml ориентирована на корректность, производительность и функциональное программирование. Стандартный стек: **OCaml 5** в качестве среды выполнения, **Dune** для сборок, **opam** для пакетов, **Dream** или **Cohttp** для Интернета, **Caqti** для баз данных, **Alcotest** для тестирования, **ocamlformat** для форматирования и **Merlin** для поддержки IDE. OCaml превосходно справляется с компиляторами, формальной проверкой, финансовыми системами и везде, где важны правильность и производительность. Система эффектов и параллелизм (домены) OCaml 5 привносят в язык современный параллелизм. Экосистема необходима для создания компиляторов (Coq, F*), средств доказательства теорем и высоконадежного программного обеспечения.