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

# ルビー
Ruby は、動的インタプリタ型オブジェクト指向プログラミング言語で、まつもとゆきひろ "Matz" によって作成され、1995 年に日本で初めてリリースされました。 Ruby はプログラマーの幸福を重視して設計されています。その構文はエレガントで自然で、ほとんど英語のように読めます。 Ruby では、整数やブール値などのプリミティブ型も含めて、すべてがオブジェクトです。 Ruby は、Ruby on Rails Web フレームワークで最もよく知られています。このフレームワークは、構成よりも慣例とラピッド プロトタイピングを普及させることで Web 開発に革命をもたらしました。
Rails 以外にも、Ruby はスクリプト作成、自動化、DevOps ツール (Chef、Puppet)、および汎用言語として使用されます。表現力豊かな構文と強力なメタプログラミング機能により、書くのが楽しくなります。
---

## Ruby が重要な理由
- **開発者の幸福度**: Ruby は読みやすく、楽しめるように設計されています。 「Ruby はプログラマを幸せにするように設計されています」 — Matz.
- **表現的な構文**: コードは英語のように読めます。最小限の句読点、自然なフレージング。
- **Ruby on Rails**: これまでに作成された中で最も生産性の高い Web フレームワークの 1 つ。 GitHub、Shopify、Basecamp、GitLab を強化します。
- **メタプログラミング**: Ruby は実行時に自身を変更できます。メソッドを動的に定義し、ドメイン固有言語 (DSL) を作成します。
- **ブロック/イテレータ パターン**: Ruby のブロックとイテレータにより、コレクション処理がエレガントになります。
- **すべてはオブジェクトです**:`3.times { puts "hello" }`— 整数にはメソッドがあります。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **パフォーマンス** |コンパイル言語よりも遅い。 MRI には GIL があります |並列処理には JRuby を使用します。 C 拡張機能へのオフロード |
| **人気の低下** | Python、Go、Rust に比べて新規採用が少ない |今でも広く使用されています。 Webスタートアップとコンサルティングに強い |
| **入力** |動的型付けは実行時エラーを引き起こす可能性があります。オプションの静的型付けには Sorbet または RBS を使用します。
| **メモリ使用量** | Go や Rust よりもメモリ フットプリントが大きい |ほとんどの Web アプリケーションで使用可能 |
| **雇用市場** | Python や JavaScript よりも新しいポジションが少ない |特定のニッチに強い (Rails ショップ、コンサルティング) |
---

## 構文の基礎
### 変数と型
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

### メソッドとブロック
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

### クラスとモジュール
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

### メタプログラミング
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
Rails は、MVC (Model-View-Controller) アーキテクチャに従い、次のことに重点を置いたフルスタック Web フレームワークです。
- **設定よりも規約**: 賢明なデフォルト — すべてを設定する必要はありません。
- **Don't Reply Yourself (DRY)**: ジェネレーター、移行、規約を使用して、繰り返しを最小限に抑えます。
- **アクティブ レコード**: データベース オブジェクトは Ruby オブジェクトです。 `User.find(1)`はユーザーを取得します。
- **移行**: データベース スキーマの変更は、バージョン管理された Ruby コードです。
Rails は、GitHub、Shopify、Stripe (初期)、Basecamp、GitLab、および多くのスタートアップを支えています。
---

## 高度な構文とパターン
### アヒルタイピングと動的ディスパッチ
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

### プロシージャ、ラムダ、クロージャ
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

### パターン マッチング (Ruby 3.0 以降)
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

### 演算子のオーバーロード
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

## 同時実行性と並列処理
### スレッド
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

### ファイバー — 軽量コルーチン
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

### 非同期 Gem による非同期/待機
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

## プロジェクトの構成とシステムの構築
### プロジェクト構造 (Rails)
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

### Gemfile — 依存関係の管理
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

### 依存関係コマンド
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### CI/CD パイプライン (GitHub アクション)
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

## テスト
### RSpec — テストフレームワーク
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

### モッキングとスタブ
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

### テストコマンド
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## 相互運用性
### C 拡張機能
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

### FFI — 外部関数インターフェイス
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

### JRuby — JVM の相互運用性
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

## デザインパターン
### オブザーバーパターン
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

### ファクトリーパターン
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

### デコレータ パターン
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

## パフォーマンスと最適化
### プロファイリングツール
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

### 最適化手法
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

## デプロイメント
### Puma Web サーバー
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### Docker のデプロイメント
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

### プラットフォームの導入
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

## Ruby を使用する場合
|シナリオ |なぜルビーなのか |より良い代替案 |
|----------|----------|----------|
| Web アプリケーション (Rails) |迅速な開発、生産性の高いフレームワーク | Django (Python)、Laravel (PHP)、Next.js |
|プロトタイピング |書き込みと反復が非常に速い | Python、JavaScript |
|スクリプト作成と自動化 |エレガントな構文、強力なテキスト処理 | Python、シェル |
| DevOps ツール (Chef、Puppet) |確立されたエコシステム |さあ、パイソン |
| CLI ツール |可能だが理想的ではない |さあ、錆びよ |
|パフォーマンスが重要なシステム |遅すぎる | C、C++、Rust、Go |
|データ サイエンス / ML |エコシステムではありません |パイソン、R |
|モバイルアプリ |適さない | Swift、Kotlin、Flutter |
---

＃＃ まとめ
Ruby は開発者の幸福感と表現力を優先した言語です。その構文はあらゆる言語の中で最も読みやすく、Ruby on Rails はこれまでに作成された Web フレームワークの中で最も生産性の高いものの 1 つであり続けています。 Ruby の人気は Python や JavaScript に比べて低下していますが、Web 開発、スクリプト作成、自動化にとって強力で楽しい言語であることに変わりはありません。エレガントなコードと迅速な開発を重視する場合は、Ruby を学ぶ価値があります。