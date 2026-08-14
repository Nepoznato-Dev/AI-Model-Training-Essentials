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
# Ruby – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im Ruby-Ökosystem.
---

## Ruby-Implementierungen
| Umsetzung | Notizen |
|---------------|-------|
| **CRuby (MRT)** | Standard, am häufigsten verwendet |
| **JRuby** | JVM-basiertes Java-Interop |
| **TruffleRuby** | GraalVM-basiert, hohe Leistung |
| **mruby** | Leicht, einbettbar |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **RubyGems** | Integrierter Gem-Paketmanager |
| **Bündeler** | Abhängigkeitsmanagement (Gemfile) |
| **rubygems.org** | Offizielles Edelstein-Repository |
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

## Web-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **Schienen** | Full-Stack | Konvention über Konfiguration |
| **Sinatra** | Mikro | Einfache APIs, kleine Apps |
| **Hanami** | Sauberer Bogen. | Wartbare, testbare Apps |
| **Roda** | Routing-Baum | Leistungsstark, flexibel |
| **Traube** | REST-API | API-fokussiertes Framework |
| **Rack** | Schnittstelle | Low-Level-Webserverschnittstelle |
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

## Datenbank und ORM
| Technologie | Geben Sie | ein
|------------|------|
| **Aktiver Datensatz** | Rails ORM (konventionsbasiert) |
| **Fortsetzung** | Flexibles, leistungsstarkes ORM |
| **ROM (Ruby Object Mapper)** | Funktional, zusammensetzbar |
| **Seite** | PostgreSQL-Adapter |
| **mysql2** | MySQL-Adapter |
| **SQLite3** | SQLite-Adapter |
| **Mongoid** | MongoDB ODM |
| **Redis** | Schlüsselwertspeicher |
---

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **RSpec** | Tests im BDD-Stil (am beliebtesten) |
| **Minitest** | Eingebaut, leicht |
| **Wasserschwein** | Integrations-/Browsertests |
| **FactoryBot** | Datenfabriken testen |
| **Fälscher** | Gefälschte Datengenerierung |
| **WebMock** | Stubbing von HTTP-Anfragen |
| **SimpleCov** | Codeabdeckung |
| **Videorecorder** | HTTP-Interaktionen aufzeichnen/wiedergeben |
| **Timecop** | Zeitmanipulation in Tests |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **RuboCop** | Linter und Formatierer |
| **StandardRB** | Meinungsbildende RuboCop-Konfiguration |
| **Stink** | Code-Geruchserkennung |
| **Bremser** | Sicherheitslückenscanner |
| **Bundler-Audit** | Gem-Schwachstellenprüfer |
| **SimpleCov** | Codeabdeckung |
| **Solargraph** | Sprachserver, YARD-Dokumente |
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

## Task Runners & CLI
| Werkzeug | Zweck |
|------|---------|
| **Rechen** | Task-Runner (Make-like) |
| **Thor** | CLI-Framework |
| **Schienenkonsole** | Interaktive Rails-Umgebung |
| **Thor** | Erstellen Sie leistungsstarke CLI-Tools |
| **Trockenlauf** | Gem-CLIs testen |
---

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Schienen** | Full-Stack-Webframework |
| **Sidekiq** | Hintergrundverarbeitung von Jobs |
| **Entwickeln** | Authentifizierung |
| **Experte** | Autorisierung |
| **Puma** | Webserver |
| **Rack** | Webserver-Schnittstelle |
| **Nokogiri** | HTML/XML-Analyse |
| **Faraday** | HTTP-Client |
| **httparty** | Einfache HTTP-Anfragen |
| **AktiverSupport** | Versorgungsklassen (Schienen) |
| **Trocken-rb** | Funktionale Ruby-Bibliotheken |
| **Hanami::Utils** | Leichte Dienstprogramme |
| **Hebeln** | Entwicklerkonsole/Debugger |
| **dotenv** | Umgebungsvariablen |
| **figaro** | App-Konfiguration |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **RubyMine** | Vollständige JetBrains Ruby IDE |
| **VS-Code + Solargraph** | Leicht, LSP-basiert |
| **Vim/Neovim + ruby-lsp** | Terminalbasiert |
| **TextMate** | Klassischer macOS-Editor |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Puma** | Standard-Rails-Webserver |
| **Passagier** | Apache/Nginx-Modul |
| **Capistrano** | Remote-Multiserverbereitstellung |
| **Docker** | Containerisierte Bereitstellung |
| **Heroku** | PaaS (Ruby-freundlich) |
| **Fly.io** | App-Hosting-Plattform |
| **Eisenbahn** | Modernes PaaS |
| **Kamal (Basislager)** | Docker-basierte Bereitstellung |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Zusammenfassung
Im Mittelpunkt des Ruby-Ökosystems stehen die Zufriedenheit der Entwickler und Konventionen vor der Konfiguration. Der Standard-Stack ist: **Ruby 3.3+** als Laufzeit, **Bundler** für Abhängigkeiten, **Rails** für Full-Stack-Web (oder **Sinatra** für Mikro-Apps), **RSpec** für Tests, **RuboCop** für Linting, **Sidekiq** für Hintergrundjobs und **Puma** als Webserver. Ruby zeichnet sich durch Rapid Prototyping, Webanwendungen, Skripting und CLI-Tools aus. Das RubyGems-Ökosystem umfasst über 170.000 Pakete. Ruby 3.x bringt Ractors für Parallelität, RBS für statische Typisierung und Mustervergleich.