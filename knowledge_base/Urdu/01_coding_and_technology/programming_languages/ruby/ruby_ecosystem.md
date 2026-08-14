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

# روبی - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ روبی ایکو سسٹم میں ضروری ٹولز، فریم ورک اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## روبی عمل درآمد
| نفاذ | نوٹس |
|---------------|---------|
| **کروبی (MRI)** | پہلے سے طے شدہ، سب سے زیادہ استعمال شدہ |
| **JRuby** | JVM پر مبنی، جاوا انٹراپ |
| **ٹرفل روبی** | GraalVM پر مبنی، اعلی کارکردگی |
| **mruby** | ہلکا پھلکا، سرایت کرنے والا |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## پیکیج مینجمنٹ
| ٹول | مقصد |
|------|---------|
| **روبی جیمز** | بلٹ ان منی پیکج مینیجر |
| **بنڈلر** | انحصار کا انتظام (جیم فائل) |
| **rubygems.org** | سرکاری منی ذخیرہ |
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

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **ریلز** | مکمل اسٹیک | کنونشن اوور کنفیگریشن |
| **سیناترا** | مائیکرو | سادہ APIs، چھوٹی ایپس |
| **حنامی** | صاف محراب۔ | برقرار رکھنے کے قابل، قابل آزمائش ایپس |
| **روڈا** | روٹنگ درخت | اعلی کارکردگی، لچکدار |
| **انگور** | REST API | API پر مرکوز فریم ورک |
| **ریک** | انٹرفیس | کم سطح کا ویب سرور انٹرفیس |
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

## ڈیٹا بیس اور ORM
| ٹیکنالوجی | قسم |
|------------|------|
| **ایکٹو ریکارڈ** | ریلز ORM (کنونشن پر مبنی) |
| **سیکوئل** | لچکدار، طاقتور ORM |
| **روم (روبی آبجیکٹ میپر)** | فنکشنل، کمپوز ایبل |
| **pg** | PostgreSQL اڈاپٹر |
| **mysql2** | MySQL اڈاپٹر |
| **SQLite3** | SQLite اڈاپٹر |
| **منگوئڈ** | MongoDB ODM |
| **ریڈیس** | کلیدی قدر کی دکان |
---

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **RSpec** | BDD طرز کی جانچ (سب سے زیادہ مقبول) |
| **کم سے کم** | بلٹ ان، ہلکا پھلکا |
| **کیپیبرا** | انٹیگریشن/براؤزر ٹیسٹنگ |
| **فیکٹری بوٹ** | ٹیسٹ ڈیٹا فیکٹریاں |
| **جعلی** | جعلی ڈیٹا جنریشن |
| **WebMock** | ایچ ٹی ٹی پی کی درخواست کو روکنا |
| **SimpleCov** | کوڈ کوریج |
| **VCR** | HTTP تعاملات کو ریکارڈ/دوبارہ چلائیں |
| **Timecop** | ٹیسٹ میں وقت کی ہیرا پھیری |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **روبو کوپ** | لنٹر اور فارمیٹر |
| **معیاری آر بی** | رائے شدہ RuboCop تشکیل |
| **ریک** | کوڈ بو کا پتہ لگانے |
| **بریک مین** | سیکورٹی کے خطرے سے متعلق سکینر |
| **بنڈلر آڈٹ** | منی خطرے کی جانچ کرنے والا |
| **SimpleCov** | کوڈ کوریج |
| **سولر گراف** | زبان کا سرور، YARD دستاویزات |
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

## ٹاسک رنرز اور CLI
| ٹول | مقصد |
|------|---------|
| **ریک** | ٹاسک رنر (میک کی طرح) |
| **تھور** | CLI فریم ورک |
| **ریلز کنسول** | انٹرایکٹو ریل ماحول |
| **تھور** | طاقتور CLI ٹولز بنائیں |
| **ڈرائیرن** | ٹیسٹ منی CLIs |
---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **ریلز** | مکمل اسٹیک ویب فریم ورک |
| **Sidekiq** | بیک گراؤنڈ جاب پروسیسنگ |
| **ڈیوائز** | تصدیق |
| **پنڈت** | اجازت |
| **پوما** | ویب سرور |
| **ریک** | ویب سرور انٹرفیس |
| **نوکوگیری** | HTML/XML پارسنگ |
| **فراڈے** | HTTP کلائنٹ |
| **httpparty** | سادہ HTTP درخواستیں |
| **ایکٹو سپورٹ** | یوٹیلیٹی کلاسز (ریلز) |
| **Dry-rb** | فنکشنل روبی لائبریریاں |
| **Hanami::Utils** | ہلکے وزن کی افادیت |
| **پری** | ڈویلپر کنسول / ڈیبگر |
| **dotenv** | ماحولیاتی متغیرات |
| **فیگارو** | ایپ کنفیگریشن |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **روبی مائن** | مکمل JetBrains روبی IDE |
| **VS کوڈ + سولر گراف** | ہلکا پھلکا، LSP پر مبنی |
| **Vim/Neovim + ruby-lsp** | ٹرمینل پر مبنی |
| **TextMate** | کلاسک macOS ایڈیٹر |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **پوما** | ڈیفالٹ ریلز ویب سرور |
| **مسافر** | Apache/Nginx ماڈیول |
| **کیپسٹرانو** | ریموٹ ملٹی سرور تعیناتی |
| **ڈوکر** | کنٹینرائزڈ تعیناتی |
| **ہیروکو** | PaaS (روبی دوستانہ) |
| **Fly.io** | ایپ ہوسٹنگ پلیٹ فارم |
| **ریلوے** | جدید PaaS |
| **کمال (بیس کیمپ)** | ڈاکر پر مبنی تعیناتی |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## خلاصہ
روبی کا ماحولیاتی نظام ڈویلپر کی خوشی اور کنفیگریشن پر کنونشن پر مرکوز ہے۔ معیاری اسٹیک یہ ہے: **Ruby 3.3+** بطور رن ٹائم، **Bundler** انحصار کے لیے، **Rails** فل اسٹیک ویب کے لیے (یا **Sinatra** مائیکرو ایپس کے لیے)، **RSpec** ٹیسٹنگ کے لیے، **RuboCop** linting کے لیے، **Sidekiq** بیک گراؤنڈ جابز کے لیے، اور **Peruma** کے طور پر۔ روبی تیز رفتار پروٹو ٹائپنگ، ویب ایپلیکیشنز، اسکرپٹنگ، اور CLI ٹولز میں سبقت لے جاتی ہے۔ RubyGems ایکو سسٹم میں 170,000 سے زیادہ پیکجز ہیں۔ Ruby 3.x کنکرنسی کے لیے Ractors، جامد ٹائپنگ کے لیے RBS، اور پیٹرن میچنگ لاتا ہے۔