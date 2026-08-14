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

#روبی
روبی ایک متحرک، تشریح شدہ، آبجیکٹ پر مبنی پروگرامنگ زبان ہے جسے Yukihiro "Matz" Matsumoto نے تخلیق کیا تھا اور پہلی بار 1995 میں جاپان میں جاری کیا گیا تھا۔ روبی کو پروگرامر کی خوشی پر فوکس کرتے ہوئے ڈیزائن کیا گیا تھا — اس کا نحو خوبصورت اور قدرتی ہے، تقریباً انگریزی کی طرح پڑھنا۔ روبی میں ہر چیز ایک آبجیکٹ ہے، بشمول انٹیجرز اور بولین جیسی قدیم اقسام۔ روبی کو روبی آن ریلز ویب فریم ورک کے لیے سب سے زیادہ جانا جاتا ہے، جس نے کنفیگریشن اور تیز رفتار پروٹو ٹائپنگ پر کنونشن کو مقبول بنا کر ویب ڈویلپمنٹ میں انقلاب برپا کیا۔
ریلوں سے آگے، روبی کو اسکرپٹنگ، آٹومیشن، ڈی او اوپس ٹولنگ (شیف، پپیٹ) اور عام مقصد کی زبان کے طور پر استعمال کیا جاتا ہے۔ اس کی تاثراتی ترکیب اور طاقتور میٹاپروگرامنگ کی صلاحیتیں اسے لکھنے میں خوشی کا باعث بنتی ہیں۔
---

## روبی کیوں اہمیت رکھتی ہے۔
- **ڈیولپر خوشی**: روبی کو پڑھنے کے قابل اور لطف اندوز ہونے کے لیے ڈیزائن کیا گیا ہے۔ "روبی پروگرامرز کو خوش کرنے کے لیے ڈیزائن کیا گیا ہے" - میٹز۔
- **اثری نحو**: کوڈ انگریزی کی طرح پڑھتا ہے۔ کم سے کم اوقاف، فطری جملہ۔
- **Ruby on Rails**: اب تک بنائے گئے سب سے زیادہ پیداواری ویب فریم ورکس میں سے ایک۔ GitHub، Shopify، Basecamp، GitLab کو طاقت دیتا ہے۔
- **Metaprogramming**: Ruby رن ٹائم پر خود کو تبدیل کر سکتا ہے — طریقوں کو متحرک طور پر متعین کریں، ڈومین کے لیے مخصوص زبانیں (DSLs) بنائیں۔
- **بلاک/ایٹریٹر پیٹرن**: روبی کے بلاکس اور تکرار کرنے والے کلیکشن پروسیسنگ کو خوبصورت بناتے ہیں۔
- **ہر چیز ایک شے ہے**:`3.times { puts "hello" }`— عدد کے طریقے ہوتے ہیں۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **کارکردگی** | مرتب شدہ زبانوں سے سست؛ MRI میں GIL ہے | متوازی کے لیے JRuby استعمال کریں۔ C ایکسٹینشن پر آف لوڈ |
| **گرتی ہوئی مقبولیت** | ازگر، گو، زنگ کے مقابلے میں کم نیا اپنانا | اب بھی بڑے پیمانے پر استعمال کیا جاتا ہے؛ ویب اسٹارٹ اپ اور مشاورت میں مضبوط |
| **ٹائپنگ** | ڈائنامک ٹائپنگ رن ٹائم کی غلطیوں کا باعث بن سکتی ہے۔ اختیاری جامد ٹائپنگ کے لیے شربت یا RBS استعمال کریں۔
| **میموری کا استعمال** | گو یا زنگ سے زیادہ میموری فوٹ پرنٹ | زیادہ تر ویب ایپلیکیشنز کے لیے قابل قبول |
| **ملازمت کی منڈی** | Python یا JavaScript سے کم نئی پوزیشنیں | مخصوص طاقوں میں مضبوط (ریل کی دکانیں، مشاورت) |
---

## نحوی بنیادی باتیں
### متغیرات اور اقسام
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

### طریقے اور بلاکس
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

### کلاسز اور ماڈیولز
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

### میٹا پروگرامنگ
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

## ریلوں پر روبی
ریلز ایک مکمل اسٹیک ویب فریم ورک ہے جو MVC (ماڈل-ویو-کنٹرولر) کے فن تعمیر اور اس پر زور دیتا ہے:
- **کنفیگریشن پر کنونشن**: سمجھدار ڈیفالٹس - ہر چیز کو ترتیب دینے کی ضرورت نہیں ہے۔
- **اپنے آپ کو نہ دہرائیں (DRY)**: تکرار کو کم سے کم کرنے کے لیے جنریٹر، منتقلی اور کنونشنز کا استعمال کریں۔
- **ایکٹو ریکارڈ**: ڈیٹا بیس کی اشیاء روبی آبجیکٹ ہیں۔ `User.find(1)`صارف کو بازیافت کرتا ہے۔
- **ہجرت**: ڈیٹا بیس اسکیما کی تبدیلیاں روبی کوڈ کی شکل میں ہیں۔
ریل GitHub، Shopify، Stripe (ابتدائی)، Basecamp، GitLab، اور بہت سے اسٹارٹ اپس کو طاقت دیتی ہے۔
---

## اعلی درجے کی نحو اور نمونے۔
### بتھ ٹائپنگ اور ڈائنامک ڈسپیچ
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

### پروکس، لیمبڈاس، اور بندش
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

### پیٹرن میچنگ (روبی 3.0+)
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

### آپریٹر اوورلوڈنگ
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

## ہم آہنگی اور ہم آہنگی
### تھریڈز
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

### فائبرز - ہلکے وزن والے کوروٹائنز
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

### Async / Async Gem کے ساتھ انتظار کریں۔
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ (ریلز)
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

### جیم فائل - انحصار کا انتظام
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

### انحصار کے احکامات
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### RSpec — ٹیسٹنگ فریم ورک
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

### طنز اور ضد
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

### ٹیسٹ کمانڈز
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## انٹرآپریبلٹی
### C ایکسٹینشنز
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

### FFI - غیر ملکی فنکشن انٹرفیس
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

### JRuby — JVM انٹرآپریبلٹی
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

## ڈیزائن پیٹرن
### مبصر پیٹرن
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

### فیکٹری پیٹرن
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

### ڈیکوریٹر پیٹرن
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
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

### اصلاح کی تکنیک
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

## تعیناتی۔
### پوما ویب سرور
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### ڈاکر کی تعیناتی۔
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

### پلیٹ فارم کی تعیناتی۔
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

## روبی کب استعمال کریں۔
| منظر نامہ | کیوں روبی | بہتر متبادل |
|------------|---------|-------------------|
| ویب ایپلیکیشنز (ریلز) | تیز رفتار ترقی، پیداواری فریم ورک | Django (Python)، Laravel (PHP)، Next.js |
| پروٹو ٹائپنگ | لکھنے اور تکرار کرنے میں بہت تیز | Python, JavaScript |
| سکرپٹ اور آٹومیشن | خوبصورت نحو، طاقتور ٹیکسٹ پروسیسنگ | ازگر، شیل |
| DevOps ٹولنگ (شیف، کٹھ پتلی) | قائم کردہ ماحولیاتی نظام | جاؤ، ازگر |
| CLI ٹولز | ممکن ہے لیکن مثالی نہیں | جاؤ، مورچا |
| کارکردگی کے اہم نظام | بہت سست | C, C++, Rust, Go |
| ڈیٹا سائنس / ایم ایل | ماحولیاتی نظام نہیں | ازگر، آر |
| موبائل ایپس | مناسب نہیں | سوئفٹ، کوٹلن، پھڑپھڑانا |
---

## مصنوعی سوال و جواب
### Q1: روبی میں `proc`، `lambda`، اور`block`میں کیا فرق ہے؟
**A:** تینوں بندشیں ہیں، لیکن وہ رویے میں مختلف ہیں۔ ایک`block`کوڈ کا ایک گمنام حصہ ہے جسے`do...end`یا`{}`کے ساتھ ایک طریقہ کو دیا گیا ہے۔ ایک`proc`ایک بلاک ہے جسے ایک آبجیکٹ کے طور پر محفوظ کیا گیا ہے - یہ دلیل کی گنتی کی جانچ نہیں کرتا ہے اور`return`منسلک کرنے کے طریقہ سے باہر نکلتا ہے۔ ایک`lambda`ایک proc کی طرح ہے لیکن دلیل کی گنتی کو چیک کرتا ہے اور`return`صرف لیمبڈا سے باہر نکلتا ہے۔ ون آف کال بیکس کے لیے بلاکس، دوبارہ قابل استعمال ٹکڑوں کے لیے پروکس، اور جب آپ کو طریقہ کار جیسا رویہ درکار ہو تو لیمبڈا استعمال کریں۔
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

### Q2: روبی جواہرات اور بنڈلر کیسے کام کرتے ہیں؟
**A:** جواہرات روبی کا پیکیج سسٹم ہیں — دوبارہ قابل استعمال لائبریریوں کو RubyGems.org کے ذریعے تقسیم کیا گیا ہے۔ ایک`Gemfile`انحصار کا اعلان کرتا ہے۔ `bundle install`ورژنز کو حل کرتا ہے اور تولیدی صلاحیت کے لیے ایک`Gemfile.lock`تخلیق کرتا ہے۔ `bundle exec`منی سیاق و سباق میں کمانڈ چلاتا ہے۔ مطابقت پذیر ورژن کی رکاوٹوں کے لیے`gem 'name', '~> 2.0'`استعمال کریں۔ ایپلیکیشنز کے لیے ہمیشہ`Gemfile.lock`کا ارتکاب کریں، لیکن لائبریریوں کے لیے نہیں۔
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

### Q3: روبی کی علامت کی اقسام کیا ہیں، اور وہ کیوں اہم ہیں؟
**A:** علامتیں (`:name`) ناقابل تغیر، اندرونی تار ہیں — ہر منفرد علامت میموری میں صرف ایک بار موجود ہوتی ہے۔ وہ ہیش کیز، طریقہ کار کے ناموں اور شناخت کنندگان کے لیے مثالی ہیں۔ روبی کے پاس`Symbol`اشیاء بھی ہیں جو میٹاپروگرامنگ میں بڑے پیمانے پر استعمال ہوتی ہیں (`send`,`define_method`)۔ مقررہ شناخت کنندگان کے لیے علامتیں استعمال کریں۔ جب آپ کو مواد میں ہیرا پھیری کرنے کی ضرورت ہو تو اسٹرنگ استعمال کریں۔
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

### Q4: روبی کی میٹا پروگرامنگ کیسے کام کرتی ہے، اور مجھے اسے کب استعمال کرنا چاہیے؟
**A:** روبی کوڈ کو رن ٹائم کے وقت کوڈ کی وضاحت کرنے کی اجازت دیتا ہے:`define_method`متحرک طریقے سے طریقے تخلیق کرتا ہے،`method_missing`غیر متعینہ طریقہ کالوں کو روکتا ہے،`send`نجی طریقوں کو کال کرتا ہے، اور`class_eval`/`instance_eval`کوڈ کو سیاق و سباق میں کلاس میں۔ Metaprogramming طاقتور ہے لیکن کوڈ کو سمجھنا مشکل بناتا ہے — اسے DSLs اور فریم ورک کے جادو کے لیے استعمال کریں، روزمرہ کی منطق کے لیے نہیں۔
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

### Q5: روبی میں غلطیوں کو سنبھالنے کا بہترین طریقہ کیا ہے؟
**A:** روبی غلطی سے نمٹنے کے لیے مستثنیات کا استعمال کرتی ہے۔`StandardError`(`Exception` نہیں — جو سسٹم کی سطح کی خرابیوں کو پکڑتا ہے) سے وراثت میں ملنے والی حسب ضرورت استثنائی کلاسز کی وضاحت کریں۔ ساختی ہینڈلنگ کے لیے`begin/rescue/else/ensure`استعمال کریں۔ مخصوص مستثنیات اٹھائیں، عام`RuntimeError`نہیں۔ سادہ ون لائنرز کے لیے`rescue`کو ترمیم کار کے طور پر استعمال کریں۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: کنفیگریشن فائلوں کے لیے ڈی ایس ایل بنائیں
**مسئلہ کا بیان:** ایک روبی ڈی ایس ایل بنائیں جو پڑھنے کے قابل، اعلانیہ نحو میں سرور کنفیگریشن کی وضاحت کرنے کی اجازت دیتا ہے۔ DSL کو JSON کو نیسٹڈ بلاکس، توثیق اور سیریلائزیشن کی حمایت کرنی چاہیے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) بلاکس اور میتھڈ کالز کا استعمال کرتے ہوئے ایک صاف DSL نحو، (2)`instance_eval`یا واضح طریقوں کے ذریعے ڈیٹا اکٹھا کرنا، (3) مطلوبہ فیلڈز کی توثیق، (4) JSON سیریلائزیشن۔ روبی کی میٹا پروگرامنگ ڈی ایس ایل کو قدرتی بناتی ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- DSL کالز کیپچر کرنے کے لیے بلڈر کلاس کے ساتھ`instance_eval`استعمال کریں۔
- مثال کے متغیر میں ترتیب کو اسٹور کریں۔
- سیریلائزیشن سے پہلے مطلوبہ فیلڈز کی توثیق کریں۔
- آؤٹ پٹ کے لیے`to_h`اور`JSON.generate`استعمال کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- DSL پڑھنے کے قابل اور اعلانیہ ہے - غیر پروگرامر اسے سمجھ سکتے ہیں۔
- توثیق تعمیر کے وقت غائب مطلوبہ فیلڈز کو پکڑتی ہے۔
-`instance_eval`کلین بلاک نحو فراہم کرتا ہے لیکن`self`کو محدود کرتا ہے — زیادہ پیچیدہ DSLs کے لیے،`BasicObject`کو بلڈر کے سپر کلاس کے طور پر استعمال کریں۔
- پیداوار: پروڈکشن گریڈ کنفیگریشن DSLs کے لیے`dry-configurable`یا`configurate`جواہرات پر غور کریں۔
### مسئلہ 2: یادداشت کی لائبریری کو لاگو کریں۔
**مسئلہ کا بیان:** ایک میموائزیشن ماڈیول بنائیں جسے کسی بھی کلاس میں ملا کر طریقہ کار کے نتائج کیش کریں۔ TTL (ٹائم ٹو لائیو)، کیش سائز کی حد، اور حسب ضرورت کیش کیز کو سپورٹ کریں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) ایک ماڈیول جو ایک`memoize`کلاس طریقہ کا اضافہ کرتا ہے، (2) طریقہ کیشنگ منطق کے ساتھ ہدف کے طریقوں کو لپیٹتا ہے، (3) TTL کی میعاد ختم ہونے کے لیے سپورٹ، (4) کیش بھر جانے پر LRU بے دخلی روبی کے`Module#prepend`اور`define_method`اس کے لیے مثالی ہیں۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- ریپر بنانے کے لیے`Module.new``define_method` کے ساتھ استعمال کریں۔
- ٹی ٹی ایل کے لیے ٹائم اسٹیمپ کے ساتھ کیشے کو ہیش میں اسٹور کریں۔
- اصل طریقہ سے پہلے کیشنگ پرت داخل کرنے کے لیے`prepend`استعمال کریں۔
- قابل ترتیب اختیارات کی حمایت کریں: `ttl`، `max_size`، `key`۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- تھریڈ سیفٹی:`Mutex`کیشے ریڈز/رائٹس کی حفاظت کرتا ہے۔ حساب کتاب تالے کے باہر ہوتا ہے۔
- ٹی ٹی ایل: میعاد ختم ہونے والی اندراجات کو رسائی پر سستی سے صاف کیا جاتا ہے۔
- LRU بے دخلی: جب کیشے`max_size`سے زیادہ ہو جاتا ہے تو سب سے پرانی اندراج (ٹائم اسٹیمپ کے لحاظ سے) ہٹا دیا جاتا ہے۔
- حسب ضرورت کیز:`key`لیمبڈا کیشے کی شناخت پر عمدہ کنٹرول کی اجازت دیتا ہے۔
- پیداوار: سادہ کیسز کے لیے`memoist`منی کا استعمال کریں، یا تقسیم شدہ کیشنگ کے لیے Redis کی حمایت یافتہ یادداشت کا استعمال کریں۔
---

## خلاصہ
روبی ایک ایسی زبان ہے جو ڈویلپر کی خوشی اور اظہار کو ترجیح دیتی ہے۔ اس کا نحو کسی بھی زبان میں سب سے زیادہ پڑھنے کے قابل ہے، اور Ruby on Rails اب تک بنائے گئے سب سے زیادہ پیداواری ویب فریم ورک میں سے ایک ہے۔ اگرچہ روبی کی مقبولیت میں Python اور JavaScript کے مقابلے میں کمی آئی ہے، لیکن یہ ویب ڈویلپمنٹ، اسکرپٹنگ اور آٹومیشن کے لیے ایک طاقتور، لطف اندوز زبان بنی ہوئی ہے۔ اگر آپ خوبصورت کوڈ اور تیز رفتار ترقی کی قدر کرتے ہیں، تو روبی سیکھنے کے قابل ہے۔