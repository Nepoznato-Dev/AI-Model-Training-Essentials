---
# Metadata
title: "Ruby — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ruby ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ruby, ecosystem, tooling, rails, gems, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ruby — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы Ruby.
---

## Реализации Ruby
| Реализация | Заметки |
|---------------|-------|
| **CRuby (МРТ)** | По умолчанию, наиболее широко используемый |
| **JРубин** | Взаимодействие с Java на основе JVM |
| **ТрюфельРубин** | Высокая производительность на базе GraalVM |
| **мруби** | Легкий, встраиваемый |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Управление пакетами
| Инструмент | Цель |
|------|---------|
| **RubyGems** | Встроенный менеджер пакетов драгоценных камней |
| **Бандлер** | Управление зависимостями (Gemfile) |
| **rubygems.org** | Официальный репозиторий драгоценных камней |
```ruby
# Gemfile
source "https://rubygems.org"

gem "rails", "~> 7.1"
gem "pg", "~> 1.5"
gem "puma", "~> 6.0"
gem "redis", "~> 5.0"

group :development, :test do
  gem "rspec", "~> 3.12"
  gem "rubocop", "~> 1.50"
  gem "debug"
end
```

```bash
bundle install          # install dependencies
bundle update           # update gems
bundle exec rspec       # run with bundled gems
```

---

## Веб-фреймворки
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **Рельсы** | Полный стек | Соглашение важнее конфигурации |
| **Синатра** | Микро | Простые API, небольшие приложения |
| **Ханами** | Чистая арка. | Удобные в обслуживании и тестируемые приложения |
| **Рода** | Дерево маршрутизации | Высокая производительность, гибкость |
| **Виноград** | ОТДЫХ API | Платформа, ориентированная на API |
| **Стойка** | Интерфейс | Низкоуровневый интерфейс веб-сервера |
```ruby
# Sinatra example
require "sinatra"

get "/hello" do
  "Hello, #{params[:name] || 'World'}!"
end

get "/users/:id" do
  user = User.find(params[:id])
  json user
end
```

```ruby
# Rails controller example
class UsersController < ApplicationController
  def index
    @users = User.order(:name).page(params[:page])
    render json: @users
  end

  def create
    @user = User.new(user_params)
    if @user.save
      render json: @user, status: :created
    else
      render json: @user.errors, status: :unprocessable_entity
    end
  end
end
```

---

## База данных и ORM
| Технология | Тип |
|------------|------|
| **Активная запись** | Rails ORM (на основе соглашений) |
| **Продолжение** | Гибкая и мощная ORM |
| **ROM (сопоставитель объектов Ruby)** | Функциональный, сборный |
| **стр** | Адаптер PostgreSQL |
| **mysql2** | MySQL-адаптер |
| **SQLite3** | SQLite-адаптер |
| **Монгоид** | MongoDB ODM |
| **Редис** | Хранилище ключей и значений |
---

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **RСпец** | Тестирование в стиле BDD (самое популярное) |
| **Минитест** | Встроенный, легкий |
| **Капибара** | Интеграция/браузерное тестирование |
| **ФабрикаБот** | Фабрики тестовых данных |
| **Фейкер** | Генерация фейковых данных |
| **ВебМок** | Заглушка HTTP-запроса |
| **ПростойКов** | Покрытие кода |
| **Видеомагнитофон** | Запись/воспроизведение HTTP-взаимодействий |
| **Полицейский** | Манипулирование временем в тестах |
```ruby
# RSpec example
RSpec.describe UserService do
  subject(:service) { described_class.new(repository) }

  describe "#find" do
    it "returns the user when found" do
      user = build(:user, name: "Alice")
      allow(repository).to receive(:find).with(1).and_return(user)

      result = service.find(1)

      expect(result.name).to eq("Alice")
    end

    it "raises NotFound when missing" do
      allow(repository).to receive(:find).and_raise(NotFound)

      expect { service.find(999) }.to raise_error(NotFound)
    end
  end
end
```

---

## Качество кода
| Инструмент | Цель |
|------|---------|
| **РубоКоп** | Линтер и форматтер |
| **СтандартныйRB** | Самоуверенный конфиг Рубокопа |
| **Вонь** | Код обнаружения запаха |
| **Тормозной мастер** | Сканер уязвимостей безопасности |
| **Бандлер-аудит** | Проверка уязвимостей Gem |
| **ПростойКов** | Покрытие кода |
| **Солнечная диаграмма** | Языковой сервер, документы YARD |
```yaml
# .rubocop.yml
AllCops:
  TargetRubyVersion: 3.3
  NewCops: enable

Style/Documentation:
  Enabled: false

Layout/LineLength:
  Max: 120
```

---

## Средства запуска задач и интерфейс командной строки
| Инструмент | Цель |
|------|---------|
| **Рейк** | Запуск задач (похож на Make) |
| **Тор** | CLI-фреймворк |
| **Консоль Rails** | Интерактивная среда Rails |
| **Тор** | Создайте мощные инструменты CLI |
| **Драйран** | Тестирование CLI для драгоценных камней |
---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **Рельсы** | Полнофункциональный веб-фреймворк |
| **Совместитель** | Обработка фоновых заданий |
| **Разработать** | Аутентификация |
| **Эксперт** | Авторизация |
| **Пума** | Веб-сервер |
| **Стойка** | Интерфейс веб-сервера |
| **Нокогири** | Парсинг HTML/XML |
| **Фарадей** | HTTP-клиент |
| **httpвечеринка** | Простые HTTP-запросы |
| **Активная поддержка** | Классы полезности (Rails) |
| **Сухой-рб** | Функциональные библиотеки Ruby |
| **Ханами::Утилиты** | Легкие коммунальные услуги |
| **Прай** | Консоль разработчика/отладчик |
| **дотенв** | Переменные среды |
| **фигаро** | Конфигурация приложения |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **РубиМайн** | Полная версия IDE JetBrains Ruby |
| **VS Code + Solargraph** | Легкий, на основе LSP |
| **Вим/Неовим + рубин-lsp** | На базе терминала |
| **TextMate** | Классический редактор macOS |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Пума** | Веб-сервер Rails по умолчанию |
| **Пассажир** | Модуль Apache/Nginx |
| **Капистрано** | Удаленное развертывание нескольких серверов |
| **Докер** | Контейнерное развертывание |
| **Хероку** | PaaS (совместимый с Ruby) |
| **Fly.io** | Платформа хостинга приложений |
| **Железная дорога** | Современный PaaS |
| **Камаль (Базовый лагерь)** | Развертывание на основе Docker |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Краткое содержание
Экосистема Ruby ориентирована на счастье разработчиков и согласие, а не на конфигурацию. Стандартный стек: **Ruby 3.3+** в качестве среды выполнения, **Bundler** для зависимостей, **Rails** для полнофункционального веб-приложения (или **Sinatra** для микроприложений), **RSpec** для тестирования, **RuboCop** для анализа, **Sidekiq** для фоновых заданий и **Puma** в качестве веб-сервера. Ruby превосходно справляется с быстрым прототипированием, веб-приложениями, написанием сценариев и инструментами CLI. Экосистема RubyGems насчитывает более 170 000 пакетов. Ruby 3.x включает в себя Ractor для параллелизма, RBS для статической типизации и сопоставления с образцом.