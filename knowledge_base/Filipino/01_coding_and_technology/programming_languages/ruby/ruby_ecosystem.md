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
# Ruby — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, framework, at imprastraktura sa Ruby ecosystem.
---

## Mga Pagpapatupad ng Ruby
| Pagpapatupad | Mga Tala |
|--------------|-------|
| **CRuby (MRI)** | Default, pinakamalawak na ginagamit |
| **JRuby** | JVM-based, Java interop |
| **TruffleRuby** | GraalVM-based, mataas na pagganap |
| **mruby** | Magaan, na-embed |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **RubyGems** | Built-in na gem package manager |
| **Bundler** | Pamamahala ng dependency (Gemfile) |
| **rubygems.org** | Opisyal na imbakan ng hiyas |
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

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **Rails** | Full-stack | Convention sa pagsasaayos |
| **Sinatra** | Micro | Mga simpleng API, maliliit na app |
| **Hanami** | Malinis na arko. | Mapapanatili, nasusubok na mga app |
| **Roda** | Puno ng ruta | Mataas na pagganap, nababaluktot |
| **Ubas** | REST API | Framework na nakatuon sa API |
| **Rack** | Interface | Mababang antas ng interface ng web server |
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

## Database at ORM
| Teknolohiya | Uri |
|------------|------|
| **Aktibong Record** | Rails ORM (batay sa convention) |
| **Karugtong** | Flexible, makapangyarihang ORM |
| **ROM (Ruby Object Mapper)** | Functional, composable |
| **pg** | PostgreSQL adapter |
| **mysql2** | MySQL adapter |
| **SQLite3** | SQLite adapter |
| **Mongoid** | MongoDB ODM |
| **Redis** | Tindahan ng key-value |
---

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **RSpec** | BDD-style na pagsubok (pinakatanyag) |
| **Minitest** | Built-in, magaan ang timbang |
| **Capybara** | Pagsubok sa pagsasama/browser |
| **FactoryBot** | Mga pabrika ng data ng pagsubok |
| **Faker** | Pagbuo ng pekeng data |
| **WebMock** | HTTP request stubbing |
| **SimpleCov** | Saklaw ng code |
| **VCR** | I-record/i-replay ang mga pakikipag-ugnayan sa HTTP |
| **Timecop** | Pagmamanipula ng oras sa mga pagsusulit |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **RuboCop** | Linter at formatter |
| **StandardRB** | Opinionated RuboCop config |
| **Reek** | Code smell detection |
| **Brakeman** | Scanner ng kahinaan sa seguridad |
| **Bundler-audit** | Tagasuri ng kahinaan ng hiyas |
| **SimpleCov** | Saklaw ng code |
| **Solargraph** | Server ng wika, mga doc ng YARD |
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

## Task Runners at CLI
| Tool | Layunin |
|------|---------|
| **Rake** | Task runner (Make-like) |
| **Thor** | CLI framework |
| **Rails console** | kapaligiran ng Interactive Rails |
| **Thor** | Bumuo ng makapangyarihang mga tool sa CLI |
| **Dryrun** | Subukan ang gem CLIs |
---

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **Rails** | Full-stack na web framework |
| **Sidekiq** | Pagproseso ng trabaho sa background |
| **Devise** | Pagpapatunay |
| **Pundit** | Pahintulot |
| **Puma** | Web server |
| **Rack** | Interface ng web server |
| **Nokogiri** | Pag-parse ng HTML/XML |
| **Faraday** | HTTP client |
| **httparty** | Mga simpleng kahilingan sa HTTP |
| **ActiveSupport** | Mga klase ng utility (Rails) |
| **Tuyo-rb** | Mga functional na aklatan ng Ruby |
| **Hanami::Utils** | Magaan na mga utility |
| **Pry** | Developer console / debugger |
| **dotenv** | Mga variable ng kapaligiran |
| **figaro** | Configuration ng app |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **RubyMine** | Buong JetBrains Ruby IDE |
| **VS Code + Solargraph** | Magaan, batay sa LSP |
| **Vim/Neovim + ruby-lsp** | Nakabatay sa terminal |
| **TextMate** | Klasikong macOS editor |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Puma** | Default na Rails web server |
| **Pasahero** | Apache/Nginx module |
| **Capistrano** | Remote multi-server deployment |
| **Docker** | Containerized deployment |
| **Heroku** | PaaS (Ruby-friendly) |
| **Fly.io** | Platform sa pagho-host ng app |
| **Riles** | Makabagong PaaS |
| **Kamal (Basecamp)** | Docker-based deployment |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Buod
Nakasentro ang ecosystem ni Ruby sa kaligayahan ng developer at kumbensyon sa pagsasaayos. Ang karaniwang stack ay: **Ruby 3.3+** bilang runtime, **Bundler** para sa mga dependency, **Rails** para sa full-stack na web (o **Sinatra** para sa mga micro app), **RSpec** para sa pagsubok, **RuboCop** para sa linting, **Sidekiq** para sa mga background na trabaho, at **Puma** bilang web server. Si Ruby ay mahusay sa mabilis na prototyping, mga web application, scripting, at mga tool sa CLI. Ang RubyGems ecosystem ay may higit sa 170,000 mga pakete. Ang Ruby 3.x ay nagdadala ng Ractors para sa concurrency, RBS para sa static na pag-type, at pagtutugma ng pattern.