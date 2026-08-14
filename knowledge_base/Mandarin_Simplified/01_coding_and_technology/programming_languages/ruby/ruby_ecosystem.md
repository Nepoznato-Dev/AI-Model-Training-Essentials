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

# Ruby — 生态系统和工具指南
本指南涵盖了 Ruby 生态系统中的基本工具、框架和基础设施。
---

## 红宝石实现
|实施 |笔记|
|----------------|--------|
| **CRuby (MRI)** |默认，使用最广泛 |
| **JRuby** |基于 JVM 的 Java 互操作 |
| **松露红宝石** |基于GraalVM，高性能|
| **姆鲁比** |轻量级、可嵌入 |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## 包管理
|工具|目的|
|------|---------|
| **红宝石** |内置gem包管理器|
| **捆绑器** |依赖管理（Gemfile）|
| **rubygems.org** |官方宝石库 |
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

## 网络框架
|框架|类型 |最适合 |
|------------|------|----------|
| **导轨** |全栈|约定优于配置|
| **西纳特拉** |微|简单的 API，小型应用程序 |
| **花见** |干净的拱门。 |可维护、可测试的应用程序 |
| **罗达** |路由树|高性能、灵活|
| **葡萄** |休息 API |以 API 为中心的框架 |
| **机架** |接口 |低级 Web 服务器接口 |
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

## 数据库和 ORM
|技术 |类型 |
|------------|------|
| **活动记录** | Rails ORM（基于约定）|
| **续集** |灵活、强大的 ORM |
| **ROM（Ruby 对象映射器）** |功能性、可组合性 |
| **页** | PostgreSQL 适配器 |
| **mysql2** | MySQL 适配器 |
| **SQLite3** | SQLite 适配器 |
| **蒙古人** | MongoDB ODM |
| **Redis** |键值存储 |
---

## 测试
|框架|目的|
|------------|---------|
| **R规格** | BDD 式测试（最流行）|
| **最小测试** |内置、轻便|
| **水豚** |集成/浏览器测试 |
| **工厂机器人** |测试数据工厂|
| **Faker** |虚假数据生成 |
| **WebMock** | HTTP 请求存根 |
| **SimpleCov** |代码覆盖率|
| **录像机** |记录/重放 HTTP 交互 |
| **时间警察** |测试中的时间操纵|
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

## 代码质量
|工具|目的|
|------|---------|
| **鲁博警察** | Linter 和格式化程序 |
| **标准RB** |固执己见的 RuboCop 配置 |
| **臭味** |代码气味检测 |
| **刹车工** |安全漏洞扫描器 |
| **捆绑器审核** | Gem 漏洞检查器 |
| **SimpleCov** |代码覆盖率|
| **太阳图** |语言服务器，YARD 文档 |
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

## 任务运行器和 CLI
|工具|目的|
|------|---------|
| **耙子** |任务运行器（类似Make）|
| **雷神** | CLI 框架 |
| **Rails 控制台** |交互式 Rails 环境 |
| **雷神** |构建强大的 CLI 工具 |
| **试运行** |测试 gem CLI |
---

## 关键库
|图书馆 |目的|
|---------|---------|
| **导轨** |全栈Web框架|
| **Sidekiq** |后台作业处理 |
| **设计** |认证|
| **专家** |授权|
| **彪马** |网络服务器|
| **机架** |网络服务器接口|
| **诺科吉里** | HTML/XML 解析 |
| **法拉第** | HTTP 客户端 |
| **httpparty** |简单的 HTTP 请求 |
| **主动支持** |实用程序类（Rails）|
| **干rb** |函数式 Ruby 库 |
| **花见::实用工具** |轻量级实用程序 |
| **撬** |开发者控制台/调试器|
| **点环境** |环境变量|
| **费加罗** |应用程序配置 |
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **红宝石矿** |完整的 JetBrains Ruby IDE |
| **VS 代码 + Solargraph** |轻量级、基于LSP |
| **Vim/Neovim + ruby​​-lsp** |基于终端 |
| **文本伴侣** |经典 macOS 编辑器 |
---

## 部署
|方法|笔记|
|--------|--------|
| **彪马** |默认 Rails Web 服务器 |
| **乘客** | Apache/Nginx 模块 |
| **卡皮斯特拉诺** |远程多服务器部署|
| **码头工人** |容器化部署|
| **赫罗库** | PaaS（Ruby 友好）|
| **Fly.io** |应用托管平台|
| **铁路** |现代PaaS |
| **卡迈勒（大本营）** |基于Docker的部署|
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

＃＃ 概括
Ruby 的生态系统以开发人员的幸福感和约定优于配置为中心。标准堆栈是：**Ruby 3.3+** 作为运行时，**Bundler** 用于依赖项，**Rails** 用于全堆栈 Web（或 **Sinatra** 用于微应用程序），**RSpec** 用于测试，**RuboCop** 用于 linting，**Sidekiq** 用于后台作业，以及 **Puma** 作为 Web 服务器。 Ruby 擅长快速原型设计、Web 应用程序、脚本编写和 CLI 工具。 RubyGems 生态系统拥有超过 170,000 个软件包。 Ruby 3.x 带来了用于并发的 Ractor、用于静态类型的 RBS 和模式匹配。