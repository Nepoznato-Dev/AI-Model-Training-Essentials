---
# فراداده
عنوان: "روبی"
توضیحات: "مرجع جامع برای زبان برنامه نویسی Ruby شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب ها: [یاقوت، زبان برنامه نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "34 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
#یاقوت
روبی یک زبان برنامه نویسی پویا، تفسیر شده و شی گرا است که توسط Yukihiro "Matz" Matsumoto ایجاد شد و اولین بار در سال 1995 در ژاپن منتشر شد. روبی با تمرکز بر شادی برنامه نویس طراحی شده است - نحو آن زیبا و طبیعی است و تقریباً مانند انگلیسی خوانده می شود. همه چیز در روبی یک شی است، از جمله انواع اولیه مانند اعداد صحیح و بولی. روبی بیشتر به خاطر چارچوب وب Ruby on Rails شناخته می شود، که توسعه وب را با رایج کردن قراردادها بر روی پیکربندی و نمونه سازی سریع، انقلابی در توسعه وب ایجاد کرد.
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

## خلاصه
روبی زبانی است که شادی و بیان توسعه دهندگان را در اولویت قرار می دهد. نحو آن یکی از خواناترین زبان‌ها است و Ruby on Rails یکی از سازنده‌ترین چارچوب‌های وب است که تا کنون ایجاد شده است. در حالی که محبوبیت روبی نسبت به پایتون و جاوا اسکریپت کاهش یافته است، اما همچنان یک زبان قدرتمند و لذت بخش برای توسعه وب، اسکریپت نویسی و اتوماسیون است. اگر برای کد ظریف و توسعه سریع ارزش قائل هستید، روبی ارزش یادگیری را دارد.