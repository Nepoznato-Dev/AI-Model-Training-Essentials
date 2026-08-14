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

# rubí
Ruby es un lenguaje de programación dinámico, interpretado y orientado a objetos creado por Yukihiro "Matz" Matsumoto y lanzado por primera vez en 1995 en Japón. Ruby fue diseñado centrándose en la felicidad del programador: su sintaxis es elegante y natural, y se lee casi como en inglés. Todo en Ruby es un objeto, incluidos los tipos primitivos como números enteros y booleanos. Ruby es mejor conocido por el marco web Ruby on Rails, que revolucionó el desarrollo web al popularizar las convenciones sobre la configuración y la creación rápida de prototipos.
Más allá de Rails, Ruby se utiliza para secuencias de comandos, automatización, herramientas DevOps (Chef, Puppet) y como lenguaje de propósito general. Su sintaxis expresiva y sus poderosas capacidades de metaprogramación hacen que escribir sea un placer.
---

## Por qué es importante Ruby
- **Felicidad del desarrollador**: Ruby está diseñado para ser legible y divertido. "Ruby está diseñado para hacer felices a los programadores" — Matz.
- **Sintaxis expresiva**: el código se lee como en inglés. Puntuación mínima, fraseo natural.
- **Ruby on Rails**: Uno de los frameworks web más productivos jamás creados. Impulsa GitHub, Shopify, Basecamp, GitLab.
- **Metaprogramación**: Ruby puede modificarse a sí mismo en tiempo de ejecución: definir métodos dinámicamente, crear lenguajes específicos de dominio (DSL).
- **Patrón de bloque/iterador**: los bloques e iteradores de Ruby hacen que el procesamiento de colecciones sea elegante.
- **Todo es un objeto**:`3.times { puts "hello" }`— los números enteros tienen métodos.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Rendimiento** | Más lento que los lenguajes compilados; La resonancia magnética tiene un GIL | Utilice JRuby para paralelismo; descargar a extensiones C |
| **Popularidad en declive** | Menos adopción nueva en comparación con Python, Go, Rust | Todavía se utiliza ampliamente; fuerte en startups y consultoría web |
| **Escribiendo** | La escritura dinámica puede provocar errores de tiempo de ejecución | Utilice Sorbet o RBS para escritura estática opcional |
| **Uso de memoria** | Mayor consumo de memoria que Go o Rust | Aceptable para la mayoría de las aplicaciones web |
| **Mercado laboral** | Menos posiciones nuevas que Python o JavaScript | Fuerte en nichos específicos (Tiendas de rieles, consultoría) |
---

## Fundamentos de sintaxis
### Variables y tipos
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

### Métodos y bloques
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

### Clases y Módulos
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

### Metaprogramación
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

## Rubí sobre rieles
Rails es un marco web completo que sigue la arquitectura MVC (Modelo-Vista-Controlador) y enfatiza:
- **Convención sobre configuración**: valores predeterminados razonables: no es necesario configurar todo.
- **No te repitas (SECO)**: utiliza generadores, migraciones y convenciones para minimizar la repetición.
- **Registro activo**: los objetos de la base de datos son objetos Ruby. `User.find(1)`recupera un usuario.
- **Migraciones**: los cambios en el esquema de la base de datos son código Ruby versionado.
Rails impulsa GitHub, Shopify, Stripe (temprano), Basecamp, GitLab y muchas empresas emergentes.
---

## Sintaxis y patrones avanzados
### Escritura de pato y envío dinámico
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

### Procesos, Lambdas y cierres
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

### Coincidencia de patrones (Ruby 3.0+)
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

### Sobrecarga del operador
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

## Concurrencia y paralelismo
### Temas
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

### Fibras: corrutinas ligeras
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

### Asíncrono/Espera con gema asíncrona
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

## Configuración del proyecto y sistema de construcción
### Estructura del proyecto (rieles)
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

### Gemfile — Gestión de dependencias
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

### Comandos de dependencia
```bash
bundle install          # Install all gems
bundle update           # Update gems
bundle add stripe       # Add a new gem
bundle remove stripe    # Remove a gem
bundle audit check --update  # Security audit
bundle outdated         # List outdated gems
```

### Canalización de CI/CD (acciones de GitHub)
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

## Pruebas
### RSpec — Marco de pruebas
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

### Burlarse y aplastar
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

### Comandos de prueba
```bash
bundle exec rspec                    # Run all tests
bundle exec rspec spec/models/       # Run model tests
bundle exec rspec spec/models/user_spec.rb:15  # Run specific test
bundle exec rspec --tag ~slow        # Skip slow tests
bundle exec rspec --format documentation  # Verbose output
```
---

## Interoperabilidad
### Extensiones C
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

### FFI: interfaz de función externa
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

### JRuby — Interoperabilidad JVM
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

## Patrones de diseño
### Patrón de observador
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

### Patrón de fábrica
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

### Patrón decorador
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

## Rendimiento y optimización
### Herramientas de creación de perfiles
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

### Técnicas de optimización
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

## Implementación
### Servidor web Puma
```ruby
# config/puma.rb
workers ENV.fetch("WEB_CONCURRENCY", 4).to_i
threads_count = ENV.fetch("RAILS_MAX_THREADS", 5).to_i
threads threads_count, threads_count

port ENV.fetch("PORT", 3000)
environment ENV.fetch("RACK_ENV", "development")
preload_app!
```

### Implementación de Docker
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

### Implementación de plataforma
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

## Cuándo usar Ruby
| Escenario | ¿Por qué Rubí? Mejor alternativa |
|----------|---------|-------------------|
| Aplicaciones web (Raíles) | Desarrollo rápido, marco productivo | Django (Python), Laravel (PHP), Next.js |
| Creación de prototipos | Muy rápido para escribir e iterar | Python, JavaScript |
| Scripting y automatización | Sintaxis elegante, potente procesamiento de textos | Pitón, concha |
| Herramientas DevOps (Chef, Puppet) | Ecosistema establecido | Vamos, Pitón |
| Herramientas CLI | Posible pero no ideal | Vamos, óxido |
| Sistemas críticos para el rendimiento | Demasiado lento | C, C++, óxido, listo |
| Ciencia de datos / ML | No el ecosistema | Pitón, R |
| Aplicaciones móviles | No adecuado | Rápido, Kotlin, Flutter |
---

## Preguntas y respuestas sintéticas
### P1: ¿Cuál es la diferencia entre `proc`,`lambda`y`block`en Ruby?
**R:** Los tres son cierres, pero difieren en su comportamiento. Un`block`es un fragmento de código anónimo pasado a un método con`do...end`o `{}`. Un`proc`es un bloque guardado como un objeto; no verifica el recuento de argumentos y`return`sale del método adjunto. Un`lambda`es como un proceso pero verifica el recuento de argumentos y`return`sale solo de lambda. Utilice bloques para devoluciones de llamadas únicas, procesos para fragmentos reutilizables y lambdas cuando necesite un comportamiento similar a un método.
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

### P2: ¿Cómo funcionan Ruby Gems y Bundler?
**R:** Las gemas son el sistema de paquetes de Ruby: bibliotecas reutilizables distribuidas a través de RubyGems.org. Un`Gemfile`declara dependencias; `bundle install`resuelve versiones y crea un`Gemfile.lock`para mayor reproducibilidad. `bundle exec`ejecuta comandos en el contexto de la gema. Utilice`gem 'name', '~> 2.0'`para restricciones de versión compatible. Confirme siempre`Gemfile.lock`para aplicaciones, pero no para bibliotecas.
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

### P3: ¿Cuáles son los tipos de símbolos de Ruby y por qué son importantes?
**R:** Los símbolos (`:name`) son cadenas internas inmutables: cada símbolo único existe solo una vez en la memoria. Son ideales para claves hash, nombres de métodos e identificadores. Ruby también tiene objetos`Symbol`que se utilizan ampliamente en metaprogramación (`send`, `define_method`). Utilice símbolos para identificadores fijos; Utilice cadenas cuando necesite manipular contenido.
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

### P4: ¿Cómo funciona la metaprogramación de Ruby y cuándo debo usarla?
**R:** Ruby permite que el código defina el código en tiempo de ejecución:`define_method`crea métodos dinámicamente,`method_missing`intercepta llamadas a métodos no definidos,`send`llama a métodos privados y`class_eval`/`instance_eval`evalúa el código en un contexto de clase/instancia. La metaprogramación es poderosa pero hace que el código sea más difícil de entender; úsela para DSL y marcos mágicos, no para la lógica cotidiana.
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

### P5: ¿Cuál es la mejor manera de manejar errores en Ruby?
**R:** Ruby usa excepciones para el manejo de errores. Defina clases de excepción personalizadas que hereden de`StandardError`(no `Exception`, que detecta errores a nivel del sistema). Utilice`begin/rescue/else/ensure`para un manejo estructurado. Plantea excepciones específicas, no genéricas `RuntimeError`. Utilice`rescue`como modificador para frases sencillas.
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

## Resolución de problemas mediante cadena de pensamiento
### Problema 1: crear un DSL para archivos de configuración
**Declaración del problema:** Cree un DSL Ruby que permita definir configuraciones de servidor en una sintaxis declarativa legible. El DSL debe admitir bloques anidados, validación y serialización a JSON.
**Paso 1: comprenda el problema:**
Necesitamos: (1) una sintaxis DSL limpia utilizando bloques y llamadas a métodos, (2) recopilación de datos mediante`instance_eval`o métodos explícitos, (3) validación de campos obligatorios, (4) serialización JSON. La metaprogramación de Ruby hace que los DSL sean naturales.
**Paso 2: Identifique el enfoque:**
- Utilice`instance_eval`con una clase de constructor para capturar llamadas DSL.
- Almacenar la configuración en variables de instancia.
- Validar los campos obligatorios antes de la serialización.
- Utilice`to_h`y`JSON.generate`para la salida.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- El DSL es legible y declarativo; los no programadores pueden entenderlo.
- La validación detecta los campos obligatorios que faltan en el momento de la construcción.
-`instance_eval`proporciona una sintaxis de bloque limpia pero limita `self`; para DSL más complejos, utilice`BasicObject`como superclase del constructor.
- Producción: considere las gemas`dry-configurable`o`configurate`para DSL de configuración de nivel de producción.
### Problema 2: implementar una biblioteca de memorización
**Declaración del problema:** Cree un módulo de memorización que pueda mezclarse con cualquier clase para almacenar en caché los resultados de los métodos. Admite TTL (tiempo de vida), límites de tamaño de caché y claves de caché personalizadas.
**Paso 1: comprenda el problema:**
Necesitamos: (1) un módulo que agregue un método de clase `memoize`, (2) el método envuelve los métodos de destino con lógica de almacenamiento en caché, (3) soporte para la caducidad de TTL, (4) desalojo de LRU cuando el caché está lleno.`Module#prepend`y`define_method`de Ruby son ideales para esto.
**Paso 2: Identifique el enfoque:**
- Utilice`Module.new`con`define_method`para crear un contenedor.
- Almacenar caché en un hash con marcas de tiempo para TTL.
- Utilice`prepend`para insertar la capa de almacenamiento en caché antes del método original.
- Admite opciones configurables: `ttl`, `max_size`, `key`.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- Seguridad de subprocesos:`Mutex`protege las lecturas/escrituras de caché; El cálculo ocurre fuera de la cerradura.
- TTL: las entradas caducadas se limpian lentamente al acceder.
- Desalojo de LRU: cuando el caché excede `max_size`, se elimina la entrada más antigua (por marca de tiempo).
- Claves personalizadas: la lambda`key`permite un control detallado sobre la identidad de la caché.
- Producción: utilice la gema`memoist`para casos sencillos o la memorización respaldada por Redis para el almacenamiento en caché distribuido.
---

## Resumen
Ruby es un lenguaje que prioriza la felicidad y expresividad del desarrollador. Su sintaxis se encuentra entre las más legibles de cualquier lenguaje y Ruby on Rails sigue siendo uno de los marcos web más productivos jamás creados. Si bien la popularidad de Ruby ha disminuido en relación con Python y JavaScript, sigue siendo un lenguaje potente y agradable para el desarrollo web, la creación de secuencias de comandos y la automatización. Si valora el código elegante y el desarrollo rápido, vale la pena aprender Ruby.