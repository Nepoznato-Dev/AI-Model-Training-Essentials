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

# Rubis
Ruby est un langage de programmation dynamique, interprété et orienté objet créé par Yukihiro "Matz" Matsumoto et lancé pour la première fois en 1995 au Japon. Ruby a été conçu en mettant l'accent sur le bonheur des programmeurs : sa syntaxe est élégante et naturelle, se lisant presque comme l'anglais. Tout dans Ruby est un objet, y compris les types primitifs comme les entiers et les booléens. Ruby est surtout connu pour le framework Web Ruby on Rails, qui a révolutionné le développement Web en vulgarisant les conventions de configuration et de prototypage rapide.
Au-delà de Rails, Ruby est utilisé pour les scripts, l'automatisation, les outils DevOps (Chef, Puppet) et comme langage à usage général. Sa syntaxe expressive et ses puissantes capacités de métaprogrammation en font un plaisir à écrire.
---

## Pourquoi Ruby est important
- **Bonheur des développeurs** : Ruby est conçu pour être lisible et agréable. "Ruby est conçu pour rendre les programmeurs heureux" — Matz.
- **Syntaxe expressive** : le code se lit comme l'anglais. Ponctuation minimale, phrasé naturel.
- **Ruby on Rails** : l'un des frameworks Web les plus productifs jamais créés. Alimente GitHub, Shopify, Basecamp, GitLab.
- **Métaprogrammation** : Ruby peut se modifier au moment de l'exécution : définir des méthodes de manière dynamique, créer des langages spécifiques à un domaine (DSL).
- **Modèle de bloc/itérateur** : les blocs et les itérateurs de Ruby rendent le traitement des collections élégant.
- **Tout est un objet** :`3.times { puts "hello" }`— les entiers ont des méthodes.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Performances** | Plus lent que les langages compilés ; L'IRM a un GIL | Utilisez JRuby pour le parallélisme ; décharger vers les extensions C |
| **Popularité en baisse** | Moins de nouvelles adoptions par rapport à Python, Go, Rust | Encore largement utilisé ; fort dans les startups web et le conseil |
| **Saisie** | La saisie dynamique peut entraîner des erreurs d'exécution | Utilisez Sorbet ou RBS pour le typage statique facultatif |
| **Utilisation de la mémoire** | Empreinte mémoire plus élevée que Go ou Rust | Acceptable pour la plupart des applications Web |
| **Marché du travail** | Moins de nouveaux postes que Python ou JavaScript | Fort dans des niches spécifiques (magasins Rails, conseil) |
---

## Fondamentaux de la syntaxe
### Variables et types
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

### Méthodes et blocs
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

### Cours et modules
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

### Métaprogrammation
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

## Ruby sur Rails
Rails est un framework Web full-stack qui suit l'architecture MVC (Model-View-Controller) et met l'accent sur :
- **Convention sur la configuration** : valeurs par défaut raisonnables – pas besoin de tout configurer.
- **Ne vous répétez pas (DRY)** : utilisez des générateurs, des migrations et des conventions pour minimiser les répétitions.
- **Active Record** : les objets de base de données sont des objets Ruby. `User.find(1)`récupère un utilisateur.
- **Migrations** : les modifications du schéma de base de données sont du code Ruby versionné.
Rails alimente GitHub, Shopify, Stripe (au début), Basecamp, GitLab et de nombreuses startups.
---

## Syntaxe et modèles avancés
### Saisie de canard et répartition dynamique
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

### Procs, Lambdas et fermetures
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

### Correspondance de modèles (Ruby 3.0+)
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

### Surcharge des opérateurs
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

## Concurrence et parallélisme
### Sujets
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

### Fibres — Coroutines légères
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

### Async/Await avec Async Gem
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

## Configuration du projet et système de construction
### Structure du projet (Rails)
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

### Gemfile — Gestion des dépendances
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

### Commandes de dépendance
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### Pipeline CI/CD (actions GitHub)
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

## Tests
### RSpec — Cadre de test
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

### Moquerie et stubbing
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

### Tester les commandes
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## Interopérabilité
### Extensions C
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

### FFI — Interface de fonction étrangère
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

### JRuby — Interopérabilité JVM
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

## Modèles de conception
### Modèle d'observateur
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

### Modèle d'usine
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

### Modèle de décorateur
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

## Performances et optimisation
### Outils de profilage
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

### Techniques d'optimisation
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

## Déploiement
### Serveur Web Puma
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### Déploiement de Docker
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

### Déploiement de la plateforme
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

## Quand utiliser Ruby
| Scénario | Pourquoi Ruby | Meilleure alternative |
|--------------|---------|-------------------|
| Applications Web (Rails) | Développement rapide, cadre productif | Django (Python), Laravel (PHP), Next.js |
| Prototypage | Très rapide à écrire et à itérer | Python, JavaScript |
| Scripts et automatisation | Syntaxe élégante, traitement de texte puissant | Python, Coquille |
| Outils DevOps (Chef, Puppet) | Écosystème établi | Allez, Python |
| Outils CLI | Possible mais pas idéal | Allez, Rouille |
| Systèmes critiques en termes de performances | Trop lent | C, C++, Rust, Go |
| Science des données / ML | Pas l'écosystème | Python, R |
| Applications mobiles | Ne convient pas | Swift, Kotlin, Flutter |
---

## Questions et réponses synthétiques
### Q1 : Quelle est la différence entre`proc`,`lambda`et`block`dans Ruby ?
**R :** Ces trois fermetures sont des fermetures, mais leur comportement diffère. Un`block`est un morceau de code anonyme transmis à une méthode avec`do...end`ou`{}`. Un`proc`est un bloc enregistré en tant qu'objet — il ne vérifie pas le nombre d'arguments et`return`quitte la méthode englobante. Un`lambda`est comme un proc mais vérifie le nombre d'arguments et`return`ne quitte que le lambda. Utilisez des blocs pour les rappels ponctuels, des procédures pour les extraits de code réutilisables et des lambdas lorsque vous avez besoin d'un comportement de type méthode.
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

### Q2 : Comment fonctionnent les gemmes Ruby et Bundler ?
**R :** Les gemmes sont le système de packages de Ruby : des bibliothèques réutilisables distribuées via RubyGems.org. Un`Gemfile`déclare les dépendances ; `bundle install`résout les versions et crée un`Gemfile.lock`pour la reproductibilité. `bundle exec`exécute des commandes dans le contexte gem. Utilisez`gem 'name', '~> 2.0'`pour les contraintes de version compatibles. Validez toujours`Gemfile.lock`pour les applications, mais pas pour les bibliothèques.
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

### Q3 : Quels sont les types de symboles de Ruby et pourquoi sont-ils importants ?
**A :** Les symboles (`:name`) sont des chaînes immuables et internes : chaque symbole unique n'existe qu'une seule fois en mémoire. Ils sont idéaux pour les clés de hachage, les noms de méthodes et les identifiants. Ruby possède également des objets`Symbol`largement utilisés en métaprogrammation (`send`,`define_method`). Utiliser des symboles pour les identifiants fixes ; utilisez des chaînes lorsque vous devez manipuler du contenu.
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

### Q4 : Comment fonctionne la métaprogrammation de Ruby et quand dois-je l'utiliser ?
**R :** Ruby permet au code de définir du code au moment de l'exécution :`define_method`crée des méthodes de manière dynamique,`method_missing`intercepte les appels de méthode non définis,`send`appelle des méthodes privées et`class_eval`/`instance_eval`évalue le code dans un contexte de classe/instance. La métaprogrammation est puissante mais rend le code plus difficile à comprendre : utilisez-la pour les DSL et la magie des frameworks, pas pour la logique quotidienne.
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

### Q5 : Quelle est la meilleure façon de gérer les erreurs dans Ruby ?
**R :** Ruby utilise des exceptions pour la gestion des erreurs. Définissez des classes d'exception personnalisées héritant de`StandardError`(et non de`Exception`- qui détecte les erreurs au niveau du système). Utilisez`begin/rescue/else/ensure`pour une manipulation structurée. Déclenchez des exceptions spécifiques, et non génériques`RuntimeError`. Utilisez`rescue`comme modificateur pour les simples one-liners.
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

## Résolution de problèmes en chaîne de pensée
### Problème 1 : Créer un DSL pour les fichiers de configuration
**Énoncé du problème :** Créez un Ruby DSL qui permet de définir les configurations de serveur dans une syntaxe déclarative lisible. Le DSL doit prendre en charge les blocs imbriqués, la validation et la sérialisation vers JSON.
**Étape 1 — Comprendre le problème :**
Nous avons besoin de : (1) une syntaxe DSL propre utilisant des blocs et des appels de méthodes, (2) la collecte de données via`instance_eval`ou des méthodes explicites, (3) la validation des champs obligatoires, (4) la sérialisation JSON. La métaprogrammation de Ruby rend les DSL naturels.
**Étape 2 — Identifiez l'approche :**
- Utilisez`instance_eval`avec une classe de constructeur pour capturer les appels DSL.
- Stocker la configuration dans des variables d'instance.
- Validez les champs obligatoires avant la sérialisation.
- Utilisez`to_h`et`JSON.generate`pour la sortie.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Le DSL est lisible et déclaratif — les non-programmeurs peuvent le comprendre.
- La validation détecte les champs obligatoires manquants au moment de la construction.
-`instance_eval`fournit la syntaxe de bloc propre mais limite`self`— pour les DSL plus complexes, utilisez`BasicObject`comme superclasse du constructeur.
- Production : envisagez les gems`dry-configurable`ou`configurate`pour les DSL de configuration de niveau production.
### Problème 2 : Implémenter une bibliothèque de mémorisation
**Énoncé du problème :** Créez un module de mémorisation qui peut être mélangé à n'importe quelle classe pour mettre en cache les résultats des méthodes. Prise en charge du TTL (durée de vie), des limites de taille du cache et des clés de cache personnalisées.
**Étape 1 — Comprendre le problème :**
Nous avons besoin de : (1) un module qui ajoute une méthode de classe `memoize`, (2) la méthode encapsule les méthodes cibles avec une logique de mise en cache, (3) la prise en charge de l'expiration TTL, (4) l'expulsion de LRU lorsque le cache est plein. Les`Module#prepend`et`define_method`de Ruby sont idéaux pour cela.
**Étape 2 — Identifiez l'approche :**
- Utilisez`Module.new`avec`define_method`pour créer un wrapper.
- Stockez le cache dans un hachage avec des horodatages pour TTL.
- Utilisez`prepend`pour insérer la couche de mise en cache avant la méthode d'origine.
- Prise en charge des options configurables :`ttl`,`max_size`,`key`.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Sécurité des threads :`Mutex`protège les lectures/écritures du cache ; le calcul s'effectue en dehors du verrou.
- TTL : les entrées expirées sont nettoyées paresseusement à l'accès.
- Expulsion LRU : lorsque le cache dépasse`max_size`, l'entrée la plus ancienne (par horodatage) est supprimée.
- Clés personnalisées : le lambda`key`permet un contrôle précis de l'identité du cache.
- Production : utilisez la gem`memoist`pour les cas simples, ou la mémorisation basée sur Redis pour la mise en cache distribuée.
---

## Résumé
Ruby est un langage qui donne la priorité au bonheur et à l'expressivité des développeurs. Sa syntaxe est parmi les plus lisibles de tous les langages, et Ruby on Rails reste l'un des frameworks Web les plus productifs jamais créés. Bien que la popularité de Ruby ait diminué par rapport à Python et JavaScript, il reste un langage puissant et agréable pour le développement Web, les scripts et l'automatisation. Si vous appréciez un code élégant et un développement rapide, Ruby vaut la peine d'être appris.