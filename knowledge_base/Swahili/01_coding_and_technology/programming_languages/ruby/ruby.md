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
#Ruby
Ruby ni lugha ya programu inayobadilika, iliyotafsiriwa, yenye mwelekeo wa kitu iliyoundwa na Yukihiro "Matz" Matsumoto na ilitolewa kwa mara ya kwanza mnamo 1995 nchini Japani. Ruby iliundwa kwa kuzingatia furaha ya mpanga programu - sintaksia yake ni maridadi na ya asili, inasoma karibu kama Kiingereza. Kila kitu katika Ruby ni kitu, ikijumuisha aina za awali kama vile nambari kamili na booleans. Ruby anajulikana zaidi kwa mfumo wa wavuti wa Ruby on Rails, ambao ulifanya mageuzi ya ukuzaji wa wavuti kwa kueneza mkusanyiko juu ya usanidi na uchapaji wa haraka.
Zaidi ya Reli, Ruby inatumika kwa uandishi, uwekaji otomatiki, zana za DevOps (Chef, Puppet), na kama lugha ya kusudi la jumla. Sintaksia yake ya kueleza na uwezo wake wa kupanga metaprogramu hufanya iwe furaha kuandika.
---

## Kwa Nini Ruby Ni Mambo
- **Furaha ya msanidi**: Ruby imeundwa ili isomeke na kufurahisha. "Ruby imeundwa kuwafurahisha waandaaji wa programu" - Matz.
- **Sintaksia ya kujieleza**: Msimbo husomeka kama Kiingereza. Uakifishaji mdogo, maneno asilia.
- **Ruby on Rails**: Mojawapo ya mifumo ya wavuti yenye tija zaidi kuwahi kuundwa. Nguvu za GitHub, Shopify, Basecamp, GitLab.
- **Upangaji programu**: Ruby inaweza kujirekebisha wakati wa utekelezaji - kufafanua mbinu kwa ubadilikaji, kuunda lugha mahususi za kikoa (DSL).
- **Muundo wa kuzuia/kurudisha nyuma**: Vitalu vya Ruby na virudia rudia hufanya uchakataji kuwa wa kifahari.
- **Kila kitu ni kitu**:`3.times { puts "hello" }`— nambari kamili zina mbinu.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Utendaji** | Polepole kuliko lugha zilizokusanywa; MRI ina GIL | Tumia JRuby kwa usawa; pakua kwa viendelezi C |
| **Kupungua kwa umaarufu** | Uasilishaji mpya mdogo ikilinganishwa na Python, Go, Rust | Bado inatumika sana; imara katika uanzishaji wa wavuti na ushauri |
| **Kuandika** | Kuandika kwa nguvu kunaweza kusababisha hitilafu za wakati wa utekelezaji | Tumia Sorbet au RBS kwa hiari ya kuandika tuli |
| **Matumizi ya kumbukumbu** | Kumbukumbu ya juu zaidi kuliko Go au Rust | Inakubalika kwa programu nyingi za wavuti |
| **Soko la ajira** | Nafasi mpya chache kuliko Python au JavaScript | Nguvu katika niches maalum (Duka za reli, ushauri) |
---

## Misingi ya Sintaksia
### Vigezo na Aina
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

### Mbinu na Vizuizi
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

### Madarasa na Moduli
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

## Ruby kwenye Reli
Rails ni mfumo kamili wa wavuti unaofuata usanifu wa MVC (Model-View-Controller) na kusisitiza:
- **Mkataba juu ya Usanidi**: Mipangilio ya busara - hakuna haja ya kusanidi kila kitu.
- **Usijirudie (KUKAUSHA)**: Tumia jenereta, uhamaji, na mikusanyiko ili kupunguza marudio.
- **Rekodi Inayotumika**: Vitu vya Hifadhidata ni vitu vya Ruby. `User.find(1)`inarejesha mtumiaji.
- ** Uhamiaji **: Mabadiliko ya schema ya Hifadhidata yametolewa msimbo wa Ruby.
Reli huwezesha GitHub, Shopify, Stripe (mapema), Basecamp, GitLab, na vianzishaji vingi.
---

## Sintaksia na Miundo ya Kina
### Kuandika Bata na Usambazaji kwa Nguvu
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

### Procs, Lambdas, na Kufungwa
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

### Ulinganishaji wa Muundo (Ruby 3.0+)
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

### Kupakia kwa Opereta
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

## Concurrency & Usambamba
### nyuzi
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

### Fibers — Nyepesi Coroutines
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

### Async/Subiri ukitumia Async Gem
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Mradi (Reli)
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

### Faili ya Vito - Usimamizi wa Utegemezi
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

### Amri za Utegemezi
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### CI/CD Bomba (Vitendo vya GitHub)
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

##Upimaji
### RSpec — Mfumo wa Kujaribu
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

### Kudhihaki na Kuchokoza
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

### Amri za Mtihani
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## Kuingiliana
### C Viendelezi
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

### FFI — Kiolesura cha Kazi za Kigeni
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

### JRuby — Ushirikiano wa JVM
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

## Miundo ya Kubuni
### Muundo wa Mwangalizi
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

### Muundo wa Kiwanda
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

### Muundo wa Kipambo
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

## Utendaji na Uboreshaji
### Zana za Kuweka Wasifu
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

### Mbinu za Kuboresha
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

## Usambazaji
### Seva ya Wavuti ya Puma
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### Usambazaji wa Docker
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

### Usambazaji wa Mfumo
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

## Wakati wa Kutumia Ruby
| Hali | Kwanini Ruby | Mbadala Bora |
|----------|---------|-------------------|
| Programu za wavuti (Reli) | Maendeleo ya haraka, mfumo wa tija | Django (Python), Laravel (PHP), Next.js |
| Uchapaji | Haraka sana kuandika na kurudia | Python, JavaScript |
| Maandishi na otomatiki | Sintaksia maridadi, usindikaji wa maandishi wenye nguvu | Chatu, Shell |
| Vifaa vya DevOps (Chef, Puppet) | Mfumo wa ikolojia | Nenda, Chatu |
| Zana za CLI | Inawezekana lakini sio bora | Nenda, Kutu |
| Mifumo muhimu ya utendaji | Polepole sana | C, C++, Rust, Nenda |
| Sayansi ya data / ML | Sio mfumo wa ikolojia | Chatu, R |
| Programu za simu | Haifai | Swift, Kotlin, Flutter |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kuna tofauti gani kati ya`proc`,`lambda`, na`block`katika Ruby?
**J:** Zote tatu ni kufungwa, lakini zinatofautiana kitabia.`block`ni sehemu ya msimbo isiyojulikana iliyopitishwa kwa mbinu kwa`do...end`au`{}`.`proc`ni kizuizi kilichohifadhiwa kama kitu - haiangalii hesabu ya hoja na`return`inaondoka kwenye mbinu ya kuambatanisha.`lambda`ni kama proc lakini hukagua hesabu ya hoja na`return`hutoka kwenye lambda pekee. Tumia vizuizi kwa kupiga simu mara moja, procs kwa vijisehemu vinavyoweza kutumika tena, na lambdas unapohitaji tabia kama ya mbinu.
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

### Q2: Je, vito vya Ruby na Bundler hufanyaje kazi?
**J:** Vito ni mfumo wa kifurushi cha Ruby - maktaba zinazoweza kutumika tena zinazosambazwa kupitia RubyGems.org.`Gemfile`inatangaza utegemezi; `bundle install`hutatua matoleo na kuunda`Gemfile.lock`kwa uzalishaji tena. `bundle exec`huendesha amri katika muktadha wa vito. Tumia`gem 'name', '~> 2.0'`kwa vikwazo vinavyooana vya toleo. Daima wasilisha`Gemfile.lock`kwa programu tumizi, lakini si kwa maktaba.
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

### Q3: Aina za alama za Ruby ni zipi, na kwa nini ni muhimu?
**A:** Alama (`:name`) hazibadiliki, mifuatano iliyoingiliana - kila alama ya kipekee inapatikana mara moja tu kwenye kumbukumbu. Ni bora kwa funguo za hashi, majina ya njia, na vitambulisho. Ruby pia ina vipengee vya`Symbol`vinavyotumika sana katika upangaji metaprogramu (`send`,`define_method`). Tumia alama kwa vitambulisho vilivyowekwa; tumia masharti unapohitaji kuchezea yaliyomo.
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

### Q4: Je, upangaji metaprogramu wa Ruby hufanya kazi vipi, na ninapaswa kuitumia lini?
**J:** Ruby inaruhusu msimbo kufafanua msimbo wakati wa utekelezaji:`define_method`huunda mbinu kwa nguvu,`method_missing`hunasa simu za mbinu ambazo hazijabainishwa,`send`hupiga simu kwa njia za kibinafsi, na`class_eval`/`instance_eval`kutathmini muktadha wa msimbo katika darasa. Upangaji programu meta ni nguvu lakini hufanya msimbo kuwa mgumu kuelewa - itumie kwa DSL na uchawi wa mifumo, si kwa mantiki ya kila siku.
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

### Q5: Ni ipi njia bora ya kushughulikia makosa katika Ruby?
**J:** Ruby hutumia vighairi katika kushughulikia makosa. Bainisha madarasa ya kutofuata kanuni maalum yanayorithi kutoka kwa`StandardError`(sio`Exception`- ambayo hupata hitilafu za kiwango cha mfumo). Tumia`begin/rescue/else/ensure`kwa utunzaji wa muundo. Onyesha vighairi maalum, sio vya kawaida`RuntimeError`. Tumia`rescue`kama kirekebishaji cha mjengo mmoja rahisi.
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

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Tengeneza DSL kwa Faili za Usanidi
**Taarifa ya Tatizo:** Unda Ruby DSL ambayo inaruhusu kufafanua usanidi wa seva katika sintaksia inayoweza kusomeka na inayotamka. DSL inapaswa kutumia vizuizi vilivyowekwa, uthibitishaji na utayarishaji wa JSON.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) sintaksia safi ya DSL kwa kutumia vizuizi na simu za mbinu, (2) ukusanyaji wa data kupitia`instance_eval`au mbinu dhahiri, (3) uthibitishaji wa sehemu zinazohitajika, (4) Usajili wa JSON. Upangaji meta wa Ruby hufanya DSL kuwa asili.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia`instance_eval`na darasa la wajenzi kunasa simu za DSL.
- Hifadhi Configuration katika vigezo mfano.
- Thibitisha sehemu zinazohitajika kabla ya kuratibu.
- Tumia`to_h`na`JSON.generate`kwa pato.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- DSL inaweza kusomeka na kutangazwa - wasio waandaaji programu wanaweza kuielewa.
- Uthibitishaji hupata kukosa sehemu zinazohitajika wakati wa ujenzi.
-`instance_eval`hutoa sintaksia safi ya vitalu lakini inawekea mipaka`self`- kwa DSL changamano zaidi, tumia`BasicObject`kama daraja kuu la wajenzi.
- Uzalishaji: zingatia vito vya`dry-configurable`au`configurate`kwa DSL za usanidi wa kiwango cha uzalishaji.
### Tatizo la 2: Tekeleza Maktaba ya Kukariri
**Taarifa ya Tatizo:** Tengeneza moduli ya kukariri ambayo inaweza kuchanganywa katika darasa lolote ili kuweka akiba ya matokeo ya mbinu. Inasaidia TTL (muda wa kuishi), vikomo vya ukubwa wa kache, na vitufe vya kache maalum.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) moduli inayoongeza mbinu ya darasa la `memoize`, (2) mbinu hiyo inajumuisha mbinu lengwa kwa mantiki ya kache, (3) usaidizi wa kuisha kwa muda wa TTL, (4) uondoaji wa LRU wakati akiba imejaa. Ruby's`Module#prepend`na`define_method`ni bora kwa hili.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia`Module.new`na`define_method`kuunda kanga.
- Hifadhi akiba katika heshi yenye mihuri ya muda ya TTL.
- Tumia`prepend`kuingiza safu ya kache kabla ya mbinu asili.
- Kusaidia chaguzi zinazoweza kusanidiwa:`ttl`,`max_size`,`key`.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Usalama wa nyuzi:`Mutex`inalinda usomaji wa kache / huandika; hesabu hufanyika nje ya kufuli.
- TTL: maingizo yaliyoisha muda wake yanasafishwa kwa uvivu kwenye ufikiaji.
- Kufukuzwa kwa LRU: wakati akiba inapozidi`max_size`, ingizo la zamani zaidi (kwa muhuri wa muda) huondolewa.
- Vifunguo maalum: lambda ya`key`inaruhusu udhibiti mzuri wa utambulisho wa akiba.
- Uzalishaji: tumia vito vya`memoist`kwa kesi rahisi, au ukariri unaoungwa mkono na Redis kwa uakibishaji uliosambazwa.
---

## Muhtasari
Ruby ni lugha inayotanguliza furaha ya msanidi programu na kujieleza. Sintaksia yake ni kati ya lugha inayosomeka zaidi, na Ruby on Rails inasalia kuwa mojawapo ya mifumo ya wavuti yenye tija zaidi kuwahi kuundwa. Ingawa umaarufu wa Ruby umepungua ikilinganishwa na Python na JavaScript, inasalia kuwa lugha yenye nguvu na ya kufurahisha kwa ukuzaji wa wavuti, uandishi, na uwekaji otomatiki. Ikiwa unathamini msimbo wa kifahari na maendeleo ya haraka, Ruby anafaa kujifunza.