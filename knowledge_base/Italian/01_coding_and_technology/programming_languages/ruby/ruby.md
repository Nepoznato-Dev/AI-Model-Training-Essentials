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
#Rubino
Ruby è un linguaggio di programmazione dinamico, interpretato e orientato agli oggetti creato da Yukihiro "Matz" Matsumoto e pubblicato per la prima volta nel 1995 in Giappone. Ruby è stato progettato concentrandosi sulla felicità del programmatore: la sua sintassi è elegante e naturale, si legge quasi come l'inglese. Tutto in Ruby è un oggetto, compresi i tipi primitivi come numeri interi e booleani. Ruby è meglio conosciuto per il framework web Ruby on Rails, che ha rivoluzionato lo sviluppo web rendendo popolari le convenzioni sulla configurazione e la prototipazione rapida.
Oltre a Rails, Ruby viene utilizzato per scripting, automazione, strumenti DevOps (Chef, Puppet) e come linguaggio generico. La sua sintassi espressiva e le potenti capacità di metaprogrammazione lo rendono una gioia da scrivere.
---

## Perché Ruby è importante
- **Felicità degli sviluppatori**: Ruby è progettato per essere leggibile e divertente. "Ruby è progettato per rendere felici i programmatori" — Matz.
- **Sintassi espressiva**: il codice si legge come l'inglese. Punteggiatura minima, fraseggio naturale.
- **Ruby on Rails**: uno dei framework web più produttivi mai creati. Alimenta GitHub, Shopify, Basecamp, GitLab.
- **Metaprogrammazione**: Ruby può modificarsi in fase di esecuzione: definire metodi dinamicamente, creare linguaggi specifici del dominio (DSL).
- **Modello blocco/iteratore**: i blocchi e gli iteratori di Ruby rendono elegante l'elaborazione della raccolta.
- **Tutto è un oggetto**:`3.times { puts "hello" }`— gli interi hanno metodi.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Prestazioni** | Linguaggi più lenti dei linguaggi compilati; La risonanza magnetica ha un GIL | Usa JRuby per il parallelismo; scaricare nelle estensioni C |
| **Popolarità in calo** | Meno nuove adozioni rispetto a Python, Go, Rust | Ancora ampiamente utilizzato; forte nelle web startup e nella consulenza |
| **Digitando** | La digitazione dinamica può portare a errori di runtime | Utilizza Sorbet o RBS per la digitazione statica opzionale |
| **Utilizzo della memoria** | Ingombro di memoria maggiore rispetto a Go o Rust | Accettabile per la maggior parte delle applicazioni web |
| **Mercato del lavoro** | Meno nuove posizioni rispetto a Python o JavaScript | Forte in nicchie specifiche (negozi di rotaie, consulenza) |
---

## Fondamenti di sintassi
### Variabili e tipi
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

### Metodi e blocchi
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

### Classi e moduli
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

### Metaprogrammazione
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

## Rubino sui binari
Rails è un framework web full-stack che segue l'architettura MVC (Model-View-Controller) ed enfatizza:
- **Convenzione sulla configurazione**: impostazioni predefinite ragionevoli: non è necessario configurare tutto.
- **Non ripeterti (DRY)**: utilizza generatori, migrazioni e convenzioni per ridurre al minimo la ripetizione.
- **Record attivo**: gli oggetti del database sono oggetti Ruby. `User.find(1)`recupera un utente.
- **Migrazioni**: le modifiche allo schema del database sono codice Ruby con versione.
Rails alimenta GitHub, Shopify, Stripe (inizio), Basecamp, GitLab e molte startup.
---

## Sintassi e modelli avanzati
### Duck Typing e Dynamic Dispatch
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

### Proc, Lambda e chiusure
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

### Corrispondenza modello (Ruby 3.0+)
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

### Sovraccarico operatore
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

## Concorrenza e parallelismo
### Discussioni
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

### Fibre: coroutine leggere
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

### Asincrona/Aspetta con Gemma asincrona
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

## Configurazione del progetto e sistema di creazione
### Struttura del progetto (Binari)
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

### Gemfile: gestione delle dipendenze
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

### Comandi di dipendenza
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### Pipeline CI/CD (azioni GitHub)
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

## Test
### RSpec: struttura di test
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

### Derisioni e sciocchezze
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

### Comandi di prova
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## Interoperabilità
### Estensioni C
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

### FFI: interfaccia per funzioni estere
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

### JRuby: interoperabilità JVM
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

## Modelli di progettazione
### Modello dell'osservatore
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

### Modello di fabbrica
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

### Motivo decorativo
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

## Prestazioni e ottimizzazione
### Strumenti di profilazione
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

### Tecniche di ottimizzazione
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

## Distribuzione
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

### Distribuzione Docker
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

### Distribuzione della piattaforma
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

## Quando usare Ruby
| Scenario | Perché Ruby | Alternativa migliore |
|----------|---------|-------------|
| Applicazioni Web (Binari) | Sviluppo rapido, quadro produttivo | Django (Python), Laravel (PHP), Next.js |
| Prototipazione | Molto veloce da scrivere e iterare | Python, JavaScript |
| Scripting e automazione | Sintassi elegante, potente elaborazione del testo | Pitone, Shell |
| Strumenti DevOps (Chef, Puppet) | Ecosistema consolidato | Vai, Pitone |
| Strumenti CLI | Possibile ma non ideale | Vai, Ruggine |
| Sistemi critici per le prestazioni | Troppo lento | C, C++, Ruggine, Go |
| Scienza dei dati/ML | Non l'ecosistema | Pitone, R |
| App mobili | Non adatto | Swift, Kotlin, Flutter |
---

## Domande e risposte sintetiche
### D1: Qual è la differenza tra`proc`,`lambda`e`block`in Ruby?
**R:** Tutte e tre sono chiusure, ma differiscono nel comportamento. Un`block`è una porzione anonima di codice passata a un metodo con`do...end`o`{}`. Un`proc`è un blocco salvato come oggetto: non controlla il conteggio degli argomenti e`return`esce dal metodo di inclusione. Un`lambda`è come un proc ma controlla il conteggio degli argomenti e`return`esce solo dal lambda. Utilizza i blocchi per callback una tantum, procedure per snippet riutilizzabili e lambda quando hai bisogno di un comportamento simile a un metodo.
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

### D2: Come funzionano le gemme Ruby e il Bundler?
**R:** Le gemme sono il sistema di pacchetti di Ruby: librerie riutilizzabili distribuite tramite RubyGems.org. Un`Gemfile`dichiara le dipendenze; `bundle install`risolve le versioni e crea un`Gemfile.lock`per la riproducibilità. `bundle exec`esegue comandi nel contesto gem. Utilizzare`gem 'name', '~> 2.0'`per i vincoli della versione compatibile. Commetti sempre`Gemfile.lock`per le applicazioni, ma non per le librerie.
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

### D3: Quali sono i tipi di simboli di Ruby e perché sono importanti?
**R:** I simboli (`:name`) sono stringhe immutabili e interne: ogni simbolo univoco esiste solo una volta in memoria. Sono ideali per chiavi hash, nomi di metodi e identificatori. Ruby ha anche oggetti`Symbol`ampiamente utilizzati nella metaprogrammazione (`send`,`define_method`). Utilizzare simboli per identificatori fissi; usa le stringhe quando devi manipolare il contenuto.
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

### D4: Come funziona la metaprogrammazione di Ruby e quando dovrei usarla?
**R:** Ruby consente al codice di definire il codice in fase di runtime:`define_method`crea metodi dinamicamente,`method_missing`intercetta chiamate di metodi non definiti,`send`chiama metodi privati ​​e`class_eval`/`instance_eval`valutano il codice in un contesto di classe/istanza. La metaprogrammazione è potente ma rende il codice più difficile da comprendere: usatela per i DSL e la magia dei framework, non per la logica quotidiana.
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

### Q5: Qual è il modo migliore per gestire gli errori in Ruby?
**R:** Ruby utilizza le eccezioni per la gestione degli errori. Definisci classi di eccezioni personalizzate che ereditano da`StandardError`(non `Exception`, che rileva errori a livello di sistema). Utilizzare`begin/rescue/else/ensure`per la gestione strutturata. Solleva eccezioni specifiche, non generiche`RuntimeError`. Usa`rescue`come modificatore per semplici battute di una riga.
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

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: creare un DSL per i file di configurazione
**Dichiarazione del problema:** Creare un Ruby DSL che consenta di definire le configurazioni del server in una sintassi leggibile e dichiarativa. Il DSL dovrebbe supportare blocchi annidati, convalida e serializzazione su JSON.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) una sintassi DSL pulita utilizzando blocchi e chiamate di metodi, (2) raccolta dati tramite`instance_eval`o metodi espliciti, (3) convalida dei campi richiesti, (4) serializzazione JSON. La metaprogrammazione di Ruby rende i DSL naturali.
**Passaggio 2: identificare l'approccio:**
- Utilizza`instance_eval`con una classe builder per acquisire chiamate DSL.
- Memorizza la configurazione nelle variabili di istanza.
- Convalidare i campi obbligatori prima della serializzazione.
- Utilizzare`to_h`e`JSON.generate`per l'output.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Il DSL è leggibile e dichiarativo: i non programmatori possono capirlo.
- La convalida rileva i campi obbligatori mancanti al momento della costruzione.
-`instance_eval`fornisce la sintassi del blocco pulita ma limita `self`: per DSL più complessi, utilizza`BasicObject`come superclasse del costruttore.
- Produzione: considera i gem`dry-configurable`o`configurate`per DSL di configurazione di livello produttivo.
### Problema 2: implementare una libreria di memoizzazione
**Dichiarazione del problema:** Crea un modulo di memorizzazione che può essere combinato in qualsiasi classe per memorizzare nella cache i risultati del metodo. Supporta TTL (time-to-live), limiti di dimensione della cache e chiavi di cache personalizzate.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) un modulo che aggiunga un metodo di classe `memoize`, (2) il metodo racchiude i metodi di destinazione con la logica di memorizzazione nella cache, (3) supporto per la scadenza TTL, (4) eliminazione LRU quando la cache è piena.`Module#prepend`e`define_method`di Ruby sono ideali per questo.
**Passaggio 2: identificare l'approccio:**
- Utilizza`Module.new`con`define_method`per creare un wrapper.
- Memorizza la cache in un hash con timestamp per TTL.
- Utilizzare`prepend`per inserire il livello di memorizzazione nella cache prima del metodo originale.
- Supporta opzioni configurabili: `ttl`, `max_size`, `key`.
**Passaggio 3: implementa la soluzione:**
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

**Passaggio 4: verifica e ottimizzazione:**
- Sicurezza del thread:`Mutex`protegge le letture/scritture della cache; il calcolo avviene fuori dalla serratura.
- TTL: le voci scadute vengono ripulite pigramente all'accesso.
- Eliminazione LRU: quando la cache supera `max_size`, la voce più vecchia (per timestamp) viene rimossa.
- Chiavi personalizzate: la lambda`key`consente un controllo approfondito sull'identità della cache.
- Produzione: utilizza il gem`memoist`per casi semplici o la memorizzazione supportata da Redis per il caching distribuito.
---

## Riepilogo
Ruby è un linguaggio che dà priorità alla felicità e all'espressività degli sviluppatori. La sua sintassi è tra le più leggibili di qualsiasi linguaggio e Ruby on Rails rimane uno dei framework web più produttivi mai creati. Sebbene la popolarità di Ruby sia diminuita rispetto a Python e JavaScript, rimane un linguaggio potente e divertente per lo sviluppo web, lo scripting e l'automazione. Se apprezzi il codice elegante e lo sviluppo rapido, vale la pena imparare Ruby.