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

## Summary

Ruby is a language that prioritises developer happiness and expressiveness. Its syntax is among the most readable of any language, and Ruby on Rails remains one of the most productive web frameworks ever created. While Ruby's popularity has declined relative to Python and JavaScript, it remains a powerful, enjoyable language for web development, scripting, and automation. If you value elegant code and rapid development, Ruby is worth learning.