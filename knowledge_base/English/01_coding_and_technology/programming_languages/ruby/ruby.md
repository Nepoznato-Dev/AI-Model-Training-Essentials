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

# Ruby

Ruby is a dynamic, interpreted, object-oriented programming language created by Yukihiro "Matz" Matsumoto and first released in 1995 in Japan. Ruby was designed with a focus on programmer happiness — its syntax is elegant and natural, reading almost like English. Everything in Ruby is an object, including primitive types like integers and booleans. Ruby is best known for the Ruby on Rails web framework, which revolutionised web development by popularising convention over configuration and rapid prototyping.

Beyond Rails, Ruby is used for scripting, automation, DevOps tooling (Chef, Puppet), and as a general-purpose language. Its expressive syntax and powerful metaprogramming capabilities make it a joy to write.

---

## Why Ruby Matters

- **Developer happiness**: Ruby is designed to be readable and enjoyable. "Ruby is designed to make programmers happy" — Matz.
- **Expressive syntax**: Code reads like English. Minimal punctuation, natural phrasing.
- **Ruby on Rails**: One of the most productive web frameworks ever created. Powers GitHub, Shopify, Basecamp, GitLab.
- **Metaprogramming**: Ruby can modify itself at runtime — define methods dynamically, create domain-specific languages (DSLs).
- **Block/iterator pattern**: Ruby's blocks and iterators make collection processing elegant.
- **Everything is an object**: `3.times { puts "hello" }` — integers have methods.

## The Trade-offs

| Limitation | Details | Typical Workaround |
|-----------|---------|-------------------|
| **Performance** | Slower than compiled languages; MRI has a GIL | Use JRuby for parallelism; offload to C extensions |
| **Declining popularity** | Less new adoption compared to Python, Go, Rust | Still widely used; strong in web startups and consulting |
| **Typing** | Dynamic typing can lead to runtime errors | Use Sorbet or RBS for optional static typing |
| **Memory usage** | Higher memory footprint than Go or Rust | Acceptable for most web applications |
| **Job market** | Fewer new positions than Python or JavaScript | Strong in specific niches (Rails shops, consulting) |

---

## Syntax Fundamentals

### Variables and Types

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

### Methods and Blocks

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

### Classes and Modules

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

### Metaprogramming

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

Rails is a full-stack web framework that follows MVC (Model-View-Controller) architecture and emphasises:

- **Convention over Configuration**: Sensible defaults — no need to configure everything.
- **Don't Repeat Yourself (DRY)**: Use generators, migrations, and conventions to minimise repetition.
- **Active Record**: Database objects are Ruby objects. `User.find(1)` retrieves a user.
- **Migrations**: Database schema changes are versioned Ruby code.

Rails powers GitHub, Shopify, Stripe (early), Basecamp, GitLab, and many startups.

---

## Advanced Syntax & Patterns

### Duck Typing and Dynamic Dispatch

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

### Procs, Lambdas, and Closures

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

### Pattern Matching (Ruby 3.0+)

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

### Operator Overloading

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

## Concurrency & Parallelism

### Threads

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

### Fibers — Lightweight Coroutines

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

## Project Configuration & Build System

### Project Structure (Rails)

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

### Gemfile — Dependency Management

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

### Dependency Commands

```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### CI/CD Pipeline (GitHub Actions)

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

## Testing

### RSpec — Testing Framework

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

### Mocking and Stubbing

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

### Test Commands

```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## Interoperability

### C Extensions

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

### FFI — Foreign Function Interface

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

### JRuby — JVM Interoperability

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

## Design Patterns

### Observer Pattern

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

### Factory Pattern

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

### Decorator Pattern

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

## Performance & Optimization

### Profiling Tools

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

### Optimisation Techniques

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

## Deployment

### Puma Web Server

```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### Docker Deployment

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

### Platform Deployment

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

## When to Use Ruby

| Scenario | Why Ruby | Better Alternative |
|----------|---------|-------------------|
| Web applications (Rails) | Rapid development, productive framework | Django (Python), Laravel (PHP), Next.js |
| Prototyping | Very fast to write and iterate | Python, JavaScript |
| Scripting and automation | Elegant syntax, powerful text processing | Python, Shell |
| DevOps tooling (Chef, Puppet) | Established ecosystem | Go, Python |
| CLI tools | Possible but not ideal | Go, Rust |
| Performance-critical systems | Too slow | C, C++, Rust, Go |
| Data science / ML | Not the ecosystem | Python, R |
| Mobile apps | Not suited | Swift, Kotlin, Flutter |

---

## Synthetic Q&A

### Q1: What is the difference between `proc`, `lambda`, and `block` in Ruby?
**A:** All three are closures, but they differ in behavior. A `block` is an anonymous chunk of code passed to a method with `do...end` or `{}`. A `proc` is a block saved as an object — it does not check argument count and `return` exits the enclosing method. A `lambda` is like a proc but checks argument count and `return` exits only the lambda. Use blocks for one-off callbacks, procs for reusable snippets, and lambdas when you need method-like behavior.

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

### Q2: How do Ruby gems and Bundler work?
**A:** Gems are Ruby's package system — reusable libraries distributed via RubyGems.org. A `Gemfile` declares dependencies; `bundle install` resolves versions and creates a `Gemfile.lock` for reproducibility. `bundle exec` runs commands in the gem context. Use `gem 'name', '~> 2.0'` for compatible version constraints. Always commit `Gemfile.lock` for applications, but not for libraries.

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

### Q3: What are Ruby's symbol types, and why are they important?
**A:** Symbols (`:name`) are immutable, interned strings — each unique symbol exists only once in memory. They are ideal for hash keys, method names, and identifiers. Ruby also has `Symbol` objects used extensively in metaprogramming (`send`, `define_method`). Use symbols for fixed identifiers; use strings when you need to manipulate content.

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

### Q4: How does Ruby's metaprogramming work, and when should I use it?
**A:** Ruby allows code to define code at runtime: `define_method` creates methods dynamically, `method_missing` intercepts undefined method calls, `send` calls private methods, and `class_eval`/`instance_eval` evaluate code in a class/instance context. Metaprogramming is powerful but makes code harder to understand — use it for DSLs and framework magic, not for everyday logic.

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

### Q5: What is the best way to handle errors in Ruby?
**A:** Ruby uses exceptions for error handling. Define custom exception classes inheriting from `StandardError` (not `Exception` — that catches system-level errors). Use `begin/rescue/else/ensure` for structured handling. Raise specific exceptions, not generic `RuntimeError`. Use `rescue` as a modifier for simple one-liners.

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

## Chain-of-Thought Problem Solving

### Problem 1: Build a DSL for Configuration Files

**Problem Statement:** Create a Ruby DSL that allows defining server configurations in a readable, declarative syntax. The DSL should support nested blocks, validation, and serialization to JSON.

**Step 1 — Understand the Problem:**
We need: (1) a clean DSL syntax using blocks and method calls, (2) data collection via `instance_eval` or explicit methods, (3) validation of required fields, (4) JSON serialization. Ruby's metaprogramming makes DSLs natural.

**Step 2 — Identify the Approach:**
- Use `instance_eval` with a builder class to capture DSL calls.
- Store configuration in instance variables.
- Validate required fields before serialization.
- Use `to_h` and `JSON.generate` for output.

**Step 3 — Implement the Solution:**

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

**Step 4 — Verify and Optimize:**
- The DSL is readable and declarative — non-programmers can understand it.
- Validation catches missing required fields at construction time.
- `instance_eval` provides the clean block syntax but limits `self` — for more complex DSLs, use `BasicObject` as the builder's superclass.
- Production: consider `dry-configurable` or `configurate` gems for production-grade configuration DSLs.

### Problem 2: Implement a Memoization Library

**Problem Statement:** Build a memoization module that can be mixed into any class to cache method results. Support TTL (time-to-live), cache size limits, and custom cache keys.

**Step 1 — Understand the Problem:**
We need: (1) a module that adds a `memoize` class method, (2) the method wraps target methods with caching logic, (3) support for TTL expiration, (4) LRU eviction when cache is full. Ruby's `Module#prepend` and `define_method` are ideal for this.

**Step 2 — Identify the Approach:**
- Use `Module.new` with `define_method` to create a wrapper.
- Store cache in a hash with timestamps for TTL.
- Use `prepend` to insert the caching layer before the original method.
- Support configurable options: `ttl`, `max_size`, `key`.

**Step 3 — Implement the Solution:**

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

**Step 4 — Verify and Optimize:**
- Thread safety: `Mutex` protects cache reads/writes; computation happens outside the lock.
- TTL: expired entries are lazily cleaned on access.
- LRU eviction: when cache exceeds `max_size`, the oldest entry (by timestamp) is removed.
- Custom keys: the `key` lambda allows fine-grained control over cache identity.
- Production: use the `memoist` gem for simple cases, or Redis-backed memoization for distributed caching.

---

## Summary

Ruby is a language that prioritises developer happiness and expressiveness. Its syntax is among the most readable of any language, and Ruby on Rails remains one of the most productive web frameworks ever created. While Ruby's popularity has declined relative to Python and JavaScript, it remains a powerful, enjoyable language for web development, scripting, and automation. If you value elegant code and rapid development, Ruby is worth learning.