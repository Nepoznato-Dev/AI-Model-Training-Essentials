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

#রুবি
রুবি হল একটি গতিশীল, ব্যাখ্যা করা, অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং ভাষা ইউকিহিরো "ম্যাটজ" মাতসুমোটো দ্বারা তৈরি এবং প্রথমবার 1995 সালে জাপানে প্রকাশিত হয়েছিল। রুবি প্রোগ্রামার সুখের উপর ফোকাস দিয়ে ডিজাইন করা হয়েছিল — এর সিনট্যাক্স মার্জিত এবং স্বাভাবিক, প্রায় ইংরেজির মতো পড়া। পূর্ণসংখ্যা এবং বুলিয়ানের মতো আদিম প্রকারগুলি সহ রুবিতে সবকিছুই একটি বস্তু। রুবি রুবি অন রেল ওয়েব ফ্রেমওয়ার্কের জন্য সবচেয়ে বেশি পরিচিত, যা কনফিগারেশন এবং দ্রুত প্রোটোটাইপিংয়ের মাধ্যমে কনভেনশন জনপ্রিয় করে ওয়েব ডেভেলপমেন্টে বিপ্লব ঘটিয়েছে।
রেলের বাইরে, রুবি স্ক্রিপ্টিং, অটোমেশন, DevOps টুলিং (শেফ, পাপেট) এবং একটি সাধারণ-উদ্দেশ্য ভাষা হিসাবে ব্যবহৃত হয়। এর অভিব্যক্তিপূর্ণ সিনট্যাক্স এবং শক্তিশালী মেটাপ্রোগ্রামিং ক্ষমতা এটি লিখতে আনন্দ দেয়।
---

## কেন রুবি ব্যাপার
- **বিকাশকারী সুখ**: রুবিকে পঠনযোগ্য এবং উপভোগ্য করার জন্য ডিজাইন করা হয়েছে। "রুবি প্রোগ্রামারদের খুশি করার জন্য ডিজাইন করা হয়েছে" - ম্যাটজ।
- **অব্যক্ত বাক্য গঠন**: কোড ইংরেজির মত পড়ে। ন্যূনতম যতিচিহ্ন, স্বাভাবিক বাক্যাংশ।
- **Ruby on Rails**: এখন পর্যন্ত তৈরি করা সবচেয়ে উৎপাদনশীল ওয়েব ফ্রেমওয়ার্কগুলির মধ্যে একটি। GitHub, Shopify, Basecamp, GitLab পাওয়ার।
- **মেটাপ্রোগ্রামিং**: রুবি রানটাইমে নিজেকে পরিবর্তন করতে পারে — গতিশীলভাবে পদ্ধতিগুলি সংজ্ঞায়িত করতে পারে, ডোমেন-নির্দিষ্ট ভাষা (ডিএসএল) তৈরি করে।
- **ব্লক/ইটারেটর প্যাটার্ন**: রুবির ব্লক এবং ইটারেটর সংগ্রহ প্রক্রিয়াকরণকে মার্জিত করে তোলে।
- **সবকিছুই একটি বস্তু**:`3.times { puts "hello" }`— পূর্ণসংখ্যার পদ্ধতি আছে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **পারফরম্যান্স** | সংকলিত ভাষার চেয়ে ধীর; MRI এর একটি GIL আছে | সমান্তরালতার জন্য JRuby ব্যবহার করুন; সি এক্সটেনশনে অফলোড |
| ** জনপ্রিয়তা কমছে** | পাইথন, গো, রাস্টের তুলনায় কম নতুন গ্রহণ | এখনও ব্যাপকভাবে ব্যবহৃত; ওয়েব স্টার্টআপ এবং পরামর্শে শক্তিশালী |
| **টাইপিং** | গতিশীল টাইপিং রানটাইম ত্রুটির কারণ হতে পারে | ঐচ্ছিক স্ট্যাটিক টাইপিংয়ের জন্য শরবত বা আরবিএস ব্যবহার করুন |
| **মেমরি ব্যবহার** | গো বা মরিচা থেকে উচ্চ মেমরি পদচিহ্ন | বেশিরভাগ ওয়েব অ্যাপ্লিকেশনের জন্য গ্রহণযোগ্য |
| **চাকরীর বাজার** | পাইথন বা জাভাস্ক্রিপ্টের চেয়ে কম নতুন অবস্থান | নির্দিষ্ট কুলুঙ্গিতে শক্তিশালী (রেল দোকান, পরামর্শ) |
---

## সিনট্যাক্স মৌলিক
### ভেরিয়েবল এবং প্রকার
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

### পদ্ধতি এবং ব্লক
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

### ক্লাস এবং মডিউল
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

### মেটাপ্রোগ্রামিং
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

## রুবি অন রেল
রেল হল একটি পূর্ণ-স্ট্যাক ওয়েব ফ্রেমওয়ার্ক যা MVC (মডেল-ভিউ-কন্ট্রোলার) আর্কিটেকচার এবং জোর দেয়:
- **কনভেনশন ওভার কনফিগারেশন**: সংবেদনশীল ডিফল্ট — সবকিছু কনফিগার করার দরকার নেই।
- **নিজেকে পুনরাবৃত্তি করবেন না (ড্রাই)**: পুনরাবৃত্তি কমাতে জেনারেটর, মাইগ্রেশন এবং কনভেনশন ব্যবহার করুন।
- **অ্যাকটিভ রেকর্ড**: ডাটাবেস অবজেক্ট হল রুবি অবজেক্ট। `User.find(1)`একজন ব্যবহারকারীকে পুনরুদ্ধার করে।
- **মাইগ্রেশন**: ডাটাবেস স্কিমা পরিবর্তন রুবি কোড সংস্করণ।
রেল GitHub, Shopify, স্ট্রাইপ (প্রথম দিকে), বেসক্যাম্প, গিটল্যাব এবং অনেকগুলি স্টার্টআপকে ক্ষমতা দেয়।
---

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### হাঁস টাইপিং এবং ডাইনামিক ডিসপ্যাচ
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

### প্রক্স, ল্যাম্বডাস এবং ক্লোজার
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

### প্যাটার্ন ম্যাচিং (রুবি 3.0+)
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

### অপারেটর ওভারলোডিং
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

## সামঞ্জস্য এবং সমান্তরালতা
### থ্রেড
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

### ফাইবারস — লাইটওয়েট কোরোটিন
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

### Async/অ্যাসিঙ্ক জেমের সাথে অপেক্ষা করুন
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো (রেল)
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

### জেমফাইল — নির্ভরতা ব্যবস্থাপনা
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

### নির্ভরতা কমান্ড
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
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

## পরীক্ষা
### RSpec — টেস্টিং ফ্রেমওয়ার্ক
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

### উপহাস এবং স্টাবিং
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

### টেস্ট কমান্ড
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## ইন্টারঅপারেবিলিটি
### সি এক্সটেনশন
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

### FFI — বিদেশী ফাংশন ইন্টারফেস
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

### JRuby — JVM ইন্টারঅপারেবিলিটি
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

## ডিজাইন প্যাটার্ন
### পর্যবেক্ষক প্যাটার্ন
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

### কারখানার প্যাটার্ন
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

### ডেকোরেটর প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
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

### অপ্টিমাইজেশন কৌশল
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

## স্থাপনা
### পুমা ওয়েব সার্ভার
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### ডকার স্থাপনা
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

### প্ল্যাটফর্ম স্থাপনা
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

## কখন রুবি ব্যবহার করবেন
| দৃশ্যকল্প | কেন রুবি | ভাল বিকল্প |
|------------|---------|---------|
| ওয়েব অ্যাপ্লিকেশন (রেল) | দ্রুত উন্নয়ন, উৎপাদনশীল কাঠামো | জ্যাঙ্গো (পাইথন), লারাভেল (পিএইচপি), Next.js |
| প্রোটোটাইপিং | লিখতে এবং পুনরাবৃত্তি করতে খুব দ্রুত | পাইথন, জাভাস্ক্রিপ্ট |
| স্ক্রিপ্টিং এবং অটোমেশন | মার্জিত বাক্য গঠন, শক্তিশালী পাঠ্য প্রক্রিয়াকরণ | পাইথন, শেল |
| DevOps টুলিং (শেফ, পুতুল) | প্রতিষ্ঠিত ইকোসিস্টেম | যান, পাইথন |
| CLI টুলস | সম্ভব কিন্তু আদর্শ নয় | যাও, মরিচা |
| কর্মক্ষমতা-সমালোচনামূলক সিস্টেম | খুব ধীর | C, C++, Rust, Go |
| ডেটা সায়েন্স / এমএল | বাস্তুতন্ত্র নয় | পাইথন, আর |
| মোবাইল অ্যাপস | উপযুক্ত নয় | সুইফট, কোটলিন, ফ্লাটার |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: রুবিতে `proc`,`lambda`এবং`block`এর মধ্যে পার্থক্য কী?
**A:** তিনটিই বন্ধ, কিন্তু তারা আচরণে ভিন্ন। একটি`block`হল`do...end`বা`{}`সহ একটি পদ্ধতিতে পাস করা কোডের একটি বেনামী অংশ। একটি`proc`হল একটি অবজেক্ট হিসাবে সংরক্ষিত একটি ব্লক — এটি আর্গুমেন্ট কাউন্ট চেক করে না এবং`return`এনক্লোজিং পদ্ধতি থেকে প্রস্থান করে। একটি`lambda`হল একটি proc এর মত কিন্তু আর্গুমেন্ট কাউন্ট চেক করে এবং`return`শুধুমাত্র ল্যাম্বডা থেকে প্রস্থান করে। এক-অফ কলব্যাকের জন্য ব্লক, পুনঃব্যবহারযোগ্য স্নিপেটগুলির জন্য প্রোকস এবং ল্যাম্বডাস ব্যবহার করুন যখন আপনার পদ্ধতির মতো আচরণের প্রয়োজন হয়।
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

### প্রশ্ন 2: রুবি রত্ন এবং বান্ডলার কিভাবে কাজ করে?
**A:** রত্ন হল রুবির প্যাকেজ সিস্টেম — RubyGems.org এর মাধ্যমে পুনরায় ব্যবহারযোগ্য লাইব্রেরি বিতরণ করা হয়। একটি`Gemfile`নির্ভরতা ঘোষণা করে; `bundle install`সংস্করণগুলি সমাধান করে এবং প্রজননযোগ্যতার জন্য একটি`Gemfile.lock`তৈরি করে৷ `bundle exec`রত্ন প্রসঙ্গে কমান্ড চালায়। সামঞ্জস্যপূর্ণ সংস্করণ সীমাবদ্ধতার জন্য`gem 'name', '~> 2.0'`ব্যবহার করুন। অ্যাপ্লিকেশনের জন্য সর্বদা`Gemfile.lock`কমিট করুন, কিন্তু লাইব্রেরির জন্য নয়।
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

### প্রশ্ন 3: রুবির প্রতীকের ধরন কী এবং কেন তারা গুরুত্বপূর্ণ?
**A:** প্রতীকগুলি (`:name`) অপরিবর্তনীয়, অন্তর্নিহিত স্ট্রিং — প্রতিটি অনন্য প্রতীক শুধুমাত্র একবার মেমরিতে বিদ্যমান থাকে। তারা হ্যাশ কী, পদ্ধতির নাম এবং শনাক্তকারীর জন্য আদর্শ। রুবির কাছে`Symbol`বস্তুও রয়েছে যা মেটাপ্রোগ্রামিং-এ ব্যাপকভাবে ব্যবহৃত হয় (`send`,`define_method`)। স্থির শনাক্তকারীর জন্য প্রতীক ব্যবহার করুন; আপনি যখন বিষয়বস্তু ম্যানিপুলেট করতে হবে তখন স্ট্রিং ব্যবহার করুন।
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

### প্রশ্ন 4: রুবির মেটাপ্রোগ্রামিং কিভাবে কাজ করে এবং আমি কখন এটি ব্যবহার করব?
**A:** রুবি কোডকে রানটাইমে কোড সংজ্ঞায়িত করার অনুমতি দেয়:`define_method`গতিশীলভাবে পদ্ধতি তৈরি করে,`method_missing`অনির্ধারিত পদ্ধতির কলগুলিকে বাধা দেয়,`send`ব্যক্তিগত পদ্ধতিগুলিকে কল করে এবং`class_eval`/`instance_eval`ক্লাশে প্রেক্ষাপটে কোড করে৷ মেটাপ্রোগ্রামিং শক্তিশালী কিন্তু কোড বোঝা কঠিন করে তোলে — এটি ডিএসএল এবং ফ্রেমওয়ার্ক ম্যাজিকের জন্য ব্যবহার করুন, দৈনন্দিন যুক্তির জন্য নয়।
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

### প্রশ্ন 5: রুবিতে ত্রুটিগুলি পরিচালনা করার সর্বোত্তম উপায় কী?
**A:** রুবি ত্রুটি পরিচালনার জন্য ব্যতিক্রম ব্যবহার করে।`StandardError`(`Exception` নয় — যা সিস্টেম-স্তরের ত্রুটিগুলি ধরে) থেকে উত্তরাধিকারসূত্রে পাওয়া কাস্টম ব্যতিক্রম ক্লাসগুলিকে সংজ্ঞায়িত করুন৷ কাঠামোগত পরিচালনার জন্য`begin/rescue/else/ensure`ব্যবহার করুন। নির্দিষ্ট ব্যতিক্রমগুলি উত্থাপন করুন, সাধারণ`RuntimeError`নয়।`rescue`সাধারণ ওয়ান-লাইনারগুলির জন্য একটি সংশোধক হিসাবে ব্যবহার করুন৷
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: কনফিগারেশন ফাইলের জন্য একটি DSL তৈরি করুন
**সমস্যা বিবৃতি:** একটি রুবি ডিএসএল তৈরি করুন যা একটি পাঠযোগ্য, ঘোষণামূলক সিনট্যাক্সে সার্ভার কনফিগারেশন সংজ্ঞায়িত করার অনুমতি দেয়। DSL-এর উচিত JSON-এ নেস্টেড ব্লক, যাচাইকরণ এবং সিরিয়ালাইজেশন সমর্থন করা।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) ব্লক এবং মেথড কল ব্যবহার করে একটি পরিষ্কার ডিএসএল সিনট্যাক্স, (2)`instance_eval`বা স্পষ্ট পদ্ধতির মাধ্যমে ডেটা সংগ্রহ, (3) প্রয়োজনীয় ক্ষেত্রগুলির বৈধতা, (4) JSON সিরিয়ালাইজেশন। রুবির মেটাপ্রোগ্রামিং ডিএসএলকে প্রাকৃতিক করে তোলে।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- DSL কলগুলি ক্যাপচার করতে একটি নির্মাতা শ্রেণীর সাথে`instance_eval`ব্যবহার করুন৷
- ইনস্ট্যান্স ভেরিয়েবলে কনফিগারেশন সংরক্ষণ করুন।
- সিরিয়ালাইজেশনের আগে প্রয়োজনীয় ক্ষেত্রগুলি যাচাই করুন।
- আউটপুটের জন্য`to_h`এবং`JSON.generate`ব্যবহার করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- ডিএসএল পঠনযোগ্য এবং ঘোষণামূলক — নন-প্রোগ্রামাররা এটি বুঝতে পারে।
- বৈধকরণ নির্মাণের সময় প্রয়োজনীয় ক্ষেত্র অনুপস্থিত ধরা পড়ে।
-`instance_eval`পরিষ্কার ব্লক সিনট্যাক্স প্রদান করে কিন্তু`self`সীমাবদ্ধ করে — আরও জটিল DSL-এর জন্য, নির্মাতার সুপারক্লাস হিসাবে`BasicObject`ব্যবহার করুন।
- উৎপাদন: উৎপাদন-গ্রেড কনফিগারেশন DSL-এর জন্য`dry-configurable`বা`configurate`রত্ন বিবেচনা করুন৷
### সমস্যা 2: একটি মেমোাইজেশন লাইব্রেরি বাস্তবায়ন করুন
**সমস্যা বিবৃতি:** একটি মেমোাইজেশন মডিউল তৈরি করুন যা ক্যাশে পদ্ধতির ফলাফলের জন্য যেকোনো ক্লাসে মিশ্রিত করা যেতে পারে। TTL (টাইম-টু-লাইভ), ক্যাশ সাইজ লিমিট এবং কাস্টম ক্যাশে কী সমর্থন করে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) একটি মডিউল যা একটি`memoize`ক্লাস পদ্ধতি যোগ করে, (2) পদ্ধতিটি ক্যাশিং লজিক সহ লক্ষ্য পদ্ধতিগুলিকে মোড়ানো, (3) TTL মেয়াদ শেষ হওয়ার জন্য সমর্থন, (4) ক্যাশে পূর্ণ হলে LRU উচ্ছেদ৷ রুবির`Module#prepend`এবং`define_method`এর জন্য আদর্শ।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- একটি মোড়ক তৈরি করতে`define_method`এর সাথে`Module.new`ব্যবহার করুন।
- TTL এর জন্য টাইমস্ট্যাম্প সহ একটি হ্যাশে ক্যাশে সংরক্ষণ করুন।
- মূল পদ্ধতির আগে ক্যাশিং স্তর সন্নিবেশ করতে`prepend`ব্যবহার করুন।
- কনফিগারযোগ্য বিকল্পগুলি সমর্থন করুন: `ttl`, `max_size`, `key`।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- থ্রেড নিরাপত্তা:`Mutex`ক্যাশে রিডস/রাইট সুরক্ষা করে; গণনা তালার বাইরে ঘটে।
- TTL: মেয়াদোত্তীর্ণ এন্ট্রিগুলি অ্যাক্সেসের সময় অলসভাবে পরিষ্কার করা হয়।
- LRU উচ্ছেদ: যখন ক্যাশে`max_size`ছাড়িয়ে যায়, প্রাচীনতম এন্ট্রি (টাইমস্ট্যাম্প দ্বারা) সরানো হয়৷
- কাস্টম কী:`key`ল্যাম্বডা ক্যাশে পরিচয়ের উপর সূক্ষ্ম-দানাযুক্ত নিয়ন্ত্রণের অনুমতি দেয়।
- উত্পাদন: সাধারণ ক্ষেত্রে`memoist`রত্ন ব্যবহার করুন, অথবা বিতরণ করা ক্যাশিংয়ের জন্য Redis-ব্যাকড মেমোাইজেশন ব্যবহার করুন।
---

## সারাংশ
রুবি এমন একটি ভাষা যা বিকাশকারীর সুখ এবং অভিব্যক্তিকে অগ্রাধিকার দেয়। এর সিনট্যাক্স যেকোন ভাষার মধ্যে সবচেয়ে বেশি পঠনযোগ্য, এবং রুবি অন রেল এখন পর্যন্ত তৈরি করা সবচেয়ে উত্পাদনশীল ওয়েব ফ্রেমওয়ার্কগুলির মধ্যে একটি। যদিও রুবির জনপ্রিয়তা পাইথন এবং জাভাস্ক্রিপ্টের তুলনায় হ্রাস পেয়েছে, এটি ওয়েব ডেভেলপমেন্ট, স্ক্রিপ্টিং এবং অটোমেশনের জন্য একটি শক্তিশালী, উপভোগ্য ভাষা হিসাবে রয়ে গেছে। আপনি যদি মার্জিত কোড এবং দ্রুত বিকাশকে মূল্য দেন তবে রুবি শেখার যোগ্য।