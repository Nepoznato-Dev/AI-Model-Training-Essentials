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

## 総合的な Q&A
### Q1: Ruby の`proc`、`lambda`、および`block`の違いは何ですか?
**A:** 3 つはすべてクロージャですが、動作が異なります。`block`は、`do...end`または`{}`を使用してメソッドに渡されるコードの匿名チャンクです。`proc`はオブジェクトとして保存されたブロックです。引数の数はチェックされず、`return` は外側のメソッドを終了します。`lambda`はプロシージャに似ていますが、引数の数をチェックし、`return` はラムダのみを終了します。 1 回限りのコールバックにはブロックを、再利用可能なスニペットには proc を、メソッドのような動作が必要な場合にはラムダを使用します。
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

### Q2: Ruby gem と Bundler はどのように機能しますか?
**A:** Gems は Ruby のパッケージ システムであり、RubyGems.org 経由で配布される再利用可能なライブラリです。`Gemfile`は依存関係を宣言します。 `bundle install`はバージョンを解決し、再現性のために`Gemfile.lock`を作成します。 `bundle exec`は gem コンテキストでコマンドを実行します。互換性のあるバージョンの制約には`gem 'name', '~> 2.0'`を使用します。アプリケーションに対しては常に`Gemfile.lock`をコミットしますが、ライブラリに対してはコミットしません。
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

### Q3: Ruby のシンボル タイプとは何ですか?また、それらが重要な理由は何ですか?
**A:** シンボル (`:name`) は不変のインターンされた文字列であり、それぞれの一意のシンボルはメモリ内に 1 回だけ存在します。これらは、ハッシュ キー、メソッド名、識別子に最適です。 Ruby には、メタプログラミングで広く使用される`Symbol`オブジェクトもあります (`send`、`define_method`)。固定識別子には記号を使用します。コンテンツを操作する必要がある場合は文字列を使用します。
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

### Q4: Ruby のメタプログラミングはどのように機能しますか?いつ使用する必要がありますか?
**A:** Ruby では実行時にコードを定義できます。`define_method` はメソッドを動的に作成し、`method_missing` は未定義のメソッド呼び出しをインターセプトし、`send` はプライベート メソッドを呼び出し、`class_eval` /`instance_eval`はクラス/インスタンス コンテキストでコードを評価します。メタプログラミングは強力ですが、コードを理解しにくくします。日常的なロジックではなく、DSL やフレームワーク マジックに使用してください。
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

### Q5: Ruby でエラーを処理する最善の方法は何ですか?
**A:** Ruby はエラー処理に例外を使用します。`StandardError`(システムレベルのエラーを捕捉する`Exception`ではありません) から継承するカスタム例外クラスを定義します。構造化された処理には`begin/rescue/else/ensure`を使用します。汎用的な`RuntimeError`ではなく、特定の例外を発生させます。単純なワンライナーの修飾子として`rescue`を使用します。
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

## 思考連鎖による問題解決
### 問題 1: 構成ファイル用の DSL を構築する
**問題ステートメント:** 読みやすい宣言構文でサーバー構成を定義できる Ruby DSL を作成します。 DSL は、ネストされたブロック、検証、JSON へのシリアル化をサポートする必要があります。
**ステップ 1 — 問題を理解する:**
(1) ブロックとメソッド呼び出しを使用したクリーンな DSL 構文、(2)`instance_eval`または明示的なメソッドによるデータ収集、(3) 必須フィールドの検証、(4) JSON シリアル化が必要です。 Ruby のメタプログラミングにより、DSL が自然になります。
**ステップ 2 — アプローチを特定する:**
- DSL 呼び出しをキャプチャするには、ビルダー クラスで`instance_eval`を使用します。
- 設定をインスタンス変数に保存します。
- シリアル化する前に必須フィールドを検証します。
- 出力には`to_h`および`JSON.generate`を使用します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- DSL は読みやすく、宣言的であるため、プログラマーでなくても理解できます。
- 検証により、構築時に欠落している必須フィールドが検出されます。
-`instance_eval`はクリーンなブロック構文を提供しますが、`self` は制限されます。より複雑な DSL の場合は、`BasicObject` をビルダーのスーパークラスとして使用します。
- 実稼働: 実稼働グレードの構成 DSL には、`dry-configurable` または`configurate`gem を検討してください。
### 問題 2: メモ化ライブラリの実装
**問題ステートメント:** メソッドの結果をキャッシュするために任意のクラスに混合できるメモ化モジュールを構築します。 TTL (存続時間)、キャッシュ サイズ制限、カスタム キャッシュ キーをサポートします。
**ステップ 1 — 問題を理解する:**
(1)`memoize`クラス メソッドを追加するモジュール、(2) メソッドがターゲット メソッドをキャッシュ ロジックでラップする、(3) TTL 有効期限のサポート、(4) キャッシュがいっぱいになった場合の LRU エビクションが必要です。 Ruby の`Module#prepend`および`define_method`はこれに最適です。
**ステップ 2 — アプローチを特定する:**
- ラッパーを作成するには、`Module.new` を`define_method`とともに使用します。
- TTL のタイムスタンプを含むハッシュにキャッシュを保存します。
-`prepend`を使用して、元のメソッドの前にキャッシュ層を挿入します。
- 構成可能なオプションをサポートします:`ttl`、`max_size`、`key`。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- スレッド セーフ:`Mutex`はキャッシュの読み取り/書き込みを保護します。計算はロックの外側で行われます。
- TTL: 期限切れのエントリはアクセス時に遅延して削除されます。
- LRU エビクション: キャッシュが`max_size`を超えると、(タイムスタンプによる) 最も古いエントリが削除されます。
- カスタム キー:`key`ラムダにより、キャッシュ ID をきめ細かく制御できます。
- 運用: 単純な場合には`memoist`gem を使用し、分散キャッシュには Redis を利用したメモ化を使用します。
---

＃＃ まとめ
Ruby は開発者の幸福感と表現力を優先した言語です。その構文はあらゆる言語の中で最も読みやすく、Ruby on Rails はこれまでに作成された Web フレームワークの中で最も生産性の高いものの 1 つであり続けています。 Ruby の人気は Python や JavaScript に比べて低下していますが、Web 開発、スクリプト作成、自動化にとって強力で楽しい言語であることに変わりはありません。エレガントなコードと迅速な開発を重視する場合は、Ruby を学ぶ価値があります。