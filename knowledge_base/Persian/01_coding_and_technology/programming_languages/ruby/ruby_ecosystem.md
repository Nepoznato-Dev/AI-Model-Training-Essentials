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

# روبی - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم روبی را پوشش می‌دهد.
---

## پیاده سازی روبی
| پیاده سازی | یادداشت ها |
|---------------|-------|
| **CRuby (MRI)** | پیش فرض، پرکاربردترین |
| **جی روبی** | مبتنی بر JVM، جاوا interop |
| **ترافل یاقوت** | مبتنی بر GraalVM با کارایی بالا |
| **مروبی** | سبک، قابل جاسازی |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **RubyGems** | توکار پکیج جم |
| **باندلر** | مدیریت وابستگی (Gemfile) |
| **rubygems.org** | مخزن رسمی جواهرات |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **ریل** | تمام پشته | کنوانسیون بیش از پیکربندی |
| **سیناترا** | میکرو | API های ساده، برنامه های کوچک |
| **هنامی** | طاق تمیز. | برنامه های قابل نگهداری و آزمایشی |
| **رودا** | درخت مسیریابی | عملکرد بالا، انعطاف پذیر |
| **انگور** | REST API | چارچوب متمرکز بر API |
| **رک** | رابط | رابط وب سرور سطح پایین |
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

## پایگاه داده و ORM
| فناوری | نوع |
|------------|------|
| **رکورد فعال** | Rails ORM (بر اساس کنوانسیون) |
| **عاقبت** | ORM انعطاف پذیر و قدرتمند |
| **ROM (Ruby Object Mapper)** | کاربردی، قابل ترکیب |
| **صفحه** | آداپتور PostgreSQL |
| **mysql2** | آداپتور MySQL |
| **SQLite3** | آداپتور SQLite |
| **Mongoid** | MongoDB ODM |
| **ردیس** | فروشگاه کلید ارزش |
---

## تست
| چارچوب | هدف |
|-----------|---------|
| **RSpec** | تست سبک BDD (محبوب ترین) |
| **مینی ترین** | توکار، سبک وزن |
| **کاپیبارا** | تست یکپارچه سازی/مرورگر |
| **FactoryBot** | کارخانه های داده تست |
| **جعلی** | تولید داده های جعلی |
| **WebMock** | حذف درخواست HTTP |
| **SimpleCov** | پوشش کد |
| **VCR** | ضبط/بازپخش فعل و انفعالات HTTP |
| **Timecop** | دستکاری زمان در تست ها |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **RuboCop** | لینتر و فرم دهنده |
| **StandardRB** | پیکربندی RuboCop Opinionated |
| **ریک** | تشخیص بوی کد |
| **ترمزدار** | اسکنر آسیب پذیری امنیتی |
| **باندلر-حسابرسی** | بررسی کننده آسیب پذیری جم |
| **SimpleCov** | پوشش کد |
| **سولارگراف** | سرور زبان، اسناد YARD |
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
| ابزار | هدف |
|------|---------|
| **راک** | Task runner (Make-like) |
| **ثور** | چارچوب CLI |
| **کنسول ریل** | محیط ریل تعاملی |
| **ثور** | ساخت ابزار قدرتمند CLI |
| **Dryrun** | تست سنگهای CLIs |
---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **ریل** | چارچوب وب تمام پشته |
| **سیدیق** | پردازش شغل پیشینه |
| **طراحی** | احراز هویت |
| **پاندیت** | مجوز |
| **پوما** | وب سرور |
| **رک** | رابط وب سرور |
| **نوکوگیری** | تجزیه HTML/XML |
| **فارادی** | سرویس گیرنده HTTP |
| **httpparty** | درخواست های ساده HTTP |
| **ActiveSupport** | کلاس های کاربردی (ریل) |
| **درای-رب** | کتابخانه های کاربردی روبی |
| **هانامی::Utils** | ابزارهای سبک وزن |
| **پری** | کنسول برنامه نویس / دیباگر |
| **dotenv** | متغیرهای محیطی |
| **فیگارو** | پیکربندی برنامه |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **RubyMine** | Full JetBrains Ruby IDE |
| **VS Code + Solargraph** | سبک وزن مبتنی بر LSP |
| **Vim/Neovim + ruby-lsp** | مبتنی بر ترمینال |
| **TextMate** | ویرایشگر کلاسیک macOS |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **پوما** | وب سرور پیش فرض Rails |
| **مسافر** | ماژول Apache/Nginx |
| **کاپیسترانو** | استقرار چند سرور از راه دور |
| **داکر** | استقرار کانتینری |
| **هروکو** | PaaS (یقوت دوست) |
| **Fly.io** | پلت فرم میزبانی اپلیکیشن |
| **راه آهن** | PaaS مدرن |
| **کمال (بیس کمپ)** | استقرار مبتنی بر داکر |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## خلاصه
اکوسیستم روبی بر روی شادی توسعه دهندگان و قرارداد بر پیکربندی متمرکز است. پشته استاندارد عبارتند از: **Ruby 3.3+** به عنوان زمان اجرا، **Bundler** برای وابستگی ها، **Rails** برای وب تمام پشته (یا **Sinatra** برای برنامه های میکرو)، **RSpec** برای آزمایش، **RuboCop** برای linting، **Sidekiq** برای کارهای پس زمینه، و به عنوان **Pum. روبی در نمونه سازی سریع، برنامه های کاربردی وب، اسکریپت نویسی و ابزارهای CLI برتری دارد. اکوسیستم RubyGems بیش از 170000 بسته دارد. Ruby 3.x Ractors را برای همزمانی، RBS را برای تایپ استاتیک، و تطبیق الگو را به ارمغان می آورد.