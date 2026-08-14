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
#रूबी
रूबी युकिहिरो "मैट्ज़" मात्सुमोतो द्वारा बनाई गई एक गतिशील, व्याख्या की गई, ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग भाषा है और पहली बार 1995 में जापान में जारी की गई थी। रूबी को प्रोग्रामर की ख़ुशी पर ध्यान केंद्रित करके डिज़ाइन किया गया था - इसका सिंटैक्स सुरुचिपूर्ण और प्राकृतिक है, लगभग अंग्रेजी की तरह पढ़ना। रूबी में सब कुछ एक वस्तु है, जिसमें पूर्णांक और बूलियन जैसे आदिम प्रकार शामिल हैं। रूबी को रूबी ऑन रेल्स वेब फ्रेमवर्क के लिए जाना जाता है, जिसने कॉन्फ़िगरेशन और रैपिड प्रोटोटाइप पर कन्वेंशन को लोकप्रिय बनाकर वेब विकास में क्रांति ला दी।
बियॉन्ड रेल्स, रूबी का उपयोग स्क्रिप्टिंग, ऑटोमेशन, डेवऑप्स टूलिंग (शेफ, पपेट) और एक सामान्य-उद्देश्य वाली भाषा के रूप में किया जाता है। इसकी अभिव्यंजक वाक्यविन्यास और शक्तिशाली मेटाप्रोग्रामिंग क्षमताएं इसे लिखने का आनंद देती हैं।
---

## रूबी क्यों मायने रखती है
- **डेवलपर खुशी**: रूबी को पढ़ने योग्य और आनंददायक बनाने के लिए डिज़ाइन किया गया है। "रूबी को प्रोग्रामर्स को खुश करने के लिए डिज़ाइन किया गया है" - मैट्ज़।
- **अभिव्यंजक वाक्यविन्यास**: कोड अंग्रेजी की तरह पढ़ता है। न्यूनतम विराम चिह्न, प्राकृतिक वाक्यांश.
- **रूबी ऑन रेल्स**: अब तक बनाए गए सबसे अधिक उत्पादक वेब फ्रेमवर्क में से एक। पॉवर्स GitHub, Shopify, Basecamp, GitLab।
- **मेटाप्रोग्रामिंग**: रूबी रनटाइम पर खुद को संशोधित कर सकती है - तरीकों को गतिशील रूप से परिभाषित कर सकती है, डोमेन-विशिष्ट भाषाएं (डीएसएल) बना सकती है।
- **ब्लॉक/इटरेटर पैटर्न**: रूबी के ब्लॉक और इटरेटर संग्रह प्रसंस्करण को सुरुचिपूर्ण बनाते हैं।
- **हर चीज़ एक वस्तु है**:`3.times { puts "hello" }`- पूर्णांकों में विधियाँ होती हैं।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **प्रदर्शन** | संकलित भाषाओं की तुलना में धीमी; एमआरआई में जीआईएल है | समानता के लिए JRuby का उपयोग करें; C एक्सटेंशन पर ऑफ़लोड करें |
| **घटती लोकप्रियता** | पाइथॉन, गो, रस्ट की तुलना में कम नए अपनाने | अभी भी व्यापक रूप से उपयोग किया जाता है; वेब स्टार्टअप और परामर्श में मजबूत |
| **टाइपिंग** | डायनामिक टाइपिंग से रनटाइम त्रुटियां हो सकती हैं | वैकल्पिक स्थैतिक टाइपिंग के लिए सॉर्बेट या आरबीएस का उपयोग करें |
| **मेमोरी उपयोग** | गो या रस्ट की तुलना में अधिक मेमोरी फ़ुटप्रिंट | अधिकांश वेब अनुप्रयोगों के लिए स्वीकार्य |
| **नौकरी बाज़ार** | पायथन या जावास्क्रिप्ट की तुलना में कम नए पद | विशिष्ट क्षेत्रों में मजबूत (रेल की दुकानें, परामर्श) |
---

## सिंटेक्स बुनियादी बातें
### चर और प्रकार
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

### तरीके और ब्लॉक
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

### कक्षाएं और मॉड्यूल
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

### मेटाप्रोग्रामिंग
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

## रूबी ऑन रेल्स
रेल्स एक फुल-स्टैक वेब फ्रेमवर्क है जो एमवीसी (मॉडल-व्यू-कंट्रोलर) आर्किटेक्चर का अनुसरण करता है और इस पर जोर देता है:
- **कॉन्फ़िगरेशन पर कन्वेंशन**: समझदार डिफ़ॉल्ट - सब कुछ कॉन्फ़िगर करने की आवश्यकता नहीं है।
- **डोंट रिपीट योरसेल्फ (DRY)**: पुनरावृत्ति को कम करने के लिए जनरेटर, माइग्रेशन और कन्वेंशन का उपयोग करें।
- **सक्रिय रिकॉर्ड**: डेटाबेस ऑब्जेक्ट रूबी ऑब्जेक्ट हैं। `User.find(1)`एक उपयोगकर्ता को पुनः प्राप्त करता है।
- **माइग्रेशन**: डेटाबेस स्कीमा परिवर्तन संस्करण रूबी कोड हैं।
रेल्स GitHub, Shopify, Stripe (प्रारंभिक), बेसकैंप, GitLab और कई स्टार्टअप को शक्ति प्रदान करता है।
---

## उन्नत सिंटैक्स और पैटर्न
### डक टाइपिंग और डायनेमिक डिस्पैच
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

### प्रोक्स, लैम्ब्डा, और क्लोजर
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

### पैटर्न मिलान (रूबी 3.0+)
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

### ऑपरेटर ओवरलोडिंग
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

## समवर्ती एवं समांतरता
### धागे
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

### फ़ाइबर - हल्के कोरटाइन
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

### Async जेम के साथ Async/प्रतीक्षा करें
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना (रेल)
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

### जेमफ़ाइल - निर्भरता प्रबंधन
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

### निर्भरता आदेश
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### आरस्पेक - परीक्षण ढांचा
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

### उपहास और ठूंठ
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

### टेस्ट कमांड
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## अंतरसंचालनीयता
### सी एक्सटेंशन
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

### एफएफआई - विदेशी फ़ंक्शन इंटरफ़ेस
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

### जेरूबी - जेवीएम इंटरऑपरेबिलिटी
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

## डिज़ाइन पैटर्न
### प्रेक्षक पैटर्न
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

### फ़ैक्टरी पैटर्न
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

### डेकोरेटर पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
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

### अनुकूलन तकनीकें
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

## तैनाती
### प्यूमा वेब सर्वर
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### डॉकर परिनियोजन
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

### प्लेटफ़ॉर्म परिनियोजन
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

## रूबी का उपयोग कब करें
| परिदृश्य | रूबी क्यों | बेहतर विकल्प |
|---|---|-----|
| वेब अनुप्रयोग (रेल) | तीव्र विकास, उत्पादक ढांचा | Django (पायथन), लारवेल (PHP), Next.js |
| प्रोटोटाइपिंग | लिखने और दोहराने में बहुत तेज़ | पायथन, जावास्क्रिप्ट |
| स्क्रिप्टिंग और स्वचालन | सुरुचिपूर्ण वाक्यविन्यास, शक्तिशाली पाठ प्रसंस्करण | अजगर, शैल |
| DevOps टूलींग (शेफ, कठपुतली) | स्थापित पारिस्थितिकी तंत्र | जाओ, पायथन |
| सीएलआई उपकरण | संभव है लेकिन आदर्श नहीं | जाओ, जंग |
| प्रदर्शन-महत्वपूर्ण सिस्टम | बहुत धीमा | सी, सी++, रस्ट, गो |
| डेटा साइंस/एमएल | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
| मोबाइल ऐप्स | अनुकूल नहीं | स्विफ्ट, कोटलिन, स्पंदन |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: रूबी में`proc`,`lambda`और`block`के बीच क्या अंतर है?
**ए:** तीनों बंद हैं, लेकिन वे व्यवहार में भिन्न हैं।`block`कोड का एक अज्ञात हिस्सा है जो`do...end`या`{}`के साथ एक विधि को पास किया जाता है।`proc`एक ऑब्जेक्ट के रूप में सहेजा गया एक ब्लॉक है - यह तर्क गणना की जांच नहीं करता है और`return`एन्क्लोजिंग विधि से बाहर निकलता है।`lambda`एक proc की तरह है लेकिन तर्क गणना की जाँच करता है और`return`केवल लैम्ब्डा से बाहर निकलता है। जब आपको विधि-सदृश व्यवहार की आवश्यकता हो तो एकबारगी कॉलबैक के लिए ब्लॉक, पुन: प्रयोज्य स्निपेट के लिए प्रोसेस और लैम्ब्डा का उपयोग करें।
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

### Q2: रूबी जेम्स और बंडलर कैसे काम करते हैं?
**ए:** रत्न रूबी के पैकेज सिस्टम हैं - रूबीगेम्स.ओआरजी के माध्यम से वितरित पुन: प्रयोज्य पुस्तकालय। एक`Gemfile`निर्भरता की घोषणा करता है; `bundle install`संस्करणों का समाधान करता है और प्रतिलिपि प्रस्तुत करने योग्यता के लिए एक`Gemfile.lock`बनाता है। `bundle exec`रत्न संदर्भ में आदेश चलाता है। संगत संस्करण बाधाओं के लिए`gem 'name', '~> 2.0'`का उपयोग करें। अनुप्रयोगों के लिए हमेशा`Gemfile.lock`प्रतिबद्ध करें, लेकिन पुस्तकालयों के लिए नहीं।
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

### Q3: रूबी के प्रतीक प्रकार क्या हैं, और वे महत्वपूर्ण क्यों हैं?
**ए:** प्रतीक (`:name`) अपरिवर्तनीय, आंतरिक स्ट्रिंग हैं - प्रत्येक अद्वितीय प्रतीक स्मृति में केवल एक बार मौजूद होता है। वे हैश कुंजियों, विधि नामों और पहचानकर्ताओं के लिए आदर्श हैं। रूबी के पास`Symbol`ऑब्जेक्ट भी हैं जिनका उपयोग मेटाप्रोग्रामिंग (`send`, `define_method`) में बड़े पैमाने पर किया जाता है। निश्चित पहचानकर्ताओं के लिए प्रतीकों का उपयोग करें; जब आपको सामग्री में हेरफेर करने की आवश्यकता हो तो स्ट्रिंग्स का उपयोग करें।
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

### Q4: रूबी की मेटाप्रोग्रामिंग कैसे काम करती है, और मुझे इसका उपयोग कब करना चाहिए?
**ए:** रूबी कोड को रनटाइम पर कोड को परिभाषित करने की अनुमति देता है:`define_method`गतिशील रूप से तरीकों का निर्माण करता है,`method_missing`अपरिभाषित विधि कॉल को रोकता है,`send`निजी तरीकों को कॉल करता है, और`class_eval`/`instance_eval`एक क्लास/इंस्टेंस संदर्भ में कोड का मूल्यांकन करता है। मेटाप्रोग्रामिंग शक्तिशाली है लेकिन कोड को समझना कठिन बना देता है - इसका उपयोग डीएसएल और फ्रेमवर्क जादू के लिए करें, रोजमर्रा के तर्क के लिए नहीं।
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

### Q5: रूबी में त्रुटियों से निपटने का सबसे अच्छा तरीका क्या है?
**ए:** रूबी त्रुटि प्रबंधन के लिए अपवादों का उपयोग करती है।`StandardError`से प्राप्त होने वाले कस्टम अपवाद वर्गों को परिभाषित करें (`Exception` नहीं - जो सिस्टम-स्तरीय त्रुटियों को पकड़ता है)। संरचित प्रबंधन के लिए`begin/rescue/else/ensure`का उपयोग करें। विशिष्ट अपवाद उठाएँ, सामान्य`RuntimeError`नहीं। सरल वन-लाइनर्स के लिए संशोधक के रूप में`rescue`का उपयोग करें।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: कॉन्फ़िगरेशन फ़ाइलों के लिए एक DSL बनाएँ
**समस्या कथन:** एक रूबी डीएसएल बनाएं जो सर्वर कॉन्फ़िगरेशन को पढ़ने योग्य, घोषणात्मक सिंटैक्स में परिभाषित करने की अनुमति देता है। DSL को JSON में नेस्टेड ब्लॉक, सत्यापन और क्रमबद्धता का समर्थन करना चाहिए।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) ब्लॉक और विधि कॉल का उपयोग करके एक साफ डीएसएल सिंटैक्स, (2)`instance_eval`या स्पष्ट तरीकों के माध्यम से डेटा संग्रह, (3) आवश्यक फ़ील्ड का सत्यापन, (4) JSON क्रमबद्धता। रूबी की मेटाप्रोग्रामिंग डीएसएल को प्राकृतिक बनाती है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- डीएसएल कॉल कैप्चर करने के लिए बिल्डर क्लास के साथ`instance_eval`का उपयोग करें।
- इंस्टेंस वेरिएबल्स में कॉन्फ़िगरेशन स्टोर करें।
- क्रमांकन से पहले आवश्यक फ़ील्ड मान्य करें।
- आउटपुट के लिए`to_h`और`JSON.generate`का उपयोग करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- डीएसएल पठनीय और घोषणात्मक है - गैर-प्रोग्रामर इसे समझ सकते हैं।
- सत्यापन निर्माण के समय लापता आवश्यक फ़ील्ड को पकड़ता है।
-`instance_eval`स्वच्छ ब्लॉक सिंटैक्स प्रदान करता है लेकिन`self`को सीमित करता है - अधिक जटिल DSL के लिए, बिल्डर के सुपरक्लास के रूप में`BasicObject`का उपयोग करें।
- उत्पादन: उत्पादन-ग्रेड कॉन्फ़िगरेशन डीएसएल के लिए`dry-configurable`या`configurate`रत्नों पर विचार करें।
### समस्या 2: एक मेमोइज़ेशन लाइब्रेरी लागू करें
**समस्या कथन:** एक मेमोइज़ेशन मॉड्यूल बनाएं जिसे विधि परिणामों को कैश करने के लिए किसी भी वर्ग में मिलाया जा सकता है। टीटीएल (टाइम-टू-लाइव), कैश आकार सीमा और कस्टम कैश कुंजियों का समर्थन करें।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) एक मॉड्यूल जो एक`memoize`क्लास विधि जोड़ता है, (2) विधि लक्ष्य विधियों को कैशिंग लॉजिक के साथ लपेटती है, (3) टीटीएल समाप्ति के लिए समर्थन, (4) कैश भर जाने पर एलआरयू निष्कासन। रूबी के`Module#prepend`और`define_method`इसके लिए आदर्श हैं।
**चरण 2 - दृष्टिकोण को पहचानें:**
- रैपर बनाने के लिए`define_method`के साथ`Module.new`का उपयोग करें।
- टीटीएल के लिए टाइमस्टैम्प के साथ हैश में कैश स्टोर करें।
- मूल विधि से पहले कैशिंग परत डालने के लिए`prepend`का उपयोग करें।
- कॉन्फ़िगर करने योग्य विकल्पों का समर्थन करें: `ttl`, `max_size`, `key`।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- थ्रेड सुरक्षा:`Mutex`कैश पढ़ने/लिखने की सुरक्षा करता है; गणना लॉक के बाहर होती है.
- टीटीएल: समाप्त हो चुकी प्रविष्टियों को एक्सेस पर आलस्यपूर्वक साफ किया जाता है।
- एलआरयू निष्कासन: जब कैश`max_size`से अधिक हो जाता है, तो सबसे पुरानी प्रविष्टि (टाइमस्टैम्प द्वारा) हटा दी जाती है।
- कस्टम कुंजियाँ:`key`लैम्ब्डा कैश पहचान पर सूक्ष्म नियंत्रण की अनुमति देता है।
- उत्पादन: साधारण मामलों के लिए`memoist`रत्न का उपयोग करें, या वितरित कैशिंग के लिए रेडिस-समर्थित मेमोइज़ेशन का उपयोग करें।
---

## सारांश
रूबी एक ऐसी भाषा है जो डेवलपर की खुशी और अभिव्यक्ति को प्राथमिकता देती है। इसका सिंटैक्स किसी भी भाषा में सबसे अधिक पठनीय है, और रूबी ऑन रेल्स अब तक बनाए गए सबसे अधिक उत्पादक वेब फ्रेमवर्क में से एक है। जबकि रूबी की लोकप्रियता पायथन और जावास्क्रिप्ट की तुलना में कम हो गई है, यह वेब विकास, स्क्रिप्टिंग और स्वचालन के लिए एक शक्तिशाली, मनोरंजक भाषा बनी हुई है। यदि आप सुरुचिपूर्ण कोड और तीव्र विकास को महत्व देते हैं, तो रूबी सीखने लायक है।