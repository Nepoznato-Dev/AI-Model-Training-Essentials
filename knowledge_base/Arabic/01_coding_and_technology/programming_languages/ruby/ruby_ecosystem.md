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
# روبي - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية التحتية الأساسية في نظام روبي البيئي.
---

## تطبيقات روبي
| التنفيذ | ملاحظات |
|---------------|-------|
| **كروبي (التصوير بالرنين المغناطيسي)** | الافتراضي، الأكثر استخدامًا |
| **جيروبي** | القائم على JVM، Java Interop |
| **تروفل روبي** | يعتمد على GraalVM، عالي الأداء |
| **مروبي** | خفيفة الوزن وقابلة للتضمين |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## إدارة الحزم
| أداة | الغرض |
|------|---------|
| **جواهر الياقوت** | مدير حزم الأحجار الكريمة المدمج |
| **المجمع** | إدارة التبعية (Gemfile) |
| ** Rubygems.org ** | مستودع الأحجار الكريمة الرسمي |
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

## أطر الويب
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| **القضبان** | مكدس كامل | اتفاقية التكوين |
| ** سيناترا ** | مايكرو | واجهات برمجة التطبيقات البسيطة والتطبيقات الصغيرة |
| **هانامي** | قوس نظيف. | تطبيقات قابلة للصيانة وقابلة للاختبار |
| **رودا** | شجرة التوجيه | أداء عالي، مرن |
| **عنب** | ريست API | إطار عمل يركز على واجهة برمجة التطبيقات |
| **رف** | الواجهة | واجهة خادم ويب منخفضة المستوى |
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

## قاعدة البيانات وORM
| تكنولوجيا | اكتب |
|------------|------|
| **السجل النشط** | Rails ORM (قائم على الاتفاقية) |
| ** تتمة ** | ORM مرن وقوي |
| ** ROM (مخطط كائن روبي) ** | وظيفية وقابلة للتركيب |
| **صفحة** | محول PostgreSQL |
| **mysql2** | محول ماي إس كيو إل |
| **SQLite3** | محول سكليتي |
| **منجي** | مونغو دي بي أوديإم |
| **ريديس** | متجر القيمة الرئيسية |
---

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **RSpec** | اختبار نمط BDD (الأكثر شيوعًا) |
| **مينيست** | مدمج وخفيف الوزن |
| **كابيبارا** | اختبار التكامل/المتصفح |
| **FactoryBot** | مصانع بيانات الاختبار |
| ** فاكر ** | توليد بيانات وهمية |
| **ويب موك** | استئصال طلب HTTP |
| **SimpleCov** | تغطية الكود |
| **فيديو** | تسجيل/إعادة تشغيل تفاعلات HTTP |
| **تيميكوب** | التلاعب بالوقت في الاختبارات |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| ** روبوكوب ** | لينتر وفورماتر |
| **ستاندرد آر بي** | التكوين RuboCop الرأي |
| **ريك** | كود كشف الرائحة |
| ** عامل الفرامل ** | ماسح الثغرات الأمنية |
| **تدقيق المجمّع** | مدقق ثغرات الجوهرة |
| **SimpleCov** | تغطية الكود |
| **رسم بياني للطاقة الشمسية** | خادم اللغة، مستندات YARD |
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

## مشغلو المهام وCLI
| أداة | الغرض |
|------|---------|
| **أشعل النار** | عداء المهمة (Make-like) |
| **ثور** | إطار عمل واجهة سطر الأوامر |
| ** وحدة التحكم في القضبان ** | بيئة القضبان التفاعلية |
| **ثور** | بناء أدوات CLI قوية |
| ** التجفيف ** | اختبار CLIs جوهرة |
---

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **القضبان** | إطار ويب متكامل |
| **صاحب** | معالجة الوظائف الخلفية |
| **ابتكر** | المصادقة |
| ** الناقد ** | إذن |
| **بوما** | خادم الويب |
| **رف** | واجهة خادم الويب |
| ** نوكوجيري ** | تحليل HTML/XML |
| **فاراداي** | عميل HTTP |
| **httparty** | طلبات HTTP البسيطة |
| **الدعم النشط** | فئات المنفعة (القضبان) |
| **دراي-رب** | مكتبات روبي الوظيفية |
| **هانامي::يوتيلز** | مرافق خفيفة الوزن |
| ** نقب ** | وحدة تحكم المطور/مصحح الأخطاء |
| **دوتنف** | متغيرات البيئة |
| **فيجارو** | تكوين التطبيق |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **روبي ماين** | كامل JetBrains روبي IDE |
| **رمز VS + رسم بياني للطاقة** | خفيف الوزن، يعتمد على LSP |
| ** فيم/نيوفيم + روبي-lsp** | القائم على المحطة الطرفية |
| **تيكست ميت** | محرر macOS الكلاسيكي |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **بوما** | خادم ويب ريلز الافتراضي |
| **الراكب** | وحدة أباتشي/إنجينكس |
| **كابيسترانو** | نشر خادم متعدد عن بعد |
| ** عامل الميناء ** | النشر في حاويات |
| **هيروكو** | PaaS (صديق روبي) |
| **Fly.io** | منصة استضافة التطبيقات |
| **السكك الحديدية** | الحديث PaaS |
| **كمال (المعسكر الأساسي)** | النشر القائم على عامل الميناء |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## ملخص
يركز النظام البيئي لروبي على سعادة المطورين والاتفاقية بشأن التكوين. المكدس القياسي هو: **Ruby 3.3+** كوقت تشغيل، **Bundler** للتبعيات، **Rails** للويب الكامل (أو **Sinatra** للتطبيقات الصغيرة)، **RSpec** للاختبار، **RuboCop** للفحص، **Sidekiq** لمهام الخلفية، و **Puma** كخادم ويب. تتفوق روبي في إنشاء النماذج الأولية السريعة وتطبيقات الويب والبرمجة النصية وأدوات واجهة سطر الأوامر (CLI). يحتوي نظام RubyGems البيئي على أكثر من 170.000 حزمة. يقدم Ruby 3.x أدوات Ractors للتزامن، وRBS للكتابة الثابتة، ومطابقة الأنماط.