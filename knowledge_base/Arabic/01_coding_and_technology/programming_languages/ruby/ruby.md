---
# البيانات الوصفية
العنوان: "روبي"
الوصف: "مرجع شامل للغة برمجة روبي يغطي النظرة العامة والمقايضات وأساسيات بناء الجملة والنظام البيئي ومتى يتم استخدامها."
الفئة: "البرمجة والتكنولوجيا"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
تمت المراجعة بواسطة: "فريق قاعدة معارف البرمجة والتكنولوجيا"
next_review: "2027-08-05"
# التصنيف
العلامات: [روبي، لغة البرمجة، بناء الجملة، النظام البيئي، الترميز والتكنولوجيا]
مستوى الصعوبة: "متوسط"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "34 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
#روبي
روبي هي لغة برمجة ديناميكية ومفسرة وموجهة نحو الكائنات أنشأها يوكيهيرو "ماتز" ماتسوموتو وتم إصدارها لأول مرة في عام 1995 في اليابان. تم تصميم روبي مع التركيز على سعادة المبرمجين، حيث أن بناء الجملة الخاص بها أنيق وطبيعي، وقراءته تشبه اللغة الإنجليزية تقريبًا. كل شيء في روبي هو كائن، بما في ذلك الأنواع البدائية مثل الأعداد الصحيحة والقيم المنطقية. تشتهر روبي بإطار عمل الويب Ruby on Rails، الذي أحدث ثورة في تطوير الويب من خلال تعميم التقليد على التكوين والنماذج الأولية السريعة.
بعيدًا عن Rails، تُستخدم لغة Ruby في البرمجة النصية والأتمتة وأدوات DevOps (Chef وPuppet) وكلغة للأغراض العامة. إن تركيبها التعبيري وقدرات البرمجة الفوقية القوية تجعل الكتابة ممتعة.
---

## لماذا تعتبر روبي مهمة؟
- **سعادة المطورين**: تم تصميم روبي لتكون سهلة القراءة وممتعة. "تم تصميم روبي لجعل المبرمجين سعداء" - ماتز.
- **بناء الجملة التعبيري**: يُقرأ الكود مثل اللغة الإنجليزية. الحد الأدنى من علامات الترقيم، والصياغة الطبيعية.
- **Ruby on Rails**: أحد أطر عمل الويب الأكثر إنتاجية على الإطلاق. القوى جيثب، Shopify، Basecamp، GitLab.
- **البرمجة الوصفية**: يمكن لروبي تعديل نفسه في وقت التشغيل — تحديد الأساليب ديناميكيًا، وإنشاء لغات خاصة بالمجال (DSLs).
- **نمط الكتلة/المكرر**: كتل روبي ومكرراته تجعل معالجة المجموعة أنيقة.
- **كل شيء هو كائن**: __محمي_0__ — للأعداد الصحيحة طرق.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **الأداء** | أبطأ من اللغات المترجمة؛ التصوير بالرنين المغناطيسي لديه GIL | استخدم JRuby للتوازي؛ تفريغ إلى ملحقات C |
| **شعبية متراجعة** | اعتماد جديد أقل مقارنة بـ Python، Go، Rust | لا تزال تستخدم على نطاق واسع. قوية في الشركات الناشئة على شبكة الإنترنت والاستشارات |
| ** الكتابة ** | يمكن أن تؤدي الكتابة الديناميكية إلى أخطاء وقت التشغيل | استخدم Sorbet أو RBS للكتابة الثابتة الاختيارية |
| **استخدام الذاكرة** | مساحة ذاكرة أعلى من Go أو Rust | مقبول لمعظم تطبيقات الويب |
| **سوق العمل** | مواضع جديدة أقل من Python أو JavaScript | قوي في مجالات محددة (محلات ريلز، استشارات) |
---

## أساسيات بناء الجملة
### المتغيرات والأنواع
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

### الطرق والكتل
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

### الفئات والوحدات
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

### البرمجة الفوقية
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

## روبي أون ريلز
Rails عبارة عن إطار عمل ويب متكامل يتبع بنية MVC (Model-View-Controller) ويركز على:
- **الاتفاقية حول التكوين**: الإعدادات الافتراضية المعقولة - لا حاجة لتهيئة كل شيء.
- **لا تكرر نفسك (جاف)**: استخدم المولدات وعمليات الترحيل والاصطلاحات لتقليل التكرار.
- **السجل النشط**: كائنات قاعدة البيانات هي كائنات روبي. `User.find(1)`يسترد مستخدمًا.
- **الهجرات**: تغييرات مخطط قاعدة البيانات هي نسخة كود روبي.
تعمل Rails على تشغيل GitHub وShopify وStripe (مبكرًا) وBascamp وGitLab والعديد من الشركات الناشئة.
---

## بناء الجملة والأنماط المتقدمة
### كتابة البطة والإرسال الديناميكي
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

### العمليات، واللامدا، والإغلاقات
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

### مطابقة الأنماط (روبي 3.0+)
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

### التحميل الزائد على المشغل
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

## التزامن والتوازي
### المواضيع
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

### ألياف — كوروتينات خفيفة الوزن
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

### غير متزامن/انتظر مع Async Gem
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

## تكوين المشروع ونظام البناء
### هيكل المشروع (القضبان)
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

### Gemfile — إدارة التبعية
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

### أوامر التبعية
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### خط أنابيب CI/CD (إجراءات GitHub)
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

## الاختبار
### RSpec — إطار عمل الاختبار
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

### السخرية والطعن
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

### أوامر الاختبار
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## إمكانية التشغيل البيني
### ملحقات C
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

### FFI — واجهة الوظائف الأجنبية
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

### JRuby — قابلية التشغيل البيني لـ JVM
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

## أنماط التصميم
### نمط المراقب
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

### نمط المصنع
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

### نمط الديكور
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

## الأداء والتحسين
### أدوات التنميط
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

### تقنيات التحسين
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

## النشر
### خادم الويب بوما
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### نشر عامل الميناء
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

### نشر النظام الأساسي
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

## متى تستخدم روبي
| السيناريو | لماذا روبي | البديل الأفضل |
|----------|--------|------------------|
| تطبيقات الويب (ريلز) | تطور سريع وإطار إنتاجي | جانغو (بايثون)، لارافيل (PHP)، Next.js |
| النماذج الأولية | سريع جدًا في الكتابة والتكرار | بايثون، جافا سكريبت |
| البرمجة النصية والأتمتة | بناء جملة أنيق، معالجة نصوص قوية | بايثون، شل |
| أدوات DevOps (الشيف، الدمية) | النظام البيئي المؤسس | اذهب يا بايثون |
| أدوات سطر الأوامر | ممكن ولكن ليس مثاليا | اذهب يا صدأ |
| أنظمة الأداء الحرجة | بطيء جدًا | C، C++، الصدأ، الذهاب |
| علم البيانات / تعلم الآلة | ليس النظام البيئي | بايثون، ر |
| تطبيقات الجوال | غير مناسب | سويفت، كوتلين، رفرفة |
---

## ملخص
روبي هي لغة تعطي الأولوية لسعادة المطورين وتعبيرهم. يعد بناء جملتها من بين أكثر اللغات قابلية للقراءة، ويظل Ruby on Rails أحد أكثر أطر الويب إنتاجية على الإطلاق. على الرغم من انخفاض شعبية روبي مقارنة ببايثون وجافا سكريبت، إلا أنها تظل لغة قوية وممتعة لتطوير الويب والبرمجة النصية والأتمتة. إذا كنت تقدر الكود الأنيق والتطور السريع، فإن روبي تستحق التعلم.