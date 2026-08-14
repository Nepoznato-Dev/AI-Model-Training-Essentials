---
# Metadata
title: "Lisp & Clojure — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Lisp and Clojure ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [lisp, clojure, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Lisp и Clojure — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы Lisp и Clojure.
---

## Реализации Lisp и Clojure
| Реализация | Язык | Заметки |
|---------------|----------|-------|
| **Кложур** | JVM | Современный Лисп на JVM |
| **ClojureScript** | Дж.С. | Clojure скомпилирован в JavaScript |
| **СБКЛ** | Общий Лисп | Высокопроизводительный CL |
| **ККЛ** | Общий Лисп | OpenMCL, быстрая компиляция |
| **ОКУ** | Общий Лисп | Встраиваемый, взаимодействие с C |
| **Emacs Лисп** | Эмакс | Язык расширения |
| **Рэкет** | Схема | Языко-ориентированное программирование |
| **Коварство** | Схема | язык расширений GNU |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Инструменты Clojure
| Инструмент | Цель |
|------|---------|
| **CLI Clojure (clj)** | Официальный инструмент CLI |
| **Лейнинген** | Классический инструмент проекта |
| **deps.edn** | Управление зависимостями |
| **Бабашка** | Быстрое написание сценариев Clojure |
| **инструменты.сборка** | Автоматизация сборки |
| **теневые-cljs** | Сборки ClojureScript |
| **Фиговое колесо** | Живая перезагрузка ClojureScript |
```clojure
;; deps.edn
{:paths ["src" "resources"]
 :deps {org.clojure/clojure {:mvn/version "1.11.1"}
        ring/ring-core {:mvn/version "1.11.0"}
        ring/ring-jetty-adapter {:mvn/version "1.11.0"}
        com.github.seancorfield/next.jdbc {:mvn/version "1.3.909"}}
 
 :aliases
 {:run {:main-opts ["-m" "myapp.core"]}
  :test {:extra-paths ["test"]
         :extra-deps {io.github.cognitect-labs/test-runner {:git/tag "v0.5.1"}}
         :main-opts ["-m" "cognitect.test-runner"]}
  :build {:deps {io.github.clojure/tools.build {:mvn/version "0.9.6"}}
          :ns-default build}}}
```

```bash
clj -M:run                # run with alias
clj -M:test               # run tests
clj -T:build jar          # build JAR
clj -M:nrepl              # start REPL
bb -e '(+ 1 2 3)'        # Babashka inline
```

---

## Общие инструменты Lisp
| Инструмент | Цель |
|------|---------|
| **Квиклисп** | Менеджер пакетов |
| **АСДФ** | Система сборки |
| **Розуэлл** | Менеджер среды Lisp |
| **Клот** | Управление локальными зависимостями |
| **СЛИЗЬ** | Emacs Lisp IDE |
| **Хитрый** | Emacs Lisp IDE (вилка SLIME) |
```lisp
;; Quicklisp
(ql:quickload "hunchentoot")  ; install/load library
(ql:quickload "cl-json")
(ql:update-all-dists)          ; update all

;; ASDF system definition
(asdf:defsystem myapp
  :description "My application"
  :depends-on ("hunchentoot" "cl-json")
  :components ((:file "package")
               (:file "main" :depends-on ("package"))))
```

---

## Веб-фреймворки
| Рамочная | Язык | Тип |
|-----------|----------|------|
| **Кольцо + Компоюре** | Кложур | HTTP-обработчик + маршрутизация |
| **Пьедестал** | Кложур | Полнофункциональный веб-интерфейс |
| **Люминус** | Кложур | Стек веб-фреймворков |
| ** Рейтит** | Кложур | Библиотека маршрутизации |
| **Хунчентут** | КЛ | HTTP-сервер |
| **Пещерный человек** | КЛ | Веб-фреймворк |
| **Рестас** | КЛ | REST-фреймворк |
```clojure
;; Ring + Compojure example
(ns myapp.handler
  (:require [compojure.core :refer [defroutes GET POST]]
            [compojure.route :as route]
            [ring.middleware.json :refer [wrap-json-body wrap-json-response]]
            [ring.adapter.jetty :refer [run-jetty]]))

(defroutes app-routes
  (GET "/" [] "Hello, World!")
  (GET "/users/:id" [id] {:status 200 :body {:id id :name "User"}})
  (route/not-found "Not Found"))

(def app (-> app-routes wrap-json-response (wrap-json-body {:keywords? true})))

(defn -main [] (run-jetty app {:port 8080}))
```

---

## База данных
| Технология | Язык | Тип |
|------------|----------|------|
| **следующий.jdbc** | Кложур | оболочка JDBC |
| **ХугSQL** | Кложур | SQL-сначала |
| **медовыйsql** | Кложур | SQL DSL |
| **clojure.jdbc** | Кложур | JDBC-интерфейс |
| **Постмодерн** | КЛ | PostgreSQL |
| **CLSQL** | КЛ | SQL-интерфейс |
| **SxQL** | КЛ | SQL DSL |
```clojure
;; next.jdbc example
(require '[next.jdbc :as jdbc]
         '[next.jdbc.result-set :as rs])

(def db {:dbtype "postgresql" :dbname "mydb" :user "admin" :password "secret"})

(defn find-users [min-age]
  (jdbc/execute! db
    ["SELECT id, name, email FROM users WHERE age > ?" min-age]
    {:builder-fn rs/as-unqualified-lower-maps}))
```

---

## Тестирование
| Рамочная | Язык | Цель |
|-----------|----------|---------|
| **clojure.test** | Кложур | Встроенное тестирование |
| **мидже** | Кложур | Тестирование в стиле BDD |
| **ожидания** | Кложур | На основе ожиданий |
| **тест.проверка** | Кложур | На основе свойств (QuickCheck) |
| **Пять утра** | КЛ | Модульное тестирование |
| **доказать** | КЛ | Платформа тестирования |
| **лисп-модуль** | КЛ | Модульное тестирование |
```clojure
;; clojure.test
(ns myapp.user-service-test
  (:require [clojure.test :refer [deftest testing is are]]
            [myapp.user-service :as sut]))

(deftest find-user-test
  (testing "returns user when found"
    (let [repo (atom {1 {:id 1 :name "Alice"}})
          user (sut/find-user repo 1)]
      (is (= "Alice" (:name user)))))
  
  (testing "returns nil when not found"
    (let [repo (atom {})
          user (sut/find-user repo 999)]
      (is (nil? user)))))

;; test.check (property-based)
(require '[clojure.test.check :as tc]
         '[clojure.test.check.generators :as gen]
         '[clojure.test.check.properties :as prop])

(tc/quick-check 100
  (prop/for-all [v (gen/vector gen/int)]
    (= (sort v) (sort (sort v)))))
```

---

## Качество кода
| Инструмент | Язык | Цель |
|------|----------|---------|
| **clj-кондо** | Кложур | Линтер |
| **cljfmt** | Кложур | Форматер |
| **Иствуд** | Кложур | Линтинг |
| **кибит** | Кложур | Предложения по коду |
| **Алекс и Терри** | Кложур | Руководство по стилю |
| **Алекс-плюс** | КЛ | Анализ кода |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Ключевые библиотеки
| Библиотека | Язык | Цель |
|---------|----------|---------|
| **core.async** | Кложур | Параллелизм CSP |
| **преобразователи** | Кложур | Составные алгоритмы |
| **призрак** | Кложур | Навигация по данным |
| **схема** | Кложур | Проверка данных |
| **малли** | Кложур | Проверка данных |
| **data.json** | Кложур | JSON |
| **Чешир** | Кложур | JSON (быстрее) |
| **икота** | Кложур | Генерация HTML |
| **переосмыслить** | Кложурескрипт | СПА-структура |
| **реагент** | Кложурескрипт | Обертка React |
| **Ом** | Кложурескрипт | Реагировать на интерфейс |
| **core.match** | Кложур | Сопоставление с образцом |
| **инструменты.ведение** | Кложур | Ведение журнала |
| **монтировать** | Кложур | Государственное управление |
| **интегрант** | Кложур | Система компонентов |
| **usocket** | КЛ | Библиотека сокетов |
| **бордо-нити** | КЛ | Резьба |
| **Александрия** | КЛ | Библиотека утилит |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **VS Code + Кальва** | Лучшая Clojure IDE |
| **СИДР (Emacs)** | Классическая среда разработки Clojure |
| **IntelliJ + Курсив** | JetBrains Clojure |
| **СЛИЗЬ / Хитрый** | Общий Лисп (Emacs) |
| **Лем** | Общая среда разработки Lisp |
| **Вим + Камин** | Вим Clojure |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Уберджар** | `clj -T:build jar`(Clojure) |
| **Встроенный GraalVM** | Исходное изображение (ограничено) |
| **Докер** | Контейнерный |
| **Бабашка** | Быстрое создание сценариев |
| **Двоичный файл Lisp** | Скомпилированный двоичный файл (SBCL) |
| **Кубернетес** | Оркестровка |
---

## Краткое содержание
Экосистема Lisp охватывает несколько диалектов: **Clojure** (JVM, современный), **Common Lisp** (классический, ANSI), **Racket** (ориентированный на язык) и **Emacs Lisp** (сценарий редактора). Стандартный стек Clojure: **Clojure CLI** с **deps.edn** для сборок, **Ring + Compojure** или **Pedestal** для Интернета, **next.jdbc** для баз данных, **clojure.test** для тестирования, **clj-kondo** для анализа и **VS Code + Calva** или **CIDER** в качестве IDE. Common Lisp использует **Quicklisp** для пакетов, **SBCL** для компиляции и **SLIME** для разработки. Сильными сторонами Lisp являются макросы, гомоиконичность, разработка на основе REPL и интерактивное программирование. Экосистема превосходно справляется с быстрым прототипированием, предметно-ориентированными языками и обработкой данных.