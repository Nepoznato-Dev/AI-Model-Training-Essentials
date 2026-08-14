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
# Ruby — 生態系與工具指南
本指南涵蓋了 Ruby 生態系統中的基本工具、框架和基礎設施。
---

## 紅寶石實現
|實施 |筆記|
|----------------|--------|
| **CRuby (MRI)** |默認，使用最廣泛 |
| **JRuby** |基於 JVM 的 Java 互通 |
| **松露紅寶石** |基於GraalVM，高性能|
| **姆魯比** |輕量級、可嵌入 |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## 套件管理
|工具|目的|
|------|---------|
| **紅寶石** |內建gem套件管理器|
| **捆綁器** |依賴管理（Gemfile）|
| **rubygems.org** |官方寶石庫 |
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **導軌** |全端|約定優於配置|
| **西納特拉** |微|簡單的 API，小型應用程式 |
| **花見** |乾淨的拱門。 |可維護、可測試的應用程式 |
| **羅達** |路由樹|高性能、靈活|
| **葡萄** |休息 API |以 API 為中心的框架 |
| **機架** |介面 |低階 Web 伺服器介面 |
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

## 資料庫和 ORM
|技術 |類型 |
|------------|------|
| **活動記錄** | Rails ORM（基於約定）|
| **續集** |靈活、強大的 ORM |
| **ROM（Ruby 物件映射器）** |功能性、可組合性 |
| **頁** | PostgreSQL 適配器 |
| **mysql2** | MySQL 適配器 |
| **SQLite3** | SQLite 適配器 |
| **蒙古人** | MongoDB ODM |
| **Redis** |鍵值儲存 |
---

## 測試
|框架|目的|
|------------|---------|
| **R規格** | BDD 式測試（最受歡迎）|
| **最小測試** |內建、輕量|
| **水豚** |整合/瀏覽器測試 |
| **工廠機器人** |測試資料工廠|
| **Faker** |假資料產生 |
| **WebMock** | HTTP 請求存根 |
| **SimpleCov** |程式碼覆蓋率|
| **錄影機** |記錄/重播 HTTP 互動 |
| **時間警察** |測驗中的時間操縱|
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

## 程式碼品質
|工具|目的|
|------|---------|
| **魯博警察** | Linter 與格式化程序 |
| **標準RB** |固執己見的 RuboCop 配置 |
| **臭味** |代碼氣味檢測 |
| **煞車工** |安全漏洞掃描器 |
| **捆綁器審核** | Gem 漏洞檢查器 |
| **SimpleCov** |程式碼覆蓋率|
| **太陽圖** |語言伺服器，YARD 文件 |
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

## 任務運行器和 CLI
|工具|目的|
|------|---------|
| **耙子** |任務運行器（類似Make）|
| **雷神索爾** | CLI 框架 |
| **Rails 控制台** |互動式 Rails 環境 |
| **雷神** |建立強大的 CLI 工具 |
| **試運行** |測試 gem CLI |
---

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **導軌** |全端Web框架|
| **Sidekiq** |背景作業處理 |
| **設計** |認證|
| **專家** |授權|
| **彪馬** |網頁伺服器|
| **機架** |網路伺服器介面|
| **諾科吉里** | HTML/XML 解析 |
| **法拉第** | HTTP 用戶端 |
| **httpparty** |簡單的 HTTP 請求 |
| **主動支援** |實用程式類別（Rails）|
| **乾rb** |函數式 Ruby 函式庫 |
| **花見::實用工具** |輕量級實用程式 |
| **撬** |開發者控制台/偵錯器|
| **點環境** |環境變數|
| **費加洛** |應用程式配置 |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **紅寶石礦坑** |完整的 JetBrains Ruby IDE |
| **VS 代碼 + Solargraph** |輕量級、基於LSP |
| **Vim/Neovim + ruby-lsp** |基於終端 |
| **文字夥伴** |經典 macOS 編輯器 |
---

## 部署
|方法|筆記|
|--------|--------|
| **彪馬** |預設 Rails Web 伺服器 |
| **乘客** | Apache/Nginx 模組 |
| **卡皮斯特拉諾** |遠端多伺服器部署|
| **碼頭工人** |容器化部署|
| **赫羅庫** | PaaS（Ruby 友善）|
| **Fly.io** |應用程式託管平台|
| **鐵路** |現代PaaS |
| **卡邁勒（大本營）** |基於Docker的部署|
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

＃＃ 概括
Ruby 的生態系統以開發人員的幸福感和約定優於配置為中心。標準堆疊是：**Ruby 3.3+** 作為運行時，**Bundler** 用於依賴項，**Rails** 用於全堆疊 Web（或 **Sinatra** 用於微型應用程式），**RSpec** 用於測試，**RuboCop** 用於 linting，**Sidekiq** 用於後台**，以及伺服器 **Pumating** Ruby 擅長快速原型設計、Web 應用程式、腳本編寫和 CLI 工具。 RubyGems 生態系統擁有超過 170,000 個軟體包。 Ruby 3.x 帶來了用於並發的 Ractor、用於靜態類型的 RBS 和模式匹配。