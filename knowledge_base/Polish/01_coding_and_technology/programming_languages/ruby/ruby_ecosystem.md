<!--
---
# Metadata
title: "Ruby — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ruby ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Ruby — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, frameworki i infrastrukturę w ekosystemie Ruby.
---

## Implementacje Rubiego
| Wdrożenie | Notatki |
|--------------|-------|
| **CRuby (MRI)** | Domyślny, najczęściej używany |
| **JRuby** | Oparta na JVM, współpraca z Java |
| **TruflaRubin** | Oparta na GraalVM, wysoka wydajność |
| **mruby** | Lekki, do osadzania |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **Rubinowe Klejnoty** | Wbudowany menedżer pakietów gem |
| **Bundler** | Zarządzanie zależnościami (Gemfile) |
| **rubygems.org** | Oficjalne repozytorium klejnotów |
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

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **Szyny** | Pełny stos | Konwencja dotycząca konfiguracji |
| **Sinatra** | Mikro | Proste API, małe aplikacje |
| **Hanami** | Czysty łuk. | Utrzymywane, testowalne aplikacje |
| **Roda** | Drzewo routingu | Wysoka wydajność, elastyczność |
| **Winogrona** | API REST | Framework zorientowany na API |
| **Stojak** | Interfejs | Niskopoziomowy interfejs serwera WWW |
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

## Baza danych i ORM
| Technologia | Wpisz |
|------------|------|
| **Aktywny rekord** | Railsy ORM (oparte na konwencji) |
| **Kontynuacja** | Elastyczny, wydajny ORM |
| **ROM (mapowanie obiektów Ruby)** | Funkcjonalne, komponowalne |
| **str.** | Adapter PostgreSQL |
| **mysql2** | Adapter MySQL |
| **SQLite3** | Adapter SQLite |
| **Mongoid** | MongoDB ODM |
| **Redis** | Magazyn klucz-wartość |
---

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **ROSpec** | Testowanie w stylu BDD (najpopularniejsze) |
| **Ministerstwo** | Wbudowany, lekki |
| **Kapibara** | Integracja/testowanie przeglądarki |
| **FabrykaBota** | Fabryki danych testowych |
| **Oszust** | Fałszywe generowanie danych |
| **WebMock** | Odcinanie żądania HTTP |
| **ProstyCov** | Pokrycie kodu |
| **magnetowid** | Nagrywaj/odtwarzaj interakcje HTTP |
| **Czas** | Manipulacja czasem w testach |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **RuboCop** | Linter i formater |
| **StandardowyRB** | Opinia o konfiguracji RuboCop |
| **Smród** | Wykrywanie zapachu kodu |
| **Brakeman** | Skaner luk w zabezpieczeniach |
| **Audyt Bundlera** | Narzędzie do sprawdzania podatności klejnotów |
| **ProstyCov** | Pokrycie kodu |
| **Słoneczny wykres** | Serwer językowy, dokumentacja YARD |
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

## Programy uruchamiające zadania i interfejs CLI
| Narzędzie | Cel |
|------|-------------|
| **Grabie** | Osoba uruchamiająca zadanie (podobna do marki) |
| **Thor** | Struktura CLI |
| **Konsola szynowa** | Interaktywne środowisko Rails |
| **Thor** | Twórz potężne narzędzia CLI |
| **Praca na sucho** | Testuj klejnoty CLI |
---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **Szyny** | Framework WWW z pełnym stosem |
| **Pomocnik** | Przetwarzanie zadań w tle |
| **Wymyśl** | Uwierzytelnianie |
| **Ekspert** | Autoryzacja |
| **Puma** | Serwer WWW |
| **Stojak** | Interfejs serwera WWW |
| **Nokogiri** | Analiza HTML/XML |
| **Faradaya** | Klient HTTP |
| **httpimpreza** | Proste żądania HTTP |
| **Aktywne wsparcie** | Klasy użytkowe (szyny) |
| **Suchy-rb** | Funkcjonalne biblioteki Ruby |
| **Hanami::Narzędzia** | Lekkie narzędzia |
| **Podważ** | Konsola programisty / debugger |
| **dotenv** | Zmienne środowiskowe |
| **Figaro** | Konfiguracja aplikacji |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kopalnia Rubinu** | Pełne Ruby IDE JetBrains |
| **Kod VS + Wykres słoneczny** | Lekki, oparty na LSP |
| **Vim/Neovim + ruby-lsp** | Oparte na terminalu |
| **Kolega tekstu** | Klasyczny edytor macOS |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Puma** | Domyślny serwer WWW Rails |
| **Pasażer** | Moduł Apache/Nginx |
| **Kapistrano** | Zdalne wdrożenie na wielu serwerach |
| **Doker** | Wdrożenie kontenerowe |
| **Heroku** | PaaS (przyjazny Rubinowi) |
| **Fly.io** | Platforma hostingu aplikacji |
| **Kolej** | Nowoczesne PaaS |
| **Kamal (obóz bazowy)** | Wdrożenie oparte na platformie Docker |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Streszczenie
Ekosystem Ruby skupia się na zadowoleniu programistów i konwencji ponad konfiguracją. Standardowy stos to: **Ruby 3.3+** jako środowisko wykonawcze, **Bundler** dla zależności, **Rails** dla sieci z pełnym stosem (lub **Sinatra** dla mikroaplikacji), **ROSpec** do testowania, **RuboCop** do lintingu, **Sidekiq** do zadań w tle i **Puma** jako serwer WWW. Ruby specjalizuje się w szybkim prototypowaniu, aplikacjach internetowych, skryptach i narzędziach CLI. Ekosystem RubyGems ma ponad 170 000 pakietów. Ruby 3.x wprowadza Ractory do współbieżności, RBS do statycznego pisania i dopasowywania wzorców.