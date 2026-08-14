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

# 紅寶石
Ruby 是一種動態、解釋性、物件導向的程式語言，由 Yukihiro "Matz" Matsumoto 創建，並於 1995 年在日本首次發布。 Ruby 的設計重點是程式設計師的幸福——它的語法優雅而自然，讀起來幾乎像英語一樣。 Ruby 中的一切都是對象，包括整數和布林值等基本類型。 Ruby 因 Ruby on Rails Web 框架而聞名，透過普及約定優於配置和快速原型設計，徹底改變了 Web 開發。
除了 Rails 之外，Ruby 還用於腳本編寫、自動化、DevOps 工具（Chef、Puppet）以及作為通用語言。其富有表現力的語法和強大的元編程功能使其成為一種編寫的樂趣。
---

## 為什麼 Ruby 很重要
- **開發人員的幸福感**：Ruby 被設計為可讀且令人愉悅。 「Ruby 的設計初衷是為了讓程式設計師快樂」—Matz。
- **富有表現力的文法**：程式碼讀起來像英文。標點符號最少，措詞自然。
- **Ruby on Rails**：有史以來最高效的 Web 框架之一。為 GitHub、Shopify、Basecamp、GitLab 提供支援。
- **元程式設計**：Ruby 可以在執行時修改自身 - 動態定義方法，建立特定於領域的語言 (DSL)。
- **區塊/迭代器模式**：Ruby 的區塊和迭代器使集合處理變得優雅。
- **一切都是物件**：`3.times { puts "hello" }` — 整數有方法。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **效能** |比編譯語言慢； MRI 有 GIL |使用 JRuby 實作並行性；卸載到 C 擴充 |
| **人氣下降** |與 Python、Go、Rust 相比，新採用者較少 |仍被廣泛使用；擅長網絡創業和諮詢|
| **打字** |動態類型可能導致運行時錯誤 |使用 Sorbet 或 RBS 進行可選的靜態類型 |
| **記憶體使用情況** |比 Go 或 Rust 更高的記憶體佔用 |適合大多數 Web 應用程式 |
| **就業市場** |新職位比 Python 或 JavaScript 少 |擅長特定領域（Rails 商店、顧問）|
---

## 文法基礎知識
### 變數和類型
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

### 方法和區塊
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

### 類別和模組
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

### 元編程
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

## Ruby on Rails
Rails 是一個全端 Web 框架，遵循 MVC（模型-視圖-控制器）架構並強調：
- **約定優於配置**：合理的預設值 - 無需配置所有內容。
- **不要重複自己（DRY）**：使用生成器、遷移和約定來最大程度地減少重複。
- **Active Record**：資料庫物件是 Ruby 物件。 `User.find(1)`檢索使用者。
- **遷移**：資料庫架構變更是版本化的 Ruby 程式碼。
Rails 為 GitHub、Shopify、Stripe（早期）、Basecamp、GitLab 和許多新創公司提供支援。
---

## 進階語法和模式
### 鴨子打字和動態調度
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

### 流程、Lambda 和閉包
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

### 模式匹配 (Ruby 3.0+)
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

### 運算子重載
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

## 並發與平行
### 話題
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

### Fibers — 輕量級協程
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

### 使用 Async Gem 進行非同步/等待
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

## 專案配置與建置系統
### 專案結構（Rails）
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

### Gemfile — 依賴管理
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

### 依賴指令
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### CI/CD 管道 (GitHub Actions)
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

## 測試
### RSpec — 測試框架
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

### 模擬與存根
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

### 測試命令
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## 互通性
### C 擴充
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

### FFI — 外部函數介面
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

### JRuby — JVM 互通性
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

## 設計模式
### 觀察者模式
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

### 工廠模式
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

### 裝飾器模式
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

## 效能與最佳化
### 分析工具
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

### 優化技術
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

## 部署
### Puma 網路伺服器
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### Docker 部署
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

### 平台部署
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

## 何時使用 Ruby
|場景|為什麼選擇紅寶石？更好的選擇|
|----------|---------|--------------------|
| Web 應用程式（Rails）|快速開發、高效的框架 | Django (Python)、Laravel (PHP)、Next.js |
|原型製作 |編寫和迭代速度非常快 | Python、JavaScript |
|腳本編寫與自動化|優雅的語法，強大的文字處理 | Python、Shell |
| DevOps 工具（Chef、Puppet） |已建立的生態系 |去吧，Python |
| CLI 工具 |可能但不理想 |去吧，魯斯特 |
|效能關鍵型系統 |太慢了 | C、C++、Rust、Go |
|資料科學/機器學習 |不是生態系| Python、R |
|手機應用程式 |不適合|斯威夫特、科特林、顫振 |
---

## 綜合問答
### Q1：Ruby 中的`proc`、`lambda`和`block`有什麼不同？
**A：** 這三個都是閉包，但它們的行為有所不同。`block`是傳遞給具有`do...end`或`{}`的方法的匿名程式碼區塊。`proc`是保存為物件的區塊 - 它不檢查參數計數，並且`return`退出封閉方法。`lambda`就像一個過程，但檢查參數計數，而`return`僅退出 lambda。當您需要類似方法的行為時，請使用區塊進行一次性回調，使用過程進行可重複使用的片段，並使用 lambda。
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

### Q2：Ruby gems 和 Bundler 如何運作？
**答：** Gems 是 Ruby 的軟體包系統 — 透過 RubyGems.org 分發的可重複使用函式庫。`Gemfile`宣告依賴關係；`bundle install`解析版本並建立`Gemfile.lock`以實現可重複性。 `bundle exec`在 gem 上下文中執行命令。使用`gem 'name', '~> 2.0'`進行相容版本約束。始終為應用程式提交 `Gemfile.lock`，但不為庫提交 `Gemfile.lock`。
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

### Q3：Ruby 的符號類型是什麼，為什麼它們很重要？
**A:** 符號 (`:name`) 是不可變的、內部字串 - 每個唯一的符號在記憶體中僅存在一次。它們非常適合哈希鍵、方法名稱和標識符。 Ruby 也具有廣泛用於元程式設計的`Symbol`物件（`send`、`define_method`）。使用符號作為固定標識符；當您需要操作內容時使用字串。
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

### Q4：Ruby 的元程式設計是如何運作的，什麼時候該使用它？
**答：** Ruby 允許程式碼在執行時間定義程式碼：`define_method` 動態建立方法，`method_missing` 封鎖未定義的方法調用，`send` 呼叫私有方法，`class_eval` /`instance_eval`在類別/實例上下文中評估程式碼。元程式設計很強大，但使程式碼更難理解——將其用於 DSL 和框架魔法，而不是日常邏輯。
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

### Q5：在 Ruby 中處理錯誤的最佳方法是什麼？
**答：** Ruby 使用異常進行錯誤處理。定義繼承自`StandardError`的自訂異常類別（不是`Exception`— 擷取系統層級錯誤）。使用`begin/rescue/else/ensure`進行結構化處理。引發特定異常，而不是通用`RuntimeError`。使用`rescue`作為簡單單行的修飾符。
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

## 解決問題的思路
### 問題 1：為設定檔建構 DSL
**問題陳述：** 建立一個 Ruby DSL，允許以可讀的聲明性語法定義伺服器配置。 DSL 應支援巢狀區塊、驗證和序列化為 JSON。
**第 1 步 — 了解問題：**
我們需要：(1) 使用區塊和方法呼叫的乾淨 DSL 語法，(2) 透過`instance_eval`或顯式方法收集數據，(3) 驗證所需字段，(4) JSON 序列化。 Ruby 的元編程使 DSL 變得自然。
**第 2 步 — 確定方法：**
- 將`instance_eval`與建構器類別一起使用來擷取 DSL 通話。
- 將組態儲存在實例變數中。
- 在序列化之前驗證必填欄位。
- 使用`to_h`和`JSON.generate`進行輸出。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- DSL 具有可讀性和聲明性——非程式設計師也能理解。
- 驗證建置時發現缺少的必填欄位。
-`instance_eval`提供乾淨的區塊語法，但限制`self`— 對於更複雜的 DSL，請使用`BasicObject`作為建構器的超類別。
- 生產：考慮使用`dry-configurable`或`configurate`gems 作為生產級配置 DSL。
### 問題 2：實現記憶庫
**問題陳述：** 建立一個記憶模組，可以將其混合到任何類別中以緩存方法結果。支援 TTL（生存時間）、快取大小限制和自訂快取鍵。
**第 1 步 — 了解問題：**
我們需要：（1）一個新增`memoize`類別方法的模組，（2）該方法用快取邏輯包裝目標方法，（3）支援 TTL 過期，（4）快取已滿時 LRU 驅逐。 Ruby 的`Module#prepend`和`define_method`非常適合此目的。
**第 2 步 — 確定方法：**
- 使用`Module.new`和`define_method`建立包裝器。
- 將快取儲存在帶有 TTL 時間戳記的雜湊中。
- 使用`prepend`在原始方法之前插入快取層。
- 支援可設定選項：`ttl`、`max_size`、`key`。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 執行緒安全性：`Mutex`保護快取讀/寫；計算發生在鎖定之外。
- TTL：過期條目在存取時被延遲清除。
- LRU 驅逐：當快取超過`max_size`時，最舊的條目（按時間戳記）將被刪除。
- 自訂鍵：`key` lambda 允許對快取標識進行細粒度控制。
- 生產：對於簡單情況使用`memoist`gem，或使用 Redis 支援的記憶體進行分散式快取。
---

＃＃ 概括
Ruby 是一種優先考慮開發人員的快樂和表現力的語言。它的語法是所有語言中最具可讀性的，而 Ruby on Rails 仍然是有史以來最高效的 Web 框架之一。雖然 Ruby 的受歡迎程度相對於 Python 和 JavaScript 有所下降，但它仍然是一種強大且令人愉悅的 Web 開發、腳本和自動化語言。如果你重視優雅的程式碼​​和快速的開發，Ruby值得學習。