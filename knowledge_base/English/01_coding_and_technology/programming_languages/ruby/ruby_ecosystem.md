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
# Ruby — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the Ruby ecosystem.

---

## Ruby Implementations

| Implementation | Notes |
|---------------|-------|
| **CRuby (MRI)** | Default, most widely used |
| **JRuby** | JVM-based, Java interop |
| **TruffleRuby** | GraalVM-based, high performance |
| **mruby** | Lightweight, embeddable |

```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Package Management

| Tool | Purpose |
|------|---------|
| **RubyGems** | Built-in gem package manager |
| **Bundler** | Dependency management (Gemfile) |
| **rubygems.org** | Official gem repository |

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

## Web Frameworks

| Framework | Type | Best For |
|-----------|------|----------|
| **Rails** | Full-stack | Convention over configuration |
| **Sinatra** | Micro | Simple APIs, small apps |
| **Hanami** | Clean arch. | Maintainable, testable apps |
| **Roda** | Routing tree | High performance, flexible |
| **Grape** | REST API | API-focused framework |
| **Rack** | Interface | Low-level web server interface |

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

## Database & ORM

| Technology | Type |
|------------|------|
| **Active Record** | Rails ORM (convention-based) |
| **Sequel** | Flexible, powerful ORM |
| **ROM (Ruby Object Mapper)** | Functional, composable |
| **pg** | PostgreSQL adapter |
| **mysql2** | MySQL adapter |
| **SQLite3** | SQLite adapter |
| **Mongoid** | MongoDB ODM |
| **Redis** | Key-value store |

---

## Testing

| Framework | Purpose |
|-----------|---------|
| **RSpec** | BDD-style testing (most popular) |
| **Minitest** | Built-in, lightweight |
| **Capybara** | Integration/browser testing |
| **FactoryBot** | Test data factories |
| **Faker** | Fake data generation |
| **WebMock** | HTTP request stubbing |
| **SimpleCov** | Code coverage |
| **VCR** | Record/replay HTTP interactions |
| **Timecop** | Time manipulation in tests |

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

## Code Quality

| Tool | Purpose |
|------|---------|
| **RuboCop** | Linter and formatter |
| **StandardRB** | Opinionated RuboCop config |
| **Reek** | Code smell detection |
| **Brakeman** | Security vulnerability scanner |
| **Bundler-audit** | Gem vulnerability checker |
| **SimpleCov** | Code coverage |
| **Solargraph** | Language server, YARD docs |

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

| Tool | Purpose |
|------|---------|
| **Rake** | Task runner (Make-like) |
| **Thor** | CLI framework |
| **Rails console** | Interactive Rails environment |
| **Thor** | Build powerful CLI tools |
| **Dryrun** | Test gem CLIs |

---

## Key Libraries

| Library | Purpose |
|---------|---------|
| **Rails** | Full-stack web framework |
| **Sidekiq** | Background job processing |
| **Devise** | Authentication |
| **Pundit** | Authorization |
| **Puma** | Web server |
| **Rack** | Web server interface |
| **Nokogiri** | HTML/XML parsing |
| **Faraday** | HTTP client |
| **httparty** | Simple HTTP requests |
| **ActiveSupport** | Utility classes (Rails) |
| **Dry-rb** | Functional Ruby libraries |
| **Hanami::Utils** | Lightweight utilities |
| **Pry** | Developer console / debugger |
| **dotenv** | Environment variables |
| **figaro** | App configuration |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **RubyMine** | Full JetBrains Ruby IDE |
| **VS Code + Solargraph** | Lightweight, LSP-based |
| **Vim/Neovim + ruby-lsp** | Terminal-based |
| **TextMate** | Classic macOS editor |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Puma** | Default Rails web server |
| **Passenger** | Apache/Nginx module |
| **Capistrano** | Remote multi-server deployment |
| **Docker** | Containerized deployment |
| **Heroku** | PaaS (Ruby-friendly) |
| **Fly.io** | App hosting platform |
| **Railway** | Modern PaaS |
| **Kamal (Basecamp)** | Docker-based deployment |

```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Summary

Ruby's ecosystem centers on developer happiness and convention over configuration. The standard stack is: **Ruby 3.3+** as runtime, **Bundler** for dependencies, **Rails** for full-stack web (or **Sinatra** for micro apps), **RSpec** for testing, **RuboCop** for linting, **Sidekiq** for background jobs, and **Puma** as web server. Ruby excels at rapid prototyping, web applications, scripting, and CLI tools. The RubyGems ecosystem has over 170,000 packages. Ruby 3.x brings Ractors for concurrency, RBS for static typing, and pattern matching.
