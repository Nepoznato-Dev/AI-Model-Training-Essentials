<!--
---
# Metadata
title: "Ruby"
description: "Comprehensive reference for the Ruby programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
# 루비
Ruby는 Yukihiro "Matz" Matsumoto가 개발하고 1995년 일본에서 처음 출시된 동적 해석형 객체 지향 프로그래밍 언어입니다. Ruby는 프로그래머의 행복에 초점을 맞춰 설계되었습니다. Ruby의 구문은 우아하고 자연스러우며 읽기가 거의 영어와 같습니다. 정수 및 부울과 같은 기본 유형을 포함하여 Ruby의 모든 것은 객체입니다. Ruby는 구성에 대한 관례와 신속한 프로토타이핑을 대중화하여 웹 개발에 혁명을 일으킨 Ruby on Rails 웹 프레임워크로 가장 잘 알려져 있습니다.
Beyond Rails에서 Ruby는 스크립팅, 자동화, DevOps 도구(Chef, Puppet) 및 범용 언어로 사용됩니다. 표현력이 풍부한 구문과 강력한 메타프로그래밍 기능 덕분에 글쓰기가 즐겁습니다.
---

## 루비가 중요한 이유
- **개발자의 행복**: Ruby는 읽기 쉽고 즐겁게 설계되었습니다. "Ruby는 프로그래머를 행복하게 만들기 위해 설계되었습니다." — Matz.
- **표현적 구문**: 코드가 영어처럼 읽힙니다. 구두점을 최소화하고 자연스러운 표현을 사용합니다.
- **Ruby on Rails**: 지금까지 만들어진 웹 프레임워크 중 가장 생산적인 웹 프레임워크 중 하나입니다. GitHub, Shopify, Basecamp, GitLab을 지원합니다.
- **메타프로그래밍**: Ruby는 런타임에 자체적으로 수정할 수 있습니다. 즉, 메서드를 동적으로 정의하고 도메인별 언어(DSL)를 생성할 수 있습니다.
- **블록/반복자 패턴**: Ruby의 블록과 반복자는 컬렉션 처리를 우아하게 만듭니다.
- **모든 것이 객체입니다**:`3.times { puts "hello" }`— 정수에는 메소드가 있습니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **성능** | 컴파일된 언어보다 느립니다. MRI에는 GIL이 있습니다 | 병렬 처리를 위해 JRuby를 사용하십시오. C 확장으로 오프로드 |
| **인기 하락** | Python, Go, Rust에 비해 새로운 채택이 적음 | 아직도 널리 사용되고 있습니다. 웹 스타트업 및 컨설팅 분야의 강자 |
| **입력** | 동적 입력으로 인해 런타임 오류가 발생할 수 있음 | 선택적 정적 입력을 위해 Sorbet 또는 RBS 사용 |
| **메모리 사용량** | Go 또는 Rust보다 더 높은 메모리 공간 | 대부분의 웹 애플리케이션에 사용 가능 |
| **취업 시장** | Python이나 JavaScript보다 새로운 직책이 적습니다 | 특정 틈새 시장에 강함(Rails 상점, 컨설팅) |
---

## 구문 기본 사항
### 변수 및 유형
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

### 메서드 및 블록
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

### 클래스 및 모듈
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

### 메타프로그래밍
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

## 루비 온 레일즈
Rails는 MVC(Model-View-Controller) 아키텍처를 따르고 다음 사항을 강조하는 풀스택 웹 프레임워크입니다.
- **구성에 대한 관례**: 합리적인 기본값 — 모든 것을 구성할 필요가 없습니다.
- **반복하지 마세요(DRY)**: 생성기, 마이그레이션 및 규칙을 사용하여 반복을 최소화하세요.
- **활성 레코드**: 데이터베이스 개체는 Ruby 개체입니다.  `User.find(1)`는 사용자를 검색합니다.
- **마이그레이션**: 데이터베이스 스키마 변경 사항은 버전이 지정된 Ruby 코드입니다.
Rails는 GitHub, Shopify, Stripe(초기), Basecamp, GitLab 및 많은 스타트업을 지원합니다.
---

## 고급 구문 및 패턴
### 덕 타이핑 및 동적 디스패치
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

### 프로세스, 람다 및 클로저
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

### 패턴 매칭(Ruby 3.0+)
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

### 연산자 오버로딩
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

## 동시성 및 병렬성
### 스레드
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

### 파이버 — 경량 코루틴
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

### Async Gem을 사용한 비동기/대기
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조(레일)
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

### Gemfile — 종속성 관리
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

### 종속성 명령
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### CI/CD 파이프라인(GitHub 작업)
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

## 테스트
### RSpec — 테스트 프레임워크
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

### 조롱과 스터빙
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

### 테스트 명령
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## 상호 운용성
### C 확장
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

### FFI — 외부 기능 인터페이스
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

### JRuby — JVM 상호 운용성
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

## 디자인 패턴
### 관찰자 패턴
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

### 팩토리 패턴
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

### 데코레이터 패턴
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

## 성능 및 최적화
### 프로파일링 도구
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

### 최적화 기술
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

## 배포
### 푸마 웹 서버
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### 도커 배포
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

### 플랫폼 배포
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

## 루비를 사용해야 하는 경우
| 시나리오 | 왜 루비인가 | 더 나은 대안 |
|----------|---------|------|
| 웹 애플리케이션(레일) | 신속한 개발, 생산적인 프레임워크 | Django(Python), Laravel(PHP), Next.js |
| 프로토타이핑 | 매우 빠른 작성 및 반복 | 파이썬, 자바스크립트 |
| 스크립팅 및 자동화 | 우아한 구문, 강력한 텍스트 처리 | 파이썬, 쉘 |
| DevOps 도구(Chef, Puppet) | 생태계 구축 | 가자, 파이썬 |
| CLI 도구 | 가능하지만 이상적이지는 않음 | 가서 러스트 |
| 성능이 중요한 시스템 | 너무 느림 | C, C++, 러스트, Go |
| 데이터 과학 / ML | 생태계가 아니다 | 파이썬, R |
| 모바일 앱 | 적합하지 않음 | 스위프트, 코틀린, 플러터 |
---

## 종합 Q&A
### Q1: Ruby에서`proc`,`lambda`,`block`의 차이점은 무엇인가요?
**답:** 세 가지 모두 클로저이지만 동작이 다릅니다. `block`는`do...end`또는 `{}`를 사용하여 메서드에 전달된 익명의 코드 청크입니다. `proc`는 객체로 저장된 블록입니다. 인수 개수를 확인하지 않고 `return`는 둘러싸는 메서드를 종료합니다. `lambda`는 proc과 비슷하지만 인수 개수를 확인하고 `return`는 람다만 종료합니다. 일회성 콜백을 위한 블록, 재사용 가능한 스니펫을 위한 프로시저, 메서드와 유사한 동작이 필요한 경우 람다를 사용하세요.
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

### Q2: Ruby gem과 Bundler는 어떻게 작동하나요?
**답:** Gem은 Ruby의 패키지 시스템으로 RubyGems.org를 통해 배포되는 재사용 가능한 라이브러리입니다. `Gemfile`는 종속성을 선언합니다.  `bundle install`는 버전을 확인하고 재현성을 위해 `Gemfile.lock`를 생성합니다.  `bundle exec`는 gem 컨텍스트에서 명령을 실행합니다. 호환 가능한 버전 제약 조건에는 `gem 'name', '~> 2.0'`를 사용하세요. 항상 애플리케이션용으로 `Gemfile.lock`를 커밋하고 라이브러리용으로는 커밋하지 마세요.
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

### Q3: Ruby의 심볼 유형은 무엇이며 왜 중요한가요?
**A:** 기호(`:name`)는 변경할 수 없는 인턴 문자열입니다. 각 고유 기호는 메모리에 한 번만 존재합니다. 해시 키, 메서드 이름 및 식별자에 이상적입니다. Ruby에는 메타프로그래밍에 광범위하게 사용되는`Symbol`개체도 있습니다(`send`,`define_method`). 고정 식별자에는 기호를 사용합니다. 콘텐츠를 조작해야 할 때는 문자열을 사용하세요.
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

### Q4: Ruby의 메타프로그래밍은 어떻게 작동하며, 언제 사용해야 합니까?
**답:** Ruby에서는 코드가 런타임에 코드를 정의할 수 있습니다. `define_method`는 동적으로 메서드를 생성하고, `method_missing`는 정의되지 않은 메서드 호출을 가로채고, `send`는 비공개 메서드를 호출하고,`class_eval`/ `instance_eval`는 클래스/인스턴스 컨텍스트에서 코드를 평가합니다. 메타프로그래밍은 강력하지만 코드를 이해하기 어렵게 만듭니다. 일상적인 논리가 아닌 DSL 및 프레임워크 매직에 사용하세요.
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

### Q5: Ruby에서 오류를 처리하는 가장 좋은 방법은 무엇인가요?
**답:** Ruby는 오류 처리를 위해 예외를 사용합니다. `StandardError`(`Exception` 아님 - 시스템 수준 오류를 포착함)에서 상속되는 사용자 정의 예외 클래스를 정의합니다. 구조화된 처리를 위해서는 `begin/rescue/else/ensure`를 사용하세요. 일반 `RuntimeError`가 아닌 특정 예외를 발생시킵니다. 간단한 단일 라이너의 수정자로 `rescue`를 사용합니다.
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

## 사고 사슬 문제 해결
### 문제 1: 구성 파일용 DSL 구축
**문제 설명:** 읽기 쉽고 선언적인 구문으로 서버 구성을 정의할 수 있는 Ruby DSL을 만듭니다. DSL은 중첩된 블록, 유효성 검사 및 JSON 직렬화를 지원해야 합니다.
**1단계 - 문제 이해:**
(1) 블록과 메서드 호출을 사용한 깔끔한 DSL 구문, (2)`instance_eval`또는 명시적 메서드를 통한 데이터 수집, (3) 필수 필드의 유효성 검사, (4) JSON 직렬화가 필요합니다. Ruby의 메타프로그래밍은 DSL을 자연스럽게 만듭니다.
**2단계 - 접근 방식 파악:**
- DSL 호출을 캡처하려면 빌더 클래스와 함께 `instance_eval`를 사용하세요.
- 인스턴스 변수에 구성을 저장합니다.
- 직렬화 전에 필수 필드를 확인하세요.
- 출력에는 `to_h`, `JSON.generate`를 사용합니다.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- DSL은 읽기 쉽고 선언적이므로 프로그래머가 아닌 사람도 이해할 수 있습니다.
- 유효성 검사는 생성 시 누락된 필수 필드를 포착합니다.
- `instance_eval`는 깔끔한 블록 구문을 제공하지만 `self`를 제한합니다. 더 복잡한 DSL의 경우 `BasicObject`를 빌더의 슈퍼클래스로 사용하세요.
- 프로덕션: 프로덕션 등급 구성 DSL을 위해`dry-configurable`또는`configurate`gem을 고려하세요.
### 문제 2: 메모 라이브러리 구현
**문제 설명:** 메소드 결과를 캐시하기 위해 모든 클래스에 혼합할 수 있는 메모 모듈을 구축하십시오. TTL(Time-to-Live), 캐시 크기 제한 및 사용자 정의 캐시 키를 지원합니다.
**1단계 - 문제 이해:**
(1)`memoize`클래스 메서드를 추가하는 모듈, (2) 이 메서드는 캐싱 로직으로 대상 메서드를 래핑하고, (3) TTL 만료 지원, (4) 캐시가 가득 찼을 때 LRU 제거가 필요합니다. Ruby의`Module#prepend`및 `define_method`는 이에 이상적입니다.
**2단계 - 접근 방식 파악:**
- `Module.new`를 `define_method`와 함께 사용하여 래퍼를 만듭니다.
- TTL에 대한 타임스탬프가 있는 해시에 캐시를 저장합니다.
- 원래 방법 앞에 캐싱 레이어를 삽입하려면 `prepend`를 사용하세요.
- 구성 가능한 옵션 지원:`ttl`,`max_size`,`key`.
**3단계 - 솔루션 구현:**
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

**4단계 - 확인 및 최적화:**
- 스레드 안전성: `Mutex`는 캐시 읽기/쓰기를 보호합니다. 계산은 잠금 외부에서 발생합니다.
- TTL: 만료된 항목은 액세스 시 지연 정리됩니다.
- LRU 제거: 캐시가`max_size`를 초과하면 가장 오래된 항목(타임스탬프 기준)이 제거됩니다.
- 사용자 정의 키:`key`람다를 사용하면 캐시 ID를 세밀하게 제어할 수 있습니다.
- 프로덕션: 간단한 경우에는`memoist`gem을 사용하고, 분산 캐싱에는 Redis 지원 메모이제이션을 사용하세요.
---

## 요약
Ruby는 개발자의 행복과 표현력을 우선시하는 언어입니다. 그 구문은 모든 언어 중에서 가장 읽기 쉬운 언어 중 하나이며 Ruby on Rails는 지금까지 만들어진 가장 생산적인 웹 프레임워크 중 하나로 남아 있습니다. Ruby의 인기는 Python 및 JavaScript에 비해 감소했지만 웹 개발, 스크립팅 및 자동화를 위한 강력하고 즐거운 언어로 남아 있습니다. 우아한 코드와 빠른 개발을 중시한다면 Ruby는 배울 가치가 있습니다.