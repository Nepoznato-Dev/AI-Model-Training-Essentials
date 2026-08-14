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
# Ruby: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e le infrastrutture essenziali nell'ecosistema Ruby.
---

## Implementazioni di Ruby
| Attuazione | Note |
|---------------|-------|
| **CRuby (MRI)** | Predefinito, più utilizzato |
| **JRubino** | Basato su JVM, interoperabilità Java |
| **Rubino al tartufo** | Basato su GraalVM, ad alte prestazioni |
| **mruby** | Leggero, integrabile |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Gestione dei pacchetti
| Strumento | Scopo |
|------|---------|
| **RubinoGemme** | Gestore di pacchetti gem integrato |
| **Bundler** | Gestione delle dipendenze (Gemfile) |
| **rubygems.org** | Repository ufficiale delle gemme |
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

## Framework Web
| Quadro | Digitare | Ideale per |
|-----------|------|----------|
| **Binari** | Stack completo | Convenzione sulla configurazione |
| **Sinatra** | Micro | API semplici, piccole app |
| **Hanami** | Arco pulito. | App gestibili e testabili |
| **Roda** | Albero dei percorsi | Alte prestazioni, flessibile |
| **Uva** | API REST | Framework incentrato sull'API |
| **Scaffale** | Interfaccia | Interfaccia server web di basso livello |
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

## Database e ORM
| Tecnologia | Digitare |
|------------|------|
| **Record attivo** | Rails ORM (basato su convenzione) |
| **Sequel** | ORM flessibile e potente |
| **ROM (mappatore oggetti Ruby)** | Funzionale, componibile |
| **pag** | Adattatore PostgreSQL |
| **mysql2** | Adattatore MySQL |
| **SQLite3** | Adattatore SQLite |
| **Mongoide** | MongoDB ODM |
| **Redis** | Negozio di valori-chiave |
---

## Test
| Quadro | Scopo |
|-----------|---------|
| **RSpec** | Test in stile BDD (più popolari) |
| **Minitest** | Integrato, leggero |
| **Capibara** | Test di integrazione/browser |
| **FabbricaBot** | Test fabbriche di dati |
| **Falsario** | Generazione di dati falsi |
| **WebMock** | Stubbing della richiesta HTTP |
| **CovSemplice** | Copertura del codice |
| **Videoregistratore** | Registra/riproduci interazioni HTTP |
| **Timecop** | Manipolazione del tempo nei test |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **RuboCop** | Linter e formattatore |
| **StandardRB** | Configurazione supponente di RuboCop |
| **Reek** | Rilevamento dell'odore del codice |
| **Frenatore** | Scanner delle vulnerabilità della sicurezza |
| **Audit del bundle** | Controllo della vulnerabilità delle gemme |
| **CovSemplice** | Copertura del codice |
| **Solargrafo** | Server linguistico, documenti YARD |
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

## Task Runner e CLI
| Strumento | Scopo |
|------|---------|
| **Rastrello** | Task runner (Make-like) |
| **Thor** | Quadro CLI |
| **Console binari** | Ambiente interattivo di Rails |
| **Thor** | Crea potenti strumenti CLI |
| **Corsa a secco** | Testare le CLI gem |
---

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **Binari** | Framework web full-stack |
| **Sidekiq** | Elaborazione del lavoro in background |
| **Ideare** | Autenticazione |
| **Esperto** | Autorizzazione |
| **Puma** | Server web |
| **Scaffale** | Interfaccia server web |
| **Nokogiri** | Analisi HTML/XML |
| **Faraday** | Client HTTP |
| **httparty** | Richieste HTTP semplici |
| **Supporto attivo** | Classi di utilità (Rotaie) |
| **Dry-RB** | Librerie Ruby funzionali |
| **Hanami::Utilità** | Utilità leggere |
| **Fai leva** | Console per sviluppatori/debugger |
| **dotenv** | Variabili d'ambiente |
| **figaro** | Configurazione dell'app |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **RubyMine** | IDE JetBrains Ruby completo |
| **Codice VS + Solargraph** | Leggero, basato su LSP |
| **Vim/Neovim + ruby-lsp** | Basato su terminale |
| **TextMate** | Editor macOS classico |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Puma** | Server Web Rails predefinito |
| **Passeggero** | Modulo Apache/Nginx |
| **Capistrano** | Distribuzione multiserver remota |
| **Docker** | Distribuzione in contenitori |
| **Heroku** | PaaS (compatibile con Ruby) |
| **Fly.io** | Piattaforma di hosting di app |
| **Ferrovia** | PaaS moderno |
| **Kamal (campo base)** | Distribuzione basata su Docker |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Riepilogo
L'ecosistema di Ruby è incentrato sulla felicità degli sviluppatori e sulla convenzione sulla configurazione. Lo stack standard è: **Ruby 3.3+** come runtime, **Bundler** per le dipendenze, **Rails** per web full-stack (o **Sinatra** per micro app), **RSpec** per test, **RuboCop** per linting, **Sidekiq** per processi in background e **Puma** come server web. Ruby eccelle nella prototipazione rapida, nelle applicazioni web, nello scripting e negli strumenti CLI. L'ecosistema RubyGems ha oltre 170.000 pacchetti. Ruby 3.x offre Ractors per la concorrenza, RBS per la tipizzazione statica e la corrispondenza dei modelli.