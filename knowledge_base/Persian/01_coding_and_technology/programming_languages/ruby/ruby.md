---
# Metadata
title: "Ruby"
description: "Comprehensive reference for the Ruby programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ruby, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "34 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

#یاقوت
روبی یک زبان برنامه نویسی پویا، تفسیر شده و شی گرا است که توسط Yukihiro "Matz" Matsumoto ایجاد شد و اولین بار در سال 1995 در ژاپن منتشر شد. روبی با تمرکز بر شادی برنامه نویس طراحی شده است - نحو آن زیبا و طبیعی است و تقریباً مانند انگلیسی خوانده می شود. همه چیز در روبی یک شی است، از جمله انواع اولیه مانند اعداد صحیح و بولی. روبی بیشتر برای چارچوب وب Ruby on Rails شناخته می‌شود، که توسعه وب را با رایج کردن قراردادها بر روی پیکربندی و نمونه‌سازی سریع، متحول کرد.
Beyond Rails، Ruby برای اسکریپت نویسی، اتوماسیون، ابزار DevOps (Cef، Puppet) و به عنوان یک زبان همه منظوره استفاده می شود. نحو بیانی و قابلیت های فرابرنامه نویسی قدرتمند آن، نوشتن را لذت بخش می کند.
---

## چرا روبی مهم است
- **خوشبختی توسعه دهنده**: روبی به گونه ای طراحی شده است که خوانا و لذت بخش باشد. "Ruby برای شاد کردن برنامه نویسان طراحی شده است" - Matz.
- ** نحو بیانی **: کد مانند انگلیسی خوانده می شود. حداقل نشانه گذاری، عبارت طبیعی.
- **Ruby on Rails**: یکی از پربازده ترین چارچوب های وب که تا کنون ایجاد شده است. قدرت های GitHub، Shopify، Basecamp، GitLab.
- ** فرابرنامه‌نویسی**: روبی می‌تواند خود را در زمان اجرا تغییر دهد - روش‌ها را به صورت پویا تعریف کند، زبان‌های مخصوص دامنه (DSL) ایجاد کند.
- **الگوی بلوک/تکرارگر**: بلوک های روبی و تکرارکننده ها پردازش مجموعه را زیبا می کنند.
- **همه چیز یک شی است**:`3.times { puts "hello" }`— اعداد صحیح متدهایی دارند.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **عملکرد** | کندتر از زبان های کامپایل شده. MRI دارای GIL | از JRuby برای موازی سازی استفاده کنید. بارگذاری به پسوندهای C |
| **کاهش محبوبیت** | پذیرش جدید کمتر در مقایسه با Python، Go، Rust | هنوز به طور گسترده استفاده می شود؛ قوی در راه اندازی وب و مشاوره |
| **تایپ** | تایپ پویا می تواند منجر به خطاهای زمان اجرا شود | از Sorbet یا RBS برای تایپ استاتیک اختیاری |
| **استفاده از حافظه** | ردپای حافظه بالاتر از Go یا Rust | قابل قبول برای اکثر برنامه های تحت وب |
| **بازار کار** | موقعیت های جدید کمتر از پایتون یا جاوا اسکریپت | قوی در سوله های خاص (فروشگاه ریل، مشاوره) |
---

## اصول نحو
### متغیرها و انواع
```ruby
# Variables (no type declarations needed)
name = "Alice"
age = 30
score = 9.5
active = true
items = [1, 2, 3]

# Symbols — immutable, reusable identifiers (unique in memory)
status = :active
type = :user

# Everything is an object
3.class           # => Integer
"hello".length     # => 5
true.to_s          # => "true"
```

### روش ها و بلوک ها
```ruby
# Method definition
def greet(name, greeting = "Hello")
  "#{greeting}, #{name}!"
end

# Blocks — Ruby's signature feature
[1, 2, 3, 4, 5].each do |n|
  puts n
end

# Enumerable methods with blocks
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = numbers.map { |n| n * 2 }
evens = numbers.select { |n| n.even? }
total = numbers.reduce(0) { |sum, n| sum + n }
adults = users.reject { |u| u.age < 18 }
grouped = users.group_by(&:department)

# .times, .upto, .downto
3.times { puts "Hello!" }
1.upto(5) { |n| puts n }

# Yield — methods that accept blocks
def repeat(times)
  times.times { yield }
end

repeat(3) { puts "Again!" }
```

### کلاس ها و ماژول ها
```ruby
# Class
class Animal
  attr_reader :name  # Getter

  def initialize(name)
    @name = name     # Instance variable
  end

  def speak
    "#{@name} makes a sound"
  end
end

# Inheritance
class Dog < Animal
  def speak
    "#{@name} says woof"
  end
end

# Modules — mixins (Ruby's alternative to multiple inheritance)
module Swimmable
  def swim
    "#{self.class.name} is swimming"
  end
end

module Fetchable
  def fetch
    "#{@name} is fetching the ball"
  end
end

class Retriever < Dog
  include Swimmable
  include Fetchable
end

dog = Retriever.new("Rex")
dog.speak   # "Rex says woof"
dog.swim    # "Retriever is swimming"
dog.fetch   # "Rex is fetching the ball"
```

### فرابرنامه نویسی
```ruby
# Dynamic method definition
class Calculator
  %i[add subtract multiply divide].each do |operation|
    define_method(operation) do |a, b|
      a.send(operation.to_s.tr('subtract', '-').tr('add', '+').tr('multiply', '*').tr('divide', '/').split(' ').last, b) rescue nil
    end
  end
end

# method_missing — handle calls to undefined methods
class DynamicHash
  def initialize
    @data = {}
  end

  def method_missing(name, *args)
    key = name.to_s.chomp('=')
    if name.to_s.end_with?('=')
      @data[key] = args.first
    else
      @data[key]
    end
  end
end

config = DynamicHash.new
config.name = "Alice"
config.age = 30
puts config.name  # "Alice"
```

---

## روبی روی ریل
Rails یک چارچوب وب تمام پشته است که از معماری MVC (Model-View-Controller) پیروی می کند و تاکید دارد:
- **کنوانسیون روی پیکربندی**: پیش فرض های معقول - بدون نیاز به پیکربندی همه چیز.
- **خودتان را تکرار نکنید (DRY)**: از ژنراتورها، مهاجرت ها و قراردادها برای به حداقل رساندن تکرار استفاده کنید.
- **Active Record**: اشیاء پایگاه داده اشیاء Ruby هستند. `User.find(1)`یک کاربر را بازیابی می کند.
- ** مهاجرت**: تغییرات طرح واره پایگاه داده کد Ruby نسخه شده است.
Rails به GitHub، Shopify، Stripe (در ابتدایی)، Basecamp، GitLab و بسیاری از استارت آپ ها قدرت می دهد.
---

## نحو و الگوهای پیشرفته
### تایپ اردک و اعزام پویا
```ruby
# Duck typing — if it walks like a duck...
class Logger
  def log(message)
    puts "[#{Time.now.strftime('%H:%M:%S')}] #{message}"
  end
end

class FileLogger
  def initialize(path)
    @path = path
  end

  def log(message)
    File.open(@path, 'a') { |f| f.puts "[#{Time.now}] #{message}" }
  end
end

# Any object that responds to #log can be used
def process(logger)
  logger.log("Processing started")
  logger.log("Processing complete")
end

process(Logger.new)
process(FileLogger.new("/tmp/app.log"))

# respond_to? and send for dynamic dispatch
obj = "hello"
if obj.respond_to?(:upcase)
  result = obj.send(:upcase)  # "HELLO"
end
```

### Procs، Lambdas و Closures
```ruby
# Proc — a block stored in a variable (not strict arity)
square = Proc.new { |x| x * x }
puts square.call(5)     # 25
puts square.call(5, 10) # 25 — extra args ignored

# Lambda — strict arity, returns control to caller
double = ->(x) { x * 2 }
puts double.call(5)     # 10
# double.call(5, 10)    # ArgumentError!

# Closures — blocks capture their surrounding scope
def make_counter
  count = 0
  Proc.new do
    count += 1
    count
  end
end

counter = make_counter
puts counter.call  # 1
puts counter.call  # 2
puts counter.call  # 3

# &block — convert block to proc parameter
def measure(name)
  start = Time.now
  yield
  elapsed = Time.now - start
  puts "#{name} took #{elapsed.round(4)}s"
end

measure("sort") { [5, 3, 1, 4, 2].sort }
```

### تطبیق الگو (Ruby 3.0+)
```ruby
# Case/in pattern matching
def describe_shape(shape)
  case shape
  in { type: :circle, radius: r }
    "Circle with radius #{r}"
  in { type: :rectangle, width: w, height: h }
    "Rectangle #{w}x#{h}"
  in { type: :triangle, base: b, height: h }
    "Triangle with base #{b} and height #{h}"
  end
end

shape = { type: :circle, radius: 5 }
puts describe_shape(shape)  # "Circle with radius 5"

# Pin operator (^) to use existing variables
expected = 200
case response
in { status: ^expected, body: String => body }
  puts "Success: #{body}"
in { status: 400..499 }
  puts "Client error"
in { status: 500..599 }
  puts "Server error"
end
```

### بارگذاری بیش از حد اپراتور
```ruby
class Vector
  attr_reader :x, :y

  def initialize(x, y)
    @x, @y = x, y
  end

  def +(other)
    Vector.new(@x + other.x, @y + other.y)
  end

  def -(other)
    Vector.new(@x - other.x, @y - other.y)
  end

  def *(scalar)
    Vector.new(@x * scalar, @y * scalar)
  end

  def ==(other)
    @x == other.x && @y == other.y
  end

  def to_s
    "Vector(#{@x}, #{@y})"
  end
end

v1 = Vector.new(1, 2)
v2 = Vector.new(3, 4)
puts (v1 + v2)        # Vector(4, 6)
puts (v1 * 3)         # Vector(3, 6)
```
---

## همزمانی و موازی
### موضوعات
```ruby
# Ruby threads (OS-level threads, limited by GIL in MRI)
threads = []
results = []
mutex = Mutex.new

5.times do |i|
  threads << Thread.new do
    result = heavy_computation(i)
    mutex.synchronize { results << result }
  end
end

threads.each(&:join)
puts results.inspect
```

### الیاف - کوروتین های سبک
```ruby
# Fibers — cooperative concurrency (lightweight, manual scheduling)
fiber = Fiber.new do
  puts "Fiber: step 1"
  Fiber.yield
  puts "Fiber: step 2"
  Fiber.yield
  puts "Fiber: step 3"
end

fiber.resume   # Fiber: step 1
fiber.resume   # Fiber: step 2
fiber.resume   # Fiber: step 3

# Fiber for producer pattern
def producer(items)
  Fiber.new do
    items.each { |item| Fiber.yield(item) }
    :done
  end
end

gen = producer([1, 2, 3, 4, 5])
puts gen.resume  # 1
puts gen.resume  # 2
puts gen.resume  # 3

# Fiber Scheduler (Ruby 3.0+) — enables async I/O
require "fiber"
Fiber.set_scheduler(Fiber::Scheduler.new)

Fiber.schedule do
  response = Net::HTTP.get(URI("https://api.example.com/data"))
  puts response
end
```

### Async/Await with Async Gem
```ruby
require "async"

# Async gem — modern async I/O for Ruby
Async do
  task1 = Async do
    sleep(1)
    "Result 1"
  end

  task2 = Async do
    sleep(1)
    "Result 2"
  end

  # Both run concurrently — total time ~1s, not 2s
  puts task1.wait
  puts task2.wait
end
```

---

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه (ریل)
```
my-rails-app/
├── Gemfile
├── Gemfile.lock
├── Rakefile
├── config/
│   ├── application.rb
│   ├── database.yml
│   ├── routes.rb
│   └── environments/
├── app/
│   ├── controllers/
│   ├── models/
│   ├── views/
│   ├── helpers/
│   ├── jobs/
│   └── mailers/
├── db/
│   ├── migrate/
│   ├── schema.rb
│   └── seeds.rb
├── spec/
├── lib/
├── public/
└── bin/
```

### Gemfile - مدیریت وابستگی
```ruby
# Gemfile
source "https://rubygems.org"
ruby "3.3.0"

gem "rails", "~> 7.1"
gem "pg", "~> 1.5"
gem "puma", "~> 6.4"
gem "redis", "~> 5.0"
gem "sidekiq", "~> 7.2"
gem "devise", "~> 4.9"

group :development, :test do
  gem "rspec-rails", "~> 6.1"
  gem "factory_bot_rails", "~> 6.4"
  gem "rubocop", "~> 1.60", require: false
  gem "brakeman", require: false
end

group :test do
  gem "capybara", "~> 3.39"
  gem "selenium-webdriver", "~> 4.16"
end
```

### دستورات وابستگی
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### خط لوله CI/CD (اقدامات GitHub)
```yaml
name: Ruby CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: password
        ports: ["5432:5432"]
    steps:
      - uses: actions/checkout@v4
      - uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true
      - run: bundle exec rails db:create db:migrate
        env:
          DATABASE_URL: postgres://postgres:password@localhost:5432/test
      - run: bundle exec rspec
      - run: bundle exec rubocop
      - run: bundle exec brakeman -q
```

---

## تست
### RSpec - چارچوب تست
```ruby
# spec/models/user_spec.rb
require "rails_helper"

RSpec.describe User, type: :model do
  describe "validations" do
    it "requires a name" do
      user = User.new(name: nil)
      expect(user).not_to be_valid
      expect(user.errors[:name]).to include("can't be blank")
    end

    it "requires a unique email" do
      create(:user, email: "alice@example.com")
      duplicate = build(:user, email: "alice@example.com")
      expect(duplicate).not_to be_valid
    end
  end

  describe "#full_name" do
    it "combines first and last name" do
      user = build(:user, first_name: "Alice", last_name: "Smith")
      expect(user.full_name).to eq("Alice Smith")
    end
  end

  describe ".active" do
    it "returns only active users" do
      active = create(:user, active: true)
      inactive = create(:user, active: false)
      expect(User.active).to include(active)
      expect(User.active).not_to include(inactive)
    end
  end
end
```

### تمسخر و لج کردن
```ruby
RSpec.describe PaymentService do
  let(:user) { build(:user) }
  let(:stripe_mock) { instance_double(Stripe::Charge) }

  before do
    allow(Stripe::Charge).to receive(:create).and_return(stripe_mock)
    allow(stripe_mock).to receive(:id).and_return("ch_123")
    allow(stripe_mock).to receive(:status).and_return("succeeded")
  end

  it "creates a Stripe charge" do
    service = PaymentService.new(user)
    result = service.charge(5000)

    expect(result.status).to eq("succeeded")
    expect(Stripe::Charge).to have_received(:create).with(
      hash_including(amount: 5000, currency: "usd")
    )
  end
end
```

### دستورات تست
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## قابلیت همکاری
### برنامه های افزودنی C
```ruby
# Ruby can call C code directly via C extensions
# ext/my_extension/extconf.rb
require "mkmf"
create_makefile("my_extension")

# ext/my_extension/my_extension.c
# #include "ruby.h"
# static VALUE rb_fast_sum(VALUE self, VALUE rb_array) {
#     int len = RARRAY_LEN(rb_array);
#     double sum = 0.0;
#     for (int i = 0; i < len; i++) {
#         sum += NUM2DBL(RARRAY_AREF(rb_array, i));
#     }
#     return rb_float_new(sum);
# }
# void Init_my_extension(void) {
#     VALUE m = rb_define_module("MyModule");
#     rb_define_singleton_method(m, "fast_sum", rb_fast_sum, 1);
# }

# Usage in Ruby
require "my_extension"
total = MyModule.fast_sum([1.5, 2.5, 3.0])  # 7.0
```

### FFI - رابط عملکرد خارجی
```ruby
require "ffi"

# Call C libraries without writing C extensions
module Zlib
  extend FFI::Library
  ffi_lib "z"

  attach_function :zlibVersion, [], :string
  attach_function :crc32, [:ulong, :pointer, :uint], :ulong
end

puts Zlib.zlibVersion  # "1.2.13"
```

### JRuby - قابلیت همکاری JVM
```ruby
# JRuby runs on the JVM — access Java classes directly
java_import "java.util.ArrayList"
java_import "java.time.LocalDate"

list = ArrayList.new
list.add("Hello")
list.add("World")
puts list.size  # 2

today = LocalDate.now
puts today  # 2024-01-15
```

---

## الگوهای طراحی
### الگوی مشاهده گر
```ruby
class EventEmitter
  def initialize
    @listeners = Hash.new { |h, k| h[k] = [] }
  end

  def on(event, &block)
    @listeners[event] << block
  end

  def emit(event, *args)
    @listeners[event].each { |listener| listener.call(*args) }
  end
end

emitter = EventEmitter.new
emitter.on(:user_created) { |user| puts "Welcome, #{user[:name]}!" }
emitter.emit(:user_created, { name: "Alice", email: "alice@example.com" })
```

### الگوی کارخانه
```ruby
class PaymentProcessor
  def self.for(type)
    case type.to_sym
    when :stripe  then StripeProcessor.new
    when :paypal  then PayPalProcessor.new
    when :crypto  then CryptoProcessor.new
    else raise ArgumentError, "Unknown payment type: #{type}"
    end
  end
end

processor = PaymentProcessor.for(:stripe)
processor.charge(5000)
```

### الگوی دکوراتور
```ruby
module Timestampable
  def log(message)
    super("[#{Time.now.strftime('%H:%M:%S')}] #{message}")
  end
end

class Logger
  def log(message)
    puts message
  end
end

class TimestampedLogger < Logger
  prepend Timestampable
end

logger = TimestampedLogger.new
logger.log("Hello!")  # [14:30:22] Hello!
```
---

## عملکرد و بهینه سازی
### ابزارهای پروفایل
```bash
# Ruby profiler (built-in)
ruby -r profile my_script.rb

# StackProf — sampling CPU profiler
gem install stackprof
ruby -r stackprof -e "StackProf.run(mode: :cpu, out: 'tmp/stackprof') { App.run }"
stackprof tmp/stackprof --text

# Memory profiling
gem install memory_profor
ruby -r memory_profiler -e "MemoryProfiler.report { App.run }.pretty_print"

# Benchmarking
require "benchmark"
Benchmark.bm do |x|
  x.report("map:")  { 1_000_000.times.map { |i| i * 2 } }
  x.report("each:") { a = []; 1_000_000.times.each { |i| a << i * 2 } }
end
```

### تکنیک های بهینه سازی
```ruby
# 1. Freeze string literals (saves memory)
# frozen_string_literal: true

# 2. Use symbols over strings for hash keys
config = { database: "pg", host: "localhost" }  # Good

# 3. Use << for string concatenation in loops
result = +""
lines.each { |line| result << line << "\n" }

# 4. Use Enumerator::Lazy for large collections
(1..1_000_000).lazy
  .select { |n| n.even? }
  .map { |n| n * n }
  .first(10)
  .to_a

# 5. Use concurrent-ruby for parallelism
require "concurrent"
future = Concurrent::Future.execute { heavy_computation }
result = future.value
```

---

## استقرار
### وب سرور پوما
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### استقرار داکر
```dockerfile
FROM ruby:3.3-slim
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
WORKDIR /app
COPY Gemfile Gemfile.lock ./
RUN bundle config set deployment true && bundle install
COPY . .
ENV RAILS_ENV=production
RUN bundle exec rails assets:precompile
EXPOSE 3000
CMD ["bundle", "exec", "puma", "-C", "config/puma.rb"]
```

### استقرار پلتفرم
```bash
# Heroku
heroku create my-app
git push heroku main
heroku run rails db:migrate

# Fly.io
fly launch --name my-ruby-app
fly deploy
```

---

## چه زمانی از روبی استفاده کنیم
| سناریو | چرا روبی | جایگزین بهتر |
|----------|---------|-------------------|
| برنامه های کاربردی وب (ریل) | توسعه سریع، چارچوب تولیدی | جنگو (پایتون)، لاراول (PHP)، Next.js |
| نمونه سازی | بسیار سریع برای نوشتن و تکرار | پایتون، جاوا اسکریپت |
| اسکریپت نویسی و اتوماسیون | نحو زیبا، پردازش متن قدرتمند | پایتون، شل |
| ابزار DevOps (آشپز، عروسک) | اکوسیستم تاسیس شده | برو، پایتون |
| ابزارهای CLI | ممکن است اما ایده آل نیست | برو زنگ بزن |
| سیستم های حیاتی عملکرد | خیلی کند | C، C++، Rust، Go |
| علم داده / ML | نه اکوسیستم | پایتون، R |
| برنامه های موبایل | مناسب نیست | سوئیفت، کاتلین، فلاتر |
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت `proc`،`lambda`و`block`در روبی چیست؟
**الف:** هر سه بسته هستند، اما در رفتار با هم فرق دارند.`block`یک تکه کد ناشناس است که به روشی با`do...end`یا`{}`ارسال می شود. یک`proc`بلوکی است که به عنوان یک شی ذخیره می شود - تعداد آرگومان ها را بررسی نمی کند و`return`از روش محصور کردن خارج می شود. یک`lambda`مانند یک proc است اما تعداد آرگومان ها را بررسی می کند و`return`فقط از لامبدا خارج می شود. هنگامی که به رفتاری شبیه به روش نیاز دارید، از بلوک‌ها برای تماس‌های یک‌باره، پروک‌ها برای تکه‌های قابل استفاده مجدد و لامبدا استفاده کنید.
```ruby
# Block — passed to method, not an object
def each_with_index(arr)
  arr.each_with_index { |item, i| yield(item, i) }
end

# Proc — reusable, return exits enclosing method
square = Proc.new { |x| x * x }
puts square.call(5)   # 25

# Lambda — checks arity, return exits only the lambda
double = ->(x) { x * 2 }
puts double.call(5)   # 10
# double.call(1, 2)   # ArgumentError: wrong number of arguments

def test_return
  lam = -> { return "from lambda" }
  result = lam.call
  puts result  # "from lambda" — method continues
  "method result"
end
```

### Q2: سنگهای روبی و باندلر چگونه کار می کنند؟
**A:** Gems سیستم بسته روبی هستند — کتابخانه های قابل استفاده مجدد که از طریق RubyGems.org توزیع شده اند. یک`Gemfile`وابستگی ها را اعلام می کند. `bundle install`نسخه ها را حل می کند و یک`Gemfile.lock`برای تکرارپذیری ایجاد می کند. `bundle exec`دستورات را در زمینه Gem اجرا می کند. از`gem 'name', '~> 2.0'`برای محدودیت های نسخه سازگار استفاده کنید. همیشه`Gemfile.lock`را برای برنامه ها متعهد کنید، اما نه برای کتابخانه ها.
```ruby
# Gemfile
source "https://rubygems.org"

ruby "3.3.0"

gem "rails", "~> 7.1"
gem "pg", "~> 1.5"
gem "puma", "~> 6.0"

group :development, :test do
  gem "rspec", "~> 3.12"
  gem "rubocop", "~> 1.50"
end
```

```bash
bundle install        # Install gems from Gemfile
bundle update rails   # Update specific gem
bundle exec rspec     # Run rspec with correct gem versions
bundle audit check    # Check for security vulnerabilities
```

### Q3: انواع نمادهای روبی چیست و چرا مهم هستند؟
**الف:** نمادها (`:name`) رشته های غیرقابل تغییر و درونی هستند - هر نماد منحصر به فرد فقط یک بار در حافظه وجود دارد. آنها برای کلیدهای هش، نام روش ها و شناسه ها ایده آل هستند. روبی همچنین دارای اشیاء`Symbol`است که به طور گسترده در فرابرنامه‌نویسی استفاده می‌شوند (`send`، `define_method`). از نمادها برای شناسه های ثابت استفاده کنید. زمانی که نیاز به دستکاری محتوا دارید از رشته ها استفاده کنید.
```ruby
# Symbols are interned — same name = same object
:name.object_id == :name.object_id   # true
"name".object_id == "name".object_id # false (different String objects)

# As hash keys (most common use)
user = { name: "Alice", age: 30 }   # Syntax sugar for { :name => "Alice" }

# Dynamic symbol creation
method_name = "to_s".to_sym
42.send(method_name)   # "42"

# Frozen string literal (Ruby 3.x defaults to frozen)
# frozen_string_literal: true
str = "hello"  # This string is frozen
```

### Q4: فرابرنامه‌نویسی Ruby چگونه کار می‌کند و چه زمانی باید از آن استفاده کنم؟
**A:** Ruby به کد اجازه می دهد تا کد را در زمان اجرا تعریف کند:`define_method`روش ها را به صورت پویا ایجاد می کند،`method_missing`فراخوانی های متد تعریف نشده را قطع می کند،`send`روش های خصوصی را فرا می خواند و`class_eval`/`instance_eval`کد زمینه را در یک کلاس ارزیابی می کند. فرابرنامه‌نویسی قدرتمند است اما درک کد را سخت‌تر می‌کند – از آن برای DSL و جادوی فریمورک استفاده کنید، نه برای منطق روزمره.
```ruby
# define_method — dynamic method creation
class Config
  %w[host port timeout].each do |attr|
    define_method(attr) { @settings[attr.to_sym] }
    define_method("#{attr}=") { |val| @settings[attr.to_sym] = val }
  end
end

# method_missing — catch-all for undefined methods
class DynamicHash
  def initialize(data = {})
    @data = data
  end

  def method_missing(name, *args)
    key = name.to_s.chomp("=").to_sym
    if name.to_s.end_with?("=")
      @data[key] = args.first
    elsif @data.key?(key)
      @data[key]
    else
      super
    end
  end

  def respond_to_missing?(name, include_private = false)
    key = name.to_s.chomp("=").to_sym
    @data.key?(key) || name.to_s.end_with?("=") || super
  end
end

config = DynamicHash.new(name: "Alice")
config.name     # "Alice"
config.age = 30 # Sets @data[:age]
```

### Q5: بهترین راه برای رسیدگی به خطاها در Ruby چیست؟
**A:** روبی از استثناها برای مدیریت خطا استفاده می کند. کلاس‌های استثنای سفارشی را تعریف کنید که از`StandardError`به ارث می‌برند (نه`Exception`- که خطاهای سطح سیستم را می‌گیرد). از`begin/rescue/else/ensure`برای مدیریت ساخت یافته استفاده کنید. استثناهای خاص را مطرح کنید، نه`RuntimeError`عمومی. از`rescue`به عنوان یک اصلاح کننده برای تک لاینرهای ساده استفاده کنید.
```ruby
# Custom exception hierarchy
class AppError < StandardError; end
class NotFoundError < AppError; end
class ValidationError < AppError; end

# Structured handling
begin
  user = find_user(id)
  validate!(user)
rescue NotFoundError => e
  logger.warn("User not found: #{e.message}")
  redirect_to "/users"
rescue ValidationError => e
  flash[:error] = e.message
  render :edit
rescue StandardError => e
  logger.error("Unexpected: #{e.class}: #{e.message}")
  raise  # Re-raise for error tracking
ensure
  cleanup_temp_files
end

# Rescue modifier
value = parse(input) rescue default_value
```

---

## حل مسئله زنجیره ای از فکر
### مشکل 1: یک DSL برای فایل های پیکربندی بسازید
**بیانیه مشکل:** یک Ruby DSL ایجاد کنید که امکان تعریف تنظیمات سرور را در یک نحو خوانا و اعلانی فراهم می کند. DSL باید بلوک‌های تودرتو، اعتبارسنجی و سریال‌سازی برای JSON را پشتیبانی کند.
** مرحله 1 - مشکل را درک کنید:**
ما نیاز داریم: (1) یک نحو DSL تمیز با استفاده از بلوک ها و فراخوانی روش، (2) جمع آوری داده ها از طریق`instance_eval`یا روش های صریح، (3) اعتبارسنجی فیلدهای مورد نیاز، (4) سریال سازی JSON. فرابرنامه نویسی روبی DSL ها را طبیعی می کند.
** مرحله 2 - شناسایی رویکرد: **
- از`instance_eval`با کلاس سازنده برای ضبط تماس های DSL استفاده کنید.
- ذخیره پیکربندی در متغیرهای نمونه.
- فیلدهای مورد نیاز را قبل از سریال سازی اعتبار سنجی کنید.
- برای خروجی از`to_h`و`JSON.generate`استفاده کنید.
**مرحله 3 - راه حل را اجرا کنید:**
```ruby
require 'json'

class ServerConfig
  attr_reader :name, :host, :port, :ssl, :endpoints, :env

  def initialize(&block)
    @endpoints = []
    @env = {}
    @ssl = false
    instance_eval(&block) if block
    validate!
  end

  def name(val = nil)
    val ? @name = val : @name
  end

  def host(val = nil)
    val ? @host = val : @host
  end

  def port(val = nil)
    val ? @port = val.to_i : @port
  end

  def ssl(val = true)
    @ssl = val
  end

  def endpoint(path, method: :get, timeout: 30)
    @endpoints << { path: path, method: method, timeout: timeout }
  end

  def environment(key, value)
    @env[key.to_s] = value.to_s
  end

  def validate!
    raise ArgumentError, "name is required" unless @name
    raise ArgumentError, "host is required" unless @host
    raise ArgumentError, "port is required" unless @port
  end

  def to_h
    {
      name: @name, host: @host, port: @port, ssl: @ssl,
      endpoints: @endpoints, environment: @env
    }
  end

  def to_json(*args)
    JSON.pretty_generate(to_h, *args)
  end
end

# DSL usage
config = ServerConfig.new do
  name "api-server"
  host "0.0.0.0"
  port 8443
  ssl true

  endpoint "/api/users", method: :get, timeout: 10
  endpoint "/api/users", method: :post, timeout: 30
  endpoint "/health", method: :get

  environment :database_url, "postgres://localhost/mydb"
  environment :redis_url, "redis://localhost:6379"
end

puts config.to_json
```

** مرحله 4 - تأیید و بهینه سازی: **
- DSL قابل خواندن و بیانی است - غیر برنامه نویسان می توانند آن را درک کنند.
- صید اعتبار سنجی از دست رفته زمینه های مورد نیاز در زمان ساخت و ساز.
-`instance_eval`سینتکس بلوک تمیز را فراهم می کند اما`self`را محدود می کند - برای DSL های پیچیده تر، از`BasicObject`به عنوان سوپرکلاس سازنده استفاده کنید.
- تولید: سنگهای`dry-configurable`یا`configurate`را برای DSLهای پیکربندی درجه تولید در نظر بگیرید.
### مشکل 2: یک کتابخانه حافظه را پیاده سازی کنید
**بیانیه مشکل:** یک ماژول ذخیره سازی بسازید که می تواند با هر کلاسی ترکیب شود تا نتایج روش کش را ذخیره کند. پشتیبانی از TTL (زمان تا زندگی)، محدودیت‌های اندازه حافظه پنهان و کلیدهای کش سفارشی.
** مرحله 1 - مشکل را درک کنید:**
ما به این موارد نیاز داریم: (1) یک ماژول که یک متد کلاس`memoize`اضافه می کند، (2) روش متدهای هدف را با منطق ذخیره سازی پنهان می کند، (3) پشتیبانی از انقضای TTL، (4) حذف LRU زمانی که کش پر است.`Module#prepend`و`define_method`روبی برای این کار ایده آل هستند.
** مرحله 2 - شناسایی رویکرد: **
- از`Module.new`با`define_method`برای ایجاد یک لفاف استفاده کنید.
- حافظه پنهان را در یک هش با مُهر زمانی برای TTL ذخیره کنید.
- از`prepend`برای درج لایه کش قبل از روش اصلی استفاده کنید.
- پشتیبانی از گزینه های قابل تنظیم: `ttl`، `max_size`، `key`.
**مرحله 3 - راه حل را اجرا کنید:**
```ruby
module Memoizable
  def memoize(method_name, ttl: nil, max_size: 1000, key: nil)
    original = instance_method(method_name)

    cache = {}
    timestamps = {}
    mutex = Mutex.new

    define_method(method_name) do |*args, **kwargs, &blk|
      cache_key = key ? key.call(*args, **kwargs) : [method_name, args, kwargs]

      mutex.synchronize do
        # Check TTL expiration
        if timestamps[cache_key] && ttl
          age = Time.now - timestamps[cache_key]
          if age > ttl
            cache.delete(cache_key)
            timestamps.delete(cache_key)
          end
        end

        # Return cached value if present
        if cache.key?(cache_key)
          return cache[cache_key]
        end

        # Evict oldest if at capacity
        if cache.size >= max_size
          oldest = timestamps.min_by { |_, v| v }&.first
          cache.delete(oldest)
          timestamps.delete(oldest)
        end
      end

      # Compute value outside lock to avoid holding lock during computation
      result = original.bind(self).call(*args, **kwargs, &blk)

      mutex.synchronize do
        cache[cache_key] = result
        timestamps[cache_key] = Time.now
      end

      result
    end
  end
end

# Usage
class UserService
  extend Memoizable

  def find_user(id)
    sleep(1)  # Simulate expensive operation
    { id: id, name: "User #{id}" }
  end
  memoize :find_user, ttl: 300, max_size: 500

  def expensive_calculation(data, options: {})
    # Expensive computation...
    data.hash * (options[:factor] || 1)
  end
  memoize :expensive_calculation, key: ->(data, **opts) { [data.hash, opts] }
end

service = UserService.new
service.find_user(1)  # Takes 1 second
service.find_user(1)  # Instant — cached!
```

** مرحله 4 - تأیید و بهینه سازی: **
- ایمنی موضوع:`Mutex`از خواندن/نوشتن حافظه پنهان محافظت می کند. محاسبه خارج از قفل اتفاق می افتد.
- TTL: ورودی های منقضی شده در هنگام دسترسی به راحتی پاک می شوند.
- اخراج LRU: وقتی حافظه پنهان از`max_size`بیشتر شود، قدیمی ترین ورودی (بر اساس زمان) حذف می شود.
- کلیدهای سفارشی: لامبدا`key`امکان کنترل دقیق روی هویت حافظه پنهان را فراهم می کند.
- تولید: از جم`memoist`برای موارد ساده، یا از یادداشت پشتیبان Redis برای ذخیره سازی توزیع شده استفاده کنید.
---

## خلاصه
روبی زبانی است که شادی و بیان توسعه دهندگان را در اولویت قرار می دهد. نحو آن یکی از خواناترین زبان‌ها است و Ruby on Rails یکی از سازنده‌ترین چارچوب‌های وب است که تا کنون ایجاد شده است. در حالی که محبوبیت روبی نسبت به پایتون و جاوا اسکریپت کاهش یافته است، اما همچنان یک زبان قدرتمند و لذت بخش برای توسعه وب، اسکریپت نویسی و اتوماسیون است. اگر برای کد ظریف و توسعه سریع ارزش قائل هستید، روبی ارزش یادگیری را دارد.