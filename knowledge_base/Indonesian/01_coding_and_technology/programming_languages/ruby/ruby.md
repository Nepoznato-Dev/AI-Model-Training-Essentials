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

#ruby
Ruby adalah bahasa pemrograman dinamis, ditafsirkan, berorientasi objek yang dibuat oleh Yukihiro "Matz" Matsumoto dan pertama kali dirilis pada tahun 1995 di Jepang. Ruby dirancang dengan fokus pada kebahagiaan programmer — sintaksisnya elegan dan alami, bacaannya hampir seperti bahasa Inggris. Segala sesuatu di Ruby adalah sebuah objek, termasuk tipe primitif seperti integer dan boolean. Ruby terkenal dengan kerangka web Ruby on Rails, yang merevolusi pengembangan web dengan mempopulerkan konvensi atas konfigurasi dan pembuatan prototipe cepat.
Selain Rails, Ruby digunakan untuk pembuatan skrip, otomatisasi, perkakas DevOps (Chef, Puppet), dan sebagai bahasa tujuan umum. Sintaksnya yang ekspresif dan kemampuan metaprogramming yang kuat membuatnya menyenangkan untuk menulis.
---

## Mengapa Ruby Penting
- **Kebahagiaan pengembang**: Ruby dirancang agar mudah dibaca dan dinikmati. "Ruby dirancang untuk membuat programmer senang" - Matz.
- **Sintaks ekspresif**: Kode dibaca seperti bahasa Inggris. Tanda baca minimal, ungkapan alami.
- **Ruby on Rails**: Salah satu kerangka web paling produktif yang pernah dibuat. Mendukung GitHub, Shopify, Basecamp, GitLab.
- **Metaprogramming**: Ruby dapat memodifikasi dirinya sendiri saat runtime — menentukan metode secara dinamis, membuat bahasa khusus domain (DSL).
- **Pola blok/iterator**: Blok dan iterator Ruby membuat pemrosesan pengumpulan menjadi elegan.
- **Semuanya adalah objek**:`3.times { puts "hello" }`— bilangan bulat memiliki metode.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Kinerja** | Lebih lambat dari bahasa yang dikompilasi; MRI memiliki GIL | Gunakan JRuby untuk paralelisme; membongkar ke ekstensi C |
| **Menurunnya popularitas** | Lebih sedikit adopsi baru dibandingkan dengan Python, Go, Rust | Masih banyak digunakan; kuat dalam startup web dan konsultasi |
| **Mengetik** | Pengetikan dinamis dapat menyebabkan kesalahan runtime | Gunakan Sorbet atau RBS untuk pengetikan statis opsional |
| **Penggunaan memori** | Jejak memori lebih tinggi daripada Go atau Rust | Dapat diterima untuk sebagian besar aplikasi web |
| **Pasar kerja** | Lebih sedikit posisi baru dibandingkan Python atau JavaScript | Kuat di ceruk tertentu (Toko Rel, konsultasi) |
---

## Dasar Sintaks
### Variabel dan Tipe
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

### Metode dan Blok
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

### Kelas dan Modul
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

### Pemrograman meta
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

## Ruby di Rel
Rails adalah kerangka web full-stack yang mengikuti arsitektur MVC (Model-View-Controller) dan menekankan:
- **Konvensi atas Konfigurasi**: Default yang masuk akal — tidak perlu mengonfigurasi semuanya.
- **Jangan Ulangi Diri Sendiri (KERING)**: Gunakan generator, migrasi, dan konvensi untuk meminimalkan pengulangan.
- **Catatan Aktif**: Objek database adalah objek Ruby. `User.find(1)`mengambil pengguna.
- **Migrasi**: Perubahan skema database adalah kode Ruby yang diversi.
Rails mendukung GitHub, Shopify, Stripe (awal), Basecamp, GitLab, dan banyak startup.
---

## Sintaks & Pola Tingkat Lanjut
### Pengetikan Bebek dan Pengiriman Dinamis
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

### Proses, Lambda, dan Penutupan
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

### Pencocokan Pola (Ruby 3.0+)
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

### Operator Kelebihan Beban
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

## Konkurensi & Paralelisme
### Utas
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

### Serat — Coroutine Ringan
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

### Async/Menunggu dengan Permata Async
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

## Konfigurasi Proyek & Sistem Pembangunan
### Struktur Proyek (Rel)
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

### Gemfile — Manajemen Ketergantungan
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

### Perintah Ketergantungan
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### Saluran CI/CD (Tindakan GitHub)
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

## Pengujian
### RSpec — Kerangka Pengujian
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

### Mengejek dan Mematikan
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

### Perintah Tes
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## Interoperabilitas
### C Ekstensi
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

### FFI — Antarmuka Fungsi Asing
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

### JRuby — Interoperabilitas JVM
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

## Pola Desain
### Pola Pengamat
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

### Pola Pabrik
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

### Pola Dekorator
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

## Kinerja & Optimasi
### Alat Pembuatan Profil
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

### Teknik Optimasi
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

## Penerapan
### Server Web Puma
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### Penerapan Docker
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

### Penerapan Platform
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

## Kapan Menggunakan Ruby
| Skenario | Mengapa Ruby | Alternatif Lebih Baik |
|----------|---------|-------------------|
| Aplikasi web (Rel) | Perkembangan pesat, kerangka produktif | Django (Python), Laravel (PHP), Berikutnya.js |
| Pembuatan Prototipe | Sangat cepat untuk menulis dan mengulangi | Python, JavaScript |
| Pembuatan skrip dan otomatisasi | Sintaks yang elegan, pemrosesan teks yang kuat | Python, Cangkang |
| Perkakas DevOps (Koki, Boneka) | Ekosistem yang mapan | Ayo, Python |
| Alat CLI | Mungkin tapi tidak ideal | Ayo, Karat |
| Sistem yang kritis terhadap kinerja | Terlalu lambat | C, C++, Karat, Buka |
| Ilmu data / ML | Bukan ekosistem | Piton, R |
| Aplikasi seluler | Tidak cocok | Cepat, Kotlin, Berkibar |
---

## Tanya Jawab Sintetis
### Q1: Apa perbedaan antara`proc`,`lambda`, dan`block`di Ruby?
**A:** Ketiganya merupakan penutupan, namun perilakunya berbeda.`block`adalah potongan kode anonim yang diteruskan ke metode dengan`do...end`atau`{}`.`proc`adalah blok yang disimpan sebagai objek — ia tidak memeriksa jumlah argumen dan`return`keluar dari metode penutup.`lambda`seperti proc tetapi memeriksa jumlah argumen dan`return`hanya keluar dari lambda. Gunakan blok untuk callback satu kali, procs untuk cuplikan yang dapat digunakan kembali, dan lambda saat Anda memerlukan perilaku seperti metode.
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

### Q2: Bagaimana cara kerja permata Ruby dan Bundler?
**A:** Permata adalah sistem paket Ruby — perpustakaan yang dapat digunakan kembali dan didistribusikan melalui RubyGems.org.`Gemfile`mendeklarasikan dependensi; `bundle install`menyelesaikan versi dan membuat`Gemfile.lock`agar dapat direproduksi. `bundle exec`menjalankan perintah dalam konteks permata. Gunakan`gem 'name', '~> 2.0'`untuk batasan versi yang kompatibel. Selalu komit`Gemfile.lock`untuk aplikasi, tetapi tidak untuk perpustakaan.
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

### Q3: Apa saja tipe simbol Ruby, dan mengapa itu penting?
**A:** Simbol (`:name`) adalah string yang tidak dapat diubah dan disimpan — setiap simbol unik hanya ada satu kali dalam memori. Mereka ideal untuk kunci hash, nama metode, dan pengidentifikasi. Ruby juga memiliki objek`Symbol`yang digunakan secara luas dalam metaprogramming (`send`,`define_method`). Gunakan simbol untuk pengidentifikasi tetap; gunakan string saat Anda perlu memanipulasi konten.
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

### Q4: Bagaimana cara kerja metaprogramming Ruby, dan kapan saya harus menggunakannya?
**A:** Ruby mengizinkan kode untuk mendefinisikan kode saat runtime:`define_method`membuat metode secara dinamis,`method_missing`mencegat pemanggilan metode yang tidak ditentukan,`send`memanggil metode privat, dan`class_eval`/`instance_eval`mengevaluasi kode dalam konteks kelas/instance. Pemrograman meta sangat ampuh namun membuat kode lebih sulit dipahami — gunakanlah untuk DSL dan keajaiban kerangka kerja, bukan untuk logika sehari-hari.
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

### Q5: Apa cara terbaik untuk menangani kesalahan di Ruby?
**A:** Ruby menggunakan pengecualian untuk penanganan kesalahan. Tentukan kelas pengecualian khusus yang diwarisi dari`StandardError`(bukan`Exception`— yang menangkap kesalahan tingkat sistem). Gunakan`begin/rescue/else/ensure`untuk penanganan terstruktur. Ajukan pengecualian khusus, bukan`RuntimeError`umum. Gunakan`rescue`sebagai pengubah untuk satu kalimat sederhana.
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

## Pemecahan Masalah Rantai Pemikiran
### Masalah 1: Membangun DSL untuk File Konfigurasi
**Pernyataan Masalah:** Buat Ruby DSL yang memungkinkan penentuan konfigurasi server dalam sintaksis deklaratif yang mudah dibaca. DSL harus mendukung blok bersarang, validasi, dan serialisasi ke JSON.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) sintaks DSL yang bersih menggunakan blok dan pemanggilan metode, (2) pengumpulan data melalui`instance_eval`atau metode eksplisit, (3) validasi bidang yang diperlukan, (4) serialisasi JSON. Metaprogramming Ruby menjadikan DSL alami.
**Langkah 2 — Identifikasi Pendekatannya:**
- Gunakan`instance_eval`dengan kelas pembuat untuk menangkap panggilan DSL.
- Simpan konfigurasi dalam variabel instan.
- Validasi bidang yang diperlukan sebelum serialisasi.
- Gunakan`to_h`dan`JSON.generate`untuk keluaran.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- DSL dapat dibaca dan bersifat deklaratif — non-programmer dapat memahaminya.
- Validasi menangkap bidang wajib yang hilang pada waktu konstruksi.
-`instance_eval`menyediakan sintaks blok yang bersih tetapi membatasi`self`— untuk DSL yang lebih kompleks, gunakan`BasicObject`sebagai superkelas pembuatnya.
- Produksi: pertimbangkan permata`dry-configurable`atau`configurate`untuk DSL konfigurasi tingkat produksi.
### Masalah 2: Menerapkan Perpustakaan Memoisasi
**Pernyataan Masalah:** Buat modul memoisasi yang dapat digabungkan ke dalam kelas mana pun untuk menyimpan hasil metode dalam cache. Mendukung TTL (time-to-live), batas ukuran cache, dan kunci cache khusus.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) modul yang menambahkan metode kelas `memoize`, (2) metode yang membungkus metode target dengan logika caching, (3) dukungan untuk kedaluwarsa TTL, (4) penggusuran LRU ketika cache penuh.`Module#prepend`dan`define_method`Ruby ideal untuk ini.
**Langkah 2 — Identifikasi Pendekatannya:**
- Gunakan`Module.new`dengan`define_method`untuk membuat pembungkus.
- Simpan cache dalam hash dengan stempel waktu untuk TTL.
- Gunakan`prepend`untuk menyisipkan lapisan caching sebelum metode aslinya.
- Mendukung opsi yang dapat dikonfigurasi: `ttl`, `max_size`, `key`.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Keamanan thread:`Mutex`melindungi pembacaan/penulisan cache; komputasi terjadi di luar kunci.
- TTL: entri yang kedaluwarsa dibersihkan dengan malas saat diakses.
- Penggusuran LRU: ketika cache melebihi`max_size`, entri terlama (berdasarkan stempel waktu) akan dihapus.
- Kunci khusus: lambda`key`memungkinkan kontrol menyeluruh atas identitas cache.
- Produksi: gunakan permata`memoist`untuk kasus sederhana, atau memoisasi yang didukung Redis untuk cache terdistribusi.
---

## Ringkasan
Ruby adalah bahasa yang mengutamakan kebahagiaan dan ekspresi pengembang. Sintaksnya termasuk bahasa yang paling mudah dibaca, dan Ruby on Rails tetap menjadi salah satu kerangka web paling produktif yang pernah dibuat. Meskipun popularitas Ruby telah menurun dibandingkan dengan Python dan JavaScript, Ruby tetap menjadi bahasa yang kuat dan menyenangkan untuk pengembangan web, pembuatan skrip, dan otomatisasi. Jika Anda menghargai kode yang elegan dan perkembangan yang cepat, Ruby layak untuk dipelajari.